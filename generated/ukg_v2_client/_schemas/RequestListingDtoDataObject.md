# RequestListingDtoDataObject

## RequestListingDtoDataObject
- Role: parent
- Schema Name: RequestListingDto
- Schema ID: schema:definitions/RequestListingDto
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `status` | `RequestListingDtoStatus` |
| `title` | `string` |
| `created_at` | `string` |
| `generated_document_id` | `string` |
| `employee_id` | `string` |
| `employee_document_type_id` | `string` |
| `upload_id` | `string` |

### Nested Types
- `RequestListingDtoStatus`

## RequestListingDtoStatus
- Role: nested
- Parent: RequestListingDtoDataObject
- Schema Name: RequestListingDtoStatus
- Schema ID: schema:anon/7379e1388fa281105e6205ef776649cb5b861682

### Enum

Values: PROCESSED, NOT_PROCESSED, RECEIVED_ASYNC, SENT_ASYNC, FAILED
