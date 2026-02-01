# RestV10ProjectsProjectIdProjectDatesGetResponse200DataObject

## RestV10ProjectsProjectIdProjectDatesGetResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdProjectDatesGetResponse200
- Schema ID: schema:anon/7e8e01a51be4b18b292bfc3b072b820086c869e2

### Fields

| Field | Type |
|------|------|
| `schedule_dates` | `RestV10ProjectsProjectIdProjectDatesGetResponse200ScheduleDates` |
| `project_dates` | `RestV10ProjectsProjectIdProjectDatesGetResponse200ProjectDatesItem[]` |

### Nested Types
- `RestV10ProjectsProjectIdProjectDatesGetResponse200ProjectDatesItem`
- `RestV10ProjectsProjectIdProjectDatesGetResponse200ScheduleDates`

## RestV10ProjectsProjectIdProjectDatesGetResponse200ProjectDatesItem
- Role: nested
- Parent: RestV10ProjectsProjectIdProjectDatesGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdProjectDatesGetResponse200ProjectDatesItem
- Schema ID: schema:anon/869f9182a7afb8ebedaab4198026e228c8d1a6f3
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `project_membership_id` | `int` |
| `name` | `string` |
| `date` | `string` |
| `actual_date` | `string` |
| `display_on_timeline` | `bool` |

## RestV10ProjectsProjectIdProjectDatesGetResponse200ScheduleDates
- Role: nested
- Parent: RestV10ProjectsProjectIdProjectDatesGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdProjectDatesGetResponse200ScheduleDates
- Schema ID: schema:anon/e0bec7941c8715d337e8d56bf0bbd6df416de7c5

### Fields

| Field | Type |
|------|------|
| `substantial_completion_date` | `string` |
| `finish_variance` | `string` |
| `percentage_complete` | `int` |
