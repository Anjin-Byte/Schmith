# RestV10ChecklistListsPostResponse201DataObject

## RestV10ChecklistListsPostResponse201DataObject
- Role: parent
- Schema Name: RestV10ChecklistListsPostResponse201
- Schema ID: schema:anon/f8ab08f40a85e7dfbca31daa63b867ac862f16f5
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `inspection_type` | `RestV10ChecklistListsPostResponse201InspectionType` |
| `list_template_id` | `int` |
| `name` | `string` |
| `description` | `string` |
| `distribution_members` | `RestV10ChecklistListsPostResponse201DistributionMembersItem[]` |
| `due_at` | `string` |
| `identifier` | `string` |
| `number` | `int` |
| `status` | `RestV10ChecklistListsPostResponse201Status` |
| `inspection_date` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `closed_at` | `string` |
| `item_count` | `int` |
| `yes_item_count` | `int` |
| `personal` | `bool` |
| `item_total` | `int` |
| `conforming_item_count` | `int` |
| `deficient_item_count` | `int` |
| `na_item_count` | `int` |
| `neutral_item_count` | `int` |
| `not_inspected_item_count` | `int` |
| `drawing_ids` | `int[]` |
| `current_drawing_revision_ids` | `int[]` |
| `location` | `RestV10ChecklistListsPostResponse201Location` |
| `specification_section` | `RestV10ChecklistListsPostResponse201SpecificationSection` |
| `trade` | `RestV10ChecklistListsPostResponse201Trade` |
| `created_by` | `RestV10ChecklistListsPostResponse201DistributionMembersItem` |
| `closed_by` | `RestV10ChecklistListsPostResponse201ClosedBy` |
| `inspectors` | `RestV10ChecklistListsPostResponse201DistributionMembersItem[]` |
| `signature_requests` | `RestV10ChecklistListsPostResponse201SignatureRequestsItem[]` |
| `responsible_contractor` | `RestV10ChecklistListsPostResponse201ResponsibleContractor` |
| `responsible_party` | `RestV10ChecklistListsPostResponse201ClosedBy` |
| `response_set` | `RestV10ChecklistListsPostResponse201ResponseSet` |
| `attachments` | `RestV10ChecklistListsPostResponse201AttachmentsItem[]` |
| `sections` | `RestV10ChecklistListsPostResponse201SectionsItem[]` |
| `custom_fields` | `RestV10ChecklistListsPostResponse201CustomFields` |
| `managed_equipment_id` | `int` |
| `template_id` | `int` |
| `list_template_name` | `string` |
| `trade_id` | `int` |
| `inspection_type_id` | `int` |
| `reinspected_by_id` | `string` |
| `reinspected_from_id` | `string` |

### Nested Types
- `RestV10ChecklistListsPostResponse201AttachmentsItem`
- `RestV10ChecklistListsPostResponse201ClosedBy`
- `RestV10ChecklistListsPostResponse201CustomFields`
- `RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}`
- `RestV10ChecklistListsPostResponse201DistributionMembersItem`
- `RestV10ChecklistListsPostResponse201InspectionType`
- `RestV10ChecklistListsPostResponse201Location`
- `RestV10ChecklistListsPostResponse201ResponseSet`
- `RestV10ChecklistListsPostResponse201ResponsibleContractor`
- `RestV10ChecklistListsPostResponse201SectionsItem`
- `RestV10ChecklistListsPostResponse201SectionsItemItemsItem`
- `RestV10ChecklistListsPostResponse201SectionsItemItemsItemAttachmentHistoriesItem`
- `RestV10ChecklistListsPostResponse201SectionsItemItemsItemAttachmentHistoriesItemAttachment`
- `RestV10ChecklistListsPostResponse201SectionsItemItemsItemCommentsItem`
- `RestV10ChecklistListsPostResponse201SectionsItemItemsItemHistoriesItem`
- `RestV10ChecklistListsPostResponse201SectionsItemItemsItemItemResponse`
- `RestV10ChecklistListsPostResponse201SectionsItemItemsItemItemResponseItemType`
- `RestV10ChecklistListsPostResponse201SectionsItemItemsItemItemResponsePayload`
- `RestV10ChecklistListsPostResponse201SectionsItemItemsItemItemResponsePayloadResponseOption`
- `RestV10ChecklistListsPostResponse201SectionsItemItemsItemObservationsItem`
- `RestV10ChecklistListsPostResponse201SectionsItemItemsItemObservationsItemType`
- `RestV10ChecklistListsPostResponse201SectionsItemItemsItemResponse`
- `RestV10ChecklistListsPostResponse201SectionsItemItemsItemResponseCorrespondingStatus`
- `RestV10ChecklistListsPostResponse201SectionsItemItemsItemResponseSet`
- `RestV10ChecklistListsPostResponse201SectionsItemItemsItemStatus`
- `RestV10ChecklistListsPostResponse201SignatureRequestsItem`
- `RestV10ChecklistListsPostResponse201SignatureRequestsItemSignatory`
- `RestV10ChecklistListsPostResponse201SignatureRequestsItemSignature`
- `RestV10ChecklistListsPostResponse201SignatureRequestsItemSignatureAttachment`
- `RestV10ChecklistListsPostResponse201SpecificationSection`
- `RestV10ChecklistListsPostResponse201Status`
- `RestV10ChecklistListsPostResponse201Trade`

