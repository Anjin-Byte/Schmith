# RestV10BudgetLineItemsPostResponse201DataObject

## RestV10BudgetLineItemsPostResponse201DataObject
- Role: parent
- Schema Name: RestV10BudgetLineItemsPostResponse201
- Schema ID: schema:anon/567656e09baca7fbb002ea7cfd9965160a4d2cd3
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `original_budget_amount` | `double` |
| `uom` | `string` |
| `quantity` | `double` |
| `unit_cost` | `double` |
| `calculation_strategy` | `string` |
| `approved_budget_changes` | `double` |
| `revised_budget` | `double` |
| `pending_budget_changes` | `double` |
| `projected_budget` | `double` |
| `committed_costs` | `double` |
| `direct_costs` | `double` |
| `pending_cost_changes` | `double` |
| `projected_costs` | `double` |
| `budget_forecast` | `double` |
| `estimated_cost_at_completion` | `double` |
| `projected_over_under` | `double` |
| `cost_code` | `RestV10BudgetLineItemsPostResponse201CostCode` |
| `division` | `RestV10BudgetLineItemsPostResponse201Division` |
| `line_item_type` | `RestV10BudgetLineItemsPostResponse201LineItemType` |
| `currency_configuration` | `RestV10BudgetLineItemsPostResponse201CurrencyConfiguration` |

### Nested Types
- `RestV10BudgetLineItemsPostResponse201CostCode`
- `RestV10BudgetLineItemsPostResponse201CurrencyConfiguration`
- `RestV10BudgetLineItemsPostResponse201Division`
- `RestV10BudgetLineItemsPostResponse201LineItemType`

## RestV10BudgetLineItemsPostResponse201CostCode
- Role: nested
- Parent: RestV10BudgetLineItemsPostResponse201DataObject
- Schema Name: RestV10BudgetLineItemsPostResponse201CostCode
- Schema ID: schema:anon/4f1d89d6569d07030822d6cd34990e8f1498b451
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `code` | `string` |
| `full_code` | `string` |

## RestV10BudgetLineItemsPostResponse201CurrencyConfiguration
- Role: nested
- Parent: RestV10BudgetLineItemsPostResponse201DataObject
- Schema Name: RestV10BudgetLineItemsPostResponse201CurrencyConfiguration
- Schema ID: schema:anon/64e9c13fd0998a6d3bb710a27f5aa0193cf39b42

### Fields

| Field | Type |
|------|------|
| `currency_iso_code` | `string` |

## RestV10BudgetLineItemsPostResponse201Division
- Role: nested
- Parent: RestV10BudgetLineItemsPostResponse201DataObject
- Schema Name: RestV10BudgetLineItemsPostResponse201Division
- Schema ID: schema:anon/84f0936801bd827ffef72c1b803b3d746ae66f3e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `full_code` | `string` |

## RestV10BudgetLineItemsPostResponse201LineItemType
- Role: nested
- Parent: RestV10BudgetLineItemsPostResponse201DataObject
- Schema Name: RestV10BudgetLineItemsPostResponse201LineItemType
- Schema ID: schema:anon/e47a0bba6fda2d4526aba1bfeee137049cd23758
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
