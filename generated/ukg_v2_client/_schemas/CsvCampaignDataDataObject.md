# CsvCampaignDataDataObject

## CsvCampaignDataDataObject
- Role: parent
- Schema Name: CsvCampaignData
- Schema ID: schema:definitions/CsvCampaignData

### Fields
- `ref`: `string`
- `fields`: `DatasetField[]`

### Nested Types
- `DatasetField`

## DatasetField
- Role: nested
- Parent: CsvCampaignDataDataObject
- Schema Name: DatasetField
- Schema ID: schema:definitions/DatasetField

### Fields
- `slug`: `string`
- `value`: `string`
- `type`: `TypeEnum`
