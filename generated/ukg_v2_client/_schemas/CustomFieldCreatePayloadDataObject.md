# CustomFieldCreatePayloadDataObject

## CustomFieldCreatePayloadDataObject
- Role: parent
- Schema Name: CustomFieldCreatePayload
- Schema ID: schema:definitions/CustomFieldCreatePayload

### Fields

| Field | Type |
|------|------|
| `type` | `CustomFieldBaseType` |
| `authorized_values` | `AuthorizedValue[]` |
| `hierarchical` | `bool` |
| `default_value` | `string` |
| `localized_labels` | `LocalizedString[]` |
| `visible` | `bool` |
| `allow_access_restrictions` | `bool` |

### Nested Types
- `AuthorizedValue`
- `CustomFieldBaseType`
- `LocalizedString`

## AuthorizedValue
- Role: nested
- Parent: CustomFieldCreatePayloadDataObject
- Schema Name: AuthorizedValue
- Schema ID: schema:definitions/AuthorizedValue

### Fields

| Field | Type |
|------|------|
| `value` | `string` |
| `label` | `string` |
| `code` | `string` |

## CustomFieldBaseType
- Role: nested
- Parent: CustomFieldCreatePayloadDataObject
- Schema Name: CustomFieldBaseType
- Schema ID: schema:anon/c11f399cc043cca752c567eceac832c67e990779

### Enum

Values: bool, string, list, int

## LocalizedString
- Role: nested
- Parent: CustomFieldCreatePayloadDataObject
- Schema Name: LocalizedString
- Schema ID: schema:definitions/LocalizedString

### Fields

| Field | Type |
|------|------|
| `language_code` | `string` |
| `value` | `string` |
