# EmployeeHour3DataObject

## EmployeeHour3DataObject
- Role: parent
- Schema Name: EmployeeHour3
- Schema ID: schema:components/EmployeeHour3
- Primary Key: Hourid

### Fields
- `hourId`: `string`
- `legalEntityEarningId`: `string`
- `departmentId`: `string`
- `total`: `double`
- `note`: `string`
- `activityTypeId`: `string`
- `hourRefId`: `string`
- `laborCodes`: `LaborCodeV3[]`
- `workLocationId`: `string`

### Nested Types
- `LaborCodeV3`

## LaborCodeV3
- Role: nested
- Parent: EmployeeHour3DataObject
- Schema Name: LaborCodeV3
- Schema ID: schema:components/LaborCodeV3

### Fields
- `laborCategoryId`: `string`
- `laborCodeId`: `string`
