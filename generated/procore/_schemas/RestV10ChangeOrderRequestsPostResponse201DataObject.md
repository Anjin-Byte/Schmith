# RestV10ChangeOrderRequestsPostResponse201DataObject

## RestV10ChangeOrderRequestsPostResponse201DataObject
- Role: parent
- Schema Name: RestV10ChangeOrderRequestsPostResponse201
- Schema ID: schema:anon/4700d348d3a7729d2d7aa89cd1db6c13da7305d4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `contract_id` | `int` |
| `created_at` | `string` |
| `creator` | `RestV10ChangeOrderRequestsPostResponse201Creator` |
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
| `status` | `RestV10ChangeOrderRequestsPostResponse201Status` |
| `title` | `string` |
| `updated_at` | `string` |
| `currency_configuration` | `RestV10ChangeOrderRequestsPostResponse201CurrencyConfiguration` |

### Nested Types
- `RestV10ChangeOrderRequestsPostResponse201Creator`
- `RestV10ChangeOrderRequestsPostResponse201CurrencyConfiguration`
- `RestV10ChangeOrderRequestsPostResponse201Status`

## RestV10ChangeOrderRequestsPostResponse201Creator
- Role: nested
- Parent: RestV10ChangeOrderRequestsPostResponse201DataObject
- Schema Name: RestV10ChangeOrderRequestsPostResponse201Creator
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10ChangeOrderRequestsPostResponse201CurrencyConfiguration
- Role: nested
- Parent: RestV10ChangeOrderRequestsPostResponse201DataObject
- Schema Name: RestV10ChangeOrderRequestsPostResponse201CurrencyConfiguration
- Schema ID: schema:anon/7f07e441f0e7f9329466802e7e43f41196c8bcb0

### Fields

| Field | Type |
|------|------|
| `base_currency_iso_code` | `string` |
| `currency_iso_code` | `string` |

## RestV10ChangeOrderRequestsPostResponse201Status
- Role: nested
- Parent: RestV10ChangeOrderRequestsPostResponse201DataObject
- Schema Name: RestV10ChangeOrderRequestsPostResponse201Status
- Schema ID: schema:anon/5b89f75b59f65acdfdc32f08e622b0fbb79dc552

### Enum

Values: draft, not_pricing, pricing, pending, revised, proceeding, not_proceeding, no_charge, approved, rejected, void
