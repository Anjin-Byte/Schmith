# DocGenCampaignPayloadDataObject

## DocGenCampaignPayloadDataObject
- Role: parent
- Schema Name: DocGenCampaignPayload
- Schema ID: schema:definitions/DocGenCampaignPayload
- Primary Key: DocumentGenerationTemplateId

### Fields

| Field | Type |
|------|------|
| `title` | `string` |
| `creator_ref` | `string` |
| `document_generation_template_id` | `string` |
| `document_generation_template_version` | `int` |
| `document_type_id` | `string` |
| `output_action` | `DocGenCampaignBaseOutputAction` |

### Nested Types
- `DocGenCampaignBaseOutputAction`

## DocGenCampaignBaseOutputAction
- Role: nested
- Parent: DocGenCampaignPayloadDataObject
- Schema Name: DocGenCampaignBaseOutputAction
- Schema ID: schema:anon/eb14f41fa7ebdcdf7b0d9f067de7ed5d09baec3b

### Enum

Values: zip, pdf, archive
