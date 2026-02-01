# RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostResponse201DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostResponse201DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostResponse201
- Schema ID: schema:anon/5838f032d887c5ffc4264590139f74ad88a417fc

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostResponse201Data` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostResponse201Data`
- `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostResponse201DataAttachment`
- `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostResponse201DataCapturedBy`

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostResponse201Data
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostResponse201Data
- Schema ID: schema:anon/2439c9e3cf173d6fae2d145078f10d7e85e1eb4f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `captured_by` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostResponse201DataCapturedBy` |
| `captured_at` | `string` |
| `attachment` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostResponse201DataAttachment` |

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostResponse201DataAttachment
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostResponse201DataAttachment
- Schema ID: schema:anon/094db0dbace92be9185cf7b0c735e5a8675a0a49
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `url` | `string` |
| `filename` | `string` |
| `name` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostResponse201DataCapturedBy
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostResponse201DataCapturedBy
- Schema ID: schema:anon/fbbbb8759506e5dc7757edceb25a08183b5df32c

### Fields
