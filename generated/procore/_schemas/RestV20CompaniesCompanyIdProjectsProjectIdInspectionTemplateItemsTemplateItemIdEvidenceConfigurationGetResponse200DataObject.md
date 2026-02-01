# RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200
- Schema ID: schema:anon/f304d1e17ed5b04f016c2c9c44dc28fc9c06440e

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200Data` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200Data`
- `RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataObservation`
- `RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataPhoto`

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200Data
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200Data
- Schema ID: schema:anon/fc124208cb12a92dc623cb86f214bb440da1505b
- Primary Key: ItemId

### Fields

| Field | Type |
|------|------|
| `item_id` | `string` |
| `photo` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataPhoto` |
| `observation` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataObservation` |
| `is_editable` | `bool` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataObservation
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataObservation
- Schema ID: schema:anon/1421dcea34accef35ee3015bd3ddbda3d8be77a1

### Fields

| Field | Type |
|------|------|
| `status_ids` | `string[]` |
| `response_option_ids` | `string[]` |

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataPhoto
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGetResponse200DataPhoto
- Schema ID: schema:anon/db9c53f45e63271c15666f7310abff419f48ea51

### Fields

| Field | Type |
|------|------|
| `status_ids` | `string[]` |
| `response_option_ids` | `string[]` |
