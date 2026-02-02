# PagedResultOfSchedulingShiftDataObject

## PagedResultOfSchedulingShiftDataObject
- Role: parent
- Schema Name: PagedResultOfSchedulingShift
- Schema ID: schema:components/PagedResultOfSchedulingShift

### Fields

| Field | Type |
|------|------|
| `hasMoreResults` | `bool` |
| `continuationToken` | `string` |
| `additionalResultsUrl` | `string` |
| `records` | `SchedulingShift[]` |

### Nested Types
- `BreakRuleWithDates`
- `SchedulingShift`
- `ShiftAcknowledgementStatus`
- `ShiftLaborCode`

## BreakRuleWithDates
- Role: nested
- Parent: PagedResultOfSchedulingShiftDataObject
- Schema Name: BreakRuleWithDates
- Schema ID: schema:components/BreakRuleWithDates

### Fields

| Field | Type |
|------|------|
| `paid` | `bool` |
| `breakInMinutes` | `int` |
| `startTime` | `string` |
| `endTime` | `string` |

## SchedulingShift
- Role: nested
- Parent: PagedResultOfSchedulingShiftDataObject
- Schema Name: SchedulingShift
- Schema ID: schema:components/SchedulingShift
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `employeeId` | `string` |
| `employeeName` | `string` |
| `schedulingJobId` | `string` |
| `schedulingJobName` | `string` |
| `scheduleGroupId` | `string` |
| `scheduleGroupName` | `string` |
| `isPublished` | `bool` |
| `title` | `string` |
| `startDateTime` | `string` |
| `endDateTime` | `string` |
| `color` | `string` |
| `departmentId` | `string` |
| `departmentName` | `string` |
| `notes` | `string` |
| `breakRules` | `BreakRuleWithDates[]` |
| `netPaidHoursOnly` | `double` |
| `workSiteId` | `string` |
| `workSiteName` | `string` |
| `distance` | `double` |
| `acknowledgementStatus` | `ShiftAcknowledgementStatus` |
| `activityTypeId` | `string` |
| `activityTypeName` | `string` |
| `activityTypeColor` | `string` |
| `laborCodes` | `ShiftLaborCode[]` |
| `workLocationId` | `string` |
| `workLocationName` | `string` |

## ShiftAcknowledgementStatus
- Role: nested
- Parent: PagedResultOfSchedulingShiftDataObject
- Schema Name: ShiftAcknowledgementStatus
- Schema ID: schema:components/ShiftAcknowledgementStatus

### Enum

Values: Pending, Confirmed, Rejected
Names: Pending, Confirmed, Rejected

## ShiftLaborCode
- Role: nested
- Parent: PagedResultOfSchedulingShiftDataObject
- Schema Name: ShiftLaborCode
- Schema ID: schema:components/ShiftLaborCode

### Fields

| Field | Type |
|------|------|
| `laborCategoryId` | `string` |
| `laborCodeId` | `string` |
| `code` | `string` |
| `laborCodeName` | `string` |
