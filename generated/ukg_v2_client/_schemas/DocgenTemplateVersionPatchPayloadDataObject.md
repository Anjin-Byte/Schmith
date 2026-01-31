# DocgenTemplateVersionPatchPayloadDataObject

## DocgenTemplateVersionPatchPayloadDataObject
- Role: parent
- Schema Name: DocgenTemplateVersionPatchPayload
- Schema ID: schema:definitions/DocgenTemplateVersionPatchPayload

### Fields

| Field | Type |
|------|------|
| `output_format` | `OutputFormatPatchRequest` |
| `fragment_mapping` | `FragmentFieldsetField[]` |

### Nested Types
- `FragmentFieldsetField`
- `OutputFormatPatchRequest`

## FragmentFieldsetField
- Role: nested
- Parent: DocgenTemplateVersionPatchPayloadDataObject
- Schema Name: FragmentFieldsetField
- Schema ID: schema:definitions/FragmentFieldsetField
- Primary Key: Slug

### Fields

| Field | Type |
|------|------|
| `slug` | `string` |
| `fragment_id` | `string` |

## OutputFormatPatchRequest
- Role: nested
- Parent: DocgenTemplateVersionPatchPayloadDataObject
- Schema Name: OutputFormatPatchRequest
- Schema ID: schema:definitions/OutputFormatPatchRequest

### Fields

| Field | Type |
|------|------|
| `format` | `FormatEnum` |
