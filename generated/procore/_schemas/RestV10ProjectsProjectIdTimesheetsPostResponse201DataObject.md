# RestV10ProjectsProjectIdTimesheetsPostResponse201DataObject

## RestV10ProjectsProjectIdTimesheetsPostResponse201DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdTimesheetsPostResponse201
- Schema ID: schema:anon/f40043c0c093953dfe6202058c748868281658d4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `date` | `string` |
| `number` | `int` |
| `created_by` | `RestV10ProjectsProjectIdTimesheetsPostResponse201CreatedBy` |
| `name` | `string` |
| `status` | `string` |

### Nested Types
- `RestV10ProjectsProjectIdTimesheetsPostResponse201CreatedBy`

## RestV10ProjectsProjectIdTimesheetsPostResponse201CreatedBy
- Role: nested
- Parent: RestV10ProjectsProjectIdTimesheetsPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdTimesheetsPostResponse201CreatedBy
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |
