# InboxItemCreatePayloadDataObject

## InboxItemCreatePayloadDataObject
- Role: parent
- Schema Name: InboxItemCreatePayload
- Schema ID: schema:definitions/InboxItemCreatePayload
- Primary Key: ToInboxId

### Fields

| Field | Type |
|------|------|
| `title` | `string` |
| `type` | `string` |
| `description` | `string` |
| `creator_email` | `string` |
| `to_users_ids` | `string[]` |
| `to_inbox_id` | `string` |
| `options` | `InboxItemCreatePayloadNestedOptions` |
| `uploaded_files` | `DocumentFileId[]` |

### Nested Types
- `DocumentFileId`
- `InboxItemCreatePayloadNestedOptions`

## DocumentFileId
- Role: nested
- Parent: InboxItemCreatePayloadDataObject
- Schema Name: DocumentFileId
- Schema ID: schema:definitions/DocumentFileId
- Primary Key: FileId

### Fields

| Field | Type |
|------|------|
| `filename` | `string` |
| `file_id` | `string` |

## InboxItemCreatePayloadNestedOptions
- Role: nested
- Parent: InboxItemCreatePayloadDataObject
- Schema Name: InboxItemCreatePayloadNestedOptions
- Schema ID: schema:anon/8e1baff229e157c5821a557c2623b7613f6d833a

### Fields

| Field | Type |
|------|------|
| `send_confirmation_email_to_creator` | `bool` |
