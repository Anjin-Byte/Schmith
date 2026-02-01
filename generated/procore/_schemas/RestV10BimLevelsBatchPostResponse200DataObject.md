# RestV10BimLevelsBatchPostResponse200DataObject

## RestV10BimLevelsBatchPostResponse200DataObject
- Role: parent
- Schema Name: RestV10BimLevelsBatchPostResponse200
- Schema ID: schema:anon/a0f8b73edd2f70ab47c79e03bc03eda156bca7c8

### Fields

| Field | Type |
|------|------|
| `bim_levels` | `RestV10BimLevelsBatchPostResponse200BimLevelsItem[]` |
| `errors` | `RestV10BimLevelsBatchPostResponse200ErrorsItem[]` |

### Nested Types
- `RestV10BimLevelsBatchPostResponse200BimLevelsItem`
- `RestV10BimLevelsBatchPostResponse200ErrorsItem`
- `RestV10BimLevelsBatchPostResponse200ErrorsItem_7abdf4Errors`

## RestV10BimLevelsBatchPostResponse200BimLevelsItem
- Role: nested
- Parent: RestV10BimLevelsBatchPostResponse200DataObject
- Schema Name: RestV10BimLevelsBatchPostResponse200BimLevelsItem
- Schema ID: schema:anon/33d2f313b33eeb6d4a8c82e44d6e5237277c322f

### Fields

## RestV10BimLevelsBatchPostResponse200ErrorsItem
- Role: nested
- Parent: RestV10BimLevelsBatchPostResponse200DataObject
- Schema Name: RestV10BimLevelsBatchPostResponse200ErrorsItem
- Schema ID: schema:anon/1c77fae4e7eab7c4d12342b84c4e1b57d37d7cf2
- Primary Key: BimFileId

### Fields

| Field | Type |
|------|------|
| `elevation` | `double` |
| `bim_file_id` | `int` |
| `location_id` | `int` |
| `errors` | `RestV10BimLevelsBatchPostResponse200ErrorsItem_7abdf4Errors` |

## RestV10BimLevelsBatchPostResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10BimLevelsBatchPostResponse200DataObject
- Schema Name: RestV10BimLevelsBatchPostResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
