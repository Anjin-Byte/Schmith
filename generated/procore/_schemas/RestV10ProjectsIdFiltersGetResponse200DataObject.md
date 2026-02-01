# RestV10ProjectsIdFiltersGetResponse200DataObject

## RestV10ProjectsIdFiltersGetResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsIdFiltersGetResponse200
- Schema ID: schema:anon/90e61890824b2af283ddefcde677e4e2df957c84

### Fields

| Field | Type |
|------|------|
| `filters` | `RestV10ProjectsIdFiltersGetResponse200FiltersItem[]` |
| `saved_filters` | `RestV10ProjectsIdFiltersGetResponse200FiltersItem[]` |

### Nested Types
- `RestV10ProjectsIdFiltersGetResponse200FiltersItem`

## RestV10ProjectsIdFiltersGetResponse200FiltersItem
- Role: nested
- Parent: RestV10ProjectsIdFiltersGetResponse200DataObject
- Schema Name: RestV10ProjectsIdFiltersGetResponse200FiltersItem
- Schema ID: schema:anon/4054ac0dc6980f7290fbab0d84f5f26deeabffc6

### Fields

| Field | Type |
|------|------|
| `index` | `int` |
| `key` | `string` |
| `endpoint` | `string` |
| `value` | `string` |
| `type` | `string` |
