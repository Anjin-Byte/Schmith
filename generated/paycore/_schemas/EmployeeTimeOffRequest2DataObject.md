# EmployeeTimeOffRequest2DataObject

## EmployeeTimeOffRequest2DataObject
- Role: parent
- Schema Name: EmployeeTimeOffRequest2
- Schema ID: schema:components/EmployeeTimeOffRequest2
- Primary Key: Employeeid

### Fields

| Field | Type |
|------|------|
| `employeeId` | `string` |
| `timeOffTypeId` | `string` |
| `status` | `EmployeeTimeOffRequestStatus` |
| `comment` | `string` |
| `days` | `TimeOffRequestDay2[]` |

### Nested Types
- `TimeOffRequestDay2`

## TimeOffRequestDay2
- Role: nested
- Parent: EmployeeTimeOffRequest2DataObject
- Schema Name: TimeOffRequestDay2
- Schema ID: schema:components/TimeOffRequestDay2
- Primary Key: Date

### Fields

| Field | Type |
|------|------|
| `date` | `string` |
| `startTime` | `string` |
| `endTime` | `string` |
| `hours` | `double` |
| `isPartial` | `bool` |
