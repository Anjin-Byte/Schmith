# SignatureProcessCreatePayloadDataObject

## SignatureProcessCreatePayloadDataObject
- Role: parent
- Schema Name: SignatureProcessCreatePayload
- Schema ID: schema:definitions/SignatureProcessCreatePayload
- Primary Key: SignatureTypeId

### Fields

| Field | Type |
|------|------|
| `signature_type_id` | `string` |
| `title` | `string` |
| `name` | `string` |
| `location` | `string` |
| `expiry_date` | `string` |
| `notify_on_signature` | `bool` |
| `notify_on_refusal` | `bool` |
| `document_type_id` | `string` |
| `document_metadata` | `MetaDataBase[]` |
| `document_date` | `string` |
| `cancellation_comment` | `string` |
| `file_number` | `string` |
| `is_cancelable` | `bool` |
| `is_deletable` | `bool` |
| `message` | `string` |
| `notify_employee_ids` | `string[]` |
| `external_id` | `string` |
| `auto_send` | `string` |
| `callback_url` | `string` |
| `reason` | `string` |
| `sender_id` | `string` |
| `document_organization_ids` | `string[]` |
| `upload_id` | `string` |

### Nested Types
- `MetaDataBase`

## MetaDataBase
- Role: nested
- Parent: SignatureProcessCreatePayloadDataObject
- Schema Name: MetaDataBase
- Schema ID: schema:definitions/MetaDataBase

### Fields

| Field | Type |
|------|------|
| `code` | `string` |
| `value` | `string` |
