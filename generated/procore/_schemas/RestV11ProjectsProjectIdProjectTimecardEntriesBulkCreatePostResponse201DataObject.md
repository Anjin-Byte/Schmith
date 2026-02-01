# RestV11ProjectsProjectIdProjectTimecardEntriesBulkCreatePostResponse201DataObject

## RestV11ProjectsProjectIdProjectTimecardEntriesBulkCreatePostResponse201DataObject
- Role: parent
- Schema Name: RestV11ProjectsProjectIdProjectTimecardEntriesBulkCreatePostResponse201
- Schema ID: schema:anon/69893a812405c25b1cee50858568d8b70cb76ef1

### Fields

| Field | Type |
|------|------|
| `timecard_entries` | `RestV11ProjectsProjectIdProjectTimecardEntriesBulkCreatePostResponse201TimecardEntriesItem[]` |

### Nested Types
- `RestV11ProjectsProjectIdProjectTimecardEntriesBulkCreatePostResponse201TimecardEntriesItem`
- `RestV11ProjectsProjectIdProjectTimecardEntriesBulkCreatePostResponse201TimecardEntriesItemApprovalStatus`

## RestV11ProjectsProjectIdProjectTimecardEntriesBulkCreatePostResponse201TimecardEntriesItem
- Role: nested
- Parent: RestV11ProjectsProjectIdProjectTimecardEntriesBulkCreatePostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdProjectTimecardEntriesBulkCreatePostResponse201TimecardEntriesItem
- Schema ID: schema:anon/eff5c3664b82d103187e85860aba8106873b4c25
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `project_id` | `int` |
| `company_id` | `int` |
| `date` | `string` |
| `hours` | `string` |
| `time_in` | `string` |
| `time_out` | `string` |
| `clock_in_time` | `string` |
| `clock_out_time` | `string` |
| `clock_in_id` | `int` |
| `clock_out_id` | `int` |
| `lunch_time` | `string` |
| `lunch_start_time` | `string` |
| `lunch_stop_time` | `string` |
| `lunch_clock_in_id` | `int` |
| `lunch_clock_out_id` | `int` |
| `description` | `string` |
| `billable` | `bool` |
| `timecard_time_type_id` | `int` |
| `cost_code_id` | `int` |
| `wbs_code_id` | `int` |
| `line_item_type_id` | `int` |
| `work_classification_id` | `int` |
| `party_id` | `int` |
| `timesheet_id` | `int` |
| `location_id` | `int` |
| `crew_id` | `int` |
| `approval_status` | `RestV11ProjectsProjectIdProjectTimecardEntriesBulkCreatePostResponse201TimecardEntriesItemApprovalStatus` |
| `approval_date` | `string` |
| `approved_by_id` | `int` |
| `set_timecard_time_type_automatically` | `bool` |
| `origin_id` | `string` |
| `origin_data` | `string` |
| `custom_field_%{custom_field_definition_id}` | `string` |
| `sub_job_id` | `int` |
| `signed` | `bool` |
| `in_progress` | `bool` |
| `split_parent_id` | `int` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `deleted_at` | `string` |

## RestV11ProjectsProjectIdProjectTimecardEntriesBulkCreatePostResponse201TimecardEntriesItemApprovalStatus
- Role: nested
- Parent: RestV11ProjectsProjectIdProjectTimecardEntriesBulkCreatePostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdProjectTimecardEntriesBulkCreatePostResponse201TimecardEntriesItemApprovalStatus
- Schema ID: schema:anon/7f1c8f8391edf02f256a843c75634a49c527138d

### Enum

Values: pending, approved, reviewed, completed
