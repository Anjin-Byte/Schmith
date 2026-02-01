# RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsGetResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsGetResponse200
- Schema ID: schema:anon/45e1c15538a738d66da75c3a6a8c0802bdf9c8f9

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsGetResponse200DataItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsGetResponse200DataItemExtendedType`
- `RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsGetResponse200DataItemWbsCode`

## RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsGetResponse200DataItem
- Schema ID: schema:anon/086ca7f74562947f4a6179c639a05e688854ef35
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `prime_line_item_id` | `string` |
| `commitment_line_item_id` | `string` |
| `id` | `string` |
| `description` | `string` |
| `uom` | `string` |
| `quantity` | `double` |
| `unit_cost` | `string` |
| `amount` | `string` |
| `extended_type` | `RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsGetResponse200DataItemExtendedType` |
| `wbs_code_id` | `string` |
| `tax_code_id` | `string` |
| `position` | `double` |
| `wbs_code` | `RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsGetResponse200DataItemWbsCode` |
| `work_breakdown_structure` | `object` |

## RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsGetResponse200DataItemExtendedType
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsGetResponse200DataItemExtendedType
- Schema ID: schema:anon/cc645dc57521e1744bf99e955dd68685060b8dc8

### Enum

Values: manual, calculated

## RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsGetResponse200DataItemWbsCode
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsGetResponse200DataItemWbsCode
- Schema ID: schema:anon/8304133577766d122c9b3e54fed893886586be21
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `flat_code` | `string` |
| `description` | `string` |
