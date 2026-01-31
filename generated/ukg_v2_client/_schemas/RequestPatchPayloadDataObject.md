# RequestPatchPayloadDataObject

## RequestPatchPayloadDataObject
- Role: parent
- Schema Name: RequestPatchPayload
- Schema ID: schema:definitions/RequestPatchPayload

### Fields

| Field | Type |
|------|------|
| `form_data` | `RequestFormDataFieldValue[]` |

### Nested Types
- `RequestFormDataFieldValue`

## RequestFormDataFieldValue
- Role: nested
- Parent: RequestPatchPayloadDataObject
- Schema Name: RequestFormDataFieldValue
- Schema ID: schema:definitions/RequestFormDataFieldValue
- Primary Key: FieldId

### Fields

| Field | Type |
|------|------|
| `field_id` | `string` |
| `values` | `string[]` |
