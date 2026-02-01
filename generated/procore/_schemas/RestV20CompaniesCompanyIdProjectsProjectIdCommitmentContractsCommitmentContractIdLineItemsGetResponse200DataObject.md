# RestV20CompaniesCompanyIdProjectsProjectIdCommitmentContractsCommitmentContractIdLineItemsGetResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdCommitmentContractsCommitmentContractIdLineItemsGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentContractsCommitmentContractIdLineItemsGetResponse200
- Schema ID: schema:anon/4866f6af940e3472a915440c208ee58359c36856

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdCommitmentContractsCommitmentContractIdLineItemsGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdCommitmentContractsCommitmentContractIdLineItemsGetResponse200DataItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdCommitmentContractsCommitmentContractIdLineItemsGetResponse200DataItemExtendedType`
- `RestV20CompaniesCompanyIdProjectsProjectIdCommitmentContractsCommitmentContractIdLineItemsGetResponse200DataItemWbsCode`

## RestV20CompaniesCompanyIdProjectsProjectIdCommitmentContractsCommitmentContractIdLineItemsGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentContractsCommitmentContractIdLineItemsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentContractsCommitmentContractIdLineItemsGetResponse200DataItem
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
| `extended_type` | `RestV20CompaniesCompanyIdProjectsProjectIdCommitmentContractsCommitmentContractIdLineItemsGetResponse200DataItemExtendedType` |
| `wbs_code_id` | `string` |
| `tax_code_id` | `string` |
| `position` | `double` |
| `wbs_code` | `RestV20CompaniesCompanyIdProjectsProjectIdCommitmentContractsCommitmentContractIdLineItemsGetResponse200DataItemWbsCode` |
| `work_breakdown_structure` | `object` |

## RestV20CompaniesCompanyIdProjectsProjectIdCommitmentContractsCommitmentContractIdLineItemsGetResponse200DataItemExtendedType
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentContractsCommitmentContractIdLineItemsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentContractsCommitmentContractIdLineItemsGetResponse200DataItemExtendedType
- Schema ID: schema:anon/cc645dc57521e1744bf99e955dd68685060b8dc8

### Enum

Values: manual, calculated

## RestV20CompaniesCompanyIdProjectsProjectIdCommitmentContractsCommitmentContractIdLineItemsGetResponse200DataItemWbsCode
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentContractsCommitmentContractIdLineItemsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentContractsCommitmentContractIdLineItemsGetResponse200DataItemWbsCode
- Schema ID: schema:anon/8304133577766d122c9b3e54fed893886586be21
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `flat_code` | `string` |
| `description` | `string` |
