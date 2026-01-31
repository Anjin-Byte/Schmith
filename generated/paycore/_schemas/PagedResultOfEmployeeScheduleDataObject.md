# PagedResultOfEmployeeScheduleDataObject

## PagedResultOfEmployeeScheduleDataObject
- Role: parent
- Schema Name: PagedResultOfEmployeeSchedule
- Schema ID: schema:components/PagedResultOfEmployeeSchedule

### Fields
- `hasMoreResults`: `bool`
- `continuationToken`: `string`
- `additionalResultsUrl`: `string`
- `records`: `EmployeeSchedule[]`

### Nested Types
- `EmployeeSchedule`
- `ResourceReference`
- `Schedule`

## EmployeeSchedule
- Role: nested
- Parent: PagedResultOfEmployeeScheduleDataObject
- Schema Name: EmployeeSchedule
- Schema ID: schema:components/EmployeeSchedule

### Fields
- `date`: `string`
- `employeeId`: `string`
- `legalEntityId`: `int`
- `schedules`: `Schedule[]`
- `totalShifts`: `int`
- `totalHours`: `double`
- `employee`: `ResourceReference`

## ResourceReference
- Role: nested
- Parent: PagedResultOfEmployeeScheduleDataObject
- Schema Name: ResourceReference
- Schema ID: schema:components/ResourceReference

### Fields
- `id`: `string`
- `url`: `string`

## Schedule
- Role: nested
- Parent: PagedResultOfEmployeeScheduleDataObject
- Schema Name: Schedule
- Schema ID: schema:components/Schedule

### Fields
- `scheduleId`: `string`
- `startDateTime`: `string`
- `endDateTime`: `string`
- `beforeStartTimeInMinutes`: `int`
- `afterEndTimeInMinutes`: `int`
- `shiftDepartmentName`: `string`
- `shiftName`: `string`
- `totalMinutesWorked`: `int`
- `totalHoursWorked`: `double`
- `startDateTimeWithBefore`: `string`
- `endDateTimeWithAfter`: `string`
- `crossesMidnight`: `bool`
- `shiftDepartment`: `ResourceReference`
