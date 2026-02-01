# DocGenTemplateVersionUpdatePayloadDataObject

## DocGenTemplateVersionUpdatePayloadDataObject
- Role: parent
- Schema Name: DocGenTemplateVersionUpdatePayload
- Schema ID: schema:definitions/DocGenTemplateVersionUpdatePayload

### Fields

| Field | Type |
|------|------|
| `format` | `DocGenTemplateVersionUpdatePayloadFormat` |
| `output_format` | `OutputFormatPatchRequest` |
| `syntax_version` | `DocGenTemplateVersionUpdatePayloadSyntaxVersion` |
| `template_information` | `GenerationInfo[]` |
| `fragment_mapping` | `FragmentFieldsetField[]` |

### Nested Types
- `DocGenTemplateVersionUpdatePayloadFormat`
- `DocGenTemplateVersionUpdatePayloadSyntaxVersion`
- `FragmentFieldsetField`
- `GenerationInfo`
- `GenerationInfoSeverity`
- `OutputFormatPatchRequest`
- `OutputFormatPatchRequestFormat`

## DocGenTemplateVersionUpdatePayloadFormat
- Role: nested
- Parent: DocGenTemplateVersionUpdatePayloadDataObject
- Schema Name: DocGenTemplateVersionUpdatePayloadFormat
- Schema ID: schema:anon/e3cd8861cef5df5d102527143fa24cd1c5df9928

### Enum

Values: DOCX, PDF, DOC, ODT, UNKNOWN

## DocGenTemplateVersionUpdatePayloadSyntaxVersion
- Role: nested
- Parent: DocGenTemplateVersionUpdatePayloadDataObject
- Schema Name: DocGenTemplateVersionUpdatePayloadSyntaxVersion
- Schema ID: schema:anon/8d85afe60184732869114b50fe8771f6f97ba872

### Enum

Values: V1, V2

## FragmentFieldsetField
- Role: nested
- Parent: DocGenTemplateVersionUpdatePayloadDataObject
- Schema Name: FragmentFieldsetField
- Schema ID: schema:definitions/FragmentFieldsetField
- Primary Key: FragmentId

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
| `severity` | `GenerationInfoSeverity` |

## GenerationInfoSeverity
- Role: nested
- Parent: DocGenTemplateVersionUpdatePayloadDataObject
- Schema Name: GenerationInfoSeverity
- Schema ID: schema:anon/4bc512f0c93de388afdbd8a134f1b285fb86a137

### Enum

Values: ERROR, WARNING

## OutputFormatPatchRequest
- Role: nested
- Parent: DocGenTemplateVersionUpdatePayloadDataObject
- Schema Name: OutputFormatPatchRequest
- Schema ID: schema:definitions/OutputFormatPatchRequest

### Fields

| Field | Type |
|------|------|
| `format` | `OutputFormatPatchRequestFormat` |

## OutputFormatPatchRequestFormat
- Role: nested
- Parent: DocGenTemplateVersionUpdatePayloadDataObject
- Schema Name: OutputFormatPatchRequestFormat
- Schema ID: schema:anon/0811d6e7055431074ebf9eb0d3986ae92377bd06

### Enum

Values: DOC, DOCX, ODT, PDF
