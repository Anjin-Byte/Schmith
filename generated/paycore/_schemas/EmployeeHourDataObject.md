# EmployeeHourDataObject

## EmployeeHourDataObject
- Role: parent
- Schema Name: EmployeeHour
- Schema ID: schema:components/EmployeeHour
- Primary Key: Employeeid

### Fields

| Field | Type |
|------|------|
| `employeeId` | `string` |
| `departmentId` | `string` |
| `legalEntityEarningId` | `string` |
| `startDateTime` | `string` |
| `total` | `double` |
| `activityTypeId` | `string` |
| `applyAllPolicies` | `bool` |
| `note` | `string` |
| `laborCodes` | `LaborCode3[]` |
| `workLocationId` | `string` |

### Nested Types
- `LaborCode3`

## LaborCode3
- Role: nested
- Parent: EmployeeHourDataObject
- Schema Name: LaborCode3
- Schema ID: schema:components/LaborCode3

### Fields

| Field | Type |
|------|------|
| `laborCategoryId` | `string` |
| `laborCodeId` | `string` |
