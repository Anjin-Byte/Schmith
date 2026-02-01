# RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGetResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGetResponse200
- Schema ID: schema:anon/507c863da3fa3f65bc578e8ef74d5f4562142541

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGetResponse200DataItem`

## RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGetResponse200DataItem
- Schema ID: schema:anon/78df2e4b86d22f13871d5bc1f03049f74faa3383
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `project_membership_id` | `string` |
| `name` | `string` |
| `date` | `string` |
| `actual_date` | `string` |
| `display_on_timeline` | `bool` |
