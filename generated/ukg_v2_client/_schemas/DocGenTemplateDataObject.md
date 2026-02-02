# DocGenTemplateDataObject

## DocGenTemplateDataObject
- Role: parent
- Schema Name: DocGenTemplate
- Schema ID: schema:definitions/DocGenTemplate
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `created_at` | `string` |
| `updated_at` | `string` |
| `id` | `string` |
| `title` | `string` |
| `description` | `string` |
| `locale` | `string` |
| `format` | `DocGenTemplateNestedFormat` |
| `latest_version` | `int` |
| `active_version` | `int` |
| `validity_start_date` | `string` |
| `validity_end_date` | `string` |
| `enabled` | `bool` |
| `is_injectable` | `bool` |
| `active_version_syntax` | `DocGenTemplateNestedActiveVersionSyntax` |
| `restrictions` | `TemplateRestriction[]` |

### Nested Types
- `DocGenTemplateNestedActiveVersionSyntax`
- `DocGenTemplateNestedFormat`
- `TemplateRestriction`

## DocGenTemplateNestedActiveVersionSyntax
- Role: nested
- Parent: DocGenTemplateDataObject
- Schema Name: DocGenTemplateNestedActiveVersionSyntax
- Schema ID: schema:anon/b7bb12c442a392530a81b3eb21df4d7928e23574

### Enum

Values: V1, V2

## DocGenTemplateNestedFormat
- Role: nested
- Parent: DocGenTemplateDataObject
- Schema Name: DocGenTemplateNestedFormat
- Schema ID: schema:anon/e3cd8861cef5df5d102527143fa24cd1c5df9928

### Enum

Values: DOCX, PDF, DOC, ODT, UNKNOWN

## TemplateRestriction
- Role: nested
- Parent: DocGenTemplateDataObject
- Schema Name: TemplateRestriction
- Schema ID: schema:definitions/TemplateRestriction
- Primary Key: OrganizationId

### Fields

| Field | Type |
|------|------|
| `organization_id` | `string` |
| `include_children` | `bool` |
