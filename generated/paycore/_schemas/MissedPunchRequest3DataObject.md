# MissedPunchRequest3DataObject

## MissedPunchRequest3DataObject
- Role: parent
- Schema Name: MissedPunchRequest3
- Schema ID: schema:components/MissedPunchRequest3
- Primary Key: Employeeid

### Fields

| Field | Type |
|------|------|
| `employeeId` | `string` |
| `departmentId` | `string` |
| `punchDateTime` | `string` |
| `punchStatusType` | `PunchStatusType` |
| `activityTypeId` | `string` |
| `isTransfer` | `bool` |
| `note` | `string` |
| `laborCodes` | `LaborCode3[]` |
| `workLocationId` | `string` |

### Nested Types
- `LaborCode3`

## LaborCode3
- Role: nested
- Parent: MissedPunchRequest3DataObject
- Schema Name: LaborCode3
- Schema ID: schema:components/LaborCode3

### Fields

| Field | Type |
|------|------|
| `laborCategoryId` | `string` |
| `laborCodeId` | `string` |
