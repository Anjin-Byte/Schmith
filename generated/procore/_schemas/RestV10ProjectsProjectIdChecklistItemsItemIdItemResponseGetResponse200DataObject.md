# RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200DataObject

## RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200
- Schema ID: schema:anon/95f97ffd39c50ea3588845ee25035da642e20fb6
- Primary Key: ItemId

### Fields

| Field | Type |
|------|------|
| `item_id` | `int` |
| `status` | `string` |
| `responded_at` | `string` |
| `responder` | `RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200Responder` |
| `item_type` | `RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200ItemType` |
| `payload` | `RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200Payload` |

### Nested Types
- `RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200ItemType`
- `RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200Payload`
- `RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200PayloadResponseOption`
- `RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200Responder`

## RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200ItemType
- Role: nested
- Parent: RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200ItemType
- Schema ID: schema:anon/ade7f59a3b8c98efa8f1ffcf727c1e8b3a77a788
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `category` | `string` |
| `name` | `string` |

## RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200Payload
- Role: nested
- Parent: RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200Payload
- Schema ID: schema:anon/58c1ef85f13ee25d4b220b66cacbff49e80c17fd

### Fields

| Field | Type |
|------|------|
| `text_value` | `string` |
| `number_value` | `int` |
| `date_value` | `string` |
| `response_option` | `RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200PayloadResponseOption` |

## RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200PayloadResponseOption
- Role: nested
- Parent: RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200PayloadResponseOption
- Schema ID: schema:anon/0f14354d50a2f1736cccf75fcc494df1550cefd3
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200Responder
- Role: nested
- Parent: RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdChecklistItemsItemIdItemResponseGetResponse200Responder
- Schema ID: schema:anon/05e77aa2c5b0ae16984d391ae1269bda6f0dbb76
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `login` | `string` |
