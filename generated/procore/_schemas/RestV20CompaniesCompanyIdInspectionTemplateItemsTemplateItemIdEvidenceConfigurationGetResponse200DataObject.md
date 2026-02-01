# RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataObject

## RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200
- Schema ID: schema:anon/195525f0e1807bbe5084dbf4e2e92c0f50932a9b

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200Data` |

### Nested Types
- `RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200Data`
- `RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataObservation`
- `RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataPhoto`

## RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200Data
- Role: nested
- Parent: RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200Data
- Schema ID: schema:anon/eecb75037e18e044064794c1bc06f1672d51d65b
- Primary Key: ItemId

### Fields

| Field | Type |
|------|------|
| `item_id` | `string` |
| `photo` | `RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataPhoto` |
| `observation` | `RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataObservation` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataObservation
- Role: nested
- Parent: RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataObservation
- Schema ID: schema:anon/1421dcea34accef35ee3015bd3ddbda3d8be77a1

### Fields

| Field | Type |
|------|------|
| `status_ids` | `string[]` |
| `response_option_ids` | `string[]` |

## RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataPhoto
- Role: nested
- Parent: RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataPhoto
- Schema ID: schema:anon/db9c53f45e63271c15666f7310abff419f48ea51

### Fields

| Field | Type |
|------|------|
| `status_ids` | `string[]` |
| `response_option_ids` | `string[]` |
