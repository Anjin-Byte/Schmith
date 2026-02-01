# RestV20CompaniesCompanyIdWorkflowsToolsGetResponse200DataObject

## RestV20CompaniesCompanyIdWorkflowsToolsGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdWorkflowsToolsGetResponse200
- Schema ID: schema:anon/23966afab7b4a7f0b2e678851ebcac6e1aefd1dc

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdWorkflowsToolsGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdWorkflowsToolsGetResponse200DataItem`
- `RestV20CompaniesCompanyIdWorkflowsToolsGetResponse200DataItemProvider`

## RestV20CompaniesCompanyIdWorkflowsToolsGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdWorkflowsToolsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWorkflowsToolsGetResponse200DataItem
- Schema ID: schema:anon/4d41ee73f51e2625d4806aacaa8105ae936d7fbf

### Fields

| Field | Type |
|------|------|
| `name` | `string` |
| `type` | `string` |
| `provider` | `RestV20CompaniesCompanyIdWorkflowsToolsGetResponse200DataItemProvider` |
| `subtype` | `string` |

## RestV20CompaniesCompanyIdWorkflowsToolsGetResponse200DataItemProvider
- Role: nested
- Parent: RestV20CompaniesCompanyIdWorkflowsToolsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWorkflowsToolsGetResponse200DataItemProvider
- Schema ID: schema:anon/ecb7dfe14ac9810f270ab8b18b769b7566806ae7

### Enum

Values: Project, Company
