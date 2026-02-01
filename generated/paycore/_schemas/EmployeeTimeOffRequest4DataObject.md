# EmployeeTimeOffRequest4DataObject

## EmployeeTimeOffRequest4DataObject
- Role: parent
- Schema Name: EmployeeTimeOffRequest4
- Schema ID: schema:components/EmployeeTimeOffRequest4

### Fields

| Field | Type |
|------|------|
| `timeOffRequestId` | `string` |
| `status` | `EmployeeTimeOffRequestStatus2` |
| `comment` | `string` |

### Nested Types
- `EmployeeTimeOffRequestStatus2`

## EmployeeTimeOffRequestStatus2
- Role: nested
- Parent: EmployeeTimeOffRequest4DataObject
- Schema Name: EmployeeTimeOffRequestStatus2
- Schema ID: schema:components/EmployeeTimeOffRequestStatus2

### Enum

Values: Approved, Denied
Names: Approved, Denied
