# RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200
- Schema ID: schema:anon/39ea1e2bed3637ff58b95709522339224ee45b2c

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataItemSignatory`
- `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataItemSignature`
- `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataItemSignatureAttachment`

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataItem
- Schema ID: schema:anon/2ca8e1683a17031e0a251a04df328d70afe5a8ba
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `requested_by_id` | `string` |
| `signatory` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataItemSignatory` |
| `signature` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataItemSignature` |

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataItemSignatory
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataItemSignatory
- Schema ID: schema:anon/fbbbb8759506e5dc7757edceb25a08183b5df32c

### Fields

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataItemSignature
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataItemSignature
- Schema ID: schema:anon/0c49a11ac5af197ae172763f79755f59a86ddb71
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `captured_by` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataItemSignatory` |
| `captured_at` | `string` |
| `attachment` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataItemSignatureAttachment` |

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataItemSignatureAttachment
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGetResponse200DataItemSignatureAttachment
- Schema ID: schema:anon/094db0dbace92be9185cf7b0c735e5a8675a0a49
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `url` | `string` |
| `filename` | `string` |
| `name` | `string` |
