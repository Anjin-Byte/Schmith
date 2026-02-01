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
- `OutputFormatPatchRequestFormat`

## FragmentFieldsetField
- Role: nested
- Parent: DocgenTemplateVersionPatchPayloadDataObject
- Schema Name: FragmentFieldsetField
- Schema ID: schema:definitions/FragmentFieldsetField
- Primary Key: FragmentId

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
| `format` | `OutputFormatPatchRequestFormat` |

## OutputFormatPatchRequestFormat
- Role: nested
- Parent: DocgenTemplateVersionPatchPayloadDataObject
- Schema Name: OutputFormatPatchRequestFormat
- Schema ID: schema:anon/0811d6e7055431074ebf9eb0d3986ae92377bd06

### Enum

Values: DOC, DOCX, ODT, PDF
