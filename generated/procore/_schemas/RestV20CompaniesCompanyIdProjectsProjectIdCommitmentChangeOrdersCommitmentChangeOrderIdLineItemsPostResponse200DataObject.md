# RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsPostResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsPostResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsPostResponse200
- Schema ID: schema:anon/fbf6c015a4370b248356086a78f17e150b9a6c3b

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsPostResponse200Data` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsPostResponse200Data`
- `RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsPostResponse200DataExtendedType`
- `RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsPostResponse200DataWbsCode`

## RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsPostResponse200Data
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsPostResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsPostResponse200Data
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
| `extended_type` | `RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsPostResponse200DataExtendedType` |
| `wbs_code_id` | `string` |
| `tax_code_id` | `string` |
| `position` | `double` |
| `wbs_code` | `RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsPostResponse200DataWbsCode` |
| `work_breakdown_structure` | `object` |

## RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsPostResponse200DataExtendedType
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsPostResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsPostResponse200DataExtendedType
- Schema ID: schema:anon/cc645dc57521e1744bf99e955dd68685060b8dc8

### Enum

Values: manual, calculated

## RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsPostResponse200DataWbsCode
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsPostResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdCommitmentChangeOrdersCommitmentChangeOrderIdLineItemsPostResponse200DataWbsCode
- Schema ID: schema:anon/8304133577766d122c9b3e54fed893886586be21
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `flat_code` | `string` |
| `description` | `string` |
