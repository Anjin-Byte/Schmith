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
| `status` | `StatusEnum` |
| `error_code` | `string` |
| `started_at` | `string` |
| `completed_at` | `string` |
| `guessed_document_types` | `DocumentTypePredictionResult[]` |
| `created_at` | `string` |
| `updated_at` | `string` |
