# RestV20CompaniesCompanyIdRolesGetResponse200DataObject

## RestV20CompaniesCompanyIdRolesGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdRolesGetResponse200
- Schema ID: schema:anon/82446493acbb4e9db6811ac0a2a86e00eeff2ffa

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdRolesGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdRolesGetResponse200DataItem`

## RestV20CompaniesCompanyIdRolesGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdRolesGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdRolesGetResponse200DataItem
- Schema ID: schema:anon/75ebd9e5cd1368def0628ad8708415bc1b979224
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `add_to_project_team` | `bool` |
| `archetype` | `string` |
| `deletable` | `bool` |
| `display_on_company_home` | `bool` |
| `name` | `string` |
| `type` | `string` |
| `position` | `int` |
