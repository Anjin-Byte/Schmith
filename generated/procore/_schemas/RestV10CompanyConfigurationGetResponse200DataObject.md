# RestV10CompanyConfigurationGetResponse200DataObject

## RestV10CompanyConfigurationGetResponse200DataObject
- Role: parent
- Schema Name: RestV10CompanyConfigurationGetResponse200
- Schema ID: schema:anon/48773421a571df4efd8e6043e39bb9b8a36c77de
- Primary Key: TimesheetDefaultCostTypeId

### Fields

| Field | Type |
|------|------|
| `strict_file_uploading` | `bool` |
| `enable_image_real_time_as_builts` | `bool` |
| `currency_symbol` | `string` |
| `currency_display` | `string` |
| `currency_iso_code` | `string` |
| `timecard_employees_see_all_projects` | `bool` |
| `timesheet_enabled_cost_type` | `int[]` |
| `timesheet_type` | `int[]` |
| `enable_sd_storage` | `bool` |
| `timesheets_custom_signature_text` | `string` |
| `timesheets_week_start_day` | `int` |
| `use_24_hour_mode` | `bool` |
| `timesheets_tab_enabled` | `bool` |
| `timecard_should_track_location` | `int[]` |
| `projects_timecard_in_out_enabled` | `int[]` |
| `rounding_configuration` | `RestV10CompanyConfigurationGetResponse200RoundingConfiguration` |
| `time_and_materials_company_config` | `RestV10CompanyConfigurationGetResponse200TimeAndMaterialsCompanyConfig` |
| `projects_timecard_default_lunch_time` | `RestV10CompanyConfigurationGetResponse200ProjectsTimecardDefaultLunchTimeItem[]` |
| `projects_timecard_default_start_time` | `RestV10CompanyConfigurationGetResponse200ProjectsTimecardDefaultStartTimeItem[]` |
| `projects_timecard_default_stop_time` | `RestV10CompanyConfigurationGetResponse200ProjectsTimecardDefaultStopTimeItem[]` |
| `projects_timecard_lunch_time_tracking` | `RestV10CompanyConfigurationGetResponse200ProjectsTimecardLunchTimeTrackingItem[]` |
| `task_codes_enabled` | `bool` |
| `timecard_employees_can_select_non_budgeted_items` | `int[]` |
| `timecards_private` | `bool` |
| `timesheet_default_cost_type_id` | `int` |
| `timesheet_erp_default_cost_type_id` | `int` |
| `timesheet_equipment_default_cost_type_id` | `int` |
| `timesheet_equipment_erp_default_cost_type_id` | `int` |

### Nested Types
- `RestV10CompanyConfigurationGetResponse200ProjectsTimecardDefaultLunchTimeItem`
- `RestV10CompanyConfigurationGetResponse200ProjectsTimecardDefaultStartTimeItem`
- `RestV10CompanyConfigurationGetResponse200ProjectsTimecardDefaultStopTimeItem`
- `RestV10CompanyConfigurationGetResponse200ProjectsTimecardLunchTimeTrackingItem`
- `RestV10CompanyConfigurationGetResponse200RoundingConfiguration`
- `RestV10CompanyConfigurationGetResponse200TimeAndMaterialsCompanyConfig`

## RestV10CompanyConfigurationGetResponse200ProjectsTimecardDefaultLunchTimeItem
- Role: nested
- Parent: RestV10CompanyConfigurationGetResponse200DataObject
- Schema Name: RestV10CompanyConfigurationGetResponse200ProjectsTimecardDefaultLunchTimeItem
- Schema ID: schema:anon/ac7194ac8da4f8b5a3a8e9b642f3753617fedf15
- Primary Key: ProjectId

### Fields

| Field | Type |
|------|------|
| `project_id` | `int` |
| `timecard_default_lunch_time` | `int` |

## RestV10CompanyConfigurationGetResponse200ProjectsTimecardDefaultStartTimeItem
- Role: nested
- Parent: RestV10CompanyConfigurationGetResponse200DataObject
- Schema Name: RestV10CompanyConfigurationGetResponse200ProjectsTimecardDefaultStartTimeItem
- Schema ID: schema:anon/7b8fe52571c917f943bd75f0db046635adf62086
- Primary Key: ProjectId

### Fields

| Field | Type |
|------|------|
| `project_id` | `int` |
| `timecard_default_start_time` | `string` |

## RestV10CompanyConfigurationGetResponse200ProjectsTimecardDefaultStopTimeItem
- Role: nested
- Parent: RestV10CompanyConfigurationGetResponse200DataObject
- Schema Name: RestV10CompanyConfigurationGetResponse200ProjectsTimecardDefaultStopTimeItem
- Schema ID: schema:anon/058b41894e5b4e7c51ca6549ce45365b6973de86
- Primary Key: ProjectId

### Fields

| Field | Type |
|------|------|
| `project_id` | `int` |
| `timecard_default_stop_time` | `string` |

## RestV10CompanyConfigurationGetResponse200ProjectsTimecardLunchTimeTrackingItem
- Role: nested
- Parent: RestV10CompanyConfigurationGetResponse200DataObject
- Schema Name: RestV10CompanyConfigurationGetResponse200ProjectsTimecardLunchTimeTrackingItem
- Schema ID: schema:anon/c0f2f6024ae523488a699bb683c6a9d1a5f6ee0a
- Primary Key: ProjectId

### Fields

| Field | Type |
|------|------|
| `project_id` | `int` |
| `timecard_lunch_time_tracking` | `string` |

## RestV10CompanyConfigurationGetResponse200RoundingConfiguration
- Role: nested
- Parent: RestV10CompanyConfigurationGetResponse200DataObject
- Schema Name: RestV10CompanyConfigurationGetResponse200RoundingConfiguration
- Schema ID: schema:anon/890ad2fcde53a20e1249fb967502656d37153de9

### Fields

| Field | Type |
|------|------|
| `rule` | `string` |
| `time_increment` | `int` |

## RestV10CompanyConfigurationGetResponse200TimeAndMaterialsCompanyConfig
- Role: nested
- Parent: RestV10CompanyConfigurationGetResponse200DataObject
- Schema Name: RestV10CompanyConfigurationGetResponse200TimeAndMaterialsCompanyConfig
- Schema ID: schema:anon/ded372c21186e6e74d4f0b502575fda3d79f2264

### Fields

| Field | Type |
|------|------|
| `materials_enabled` | `bool` |
| `labor_enabled` | `bool` |
| `equipment_enabled` | `bool` |
| `subcontractors_enabled` | `bool` |
