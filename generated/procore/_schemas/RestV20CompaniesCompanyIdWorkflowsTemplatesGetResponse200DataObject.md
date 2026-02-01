# RestV20CompaniesCompanyIdWorkflowsTemplatesGetResponse200DataObject

## RestV20CompaniesCompanyIdWorkflowsTemplatesGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdWorkflowsTemplatesGetResponse200
- Schema ID: schema:anon/3edbc658002cded7ff155e4a5dd765a9d9c48a36

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdWorkflowsTemplatesGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdWorkflowsTemplatesGetResponse200DataItem`
- `RestV20CompaniesCompanyIdWorkflowsTemplatesGetResponse200DataItemLatestPublishedVersion`
- `RestV20CompaniesCompanyIdWorkflowsTemplatesGetResponse200DataItemVersionsItem`

## RestV20CompaniesCompanyIdWorkflowsTemplatesGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdWorkflowsTemplatesGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWorkflowsTemplatesGetResponse200DataItem
- Schema ID: schema:anon/b9741b079164bf15aa42a30e7f159f8fe7675b1b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `archived_at` | `string` |
| `assigned_projects_count` | `int` |
| `tool_type` | `string` |
| `tool_subtype` | `string` |
| `latest_published_version` | `RestV20CompaniesCompanyIdWorkflowsTemplatesGetResponse200DataItemLatestPublishedVersion` |
| `versions` | `RestV20CompaniesCompanyIdWorkflowsTemplatesGetResponse200DataItemVersionsItem[]` |

## RestV20CompaniesCompanyIdWorkflowsTemplatesGetResponse200DataItemLatestPublishedVersion
- Role: nested
- Parent: RestV20CompaniesCompanyIdWorkflowsTemplatesGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWorkflowsTemplatesGetResponse200DataItemLatestPublishedVersion
- Schema ID: schema:anon/0d4b0bf70127bf9cdbc573b2efd3b9e8f197eaae
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `version` | `string` |

## RestV20CompaniesCompanyIdWorkflowsTemplatesGetResponse200DataItemVersionsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdWorkflowsTemplatesGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWorkflowsTemplatesGetResponse200DataItemVersionsItem
- Schema ID: schema:anon/baf5d21e5bdbd1b14a797e1a767a0581d47ea7a2
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `version` | `string` |
