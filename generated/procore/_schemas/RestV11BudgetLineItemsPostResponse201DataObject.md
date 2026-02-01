# RestV11BudgetLineItemsPostResponse201DataObject

## RestV11BudgetLineItemsPostResponse201DataObject
- Role: parent
- Schema Name: RestV11BudgetLineItemsPostResponse201
- Schema ID: schema:anon/787f41fd6282f7960e031643cf480fd877c58e6c
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
| `wbs_code` | `RestV11BudgetLineItemsPostResponse201WbsCode` |
| `currency_configuration` | `RestV11BudgetLineItemsPostResponse201CurrencyConfiguration` |

### Nested Types
- `RestV11BudgetLineItemsPostResponse201CurrencyConfiguration`
- `RestV11BudgetLineItemsPostResponse201WbsCode`

## RestV11BudgetLineItemsPostResponse201CurrencyConfiguration
- Role: nested
- Parent: RestV11BudgetLineItemsPostResponse201DataObject
- Schema Name: RestV11BudgetLineItemsPostResponse201CurrencyConfiguration
- Schema ID: schema:anon/64e9c13fd0998a6d3bb710a27f5aa0193cf39b42

### Fields

| Field | Type |
|------|------|
| `currency_iso_code` | `string` |

## RestV11BudgetLineItemsPostResponse201WbsCode
- Role: nested
- Parent: RestV11BudgetLineItemsPostResponse201DataObject
- Schema Name: RestV11BudgetLineItemsPostResponse201WbsCode
- Schema ID: schema:anon/730e72695ef7aa6a8c4861eea5d8e1f110168993
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `flat_code` | `string` |
| `description` | `string` |
