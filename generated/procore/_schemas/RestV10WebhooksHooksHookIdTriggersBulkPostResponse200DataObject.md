# RestV10WebhooksHooksHookIdTriggersBulkPostResponse200DataObject

## RestV10WebhooksHooksHookIdTriggersBulkPostResponse200DataObject
- Role: parent
- Schema Name: RestV10WebhooksHooksHookIdTriggersBulkPostResponse200
- Schema ID: schema:anon/fa04a29d414a59f97e9e0cc5eb01c304a37fee87

### Fields

| Field | Type |
|------|------|
| `success` | `RestV10WebhooksHooksHookIdTriggersBulkPostResponse200SuccessItem[]` |

### Nested Types
- `RestV10WebhooksHooksHookIdTriggersBulkPostResponse200SuccessItem`
- `RestV10WebhooksHooksHookIdTriggersBulkPostResponse200SuccessItemEventType`

## RestV10WebhooksHooksHookIdTriggersBulkPostResponse200SuccessItem
- Role: nested
- Parent: RestV10WebhooksHooksHookIdTriggersBulkPostResponse200DataObject
- Schema Name: RestV10WebhooksHooksHookIdTriggersBulkPostResponse200SuccessItem
- Schema ID: schema:anon/11d930403eb31364a3a7136cc1fada85ba65f072
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `webhook_hook_id` | `int` |
| `resource_name` | `string` |
| `resource_id` | `int` |
| `event_type` | `RestV10WebhooksHooksHookIdTriggersBulkPostResponse200SuccessItemEventType` |
| `company_id` | `int` |
| `project_id` | `int` |
| `user_id` | `int` |

## RestV10WebhooksHooksHookIdTriggersBulkPostResponse200SuccessItemEventType
- Role: nested
- Parent: RestV10WebhooksHooksHookIdTriggersBulkPostResponse200DataObject
- Schema Name: RestV10WebhooksHooksHookIdTriggersBulkPostResponse200SuccessItemEventType
- Schema ID: schema:anon/0ad92aaaee103e658a449c3575181afc3fe7fd20

### Enum

Values: CREATE, UPDATE, DELETE
