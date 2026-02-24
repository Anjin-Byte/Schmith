# Reading Data

This guide will tell you how to define a data object, read from a target system, and write that data to the cache. 

For context:

1. A data object is the defining unit of data storage and transfer on App Xchange
1. You will need to reference the [Object Schema Guide](../object-schema/) to correctly define the data object 
1. The `ObjectDataReader.cs` is enabling a [cache writer service](https://help.trimble.com/en/app-xchange/app-xchange/jobs/services) on platform - from the connector code perspective you are trying to read the data, but from an App Xchange user perspective you are trying to write that data to thr cache. These are two sides of the same coin. 

## Process of implementing a data reader

### Define the Data Objects you want to get from your system.

You will need to provide the specific data objects you want to share to the App Xchange cache. This structure is in the form of a C# model.

Key considerations

- Each data object identified for sharing in your Connector Strategy will be represented as separate C# models.
- These models will be stored in your repository and referenced in your code.
- These models are converted to json and stored by App Xchange so they can enable future Integrations using your Connector.

### Get your Data Using a Data Reader.

The App Xchange Data Reader is how you get the data from your system that you designate into the App Xchange Cache. 

Key considerations

- The data reader is defined through code you write (in C#) and is included in your Connector codebase (in your Connector Github Repository).
- The CLI Tool will help you generate and structure much of the code you need.
- You will need to know the properties of your data as represented in your C# models. 
- Before you begin, consider using an [incremental data reader](../incremental-data-reader/) if a full data read is impractical. 

### The App Xchange Connector Cache.

The Xchange Cache keeps a copy of your data for the purpose of detecting changes and triggering Flows.

Key considerations

- The cache is a Cosmos DB document storage and it is the source of truth for your Xchange Connector.
- The cache is updated based on a variety of factors, but most often based on a polling of changes.
- The cache will persist until it is purged.

The [App Xchange cache](https://docs.appxchange.trimble.com/data-explorer/cache-explorer) is the source of truth for your Xchange Connector. The data in the cache is what will be shared to other systems. In this next step we'll build what is required to write the shareable data to the Xchange cache. Cache writing is performed automatically by the Xchange platform, however, you will need to use a ***Data Reader*** in order to get the data from your system into the Xchange platform.

---

## Creating an example a data object

### Run the `data-object new` command

In the directory your Connector’s C# project resides use this CLI command to begin:

> 

This directory is named `Connector` by default

#### Example CLI command

```
xchange data-object new --module-id app-1 --name Employees

```

Key considerations

By default, this command generates code in the `EmployeesDataReader.cs` file to handle a paginated response from the ApiClient. If the ApiClient's response is not paginated, you can append the `--no-pagination` option to the command.

#### About this command

`data-object new` This command will instantiate a new data object. The following are options for that command:

`module-id` (required) A module allows for the grouping of various functionality in your Connector code. In this specific instance, we’re using a generic default group called: `app-1`.

`connector-path` This defines the path to which your Connector’s C# project resides within the repository. Defaults to the current directory.

`object-name` (required) In this instance we are using Employees as a placeholder for your object’s name. When you're naming your data objects, PascalCase is preferred. Object names tend to be plural, since that's an API convention commonality.

#### Example result

This command will create a new directory in your connector project. Within the `App/v1` directory there is a file named `Employees` (Where Employees is the object name provided).

It will also create the following:

`EmployeesDataObject``EmployeesDataReader`

`EmployeesDataObject` will also be added to its corresponding config and service definitions for this module. These files can be found at:

Connector / App / v1 / `AppV1CacheWriterConfig.cs`  
 Connector / App / v1 / `AppV1CacheWriterServiceDefinition.cs`

---

### Add Properties to the initial placeholder data object

Within the codebase, go to the initial placeholder data object you have created within **App / v1 /**`EmployeesDataObject`. Open `EmployeesDataObject.cs` so you can add properties to that data object. PascalCase is preferred when you're declaring your properties.

The data properties you add should match those provided by your API. Refer to [our planning guide](https://help.trimble.com/en/app-xchange/app-xchange/connectivity/build-a-connector/pre-development-considerations#data-strategy-0) to have a better understanding on connector's scope. 

It is critical that you add properties to your data objects according to our [object schema guide](../object-schema/). Failure to use [WriteOnly](../object-schema/#writeonly-attribute) and [Nullable(true)](../object-schema/#nullable-attribute) are common reasons for connector submission rejection. 

---

### Implement a method in ApiClient to retrieve your data objects

If you haven't done the initial setup for your client, please follow the instructions in how to [build a client for your connector](../creating-an-api-client/).

In this step we will implement a get method in the ApiClient to retrieve you data object items from the external system, this method will be later used by the data reader which will write the data objects to the App Xchange cache.

The way an API returns items can vary. Below are examples API client GET method implementations.

#### When the API returns a JSON array

**Example for an API that returns a JSON array**

This method sends a GET request to the specified relative URL. It then processes the response, deserializes the JSON content into an IEnumerable if successful, and returns an ApiResponse object containing the result. For a streamed example, refer to the "Example for an API that returns streamed JSON objects" section below.

```
public async Task<ApiResponse<IEnumerable<T>>> GetRecords<T>(string relativeUrl, CancellationToken cancellationToken = default)
{
    var response = await _httpClient.GetAsync(relativeUrl, cancellationToken: cancellationToken).ConfigureAwait(false);
    return new ApiResponse<IEnumerable<T>>
    {
        IsSuccessful = response.IsSuccessStatusCode,
        StatusCode = (int)response.StatusCode,
        Data = response.IsSuccessStatusCode ? await response.Content.ReadFromJsonAsync<IEnumerable<T>>(cancellationToken: cancellationToken) : default,
        RawResult = await response.Content.ReadAsStreamAsync(cancellationToken: cancellationToken)
    };
}

```

#### When the API returns a paginated JSON object

**Example for an API that returns a paginated JSON object**

This method sends a GET request to the specified relative URL with pagination support. It then processes the response, deserializes the JSON content into a `PaginatedResponse<T>` if successful, and returns an ApiResponse object containing the result. The PaginatedReponse class should be updated to match your API paginated response. For a streamed example, refer to the "Example for an API that returns streamed JSON objects" section below.

```
public async Task<ApiResponse<PaginatedResponse<T>>> GetRecords<T>(string relativeUrl, int page, CancellationToken cancellationToken = default)
{
    var response = await _httpClient.GetAsync($"{relativeUrl}?page={page}", cancellationToken: cancellationToken).ConfigureAwait(false);
    return new ApiResponse<PaginatedResponse<T>>
    {
        IsSuccessful = response.IsSuccessStatusCode,
        StatusCode = (int)response.StatusCode,
        Data = response.IsSuccessStatusCode ? await response.Content.ReadFromJsonAsync<PaginatedResponse<T>>(cancellationToken: cancellationToken) : default,
        RawResult = await response.Content.ReadAsStreamAsync(cancellationToken: cancellationToken)
    };
}

```

#### When the API returns streamed JSON objects

**Example for an API that returns streamed JSON objects**

This method sends a GET request to the specified URL. It then processes the response, deserializes the JSON content into an asynchronous stream of items of type T, and yields each item to the caller.

```
public async IAsyncEnumerable<T> GetRecords<T>(string relativeUrl, [EnumeratorCancellation] CancellationToken cancellationToken = default)
{
    var response = await _httpClient.GetAsync(relativeUrl, cancellationToken: cancellationToken).ConfigureAwait(false);
    response.EnsureSuccessStatusCode();

    await foreach (var record in JsonSerializer.DeserializeAsyncEnumerable<T>(await response.Content.ReadAsStreamAsync(cancellationToken)))
    {
        if (record == null) continue;
        yield return record;
    }
}

```

You may use the `System.Text.Json` library to deserialize Streams from the response. For more information, you can check [the official documentation](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonserializer.deserializeasync?view=net-9.0).

### Modify the DataReader placeholder class to use your ApiClient

In CLI versions 1.4.9 and later, the `data-object new` command generates a data reader that is pre-configured to use the `ApiClient` you previously created (pay attention to warnings in the console for issues with this process). Your data reader code will likely need access to the `ApiClient` class you created with the `client new` command. If you are using an earlier version of the CLI or your data reader code does not already have your `ApiClient` injected into it, you will need to follow the steps below to manually modify the data reader to utilize your `ApiClient`.

We will start by modifying `EmployeesDataReader.cs`. Here is the path to that file: `Connector/App/v1/Employees/EmployeesDataReader.cs`

Modify the `EmployeesDataReader.cs` file in the following ways:

Add `ApiClient` client to the constructor and inject so that it can be used for `GetDataTypeAsync` method.

**Example of a client injection into `EmployeesDataReader`**

```
public class EmployeesDataReader : TypedAsyncDataReaderBase<EmployeesDataObject>
{
    private readonly ILogger<EmployeesDataReader> _logger;
    private ApiClient _apiClient;
    private int _currentPage = 0;

    public EmployeesDataReader(
        ILogger<EmployeesDataReader> logger,
        ApiClient apiClient)
    {
        _logger = logger;
        _apiClient = apiClient;
    }
}

```

Change the `GetDataTypeAsync` method so that it can be used to get actual data from your system. 

**Example of a `GetDataTypeAsync` implementation with a paginated ApiClient response**
GetDataTypeAsync.cs

```
public override async IAsyncEnumerable<EmployeesDataObject> GetTypedDataAsync(DataObjectCacheWriteArguments ? dataObjectRunArguments, [EnumeratorCancellation] CancellationToken cancellationToken)
{
    while (true)
    {
        var response = new ApiResponse<PaginatedResponse<EmployeesDataObject>>(); // (1)

        try
        {
            response = await _apiClient.GetRecords<EmployeesDataObject>( // (2)
                relativeUrl: "employees",
                page: _currentPage,
                cancellationToken: cancellationToken)
                .ConfigureAwait(false);
        }
        catch (HttpRequestException exception)
        {
            _logger.LogError(exception, "Exception while making a read request to data object 'EmployeesDataObject'");
            throw;
        }

        if (!response.IsSuccessful) // (3)
        {
            throw new Exception($"Failed to retrieve records for 'EmployeesDataObject'. API StatusCode: {response.StatusCode}");
        }

        if (response.Data == null || !response.Data.Items.Any()) break;

        foreach (var item in response.Data.Items)
        {
            yield return item; // (4)
        }

        // (5)
        _currentPage++;
        if (_currentPage >= response.Data.TotalPages)
        {
            break;
        }
    }
}

```

When using a full data reader with change detection and deletes enabled, make sure not to exit the data reader with a break - keep the exception. Otherwise, records and pages after the unsuccessful request will be presumed deleted and also deleted from the cache. 

---

1. If the `DataObject` class does not have the same structure as the response from the API, you can create a new class to deserialize into. Use this class to assist in mapping into a `DataObject` object that will be yielded.
1. Make a call to your API to retrieve the objects from your system.
1. Verify the API call retrieved the objects from your system.
1. Return new EmployeesDataObject to Xchange cache.
1. Handle pagination per API client design.

The default `IAsyncEnumerable` interface used in the Data Reader template allows for asynchronous iteration over a collection of data, and it should not be changed. Since connectors run in environments with limited resources, `IAsyncEnumerable` prevents an out of memory error from attempting to read all data without streaming.

Benefits of using `IAsyncEnumerable` - Non-blocking operations: Asynchronous iteration allows your application to continue processing other tasks while waiting for data to be read. - Improved performance: By not blocking the main thread, your application can handle more concurrent operations, leading to better overall performance. - Scalability: Asynchronous operations can help your application scale better, especially when dealing with large datasets or high-latency data sources.

### Let’s test it out!

Now that you've built a data object and a cache writer, we can test to ensure that everything is behaving like it should.

To test your connector locally, check out our [guide for local testing here](../local-testing/). Otherwise, continue to [Creating Actions](../creating-actions/)
January 14, 2026January 14, 2026