## RestV10ChecklistListsPostResponse201AttachmentsItem
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201AttachmentsItem
- Schema ID: schema:anon/9db8b0487ffdc4ed217bad0fc75f0ca36767226c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `name` | `string` |
| `filename` | `string` |

## RestV10ChecklistListsPostResponse201ClosedBy
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201ClosedBy
- Schema ID: schema:anon/0a03023ef02b99e04c81d4bcbc9985f628b98c90
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10ChecklistListsPostResponse201CustomFields
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201CustomFields
- Schema ID: schema:anon/18c858aabec7b2c6828e2c316ea32d80e8f6c1be

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/d7aaf7e4245f8b5e58720e73973a9fdbdbc7839e

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/8178757753fe7302f7d5443936cb13b481bd73ff

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/d50bbe7063fb38ebfcc50625f772776d0020e2f7

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/98dfbe72f61b8f25de0fb5b18d6fa8d9a4ec580a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/33d4a72922e5630c3242f8b04f6ee313e990b793

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/87cff48788164388a7c8910cf94ab26c21bee6e1
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/8c3d88cb61be32fb0e8459abd64e13d194ffdb10

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |

## RestV10ChecklistListsPostResponse201DistributionMembersItem
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201DistributionMembersItem
- Schema ID: schema:anon/121288c30b14d925f7a9c37e3dca7d3325344ec8
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10ChecklistListsPostResponse201InspectionType
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201InspectionType
- Schema ID: schema:anon/15da4226f759b9f46fc09f42313ac0c4ff7037ec
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV10ChecklistListsPostResponse201Location
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201Location
- Schema ID: schema:anon/297097a686ac88e6c9de41e719fcaf5d2188dae0
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `node_name` | `string` |
| `parent_id` | `int` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV10ChecklistListsPostResponse201ResponseSet
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201ResponseSet
- Schema ID: schema:anon/6f0bda3d13d22d6311a0c8b07848773427063e30

### Fields

| Field | Type |
|------|------|
| `conforming_response` | `string` |
| `deficient_response` | `string` |
| `global` | `bool` |
| `updated_at` | `string` |
| `created_at` | `string` |

## RestV10ChecklistListsPostResponse201ResponsibleContractor
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201ResponsibleContractor
- Schema ID: schema:anon/ca88192e4c703ceb907b9198ecb7dae067312aea
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ChecklistListsPostResponse201SectionsItem
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SectionsItem
- Schema ID: schema:anon/f1436a993441cb8afaf9d8b5794c30d28319c968
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `position` | `int` |
| `origin_id` | `int` |
| `items` | `RestV10ChecklistListsPostResponse201SectionsItemItemsItem[]` |
| `template_section_id` | `int` |

