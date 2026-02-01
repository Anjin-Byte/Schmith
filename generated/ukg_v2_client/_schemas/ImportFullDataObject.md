# ImportFullDataObject

## ImportFullDataObject
- Role: parent
- Schema Name: ImportFull
- Schema ID: schema:definitions/ImportFull
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `type` | `ImportBaseType` |
| `creator` | `string` |
| `id` | `string` |
| `status` | `ImportComputedFieldsStatus` |
| `origin` | `ImportComputedFieldsOrigin` |
| `rows_count` | `int` |
| `created_objects_count` | `int` |
| `updated_objects_count` | `int` |
| `deleted_objects_count` | `int` |
| `errors_count` | `int` |
| `created_at` | `string` |
| `updated_at` | `string` |

### Nested Types
- `ImportBaseType`
- `ImportComputedFieldsOrigin`
- `ImportComputedFieldsStatus`

## ImportBaseType
- Role: nested
- Parent: ImportFullDataObject
- Schema Name: ImportBaseType
- Schema ID: schema:anon/0e325a09191808a827013f95b158266db695cc5c

### Enum

Values: employee, manager, organization

## ImportComputedFieldsOrigin
- Role: nested
- Parent: ImportFullDataObject
- Schema Name: ImportComputedFieldsOrigin
- Schema ID: schema:anon/4d4d275cc204995dd90bd4455ecb42d571db2f75

### Enum

Values: api, sftp, web

## ImportComputedFieldsStatus
- Role: nested
- Parent: ImportFullDataObject
- Schema Name: ImportComputedFieldsStatus
- Schema ID: schema:anon/729b7a06e7564973799358ca464f9dfd723a8d0c

### Enum

Values: created, failed, in_progress, partial_success, success
