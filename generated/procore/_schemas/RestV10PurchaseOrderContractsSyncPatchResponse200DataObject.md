# RestV10PurchaseOrderContractsSyncPatchResponse200DataObject

## RestV10PurchaseOrderContractsSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10PurchaseOrderContractsSyncPatchResponse200
- Schema ID: schema:anon/0b2384079175657bcdb2523e685b0c09ecdb5569

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItem[]` |
| `errors` | `object[]` |

### Nested Types
- `RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItem`
- `RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemAccountingMethod`
- `RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemAssignee`
- `RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemBillingScheduleOfValuesStatus`
- `RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemCurrencyConfiguration`
- `RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemProject`
- `RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemStatus`
- `RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemVendor`

## RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10PurchaseOrderContractsSyncPatchResponse200DataObject
- Schema Name: RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItem
- Schema ID: schema:anon/b1fefd05f643ff692e2b0688f538e034517a809c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `accounting_method` | `RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemAccountingMethod` |
| `approval_letter_date` | `string` |
| `approved_change_orders` | `string` |
| `assignee` | `RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemAssignee` |
| `bill_to_address` | `string` |
| `billing_schedule_of_values_status` | `RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemBillingScheduleOfValuesStatus` |
| `contract_date` | `string` |
| `created_at` | `string` |
| `deleted_at` | `string` |
| `delivery_date` | `string` |
| `description` | `string` |
| `draft_change_orders_amount` | `string` |
| `executed` | `bool` |
| `execution_date` | `string` |
| `grand_total` | `string` |
| `id` | `int` |
| `issued_on_date` | `string` |
| `letter_of_intent_date` | `string` |
| `number` | `string` |
| `origin_code` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `payment_terms` | `string` |
| `pending_change_orders` | `string` |
| `pending_revised_contract` | `string` |
| `percentage_paid` | `string` |
| `private` | `bool` |
| `project` | `RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemProject` |
| `remaining_balance_outstanding` | `string` |
| `requisitions_are_enabled` | `bool` |
| `retainage_percent` | `string` |
| `returned_date` | `string` |
| `revised_contract` | `string` |
| `ship_to_address` | `string` |
| `ship_via` | `string` |
| `show_line_items_to_non_admins` | `bool` |
| `signed_contract_received_date` | `string` |
| `status` | `RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemStatus` |
| `title` | `string` |
| `total_draw_requests_amount` | `string` |
| `total_payments` | `string` |
| `total_requisitions_amount` | `string` |
| `updated_at` | `string` |
| `vendor` | `RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemVendor` |
| `currency_configuration` | `RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemCurrencyConfiguration` |

## RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemAccountingMethod
- Role: nested
- Parent: RestV10PurchaseOrderContractsSyncPatchResponse200DataObject
- Schema Name: RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemAccountingMethod
- Schema ID: schema:anon/e1055d906a991a78b8abbae1161941e7d6036bb9

### Enum

Values: amount, unit

## RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemAssignee
- Role: nested
- Parent: RestV10PurchaseOrderContractsSyncPatchResponse200DataObject
- Schema Name: RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemAssignee
- Schema ID: schema:anon/aeae5c1d29301753eab0ee2db614e9e887f7cf40
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemBillingScheduleOfValuesStatus
- Role: nested
- Parent: RestV10PurchaseOrderContractsSyncPatchResponse200DataObject
- Schema Name: RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemBillingScheduleOfValuesStatus
- Schema ID: schema:anon/1df8987616d3f534ae8c04305cd4565811f6164b

### Enum

Values: draft, under_review, revise_and_submit, approved

## RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemCurrencyConfiguration
- Role: nested
- Parent: RestV10PurchaseOrderContractsSyncPatchResponse200DataObject
- Schema Name: RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemCurrencyConfiguration
- Schema ID: schema:anon/604508c10ceb4d00db265015715c4f3c345909ea

### Fields

| Field | Type |
|------|------|
| `base_currency_iso_code` | `string` |
| `currency_iso_code` | `string` |

## RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemProject
- Role: nested
- Parent: RestV10PurchaseOrderContractsSyncPatchResponse200DataObject
- Schema Name: RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemProject
- Schema ID: schema:anon/a6af6eb0e462865bcb4d406febc45b2f69ca396e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemStatus
- Role: nested
- Parent: RestV10PurchaseOrderContractsSyncPatchResponse200DataObject
- Schema Name: RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemStatus
- Schema ID: schema:anon/7bc47b8fc64636104cb4714bc5d9c3f2a3dd9258

### Enum

Values: Draft, Processing, Submitted, Partially Received, Received, Approved, Closed

## RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemVendor
- Role: nested
- Parent: RestV10PurchaseOrderContractsSyncPatchResponse200DataObject
- Schema Name: RestV10PurchaseOrderContractsSyncPatchResponse200EntitiesItemVendor
- Schema ID: schema:anon/14cdfd050285bb05a68dc76da452852fa0eec16b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `company` | `string` |
