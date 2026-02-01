# DatasetFullDataObject

## DatasetFullDataObject
- Role: parent
- Schema Name: DatasetFull
- Schema ID: schema:definitions/DatasetFull
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `localized_names` | `LocalizedString[]` |
| `id` | `string` |
| `name` | `string` |
| `dimensions` | `DatasetDimensionFull[]` |
| `values_count` | `int` |
| `last_import_status` | `DatasetComputedFieldsLastImportStatus` |
| `last_import_result` | `DatasetComputedFieldsLastImportResult` |
| `created_at` | `string` |
| `updated_at` | `string` |

### Nested Types
- `DatasetComputedFieldsLastImportResult`
- `DatasetComputedFieldsLastImportStatus`
- `DatasetDimensionFull`
- `LocalizedString`

## DatasetComputedFieldsLastImportResult
- Role: nested
- Parent: DatasetFullDataObject
- Schema Name: DatasetComputedFieldsLastImportResult
- Schema ID: schema:anon/27905151b61e69f2c7fdcdcd6a2e88113c9b5839

### Enum

Values: error, success

## DatasetComputedFieldsLastImportStatus
- Role: nested
- Parent: DatasetFullDataObject
- Schema Name: DatasetComputedFieldsLastImportStatus
- Schema ID: schema:anon/171d3fcd1ce50c97dff5ab570d8f5850b325c322

### Enum

Values: queued, in_progress, finished

## DatasetDimensionFull
- Role: nested
- Parent: DatasetFullDataObject
- Schema Name: DatasetDimensionFull
- Schema ID: schema:definitions/DatasetDimensionFull
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `localized_names` | `LocalizedString[]` |
| `name` | `string` |

## LocalizedString
- Role: nested
- Parent: DatasetFullDataObject
- Schema Name: LocalizedString
- Schema ID: schema:definitions/LocalizedString

### Fields

| Field | Type |
|------|------|
| `language_code` | `string` |
| `value` | `string` |
