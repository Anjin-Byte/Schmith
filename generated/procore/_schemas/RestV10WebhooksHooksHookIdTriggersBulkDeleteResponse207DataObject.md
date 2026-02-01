# RestV10WebhooksHooksHookIdTriggersBulkDeleteResponse207DataObject

## RestV10WebhooksHooksHookIdTriggersBulkDeleteResponse207DataObject
- Role: parent
- Schema Name: RestV10WebhooksHooksHookIdTriggersBulkDeleteResponse207
- Schema ID: schema:anon/21f5b639062c62ea2655f7598e0f38626f9a7fa1

### Fields

| Field | Type |
|------|------|
| `success` | `int[]` |
| `failed` | `RestV10WebhooksHooksHookIdTriggersBulkDeleteResponse207FailedItem[]` |

### Nested Types
- `RestV10WebhooksHooksHookIdTriggersBulkDeleteResponse207FailedItem`

## RestV10WebhooksHooksHookIdTriggersBulkDeleteResponse207FailedItem
- Role: nested
- Parent: RestV10WebhooksHooksHookIdTriggersBulkDeleteResponse207DataObject
- Schema Name: RestV10WebhooksHooksHookIdTriggersBulkDeleteResponse207FailedItem
- Schema ID: schema:anon/1bc2b1093f915d9d30ba604e147b566aff240c7a

### Fields

| Field | Type |
|------|------|
| `code` | `string` |
| `trigger` | `int` |
