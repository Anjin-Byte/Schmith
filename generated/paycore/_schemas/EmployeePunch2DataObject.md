# EmployeePunch2DataObject

## EmployeePunch2DataObject
- Role: parent
- Schema Name: EmployeePunch2
- Schema ID: schema:components/EmployeePunch2

### Fields

| Field | Type |
|------|------|
| `punchId` | `string` |
| `punchRefId` | `string` |
| `punchDateTime` | `string` |
| `punchStatusType` | `PunchStatusType` |
| `isTransfer` | `bool` |
| `activityTypeId` | `string` |
| `departmentId` | `string` |
| `note` | `string` |
| `laborCodes` | `LaborCode3[]` |
| `workLocationId` | `string` |

### Nested Types
- `LaborCode3`
- `PunchStatusType`

## LaborCode3
- Role: nested
- Parent: EmployeePunch2DataObject
- Schema Name: LaborCode3
- Schema ID: schema:components/LaborCode3

### Fields

| Field | Type |
|------|------|
| `laborCategoryId` | `string` |
| `laborCodeId` | `string` |

## PunchStatusType
- Role: nested
- Parent: EmployeePunch2DataObject
- Schema Name: PunchStatusType
- Schema ID: schema:components/PunchStatusType

### Enum

Values: Auto, In, Out, Transfer
Names: Auto, In, Out, Transfer
