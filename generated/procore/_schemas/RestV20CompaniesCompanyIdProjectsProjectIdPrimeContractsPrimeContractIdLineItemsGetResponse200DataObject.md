# RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsGetResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsGetResponse200
- Schema ID: schema:anon/4e50f808cb2e796ceafcb634e7824a592db9a26d

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsGetResponse200DataItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsGetResponse200DataItemExtendedType`
- `RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsGetResponse200DataItemWbsCode`

## RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsGetResponse200DataItem
- Schema ID: schema:anon/aa8c3e4f80860e7cdb589058a1d92c8ad6036209
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `line_item_group_id` | `string` |
| `id` | `string` |
| `description` | `string` |
| `uom` | `string` |
| `quantity` | `double` |
| `unit_cost` | `string` |
| `amount` | `string` |
| `extended_type` | `RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsGetResponse200DataItemExtendedType` |
| `wbs_code_id` | `string` |
| `tax_code_id` | `string` |
| `position` | `double` |
| `wbs_code` | `RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsGetResponse200DataItemWbsCode` |
| `work_breakdown_structure` | `object` |

## RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsGetResponse200DataItemExtendedType
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsGetResponse200DataItemExtendedType
- Schema ID: schema:anon/cc645dc57521e1744bf99e955dd68685060b8dc8

### Enum

Values: manual, calculated

## RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsGetResponse200DataItemWbsCode
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsGetResponse200DataItemWbsCode
- Schema ID: schema:anon/8304133577766d122c9b3e54fed893886586be21
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `flat_code` | `string` |
| `description` | `string` |
