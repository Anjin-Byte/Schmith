# EmployeeDocumentFullDataObject

## EmployeeDocumentFullDataObject
- Role: parent
- Schema Name: EmployeeDocumentFull
- Schema ID: schema:definitions/EmployeeDocumentFull
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `employee_id` | `string` |
| `employee_external_id` | `string` |
| `document_type_id` | `string` |
| `title` | `string` |
| `date` | `string` |
| `organization_ids` | `string[]` |
| `metadata` | `MetaDataBase[]` |
| `external_reference` | `string` |
| `id` | `string` |
| `origin` | `EmployeeDocumentComputedFieldsOrigin` |
| `origin_details` | `EmployeeDocumentComputedFieldsOriginDetails` |
| `sender_id` | `string` |
| `name` | `string` |
| `trashed` | `bool` |
| `expired` | `bool` |
| `expiry_date` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `code` | `string` |
| `value` | `string` |
| `label` | `string` |

### Nested Types
- `EmployeeDocumentComputedFieldsOrigin`
- `EmployeeDocumentComputedFieldsOriginDetails`
- `MetaDataBase`

## EmployeeDocumentComputedFieldsOrigin
- Role: nested
- Parent: EmployeeDocumentFullDataObject
- Schema Name: EmployeeDocumentComputedFieldsOrigin
- Schema ID: schema:anon/da2408f83f2afd3b041ed3f588208b3d92fe7080

### Enum

Values: api, distribution, doc_management, mass_mailing, signature, web

## EmployeeDocumentComputedFieldsOriginDetails
- Role: nested
- Parent: EmployeeDocumentFullDataObject
- Schema Name: EmployeeDocumentComputedFieldsOriginDetails
- Schema ID: schema:anon/8431fe4a00b2656a6bbf17e3bdb1b278a8abec19

### Enum

Values: drop_in_vault, employee, mass_mailing, signature, user

## MetaDataBase
- Role: nested
- Parent: EmployeeDocumentFullDataObject
- Schema Name: MetaDataBase
- Schema ID: schema:definitions/MetaDataBase

### Fields

| Field | Type |
|------|------|
| `code` | `string` |
| `value` | `string` |
