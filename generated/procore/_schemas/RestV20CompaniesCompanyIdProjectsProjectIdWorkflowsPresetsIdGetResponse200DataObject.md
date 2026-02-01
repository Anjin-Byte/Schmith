# RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200
- Schema ID: schema:anon/14b9d5dcc71c977365f91efae80ba2d1ff565833

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200Data` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200Data`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataDistributionList`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataResponsibleGroupMembershipsItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataResponsibleGroupMembershipsItemAssigneesItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataTemplate`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataWorkflowManager`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataWorkflowManagerCompany`

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200Data
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200Data
- Schema ID: schema:anon/7688cb081ab2133454c95f94113ca544edaa6413
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `valid` | `bool` |
| `default` | `bool` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `template` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataTemplate` |
| `workflow_manager` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataWorkflowManager` |
| `distribution_list` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataDistributionList` |
| `responsible_group_memberships` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataResponsibleGroupMembershipsItem[]` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataDistributionList
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataDistributionList
- Schema ID: schema:anon/73634126d2f27529b82e13979dfeded65e35b317
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataResponsibleGroupMembershipsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataResponsibleGroupMembershipsItem
- Schema ID: schema:anon/54b09053373c94ebd526639212c0cf88a4ed7c40

### Fields

| Field | Type |
|------|------|
| `responsible_group_uuid` | `string` |
| `assignees` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataResponsibleGroupMembershipsItemAssigneesItem[]` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataResponsibleGroupMembershipsItemAssigneesItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataResponsibleGroupMembershipsItemAssigneesItem
- Schema ID: schema:anon/d1ee080ca0ffb56087e293c823d1d6cafa2f2952
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `login` | `string` |
| `name` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataTemplate
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataTemplate
- Schema ID: schema:anon/53ab26470bc39eb9469b51db5d6c22dfc8aac1d4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `last_published_version_id` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataWorkflowManager
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataWorkflowManager
- Schema ID: schema:anon/815187ebbedf0e2e48f76d21085acecddfb76e09
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `login` | `string` |
| `name` | `string` |
| `company` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataWorkflowManagerCompany` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataWorkflowManagerCompany
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdGetResponse200DataWorkflowManagerCompany
- Schema ID: schema:anon/57ce472e3196601e806400c771d1dee26ad7d105

### Fields

| Field | Type |
|------|------|
| `name` | `string` |
