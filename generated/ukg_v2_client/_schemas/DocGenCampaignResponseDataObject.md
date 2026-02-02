# DocGenCampaignResponseDataObject

## DocGenCampaignResponseDataObject
- Role: parent
- Schema Name: DocGenCampaignResponse
- Schema ID: schema:definitions/DocGenCampaignResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `title` | `string` |
| `creator_ref` | `string` |
| `document_generation_template_id` | `string` |
| `document_generation_template_version` | `int` |
| `document_type_id` | `string` |
| `output_action` | `DocGenCampaignBaseOutputAction` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `status` | `DocGenCampaignResponseNested_b9192eStatus` |
| `started_at` | `string` |
| `ended_at` | `string` |

### Nested Types
- `DocGenCampaignBaseOutputAction`
- `DocGenCampaignResponseNested_b9192eStatus`

## DocGenCampaignBaseOutputAction
- Role: nested
- Parent: DocGenCampaignResponseDataObject
- Schema Name: DocGenCampaignBaseOutputAction
- Schema ID: schema:anon/eb14f41fa7ebdcdf7b0d9f067de7ed5d09baec3b

### Enum

Values: zip, pdf, archive

## DocGenCampaignResponseNested_b9192eStatus
- Role: nested
- Parent: DocGenCampaignResponseDataObject
- Schema Name: DocGenCampaignResponseNested_b9192eStatus
- Schema ID: schema:anon/b5f63d52b596fe43b050b390e66d85e4c8e0a863

### Enum

Values: created, started #Deprecated: use in_progress instead, in_progress, completed, failed, canceled
