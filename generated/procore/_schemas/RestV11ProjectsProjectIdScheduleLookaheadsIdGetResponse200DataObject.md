# RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200DataObject

## RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200DataObject
- Role: parent
- Schema Name: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200
- Schema ID: schema:anon/54711a015c2b3017f7c6df2d02144ec3598d6ac6
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `start_date` | `string` |
| `end_date` | `string` |
| `created_at` | `string` |
| `data_date` | `string` |
| `created_by` | `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200CreatedBy` |
| `label` | `string` |
| `lookahead_tasks` | `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItem[]` |
| `generation_errors` | `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200GenerationErrorsItem[]` |
| `status` | `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200Status` |
| `weeks` | `int` |

### Nested Types
- `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200CreatedBy`
- `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200GenerationErrorsItem`
- `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200GenerationErrorsItemTask`
- `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItem`
- `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemAssigneesItem`
- `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemResourcesItem`
- `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemSegmentsItem`
- `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemSegmentsItemStatus`
- `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemSubtasksItem`
- `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemTask`
- `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemVendorsItem`
- `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200Status`

## RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200CreatedBy
- Role: nested
- Parent: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200CreatedBy
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200GenerationErrorsItem
- Role: nested
- Parent: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200GenerationErrorsItem
- Schema ID: schema:anon/584b624289d96de46fb39cf11900ae8980cd1e99

### Fields

| Field | Type |
|------|------|
| `task` | `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200GenerationErrorsItemTask` |
| `errors` | `string[]` |

## RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200GenerationErrorsItemTask
- Role: nested
- Parent: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200GenerationErrorsItemTask
- Schema ID: schema:anon/5b4d5d33ae8fb352a756ba414c9b6fe25e07cb35
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `row_number` | `int` |
| `name` | `string` |

## RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItem
- Role: nested
- Parent: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItem
- Schema ID: schema:anon/f54890c2c5a96081e0bdba2ca8ffd17e0a5340e7
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `parent_id` | `int` |
| `name` | `string` |
| `row_number` | `int` |
| `critical_path` | `bool` |
| `comment` | `string` |
| `activity_id` | `string` |
| `wbs` | `string` |
| `segments` | `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemSegmentsItem[]` |
| `resources` | `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemResourcesItem[]` |
| `assignees` | `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemAssigneesItem[]` |
| `vendors` | `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemVendorsItem[]` |
| `task` | `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemTask` |
| `subtasks` | `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemSubtasksItem[]` |

## RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemAssigneesItem
- Role: nested
- Parent: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemAssigneesItem
- Schema ID: schema:anon/b1355c88aaf4427a87a24cf1a36027307bb7133f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `email` | `string` |
| `login_information_id` | `int` |
| `name` | `string` |

## RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemResourcesItem
- Role: nested
- Parent: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemResourcesItem
- Schema ID: schema:anon/03e9b805924d6c3ba795e1519da15da7320925a2
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `company_id` | `int` |
| `deleted_at` | `string` |
| `project_id` | `int` |
| `source_uid` | `string` |

## RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemSegmentsItem
- Role: nested
- Parent: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemSegmentsItem
- Schema ID: schema:anon/6cbe154d3e84b1c159495cd674874f7d8c7100ea

### Fields

| Field | Type |
|------|------|
| `date` | `string` |
| `status` | `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemSegmentsItemStatus` |

## RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemSegmentsItemStatus
- Role: nested
- Parent: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemSegmentsItemStatus
- Schema ID: schema:anon/b50244db7bf93cc4be52dc6f00011c9dc3613cf5

### Enum

Values: blank, complete, incomplete

## RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemSubtasksItem
- Role: nested
- Parent: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemSubtasksItem
- Schema ID: schema:anon/6740cb7dc43cdc896afb38e27b3bf758930fb37c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `parent_id` | `int` |
| `name` | `string` |
| `row_number` | `int` |
| `critical_path` | `bool` |
| `comment` | `string` |
| `activity_id` | `string` |
| `wbs` | `string` |
| `segments` | `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemSegmentsItem[]` |
| `resources` | `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemResourcesItem[]` |
| `assignees` | `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemAssigneesItem[]` |
| `vendors` | `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemVendorsItem[]` |
| `task` | `RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemTask` |
| `subtasks` | `object[]` |

## RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemTask
- Role: nested
- Parent: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemTask
- Schema ID: schema:anon/02592b544f98c50c6f7aefaaad0cefbc4118e166
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `finish` | `string` |
| `start` | `string` |

## RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemVendorsItem
- Role: nested
- Parent: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200LookaheadTasksItemVendorsItem
- Schema ID: schema:anon/e21f8241163879c3073268051eae91fec2da42ce
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200Status
- Role: nested
- Parent: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdScheduleLookaheadsIdGetResponse200Status
- Schema ID: schema:anon/842b315bc861a866e35f5ade07997b125559eb40

### Enum

Values: queued, processing_previous_lookahead, processing_master_schedule, ready
