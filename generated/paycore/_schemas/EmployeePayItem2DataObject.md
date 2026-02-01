# EmployeePayItem2DataObject

## EmployeePayItem2DataObject
- Role: parent
- Schema Name: EmployeePayItem2
- Schema ID: schema:components/EmployeePayItem2

### Fields

| Field | Type |
|------|------|
| `payItemId` | `string` |
| `payItemRefId` | `string` |
| `legalEntityEarningId` | `string` |
| `amount` | `double` |
| `departmentId` | `string` |
| `note` | `string` |
| `laborCodes` | `LaborCode3[]` |
| `workLocationId` | `string` |

### Nested Types
- `LaborCode3`

## LaborCode3
- Role: nested
- Parent: EmployeePayItem2DataObject
- Schema Name: LaborCode3
- Schema ID: schema:components/LaborCode3

### Fields

| Field | Type |
|------|------|
| `laborCategoryId` | `string` |
| `laborCodeId` | `string` |
