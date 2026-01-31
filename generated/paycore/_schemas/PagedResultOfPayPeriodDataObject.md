# PagedResultOfPayPeriodDataObject

## PagedResultOfPayPeriodDataObject
- Role: parent
- Schema Name: PagedResultOfPayPeriod
- Schema ID: schema:components/PagedResultOfPayPeriod

### Fields

| Field | Type |
|------|------|
| `hasMoreResults` | `bool` |
| `continuationToken` | `string` |
| `additionalResultsUrl` | `string` |
| `records` | `PayPeriod[]` |

### Nested Types
- `PayPeriod`

## PayPeriod
- Role: nested
- Parent: PagedResultOfPayPeriodDataObject
- Schema Name: PayPeriod
- Schema ID: schema:components/PayPeriod

### Fields

| Field | Type |
|------|------|
| `periodStartDate` | `string` |
| `periodEndDate` | `string` |
| `checkDate` | `string` |
| `processDate` | `string` |
| `plannerId` | `string` |
| `payrollStatus` | `PayrollStatus` |
