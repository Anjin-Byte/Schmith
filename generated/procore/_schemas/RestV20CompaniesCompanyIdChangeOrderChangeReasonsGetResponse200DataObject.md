# RestV20CompaniesCompanyIdChangeOrderChangeReasonsGetResponse200DataObject

## RestV20CompaniesCompanyIdChangeOrderChangeReasonsGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdChangeOrderChangeReasonsGetResponse200
- Schema ID: schema:anon/35f6d1663165cc56bc92ba13d759499b9f097697

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdChangeOrderChangeReasonsGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdChangeOrderChangeReasonsGetResponse200DataItem`

## RestV20CompaniesCompanyIdChangeOrderChangeReasonsGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdChangeOrderChangeReasonsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdChangeOrderChangeReasonsGetResponse200DataItem
- Schema ID: schema:anon/7d54baedbacf144768b9cef17f753ef22224644f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `change_reason` | `string` |
| `show_in_select` | `bool` |
| `deletable` | `bool` |
