# RestV10ProjectsProjectIdInspectionsInspectionIdCommentsPostResponse201DataObject

## RestV10ProjectsProjectIdInspectionsInspectionIdCommentsPostResponse201DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdInspectionsInspectionIdCommentsPostResponse201
- Schema ID: schema:anon/1da61f467d65e95d88ca36ecddf68e8228f8c02b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `body` | `string` |
| `item_id` | `int` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `created_by` | `RestV10ProjectsProjectIdInspectionsInspectionIdCommentsPostResponse201CreatedBy` |

### Nested Types
- `RestV10ProjectsProjectIdInspectionsInspectionIdCommentsPostResponse201CreatedBy`

## RestV10ProjectsProjectIdInspectionsInspectionIdCommentsPostResponse201CreatedBy
- Role: nested
- Parent: RestV10ProjectsProjectIdInspectionsInspectionIdCommentsPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdInspectionsInspectionIdCommentsPostResponse201CreatedBy
- Schema ID: schema:anon/67385da91d6062b1e9bede72679fdb0364034afa
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `company_name` | `string` |
| `login` | `string` |
| `name` | `string` |
