# CompanyDocumentFullDataObject

## CompanyDocumentFullDataObject
- Role: parent
- Schema Name: CompanyDocumentFull
- Schema ID: schema:definitions/CompanyDocumentFull
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `document_type_id` | `string` |
| `title` | `string` |
| `date` | `string` |
| `organization_ids` | `string[]` |
| `metadata` | `MetaDataBase[]` |
| `external_reference` | `string` |
| `id` | `string` |
| `name` | `string` |
| `origin` | `CompanyDocumentComputedFieldsOrigin` |
| `origin_details` | `CompanyDocumentComputedFieldsOriginDetails` |
| `sender_id` | `string` |
| `trashed` | `bool` |
| `expired` | `bool` |
| `expiry_date` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |

### Nested Types
- `CompanyDocumentComputedFieldsOrigin`
- `CompanyDocumentComputedFieldsOriginDetails`
- `MetaDataBase`

## CompanyDocumentComputedFieldsOrigin
- Role: nested
- Parent: CompanyDocumentFullDataObject
- Schema Name: CompanyDocumentComputedFieldsOrigin
- Schema ID: schema:anon/cadbfbddfd821060b2551746f93be6daaba3e372

### Enum

Values: api, doc_management, mass_mailing, web

## CompanyDocumentComputedFieldsOriginDetails
- Role: nested
- Parent: CompanyDocumentFullDataObject
- Schema Name: CompanyDocumentComputedFieldsOriginDetails
- Schema ID: schema:anon/ce12bec151cb5a7977620d36961eb985d5a7f529

### Enum

Values: mass_mailing, user

## MetaDataBase
- Role: nested
- Parent: CompanyDocumentFullDataObject
- Schema Name: MetaDataBase
- Schema ID: schema:definitions/MetaDataBase

### Fields

| Field | Type |
|------|------|
| `code` | `string` |
| `value` | `string` |
