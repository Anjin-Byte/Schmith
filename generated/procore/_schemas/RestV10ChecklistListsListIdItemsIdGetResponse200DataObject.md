# RestV10ChecklistListsListIdItemsIdGetResponse200DataObject

## RestV10ChecklistListsListIdItemsIdGetResponse200DataObject
- Role: parent
- Schema Name: RestV10ChecklistListsListIdItemsIdGetResponse200
- Schema ID: schema:anon/0429c1862fc12f16e7682245db9ff13c29d711ae
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `details` | `string` |
| `status` | `RestV10ChecklistListsListIdItemsIdGetResponse200Status` |
| `responded_with` | `string` |
| `origin_id` | `int` |
| `section_id` | `int` |
| `position` | `int` |
| `observations` | `RestV10ChecklistListsListIdItemsIdGetResponse200ObservationsItem[]` |
| `attachment_histories` | `RestV10ChecklistListsListIdItemsIdGetResponse200AttachmentHistoriesItem[]` |
| `attachments` | `RestV10ChecklistListsListIdItemsIdGetResponse200AttachmentsItem[]` |
| `histories` | `RestV10ChecklistListsListIdItemsIdGetResponse200HistoriesItem[]` |
| `item_response` | `RestV10ChecklistListsListIdItemsIdGetResponse200ItemResponse` |
| `comments` | `RestV10ChecklistListsListIdItemsIdGetResponse200CommentsItem[]` |
| `response` | `RestV10ChecklistListsListIdItemsIdGetResponse200Response` |
| `response_set` | `RestV10ChecklistListsListIdItemsIdGetResponse200ResponseSet` |
| `response_set_id` | `int` |
| `type` | `RestV10ChecklistListsListIdItemsIdGetResponse200ItemResponseItemType` |
| `template_item_id` | `int` |
| `response_type_id` | `int` |
| `updated_at` | `string` |

### Nested Types
- `RestV10ChecklistListsListIdItemsIdGetResponse200AttachmentHistoriesItem`
- `RestV10ChecklistListsListIdItemsIdGetResponse200AttachmentHistoriesItemAttachment`
- `RestV10ChecklistListsListIdItemsIdGetResponse200AttachmentsItem`
- `RestV10ChecklistListsListIdItemsIdGetResponse200CommentsItem`
- `RestV10ChecklistListsListIdItemsIdGetResponse200HistoriesItem`
- `RestV10ChecklistListsListIdItemsIdGetResponse200ItemResponse`
- `RestV10ChecklistListsListIdItemsIdGetResponse200ItemResponseItemType`
- `RestV10ChecklistListsListIdItemsIdGetResponse200ItemResponsePayload`
- `RestV10ChecklistListsListIdItemsIdGetResponse200ItemResponsePayloadResponseOption`
- `RestV10ChecklistListsListIdItemsIdGetResponse200ObservationsItem`
- `RestV10ChecklistListsListIdItemsIdGetResponse200ObservationsItemAssignee`
- `RestV10ChecklistListsListIdItemsIdGetResponse200ObservationsItemType`
- `RestV10ChecklistListsListIdItemsIdGetResponse200Response`
- `RestV10ChecklistListsListIdItemsIdGetResponse200ResponseCorrespondingStatus`
- `RestV10ChecklistListsListIdItemsIdGetResponse200ResponseSet`
- `RestV10ChecklistListsListIdItemsIdGetResponse200Status`

## RestV10ChecklistListsListIdItemsIdGetResponse200AttachmentHistoriesItem
- Role: nested
- Parent: RestV10ChecklistListsListIdItemsIdGetResponse200DataObject
- Schema Name: RestV10ChecklistListsListIdItemsIdGetResponse200AttachmentHistoriesItem
- Schema ID: schema:anon/e98703a1eda855fa74dc251f40597620a2506677
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `created_at` | `string` |
| `created_by` | `RestV10ChecklistListsListIdItemsIdGetResponse200ObservationsItemAssignee` |
| `attachment` | `RestV10ChecklistListsListIdItemsIdGetResponse200AttachmentHistoriesItemAttachment` |

