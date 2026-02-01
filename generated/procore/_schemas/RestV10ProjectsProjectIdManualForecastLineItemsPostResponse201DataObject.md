# RestV10ProjectsProjectIdManualForecastLineItemsPostResponse201DataObject

## RestV10ProjectsProjectIdManualForecastLineItemsPostResponse201DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdManualForecastLineItemsPostResponse201
- Schema ID: schema:anon/493330297c6ff7a3e53d70566825b95a7ccd94d4

### Fields

| Field | Type |
|------|------|
| `data` | `RestV10ProjectsProjectIdManualForecastLineItemsPostResponse201Data` |

### Nested Types
- `RestV10ProjectsProjectIdManualForecastLineItemsPostResponse201Data`
- `RestV10ProjectsProjectIdManualForecastLineItemsPostResponse201DataCurrencyConfiguration`

## RestV10ProjectsProjectIdManualForecastLineItemsPostResponse201Data
- Role: nested
- Parent: RestV10ProjectsProjectIdManualForecastLineItemsPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdManualForecastLineItemsPostResponse201Data
- Schema ID: schema:anon/7d90f2cfd8f14bda3adc11e6c2a6c6378e73c44f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `budget_line_item_id` | `int` |
| `wbs_code_id` | `int` |
| `budget_forecast_id` | `int` |
| `project_id` | `int` |
| `company_id` | `int` |
| `description` | `string` |
| `quantity` | `int` |
| `uom` | `string` |
| `unit_cost` | `string` |
| `amount` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `currency_configuration` | `RestV10ProjectsProjectIdManualForecastLineItemsPostResponse201DataCurrencyConfiguration` |

## RestV10ProjectsProjectIdManualForecastLineItemsPostResponse201DataCurrencyConfiguration
- Role: nested
- Parent: RestV10ProjectsProjectIdManualForecastLineItemsPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdManualForecastLineItemsPostResponse201DataCurrencyConfiguration
- Schema ID: schema:anon/f884a729d35e590d8f5a68a341a5a0587ffe2382

### Fields

| Field | Type |
|------|------|
| `currency_iso_code` | `string` |
