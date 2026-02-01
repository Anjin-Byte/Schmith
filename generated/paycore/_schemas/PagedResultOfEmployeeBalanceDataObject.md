# PagedResultOfEmployeeBalanceDataObject

## PagedResultOfEmployeeBalanceDataObject
- Role: parent
- Schema Name: PagedResultOfEmployeeBalance
- Schema ID: schema:components/PagedResultOfEmployeeBalance

### Fields

| Field | Type |
|------|------|
| `hasMoreResults` | `bool` |
| `continuationToken` | `string` |
| `additionalResultsUrl` | `string` |
| `records` | `EmployeeBalance[]` |

### Nested Types
- `EarningCodeLight`
- `EmployeeBalance`
- `TypeBalance`

## EarningCodeLight
- Role: nested
- Parent: PagedResultOfEmployeeBalanceDataObject
- Schema Name: EarningCodeLight
- Schema ID: schema:components/EarningCodeLight
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `legalEntityId` | `string` |
| `tenantId` | `int` |
| `code` | `string` |
| `description` | `string` |
| `effectiveStartDate` | `string` |
| `effectiveEndDate` | `string` |

## EmployeeBalance
- Role: nested
- Parent: PagedResultOfEmployeeBalanceDataObject
- Schema Name: EmployeeBalance
- Schema ID: schema:components/EmployeeBalance

### Fields

| Field | Type |
|------|------|
| `employeeName` | `string` |
| `employeeNumber` | `string` |
| `employeeId` | `string` |
| `typeBalances` | `TypeBalance[]` |

## TypeBalance
- Role: nested
- Parent: PagedResultOfEmployeeBalanceDataObject
- Schema Name: TypeBalance
- Schema ID: schema:components/TypeBalance

### Fields

| Field | Type |
|------|------|
| `timeOffPlanName` | `string` |
| `timeOffTypeId` | `string` |
| `timeOffTypeCode` | `string` |
| `timeOffTypeName` | `string` |
| `activityStartDate` | `string` |
| `activityEndDate` | `string` |
| `currentBalance` | `double` |
| `accruedBalance` | `double` |
| `usedBalance` | `double` |
| `scheduledBalance` | `double` |
| `defaultEarning` | `EarningCodeLight` |
