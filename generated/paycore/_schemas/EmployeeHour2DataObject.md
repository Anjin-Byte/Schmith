# EmployeeHour2DataObject

## EmployeeHour2DataObject
- Role: parent
- Schema Name: EmployeeHour2
- Schema ID: schema:components/EmployeeHour2

### Fields
- `hourId`: `string`
- `legalEntityEarningId`: `string`
- `departmentId`: `string`
- `startDateTime`: `string`
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
- Parent: EmployeeHour2DataObject
- Schema Name: LaborCodeV3
- Schema ID: schema:components/LaborCodeV3

### Fields
- `laborCategoryId`: `string`
- `laborCodeId`: `string`
