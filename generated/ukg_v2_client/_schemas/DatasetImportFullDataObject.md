# DatasetImportFullDataObject

## DatasetImportFullDataObject
- Role: parent
- Schema Name: DatasetImportFull
- Schema ID: schema:definitions/DatasetImportFull
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `dataset_id` | `string` |
| `id` | `string` |
| `filename` | `string` |
| `status` | `DatasetImportComputedFieldsStatus` |
| `result` | `DatasetImportComputedFieldsResult` |
| `origin` | `DatasetImportComputedFieldsOrigin` |
| `creator_id` | `string` |
| `total_dimensions_count` | `int` |
| `total_values_count` | `int` |
| `started_at` | `string` |
| `finished_at` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |

### Nested Types
- `DatasetImportComputedFieldsOrigin`
- `DatasetImportComputedFieldsResult`
- `DatasetImportComputedFieldsStatus`

## DatasetImportComputedFieldsOrigin
- Role: nested
- Parent: DatasetImportFullDataObject
- Schema Name: DatasetImportComputedFieldsOrigin
- Schema ID: schema:anon/4d4d275cc204995dd90bd4455ecb42d571db2f75

### Enum

Values: api, sftp, web

## DatasetImportComputedFieldsResult
- Role: nested
- Parent: DatasetImportFullDataObject
- Schema Name: DatasetImportComputedFieldsResult
- Schema ID: schema:anon/452069ce22972a77787cecc0440ef4539efc41b1

### Enum

Values: success, partial_success, error

## DatasetImportComputedFieldsStatus
- Role: nested
- Parent: DatasetImportFullDataObject
- Schema Name: DatasetImportComputedFieldsStatus
- Schema ID: schema:anon/b1565af67104674e5c1f8bcc9f427c452a60eab0

### Enum

Values: queued, in_progress, finished
