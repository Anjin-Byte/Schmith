# RestV10ProjectsProjectIdScheduleLookaheadTasksPostResponse201DataObject

## RestV10ProjectsProjectIdScheduleLookaheadTasksPostResponse201DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdScheduleLookaheadTasksPostResponse201
- Schema ID: schema:anon/26c496f38ee7b25803ffff3cff12750ed675570f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `project_id` | `int` |
| `company_id` | `int` |
| `lookahead_id` | `int` |
| `task_id` | `int` |
| `created_at` | `string` |
| `created_by_id` | `int` |
| `parent_id` | `int` |
| `name` | `string` |
| `start_date` | `string` |
| `end_date` | `string` |
| `row_number` | `int` |
| `critical_path` | `bool` |
| `comment` | `string` |
| `activity_id` | `string` |
| `wbs` | `string` |
| `assignee_ids` | `int[]` |
| `resource_ids` | `int[]` |
| `vendor_ids` | `int[]` |
| `segments` | `RestV10ProjectsProjectIdScheduleLookaheadTasksPostResponse201SegmentsItem[]` |
| `resources` | `RestV10ProjectsProjectIdScheduleLookaheadTasksPostResponse201ResourcesItem[]` |

### Nested Types
- `RestV10ProjectsProjectIdScheduleLookaheadTasksPostResponse201ResourcesItem`
- `RestV10ProjectsProjectIdScheduleLookaheadTasksPostResponse201SegmentsItem`
- `RestV10ProjectsProjectIdScheduleLookaheadTasksPostResponse201SegmentsItemStatus`

## RestV10ProjectsProjectIdScheduleLookaheadTasksPostResponse201ResourcesItem
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleLookaheadTasksPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleLookaheadTasksPostResponse201ResourcesItem
- Schema ID: schema:anon/ddace1a4adea6244c117059c9672b533fa539aa3

### Fields

## RestV10ProjectsProjectIdScheduleLookaheadTasksPostResponse201SegmentsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleLookaheadTasksPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleLookaheadTasksPostResponse201SegmentsItem
- Schema ID: schema:anon/07fb401dd0195eb0682331149c52341ca8b534e1

### Fields

| Field | Type |
|------|------|
| `date` | `string` |
| `status` | `RestV10ProjectsProjectIdScheduleLookaheadTasksPostResponse201SegmentsItemStatus` |

## RestV10ProjectsProjectIdScheduleLookaheadTasksPostResponse201SegmentsItemStatus
- Role: nested
- Parent: RestV10ProjectsProjectIdScheduleLookaheadTasksPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdScheduleLookaheadTasksPostResponse201SegmentsItemStatus
- Schema ID: schema:anon/dfa55d793784fd6d67f7c73475666a04b0334cd9

### Enum

Values: blank, complete, incomplete
