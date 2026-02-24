# Creating Actions

When a user in the Xchange platform wants to perform some action against a target system, that request is called an `Action`. These Actions that can be performed against a system are defined by the connector builders.

For context, your action will be available as the [Connector Action Flow Step](https://help.trimble.com/en/app-xchange/app-xchange/flows/flow-steps/connector-action-flow-step).

The service that contains all of the Action Handlers defined in the connector is called Action Processor. The Action Processor, using a path-based factory, is the one that gets the correct Handler to instantiate when a user creates an action payload, and it passes the action payload.

## About Action Handlers

The Action Handler decides what should happen in response to the event and is used to change data in your system.

When Action Processing is required, the Xchange platform will create an event that passes the data that needs to be changed to your Handler in the form of an ActionInput.

A Handler uses an Action to define the `ActionInput`,`ActionOutput` and `ActionFailure` models, and it uses them in a request to your system.

## Putting Action Handlers into action

We’ll start using the CLI to create your first Action, using PascalCase for the name.

#### The CLI command:

```
xchange action new --module-id app-1 --object-name Employees --name Create
```

### Options for this command

- **--module-id**

  - A module allows for the grouping of various functionality in your Connector code. In this specific instance, we’re using a generic default group called: `app-1`.
  - Required: True

- **--object-name**(aliases: -o)

  - The name of the data object to create an Action Handler for. PascalCase is preferred. In this instance we are using `Employees` as a placeholder for your object's name.
  - Required: True

> NOTE! The object-name you use here must match the name of the data object you previously created. Actions are always associated with a specific data object.

- 

**--name**(aliases: -n, --action-name)

  - Create a name for this Action. In this instance we’ll call this Action Create.
  - Required: True

- 

**--connector-path**

  - The path of the folder in which the connector project lives. Defaults to the current working directory if not set.
  - Required: False
  - Default: Current working directory

This command will create a new folder in your repository, within the `App/v1/Employees` folder, named `Create`(or whatever the actual action name is that you provided).

In the `CreateEmployeesAction.cs` file there will be three new classes for data transfer:`CreateEmployeesAction`,`CreateEmployeesActionInput`,`CreateEmployeesActionOutput`. `CreateEmployeesActionInput` will need to be modified to include all the properties required for the Handler. These properties are based on what you want your Handler to do, since they are the input for your connector. The `ActionInput` property is an instance of this class. `CreateEmployeesActionOutput` will need to be modified to include all the properties you want to return to the Xchange platform. These properties will usually match the properties of the data object so that the Xchange cache can be updated for your Connector. The `ActionOutput` property is an instance of this class.

Note it can be convenient to use inheritance here.

**Create Inheritance Example**

When Create, Update, or Upsert matches the data object, you may want to use the following: ```public class CreateEmployeeActionInput: EmployeesDataObject {}``` `StandardActionFailure` is a Connector SDK defined class that also makes an appearance on `CreateEmployeesAction.cs`, since the `ActionFailure` property is an instance of it, and it's a class for error handling. The properties of this class provide details of an error, its message and its source.

For more guidance on how to add properties to your input and output data objects follow our [object schema guide](../object-schema/).

---

## Implement a method in ApiClient to perform your action

If you haven't done the initial setup for your client, please follow the instructions in how to [build a client for your connector](../creating-an-api-client/).

In this step we will implement a method in the `ApiClient` class to update your data objects on the external system. This method will later be used by the action handler, which will write the data objects to the App Xchange cache.

Below is an example of an API client POST method implementation. Make sure to modify the method according to the particular API endpoint's HTTP verb and response structure.

**Example for a POST API method**

This method sends a POST request to the specified relative URL. It then processes the response, deserializes the JSON content into an object of type `T` if successful, and returns an ApiResponse object containing the result. ```public async Task<ApiResponse<T>> PostDataObject<T>(string relativeUrl, object requestBody, CancellationToken cancellationToken = default)
{
    var response = await _httpClient.PostAsJsonAsync(relativeUrl, requestBody, cancellationToken).ConfigureAwait(false);

    return new ApiResponse<T>
    {
        IsSuccessful = response.IsSuccessStatusCode,
        StatusCode = (int)response.StatusCode,
        Data = response.IsSuccessStatusCode ? await response.Content.ReadFromJsonAsync<T>(cancellationToken: cancellationToken): default,
        RawResult = await response.Content.ReadAsStreamAsync(cancellationToken: cancellationToken)
    };
}```## Modify the ActionHandler placeholder class to use your ApiClient

In CLI versions 1.4.9 and later, the` action new `command generates an action handler that is pre-configured to use the` ApiClient `you previously created (pay attention to console warnings for issues with this process). Your action handler code will likely need access to the` ApiClient `class you created with the` client new `command. If you are using an earlier version of the CLI or your action handler code does not already have your` ApiClient `injected into it, you will need to follow the steps below to manually modify the data reader to utilize your` ApiClient `.

With your CLI command a placeholder class file was created called `CreateEmployeesHandler.cs`. We now want to modify that file so that it does what you want.

We will want to inject your `ApiClient` into `CreateEmployeesHandler`.

**Example of an ApiClient injection into `CreateEmployeesHandler`** ```public class CreateEmployeesHandler: IActionHandler<CreateEmployeesAction>
{   
    ILogger<CreateEmployeesHandler> _logger;
    private readonly ApiClient _apiClient;

    public CreateEmployeesHandler(
        ILogger<CreateEmployeesHandler> logger,
        ApiClient apiClient)
    {
        _logger = logger;
        _apiClient = apiClient;
    }
}```Below are additional basic modifications to the` CreateEmployeesHandler `with comments inline. Change the` HandleQueuedActionAsync `method so that it can be used to write changes back to your system.

**Example of a basic` HandleQueuedActionAsync `implementation**

In summary what is being done is:

1. Given the input for the action, make a call to your API/system.
1. Build sync operations to update the local cache as well as the Xchange cache system (if the data type is cached).
1. If an error occurs, we want to create a failure result for the action that matches the failure type for the action. Common to create extension methods to map to` StandardActionFailure `. ```public async Task<ActionHandlerOutcome> HandleQueuedActionAsync(ActionInstance actionInstance, CancellationToken cancellationToken)
{
    var input = JsonSerializer.Deserialize<CreateEmployeesActionInput> (actionInstance.InputJson)!;
    try
    {
        // (1) 
        var response = await _apiClient.CreateEmployee(input, cancellationToken).ConfigureAwait(false);

        // The full record is needed for SyncOperations. If the endpoint used for the action returns a partial record (such as only returning the ID) then you can either:
        // - Make a GET call using the ID that was returned
        // - Add the ID property to your action input (Assuming this results in the proper data object shape)

        // var resource = await _apiClient.GetEmployee(response.Data.id, cancellationToken);

        // var resource = new CreateEmployeesActionOutput
        // {
        //      TODO: map
        // };

        // If the response is already the output object for the action, you can use the response directly

        if (!response.IsSuccessful || response.Data == default)
            return ActionHandlerOutcome.Failed(new StandardActionFailure
            {
                Code = response.StatusCode.ToString(),
                Errors = new []
                {
                    new Error
                    {
                        Source = new [] { nameof(CreateEmployeesHandler) },
                        Text = $"Failed to create employee with status code {response.StatusCode}"
                    }
                }
            });

        // (2)
        // Build sync operations to update the local cache as well as the Xchange cache system (if the data type is cached)
        // For more information on SyncOperations and the KeyResolver, check:
        //  https://trimble-xchange.github.io/connector-docs/guides/creating-actions/#sync-operations-in-detail
        var operations = new List<SyncOperation>();
        var keyResolver = new DefaultDataObjectKey();
        var key = keyResolver.BuildKeyResolver()(response.Data);
        operations.Add(SyncOperation.CreateSyncOperation(UpdateOperation.Upsert.ToString(), key.UrlPart, key.PropertyNames, response.Data));

        var resultList = new List<CacheSyncCollection>
        {
            new CacheSyncCollection() { DataObjectType = typeof(EmployeesDataObject), CacheChanges = operations.ToArray() }
        };

        return ActionHandlerOutcome.Successful(response.Data, resultList);
    }
    catch (ApiException exception)
    {
        // (3)

        var errorSource = new List<string> { nameof(CreateEmployeesHandler) };
        if (string.IsNullOrEmpty(exception.Source)) errorSource.Add(exception.Source!);

        return ActionHandlerOutcome.Failed(new StandardActionFailure
        {
            Code = exception.StatusCode?.ToString() ?? "500",
            Errors = new []
            {
                new Error
                {
                    Source = errorSource.ToArray(),
                    Text = exception.Message
                }
            }
        });
    }
}```## Sync Operations in Detail

The sync operations update the Connector's current cache. When new records are created, or existing records are updated, the cache needs to be updated to reflect the changes. The` DefaultDataObjectKey `object is used to derive the key from the record.

Take the following as an example when using the` DefaultDataObjectKey `for resolving```var operations = new List<SyncOperation>();
var keyResolver = new DefaultDataObjectKey();
var key = keyResolver.BuildKeyResolver()(response.Data);  // Where` response.Data `is the new record
operations.Add(SyncOperation.CreateSyncOperation(
    UpdateOperation.Upsert.ToString(),
    key.UrlPart, 
    key.PropertyNames, 
    response.Data));

var resultList = new List<CacheSyncCollection>
{
    new CacheSyncCollection()
    { 
        DataObjectType = typeof(EmployeeDataObject), 
        CacheChanges = operations.ToArray() 
    }
};

return ActionHandlerOutcome.Successful(response.Data, resultList);```### Deletions

When a record is deleted, there are a few things to note: 1. Your input and output objects are likely much more limited, for example, having only the` Id `of the object to be deleted 2. You will need to change```operations.Add(SyncOperation.CreateSyncOperation(UpdateOperation.Upsert.ToString(), key.UrlPart, key.PropertyNames, response.Data));```to```operations.Add(SyncOperation.CreateSyncOperation(UpdateOperation.Delete.ToString(), key.UrlPart, key.PropertyNames, response.Data));```3. the target system API will sometimes return a 204 status code, which would mean that` response.Data `is null. In this case, you can still create a sync operation to remove the record from the cache, using the following example:```// Given that response.Data is null, no key can be derived.
// Thus, you need to manually provide the key name and the properties that correspond to the key.
// i.e. if you had a composite key of` id `and` division `, you would provide those as the property names.
var input = JsonSerializer.Deserialize<DeleteEmployeesActionInput>(actionInstance.InputJson)!; // Action input for delete action
try
{
    var response = await _apiClient.DeleteRecord($"employees/{input.EmployeeId}", cancellationToken);

     // Handle response, e.g., check if deletion was successful
     // If it was successful:
     var operations = new List<SyncOperation>();
     operations.Add(SyncOperation.CreateSyncOperation(
        UpdateOperation.Delete.ToString(), // Note the change from Upsert to Delete
        "id", // The key name, which must match the key defined in your data object schema
        new [] { input.EmployeeId.ToString() }, // The property names that make up the key
        null // No data is needed for delete operations));

    var resultList = new List<CacheSyncCollection>
    {
        new() { DataObjectType = typeof(EmployeesDataObject), CacheChanges = operations.ToArray() }
    };
    return ActionHandlerOutcome.Successful(input, resultList);
} catch (ApiException exception)
{
    // Handle exception
} ```By default` DefaultDataObjectKey `will attempt to create a key using` id `as its name and` id `as the property to retrieve the value from. For example if given a record that looks as seen below the key will resolve as` id/123 `. ```{
    "id": 123,
    "firstName": "John",
    "lastName": "Smith"
}```This should match what was defined on the [data object's key](../object-schema/#primary-key-attribute)you are acting on for this sync operation.

If your record does not fit what is done by default then you can change it by supplying different parameters to` DefaultDataObjectKey `on its constructor.```var keyResolver = new DefaultDataObjectKey("employeeId", "primaryKey");```Using the same example provided about the key would resolve as` employeeId/123 `. This also means that the data object should be defined as: ```[PrimaryKey("employeeId", "primaryKey")]
[Description("The representation of an employee")]
public class EmployeeDataObject
{
    [Required]
    public required long PrimaryKey { get; init; }
}```A similar pattern is also done if trying to resolve a key that is composed of multiple properties, these are known as [Composite Keys](../object-schema/#composite-keys). Using the example defined in the [Composite Keys](../object-schema/#composite-keys)we can construct a key resolver as follows:```var keyResolver = new DefaultDataObjectKey("id", "division", "id");``` ## Testing

To test your connector locally, check out our [guide for local testing here](../local-testing/).
January 14, 2026January 14, 2026
