# Incremental Data Reader

An `Incremental Data Reader` allows for the ability to run data readers that update incrementally rather than populate the full set of data, provided the data source (API or database) provides some pointer/date that makes it possible to track that information. Incremental data readers are based on checkpoints. A checkpoint could be a date time such as the last time the data reader ran, therefore each invocation would get a record set of any changed records using the timestamp as the checkpoint.

## When to use an Incremental Data Reader

We recommend a full data reader by default in order to support change detection. You should have a specific reason to implement an incremental data reader, such as when it is impractical to read the entire data set, and take care to consider how deletes will be handled. 

## How the Checkpoint Works

On first run the checkpoint value in the configuration for the data reader will be `null`. When a data reader completes successfully the configuration will persist with the value returned by `GetCheckpoint()` on the data reader. If no override implementation of `GetCheckpoint()` exists on the data reader then the value persisted will be a UTC datetime of when the data reader started. 

> 

Note: Incremental data readers do not support change detection. This is because incremental readers operate using checkpoints, which means each run only processes records that have changed since the last checkpoint, rather than the entire dataset. As a result, the reader may not have access to all records needed to reliably detect changes, such as modifications or deletions that occurred before the current checkpoint. For this reason, reliable change detection is not possible with incremental data readers.

## Creating an Incremental Data Reader

When creating a data object via the CLI you can set the reader type like so:

```
xchange data-object new --module-id app-1 --name Example --reader-type incremental

```

The data reader you create for incremental updates will share much of its structure and logic with a full data reader, such as how it connects to the data source and maps records to your data objects, however, the key difference is the addition of checkpoint logic. For example if you have an API that lets you pass in a cursor that will then return a record set of all the changes based on that cursor you could implement the data read as follows:

**App/v1/Example/ExampleDataReader.cs**

```
public class ExampleObjectDataReader : IncrementalDataReaderBase<ExampleObjectDataReader>
{
    private readonly ILogger<ExampleObjectDataReader> _logger;
    private readonly IHostContext _hostContext;
    private readonly IApiClient _apiClient;
    private readonly IncrementalCacheWriterConfig _config;
    private string? _checkpoint;

    public ExampleObjectDataReader(
        ILogger<ExampleObjectDataReader> logger,
        IHostContext hostContext,
        IApiClient client,
        AppV1CacheWriterConfig config)
    {
        _logger = logger;
        _hostContext = hostContext;
        _apiClient = client;
        _config = config.ExampleObjectConfig;
    }

    public override string GetCheckpoint()
    {
        return _checkpoint;
    }

    public override async IAsyncEnumerable<IDataReaderObject<ExampleDataObject>> GetTypedDataAsync(
        DataObjectCacheWriteArguments? dataObjectRunArguments, 
        [EnumeratorCancellation] CancellationToken cancellationToken) 
    {
        var response = new ApiResponse<IEnumerable<ExampleDataObject?>>();
        try
        {
            response = await _apiClient.GetExamples(_config.Checkpoint, cancellationToken).ConfigureAwait(false);
        }
        catch (Exception exception)
        {
            _logger.LogError("API response: {Message}", exception.Message);
            throw;
        }

        if (response.Result != null && response.IsSuccessful)
        {
            foreach (var item in response.Result.Changes)
            {
                var resource = new ExampleDataObject()
                {
                    Age = item.Age,
                    Date = item.Date,
                    Name = item.Name,
                    Position = item.Position,
                    Id = item.Id,
                };
                yield return new DataReaderObject<ExampleDataObject>(resource, UpdateOperation.Upsert);
            }

            foreach (var item in response.Result.Deletes)
            {
                var resource = new ExampleDataObject()
                {
                    Age = item.Age,
                    Date = item.Date,
                    Name = item.Name,
                    Position = item.Position,
                    Id = item.Id,
                };
                yield return new DataReaderObject<ExampleDataObject>(resource, UpdateOperation.Delete);
            }
        }

        _checkpoint = response.Result.Cursor;
    }
}

```

The incremental data reader tracks a "checkpoint" value such as a timestamp, ID, or cursor representing the last successful read. On each run, the reader uses this checkpoint to request only records that have changed since the last run, rather than retrieving the entire dataset. After processing, the reader updates the checkpoint so that future runs continue from where the last one left off.

### Delete Handling in Upsert Operations

