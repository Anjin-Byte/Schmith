# RestV20CompaniesCompanyIdWorkflowsToolsGetResponse401DataObject

## RestV20CompaniesCompanyIdWorkflowsToolsGetResponse401DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdWorkflowsToolsGetResponse401
- Schema ID: schema:anon/3ff1c5fdb9b08c6e4d5f4bea9bae42c60eb39a1a

### Fields

| Field | Type |
|------|------|
| `error` | `RestV20CompaniesCompanyIdWorkflowsToolsGetResponse401Error` |

### Nested Types
- `RestV20CompaniesCompanyIdWorkflowsToolsGetResponse401Error`
- `RestV20CompaniesCompanyIdWorkflowsToolsGetResponse401ErrorDetailsItem`

## RestV20CompaniesCompanyIdWorkflowsToolsGetResponse401Error
- Role: nested
- Parent: RestV20CompaniesCompanyIdWorkflowsToolsGetResponse401DataObject
- Schema Name: RestV20CompaniesCompanyIdWorkflowsToolsGetResponse401Error
- Schema ID: schema:anon/a35b8a340745a5b9c5769b525676f6464fe11dea

### Fields

| Field | Type |
|------|------|
| `code` | `string` |
| `message` | `string` |
| `details` | `RestV20CompaniesCompanyIdWorkflowsToolsGetResponse401ErrorDetailsItem[]` |

## RestV20CompaniesCompanyIdWorkflowsToolsGetResponse401ErrorDetailsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdWorkflowsToolsGetResponse401DataObject
- Schema Name: RestV20CompaniesCompanyIdWorkflowsToolsGetResponse401ErrorDetailsItem
- Schema ID: schema:anon/2e24f2f8404125b5c681d87a20fa27ce0cfd69e5

### Fields

| Field | Type |
|------|------|
| `reason_code` | `string` |
| `message` | `string` |
| `source` | `string` |
