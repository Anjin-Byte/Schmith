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
| `format` | `FormatEnum` |
| `enabled` | `bool` |
| `validity_start_date` | `string` |
| `validity_end_date` | `string` |
| `active_version` | `int` |
| `restrictions` | `TemplateRestriction[]` |

### Nested Types
- `TemplateRestriction`

## TemplateRestriction
- Role: nested
- Parent: DocGenTemplatePatchPayloadDataObject
- Schema Name: TemplateRestriction
- Schema ID: schema:definitions/TemplateRestriction

### Fields

| Field | Type |
|------|------|
| `organization_id` | `string` |
| `include_children` | `bool` |
