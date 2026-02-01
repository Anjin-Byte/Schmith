# RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200DataObject

## RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200
- Schema ID: schema:anon/92a4a7f03c54fc5a08872e3cf773af482113acd2

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200EntitiesItem[]` |
| `errors` | `RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200ErrorsItem[]` |

### Nested Types
- `RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200EntitiesItem`
- `RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200EntitiesItemAssigned`
- `RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200ErrorsItem`
- `RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200ErrorsItemErrors`

## RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200EntitiesItem
- Schema ID: schema:anon/0bcc55bf3544766c66788d49c7331f543978dffb
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `assigned` | `RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200EntitiesItemAssigned` |
| `color` | `string` |
| `created_by` | `RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200EntitiesItemAssigned` |
| `description` | `string` |
| `finish` | `string` |
| `full_outline_path` | `string` |
| `milestone` | `bool` |
| `name` | `string` |
| `percentage` | `int` |
| `private` | `bool` |
| `start` | `string` |
| `task_name` | `string` |
| `updated_at` | `string` |

## RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200EntitiesItemAssigned
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200EntitiesItemAssigned
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200ErrorsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200ErrorsItem
- Schema ID: schema:anon/7abdf4f55a4d2c36a8a9be6450ac089d3cedf818

### Fields

| Field | Type |
|------|------|
| `errors` | `RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200ErrorsItemErrors` |

## RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200ErrorsItemErrors
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatchResponse200ErrorsItemErrors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
