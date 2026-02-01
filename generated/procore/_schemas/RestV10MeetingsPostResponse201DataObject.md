# RestV10MeetingsPostResponse201DataObject

## RestV10MeetingsPostResponse201DataObject
- Role: parent
- Schema Name: RestV10MeetingsPostResponse201
- Schema ID: schema:anon/360bdd30cde5d354c939764ae090aefb0e68d08e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `position` | `int` |
| `created_by_id` | `int` |
| `title` | `string` |
| `location` | `string` |
| `meeting_date` | `string` |
| `occurred` | `bool` |
| `start_time` | `string` |
| `finish_time` | `string` |
| `time_zone` | `string` |
| `is_private` | `bool` |
| `is_draft` | `bool` |
| `mode` | `RestV10MeetingsPostResponse201Mode` |
| `description` | `string` |
| `conclusion` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `attachments` | `RestV10MeetingsPostResponse201AttachmentsItem[]` |
| `attendees` | `RestV10MeetingsPostResponse201AttendeesItem[]` |
| `meeting_categories` | `RestV10MeetingsPostResponse201MeetingCategoriesItem[]` |

### Nested Types
- `RestV10MeetingsPostResponse201AttachmentsItem`
- `RestV10MeetingsPostResponse201AttendeesItem`
- `RestV10MeetingsPostResponse201AttendeesItemLoginInformation`
- `RestV10MeetingsPostResponse201MeetingCategoriesItem`
- `RestV10MeetingsPostResponse201MeetingCategoriesItemMeetingTopicItem`
- `RestV10MeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemMeetingCategory`
- `RestV10MeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemPriority`
- `RestV10MeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemStatus`
- `RestV10MeetingsPostResponse201Mode`

## RestV10MeetingsPostResponse201AttachmentsItem
- Role: nested
- Parent: RestV10MeetingsPostResponse201DataObject
- Schema Name: RestV10MeetingsPostResponse201AttachmentsItem
- Schema ID: schema:anon/c337dee3df228286468f0ff6d8c4852152f75cf4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |

## RestV10MeetingsPostResponse201AttendeesItem
- Role: nested
- Parent: RestV10MeetingsPostResponse201DataObject
- Schema Name: RestV10MeetingsPostResponse201AttendeesItem
- Schema ID: schema:anon/bb11a8ebf28303e3f3d37e86e3aa922a32092000
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `status` | `string` |
| `login_information` | `RestV10MeetingsPostResponse201AttendeesItemLoginInformation` |

## RestV10MeetingsPostResponse201AttendeesItemLoginInformation
- Role: nested
- Parent: RestV10MeetingsPostResponse201DataObject
- Schema Name: RestV10MeetingsPostResponse201AttendeesItemLoginInformation
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10MeetingsPostResponse201MeetingCategoriesItem
- Role: nested
- Parent: RestV10MeetingsPostResponse201DataObject
- Schema Name: RestV10MeetingsPostResponse201MeetingCategoriesItem
- Schema ID: schema:anon/fced65a600ec48f8d3df81540d29d3aa114726e9
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `title` | `string` |
| `position` | `int` |
| `meeting_topic` | `RestV10MeetingsPostResponse201MeetingCategoriesItemMeetingTopicItem[]` |

## RestV10MeetingsPostResponse201MeetingCategoriesItemMeetingTopicItem
- Role: nested
- Parent: RestV10MeetingsPostResponse201DataObject
- Schema Name: RestV10MeetingsPostResponse201MeetingCategoriesItemMeetingTopicItem
- Schema ID: schema:anon/33c3025607f9cc4bbe90203cc14262281e57665d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `number` | `string` |
| `created_on` | `string` |
| `position` | `int` |
| `due_date` | `string` |
| `priority` | `RestV10MeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemPriority` |
| `status` | `RestV10MeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemStatus` |
| `title` | `string` |
| `minutes` | `string` |
| `description` | `string` |
| `meeting_category` | `RestV10MeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemMeetingCategory` |
| `assignments` | `RestV10MeetingsPostResponse201AttendeesItemLoginInformation[]` |
| `attachments` | `RestV10MeetingsPostResponse201AttachmentsItem[]` |

## RestV10MeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemMeetingCategory
- Role: nested
- Parent: RestV10MeetingsPostResponse201DataObject
- Schema Name: RestV10MeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemMeetingCategory
- Schema ID: schema:anon/471fe4bc2ef0a1418a362e896803678bc704923a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `title` | `string` |

## RestV10MeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemPriority
- Role: nested
- Parent: RestV10MeetingsPostResponse201DataObject
- Schema Name: RestV10MeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemPriority
- Schema ID: schema:anon/dcba677e5de0d2a9c2feb61d08a7d60c95985e4d

### Enum

Values: , High, Medium, Low

## RestV10MeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemStatus
- Role: nested
- Parent: RestV10MeetingsPostResponse201DataObject
- Schema Name: RestV10MeetingsPostResponse201MeetingCategoriesItemMeetingTopicItemStatus
- Schema ID: schema:anon/127585b0435e9d7b05a654d248dbe8babb051b49

### Enum

Values: Open, On Hold, Closed

## RestV10MeetingsPostResponse201Mode
- Role: nested
- Parent: RestV10MeetingsPostResponse201DataObject
- Schema Name: RestV10MeetingsPostResponse201Mode
- Schema ID: schema:anon/2fd56d1170f528ff30473148e32ed8e64c6b0c46

### Enum

Values: minutes, agenda
