# RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdAssigneesPatchResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdAssigneesPatchResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdAssigneesPatchResponse200
- Schema ID: schema:anon/5231651de4ea0f4a6264287625b9b0400b6ad154

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdAssigneesPatchResponse200Data` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdAssigneesPatchResponse200Data`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdAssigneesPatchResponse200DataResponsibleGroupMembershipsItem`

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdAssigneesPatchResponse200Data
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdAssigneesPatchResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdAssigneesPatchResponse200Data
- Schema ID: schema:anon/fd52da3e64c3e9297be58e87e0f08910696aa0f2
- Primary Key: WorkflowManagerId

### Fields

| Field | Type |
|------|------|
| `workflow_manager_id` | `string` |
| `responsible_group_memberships` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdAssigneesPatchResponse200DataResponsibleGroupMembershipsItem[]` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdAssigneesPatchResponse200DataResponsibleGroupMembershipsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdAssigneesPatchResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsPresetsIdAssigneesPatchResponse200DataResponsibleGroupMembershipsItem
- Schema ID: schema:anon/bc4bc62f27261891ff33359dccd1601d9f11a897

### Fields

| Field | Type |
|------|------|
| `uuid` | `string` |
| `login_ids` | `string[]` |
