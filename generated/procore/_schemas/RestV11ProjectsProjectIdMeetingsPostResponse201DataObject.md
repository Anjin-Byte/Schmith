# RestV11ProjectsProjectIdMeetingsPostResponse201DataObject

## RestV11ProjectsProjectIdMeetingsPostResponse201DataObject
- Role: parent
- Schema Name: RestV11ProjectsProjectIdMeetingsPostResponse201
- Schema ID: schema:anon/1ed424da2853eed24c259695e7a33aa56d7c702e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `meeting_template_id` | `int` |
| `position` | `int` |
| `created_by_id` | `int` |
| `title` | `string` |
| `location` | `string` |
| `occurred` | `bool` |
| `starts_at` | `string` |
| `ends_at` | `string` |
| `time_zone` | `string` |
| `is_private` | `bool` |
| `is_draft` | `bool` |
| `mode` | `RestV11ProjectsProjectIdMeetingsPostResponse201Mode` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `description` | `string` |
| `conclusion` | `string` |
| `remote_meeting_url` | `string` |
| `attachments` | `RestV11ProjectsProjectIdMeetingsPostResponse201AttachmentsItem[]` |
| `attendees` | `RestV11ProjectsProjectIdMeetingsPostResponse201AttendeesItem[]` |
| `meeting_categories` | `RestV11ProjectsProjectIdMeetingsPostResponse201MeetingCategoriesItem[]` |

### Nested Types
- `RestV11ProjectsProjectIdMeetingsPostResponse201AttachmentsItem`
- `RestV11ProjectsProjectIdMeetingsPostResponse201AttendeesItem`
- `RestV11ProjectsProjectIdMeetingsPostResponse201AttendeesItemLoginInformation`
- `RestV11ProjectsProjectIdMeetingsPostResponse201AttendeesItemStatus`
- `RestV11ProjectsProjectIdMeetingsPostResponse201MeetingCategoriesItem`
- `RestV11ProjectsProjectIdMeetingsPostResponse201MeetingCategoriesItemMeetingTopicItem`
- `RestV11ProjectsProjectIdMeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemMeetingCategory`
- `RestV11ProjectsProjectIdMeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemPriority`
- `RestV11ProjectsProjectIdMeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemStatus`
- `RestV11ProjectsProjectIdMeetingsPostResponse201Mode`

## RestV11ProjectsProjectIdMeetingsPostResponse201AttachmentsItem
- Role: nested
- Parent: RestV11ProjectsProjectIdMeetingsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdMeetingsPostResponse201AttachmentsItem
- Schema ID: schema:anon/c337dee3df228286468f0ff6d8c4852152f75cf4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |

## RestV11ProjectsProjectIdMeetingsPostResponse201AttendeesItem
- Role: nested
- Parent: RestV11ProjectsProjectIdMeetingsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdMeetingsPostResponse201AttendeesItem
- Schema ID: schema:anon/d9758364e87331486f6148ec22cd7981c9882f2c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `status` | `RestV11ProjectsProjectIdMeetingsPostResponse201AttendeesItemStatus` |
| `login_information` | `RestV11ProjectsProjectIdMeetingsPostResponse201AttendeesItemLoginInformation` |

## RestV11ProjectsProjectIdMeetingsPostResponse201AttendeesItemLoginInformation
- Role: nested
- Parent: RestV11ProjectsProjectIdMeetingsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdMeetingsPostResponse201AttendeesItemLoginInformation
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV11ProjectsProjectIdMeetingsPostResponse201AttendeesItemStatus
- Role: nested
- Parent: RestV11ProjectsProjectIdMeetingsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdMeetingsPostResponse201AttendeesItemStatus
- Schema ID: schema:anon/c075aace11a4991897fd8dfb489d62c01cf336d9

### Enum

Values: Present, Absent, For Distribution Only, Conference, None

## RestV11ProjectsProjectIdMeetingsPostResponse201MeetingCategoriesItem
- Role: nested
- Parent: RestV11ProjectsProjectIdMeetingsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdMeetingsPostResponse201MeetingCategoriesItem
- Schema ID: schema:anon/1f777025bb96453a5cb43f794549ba9083fe9912
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `title` | `string` |
| `position` | `int` |
| `meeting_topic` | `RestV11ProjectsProjectIdMeetingsPostResponse201MeetingCategoriesItemMeetingTopicItem[]` |

## RestV11ProjectsProjectIdMeetingsPostResponse201MeetingCategoriesItemMeetingTopicItem
- Role: nested
- Parent: RestV11ProjectsProjectIdMeetingsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdMeetingsPostResponse201MeetingCategoriesItemMeetingTopicItem
- Schema ID: schema:anon/abb09eca183ed987987d22b9c68564a48fcac7c6
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `number` | `string` |
| `created_on` | `string` |
| `position` | `int` |
| `due_date` | `string` |
| `priority` | `RestV11ProjectsProjectIdMeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemPriority` |
| `status` | `RestV11ProjectsProjectIdMeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemStatus` |
| `title` | `string` |
| `minutes` | `string` |
| `description` | `string` |
| `meeting_category` | `RestV11ProjectsProjectIdMeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemMeetingCategory` |
| `assignments` | `RestV11ProjectsProjectIdMeetingsPostResponse201AttendeesItemLoginInformation[]` |
| `attachments` | `RestV11ProjectsProjectIdMeetingsPostResponse201AttachmentsItem[]` |
| `download_all_url` | `string` |

## RestV11ProjectsProjectIdMeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemMeetingCategory
- Role: nested
- Parent: RestV11ProjectsProjectIdMeetingsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdMeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemMeetingCategory
- Schema ID: schema:anon/471fe4bc2ef0a1418a362e896803678bc704923a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `title` | `string` |

## RestV11ProjectsProjectIdMeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemPriority
- Role: nested
- Parent: RestV11ProjectsProjectIdMeetingsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdMeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemPriority
- Schema ID: schema:anon/dcba677e5de0d2a9c2feb61d08a7d60c95985e4d

### Enum

Values: , High, Medium, Low

## RestV11ProjectsProjectIdMeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemStatus
- Role: nested
- Parent: RestV11ProjectsProjectIdMeetingsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdMeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemStatus
- Schema ID: schema:anon/127585b0435e9d7b05a654d248dbe8babb051b49

### Enum

Values: Open, On Hold, Closed

## RestV11ProjectsProjectIdMeetingsPostResponse201Mode
- Role: nested
- Parent: RestV11ProjectsProjectIdMeetingsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdMeetingsPostResponse201Mode
- Schema ID: schema:anon/2fd56d1170f528ff30473148e32ed8e64c6b0c46

### Enum

Values: minutes, agenda
