# EmployeeDocumentUpdatePayloadDataObject

## EmployeeDocumentUpdatePayloadDataObject
- Role: parent
- Schema Name: EmployeeDocumentUpdatePayload
- Schema ID: schema:definitions/EmployeeDocumentUpdatePayload
- Primary Key: EmployeeId

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
| `external_reference_is_unique` | `bool` |

### Nested Types
- `MetaDataBase`

## MetaDataBase
- Role: nested
- Parent: EmployeeDocumentUpdatePayloadDataObject
- Schema Name: MetaDataBase
- Schema ID: schema:definitions/MetaDataBase

### Fields

| Field | Type |
|------|------|
| `code` | `string` |
| `value` | `string` |
