# DocGenTemplateVersionDataObject

## DocGenTemplateVersionDataObject
- Role: parent
- Schema Name: DocGenTemplateVersion
- Schema ID: schema:definitions/DocGenTemplateVersion
- Primary Key: DocumentGenerationTemplateId

### Fields

| Field | Type |
|------|------|
| `created_at` | `string` |
| `updated_at` | `string` |
| `version` | `int` |
| `document_generation_template_id` | `string` |
| `syntax_version` | `DocGenTemplateVersionNestedSyntaxVersion` |
| `format` | `DocGenTemplateVersionNestedFormat` |
| `output_format` | `OutputFormatResponse` |
| `template_information` | `GenerationInfo[]` |
| `fragment_mapping` | `FragmentFieldsetField[]` |

### Nested Types
- `DocGenTemplateVersionNestedFormat`
- `DocGenTemplateVersionNestedSyntaxVersion`
- `FragmentFieldsetField`
- `GenerationInfo`
- `GenerationInfoSeverityItem`
- `OutputFormatResponse`
- `OutputFormatResponseFormat`

## DocGenTemplateVersionNestedFormat
- Role: nested
- Parent: DocGenTemplateVersionDataObject
- Schema Name: DocGenTemplateVersionNestedFormat
- Schema ID: schema:anon/e3cd8861cef5df5d102527143fa24cd1c5df9928

### Enum

Values: DOCX, PDF, DOC, ODT, UNKNOWN

## DocGenTemplateVersionNestedSyntaxVersion
- Role: nested
- Parent: DocGenTemplateVersionDataObject
- Schema Name: DocGenTemplateVersionNestedSyntaxVersion
- Schema ID: schema:anon/8d85afe60184732869114b50fe8771f6f97ba872

### Enum

Values: V1, V2

## FragmentFieldsetField
- Role: nested
- Parent: DocGenTemplateVersionDataObject
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
- Parent: DocGenTemplateVersionDataObject
- Schema Name: GenerationInfo
- Schema ID: schema:definitions/GenerationInfo

### Fields

| Field | Type |
|------|------|
| `code` | `string` |
| `field` | `string` |
| `message` | `string` |
| `severity` | `GenerationInfoSeverityItem` |

## GenerationInfoSeverityItem
- Role: nested
- Parent: DocGenTemplateVersionDataObject
- Schema Name: GenerationInfoSeverityItem
- Schema ID: schema:anon/4bc512f0c93de388afdbd8a134f1b285fb86a137

### Enum

Values: ERROR, WARNING

## OutputFormatResponse
- Role: nested
- Parent: DocGenTemplateVersionDataObject
- Schema Name: OutputFormatResponse
- Schema ID: schema:definitions/OutputFormatResponse

### Fields

| Field | Type |
|------|------|
| `format` | `OutputFormatResponseFormat` |

## OutputFormatResponseFormat
- Role: nested
- Parent: DocGenTemplateVersionDataObject
- Schema Name: OutputFormatResponseFormat
- Schema ID: schema:anon/93d66a5bdaa8c1afcaa76ed31fae31467a605c6e

### Enum

Values: DOC, DOCX, ODT, PDF
