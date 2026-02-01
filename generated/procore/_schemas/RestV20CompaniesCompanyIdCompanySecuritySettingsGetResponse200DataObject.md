# RestV20CompaniesCompanyIdCompanySecuritySettingsGetResponse200DataObject

## RestV20CompaniesCompanyIdCompanySecuritySettingsGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdCompanySecuritySettingsGetResponse200
- Schema ID: schema:anon/4039f8eb952454e54274bd50f0362ea390abd9a9

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdCompanySecuritySettingsGetResponse200Data` |

### Nested Types
- `RestV20CompaniesCompanyIdCompanySecuritySettingsGetResponse200Data`

## RestV20CompaniesCompanyIdCompanySecuritySettingsGetResponse200Data
- Role: nested
- Parent: RestV20CompaniesCompanyIdCompanySecuritySettingsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdCompanySecuritySettingsGetResponse200Data
- Schema ID: schema:anon/a3dd8f25118d11ea1c156461037f09f210d098a0

### Fields

| Field | Type |
|------|------|
| `enable_login_lockout` | `bool` |
| `password_reset_after` | `int` |
| `session_timeout` | `int` |
| `enforce_password_reset_by_email` | `bool` |
| `is_pin_required_for_jit` | `bool` |
| `password_security_url` | `string` |
