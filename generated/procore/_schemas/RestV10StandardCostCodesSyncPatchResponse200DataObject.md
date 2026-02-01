# RestV10StandardCostCodesSyncPatchResponse200DataObject

## RestV10StandardCostCodesSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10StandardCostCodesSyncPatchResponse200
- Schema ID: schema:anon/449eecdbc2d380e2dd74f2689b487801f7bd4187

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10StandardCostCodesSyncPatchResponse200EntitiesItem[]` |
| `errors` | `object[]` |

### Nested Types
- `RestV10StandardCostCodesSyncPatchResponse200EntitiesItem`

## RestV10StandardCostCodesSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10StandardCostCodesSyncPatchResponse200DataObject
- Schema Name: RestV10StandardCostCodesSyncPatchResponse200EntitiesItem
- Schema ID: schema:anon/1d39282a2b8a822bd909ebb6340949391efab3be
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `standard_cost_code_list_id` | `int` |
| `parent_id` | `int` |
| `code` | `string` |
| `full_code` | `string` |
| `name` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
