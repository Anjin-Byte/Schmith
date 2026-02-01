# RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataObject

## RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200
- Schema ID: schema:anon/651cdadd4e9220d027b3cd0e5cc31cd96f65aea9

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200Data` |

### Nested Types
- `RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200Data`
- `RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataFlowVisualizerSettings`
- `RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataFlowVisualizerSettingsEdgesItem`
- `RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataFlowVisualizerSettingsNodesItem`
- `RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataFlowVisualizerSettingsNodesItemPosition`
- `RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataResponsibleGroupsItem`
- `RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataStepsItem`
- `RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataStepsItemResponsibleGroupsItem`

## RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200Data
- Role: nested
- Parent: RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200Data
- Schema ID: schema:anon/778fb8bfefefbd0f42d6b757d5c3dcca347bc9e1
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `version` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `tool_type` | `string` |
| `tool_subtype` | `string` |
| `steps` | `RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataStepsItem[]` |
| `responsible_groups` | `RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataResponsibleGroupsItem[]` |
| `flow_visualizer_settings` | `RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataFlowVisualizerSettings` |

## RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataFlowVisualizerSettings
- Role: nested
- Parent: RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataFlowVisualizerSettings
- Schema ID: schema:anon/4aac2de39f49a93ce3dd6f4895512a7fc6bfa977

### Fields

| Field | Type |
|------|------|
| `nodes` | `RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataFlowVisualizerSettingsNodesItem[]` |
| `edges` | `RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataFlowVisualizerSettingsEdgesItem[]` |

## RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataFlowVisualizerSettingsEdgesItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataFlowVisualizerSettingsEdgesItem
- Schema ID: schema:anon/8c29e0d7ef3f20cc4c7be6bcc10776ec0d8a8097
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `source` | `string` |
| `target` | `string` |
| `type` | `string` |
| `sourceHandle` | `string` |
| `targetHandle` | `string` |

## RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataFlowVisualizerSettingsNodesItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataFlowVisualizerSettingsNodesItem
- Schema ID: schema:anon/6486329feef6de81fa3a7a1048b9803049a38f3b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `type` | `string` |
| `position` | `RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataFlowVisualizerSettingsNodesItemPosition` |
| `data` | `object` |

## RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataFlowVisualizerSettingsNodesItemPosition
- Role: nested
- Parent: RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataFlowVisualizerSettingsNodesItemPosition
- Schema ID: schema:anon/7c68737d7791de136fc6d15711e0a4df20e74585

### Fields

| Field | Type |
|------|------|
| `x` | `double` |
| `y` | `double` |

## RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataResponsibleGroupsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataResponsibleGroupsItem
- Schema ID: schema:anon/b7e84032a7d0664588010c6900f4906d5aabaa1d

### Fields

| Field | Type |
|------|------|
| `uuid` | `string` |
| `name` | `string` |
| `type` | `string` |

## RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataStepsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataStepsItem
- Schema ID: schema:anon/c4715168318dbd13225b55af901f1a499af97450

### Fields

| Field | Type |
|------|------|
| `uuid` | `string` |
| `name` | `string` |
| `type` | `string` |
| `responsible_groups` | `RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataStepsItemResponsibleGroupsItem[]` |

## RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataStepsItemResponsibleGroupsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWorkflowsTemplatesVersionsIdGetResponse200DataStepsItemResponsibleGroupsItem
- Schema ID: schema:anon/a6f5e956f9ac2ea18d662bc795eeec771985b1a8

### Fields

| Field | Type |
|------|------|
| `uuid` | `string` |
| `responses_required` | `string` |
