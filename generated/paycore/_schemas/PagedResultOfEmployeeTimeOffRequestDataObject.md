# PagedResultOfEmployeeTimeOffRequestDataObject

## PagedResultOfEmployeeTimeOffRequestDataObject
- Role: parent
- Schema Name: PagedResultOfEmployeeTimeOffRequest
- Schema ID: schema:components/PagedResultOfEmployeeTimeOffRequest

### Fields
- `hasMoreResults`: `bool`
- `continuationToken`: `string`
- `additionalResultsUrl`: `string`
- `records`: `EmployeeTimeOffRequest[]`

### Nested Types
- `EmployeeTimeOffRequest`
- `TimeOffRequestDay`

## EmployeeTimeOffRequest
- Role: nested
- Parent: PagedResultOfEmployeeTimeOffRequestDataObject
- Schema Name: EmployeeTimeOffRequest
- Schema ID: schema:components/EmployeeTimeOffRequest

### Fields
- `legalEntityId`: `int`
- `timeOffRequestId`: `string`
- `benefitCode`: `string`
- `totalHours`: `double`
- `days`: `TimeOffRequestDay[]`
- `comment`: `string`
- `status`: `string`
- `createdDate`: `string`
- `statusUpdateTime`: `string`
- `statusUpdateByEmployeeId`: `string`
- `createdByEmployeeId`: `string`
- `employeeId`: `string`

## TimeOffRequestDay
- Role: nested
- Parent: PagedResultOfEmployeeTimeOffRequestDataObject
- Schema Name: TimeOffRequestDay
- Schema ID: schema:components/TimeOffRequestDay

### Fields
- `timeOffRequestDayId`: `string`
- `date`: `string`
- `hours`: `double`
- `startTime`: `string`
- `endTime`: `string`
- `isPartial`: `bool`
