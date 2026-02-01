# RestV10CalendarEventsGetResponse200DataObject

## RestV10CalendarEventsGetResponse200DataObject
- Role: parent
- Schema Name: RestV10CalendarEventsGetResponse200
- Schema ID: schema:anon/b31d51d40b3f4065a35a6adb0caf96698cd0fddb

### Fields

| Field | Type |
|------|------|
| `schedule_tasks_last_updated_at` | `string` |
| `tasks` | `RestV10CalendarEventsGetResponse200TasksItem[]` |
| `todos` | `RestV10CalendarEventsGetResponse200TodosItem[]` |

### Nested Types
- `RestV10CalendarEventsGetResponse200TasksItem`
- `RestV10CalendarEventsGetResponse200TasksItemCreatedBy`
- `RestV10CalendarEventsGetResponse200TodosItem`

## RestV10CalendarEventsGetResponse200TasksItem
- Role: nested
- Parent: RestV10CalendarEventsGetResponse200DataObject
- Schema Name: RestV10CalendarEventsGetResponse200TasksItem
- Schema ID: schema:anon/a4fa7777c9d50b8e09e9c82dda9059719efaa618
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `task_name` | `string` |
| `key` | `string` |
| `start_datetime` | `string` |
| `finish_datetime` | `string` |
| `percentage` | `int` |
| `color` | `string` |
| `parent_id` | `int` |
| `pending` | `bool` |
| `activity_id` | `string` |
| `schedule_activity_id` | `string` |
| `resource_name` | `string` |
| `critical_path` | `bool` |
| `milestone` | `bool` |
| `actual_start` | `string` |
| `actual_finish` | `string` |
| `row_number` | `int` |
| `has_children` | `bool` |
| `full_outline_path` | `string` |
| `source_uid` | `string` |
| `wbs` | `string` |
| `schedule_duration` | `double` |
| `resource_ids` | `int[]` |
| `notes` | `string` |
| `baseline_start` | `string` |
| `baseline_finish` | `string` |
| `start_variance` | `double` |
| `finish_variance` | `double` |
| `manually_edited` | `bool` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `created_by` | `RestV10CalendarEventsGetResponse200TasksItemCreatedBy` |
| `updated_by` | `RestV10CalendarEventsGetResponse200TasksItemCreatedBy` |

## RestV10CalendarEventsGetResponse200TasksItemCreatedBy
- Role: nested
- Parent: RestV10CalendarEventsGetResponse200DataObject
- Schema Name: RestV10CalendarEventsGetResponse200TasksItemCreatedBy
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10CalendarEventsGetResponse200TodosItem
- Role: nested
- Parent: RestV10CalendarEventsGetResponse200DataObject
- Schema Name: RestV10CalendarEventsGetResponse200TodosItem
- Schema ID: schema:anon/89b0e6d4509db735673e9b924d9442472575e9ab
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `assignment` | `RestV10CalendarEventsGetResponse200TasksItemCreatedBy` |
| `color` | `string` |
| `created_by` | `RestV10CalendarEventsGetResponse200TasksItemCreatedBy` |
| `description` | `string` |
| `finish_datetime` | `string` |
| `full_outline_path` | `string` |
| `milestone` | `bool` |
| `name` | `string` |
| `percentage` | `int` |
| `private` | `bool` |
| `start_datetime` | `string` |
| `task_name` | `string` |
| `updated_at` | `string` |
