# DocGenTemplateVersionUpdatePayloadDataObject

## DocGenTemplateVersionUpdatePayloadDataObject
- Role: parent
- Schema Name: DocGenTemplateVersionUpdatePayload
- Schema ID: schema:definitions/DocGenTemplateVersionUpdatePayload

### Fields

| Field | Type |
|------|------|
| `format` | `FormatEnum` |
| `output_format` | `OutputFormatPatchRequest` |
| `syntax_version` | `SyntaxVersionEnum` |
| `template_information` | `GenerationInfo[]` |
| `fragment_mapping` | `FragmentFieldsetField[]` |

### Nested Types
- `FragmentFieldsetField`
- `GenerationInfo`
- `OutputFormatPatchRequest`

## FragmentFieldsetField
- Role: nested
- Parent: DocGenTemplateVersionUpdatePayloadDataObject
- Schema Name: FragmentFieldsetField
- Schema ID: schema:definitions/FragmentFieldsetField
- Primary Key: Slug

### Fields

| Field | Type |
|------|------|
| `slug` | `string` |
| `fragment_id` | `string` |

## GenerationInfo
- Role: nested
- Parent: DocGenTemplateVersionUpdatePayloadDataObject
- Schema Name: GenerationInfo
- Schema ID: schema:definitions/GenerationInfo

### Fields

| Field | Type |
|------|------|
| `code` | `string` |
| `field` | `string` |
| `message` | `string` |
| `severity` | `SeverityEnum` |

## OutputFormatPatchRequest
- Role: nested
- Parent: DocGenTemplateVersionUpdatePayloadDataObject
- Schema Name: OutputFormatPatchRequest
- Schema ID: schema:definitions/OutputFormatPatchRequest

### Fields

| Field | Type |
|------|------|
| `format` | `FormatEnum` |
