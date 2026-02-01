# RestV20CompaniesCompanyIdWebhooksHooksHookIdTriggersGetResponse200DataObject

## RestV20CompaniesCompanyIdWebhooksHooksHookIdTriggersGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdWebhooksHooksHookIdTriggersGetResponse200
- Schema ID: schema:anon/6d5b67376447dff69f0d59be213fdf90029b174c

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdWebhooksHooksHookIdTriggersGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdWebhooksHooksHookIdTriggersGetResponse200DataItem`

## RestV20CompaniesCompanyIdWebhooksHooksHookIdTriggersGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdWebhooksHooksHookIdTriggersGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWebhooksHooksHookIdTriggersGetResponse200DataItem
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
