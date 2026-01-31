# PagedResultOfPayItemDataObject

## PagedResultOfPayItemDataObject
- Role: parent
- Schema Name: PagedResultOfPayItem
- Schema ID: schema:components/PagedResultOfPayItem

### Fields
- `hasMoreResults`: `bool`
- `continuationToken`: `string`
- `additionalResultsUrl`: `string`
- `records`: `PayItem[]`

### Nested Types
- `LaborCode3`
- `PayItem`

## LaborCode3
- Role: nested
- Parent: PagedResultOfPayItemDataObject
- Schema Name: LaborCode3
- Schema ID: schema:components/LaborCode3

### Fields
- `laborCategoryId`: `string`
- `laborCodeId`: `string`

## PayItem
- Role: nested
- Parent: PagedResultOfPayItemDataObject
- Schema Name: PayItem
- Schema ID: schema:components/PayItem

### Fields
- `payItemId`: `string`
- `payItemRefId`: `string`
- `employeeId`: `string`
- `legalEntityEarningId`: `string`
- `amount`: `double`
- `departmentId`: `string`
- `note`: `string`
- `laborCodes`: `LaborCode3[]`
- `date`: `string`
- `workLocationId`: `string`
