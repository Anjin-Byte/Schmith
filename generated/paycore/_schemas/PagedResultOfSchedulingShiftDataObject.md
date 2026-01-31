# PagedResultOfSchedulingShiftDataObject

## PagedResultOfSchedulingShiftDataObject
- Role: parent
- Schema Name: PagedResultOfSchedulingShift
- Schema ID: schema:components/PagedResultOfSchedulingShift

### Fields
- `hasMoreResults`: `bool`
- `continuationToken`: `string`
- `additionalResultsUrl`: `string`
- `records`: `SchedulingShift[]`

### Nested Types
- `BreakRuleWithDates`
- `SchedulingShift`

## BreakRuleWithDates
- Role: nested
- Parent: PagedResultOfSchedulingShiftDataObject
- Schema Name: BreakRuleWithDates
- Schema ID: schema:components/BreakRuleWithDates

### Fields
- `paid`: `bool`
- `breakInMinutes`: `int`
- `startTime`: `string`
- `endTime`: `string`

## SchedulingShift
- Role: nested
- Parent: PagedResultOfSchedulingShiftDataObject
- Schema Name: SchedulingShift
- Schema ID: schema:components/SchedulingShift

### Fields
- `id`: `string`
- `employeeId`: `string`
- `employeeName`: `string`
- `schedulingJobId`: `string`
- `schedulingJobName`: `string`
- `scheduleGroupId`: `string`
- `scheduleGroupName`: `string`
- `isPublished`: `bool`
- `title`: `string`
- `startDateTime`: `string`
- `endDateTime`: `string`
- `color`: `string`
- `departmentId`: `string`
- `departmentName`: `string`
- `notes`: `string`
- `breakRules`: `BreakRuleWithDates[]`
- `netPaidHoursOnly`: `double`
- `workSiteId`: `string`
- `workSiteName`: `string`
- `distance`: `double`
- `acknowledgementStatus`: `ShiftAcknowledgementStatus`
- `activityTypeId`: `string`
- `activityTypeName`: `string`
- `activityTypeColor`: `string`
- `laborCodes`: `ShiftLaborCode[]`
- `workLocationId`: `string`
- `workLocationName`: `string`
