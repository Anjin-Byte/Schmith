# RestV10WebhooksHooksHookIdTriggersBulkPostResponse207DataObject

## RestV10WebhooksHooksHookIdTriggersBulkPostResponse207DataObject
- Role: parent
- Schema Name: RestV10WebhooksHooksHookIdTriggersBulkPostResponse207
- Schema ID: schema:anon/5c859f3041d74b72d263fc674630da3dc54f3e83

### Fields

| Field | Type |
|------|------|
| `success` | `RestV10WebhooksHooksHookIdTriggersBulkPostResponse207SuccessItem[]` |
| `failed` | `RestV10WebhooksHooksHookIdTriggersBulkPostResponse207FailedItem[]` |

### Nested Types
- `RestV10WebhooksHooksHookIdTriggersBulkPostResponse207FailedItem`
- `RestV10WebhooksHooksHookIdTriggersBulkPostResponse207FailedItemErrors`
- `RestV10WebhooksHooksHookIdTriggersBulkPostResponse207FailedItemTrigger`
- `RestV10WebhooksHooksHookIdTriggersBulkPostResponse207SuccessItem`
- `RestV10WebhooksHooksHookIdTriggersBulkPostResponse207SuccessItemEventType`

## RestV10WebhooksHooksHookIdTriggersBulkPostResponse207FailedItem
- Role: nested
- Parent: RestV10WebhooksHooksHookIdTriggersBulkPostResponse207DataObject
- Schema Name: RestV10WebhooksHooksHookIdTriggersBulkPostResponse207FailedItem
- Schema ID: schema:anon/980c762e58fd25b8ea57ef88d0cfcd2ce62f7142

### Fields

| Field | Type |
|------|------|
| `code` | `string` |
| `message` | `string` |
| `trigger` | `RestV10WebhooksHooksHookIdTriggersBulkPostResponse207FailedItemTrigger` |
| `errors` | `RestV10WebhooksHooksHookIdTriggersBulkPostResponse207FailedItemErrors` |

## RestV10WebhooksHooksHookIdTriggersBulkPostResponse207FailedItemErrors
- Role: nested
- Parent: RestV10WebhooksHooksHookIdTriggersBulkPostResponse207DataObject
- Schema Name: RestV10WebhooksHooksHookIdTriggersBulkPostResponse207FailedItemErrors
- Schema ID: schema:anon/2d4b16b8f5116a4c588d3d6a87b753685554c512

### Fields

| Field | Type |
|------|------|
| `event_type` | `string` |

## RestV10WebhooksHooksHookIdTriggersBulkPostResponse207FailedItemTrigger
- Role: nested
- Parent: RestV10WebhooksHooksHookIdTriggersBulkPostResponse207DataObject
- Schema Name: RestV10WebhooksHooksHookIdTriggersBulkPostResponse207FailedItemTrigger
- Schema ID: schema:anon/c1c1eaf07614306b46517c2b8d57b475f469bc3c

### Fields

| Field | Type |
|------|------|
| `resource_name` | `string` |

## RestV10WebhooksHooksHookIdTriggersBulkPostResponse207SuccessItem
- Role: nested
- Parent: RestV10WebhooksHooksHookIdTriggersBulkPostResponse207DataObject
- Schema Name: RestV10WebhooksHooksHookIdTriggersBulkPostResponse207SuccessItem
- Schema ID: schema:anon/11d930403eb31364a3a7136cc1fada85ba65f072
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `webhook_hook_id` | `int` |
| `resource_name` | `string` |
| `resource_id` | `int` |
| `event_type` | `RestV10WebhooksHooksHookIdTriggersBulkPostResponse207SuccessItemEventType` |
| `company_id` | `int` |
| `project_id` | `int` |
| `user_id` | `int` |

## RestV10WebhooksHooksHookIdTriggersBulkPostResponse207SuccessItemEventType
- Role: nested
- Parent: RestV10WebhooksHooksHookIdTriggersBulkPostResponse207DataObject
- Schema Name: RestV10WebhooksHooksHookIdTriggersBulkPostResponse207SuccessItemEventType
- Schema ID: schema:anon/0ad92aaaee103e658a449c3575181afc3fe7fd20

### Enum

Values: CREATE, UPDATE, DELETE
