# PagedResultOfScheduleGroupDataObject

## PagedResultOfScheduleGroupDataObject
- Role: parent
- Schema Name: PagedResultOfScheduleGroup
- Schema ID: schema:components/PagedResultOfScheduleGroup

### Fields

| Field | Type |
|------|------|
| `hasMoreResults` | `bool` |
| `continuationToken` | `string` |
| `additionalResultsUrl` | `string` |
| `records` | `ScheduleGroup[]` |

### Nested Types
- `ScheduleGroup`

## ScheduleGroup
- Role: nested
- Parent: PagedResultOfScheduleGroupDataObject
- Schema Name: ScheduleGroup
- Schema ID: schema:components/ScheduleGroup

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |
| `isActive` | `bool` |
