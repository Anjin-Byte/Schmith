# PagedResultOfSchedulingJobDataObject

## PagedResultOfSchedulingJobDataObject
- Role: parent
- Schema Name: PagedResultOfSchedulingJob
- Schema ID: schema:components/PagedResultOfSchedulingJob

### Fields
- `hasMoreResults`: `bool`
- `continuationToken`: `string`
- `additionalResultsUrl`: `string`
- `records`: `SchedulingJob[]`

### Nested Types
- `SchedulingJob`

## SchedulingJob
- Role: nested
- Parent: PagedResultOfSchedulingJobDataObject
- Schema Name: SchedulingJob
- Schema ID: schema:components/SchedulingJob

### Fields
- `schedulingJobId`: `string`
- `schedulingJobName`: `string`
