# RestV10PunchItemsIdCommentsPostResponse201DataObject

## RestV10PunchItemsIdCommentsPostResponse201DataObject
- Role: parent
- Schema Name: RestV10PunchItemsIdCommentsPostResponse201
- Schema ID: schema:anon/d4960b2db5064571ae30694533e4b5272bd9d6b8
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `attachments` | `RestV10PunchItemsIdCommentsPostResponse201AttachmentsItem[]` |
| `body` | `string` |
| `created_at` | `string` |
| `created_by` | `RestV10PunchItemsIdCommentsPostResponse201CreatedBy` |
| `type` | `string` |

### Nested Types
- `RestV10PunchItemsIdCommentsPostResponse201AttachmentsItem`
- `RestV10PunchItemsIdCommentsPostResponse201CreatedBy`

## RestV10PunchItemsIdCommentsPostResponse201AttachmentsItem
- Role: nested
- Parent: RestV10PunchItemsIdCommentsPostResponse201DataObject
- Schema Name: RestV10PunchItemsIdCommentsPostResponse201AttachmentsItem
- Schema ID: schema:anon/8e7c05c6c17fa645c56cce4f0a26da7dd79c417e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `url` | `string` |
| `filename` | `string` |
| `thumbnail_url` | `string` |

## RestV10PunchItemsIdCommentsPostResponse201CreatedBy
- Role: nested
- Parent: RestV10PunchItemsIdCommentsPostResponse201DataObject
- Schema Name: RestV10PunchItemsIdCommentsPostResponse201CreatedBy
- Schema ID: schema:anon/796a6b5054a4efaa2e60caf60530a5ae8aa1d188
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `login` | `string` |
| `company_name` | `string` |
