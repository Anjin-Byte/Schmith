# RestV10ProjectsProjectIdDailyLogHeadersGetResponse200DataObject

## RestV10ProjectsProjectIdDailyLogHeadersGetResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdDailyLogHeadersGetResponse200
- Schema ID: schema:anon/e4af7b6e8df7b720183814669bf014f74f7cdbce
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `log_date` | `string` |
| `log_datetime` | `string` |
| `completed` | `bool` |
| `completed_by` | `RestV10ProjectsProjectIdDailyLogHeadersGetResponse200CompletedBy` |
| `completed_at` | `string` |
| `completable` | `bool` |
| `distributed` | `bool` |
| `distributed_by` | `RestV10ProjectsProjectIdDailyLogHeadersGetResponse200CompletedBy` |
| `distributed_at` | `string` |
| `distributable` | `bool` |

### Nested Types
- `RestV10ProjectsProjectIdDailyLogHeadersGetResponse200CompletedBy`

## RestV10ProjectsProjectIdDailyLogHeadersGetResponse200CompletedBy
- Role: nested
- Parent: RestV10ProjectsProjectIdDailyLogHeadersGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDailyLogHeadersGetResponse200CompletedBy
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |
