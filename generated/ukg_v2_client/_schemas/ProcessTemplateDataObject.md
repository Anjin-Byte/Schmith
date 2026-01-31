# ProcessTemplateDataObject

## ProcessTemplateDataObject
- Role: parent
- Schema Name: ProcessTemplate
- Schema ID: schema:definitions/ProcessTemplate

### Fields
- `id`: `string`
- `title`: `string`
- `public_title`: `string`
- `description`: `string`
- `created_at`: `string`
- `created_by`: `object`
- `updated_at`: `string`
- `updated_by`: `object`
- `automatic_archiving`: `bool`
- `restrictions`: `ProcessTemplateRestriction[]`

### Nested Types
- `Organization`
- `ProcessTemplateRestriction`

## Organization
- Role: nested
- Parent: ProcessTemplateDataObject
- Schema Name: Organization
- Schema ID: schema:definitions/Organization

### Fields
- `id`: `string`
- `operator`: `OperatorEnum`

## ProcessTemplateRestriction
- Role: nested
- Parent: ProcessTemplateDataObject
- Schema Name: ProcessTemplateRestriction
- Schema ID: schema:definitions/ProcessTemplateRestriction

### Fields
- `organizations`: `Organization[]`
