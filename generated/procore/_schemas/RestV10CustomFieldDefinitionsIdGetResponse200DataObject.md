# RestV10CustomFieldDefinitionsIdGetResponse200DataObject

## RestV10CustomFieldDefinitionsIdGetResponse200DataObject
- Role: parent
- Schema Name: RestV10CustomFieldDefinitionsIdGetResponse200
- Schema ID: schema:anon/63c723fb83bb8674379dd40a0a581eb13e992a37
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |
| `active` | `bool` |
| `company_id` | `int` |
| `data_type` | `string` |
| `variant` | `string` |
| `description` | `string` |
| `default_value` | `string` |
| `configurable_field_sets_count` | `int` |
| `custom_field_lov_entries` | `RestV10CustomFieldDefinitionsIdGetResponse200CustomFieldLovEntriesItem[]` |

### Nested Types
- `RestV10CustomFieldDefinitionsIdGetResponse200CustomFieldLovEntriesItem`

## RestV10CustomFieldDefinitionsIdGetResponse200CustomFieldLovEntriesItem
- Role: nested
- Parent: RestV10CustomFieldDefinitionsIdGetResponse200DataObject
- Schema Name: RestV10CustomFieldDefinitionsIdGetResponse200CustomFieldLovEntriesItem
- Schema ID: schema:anon/ab04e1649bdcb9e6b1cc62d262a97afff0db80f8
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |
| `position` | `double` |
| `active` | `bool` |
