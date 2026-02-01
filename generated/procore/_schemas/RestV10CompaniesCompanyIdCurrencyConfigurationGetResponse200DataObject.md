# RestV10CompaniesCompanyIdCurrencyConfigurationGetResponse200DataObject

## RestV10CompaniesCompanyIdCurrencyConfigurationGetResponse200DataObject
- Role: parent
- Schema Name: RestV10CompaniesCompanyIdCurrencyConfigurationGetResponse200
- Schema ID: schema:anon/cd10b63097a9af95b53a9132930419561dbfcdcf
- Primary Key: CompanyId

### Fields

| Field | Type |
|------|------|
| `company_id` | `int` |
| `currency_iso_code` | `string` |
| `currency_display` | `RestV10CompaniesCompanyIdCurrencyConfigurationGetResponse200CurrencyDisplay` |
| `multicurrency_enabled` | `bool` |
| `multicurrency_enabled_effective_date` | `string` |
| `eligible_for_multicurrency` | `bool` |

### Nested Types
- `RestV10CompaniesCompanyIdCurrencyConfigurationGetResponse200CurrencyDisplay`

## RestV10CompaniesCompanyIdCurrencyConfigurationGetResponse200CurrencyDisplay
- Role: nested
- Parent: RestV10CompaniesCompanyIdCurrencyConfigurationGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdCurrencyConfigurationGetResponse200CurrencyDisplay
- Schema ID: schema:anon/5023569015105775626fe09f4db2a0a7f75466e5

### Enum

Values: symbol, code
