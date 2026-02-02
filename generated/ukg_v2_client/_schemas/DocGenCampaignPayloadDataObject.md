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
| `data` | `CampaignData[]` |

### Nested Types
- `CampaignData`
- `CampaignDataFragmentFieldsItem`
- `DatasetField`
- `DatasetFieldTypeTypeItemItem`
- `DocGenCampaignBaseOutputAction`

## CampaignData
- Role: nested
- Parent: DocGenCampaignPayloadDataObject
- Schema Name: CampaignData
- Schema ID: schema:definitions/CampaignData
- Primary Key: EmployeeId

### Fields

| Field | Type |
|------|------|
| `employee_id` | `string` |
| `ref` | `string` |
| `fields` | `DatasetField[]` |
| `fragment_fields` | `CampaignDataFragmentFieldsItem` |

## CampaignDataFragmentFieldsItem
- Role: nested
- Parent: DocGenCampaignPayloadDataObject
- Schema Name: CampaignDataFragmentFieldsItem
- Schema ID: schema:anon/350bec8262fdece6efca0518a57cc29460bbfd7e

### Fields

| Field | Type |
|------|------|
| `fragment_placeholder_1` | `DatasetField[]` |
| `fragment_placeholder_n` | `DatasetField[]` |

## DatasetField
- Role: nested
- Parent: DocGenCampaignPayloadDataObject
- Schema Name: DatasetField
- Schema ID: schema:definitions/DatasetField

### Fields

| Field | Type |
|------|------|
| `slug` | `string` |
| `value` | `string` |
| `type` | `DatasetFieldTypeTypeItemItem` |

## DatasetFieldTypeTypeItemItem
- Role: nested
- Parent: DocGenCampaignPayloadDataObject
- Schema Name: DatasetFieldTypeTypeItemItem
- Schema ID: schema:anon/07b949304bddf335c6eb4571c1c40044809b0b32

### Enum

Values: date

## DocGenCampaignBaseOutputAction
- Role: nested
- Parent: DocGenCampaignPayloadDataObject
- Schema Name: DocGenCampaignBaseOutputAction
- Schema ID: schema:anon/eb14f41fa7ebdcdf7b0d9f067de7ed5d09baec3b

### Enum

Values: zip, pdf, archive
