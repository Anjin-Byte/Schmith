# EmployeeDocumentCreatePayloadDataObject

## EmployeeDocumentCreatePayloadDataObject
- Role: parent
- Schema Name: EmployeeDocumentCreatePayload
- Schema ID: schema:definitions/EmployeeDocumentCreatePayload
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
| `uploaded_file` | `DocumentFileId` |

### Nested Types
- `DocumentFileId`
- `MetaDataBase`

## DocumentFileId
- Role: nested
- Parent: EmployeeDocumentCreatePayloadDataObject
- Schema Name: DocumentFileId
- Schema ID: schema:definitions/DocumentFileId
- Primary Key: FileId

### Fields

| Field | Type |
|------|------|
| `filename` | `string` |
| `file_id` | `string` |

## MetaDataBase
- Role: nested
- Parent: EmployeeDocumentCreatePayloadDataObject
- Schema Name: MetaDataBase
- Schema ID: schema:definitions/MetaDataBase

### Fields

| Field | Type |
|------|------|
| `code` | `string` |
| `value` | `string` |
