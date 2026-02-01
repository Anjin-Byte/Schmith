# DocGenTemplateVersionFullDataObject

## DocGenTemplateVersionFullDataObject
- Role: parent
- Schema Name: DocGenTemplateVersionFull
- Schema ID: schema:definitions/DocGenTemplateVersionFull

### Fields

| Field | Type |
|------|------|
| `format` | `DocGenTemplateVersionBaseFormat` |
| `syntax_version` | `DocGenTemplateVersionBaseSyntaxVersion` |
| `template_information` | `GenerationInfo[]` |
| `fragment_mapping` | `FragmentFieldsetField[]` |
| `created_at` | `string` |
| `updated_at` | `string` |

### Nested Types
- `DocGenTemplateVersionBaseFormat`
- `DocGenTemplateVersionBaseSyntaxVersion`
- `FragmentFieldsetField`
- `GenerationInfo`
- `GenerationInfoSeverity`

## DocGenTemplateVersionBaseFormat
- Role: nested
- Parent: DocGenTemplateVersionFullDataObject
- Schema Name: DocGenTemplateVersionBaseFormat
- Schema ID: schema:anon/e3cd8861cef5df5d102527143fa24cd1c5df9928

### Enum

Values: DOCX, PDF, DOC, ODT, UNKNOWN

## DocGenTemplateVersionBaseSyntaxVersion
- Role: nested
- Parent: DocGenTemplateVersionFullDataObject
- Schema Name: DocGenTemplateVersionBaseSyntaxVersion
- Schema ID: schema:anon/8d85afe60184732869114b50fe8771f6f97ba872

### Enum

Values: V1, V2

## FragmentFieldsetField
- Role: nested
- Parent: DocGenTemplateVersionFullDataObject
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
- Parent: DocGenTemplateVersionFullDataObject
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
- Parent: DocGenTemplateVersionFullDataObject
- Schema Name: GenerationInfoSeverity
- Schema ID: schema:anon/4bc512f0c93de388afdbd8a134f1b285fb86a137

### Enum

Values: ERROR, WARNING