Since change detection is not supported in Incremental Data Readers, it is important to handle deletes explicitly to keep your cache accurate. Many APIs that support incremental updates will also provide a way to retrieve deleted records (for example, a Deletes collection in the response). If your data source supports this, you should yield delete operations in your data reader. You can use as reference the previous Incremental Data Reader code for an example [Creating an Incremental Data Reader](#creating-an-incremental-data-reader). 

## Convert a Full Data Reader to Incremental

In the case that you have a data object already created but want to convert it to be read incrementally then this will take you through each of the steps to do so.

The example code below is converting a data object named `Example` and the module named `App`

### Updating the Cache Writer Service Configuration

First we'll want to update the cache writer service's configuration to have the `ExampleObjectConfig` to be a different property type.

**App/v1/AppV1CacheWriterConfig.cs**

```
namespace Connector.App.v1;

[Title("App V1 Cache Writer Configuration")]
[Description("Configuration of the data object caches for the module.")]
public class AppV1CacheWriterConfig
{
    public HealthCheckConfig HealthCheckConfig { get; set; } = new();
    public IncrementalCacheWriterConfig ExampleObjectConfig { get; set; } = new();
}

```

### Updating the Cache Writer Service Definition

The cache writer service definition is used for registering all of the data readers for a module. In the case of an incremental data reader we want to use the `RegisterIncrementalDataReader` method instead of the generic `RegisterDataReader`

**App/v1/AppV1CacheWriterDefinition.cs**

```
public override void ConfigureService(ICacheWriterService service, AppV1CacheWriterConfig config)
{
    var dataReaderSettings = new DataReaderSettings
    {
        DisableDeletes = false,
        UseChangeDetection = false
    };
    service.RegisterDataReader<HealthCheckDataReader, HealthCheckDataObject>(ModuleId, config.HealthCheckConfig, dataReaderSettings);
    service.RegisterIncrementalDataReader<ExampleObjectDataReader, ExampleDataObject>(
        ModuleId, 
        config.TestWorkersConfig, 
        new DataReaderSettings 
        { 
            DisableDeletes = false, 
            UseChangeDetection = false
        });
}

```

### Updating the Data Reader

The data reader for the `Example` data object now needs to be updated to implement `IIncrementalDataReader`. The SDK comes with `IncrementalDataReaderBase` which can be used instead.

The checkpoints for this data reader will be a date time with UTC as the timezone. Each time there is a successful run the data reader the checkpoint will automatically be set to the start time (in UTC) of the data reader.

**App/v1/Example/ExampleDataReader.cs**

```
public class ExampleObjectDataReader : IncrementalDataReaderBase<ExampleObjectDataReader>
{
    private readonly ILogger<ExampleObjectDataReader> _logger;
    private readonly IHostContext _hostContext;
    private readonly IApiClient _apiClient;
    private readonly IncrementalCacheWriterConfig _config;

    public ExampleObjectDataReader(
        ILogger<ExampleObjectDataReader> logger,
        IHostContext hostContext,
        IApiClient client,
        AppV1CacheWriterConfig config)
    {
        _logger = logger;
        _hostContext = hostContext;
        _apiClient = client;
        _config = config.ExampleObjectConfig;
    }

    public override async IAsyncEnumerable<IDataReaderObject<ExampleDataObject>> GetTypedDataAsync(
        DataObjectCacheWriteArguments? dataObjectRunArguments, 
        [EnumeratorCancellation] CancellationToken cancellationToken) 
    {
        DateTime.TryParse(_config.Checkpoint, out var modifiedSinceDateTime);
        var response = new ApiResponse<IEnumerable<ExampleDataObject?>>();
        try
        {
            response = await _apiClient.GetExamples(modifiedSinceDateTime, cancellationToken).ConfigureAwait(false);
        }
        catch (Exception exception)
        {
            _logger.LogError("API response: {Message}", exception.Message);
            throw;
        }

        if (response.Result != null && response.IsSuccessful)
        {
            foreach (var item in response.Result)
            {
                var resource = new ExampleDataObject()
                {
                    Age = item.Age,
                    Date = item.Date,
                    Name = item.Name,
                    Position = item.Position,
                    Id = item.Id,
                };
                yield return new DataReaderObject<ExampleDataObject>(resource, UpdateOperation.Upsert);
            }
        }
    }
}

```

If you want to customize the checkpoint value, then your reader can implement its own `GetCheckpoint()` method. You can see an example of that in [Creating an Incremental Data Reader](#creating-an-incremental-data-reader)

### Updating the API Client

The API client needs to be updated to support using the query parameter on the target API for getting the partial record set. An Example of API Client that has been updated to include the `modifiedSinceDateTime` could look something like this

**Client/ApiClient.cs**

```
public async Task<ApiResponse<IEnumerable<ExampleObjectDataReader?>>> GetExamples(DateTime modifiedSinceDate, CancellationToken cancellationToken = default)
{
    var queryParameter = new Dictionary<string, string>
    {
        { "date", modifiedSinceDate.ToString("yyyy-MM-dd") },
    };
    var queryString = QueryString.Create(queryParameter).ToString();
    var response = await _httpClient
        .GetAsync("api/example" + queryString.ToString(), cancellationToken)
        .ConfigureAwait(false);

    return new ApiResponse<IEnumerable<ExampleDataObject?>>()
    {
        IsSuccessful = response.IsSuccessStatusCode,
        StatusCode = (int)response.StatusCode,
        Result = response.IsSuccessStatusCode ? await response.Content.LoadFromJsonAsync<Enumerable<ExampleDataObject>> : default,
        RawResult = response.IsSuccessStatusCode ? null : await response.Content.ReadAsStreamAsync(),
    };
}

```
January 14, 2026January 14, 2026
