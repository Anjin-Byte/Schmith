# RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsGetResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsGetResponse200
- Schema ID: schema:anon/fc3cff39e10a72afcf4d3c197b51b7165777b9ec

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsGetResponse200DataItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsGetResponse200DataItemTemplate`

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsGetResponse200DataItem
- Schema ID: schema:anon/bdeda25b83c84baebc1d9bd5b7de3f1af8e72cdb
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `valid` | `bool` |
| `default` | `bool` |
| `template` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsGetResponse200DataItemTemplate` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsGetResponse200DataItemTemplate
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsGetResponse200DataItemTemplate
- Schema ID: schema:anon/f6bb384b0668dcb046212afb6427e9fb14f68c65
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |
| `last_published_version_id` | `string` |