## RestV10ChecklistListsPostResponse201SectionsItemItemsItem
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SectionsItemItemsItem
- Schema ID: schema:anon/f5a087eebe19db6b5deb286ea8a4d0f4e7b8eb7e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `details` | `string` |
| `status` | `RestV10ChecklistListsPostResponse201SectionsItemItemsItemStatus` |
| `responded_with` | `string` |
| `origin_id` | `int` |
| `section_id` | `int` |
| `position` | `int` |
| `observations` | `RestV10ChecklistListsPostResponse201SectionsItemItemsItemObservationsItem[]` |
| `attachment_histories` | `RestV10ChecklistListsPostResponse201SectionsItemItemsItemAttachmentHistoriesItem[]` |
| `attachments` | `RestV10ChecklistListsPostResponse201SectionsItemItemsItemAttachmentHistoriesItem[]` |
| `histories` | `RestV10ChecklistListsPostResponse201SectionsItemItemsItemHistoriesItem[]` |
| `item_response` | `RestV10ChecklistListsPostResponse201SectionsItemItemsItemItemResponse` |
| `comments` | `RestV10ChecklistListsPostResponse201SectionsItemItemsItemCommentsItem[]` |
| `response` | `RestV10ChecklistListsPostResponse201SectionsItemItemsItemResponse` |
| `response_set` | `RestV10ChecklistListsPostResponse201SectionsItemItemsItemResponseSet` |
| `type` | `RestV10ChecklistListsPostResponse201SectionsItemItemsItemItemResponseItemType` |
| `response_set_id` | `int` |
| `template_item_id` | `int` |
| `response_type_id` | `int` |

## RestV10ChecklistListsPostResponse201SectionsItemItemsItemAttachmentHistoriesItem
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SectionsItemItemsItemAttachmentHistoriesItem
- Schema ID: schema:anon/b07e96aacc1d498837a3cb3faf88d6733e128971
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `created_at` | `string` |
| `created_by` | `RestV10ChecklistListsPostResponse201DistributionMembersItem` |
| `attachment` | `RestV10ChecklistListsPostResponse201SectionsItemItemsItemAttachmentHistoriesItemAttachment` |

## RestV10ChecklistListsPostResponse201SectionsItemItemsItemAttachmentHistoriesItemAttachment
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SectionsItemItemsItemAttachmentHistoriesItemAttachment
- Schema ID: schema:anon/8f49d5d461933f8fd19e1155ddab38b50a226cb1
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |
| `name` | `string` |

## RestV10ChecklistListsPostResponse201SectionsItemItemsItemCommentsItem
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SectionsItemItemsItemCommentsItem
- Schema ID: schema:anon/90db79dc84965c9df1481e435f1e4765d3f384d4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `body` | `string` |
| `created_at` | `string` |
| `created_by` | `RestV10ChecklistListsPostResponse201DistributionMembersItem` |

## RestV10ChecklistListsPostResponse201SectionsItemItemsItemHistoriesItem
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SectionsItemItemsItemHistoriesItem
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
| `created_by` | `RestV10ChecklistListsPostResponse201DistributionMembersItem` |

## RestV10ChecklistListsPostResponse201SectionsItemItemsItemItemResponse
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SectionsItemItemsItemItemResponse
- Schema ID: schema:anon/ee720497fbc78b356404975115a525f903196083
- Primary Key: ItemId

### Fields

| Field | Type |
|------|------|
| `item_id` | `int` |
| `status` | `string` |
| `responded_at` | `string` |
| `responder` | `RestV10ChecklistListsPostResponse201DistributionMembersItem` |
| `item_type` | `RestV10ChecklistListsPostResponse201SectionsItemItemsItemItemResponseItemType` |
| `payload` | `RestV10ChecklistListsPostResponse201SectionsItemItemsItemItemResponsePayload` |

## RestV10ChecklistListsPostResponse201SectionsItemItemsItemItemResponseItemType
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SectionsItemItemsItemItemResponseItemType
- Schema ID: schema:anon/ade7f59a3b8c98efa8f1ffcf727c1e8b3a77a788
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `category` | `string` |
| `name` | `string` |

## RestV10ChecklistListsPostResponse201SectionsItemItemsItemItemResponsePayload
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SectionsItemItemsItemItemResponsePayload
- Schema ID: schema:anon/58c1ef85f13ee25d4b220b66cacbff49e80c17fd

### Fields

| Field | Type |
|------|------|
| `text_value` | `string` |
| `number_value` | `int` |
| `date_value` | `string` |
| `response_option` | `RestV10ChecklistListsPostResponse201SectionsItemItemsItemItemResponsePayloadResponseOption` |

## RestV10ChecklistListsPostResponse201SectionsItemItemsItemItemResponsePayloadResponseOption
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SectionsItemItemsItemItemResponsePayloadResponseOption
- Schema ID: schema:anon/0f14354d50a2f1736cccf75fcc494df1550cefd3
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ChecklistListsPostResponse201SectionsItemItemsItemObservationsItem
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SectionsItemItemsItemObservationsItem
- Schema ID: schema:anon/84fa066be070d1c4169fba3ae6e2102238a55d13
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `created_at` | `string` |
| `number` | `string` |
| `status` | `string` |
| `title` | `string` |
| `type` | `RestV10ChecklistListsPostResponse201SectionsItemItemsItemObservationsItemType` |
| `assignee` | `RestV10ChecklistListsPostResponse201DistributionMembersItem` |
| `created_by` | `RestV10ChecklistListsPostResponse201DistributionMembersItem` |

