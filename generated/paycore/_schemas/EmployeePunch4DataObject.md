# EmployeePunch4DataObject

## EmployeePunch4DataObject
- Role: parent
- Schema Name: EmployeePunch4
- Schema ID: schema:components/EmployeePunch4

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
- Parent: EmployeePunch4DataObject
- Schema Name: LaborCode3
- Schema ID: schema:components/LaborCode3

### Fields

| Field | Type |
|------|------|
| `laborCategoryId` | `string` |
| `laborCodeId` | `string` |

## PunchStatusType
- Role: nested
- Parent: EmployeePunch4DataObject
- Schema Name: PunchStatusType
- Schema ID: schema:components/PunchStatusType

### Enum

Values: Auto, In, Out, Transfer
Names: Auto, In, Out, Transfer
