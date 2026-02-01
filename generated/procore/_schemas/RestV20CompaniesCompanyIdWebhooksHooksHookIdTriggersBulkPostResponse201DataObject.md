# RestV20CompaniesCompanyIdWebhooksHooksHookIdTriggersBulkPostResponse201DataObject

## RestV20CompaniesCompanyIdWebhooksHooksHookIdTriggersBulkPostResponse201DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdWebhooksHooksHookIdTriggersBulkPostResponse201
- Schema ID: schema:anon/cd9af84bfb8678d428af2642f5bbb3ed699f0f23

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdWebhooksHooksHookIdTriggersBulkPostResponse201DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdWebhooksHooksHookIdTriggersBulkPostResponse201DataItem`

## RestV20CompaniesCompanyIdWebhooksHooksHookIdTriggersBulkPostResponse201DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdWebhooksHooksHookIdTriggersBulkPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdWebhooksHooksHookIdTriggersBulkPostResponse201DataItem
- Schema ID: schema:anon/82a44e811a98447d4e51518319af5e3e43f8239e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `webhook_hook_id` | `string` |
| `resource_name` | `string` |
| `event_type` | `string` |
| `company_id` | `string` |
| `project_id` | `string` |