## RestV10ChecklistListsListIdItemsIdGetResponse200AttachmentHistoriesItemAttachment
- Role: nested
- Parent: RestV10ChecklistListsListIdItemsIdGetResponse200DataObject
- Schema Name: RestV10ChecklistListsListIdItemsIdGetResponse200AttachmentHistoriesItemAttachment
- Schema ID: schema:anon/c337dee3df228286468f0ff6d8c4852152f75cf4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |

## RestV10ChecklistListsListIdItemsIdGetResponse200AttachmentsItem
- Role: nested
- Parent: RestV10ChecklistListsListIdItemsIdGetResponse200DataObject
- Schema Name: RestV10ChecklistListsListIdItemsIdGetResponse200AttachmentsItem
- Schema ID: schema:anon/dec4aab8e4d246a8ddc05b8de35713d3449e7fd9
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |

## RestV10ChecklistListsListIdItemsIdGetResponse200CommentsItem
- Role: nested
- Parent: RestV10ChecklistListsListIdItemsIdGetResponse200DataObject
- Schema Name: RestV10ChecklistListsListIdItemsIdGetResponse200CommentsItem
- Schema ID: schema:anon/90db79dc84965c9df1481e435f1e4765d3f384d4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `body` | `string` |
| `created_at` | `string` |
| `created_by` | `RestV10ChecklistListsListIdItemsIdGetResponse200ObservationsItemAssignee` |

## RestV10ChecklistListsListIdItemsIdGetResponse200HistoriesItem
- Role: nested
- Parent: RestV10ChecklistListsListIdItemsIdGetResponse200DataObject
- Schema Name: RestV10ChecklistListsListIdItemsIdGetResponse200HistoriesItem
- Schema ID: schema:anon/bed87d2feb6262ad145f78c79d6b07bb87d7b01e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `body` | `string` |
| `status` | `string` |
| `responded_with` | `string` |
| `created_at` | `string` |
| `created_by` | `RestV10ChecklistListsListIdItemsIdGetResponse200ObservationsItemAssignee` |

## RestV10ChecklistListsListIdItemsIdGetResponse200ItemResponse
- Role: nested
- Parent: RestV10ChecklistListsListIdItemsIdGetResponse200DataObject
- Schema Name: RestV10ChecklistListsListIdItemsIdGetResponse200ItemResponse
- Schema ID: schema:anon/ee720497fbc78b356404975115a525f903196083
- Primary Key: ItemId

### Fields

| Field | Type |
|------|------|
| `item_id` | `int` |
| `status` | `string` |
| `responded_at` | `string` |
| `responder` | `RestV10ChecklistListsListIdItemsIdGetResponse200ObservationsItemAssignee` |
| `item_type` | `RestV10ChecklistListsListIdItemsIdGetResponse200ItemResponseItemType` |
| `payload` | `RestV10ChecklistListsListIdItemsIdGetResponse200ItemResponsePayload` |

## RestV10ChecklistListsListIdItemsIdGetResponse200ItemResponseItemType
- Role: nested
- Parent: RestV10ChecklistListsListIdItemsIdGetResponse200DataObject
- Schema Name: RestV10ChecklistListsListIdItemsIdGetResponse200ItemResponseItemType
- Schema ID: schema:anon/ade7f59a3b8c98efa8f1ffcf727c1e8b3a77a788
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `category` | `string` |
| `name` | `string` |

## RestV10ChecklistListsListIdItemsIdGetResponse200ItemResponsePayload
- Role: nested
- Parent: RestV10ChecklistListsListIdItemsIdGetResponse200DataObject
- Schema Name: RestV10ChecklistListsListIdItemsIdGetResponse200ItemResponsePayload
- Schema ID: schema:anon/58c1ef85f13ee25d4b220b66cacbff49e80c17fd

### Fields

| Field | Type |
|------|------|
| `text_value` | `string` |
| `number_value` | `int` |
| `date_value` | `string` |
| `response_option` | `RestV10ChecklistListsListIdItemsIdGetResponse200ItemResponsePayloadResponseOption` |

