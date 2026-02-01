# DatasetValueFullDataObject

## DatasetValueFullDataObject
- Role: parent
- Schema Name: DatasetValueFull
- Schema ID: schema:definitions/DatasetValueFull
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `localized_names` | `LocalizedString[]` |
| `code` | `string` |
| `name` | `string` |
| `id` | `string` |
| `dataset_id` | `string` |
| `dimension_id` | `string` |

### Nested Types
- `LocalizedString`

## LocalizedString
- Role: nested
- Parent: DatasetValueFullDataObject
- Schema Name: LocalizedString
- Schema ID: schema:definitions/LocalizedString

### Fields

| Field | Type |
|------|------|
| `language_code` | `string` |
| `value` | `string` |
