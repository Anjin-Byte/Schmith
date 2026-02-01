# RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationExchangeRatesGetResponse200DataObject

## RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationExchangeRatesGetResponse200DataObject
- Role: parent
- Schema Name: RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationExchangeRatesGetResponse200
- Schema ID: schema:anon/eb18970fea9e3d817737d8c239bc7942601bf432

### Fields

| Field | Type |
|------|------|
| `exchange_rates` | `RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationExchangeRatesGetResponse200ExchangeRatesItem[]` |

### Nested Types
- `RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationExchangeRatesGetResponse200ExchangeRatesItem`

## RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationExchangeRatesGetResponse200ExchangeRatesItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationExchangeRatesGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationExchangeRatesGetResponse200ExchangeRatesItem
- Schema ID: schema:anon/6540a8513b891f4f09943aa689887b8e306b2762
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `company_id` | `int` |
| `project_id` | `int` |
| `base_currency_iso_code` | `string` |
| `quote_currency_iso_code` | `string` |
| `exchange_rate` | `string` |
| `is_active` | `bool` |
| `updated_at` | `string` |
| `created_at` | `string` |