## RestV10ChecklistListsListIdItemsIdGetResponse200ItemResponsePayloadResponseOption
- Role: nested
- Parent: RestV10ChecklistListsListIdItemsIdGetResponse200DataObject
- Schema Name: RestV10ChecklistListsListIdItemsIdGetResponse200ItemResponsePayloadResponseOption
- Schema ID: schema:anon/0f14354d50a2f1736cccf75fcc494df1550cefd3
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ChecklistListsListIdItemsIdGetResponse200ObservationsItem
- Role: nested
- Parent: RestV10ChecklistListsListIdItemsIdGetResponse200DataObject
- Schema Name: RestV10ChecklistListsListIdItemsIdGetResponse200ObservationsItem
- Schema ID: schema:anon/5a20d751deca22f6b52b85c5d0d67e9871c2a13b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `created_at` | `string` |
| `number` | `string` |
| `status` | `string` |
| `title` | `string` |
| `type` | `RestV10ChecklistListsListIdItemsIdGetResponse200ObservationsItemType` |
| `assignee` | `RestV10ChecklistListsListIdItemsIdGetResponse200ObservationsItemAssignee` |
| `created_by` | `RestV10ChecklistListsListIdItemsIdGetResponse200ObservationsItemAssignee` |

## RestV10ChecklistListsListIdItemsIdGetResponse200ObservationsItemAssignee
- Role: nested
- Parent: RestV10ChecklistListsListIdItemsIdGetResponse200DataObject
- Schema Name: RestV10ChecklistListsListIdItemsIdGetResponse200ObservationsItemAssignee
- Schema ID: schema:anon/121288c30b14d925f7a9c37e3dca7d3325344ec8
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10ChecklistListsListIdItemsIdGetResponse200ObservationsItemType
- Role: nested
- Parent: RestV10ChecklistListsListIdItemsIdGetResponse200DataObject
- Schema Name: RestV10ChecklistListsListIdItemsIdGetResponse200ObservationsItemType
- Schema ID: schema:anon/752878c535509baef7317390e5fdf94e9c16eb44
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ChecklistListsListIdItemsIdGetResponse200Response
- Role: nested
- Parent: RestV10ChecklistListsListIdItemsIdGetResponse200DataObject
- Schema Name: RestV10ChecklistListsListIdItemsIdGetResponse200Response
- Schema ID: schema:anon/731cf14ed573edfdf6d581338f98b8462504ca3c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `corresponding_status` | `RestV10ChecklistListsListIdItemsIdGetResponse200ResponseCorrespondingStatus` |

## RestV10ChecklistListsListIdItemsIdGetResponse200ResponseCorrespondingStatus
- Role: nested
- Parent: RestV10ChecklistListsListIdItemsIdGetResponse200DataObject
- Schema Name: RestV10ChecklistListsListIdItemsIdGetResponse200ResponseCorrespondingStatus
- Schema ID: schema:anon/4935f1f79cd9068abcb0cf5483f118fedaf5a1eb

### Enum

Values: yes, no, n/a, none

## RestV10ChecklistListsListIdItemsIdGetResponse200ResponseSet
- Role: nested
- Parent: RestV10ChecklistListsListIdItemsIdGetResponse200DataObject
- Schema Name: RestV10ChecklistListsListIdItemsIdGetResponse200ResponseSet
- Schema ID: schema:anon/10bc57f06a82c1772a743c0eaf4428173a16b898
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `responses` | `RestV10ChecklistListsListIdItemsIdGetResponse200Response[]` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV10ChecklistListsListIdItemsIdGetResponse200Status
- Role: nested
- Parent: RestV10ChecklistListsListIdItemsIdGetResponse200DataObject
- Schema Name: RestV10ChecklistListsListIdItemsIdGetResponse200Status
- Schema ID: schema:anon/eed02ed74cc85dbd625fb759b2f1452ace08377a

### Enum

Values: yes, no, n/a, none
