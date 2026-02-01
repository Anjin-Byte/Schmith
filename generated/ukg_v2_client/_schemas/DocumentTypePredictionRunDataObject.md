# DocumentTypePredictionRunDataObject

## DocumentTypePredictionRunDataObject
- Role: parent
- Schema Name: DocumentTypePredictionRun
- Schema ID: schema:definitions/DocumentTypePredictionRun
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `document_id` | `int` |
| `id` | `string` |
| `status` | `_RunStatus` |
| `error_code` | `string` |
| `started_at` | `string` |
| `completed_at` | `string` |
| `guessed_document_types` | `DocumentTypePredictionResult[]` |
| `created_at` | `string` |
| `updated_at` | `string` |

### Nested Types
- `DocumentTypePredictionResult`
- `_RunStatus`

## DocumentTypePredictionResult
- Role: nested
- Parent: DocumentTypePredictionRunDataObject
- Schema Name: DocumentTypePredictionResult
- Schema ID: schema:definitions/DocumentTypePredictionResult
- Primary Key: DocumentTypeId

### Fields

| Field | Type |
|------|------|
| `document_type_id` | `string` |
| `probability` | `double` |

## _RunStatus
- Role: nested
- Parent: DocumentTypePredictionRunDataObject
- Schema Name: _RunStatus
- Schema ID: schema:anon/74af9ce652d5438531b418fef7e7f5f529ac55f2

### Enum

Values: SCHEDULED, IN_PROGRESS, DONE, FAILED
