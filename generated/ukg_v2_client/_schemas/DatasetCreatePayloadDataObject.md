# DatasetCreatePayloadDataObject

## DatasetCreatePayloadDataObject
- Role: parent
- Schema Name: DatasetCreatePayload
- Schema ID: schema:definitions/DatasetCreatePayload

### Fields

| Field | Type |
|------|------|
| `dimensions` | `DatasetDimensionCreatePayload[]` |
| `localized_names` | `LocalizedString[]` |

### Nested Types
- `DatasetDimensionCreatePayload`
- `LocalizedString`

## DatasetDimensionCreatePayload
- Role: nested
- Parent: DatasetCreatePayloadDataObject
- Schema Name: DatasetDimensionCreatePayload
- Schema ID: schema:definitions/DatasetDimensionCreatePayload
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `localized_names` | `LocalizedString[]` |

## LocalizedString
- Role: nested
- Parent: DatasetCreatePayloadDataObject
- Schema Name: LocalizedString
- Schema ID: schema:definitions/LocalizedString

### Fields

| Field | Type |
|------|------|
| `language_code` | `string` |
| `value` | `string` |
