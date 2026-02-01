# RestV11ProjectsProjectIdDrawingUploadsPostResponse200DataObject

## RestV11ProjectsProjectIdDrawingUploadsPostResponse200DataObject
- Role: parent
- Schema Name: RestV11ProjectsProjectIdDrawingUploadsPostResponse200
- Schema ID: schema:anon/0f44edc6fdca89d83f631785a7bb20f005c1aa52
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `project_id` | `int` |
| `company_id` | `int` |
| `created_by_id` | `int` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `error_email_sent` | `bool` |
| `notify_on_success` | `bool` |
| `deletion_in_progress` | `bool` |
| `success_email_sent` | `bool` |
| `drawing_area_id` | `int` |
| `status` | `RestV11ProjectsProjectIdDrawingUploadsPostResponse200Status` |
| `pre_adaptive_complete` | `bool` |
| `drawing_number_contains_revision` | `bool` |
| `get_info_from_filename` | `bool` |
| `language` | `string` |

### Nested Types
- `RestV11ProjectsProjectIdDrawingUploadsPostResponse200Status`

## RestV11ProjectsProjectIdDrawingUploadsPostResponse200Status
- Role: nested
- Parent: RestV11ProjectsProjectIdDrawingUploadsPostResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdDrawingUploadsPostResponse200Status
- Schema ID: schema:anon/8732639ab6c22d15a053284c45095939037ce917

### Enum

Values: in_queue, in_progress, mechanical_turk, failed, ready_for_review, reviewed
