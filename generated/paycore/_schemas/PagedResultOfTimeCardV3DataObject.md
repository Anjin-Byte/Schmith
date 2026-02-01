# PagedResultOfTimeCardV3DataObject

## PagedResultOfTimeCardV3DataObject
- Role: parent
- Schema Name: PagedResultOfTimeCardV3
- Schema ID: schema:components/PagedResultOfTimeCardV3

### Fields

| Field | Type |
|------|------|
| `hasMoreResults` | `bool` |
| `continuationToken` | `string` |
| `additionalResultsUrl` | `string` |
| `records` | `TimeCardV3[]` |

### Nested Types
- `LaborCodeV2`
- `TimeCardV3`

## LaborCodeV2
- Role: nested
- Parent: PagedResultOfTimeCardV3DataObject
- Schema Name: LaborCodeV2
- Schema ID: schema:components/LaborCodeV2

### Fields

| Field | Type |
|------|------|
| `laborCategoryLevel` | `int` |
| `laborCode` | `string` |
| `laborCodeName` | `string` |

## TimeCardV3
- Role: nested
- Parent: PagedResultOfTimeCardV3DataObject
- Schema Name: TimeCardV3
- Schema ID: schema:components/TimeCardV3

### Fields

| Field | Type |
|------|------|
| `employeeId` | `string` |
| `badgeNumber` | `int` |
| `displayDate` | `string` |
| `punchIn` | `string` |
| `punchOut` | `string` |
| `hourAmount` | `double` |
| `departmentCode` | `int` |
| `departmentName` | `string` |
| `earningCode` | `string` |
| `estimatedGrossPay` | `double` |
| `laborCodes` | `LaborCodeV2[]` |
