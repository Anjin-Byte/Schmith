# EmployeeTimeOffRequest2DataObject

## EmployeeTimeOffRequest2DataObject
- Role: parent
- Schema Name: EmployeeTimeOffRequest2
- Schema ID: schema:components/EmployeeTimeOffRequest2

### Fields

| Field | Type |
|------|------|
| `employeeId` | `string` |
| `timeOffTypeId` | `string` |
| `status` | `EmployeeTimeOffRequestStatus` |
| `comment` | `string` |
| `days` | `TimeOffRequestDay2[]` |

### Nested Types
- `EmployeeTimeOffRequestStatus`
- `TimeOffRequestDay2`

## EmployeeTimeOffRequestStatus
- Role: nested
- Parent: EmployeeTimeOffRequest2DataObject
- Schema Name: EmployeeTimeOffRequestStatus
- Schema ID: schema:components/EmployeeTimeOffRequestStatus

### Enum

Values: Pending, Approved, Denied, Canceled, Removed
Names: Pending, Approved, Denied, Canceled, Removed

## TimeOffRequestDay2
- Role: nested
- Parent: EmployeeTimeOffRequest2DataObject
- Schema Name: TimeOffRequestDay2
- Schema ID: schema:components/TimeOffRequestDay2

### Fields

| Field | Type |
|------|------|
| `date` | `string` |
| `startTime` | `string` |
| `endTime` | `string` |
| `hours` | `double` |
| `isPartial` | `bool` |
