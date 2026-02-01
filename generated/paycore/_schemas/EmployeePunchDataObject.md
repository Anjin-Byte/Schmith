# EmployeePunchDataObject

## EmployeePunchDataObject
- Role: parent
- Schema Name: EmployeePunch
- Schema ID: schema:components/EmployeePunch

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
- `PunchStatusType`

## LaborCode3
- Role: nested
- Parent: EmployeePunchDataObject
- Schema Name: LaborCode3
- Schema ID: schema:components/LaborCode3

### Fields

| Field | Type |
|------|------|
| `laborCategoryId` | `string` |
| `laborCodeId` | `string` |

## PunchStatusType
- Role: nested
- Parent: EmployeePunchDataObject
- Schema Name: PunchStatusType
- Schema ID: schema:components/PunchStatusType

### Enum

Values: Auto, In, Out, Transfer
Names: Auto, In, Out, Transfer
