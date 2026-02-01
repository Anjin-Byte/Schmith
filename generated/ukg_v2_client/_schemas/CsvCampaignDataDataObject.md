# CsvCampaignDataDataObject

## CsvCampaignDataDataObject
- Role: parent
- Schema Name: CsvCampaignData
- Schema ID: schema:definitions/CsvCampaignData

### Fields

| Field | Type |
|------|------|
| `ref` | `string` |
| `fields` | `DatasetField[]` |

### Nested Types
- `DatasetField`
- `DatasetFieldTypeType`

## DatasetField
- Role: nested
- Parent: CsvCampaignDataDataObject
- Schema Name: DatasetField
- Schema ID: schema:definitions/DatasetField

### Fields

| Field | Type |
|------|------|
| `slug` | `string` |
| `value` | `string` |
| `type` | `DatasetFieldTypeType` |

## DatasetFieldTypeType
- Role: nested
- Parent: CsvCampaignDataDataObject
- Schema Name: DatasetFieldTypeType
- Schema ID: schema:anon/07b949304bddf335c6eb4571c1c40044809b0b32

### Enum

Values: date
