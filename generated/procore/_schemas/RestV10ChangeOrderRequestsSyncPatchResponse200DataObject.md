# RestV10ChangeOrderRequestsSyncPatchResponse200DataObject

## RestV10ChangeOrderRequestsSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10ChangeOrderRequestsSyncPatchResponse200
- Schema ID: schema:anon/59435e65dc9659c22df35e542f8667227ebe7885

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItem[]` |
| `errors` | `RestV10ChangeOrderRequestsSyncPatchResponse200ErrorsItem[]` |

### Nested Types
- `RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItem`
- `RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemAttachmentsItem`
- `RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemBatch`
- `RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemContract`
- `RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemContractVendor`
- `RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemCreator`
- `RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemCurrencyConfiguration`
- `RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemStatus`
- `RestV10ChangeOrderRequestsSyncPatchResponse200ErrorsItem`
- `RestV10ChangeOrderRequestsSyncPatchResponse200ErrorsItem_7abdf4Errors`

## RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10ChangeOrderRequestsSyncPatchResponse200DataObject
- Schema Name: RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItem
- Schema ID: schema:anon/c18c14b0d267c5ececc3b5794d19058f58a107a7
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `change_order_package_id` | `int` |
| `contract_id` | `int` |
| `created_at` | `string` |
| `executed` | `bool` |
| `creator` | `RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemCreator` |
| `deleted_at` | `string` |
| `description` | `string` |
| `due_date` | `string` |
| `grand_total` | `string` |
| `invoiced_date` | `string` |
| `number` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `paid_date` | `string` |
| `position` | `int` |
| `private` | `bool` |
| `revision` | `int` |
| `schedule_impact_amount` | `int` |
| `signed_change_order_received_date` | `string` |
| `status` | `RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemStatus` |
| `title` | `string` |
| `updated_at` | `string` |
| `attachments` | `RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemAttachmentsItem[]` |
| `currency_configuration` | `RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemCurrencyConfiguration` |
| `contract` | `RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemContract` |
| `batch` | `RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemBatch` |

## RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemAttachmentsItem
- Role: nested
- Parent: RestV10ChangeOrderRequestsSyncPatchResponse200DataObject
- Schema Name: RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemAttachmentsItem
- Schema ID: schema:anon/0fed82b2ab013163afe0e50420982438fd21bbb8
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `url` | `string` |
| `filename` | `string` |

## RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemBatch
- Role: nested
- Parent: RestV10ChangeOrderRequestsSyncPatchResponse200DataObject
- Schema Name: RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemBatch
- Schema ID: schema:anon/84541451451488f1eb95b7e9895d2e7774485b1f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `title` | `string` |
| `number` | `string` |

## RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemContract
- Role: nested
- Parent: RestV10ChangeOrderRequestsSyncPatchResponse200DataObject
- Schema Name: RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemContract
- Schema ID: schema:anon/d370f5348bd920025070f82b28cf71c16d89cb49
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `number` | `string` |
| `title` | `string` |
| `type` | `string` |
| `status` | `string` |
| `vendor` | `RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemContractVendor` |

## RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemContractVendor
- Role: nested
- Parent: RestV10ChangeOrderRequestsSyncPatchResponse200DataObject
- Schema Name: RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemContractVendor
- Schema ID: schema:anon/5b8b3d259fcad860880e5242a2d36d81a88aec6b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemCreator
- Role: nested
- Parent: RestV10ChangeOrderRequestsSyncPatchResponse200DataObject
- Schema Name: RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemCreator
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemCurrencyConfiguration
- Role: nested
- Parent: RestV10ChangeOrderRequestsSyncPatchResponse200DataObject
- Schema Name: RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemCurrencyConfiguration
- Schema ID: schema:anon/7f07e441f0e7f9329466802e7e43f41196c8bcb0

### Fields

| Field | Type |
|------|------|
| `base_currency_iso_code` | `string` |
| `currency_iso_code` | `string` |

## RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemStatus
- Role: nested
- Parent: RestV10ChangeOrderRequestsSyncPatchResponse200DataObject
- Schema Name: RestV10ChangeOrderRequestsSyncPatchResponse200EntitiesItemStatus
- Schema ID: schema:anon/5b89f75b59f65acdfdc32f08e622b0fbb79dc552

### Enum

Values: draft, not_pricing, pricing, pending, revised, proceeding, not_proceeding, no_charge, approved, rejected, void

## RestV10ChangeOrderRequestsSyncPatchResponse200ErrorsItem
- Role: nested
- Parent: RestV10ChangeOrderRequestsSyncPatchResponse200DataObject
- Schema Name: RestV10ChangeOrderRequestsSyncPatchResponse200ErrorsItem
- Schema ID: schema:anon/3fc6586538009ddad007eb30759232b7a8ea77e5

### Fields

| Field | Type |
|------|------|
| `errors` | `RestV10ChangeOrderRequestsSyncPatchResponse200ErrorsItem_7abdf4Errors` |

## RestV10ChangeOrderRequestsSyncPatchResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10ChangeOrderRequestsSyncPatchResponse200DataObject
- Schema Name: RestV10ChangeOrderRequestsSyncPatchResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
