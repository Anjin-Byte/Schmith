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
- `PayrollStatus`

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

## PayrollStatus
- Role: nested
- Parent: PagedResultOfPayPeriodDataObject
- Schema Name: PayrollStatus
- Schema ID: schema:components/PayrollStatus

### Enum

Values: B, D, E, H, I, P, R, S, W
Names: B, D, E, H, I, P, R, S, W
