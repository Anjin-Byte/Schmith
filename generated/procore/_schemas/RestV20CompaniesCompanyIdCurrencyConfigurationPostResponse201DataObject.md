# RestV20CompaniesCompanyIdCurrencyConfigurationPostResponse201DataObject

## RestV20CompaniesCompanyIdCurrencyConfigurationPostResponse201DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdCurrencyConfigurationPostResponse201
- Schema ID: schema:anon/c48608d8078e495f38afb391dfe8605d25b42f18

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdCurrencyConfigurationPostResponse201Data` |

### Nested Types
- `RestV20CompaniesCompanyIdCurrencyConfigurationPostResponse201Data`
- `RestV20CompaniesCompanyIdCurrencyConfigurationPostResponse201DataCurrencyDisplay`

## RestV20CompaniesCompanyIdCurrencyConfigurationPostResponse201Data
- Role: nested
- Parent: RestV20CompaniesCompanyIdCurrencyConfigurationPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdCurrencyConfigurationPostResponse201Data
- Schema ID: schema:anon/0713b3af2ba2e0833c0f88e12e9ab54b4b596762
- Primary Key: CompanyId

### Fields

| Field | Type |
|------|------|
| `company_id` | `string` |
| `currency_iso_code` | `string` |
| `currency_display` | `RestV20CompaniesCompanyIdCurrencyConfigurationPostResponse201DataCurrencyDisplay` |
| `multicurrency_enabled` | `bool` |
| `multicurrency_enabled_effective_date` | `string` |

## RestV20CompaniesCompanyIdCurrencyConfigurationPostResponse201DataCurrencyDisplay
- Role: nested
- Parent: RestV20CompaniesCompanyIdCurrencyConfigurationPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdCurrencyConfigurationPostResponse201DataCurrencyDisplay
- Schema ID: schema:anon/deca1ca960b32268ffc46f421d25631e3b12e2e8

### Enum

Values: symbol, code
