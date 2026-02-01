# RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsGetResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsGetResponse200
- Schema ID: schema:anon/16ff4a742bd037c072316b59c7331147bd6d9d4b

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsGetResponse200DataItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsGetResponse200DataItemExtendedType`
- `RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsGetResponse200DataItemWbsCode`

## RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsGetResponse200DataItem
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
| `extended_type` | `RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsGetResponse200DataItemExtendedType` |
| `wbs_code_id` | `string` |
| `tax_code_id` | `string` |
| `position` | `double` |
| `wbs_code` | `RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsGetResponse200DataItemWbsCode` |
| `work_breakdown_structure` | `object` |

## RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsGetResponse200DataItemExtendedType
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsGetResponse200DataItemExtendedType
- Schema ID: schema:anon/cc645dc57521e1744bf99e955dd68685060b8dc8

### Enum

Values: manual, calculated

## RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsGetResponse200DataItemWbsCode
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdPrimeChangeOrdersPrimeChangeOrderIdLineItemsGetResponse200DataItemWbsCode
- Schema ID: schema:anon/8304133577766d122c9b3e54fed893886586be21
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `flat_code` | `string` |
| `description` | `string` |
