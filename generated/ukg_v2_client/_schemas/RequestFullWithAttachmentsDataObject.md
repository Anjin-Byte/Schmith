# RequestFullWithAttachmentsDataObject

## RequestFullWithAttachmentsDataObject
- Role: parent
- Schema Name: RequestFullWithAttachments
- Schema ID: schema:definitions/RequestFullWithAttachments
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `request_number` | `string` |
| `status` | `StatusEnum` |
| `read_by_employee` | `bool` |
| `public_comment_count` | `int` |
| `internal_comment_count` | `int` |
| `total_comment_count` | `int` |
| `public_deleted_comment_count` | `int` |
| `internal_deleted_comment_count` | `int` |
| `total_deleted_comment_count` | `int` |
| `attachment_count` | `int` |
| `read_only` | `bool` |
| `visible_by_employee` | `bool` |
| `need_edit_by_employee` | `bool` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `closed_at` | `string` |
| `archived_at` | `string` |
| `name` | `string` |
| `priority` | `PriorityEnum` |
| `employee` | `EmployeeSimplified` |
| `employee_id` | `string` |
| `creator` | `UserSimplified` |
| `creator_id` | `string` |
| `closed_by` | `UserSimplified` |
| `closed_by_id` | `string` |
| `organization_ids` | `string[]` |
| `form_id` | `string` |
| `form_files` | `FormFile[]` |
| `due_date` | `string` |
| `custom_status` | `CustomStatusField` |
| `category` | `RequestCategory` |
| `form_data` | `RequestFormDataFieldValue[]` |
| `feedback` | `RequestFeedback` |
| `attachments` | `RequestAttachment[]` |
