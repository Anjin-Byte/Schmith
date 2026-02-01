# RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationGetResponse200DataObject

## RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationGetResponse200DataObject
- Role: parent
- Schema Name: RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationGetResponse200
- Schema ID: schema:anon/536de0a52a52ed0c4b089c9bfa9aebb908394599
- Primary Key: CompanyId

### Fields

| Field | Type |
|------|------|
| `company_id` | `int` |
| `project_id` | `int` |
| `currency_iso_code` | `string` |
| `currency_display` | `RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationGetResponse200CurrencyDisplay` |
| `company_currency_exchange_rate_override` | `string` |
| `multicurrency_enabled` | `bool` |
| `eligible_for_financial_objs_multicurrency` | `bool` |

### Nested Types
- `RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationGetResponse200CurrencyDisplay`

## RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationGetResponse200CurrencyDisplay
- Role: nested
- Parent: RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationGetResponse200CurrencyDisplay
- Schema ID: schema:anon/5023569015105775626fe09f4db2a0a7f75466e5

### Enum

Values: symbol, code
