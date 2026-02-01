# RestV10NestedBimViewFoldersBatchPostResponse200DataObject

## RestV10NestedBimViewFoldersBatchPostResponse200DataObject
- Role: parent
- Schema Name: RestV10NestedBimViewFoldersBatchPostResponse200
- Schema ID: schema:anon/bd8ef67af7dddf9410166458168c2c00f6503709

### Fields

| Field | Type |
|------|------|
| `bim_view_folders` | `RestV10NestedBimViewFoldersBatchPostResponse200BimViewFoldersItem[]` |
| `errors` | `RestV10NestedBimViewFoldersBatchPostResponse200ErrorsItem[]` |

### Nested Types
- `RestV10NestedBimViewFoldersBatchPostResponse200BimViewFoldersItem`
- `RestV10NestedBimViewFoldersBatchPostResponse200ErrorsItem`
- `RestV10NestedBimViewFoldersBatchPostResponse200ErrorsItem_7abdf4Errors`

## RestV10NestedBimViewFoldersBatchPostResponse200BimViewFoldersItem
- Role: nested
- Parent: RestV10NestedBimViewFoldersBatchPostResponse200DataObject
- Schema Name: RestV10NestedBimViewFoldersBatchPostResponse200BimViewFoldersItem
- Schema ID: schema:anon/69047bb99c4d91d21731a84b466af241b8112811
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `parent_id` | `int` |
| `bim_file_id` | `int` |
| `project_id` | `int` |
| `created_by_id` | `int` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV10NestedBimViewFoldersBatchPostResponse200ErrorsItem
- Role: nested
- Parent: RestV10NestedBimViewFoldersBatchPostResponse200DataObject
- Schema Name: RestV10NestedBimViewFoldersBatchPostResponse200ErrorsItem
- Schema ID: schema:anon/05efd59459d607c77fc677a388548b201008aaee
- Primary Key: BimFileId

### Fields

| Field | Type |
|------|------|
| `path` | `string[]` |
| `bim_file_id` | `int` |
| `errors` | `RestV10NestedBimViewFoldersBatchPostResponse200ErrorsItem_7abdf4Errors` |

## RestV10NestedBimViewFoldersBatchPostResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10NestedBimViewFoldersBatchPostResponse200DataObject
- Schema Name: RestV10NestedBimViewFoldersBatchPostResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
