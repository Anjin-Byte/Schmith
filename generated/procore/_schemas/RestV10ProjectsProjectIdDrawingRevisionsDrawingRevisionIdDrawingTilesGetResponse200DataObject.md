# RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGetResponse200DataObject

## RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGetResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGetResponse200
- Schema ID: schema:anon/b91cc11ddace930bdc213166831e6ecacee4ded9

### Fields

| Field | Type |
|------|------|
| `max_zoom_level` | `int` |
| `tile_size` | `int[]` |
| `zip_url` | `string` |
| `tiles` | `RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGetResponse200TilesItem[]` |

### Nested Types
- `RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGetResponse200TilesItem`

## RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGetResponse200TilesItem
- Role: nested
- Parent: RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGetResponse200TilesItem
- Schema ID: schema:anon/cfa47d4f3bb412f9a3b777b8f4ff7684221d9fb0
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `x` | `int` |
| `y` | `int` |
| `z` | `int` |
| `url` | `string` |
