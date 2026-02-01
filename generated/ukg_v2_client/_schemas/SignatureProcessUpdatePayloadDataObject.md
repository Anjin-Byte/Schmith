# SignatureProcessUpdatePayloadDataObject

## SignatureProcessUpdatePayloadDataObject
- Role: parent
- Schema Name: SignatureProcessUpdatePayload
- Schema ID: schema:definitions/SignatureProcessUpdatePayload
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
| `state` | `SignatureProcessStateState` |
| `sender_id` | `string` |
| `document_organization_ids` | `string[]` |
| `upload_id` | `string` |

### Nested Types
- `MetaDataBase`
- `SignatureProcessStateState`

## MetaDataBase
- Role: nested
- Parent: SignatureProcessUpdatePayloadDataObject
- Schema Name: MetaDataBase
- Schema ID: schema:definitions/MetaDataBase

### Fields

| Field | Type |
|------|------|
| `code` | `string` |
| `value` | `string` |

## SignatureProcessStateState
- Role: nested
- Parent: SignatureProcessUpdatePayloadDataObject
- Schema Name: SignatureProcessStateState
- Schema ID: schema:anon/2fcab3527a3bca80b6d200978e58b5e325e792e4

### Enum

Values: draft, signing, signed, sending, done, expired, rejected, error, canceled, id_check_failed
