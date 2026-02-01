# RestV11ProjectsProjectIdMeetingTopicsPostResponse201DataObject

## RestV11ProjectsProjectIdMeetingTopicsPostResponse201DataObject
- Role: parent
- Schema Name: RestV11ProjectsProjectIdMeetingTopicsPostResponse201
- Schema ID: schema:anon/f6f0f42e56e1b9e37b9d346d2b2c8d049adab8aa
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `number` | `string` |
| `created_on` | `string` |
| `position` | `int` |
| `due_date` | `string` |
| `priority` | `RestV11ProjectsProjectIdMeetingTopicsPostResponse201Priority` |
| `status` | `RestV11ProjectsProjectIdMeetingTopicsPostResponse201Status` |
| `title` | `string` |
| `minutes` | `string` |
| `description` | `string` |
| `meeting_category` | `RestV11ProjectsProjectIdMeetingTopicsPostResponse201MeetingCategory` |
| `assignments` | `RestV11ProjectsProjectIdMeetingTopicsPostResponse201AssignmentsItem[]` |
| `attachments` | `RestV11ProjectsProjectIdMeetingTopicsPostResponse201AttachmentsItem[]` |

### Nested Types
- `RestV11ProjectsProjectIdMeetingTopicsPostResponse201AssignmentsItem`
- `RestV11ProjectsProjectIdMeetingTopicsPostResponse201AttachmentsItem`
- `RestV11ProjectsProjectIdMeetingTopicsPostResponse201MeetingCategory`
- `RestV11ProjectsProjectIdMeetingTopicsPostResponse201Priority`
- `RestV11ProjectsProjectIdMeetingTopicsPostResponse201Status`

## RestV11ProjectsProjectIdMeetingTopicsPostResponse201AssignmentsItem
- Role: nested
- Parent: RestV11ProjectsProjectIdMeetingTopicsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdMeetingTopicsPostResponse201AssignmentsItem
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV11ProjectsProjectIdMeetingTopicsPostResponse201AttachmentsItem
- Role: nested
- Parent: RestV11ProjectsProjectIdMeetingTopicsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdMeetingTopicsPostResponse201AttachmentsItem
- Schema ID: schema:anon/c337dee3df228286468f0ff6d8c4852152f75cf4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |

## RestV11ProjectsProjectIdMeetingTopicsPostResponse201MeetingCategory
- Role: nested
- Parent: RestV11ProjectsProjectIdMeetingTopicsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdMeetingTopicsPostResponse201MeetingCategory
- Schema ID: schema:anon/471fe4bc2ef0a1418a362e896803678bc704923a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `title` | `string` |

## RestV11ProjectsProjectIdMeetingTopicsPostResponse201Priority
- Role: nested
- Parent: RestV11ProjectsProjectIdMeetingTopicsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdMeetingTopicsPostResponse201Priority
- Schema ID: schema:anon/282e4b29261da1782394027f76d61444c681beba

### Enum

Values: , High, Medium, Low, None

## RestV11ProjectsProjectIdMeetingTopicsPostResponse201Status
- Role: nested
- Parent: RestV11ProjectsProjectIdMeetingTopicsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdMeetingTopicsPostResponse201Status
- Schema ID: schema:anon/127585b0435e9d7b05a654d248dbe8babb051b49

### Enum

Values: Open, On Hold, Closed
