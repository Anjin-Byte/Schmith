# RestV10ProjectsProjectIdDirectCostsPostResponse201DataObject

## RestV10ProjectsProjectIdDirectCostsPostResponse201DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdDirectCostsPostResponse201
- Schema ID: schema:anon/1cdec4f96f26fb42b9d1e068b474bcdab6e1202f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `attachments` | `RestV10ProjectsProjectIdDirectCostsPostResponse201AttachmentsItem[]` |
| `attachments_count` | `int` |
| `created_at` | `string` |
| `deleted_at` | `string` |
| `description` | `string` |
| `direct_cost_type` | `RestV10ProjectsProjectIdDirectCostsPostResponse201DirectCostType` |
| `employee` | `RestV10ProjectsProjectIdDirectCostsPostResponse201Employee` |
| `invoice_number` | `string` |
| `direct_cost_date` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `grand_total` | `string` |
| `line_items_count` | `int` |
| `payment_date` | `string` |
| `received_date` | `string` |
| `status` | `RestV10ProjectsProjectIdDirectCostsPostResponse201Status` |
| `terms` | `string` |
| `updated_at` | `string` |
| `vendor` | `RestV10ProjectsProjectIdDirectCostsPostResponse201Vendor` |
| `vendor_id` | `int` |
| `vendor_name` | `string` |
| `currency_configuration` | `RestV10ProjectsProjectIdDirectCostsPostResponse201CurrencyConfiguration` |

### Nested Types
- `RestV10ProjectsProjectIdDirectCostsPostResponse201AttachmentsItem`
- `RestV10ProjectsProjectIdDirectCostsPostResponse201CurrencyConfiguration`
- `RestV10ProjectsProjectIdDirectCostsPostResponse201DirectCostType`
- `RestV10ProjectsProjectIdDirectCostsPostResponse201Employee`
- `RestV10ProjectsProjectIdDirectCostsPostResponse201Status`
- `RestV10ProjectsProjectIdDirectCostsPostResponse201Vendor`

## RestV10ProjectsProjectIdDirectCostsPostResponse201AttachmentsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsPostResponse201AttachmentsItem
- Schema ID: schema:anon/c337dee3df228286468f0ff6d8c4852152f75cf4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |

## RestV10ProjectsProjectIdDirectCostsPostResponse201CurrencyConfiguration
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsPostResponse201CurrencyConfiguration
- Schema ID: schema:anon/604508c10ceb4d00db265015715c4f3c345909ea

### Fields

| Field | Type |
|------|------|
| `base_currency_iso_code` | `string` |
| `currency_iso_code` | `string` |

## RestV10ProjectsProjectIdDirectCostsPostResponse201DirectCostType
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsPostResponse201DirectCostType
- Schema ID: schema:anon/bb72991481f1872de70f6d554a7751ef3558918e

### Enum

Values: invoice, expense, payroll

## RestV10ProjectsProjectIdDirectCostsPostResponse201Employee
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsPostResponse201Employee
- Schema ID: schema:anon/8530528315133d74fc3a99d06b50a136aa519422
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsProjectIdDirectCostsPostResponse201Status
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsPostResponse201Status
- Schema ID: schema:anon/8da70385007d7e3ca99257bbe19b9baff2888939

### Enum

Values: draft, pending, revise_and_resubmit, approved

## RestV10ProjectsProjectIdDirectCostsPostResponse201Vendor
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsPostResponse201Vendor
- Schema ID: schema:anon/84c244671e471755e3ea5d82534f282f7e17dace
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
