# DocGenFullDataObject

## DocGenFullDataObject
- Role: parent
- Schema Name: DocGenFull
- Schema ID: schema:definitions/DocGenFull
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `created_at` | `string` |
| `updated_at` | `string` |
| `id` | `string` |
| `format` | `DocGenFullNestedFormat` |
| `document_generation_template_id` | `string` |
| `document_generation_template_version` | `int` |
| `context` | `string` |
| `upload_id` | `string` |
| `status` | `DocGenFullNestedStatus` |
| `generation_started_at` | `string` |
| `generation_finished_at` | `string` |

### Nested Types
- `DocGenFullNestedFormat`
- `DocGenFullNestedStatus`

## DocGenFullNestedFormat
- Role: nested
- Parent: DocGenFullDataObject
- Schema Name: DocGenFullNestedFormat
- Schema ID: schema:anon/386e85ad5e7f2f45b9212196f4c3e52b99e44a75

### Enum

Values: DOCX, PDF, DOC, ODT, UNKNOWN

## DocGenFullNestedStatus
- Role: nested
- Parent: DocGenFullDataObject
- Schema Name: DocGenFullNestedStatus
- Schema ID: schema:anon/f525805553dcc19e30688085c33c2e08ee4c156a

### Enum

Values: GENERATED, NOT_GENERATED, GENERATING, FAILED, CANCELED
