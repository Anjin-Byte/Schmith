# RestV10TodosPostResponse201DataObject

## RestV10TodosPostResponse201DataObject
- Role: parent
- Schema Name: RestV10TodosPostResponse201
- Schema ID: schema:anon/89b0e6d4509db735673e9b924d9442472575e9ab
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `assignment` | `RestV10TodosPostResponse201Assignment` |
| `color` | `string` |
| `created_by` | `RestV10TodosPostResponse201Assignment` |
| `description` | `string` |
| `finish_datetime` | `string` |
| `full_outline_path` | `string` |
| `milestone` | `bool` |
| `name` | `string` |
| `percentage` | `int` |
| `private` | `bool` |
| `start_datetime` | `string` |
| `task_name` | `string` |
| `updated_at` | `string` |

### Nested Types
- `RestV10TodosPostResponse201Assignment`

## RestV10TodosPostResponse201Assignment
- Role: nested
- Parent: RestV10TodosPostResponse201DataObject
- Schema Name: RestV10TodosPostResponse201Assignment
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |
