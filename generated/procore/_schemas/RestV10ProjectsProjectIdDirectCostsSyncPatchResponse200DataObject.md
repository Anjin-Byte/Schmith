# RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200DataObject

## RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200
- Schema ID: schema:anon/bdef1c3cd34c70091f0727c9a2c33a0e7fda92c8

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItem[]` |
| `errors` | `RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200ErrorsItem[]` |

### Nested Types
- `RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItem`
- `RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemAttachmentsItem`
- `RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemCurrencyConfiguration`
- `RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemDirectCostType`
- `RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemEmployee`
- `RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemStatus`
- `RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemVendor`
- `RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200ErrorsItem`
- `RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200ErrorsItem_7abdf4Errors`

## RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItem
- Schema ID: schema:anon/1cdec4f96f26fb42b9d1e068b474bcdab6e1202f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `attachments` | `RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemAttachmentsItem[]` |
| `attachments_count` | `int` |
| `created_at` | `string` |
| `deleted_at` | `string` |
| `description` | `string` |
| `direct_cost_type` | `RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemDirectCostType` |
| `employee` | `RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemEmployee` |
| `invoice_number` | `string` |
| `direct_cost_date` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `grand_total` | `string` |
| `line_items_count` | `int` |
| `payment_date` | `string` |
| `received_date` | `string` |
| `status` | `RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemStatus` |
| `terms` | `string` |
| `updated_at` | `string` |
| `vendor` | `RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemVendor` |
| `vendor_id` | `int` |
| `vendor_name` | `string` |
| `currency_configuration` | `RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemCurrencyConfiguration` |

## RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemAttachmentsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemAttachmentsItem
- Schema ID: schema:anon/c337dee3df228286468f0ff6d8c4852152f75cf4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |

## RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemCurrencyConfiguration
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemCurrencyConfiguration
- Schema ID: schema:anon/604508c10ceb4d00db265015715c4f3c345909ea

### Fields

| Field | Type |
|------|------|
| `base_currency_iso_code` | `string` |
| `currency_iso_code` | `string` |

## RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemDirectCostType
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemDirectCostType
- Schema ID: schema:anon/bb72991481f1872de70f6d554a7751ef3558918e

### Enum

Values: invoice, expense, payroll

## RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemEmployee
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemEmployee
- Schema ID: schema:anon/8530528315133d74fc3a99d06b50a136aa519422
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemStatus
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemStatus
- Schema ID: schema:anon/8da70385007d7e3ca99257bbe19b9baff2888939

### Enum

Values: draft, pending, revise_and_resubmit, approved

## RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemVendor
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200EntitiesItemVendor
- Schema ID: schema:anon/84c244671e471755e3ea5d82534f282f7e17dace
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200ErrorsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200ErrorsItem
- Schema ID: schema:anon/6dda3f73050b0157b8a75c3a0bfddccbe6a997c6

### Fields

| Field | Type |
|------|------|
| `errors` | `RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200ErrorsItem_7abdf4Errors` |

## RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsSyncPatchResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
