# RestV10ProjectsProjectIdScheduleGetResponse200DataObject

## RestV10ProjectsProjectIdScheduleGetResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdScheduleGetResponse200
- Schema ID: schema:anon/12af4e128db85571df5928b00798d06787eff296

### Fields

| Field | Type |
|------|------|
| `active_features` | `RestV10ProjectsProjectIdScheduleGetResponse200ActiveFeatures` |
| `last_calendar_view` | `string` |
| `schedule_present` | `bool` |
| `schedule_processing` | `bool` |
| `schedule_crud_beta_agreement` | `RestV10ProjectsProjectIdScheduleGetResponse200ScheduleCrudBetaAgreement` |
| `schedule_tasks_last_updated_at` | `string` |
| `schedule_tasks_edited_manually` | `bool` |
| `type` | `RestV10ProjectsProjectIdScheduleGetResponse200Type` |
| `data_date` | `string` |
| `lookahead_data_date` | `string` |
| `number_of_pending_requested_changes` | `double` |
| `uploaded_at` | `string` |
| `office` | `RestV10ProjectsProjectIdScheduleGetResponse200Office` |
| `project` | `RestV10ProjectsProjectIdScheduleGetResponse200Project` |

### Nested Types
- `RestV10ProjectsProjectIdScheduleGetResponse200ActiveFeatures`
- `RestV10ProjectsProjectIdScheduleGetResponse200Office`
- `RestV10ProjectsProjectIdScheduleGetResponse200OfficeLogo`
- `RestV10ProjectsProjectIdScheduleGetResponse200Project`
- `RestV10ProjectsProjectIdScheduleGetResponse200ScheduleCrudBetaAgreement`
- `RestV10ProjectsProjectIdScheduleGetResponse200Type`
- `RestV10ProjectsProjectIdScheduleGetResponse200TypeKey`

## RestV10ProjectsProjectIdScheduleGetResponse200ActiveFeatures
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleGetResponse200ActiveFeatures
- Schema ID: schema:anon/78000e61732f8269d3691ccd8a95d4ad419b3836

### Fields

| Field | Type |
|------|------|
| `schedule_activity_feed` | `bool` |
| `schedule_comment_mentions` | `bool` |
| `schedule_gantt_crud` | `bool` |
| `schedule_task_comments` | `bool` |
| `schedule_task_details` | `bool` |
| `schedule_linked_items` | `bool` |

## RestV10ProjectsProjectIdScheduleGetResponse200Office
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleGetResponse200Office
- Schema ID: schema:anon/70e6576558ed8f58686e469c0bf23202f2adbf02
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `address` | `string` |
| `city` | `string` |
| `state_code` | `string` |
| `country_code` | `string` |
| `zip` | `string` |
| `phone` | `string` |
| `fax` | `string` |
| `division` | `string` |
| `logo` | `RestV10ProjectsProjectIdScheduleGetResponse200OfficeLogo` |

## RestV10ProjectsProjectIdScheduleGetResponse200OfficeLogo
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleGetResponse200OfficeLogo
- Schema ID: schema:anon/6e0e2621b0a5281452753168c0bb8b79af25335f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `url` | `string` |
| `filename` | `string` |

## RestV10ProjectsProjectIdScheduleGetResponse200Project
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleGetResponse200Project
- Schema ID: schema:anon/4f6b52272e0ce3b83cc9005f664715bf4e6b4b74
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `country_code` | `string` |
| `country_name` | `string` |
| `state_code` | `string` |
| `state_name` | `string` |
| `county` | `string` |
| `city` | `string` |
| `address` | `string` |
| `zip` | `string` |
| `phone` | `string` |
| `fax` | `string` |
| `time_zone` | `string` |
| `time_zone_name` | `string` |
| `logo_url` | `string` |

## RestV10ProjectsProjectIdScheduleGetResponse200ScheduleCrudBetaAgreement
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleGetResponse200ScheduleCrudBetaAgreement
- Schema ID: schema:anon/7fb2aed467354290c68ac5d8ad1af74e669fcd92

### Fields

| Field | Type |
|------|------|
| `signed` | `bool` |
| `version` | `string` |

## RestV10ProjectsProjectIdScheduleGetResponse200Type
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleGetResponse200Type
- Schema ID: schema:anon/64f34f984557f362177b5fe5b8e3cbaca2be39e4
- Primary Key: P6Id

### Fields

| Field | Type |
|------|------|
| `key` | `RestV10ProjectsProjectIdScheduleGetResponse200TypeKey` |
| `p6_id` | `string` |

## RestV10ProjectsProjectIdScheduleGetResponse200TypeKey
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleGetResponse200TypeKey
- Schema ID: schema:anon/62b237607a68eef867d82378b0cbd8d8bf6eb01f

### Enum

Values: Microsoft Project, Microsoft Project 2010, Microsoft Project Documents, Primavera P6, None
