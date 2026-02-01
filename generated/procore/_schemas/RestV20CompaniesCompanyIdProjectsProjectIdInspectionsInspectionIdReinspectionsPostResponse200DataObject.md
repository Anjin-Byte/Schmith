# RestV20CompaniesCompanyIdProjectsProjectIdInspectionsInspectionIdReinspectionsPostResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionsInspectionIdReinspectionsPostResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionsInspectionIdReinspectionsPostResponse200
- Schema ID: schema:anon/9993829cadac52de7d2dc89a35116d8bd39a0b3f

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionsInspectionIdReinspectionsPostResponse200Data` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdInspectionsInspectionIdReinspectionsPostResponse200Data`
- `RestV20CompaniesCompanyIdProjectsProjectIdInspectionsInspectionIdReinspectionsPostResponse200DataAttachmentsItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdInspectionsInspectionIdReinspectionsPostResponse200DataStatus`

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionsInspectionIdReinspectionsPostResponse200Data
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdInspectionsInspectionIdReinspectionsPostResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionsInspectionIdReinspectionsPostResponse200Data
- Schema ID: schema:anon/02609aea2ebeb45b5e9f58bf1e48410772489dca
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |
| `description` | `string` |
| `due_at` | `string` |
| `identifier` | `string` |
| `inspection_template_id` | `string` |
| `inspection_date` | `string` |
| `inspection_type_id` | `string` |
| `inspector_ids` | `string[]` |
| `private` | `bool` |
| `spec_section_id` | `string` |
| `status` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionsInspectionIdReinspectionsPostResponse200DataStatus` |
| `trade_id` | `string` |
| `distribution_member_ids` | `string[]` |
| `location_id` | `string` |
| `equipment_id` | `string` |
| `reinspected_by_id` | `string` |
| `reinspected_from_id` | `string` |
| `attachments` | `RestV20CompaniesCompanyIdProjectsProjectIdInspectionsInspectionIdReinspectionsPostResponse200DataAttachmentsItem[]` |

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionsInspectionIdReinspectionsPostResponse200DataAttachmentsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdInspectionsInspectionIdReinspectionsPostResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionsInspectionIdReinspectionsPostResponse200DataAttachmentsItem
- Schema ID: schema:anon/08f1f5e206e0aa2dd72c93dbeec0041e05653125
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `content_type` | `string` |
| `filename` | `string` |
| `name` | `string` |
| `thumbnail_url` | `string` |
| `url` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdInspectionsInspectionIdReinspectionsPostResponse200DataStatus
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdInspectionsInspectionIdReinspectionsPostResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdInspectionsInspectionIdReinspectionsPostResponse200DataStatus
- Schema ID: schema:anon/2007693a1e105d6d242c9edd28d995a3359d55f6

### Enum

Values: open, in_review, closed
