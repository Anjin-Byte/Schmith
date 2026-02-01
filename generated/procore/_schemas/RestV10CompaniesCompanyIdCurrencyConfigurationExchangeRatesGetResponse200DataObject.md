# RestV10CompaniesCompanyIdCurrencyConfigurationExchangeRatesGetResponse200DataObject

## RestV10CompaniesCompanyIdCurrencyConfigurationExchangeRatesGetResponse200DataObject
- Role: parent
- Schema Name: RestV10CompaniesCompanyIdCurrencyConfigurationExchangeRatesGetResponse200
- Schema ID: schema:anon/3d168ddf003638a9e6efa22792c03d25ace0dae9

### Fields

| Field | Type |
|------|------|
| `exchange_rates` | `RestV10CompaniesCompanyIdCurrencyConfigurationExchangeRatesGetResponse200ExchangeRatesItem[]` |

### Nested Types
- `RestV10CompaniesCompanyIdCurrencyConfigurationExchangeRatesGetResponse200ExchangeRatesItem`

## RestV10CompaniesCompanyIdCurrencyConfigurationExchangeRatesGetResponse200ExchangeRatesItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdCurrencyConfigurationExchangeRatesGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdCurrencyConfigurationExchangeRatesGetResponse200ExchangeRatesItem
- Schema ID: schema:anon/ec098ab43dc4d3fcf82417e347a00442ee0637b2
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `company_id` | `int` |
| `base_currency_iso_code` | `string` |
| `quote_currency_iso_code` | `string` |
| `exchange_rate` | `string` |
| `is_active` | `bool` |
| `updated_at` | `string` |
| `created_at` | `string` |
