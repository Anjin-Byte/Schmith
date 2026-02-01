# SchedulingShiftsDataObject

## SchedulingShiftsDataObject
- Role: parent
- Schema Name: SchedulingShifts
- Schema ID: schema:components/SchedulingShifts

### Fields

| Field | Type |
|------|------|
| `ignoreWarnings` | `bool` |
| `shifts` | `SchedulingShiftItem[]` |

### Nested Types
- `LaborCode3`
- `SchedulingShiftBreak`
- `SchedulingShiftItem`

## LaborCode3
- Role: nested
- Parent: SchedulingShiftsDataObject
- Schema Name: LaborCode3
- Schema ID: schema:components/LaborCode3

### Fields

| Field | Type |
|------|------|
| `laborCategoryId` | `string` |
| `laborCodeId` | `string` |

## SchedulingShiftBreak
- Role: nested
- Parent: SchedulingShiftsDataObject
- Schema Name: SchedulingShiftBreak
- Schema ID: schema:components/SchedulingShiftBreak

### Fields

| Field | Type |
|------|------|
| `startTime` | `string` |
| `endTime` | `string` |

## SchedulingShiftItem
- Role: nested
- Parent: SchedulingShiftsDataObject
- Schema Name: SchedulingShiftItem
- Schema ID: schema:components/SchedulingShiftItem

### Fields

| Field | Type |
|------|------|
| `isPublished` | `bool` |
| `title` | `string` |
| `employeeId` | `string` |
| `scheduleGroupId` | `string` |
| `schedulingJobId` | `string` |
| `startDateTime` | `string` |
| `endDateTime` | `string` |
| `notes` | `string` |
| `departmentId` | `string` |
| `workSiteId` | `string` |
| `activityTypeId` | `string` |
| `breaks` | `SchedulingShiftBreak[]` |
| `laborCodes` | `LaborCode3[]` |
| `shiftModelId` | `string` |
| `workLocationId` | `string` |
