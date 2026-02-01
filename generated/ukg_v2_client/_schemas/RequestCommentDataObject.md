# RequestCommentDataObject

## RequestCommentDataObject
- Role: parent
- Schema Name: RequestComment
- Schema ID: schema:definitions/RequestComment
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `creator` | `UserSimplified` |
| `creator_id` | `string` |
| `created_at` | `string` |
| `content` | `string` |
| `is_informative` | `bool` |
| `is_internal` | `bool` |
| `comment_source` | `string` |
| `is_deleted` | `bool` |
| `attachments` | `RequestAttachment[]` |

### Nested Types
- `RequestAttachment`
- `UserSimplified`

## RequestAttachment
- Role: nested
- Parent: RequestCommentDataObject
- Schema Name: RequestAttachment
- Schema ID: schema:definitions/RequestAttachment
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |

## UserSimplified
- Role: nested
- Parent: RequestCommentDataObject
- Schema Name: UserSimplified
- Schema ID: schema:definitions/UserSimplified
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `firstname` | `string` |
| `lastname` | `string` |
| `email` | `string` |
| `external_id` | `string` |
