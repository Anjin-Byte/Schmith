# SchedulingShift2DataObject

## SchedulingShift2DataObject
- Role: parent
- Schema Name: SchedulingShift2
- Schema ID: schema:components/SchedulingShift2
- Primary Key: Ignorewarnings

### Fields

| Field | Type |
|------|------|
| `ignoreWarnings` | `bool` |
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
| `workLocationId` | `string` |

### Nested Types
- `LaborCode3`
- `SchedulingShiftBreak`

## LaborCode3
- Role: nested
- Parent: SchedulingShift2DataObject
- Schema Name: LaborCode3
- Schema ID: schema:components/LaborCode3

### Fields

| Field | Type |
|------|------|
| `laborCategoryId` | `string` |
| `laborCodeId` | `string` |

## SchedulingShiftBreak
- Role: nested
- Parent: SchedulingShift2DataObject
- Schema Name: SchedulingShiftBreak
- Schema ID: schema:components/SchedulingShiftBreak

### Fields

| Field | Type |
|------|------|
| `startTime` | `string` |
| `endTime` | `string` |
