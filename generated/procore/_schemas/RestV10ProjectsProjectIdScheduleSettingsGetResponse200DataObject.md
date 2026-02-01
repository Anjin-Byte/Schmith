# RestV10ProjectsProjectIdScheduleSettingsGetResponse200DataObject

## RestV10ProjectsProjectIdScheduleSettingsGetResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdScheduleSettingsGetResponse200
- Schema ID: schema:anon/8afb703b221d0c1048344bd9f28c5b024fbbdee7
- Primary Key: ProjectId

### Fields

| Field | Type |
|------|------|
| `project_id` | `int` |
| `company_id` | `int` |
| `primavera_schedule_id` | `string` |
| `schedule_type` | `string` |
| `schedule_file_pattern` | `string` |
| `project_integration` | `bool` |
| `display_task_names_with_full_outline_path` | `bool` |
| `schedule_show_resources_on_calendar` | `bool` |
| `schedule_allow_task_updates` | `bool` |
| `schedule_task_auto_formatting` | `bool` |
| `create_calendar_item_enabled` | `bool` |
| `calendar_people_filters_enabled` | `bool` |
| `schedule_use_project_admin_working_days` | `bool` |
| `email_settings` | `RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettings` |

### Nested Types
- `RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettings`
- `RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsDayOfWeek`
- `RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsHourToSend`
- `RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsLookaheadDayOfWeek`
- `RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsLookaheadHourToSend`
- `RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsResourceDayOfWeek`
- `RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsResourceHourToSend`
- `RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsResourceWeeksToShow`
- `RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsWeeksToShow`

## RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettings
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleSettingsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettings
- Schema ID: schema:anon/1fa0c9113211d150d9007913ce369b4e8cb01b3d
- Primary Key: ProjectScheduleEmailSettingId

### Fields

| Field | Type |
|------|------|
| `project_schedule_email_setting_id` | `int` |
| `send_weekly` | `bool` |
| `day_of_week` | `RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsDayOfWeek` |
| `hour_to_send` | `RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsHourToSend` |
| `weeks_to_show` | `RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsWeeksToShow` |
| `last_sent_at` | `string` |
| `next_scheduled_at` | `string` |
| `lookahead_send_weekly` | `bool` |
| `lookahead_day_of_week` | `RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsLookaheadDayOfWeek` |
| `lookahead_hour_to_send` | `RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsLookaheadHourToSend` |
| `lookahead_last_sent_at` | `string` |
| `lookahead_next_scheduled_at` | `string` |
| `resource_send_weekly` | `bool` |
| `resource_day_of_week` | `RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsResourceDayOfWeek` |
| `resource_hour_to_send` | `RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsResourceHourToSend` |
| `resource_weeks_to_show` | `RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsResourceWeeksToShow` |
| `resource_last_sent_at` | `string` |
| `resource_next_scheduled_at` | `string` |

## RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsDayOfWeek
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleSettingsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsDayOfWeek
- Schema ID: schema:anon/37c82922bc3c0630c5eb0b29abbe0307e2f6ca5a

### Enum

Values: 0, 1, 2, 3, 4, 5, 6

## RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsHourToSend
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleSettingsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsHourToSend
- Schema ID: schema:anon/e19234bf90acd3c16d5af8a1cce70e3d68af1646

### Enum

Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23

## RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsLookaheadDayOfWeek
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleSettingsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsLookaheadDayOfWeek
- Schema ID: schema:anon/8e98c32a83af97b69c1f4a65b658a88db04f25b0

### Enum

Values: 0, 1, 2, 3, 4, 5, 6

## RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsLookaheadHourToSend
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleSettingsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsLookaheadHourToSend
- Schema ID: schema:anon/e20314b30f6bcf8054b861c30473fd7ba561b588

### Enum

Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23

## RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsResourceDayOfWeek
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleSettingsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsResourceDayOfWeek
- Schema ID: schema:anon/eee28e601dca696387a6d88ece29daa43a454cde

### Enum

Values: 0, 1, 2, 3, 4, 5, 6

## RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsResourceHourToSend
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleSettingsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsResourceHourToSend
- Schema ID: schema:anon/020408e172bb7ca85edee07fbd7647df16b9f602

### Enum

Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23

## RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsResourceWeeksToShow
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleSettingsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsResourceWeeksToShow
- Schema ID: schema:anon/fbfd8db8d49e9a92130cd1f4880c7ee1967a542a

### Enum

Values: 1, 2, 3, 4, 5, 6, 7, 8

## RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsWeeksToShow
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleSettingsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleSettingsGetResponse200EmailSettingsWeeksToShow
- Schema ID: schema:anon/0962fb90d7d70cdea9893be78b470ade5ca226e4

### Enum

Values: 1, 2, 3, 4, 5, 6, 7, 8
