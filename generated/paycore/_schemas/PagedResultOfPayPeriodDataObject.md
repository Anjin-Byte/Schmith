# PagedResultOfPayPeriodDataObject

## PagedResultOfPayPeriodDataObject
- Role: parent
- Schema Name: PagedResultOfPayPeriod
- Schema ID: schema:components/PagedResultOfPayPeriod

### Fields
- `hasMoreResults`: `bool`
- `continuationToken`: `string`
- `additionalResultsUrl`: `string`
- `records`: `PayPeriod[]`

### Nested Types
- `PayPeriod`

## PayPeriod
- Role: nested
- Parent: PagedResultOfPayPeriodDataObject
- Schema Name: PayPeriod
- Schema ID: schema:components/PayPeriod

### Fields
- `periodStartDate`: `string`
- `periodEndDate`: `string`
- `checkDate`: `string`
- `processDate`: `string`
- `plannerId`: `string`
- `payrollStatus`: `PayrollStatus`
