# MissedPunchRequest3DataObject

## MissedPunchRequest3DataObject
- Role: parent
- Schema Name: MissedPunchRequest3
- Schema ID: schema:components/MissedPunchRequest3

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
- Parent: MissedPunchRequest3DataObject
- Schema Name: LaborCode3
- Schema ID: schema:components/LaborCode3

### Fields

| Field | Type |
|------|------|
| `laborCategoryId` | `string` |
| `laborCodeId` | `string` |

## PunchStatusType
- Role: nested
- Parent: MissedPunchRequest3DataObject
- Schema Name: PunchStatusType
- Schema ID: schema:components/PunchStatusType

### Enum

Values: Auto, In, Out, Transfer
Names: Auto, In, Out, Transfer
