# PagedResultOfTimeOffPlanDataObject

## PagedResultOfTimeOffPlanDataObject
- Role: parent
- Schema Name: PagedResultOfTimeOffPlan
- Schema ID: schema:components/PagedResultOfTimeOffPlan

### Fields

| Field | Type |
|------|------|
| `hasMoreResults` | `bool` |
| `continuationToken` | `string` |
| `additionalResultsUrl` | `string` |
| `records` | `TimeOffPlan[]` |

### Nested Types
- `TimeOffPlan`

## TimeOffPlan
- Role: nested
- Parent: PagedResultOfTimeOffPlanDataObject
- Schema Name: TimeOffPlan
- Schema ID: schema:components/TimeOffPlan

### Fields

| Field | Type |
|------|------|
| `timeOffPlanId` | `string` |
| `timeOffPlanName` | `string` |
| `timeOffTypeId` | `string` |
| `tenantId` | `int` |
