# File Usage

Below is a guide on how to use the connector to interact with files on the App Xchange platform.

## Overview

This guide will explain how to transfer file data from one connected product or application to another using the Xchange platform.

Creating files on App Xchange is only supported through the use of flows. You may temporarily stage a file on the Xchange platform via the use of [file pointers](../file-pointers/), such that you can pass its contents through action inputs and outputs. You cannot directly upload files to App Xchange.

If you have a file you want to share as part of an integration, that file needs to be publicly accessible. A URL for the file will be streamed to the target system’s connector.

## Example Data Reader Implementation

In this example, a 'job' resource has files attached. The connector cannot pass through those files to the App Xchange cache database and cannot do change detection to evaluate for differences. Instead, replace the file with a URL that can later be used to read from, or remove the property containing the file (byte []/Stream) altogether.

A dedicated endpoint on your system may be required to allow for streaming back the desired file content.

### Data Models

For example, if your API schema for an endpoint is as follows: ``` {
    "type": "object",
    "properties": {
        "JobNumber": {
            "type": "string"
        },
        "Filename": {
            "type": "string"
        },
        "Description": {
            "type": "string"
        },
        "File": {
            "type": "array",
            "items": {
                "type": "integer"
            }
        }
    }
} ``` The C# class for representing the API response would look like this: ``` public class JobResponse
{
    public string JobNumber { get; init; }
    public string Description { get; init; }
    public string FileName { get; init; }
    public byte [] File { get; init; }
} ``` ### Data Reader Logic

There are two methods we can use when the resource we are reading from also contains a file:

- Replace the property containing or pointing to the file with a publicly accessible URL to allow for streaming back the contents of the file
- Remove the property containing or pointing to the file

#### Replacement Method

Within ` GetTypeDataAsync `, we can use the context we know to call an endpoint on your system to generate a URL that can be called at a later date to retrieve this file. ``` public override async IAsyncEnumerable<JobFileAttachmentDataObject> GetTypedDataAsync(DataObjectCacheWriteArguments ? dataObjectRunArguments, [EnumeratorCancellation] CancellationToken cancellationToken)
{
    await foreach (var jobResponse in _apiClient.GetAllJobs<JobResponse>(cancellationToken))
    {
        var fileUrlResponse = await _apiClient.GetJobFileUrl(jobResponse.JobNumber, cancellationToken);
        if (fileUrlResponse is { Successful: false, Data: null })
        {
            _logger.LogError(
                "Failed to retrieve file URL for Job {JobNumber} with filename {Filename}", 
                jobResponse.JobNumber, 
                jobResponse.Filename);
            continue; // Try again on next run
        }

        yield return new JobsDataObject
        {
            JobNumber = jobResponse.JobNumber,
            Filename = jobResponse.Filename,
            Description = jobResponse.Description,
            FileUrl = fileUrlResponse.Data.Url
        };
    }
} ``` Where the JobsDataObject shape looks as follows: ``` public class JobsDataObject
{
    public string JobNumber { get; init; }
    public string Description { get; init; }
    public string FileName { get; init; }
    public string FileUrl { get; init; }
} ``` > 

You may not want to include the FileUrl in the data object being yielded from data readers, such as for performance or security posture reasons. More on this in the [removal method](#removal-method)section.


This results in the job resource put on App Xchange as a URL property. The URL property can be used at a later time to get the file contents based on integration needs.

#### Removal Method

Use ` GetTypeDataAsync ` to remove the property we don't want to send to App Xchange. ``` public override async IAsyncEnumerable<JobFileAttachmentDataObject> GetTypedDataAsync(DataObjectCacheWriteArguments ? dataObjectRunArguments, [EnumeratorCancellation] CancellationToken cancellationToken)
{
    await foreach (var jobResponse in _apiClient.GetAllJobs<JobResponse>(cancellationToken))
    {
        yield return new JobsDataObject
        {
            JobNumber = jobResponse.JobNumber,
            Filename = jobResponse.Filename,
            Description = jobResponse.Description
        };
    }
} ``` Where the JobsDataObject shape looks as follows: ``` public class JobsDataObject
{
    public string JobNumber { get; init; }
    public string Description { get; init; }
    public string FileName { get; init; }
} ``` This means if part of an integration needs to access the job's file content, we need to get it on demand. This is preferred as your target system can create a presigned URL that could expire after a period of time. In order to provide this functionality, you will need to create an action in the connector.

## Action Handler for Generating File URLs

In this case here the method for sharing files to a target system is done on demand through the use of a publicly accessible URL. In order for the action to do this it will need some context. Continuing from the example set above in the [Data Reader Replacement](#replacement-method)method.

The Connector will need an action that takes in an input that gives the action handler enough context as to which file in question it is after and then the action would then want to return an output of the URL for accessing the file.

> 

This file URL could be pre-signed and have a TTL


Here is an example action input shape: ``` public class CreateJobFileUrlInput
{
    public string JobNumber { get; init; }
} ``` The action handler's logic would go as follows: ``` public async Task<ActionHandlerOutcome> HandleQueuedActionAsync(ActionInstance actionInstance, CancellationToken cancellationToken)
{
    var input = JsonSerializer.Deserialize<CreateJobFileUrlInput>(actionInstance.InputJson);
    var fileUrlResponse = await _apiClient.CreateJobFileUrl(input.JobNumber, cancellationToken);
    if (fileUrlResponse is { Successful: true, Data: not null })
        return ActionHandlerOutcome.Successful(fileUrlResponse.Data.Url);

    return ActionHandlerOutcome.Failed(new StandardActionFailure
    {
        Code = fileUrlResponse.StatusCode,
        Errors = new []
        {
            new Xchange.Connector.SDK.Action.Error
            {
                Source = new string [] { "CreateJobFileUrl" };,
                Text = new StreamReader(fileUrlResponse.RawContent).ReadToEnd()
            }
        }
    });
} ``` This results in integrations being able to get access to a file on a job on demand by consuming the action's output.

> 

The action could also take in a list of ` JobNumbers ` and produce a map of file URLs

## Action Handler for Uploading a File

In this example the problem at hand is that part of performing the action also includes a file as part of its input. Since you cannot pass a file within an action input you can instead update the action's input to include how to get the file.

The scenario here is that you have an action that adds a file to a job resource. Therefore the target endpoint wants the following things:

- The job resource being acted on
- Metadata about the file
- The file

### Data Models

For example if your API schema for an endpoint is as follows: ``` {
    "type": "object",
    "properties": {
        "JobNumber": {
            "type": "string"
        },
        "Filename": {
            "type": "string"
        },
        "Description": {
            "type": "string"
        },
        "File": {
            "type": "array",
            "items": {
                "type": "integer"
            }
        }
    }
} ``` Where the ` File ` property is a byte array. Since you cannot have a byte array as an action input then you cannot have this as part of the schema or model for the connector's action input. This should instead be replaced with a URL of where to access the file. Making your action input class look as follows: ``` public class UploadJobFileInput
{
    public string JobNumber { get; init; }
    public string Filename { get; init; }
    public string Description { get; init; }
    public string FileUrl { get; init; }
} ``` ### Action Handler Logic

In order to get the file's contents to stream to the target system API we need to use an HTTP client. You can inject the IHttpClientFactory via the action handler's constructor. ``` public UploadJobFileHandler(
        IHostContext hostContext,
        ILogger<UploadJobFileHandler> logger,
        IApiClient apiClient,
        IHttpClientFactory clientFactory)
{
    _hostContext = hostContext;
    _logger = logger;
    _apiClient = apiClient;
    _fileClient = clientFactory.CreateClient();
} ``` Then within the action handler the following can be done to retrieve the file and upload to the target system API ``` public async Task<ActionHandlerOutcome> HandleQueuedActionAsync(ActionInstance actionInstance, CancellationToken cancellationToken)
{
    var input = JsonSerializer.Deserialize<UploadJobFileInput>(actionInstance.InputJson);
    using var fileResponse = await _fileClient.GetAsync(
        input.FileUrl,
        HttpCompletionOption.ResponseHeadersRead,
        cancellationToken: cancellationToken);        
    var uploadResponse = await _apiClient.CreateJobFile(
            jobNumber: input.JobNumber,
            filename: input.Filename,
            description: input.Description,
            File: await fileResponse.Content.ReadAsStreamAsync(cancellationToken), 
            cancellationToken);
    if (uploadResponse is { Successful: true, Data: not null })
        // Note: If a job resource on the Xchange platform keeps track of file(s) for a job then we want to 
        // produce a cache change here with this new file on the job resource
        return ActionHandlerOutcome.Successful(uploadResponse.Data.Id); 

    return ActionHandlerOutcome.Failed(new StandardActionFailure
    {
        Code = uploadResponse.StatusCode,
        Errors = new []
        {
            new Xchange.Connector.SDK.Action.Error
            {
                Source = new string [] { "UploadJobFile" };,
                Text = new StreamReader(uploadResponse.RawContent).ReadToEnd()
            }
        }
    }); 
} ``` January 14, 2026January 14, 2026
