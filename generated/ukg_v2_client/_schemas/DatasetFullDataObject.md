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
| `last_import_status` | `LastImportStatusEnum` |
| `last_import_result` | `LastImportResultEnum` |
| `created_at` | `string` |
| `updated_at` | `string` |
