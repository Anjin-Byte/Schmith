# RestV10ProjectsProjectIdDailyLogsClonesPostResponse201DataObject

## RestV10ProjectsProjectIdDailyLogsClonesPostResponse201DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdDailyLogsClonesPostResponse201
- Schema ID: schema:anon/db56d20f4a15b6b217919c1f66fdaa9eb83c5071

### Fields

| Field | Type |
|------|------|
| `notes_log` | `RestV10ProjectsProjectIdDailyLogsClonesPostResponse201NotesLog` |

### Nested Types
- `RestV10ProjectsProjectIdDailyLogsClonesPostResponse201NotesLog`
- `RestV10ProjectsProjectIdDailyLogsClonesPostResponse201NotesLogCreatedBy`
- `RestV10ProjectsProjectIdDailyLogsClonesPostResponse201NotesLogPermissions`

## RestV10ProjectsProjectIdDailyLogsClonesPostResponse201NotesLog
- Role: nested
- Parent: RestV10ProjectsProjectIdDailyLogsClonesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdDailyLogsClonesPostResponse201NotesLog
- Schema ID: schema:anon/5e1bc47ecc90ca6228fdabdaf0cf6e7ba26ca124
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `double` |
| `comment` | `string` |
| `created_at` | `string` |
| `created_by_collaborator` | `bool` |
| `custom_fields` | `object` |
| `date` | `string` |
| `datetime` | `string` |
| `daily_log_header_id` | `double` |
| `deleted_at` | `string` |
| `is_issue_day` | `string` |
| `permissions` | `RestV10ProjectsProjectIdDailyLogsClonesPostResponse201NotesLogPermissions` |
| `position` | `double` |
| `updated_at` | `string` |
| `status` | `string` |
| `attachments` | `RestV10ProjectsProjectIdDailyLogsClonesPostResponse201NotesLogCustomFields[]` |
| `created_by` | `RestV10ProjectsProjectIdDailyLogsClonesPostResponse201NotesLogCreatedBy` |
| `location` | `string` |

## RestV10ProjectsProjectIdDailyLogsClonesPostResponse201NotesLogCreatedBy
- Role: nested
- Parent: RestV10ProjectsProjectIdDailyLogsClonesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdDailyLogsClonesPostResponse201NotesLogCreatedBy
- Schema ID: schema:anon/48cbb491d5bf9bcbe9d4989a158c348c87d685f3
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `double` |
| `login` | `string` |
| `name` | `string` |

## RestV10ProjectsProjectIdDailyLogsClonesPostResponse201NotesLogPermissions
- Role: nested
- Parent: RestV10ProjectsProjectIdDailyLogsClonesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdDailyLogsClonesPostResponse201NotesLogPermissions
- Schema ID: schema:anon/cdf4f239f0e8a22c2f5aed1003d9522374b8b46e

### Fields

| Field | Type |
|------|------|
| `can_update` | `bool` |
| `can_delete` | `bool` |
