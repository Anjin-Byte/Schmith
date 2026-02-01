# EventActionFilterComputedFieldsDataObject

## EventActionFilterComputedFieldsDataObject
- Role: parent
- Schema Name: EventActionFilterComputedFields
- Schema ID: schema:definitions/EventActionFilterComputedFields

### Fields

| Field | Type |
|------|------|
| `application_name` | `string` |
| `resources` | `EventActionFilterComputedFieldsResourcesItem[]` |

### Nested Types
- `EventActionFilterComputedFieldsResourcesItem`

## EventActionFilterComputedFieldsResourcesItem
- Role: nested
- Parent: EventActionFilterComputedFieldsDataObject
- Schema Name: EventActionFilterComputedFieldsResourcesItem
- Schema ID: schema:anon/6790023f2eeabfd26706286439c8b415fa6f8a7c

### Fields

| Field | Type |
|------|------|
| `resource_name` | `string` |
| `actions` | `string[]` |
