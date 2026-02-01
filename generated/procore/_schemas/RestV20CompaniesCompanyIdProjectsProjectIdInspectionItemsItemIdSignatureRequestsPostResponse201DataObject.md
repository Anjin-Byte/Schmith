# RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201
- Schema ID: schema:anon/8b4f19e70c1243b72eda8bdac3d95336c833b5b9

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201Data` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201Data`
- `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201DataSignatory`
- `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201DataSignature`
- `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201DataSignatureAttachment`

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201Data
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201Data
- Schema ID: schema:anon/2ca8e1683a17031e0a251a04df328d70afe5a8ba
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `requested_by_id` | `string` |
| `signatory` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201DataSignatory` |
| `signature` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201DataSignature` |

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201DataSignatory
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201DataSignatory
- Schema ID: schema:anon/fbbbb8759506e5dc7757edceb25a08183b5df32c

### Fields

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201DataSignature
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201DataSignature
- Schema ID: schema:anon/0c49a11ac5af197ae172763f79755f59a86ddb71
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `captured_by` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201DataSignatory` |
| `captured_at` | `string` |
| `attachment` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201DataSignatureAttachment` |

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201DataSignatureAttachment
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostResponse201DataSignatureAttachment
- Schema ID: schema:anon/094db0dbace92be9185cf7b0c735e5a8675a0a49
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `url` | `string` |
| `filename` | `string` |
| `name` | `string` |
