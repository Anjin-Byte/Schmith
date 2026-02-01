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
| `status` | `RequestComputedFieldsStatus` |
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
| `priority` | `RequestBasePriority` |
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

### Nested Types
- `CustomStatusField`
- `EmployeeSimplified`
- `FormFile`
- `RequestAttachment`
- `RequestBasePriority`
- `RequestCategory`
- `RequestComputedFieldsStatus`
- `RequestFeedback`
- `RequestFormDataFieldValue`
- `UserSimplified`

## CustomStatusField
- Role: nested
- Parent: RequestFullWithAttachmentsDataObject
- Schema Name: CustomStatusField
- Schema ID: schema:definitions/CustomStatusField
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |

## EmployeeSimplified
- Role: nested
- Parent: RequestFullWithAttachmentsDataObject
- Schema Name: EmployeeSimplified
- Schema ID: schema:definitions/EmployeeSimplified
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `external_id` | `string` |
| `firstname` | `string` |
| `lastname` | `string` |
| `email` | `string` |
| `id` | `string` |

## FormFile
- Role: nested
- Parent: RequestFullWithAttachmentsDataObject
- Schema Name: FormFile
- Schema ID: schema:definitions/FormFile
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `filename` | `string` |
| `field_id` | `string` |

## RequestAttachment
- Role: nested
- Parent: RequestFullWithAttachmentsDataObject
- Schema Name: RequestAttachment
- Schema ID: schema:definitions/RequestAttachment
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |

## RequestBasePriority
- Role: nested
- Parent: RequestFullWithAttachmentsDataObject
- Schema Name: RequestBasePriority
- Schema ID: schema:anon/e616cc07e9e84b75aae74f0c458061091d611755

### Enum

Values: 1, 2, 3

## RequestCategory
- Role: nested
- Parent: RequestFullWithAttachmentsDataObject
- Schema Name: RequestCategory
- Schema ID: schema:definitions/RequestCategory
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |

## RequestComputedFieldsStatus
- Role: nested
- Parent: RequestFullWithAttachmentsDataObject
- Schema Name: RequestComputedFieldsStatus
- Schema ID: schema:anon/5614592567f7ba3571f08b43d9d3a9b8456db10d

### Enum

Values: created, opened, pending, closed, archived

## RequestFeedback
- Role: nested
- Parent: RequestFullWithAttachmentsDataObject
- Schema Name: RequestFeedback
- Schema ID: schema:definitions/RequestFeedback

### Fields

| Field | Type |
|------|------|
| `created_at` | `string` |
| `rate` | `double` |
| `comment` | `string` |

## RequestFormDataFieldValue
- Role: nested
- Parent: RequestFullWithAttachmentsDataObject
- Schema Name: RequestFormDataFieldValue
- Schema ID: schema:definitions/RequestFormDataFieldValue
- Primary Key: FieldId

### Fields

| Field | Type |
|------|------|
| `field_id` | `string` |
| `values` | `string[]` |

## UserSimplified
- Role: nested
- Parent: RequestFullWithAttachmentsDataObject
- Schema Name: UserSimplified
- Schema ID: schema:definitions/UserSimplified
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `firstname` | `string` |
| `lastname` | `string` |
| `email` | `string` |
| `external_id` | `string` |
