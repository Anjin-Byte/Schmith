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
| `sender` | `SignatureProcessNestedSenderSender` |
| `signers` | `SignatureProcessSignersSignersNestedItem[]` |
| `document_organizations` | `SignatureProcessOrganizationsDocumentOrganizationsNestedItem[]` |

### Nested Types
- `MetaDataBase`
- `SignatureProcessNestedSenderSender`
- `SignatureProcessOrganizationsDocumentOrganizationsNestedItem`
- `SignatureProcessSignersSignersNestedItem`
- `SignatureProcessStateState`
- `SignerState`

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

## SignatureProcessNestedSenderSender
- Role: nested
- Parent: SignatureProcessFullDataObject
- Schema Name: SignatureProcessNestedSenderSender
- Schema ID: schema:anon/2eda0077944596f5a8508bfdd7980efbb51b5678
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `first_name` | `string` |
| `last_name` | `string` |

## SignatureProcessOrganizationsDocumentOrganizationsNestedItem
- Role: nested
- Parent: SignatureProcessFullDataObject
- Schema Name: SignatureProcessOrganizationsDocumentOrganizationsNestedItem
- Schema ID: schema:anon/4424aa26b85dd20ae1ca81506c7322cef8e82281
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |

## SignatureProcessSignersSignersNestedItem
- Role: nested
- Parent: SignatureProcessFullDataObject
- Schema Name: SignatureProcessSignersSignersNestedItem
- Schema ID: schema:anon/ffa305924e481b1c8132496caf32364f1bddbc9f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `first_name` | `string` |
| `last_name` | `string` |
| `state` | `SignerState` |

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
