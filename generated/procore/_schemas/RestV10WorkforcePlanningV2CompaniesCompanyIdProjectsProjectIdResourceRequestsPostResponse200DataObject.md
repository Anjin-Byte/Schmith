# RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdResourceRequestsPostResponse200DataObject

## RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdResourceRequestsPostResponse200DataObject
- Role: parent
- Schema Name: RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdResourceRequestsPostResponse200
- Schema ID: schema:anon/a1ff65afad7f691009ca31f205389701612174a2
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `project_id` | `string` |
| `start_day` | `string` |
| `end_day` | `string` |
| `start_time` | `string` |
| `end_time` | `string` |
| `percent_allocated` | `int` |
| `work_days` | `RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdResourceRequestsPostResponse200WorkDays` |
| `job_title_id` | `string` |
| `category_id` | `string` |
| `subcategory_id` | `string` |
| `work_scope_text` | `string` |
| `instruction_text` | `string` |

### Nested Types
- `RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdResourceRequestsPostResponse200WorkDays`

## RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdResourceRequestsPostResponse200WorkDays
- Role: nested
- Parent: RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdResourceRequestsPostResponse200DataObject
- Schema Name: RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdResourceRequestsPostResponse200WorkDays
- Schema ID: schema:anon/e384abcb7836c25e72675bdfa605092ac7f7417b

### Fields

| Field | Type |
|------|------|
| `0` | `bool` |
| `1` | `bool` |
| `2` | `bool` |
| `3` | `bool` |
| `4` | `bool` |
| `5` | `bool` |
| `6` | `bool` |
