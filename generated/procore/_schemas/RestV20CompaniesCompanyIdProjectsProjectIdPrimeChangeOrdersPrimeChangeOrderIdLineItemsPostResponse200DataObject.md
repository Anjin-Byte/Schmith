# RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsPostResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsPostResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsPostResponse200
- Schema ID: schema:anon/c67117d0fa698e41076a126019f6417d92c5f19c

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsPostResponse200Data` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsPostResponse200Data`
- `RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsPostResponse200DataExtendedType`
- `RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsPostResponse200DataWbsCode`

## RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsPostResponse200Data
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsPostResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsPostResponse200Data
- Schema ID: schema:anon/b5a13d10aca25dd777bb32d3999936b4db404b8c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `prime_line_item_id` | `string` |
| `id` | `string` |
| `description` | `string` |
| `uom` | `string` |
| `quantity` | `double` |
| `unit_cost` | `string` |
| `amount` | `string` |
| `extended_type` | `RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsPostResponse200DataExtendedType` |
| `wbs_code_id` | `string` |
| `tax_code_id` | `string` |
| `position` | `double` |
| `wbs_code` | `RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsPostResponse200DataWbsCode` |
| `work_breakdown_structure` | `object` |

## RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsPostResponse200DataExtendedType
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsPostResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsPostResponse200DataExtendedType
- Schema ID: schema:anon/cc645dc57521e1744bf99e955dd68685060b8dc8

### Enum

Values: manual, calculated

## RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsPostResponse200DataWbsCode
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsPostResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsPostResponse200DataWbsCode
- Schema ID: schema:anon/8304133577766d122c9b3e54fed893886586be21
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `flat_code` | `string` |
| `description` | `string` |
