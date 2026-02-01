# RestV10CompaniesCompanyIdCurrencyConfigurationDeleteResponse200DataObject

## RestV10CompaniesCompanyIdCurrencyConfigurationDeleteResponse200DataObject
- Role: parent
- Schema Name: RestV10CompaniesCompanyIdCurrencyConfigurationDeleteResponse200
- Schema ID: schema:anon/7f94eb35f21e7f670f53494fa6ac4f1ac184c16b
- Primary Key: CompanyId

### Fields

| Field | Type |
|------|------|
| `company_id` | `int` |
| `currency_iso_code` | `string` |
| `currency_display` | `RestV10CompaniesCompanyIdCurrencyConfigurationDeleteResponse200CurrencyDisplay` |
| `multicurrency_enabled` | `bool` |
| `multicurrency_enabled_effective_date` | `string` |

### Nested Types
- `RestV10CompaniesCompanyIdCurrencyConfigurationDeleteResponse200CurrencyDisplay`

## RestV10CompaniesCompanyIdCurrencyConfigurationDeleteResponse200CurrencyDisplay
- Role: nested
- Parent: RestV10CompaniesCompanyIdCurrencyConfigurationDeleteResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdCurrencyConfigurationDeleteResponse200CurrencyDisplay
- Schema ID: schema:anon/deca1ca960b32268ffc46f421d25631e3b12e2e8

### Enum

Values: symbol, code
