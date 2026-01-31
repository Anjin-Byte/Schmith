# EmployeePunchDataObject

## EmployeePunchDataObject
- Role: parent
- Schema Name: EmployeePunch
- Schema ID: schema:components/EmployeePunch
- Primary Key: Employeeid

### Fields
- `employeeId`: `string`
- `departmentId`: `string`
- `punchDateTime`: `string`
- `punchStatusType`: `PunchStatusType`
- `activityTypeId`: `string`
- `isTransfer`: `bool`
- `note`: `string`
- `laborCodes`: `LaborCode3[]`
- `workLocationId`: `string`

### Nested Types
- `LaborCode3`

## LaborCode3
- Role: nested
- Parent: EmployeePunchDataObject
- Schema Name: LaborCode3
- Schema ID: schema:components/LaborCode3

### Fields
- `laborCategoryId`: `string`
- `laborCodeId`: `string`
