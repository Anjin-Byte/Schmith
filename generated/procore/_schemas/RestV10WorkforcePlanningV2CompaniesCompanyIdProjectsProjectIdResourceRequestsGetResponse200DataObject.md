# RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdResourceRequestsGetResponse200DataObject

## RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdResourceRequestsGetResponse200DataObject
- Role: parent
- Schema Name: RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdResourceRequestsGetResponse200
- Schema ID: schema:anon/a02ec8a0c167165176e683c4f733086f43d5f8f3

### Fields

| Field | Type |
|------|------|
| `possible_pages` | `int` |
| `current_page` | `int` |
| `data` | `RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdResourceRequestsGetResponse200DataItem[]` |

### Nested Types
- `RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdResourceRequestsGetResponse200DataItem`

## RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdResourceRequestsGetResponse200DataItem
- Role: nested
- Parent: RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdResourceRequestsGetResponse200DataObject
- Schema Name: RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdResourceRequestsGetResponse200DataItem
- Schema ID: schema:anon/689b06776c2d21db718d2238d530c5bffbb437c2
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `creator_id` | `string` |
| `project_id` | `string` |
| `start_day` | `string` |
| `end_day` | `string` |
| `start_time` | `string` |
| `end_time` | `string` |
| `percent_allocated` | `int` |
| `job_title_id` | `string` |
| `category_id` | `string` |
| `subcategory_id` | `string` |
| `state_id` | `string` |
| `work_scope_text` | `string` |
| `instruction_text` | `string` |
| `work_days` | `object` |
