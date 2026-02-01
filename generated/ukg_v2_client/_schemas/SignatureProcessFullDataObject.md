# SignatureProcessFullDataObject

## SignatureProcessFullDataObject
- Role: parent
- Schema Name: SignatureProcessFull
- Schema ID: schema:definitions/SignatureProcessFull
- Primary Key: Id

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
| `state` | `SignatureProcessStateState` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `sender` | `Anonymous_2eda0077` |
| `signers` | `Anonymous_ffa30592[]` |
| `document_organizations` | `Anonymous_4424aa26[]` |

### Nested Types
- `Anonymous_2eda0077`
- `Anonymous_4424aa26`
- `Anonymous_ffa30592`
- `MetaDataBase`
- `SignatureProcessStateState`
- `SignerState`

## Anonymous_2eda0077
- Role: nested
- Parent: SignatureProcessFullDataObject
- Schema Name: Anonymous_2eda0077
- Schema ID: schema:anon/2eda0077944596f5a8508bfdd7980efbb51b5678
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `first_name` | `string` |
| `last_name` | `string` |

## Anonymous_4424aa26
- Role: nested
- Parent: SignatureProcessFullDataObject
- Schema Name: Anonymous_4424aa26
- Schema ID: schema:anon/4424aa26b85dd20ae1ca81506c7322cef8e82281
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |

## Anonymous_ffa30592
- Role: nested
- Parent: SignatureProcessFullDataObject
- Schema Name: Anonymous_ffa30592
- Schema ID: schema:anon/ffa305924e481b1c8132496caf32364f1bddbc9f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `first_name` | `string` |
| `last_name` | `string` |
| `state` | `SignerState` |

## MetaDataBase
- Role: nested
- Parent: SignatureProcessFullDataObject
- Schema Name: MetaDataBase
- Schema ID: schema:definitions/MetaDataBase

### Fields

| Field | Type |
|------|------|
| `code` | `string` |
| `value` | `string` |

## SignatureProcessStateState
- Role: nested
- Parent: SignatureProcessFullDataObject
- Schema Name: SignatureProcessStateState
- Schema ID: schema:anon/2fcab3527a3bca80b6d200978e58b5e325e792e4

### Enum

Values: draft, signing, signed, sending, done, expired, rejected, error, canceled, id_check_failed

## SignerState
- Role: nested
- Parent: SignatureProcessFullDataObject
- Schema Name: SignerState
- Schema ID: schema:definitions/SignerState

### Enum

Values: pending, in_progress, signed, rejected, error, done, delivered, delayed
