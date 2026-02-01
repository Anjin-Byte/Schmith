# RestV10TasksSyncPatchResponse200DataObject

## RestV10TasksSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10TasksSyncPatchResponse200
- Schema ID: schema:anon/4543ceceffbb0849a6f6ed3af36cf768273539e7

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10TasksSyncPatchResponse200EntitiesItem[]` |
| `errors` | `RestV10TasksSyncPatchResponse200ErrorsItem[]` |

### Nested Types
- `RestV10TasksSyncPatchResponse200EntitiesItem`
- `RestV10TasksSyncPatchResponse200EntitiesItemCreatedBy`
- `RestV10TasksSyncPatchResponse200ErrorsItem`
- `RestV10TasksSyncPatchResponse200ErrorsItem_7abdf4Errors`

## RestV10TasksSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10TasksSyncPatchResponse200DataObject
- Schema Name: RestV10TasksSyncPatchResponse200EntitiesItem
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
| `created_by` | `RestV10TasksSyncPatchResponse200EntitiesItemCreatedBy` |
| `updated_by` | `RestV10TasksSyncPatchResponse200EntitiesItemCreatedBy` |

## RestV10TasksSyncPatchResponse200EntitiesItemCreatedBy
- Role: nested
- Parent: RestV10TasksSyncPatchResponse200DataObject
- Schema Name: RestV10TasksSyncPatchResponse200EntitiesItemCreatedBy
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10TasksSyncPatchResponse200ErrorsItem
- Role: nested
- Parent: RestV10TasksSyncPatchResponse200DataObject
- Schema Name: RestV10TasksSyncPatchResponse200ErrorsItem
- Schema ID: schema:anon/862fdf4bb01e3cfa1130bb2c41cc066b024a17ef
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
| `created_by` | `RestV10TasksSyncPatchResponse200EntitiesItemCreatedBy` |
| `updated_by` | `RestV10TasksSyncPatchResponse200EntitiesItemCreatedBy` |
| `errors` | `RestV10TasksSyncPatchResponse200ErrorsItem_7abdf4Errors` |

## RestV10TasksSyncPatchResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10TasksSyncPatchResponse200DataObject
- Schema Name: RestV10TasksSyncPatchResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
