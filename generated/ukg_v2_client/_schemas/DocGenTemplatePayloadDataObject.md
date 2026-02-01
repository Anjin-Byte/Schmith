# DocGenTemplatePayloadDataObject

## DocGenTemplatePayloadDataObject
- Role: parent
- Schema Name: DocGenTemplatePayload
- Schema ID: schema:definitions/DocGenTemplatePayload

### Fields

| Field | Type |
|------|------|
| `title` | `string` |
| `description` | `string` |
| `locale` | `string` |
| `validity_start_date` | `string` |
| `validity_end_date` | `string` |
| `enabled` | `bool` |
| `is_injectable` | `bool` |
| `restrictions` | `TemplateRestriction[]` |

### Nested Types
- `TemplateRestriction`

## TemplateRestriction
- Role: nested
- Parent: DocGenTemplatePayloadDataObject
- Schema Name: TemplateRestriction
- Schema ID: schema:definitions/TemplateRestriction
- Primary Key: OrganizationId

### Fields

| Field | Type |
|------|------|
| `organization_id` | `string` |
| `include_children` | `bool` |
