# PayItem2DataObject

## PayItem2DataObject
- Role: parent
- Schema Name: PayItem2
- Schema ID: schema:components/PayItem2
- Primary Key: Employeeid

### Fields
- `employeeId`: `string`
- `legalEntityEarningId`: `string`
- `amount`: `double`
- `departmentId`: `string`
- `note`: `string`
- `laborCodes`: `LaborCode3[]`
- `date`: `string`
- `workLocationId`: `string`

### Nested Types
- `LaborCode3`

## LaborCode3
- Role: nested
- Parent: PayItem2DataObject
- Schema Name: LaborCode3
- Schema ID: schema:components/LaborCode3

### Fields
- `laborCategoryId`: `string`
- `laborCodeId`: `string`
