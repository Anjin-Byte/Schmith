# CompanyDocumentUpdatePayloadDataObject

## CompanyDocumentUpdatePayloadDataObject
- Role: parent
- Schema Name: CompanyDocumentUpdatePayload
- Schema ID: schema:definitions/CompanyDocumentUpdatePayload
- Primary Key: DocumentTypeId

### Fields

| Field | Type |
|------|------|
| `document_type_id` | `string` |
| `title` | `string` |
| `date` | `string` |
| `organization_ids` | `string[]` |
| `metadata` | `MetaDataBase[]` |
| `external_reference` | `string` |

### Nested Types
- `MetaDataBase`

## MetaDataBase
- Role: nested
- Parent: CompanyDocumentUpdatePayloadDataObject
- Schema Name: MetaDataBase
- Schema ID: schema:definitions/MetaDataBase

### Fields

| Field | Type |
|------|------|
| `code` | `string` |
| `value` | `string` |
