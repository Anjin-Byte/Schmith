# EmployeePunch2DataObject

## EmployeePunch2DataObject
- Role: parent
- Schema Name: EmployeePunch2
- Schema ID: schema:components/EmployeePunch2

### Fields
- `punchId`: `string`
- `punchRefId`: `string`
- `punchDateTime`: `string`
- `punchStatusType`: `PunchStatusType`
- `isTransfer`: `bool`
- `activityTypeId`: `string`
- `departmentId`: `string`
- `note`: `string`
- `laborCodes`: `LaborCode3[]`
- `workLocationId`: `string`

### Nested Types
- `LaborCode3`

## LaborCode3
- Role: nested
- Parent: EmployeePunch2DataObject
- Schema Name: LaborCode3
- Schema ID: schema:components/LaborCode3

### Fields
- `laborCategoryId`: `string`
- `laborCodeId`: `string`
