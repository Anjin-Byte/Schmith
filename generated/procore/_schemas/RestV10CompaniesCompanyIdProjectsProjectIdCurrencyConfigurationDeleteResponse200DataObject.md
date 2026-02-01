# RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationDeleteResponse200DataObject

## RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationDeleteResponse200DataObject
- Role: parent
- Schema Name: RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationDeleteResponse200
- Schema ID: schema:anon/1babfe8837d73d248178b90b181ac3d533847fee
- Primary Key: CompanyId

### Fields

| Field | Type |
|------|------|
| `company_id` | `int` |
| `project_id` | `int` |
| `currency_iso_code` | `string` |
| `currency_display` | `RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationDeleteResponse200CurrencyDisplay` |
| `company_currency_exchange_rate_override` | `string` |
| `multicurrency_enabled` | `bool` |

### Nested Types
- `RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationDeleteResponse200CurrencyDisplay`

## RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationDeleteResponse200CurrencyDisplay
- Role: nested
- Parent: RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationDeleteResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdProjectsProjectIdCurrencyConfigurationDeleteResponse200CurrencyDisplay
- Schema ID: schema:anon/deca1ca960b32268ffc46f421d25631e3b12e2e8

### Enum

Values: symbol, code
