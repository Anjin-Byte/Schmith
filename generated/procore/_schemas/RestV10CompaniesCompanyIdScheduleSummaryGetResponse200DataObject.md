# RestV10CompaniesCompanyIdScheduleSummaryGetResponse200DataObject

## RestV10CompaniesCompanyIdScheduleSummaryGetResponse200DataObject
- Role: parent
- Schema Name: RestV10CompaniesCompanyIdScheduleSummaryGetResponse200
- Schema ID: schema:anon/30fee9296dcef11b3d58fa430840c42423e1ad09

### Fields

| Field | Type |
|------|------|
| `data` | `RestV10CompaniesCompanyIdScheduleSummaryGetResponse200DataItem[]` |

### Nested Types
- `RestV10CompaniesCompanyIdScheduleSummaryGetResponse200DataItem`
- `RestV10CompaniesCompanyIdScheduleSummaryGetResponse200DataItemProjectsItem`

## RestV10CompaniesCompanyIdScheduleSummaryGetResponse200DataItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdScheduleSummaryGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdScheduleSummaryGetResponse200DataItem
- Schema ID: schema:anon/f389ed95def738d8349c7141b2e0f5ae23ae218c

### Fields

| Field | Type |
|------|------|
| `date` | `string` |
| `projects_count` | `int` |
| `projects` | `RestV10CompaniesCompanyIdScheduleSummaryGetResponse200DataItemProjectsItem[]` |

## RestV10CompaniesCompanyIdScheduleSummaryGetResponse200DataItemProjectsItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdScheduleSummaryGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdScheduleSummaryGetResponse200DataItemProjectsItem
- Schema ID: schema:anon/ce36a941a3b7d2ad8f9bf0de6ea746254db1695c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `tasks_count` | `int` |
| `calendar_items_count` | `int` |
