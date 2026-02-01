# CustomFieldFullDataObject

## CustomFieldFullDataObject
- Role: parent
- Schema Name: CustomFieldFull
- Schema ID: schema:definitions/CustomFieldFull
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `label` | `string` |
| `type` | `CustomFieldBaseType` |
| `authorized_values` | `AuthorizedValue[]` |
| `hierarchical` | `bool` |
| `default_value` | `string` |
| `localized_labels` | `LocalizedString[]` |
| `visible` | `bool` |
| `allow_access_restrictions` | `bool` |
| `created_at` | `string` |
| `updated_at` | `string` |

### Nested Types
- `AuthorizedValue`
- `CustomFieldBaseType`
- `LocalizedString`

## AuthorizedValue
- Role: nested
- Parent: CustomFieldFullDataObject
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
- Parent: CustomFieldFullDataObject
- Schema Name: CustomFieldBaseType
- Schema ID: schema:anon/c11f399cc043cca752c567eceac832c67e990779

### Enum

Values: bool, string, list, int

## LocalizedString
- Role: nested
- Parent: CustomFieldFullDataObject
- Schema Name: LocalizedString
- Schema ID: schema:definitions/LocalizedString

### Fields

| Field | Type |
|------|------|
| `language_code` | `string` |
| `value` | `string` |
