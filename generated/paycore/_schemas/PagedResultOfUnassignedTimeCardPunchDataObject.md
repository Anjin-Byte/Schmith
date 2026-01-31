# PagedResultOfUnassignedTimeCardPunchDataObject

## PagedResultOfUnassignedTimeCardPunchDataObject
- Role: parent
- Schema Name: PagedResultOfUnassignedTimeCardPunch
- Schema ID: schema:components/PagedResultOfUnassignedTimeCardPunch

### Fields

| Field | Type |
|------|------|
| `hasMoreResults` | `bool` |
| `continuationToken` | `string` |
| `additionalResultsUrl` | `string` |
| `records` | `UnassignedTimeCardPunch[]` |

### Nested Types
- `UnassignedTimeCardPunch`

## UnassignedTimeCardPunch
- Role: nested
- Parent: PagedResultOfUnassignedTimeCardPunchDataObject
- Schema Name: UnassignedTimeCardPunch
- Schema ID: schema:components/UnassignedTimeCardPunch

### Fields

| Field | Type |
|------|------|
| `punchId` | `string` |
| `badgeNumber` | `int` |
| `employeeId` | `string` |
| `punchDateTime` | `string` |
| `departmentId` | `string` |
| `reason` | `string` |
| `activityTypeName` | `string` |
| `activityTypeId` | `string` |
| `workLocationId` | `string` |
