# PagedResultOfTimeOffTypeDataObject

## PagedResultOfTimeOffTypeDataObject
- Role: parent
- Schema Name: PagedResultOfTimeOffType
- Schema ID: schema:components/PagedResultOfTimeOffType

### Fields

| Field | Type |
|------|------|
| `hasMoreResults` | `bool` |
| `continuationToken` | `string` |
| `additionalResultsUrl` | `string` |
| `records` | `TimeOffType[]` |

### Nested Types
- `TimeOffType`

## TimeOffType
- Role: nested
- Parent: PagedResultOfTimeOffTypeDataObject
- Schema Name: TimeOffType
- Schema ID: schema:components/TimeOffType
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |
| `code` | `string` |
