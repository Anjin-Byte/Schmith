# CalendarTaskDataObject

## CalendarTaskDataObject
- Role: parent
- Schema Name: CalendarTask
- Schema ID: schema:types/typ.CalendarTask
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `type` | `string` |
| `description` | `string` |
| `start_time` | `string` |
| `end_time` | `string` |
| `start_date` | `DateTime` |
| `end_date` | `DateTime` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |
| `is_public` | `bool` |
| `is_completed` | `bool` |
| `repeat_id` | `int` |
| `users_id` | `int[]` |
| `customers_id` | `int[]` |
| `jobs_id` | `int[]` |
| `estimates_id` | `int[]` |
| `repeat` | `CalendarTaskRepeat` |

### Nested Types
- `CalendarTaskRepeat`

## CalendarTaskRepeat
- Role: nested
- Parent: CalendarTaskDataObject
- Schema Name: CalendarTaskRepeat
- Schema ID: schema:types/typ.CalendarTaskRepeat
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `repeat_type` | `string` |
| `repeat_frequency` | `int` |
| `repeat_weekly_days` | `string[]` |
| `repeat_monthly_type` | `string` |
| `stop_repeat_type` | `string` |
| `stop_repeat_on_occurrence` | `int` |
| `stop_repeat_on_date` | `DateTime` |
| `start_date` | `DateTime` |
| `end_date` | `DateTime` |
