# DocGenTemplatePatchPayloadDataObject

## DocGenTemplatePatchPayloadDataObject
- Role: parent
- Schema Name: DocGenTemplatePatchPayload
- Schema ID: schema:definitions/DocGenTemplatePatchPayload

### Fields

| Field | Type |
|------|------|
| `title` | `string` |
| `description` | `string` |
| `locale` | `string` |
| `format` | `DocGenTemplatePatchPayloadFormat` |
| `enabled` | `bool` |
| `validity_start_date` | `string` |
| `validity_end_date` | `string` |
| `active_version` | `int` |
| `restrictions` | `TemplateRestriction[]` |

### Nested Types
- `DocGenTemplatePatchPayloadFormat`
- `TemplateRestriction`

## DocGenTemplatePatchPayloadFormat
- Role: nested
- Parent: DocGenTemplatePatchPayloadDataObject
- Schema Name: DocGenTemplatePatchPayloadFormat
- Schema ID: schema:anon/e3cd8861cef5df5d102527143fa24cd1c5df9928

### Enum

Values: DOCX, PDF, DOC, ODT, UNKNOWN

## TemplateRestriction
- Role: nested
- Parent: DocGenTemplatePatchPayloadDataObject
- Schema Name: TemplateRestriction
- Schema ID: schema:definitions/TemplateRestriction
- Primary Key: OrganizationId

### Fields

| Field | Type |
|------|------|
| `organization_id` | `string` |
| `include_children` | `bool` |
