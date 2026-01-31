# EmployeePunch4DataObject

## EmployeePunch4DataObject
- Role: parent
- Schema Name: EmployeePunch4
- Schema ID: schema:components/EmployeePunch4
- Primary Key: Punchid

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
- Parent: EmployeePunch4DataObject
- Schema Name: LaborCode3
- Schema ID: schema:components/LaborCode3

### Fields
- `laborCategoryId`: `string`
- `laborCodeId`: `string`
