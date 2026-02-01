# RestV10ChecklistListsListIdItemsItemIdItemAttachmentsPostResponse200DataObject

## RestV10ChecklistListsListIdItemsItemIdItemAttachmentsPostResponse200DataObject
- Role: parent
- Schema Name: RestV10ChecklistListsListIdItemsItemIdItemAttachmentsPostResponse200
- Schema ID: schema:anon/a6d834d5c4bd5ca309813d6f8bdd0139b3cd8366
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `created_at` | `string` |
| `created_by` | `RestV10ChecklistListsListIdItemsItemIdItemAttachmentsPostResponse200CreatedBy` |
| `attachment` | `RestV10ChecklistListsListIdItemsItemIdItemAttachmentsPostResponse200Attachment` |

### Nested Types
- `RestV10ChecklistListsListIdItemsItemIdItemAttachmentsPostResponse200Attachment`
- `RestV10ChecklistListsListIdItemsItemIdItemAttachmentsPostResponse200CreatedBy`

## RestV10ChecklistListsListIdItemsItemIdItemAttachmentsPostResponse200Attachment
- Role: nested
- Parent: RestV10ChecklistListsListIdItemsItemIdItemAttachmentsPostResponse200DataObject
- Schema Name: RestV10ChecklistListsListIdItemsItemIdItemAttachmentsPostResponse200Attachment
- Schema ID: schema:anon/ba3273069e599476dd1af865fa02999937cfbd1a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |
| `name` | `string` |

## RestV10ChecklistListsListIdItemsItemIdItemAttachmentsPostResponse200CreatedBy
- Role: nested
- Parent: RestV10ChecklistListsListIdItemsItemIdItemAttachmentsPostResponse200DataObject
- Schema Name: RestV10ChecklistListsListIdItemsItemIdItemAttachmentsPostResponse200CreatedBy
- Schema ID: schema:anon/67385da91d6062b1e9bede72679fdb0364034afa
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `company_name` | `string` |
| `login` | `string` |
| `name` | `string` |
