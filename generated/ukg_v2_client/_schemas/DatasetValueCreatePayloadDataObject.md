# DatasetValueCreatePayloadDataObject

## DatasetValueCreatePayloadDataObject
- Role: parent
- Schema Name: DatasetValueCreatePayload
- Schema ID: schema:definitions/DatasetValueCreatePayload

### Fields

| Field | Type |
|------|------|
| `localized_names` | `LocalizedString[]` |

### Nested Types
- `LocalizedString`

## LocalizedString
- Role: nested
- Parent: DatasetValueCreatePayloadDataObject
- Schema Name: LocalizedString
- Schema ID: schema:definitions/LocalizedString

### Fields

| Field | Type |
|------|------|
| `language_code` | `string` |
| `value` | `string` |