## RestV10ChecklistListsPostResponse201SectionsItemItemsItemObservationsItemType
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SectionsItemItemsItemObservationsItemType
- Schema ID: schema:anon/1ddee2291153c76db9c9fd6668f55cff0c14edd8
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `active` | `bool` |

## RestV10ChecklistListsPostResponse201SectionsItemItemsItemResponse
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SectionsItemItemsItemResponse
- Schema ID: schema:anon/731cf14ed573edfdf6d581338f98b8462504ca3c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `corresponding_status` | `RestV10ChecklistListsPostResponse201SectionsItemItemsItemResponseCorrespondingStatus` |

## RestV10ChecklistListsPostResponse201SectionsItemItemsItemResponseCorrespondingStatus
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SectionsItemItemsItemResponseCorrespondingStatus
- Schema ID: schema:anon/4935f1f79cd9068abcb0cf5483f118fedaf5a1eb

### Enum

Values: yes, no, n/a, none

## RestV10ChecklistListsPostResponse201SectionsItemItemsItemResponseSet
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SectionsItemItemsItemResponseSet
- Schema ID: schema:anon/780f3a0205d58da5e271fc45014eb9ebfef3b083
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `responses` | `RestV10ChecklistListsPostResponse201SectionsItemItemsItemResponse[]` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV10ChecklistListsPostResponse201SectionsItemItemsItemStatus
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SectionsItemItemsItemStatus
- Schema ID: schema:anon/eed02ed74cc85dbd625fb759b2f1452ace08377a

### Enum

Values: yes, no, n/a, none

## RestV10ChecklistListsPostResponse201SignatureRequestsItem
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SignatureRequestsItem
- Schema ID: schema:anon/1ee3208345eb5c48f7d00340ddebe927b925d5d1
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `signatory` | `RestV10ChecklistListsPostResponse201SignatureRequestsItemSignatory` |
| `signature` | `RestV10ChecklistListsPostResponse201SignatureRequestsItemSignature` |

## RestV10ChecklistListsPostResponse201SignatureRequestsItemSignatory
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SignatureRequestsItemSignatory
- Schema ID: schema:anon/803a12c7aea5299f4d566a8c46509c126a7db6c0

### Fields

## RestV10ChecklistListsPostResponse201SignatureRequestsItemSignature
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SignatureRequestsItemSignature
- Schema ID: schema:anon/18cf845fe359b53cd47607d073bd8aadd6c3799e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `captured_by` | `RestV10ChecklistListsPostResponse201SignatureRequestsItemSignatory` |
| `captured_at` | `string` |
| `attachment` | `RestV10ChecklistListsPostResponse201SignatureRequestsItemSignatureAttachment` |

## RestV10ChecklistListsPostResponse201SignatureRequestsItemSignatureAttachment
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SignatureRequestsItemSignatureAttachment
- Schema ID: schema:anon/16140cb0f27f461f74dd257afd30b52b40c1864b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `thumbnail_url` | `string` |
| `url` | `string` |
| `filename` | `string` |
| `name` | `string` |
| `viewable_document_id` | `int` |
| `attached_to_item_id` | `int` |
| `attached_to_item_type` | `string` |
| `viewer_url` | `string` |

## RestV10ChecklistListsPostResponse201SpecificationSection
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201SpecificationSection
- Schema ID: schema:anon/99b8bb3bd2da465e1aefdee43054172c36a41a91
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `description` | `string` |
| `section` | `string` |
| `latest_revision_url` | `string` |

## RestV10ChecklistListsPostResponse201Status
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201Status
- Schema ID: schema:anon/0c8e87da5e52dab79b89222d980535d3a790a11f

### Enum

Values: Open, Closed

## RestV10ChecklistListsPostResponse201Trade
- Role: nested
- Parent: RestV10ChecklistListsPostResponse201DataObject
- Schema Name: RestV10ChecklistListsPostResponse201Trade
- Schema ID: schema:anon/0dc5e552de3604c2a1edbab95ae258e0afaa1167
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `active` | `bool` |
| `updated_at` | `string` |
