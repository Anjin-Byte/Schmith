# SignatureProcessFullDataObject

## SignatureProcessFullDataObject
- Role: parent
- Schema Name: SignatureProcessFull
- Schema ID: schema:definitions/SignatureProcessFull
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
| `id` | `string` |
| `state` | `StateEnum` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `sender` | `object` |
| `signers` | `object[]` |
| `document_organizations` | `object[]` |
