# RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsPostResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsPostResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsPostResponse200
- Schema ID: schema:anon/2229426bc915ec9523dbc0dbf8d6be561ac59e6d

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsPostResponse200Data` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsPostResponse200Data`
- `RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsPostResponse200DataExtendedType`
- `RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsPostResponse200DataWbsCode`

## RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsPostResponse200Data
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsPostResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsPostResponse200Data
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
| `extended_type` | `RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsPostResponse200DataExtendedType` |
| `wbs_code_id` | `string` |
| `tax_code_id` | `string` |
| `position` | `double` |
| `wbs_code` | `RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsPostResponse200DataWbsCode` |
| `work_breakdown_structure` | `object` |

## RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsPostResponse200DataExtendedType
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsPostResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsPostResponse200DataExtendedType
- Schema ID: schema:anon/cc645dc57521e1744bf99e955dd68685060b8dc8

### Enum

Values: manual, calculated

## RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsPostResponse200DataWbsCode
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsPostResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsPrimeContractIdLineItemsPostResponse200DataWbsCode
- Schema ID: schema:anon/8304133577766d122c9b3e54fed893886586be21
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `flat_code` | `string` |
| `description` | `string` |
