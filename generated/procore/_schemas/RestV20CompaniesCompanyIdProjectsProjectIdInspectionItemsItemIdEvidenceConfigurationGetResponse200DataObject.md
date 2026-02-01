# RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGetResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGetResponse200
- Schema ID: schema:anon/41b9823b585956e4c604aa9c87023384bcb4c9e6

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGetResponse200DataItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGetResponse200DataItemObservation`
- `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGetResponse200DataItemPhoto`

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGetResponse200DataItem
- Schema ID: schema:anon/eecb75037e18e044064794c1bc06f1672d51d65b
- Primary Key: ItemId

### Fields

| Field | Type |
|------|------|
| `item_id` | `string` |
| `photo` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGetResponse200DataItemPhoto` |
| `observation` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGetResponse200DataItemObservation` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGetResponse200DataItemObservation
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGetResponse200DataItemObservation
- Schema ID: schema:anon/1421dcea34accef35ee3015bd3ddbda3d8be77a1

### Fields

| Field | Type |
|------|------|
| `status_ids` | `string[]` |
| `response_option_ids` | `string[]` |

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGetResponse200DataItemPhoto
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGetResponse200DataItemPhoto
- Schema ID: schema:anon/db9c53f45e63271c15666f7310abff419f48ea51

### Fields

| Field | Type |
|------|------|
| `status_ids` | `string[]` |
| `response_option_ids` | `string[]` |
