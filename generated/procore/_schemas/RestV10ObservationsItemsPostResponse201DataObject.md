# RestV10ObservationsItemsPostResponse201DataObject

## RestV10ObservationsItemsPostResponse201DataObject
- Role: parent
- Schema Name: RestV10ObservationsItemsPostResponse201
- Schema ID: schema:anon/7777afc082710d2f2d4d40988eeabea2f7486b63
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `number` | `string` |
| `name` | `string` |
| `description` | `string` |
| `status` | `RestV10ObservationsItemsPostResponse201Status` |
| `checklist_item` | `RestV10ObservationsItemsPostResponse201ChecklistItem` |
| `checklist_list` | `RestV10ObservationsItemsPostResponse201ChecklistList` |
| `priority` | `RestV10ObservationsItemsPostResponse201Priority` |
| `date_notified` | `string` |
| `due_date` | `string` |
| `closed_at` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `deleted_at` | `string` |
| `description_rich_text` | `string` |
| `personal` | `bool` |
| `current_drawing_revision_ids` | `int[]` |
| `drawing_revisions` | `int[]` |
| `drawing_ids` | `int[]` |
| `origin` | `RestV10ObservationsItemsPostResponse201Origin` |
| `attachments` | `RestV10ObservationsItemsPostResponse201AttachmentsItem[]` |
| `assignee` | `RestV10ObservationsItemsPostResponse201Assignee` |
| `distribution_members` | `RestV10ObservationsItemsPostResponse201DistributionMembersItem[]` |
| `created_by` | `RestV10ObservationsItemsPostResponse201CreatedBy` |
| `specification_section` | `RestV10ObservationsItemsPostResponse201SpecificationSection` |
| `location` | `RestV10ObservationsItemsPostResponse201Location` |
| `trade` | `RestV10ObservationsItemsPostResponse201Trade` |
| `type` | `RestV10ObservationsItemsPostResponse201Type` |
| `contributing_behavior` | `RestV10ObservationsItemsPostResponse201ContributingBehavior` |
| `contributing_condition` | `RestV10ObservationsItemsPostResponse201ContributingCondition` |
| `hazard` | `RestV10ObservationsItemsPostResponse201Hazard` |
| `custom_fields` | `RestV10ObservationsItemsPostResponse201CustomFields` |

### Nested Types
- `RestV10ObservationsItemsPostResponse201Assignee`
- `RestV10ObservationsItemsPostResponse201AssigneeVendor`
- `RestV10ObservationsItemsPostResponse201AttachmentsItem`
- `RestV10ObservationsItemsPostResponse201ChecklistItem`
- `RestV10ObservationsItemsPostResponse201ChecklistList`
- `RestV10ObservationsItemsPostResponse201ContributingBehavior`
- `RestV10ObservationsItemsPostResponse201ContributingCondition`
- `RestV10ObservationsItemsPostResponse201CreatedBy`
- `RestV10ObservationsItemsPostResponse201CreatedByVendor`
- `RestV10ObservationsItemsPostResponse201CustomFields`
- `RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}`
- `RestV10ObservationsItemsPostResponse201DistributionMembersItem`
- `RestV10ObservationsItemsPostResponse201Hazard`
- `RestV10ObservationsItemsPostResponse201Location`
- `RestV10ObservationsItemsPostResponse201Origin`
- `RestV10ObservationsItemsPostResponse201OriginPayload`
- `RestV10ObservationsItemsPostResponse201Priority`
- `RestV10ObservationsItemsPostResponse201SpecificationSection`
- `RestV10ObservationsItemsPostResponse201Status`
- `RestV10ObservationsItemsPostResponse201Trade`
- `RestV10ObservationsItemsPostResponse201Type`
- `RestV10ObservationsItemsPostResponse201TypeCategory`
- `RestV10ObservationsItemsPostResponse201TypeNameTranslations`

## RestV10ObservationsItemsPostResponse201Assignee
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201Assignee
- Schema ID: schema:anon/3afb6f46d61867400e43494e5542e18397bc77bb
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `vendor` | `RestV10ObservationsItemsPostResponse201AssigneeVendor` |

## RestV10ObservationsItemsPostResponse201AssigneeVendor
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201AssigneeVendor
- Schema ID: schema:anon/c0dcba9bde69d501afc483285c47875d8d0a4198
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ObservationsItemsPostResponse201AttachmentsItem
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201AttachmentsItem
- Schema ID: schema:anon/30d1b6326ad260f608fa9a0e2b6be62ddaa3212b

### Fields

## RestV10ObservationsItemsPostResponse201ChecklistItem
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201ChecklistItem
- Schema ID: schema:anon/0f64ab912913c10db3a9725f97cdfba284b6596a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV10ObservationsItemsPostResponse201ChecklistList
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201ChecklistList
- Schema ID: schema:anon/a51b03a9f231e1306c547445bdd61c8b166f216e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV10ObservationsItemsPostResponse201ContributingBehavior
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201ContributingBehavior
- Schema ID: schema:anon/124ae5778a8c20cfcb3c7b72f184c50bbf558fdc
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `active` | `bool` |
| `global` | `bool` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV10ObservationsItemsPostResponse201ContributingCondition
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201ContributingCondition
- Schema ID: schema:anon/5c541a5bcdb9633eaeea90340e7f42564348de3f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `active` | `bool` |
| `global` | `bool` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV10ObservationsItemsPostResponse201CreatedBy
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201CreatedBy
- Schema ID: schema:anon/a4792d1e1ef6b072cf589094e8991e799dcd6bc9
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `login` | `string` |
| `vendor` | `RestV10ObservationsItemsPostResponse201CreatedByVendor` |

## RestV10ObservationsItemsPostResponse201CreatedByVendor
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201CreatedByVendor
- Schema ID: schema:anon/ad206378a13d17e4aecb386c404eea942cc80a17
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ObservationsItemsPostResponse201CustomFields
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201CustomFields
- Schema ID: schema:anon/18c858aabec7b2c6828e2c316ea32d80e8f6c1be

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/d7aaf7e4245f8b5e58720e73973a9fdbdbc7839e

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/8178757753fe7302f7d5443936cb13b481bd73ff

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/d50bbe7063fb38ebfcc50625f772776d0020e2f7

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/98dfbe72f61b8f25de0fb5b18d6fa8d9a4ec580a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/33d4a72922e5630c3242f8b04f6ee313e990b793

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/87cff48788164388a7c8910cf94ab26c21bee6e1
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/8c3d88cb61be32fb0e8459abd64e13d194ffdb10

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |

## RestV10ObservationsItemsPostResponse201DistributionMembersItem
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201DistributionMembersItem
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10ObservationsItemsPostResponse201Hazard
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201Hazard
- Schema ID: schema:anon/cd1734d060f2c2d7a98e8e636575eddbe37dc0e6
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `active` | `bool` |
| `global` | `bool` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV10ObservationsItemsPostResponse201Location
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201Location
- Schema ID: schema:anon/7d4098f2df6d84102332d015429ec5ed48bef6c6
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

## RestV10ObservationsItemsPostResponse201Origin
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201Origin
- Schema ID: schema:anon/50c45df24b0c31abd237887f19d3f2576d4f0757

### Fields

| Field | Type |
|------|------|
| `type` | `string` |
| `payload` | `RestV10ObservationsItemsPostResponse201OriginPayload` |

## RestV10ObservationsItemsPostResponse201OriginPayload
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201OriginPayload
- Schema ID: schema:anon/264e5479bacda47b0681945e689de0567cb86235
- Primary Key: ChecklistItemId

### Fields

| Field | Type |
|------|------|
| `checklist_item_id` | `int` |
| `checklist_list_id` | `int` |
| `coordination_issue_id` | `int` |
| `coordination_issue_number` | `int` |
| `incident_action_id` | `int` |
| `incident_id` | `int` |
| `bim_model_id` | `int` |
| `bim_model_name` | `string` |
| `name` | `string` |

## RestV10ObservationsItemsPostResponse201Priority
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201Priority
- Schema ID: schema:anon/e39c4ac7aa75589f63b5f9530fdba300d56b554c

### Enum

Values: Low, Medium, High, Urgent

## RestV10ObservationsItemsPostResponse201SpecificationSection
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201SpecificationSection
- Schema ID: schema:anon/d6cbf4bda886f52884bac1e30318a653476d9d95
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `description` | `string` |
| `number` | `string` |
| `section` | `string` |
| `latest_revision_url` | `string` |
| `current_revision_id` | `int` |
| `viewable_document_id` | `int` |

## RestV10ObservationsItemsPostResponse201Status
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201Status
- Schema ID: schema:anon/72b4ca92c36b07d1cc78522655637b830187e557

### Enum

Values: initiated, ready_for_review, not_accepted, closed

## RestV10ObservationsItemsPostResponse201Trade
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201Trade
- Schema ID: schema:anon/0dc5e552de3604c2a1edbab95ae258e0afaa1167
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `active` | `bool` |
| `updated_at` | `string` |

## RestV10ObservationsItemsPostResponse201Type
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201Type
- Schema ID: schema:anon/032811976c8a406724e4ac53062e0a7194ed41d5
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `category` | `RestV10ObservationsItemsPostResponse201TypeCategory` |
| `category_key` | `string` |
| `category_id` | `int` |
| `name` | `string` |
| `active` | `bool` |
| `company_active` | `bool` |
| `parent_inactive` | `bool` |
| `in_use` | `bool` |
| `kind` | `string` |
| `name_translations` | `RestV10ObservationsItemsPostResponse201TypeNameTranslations` |
| `localized_name` | `string` |

## RestV10ObservationsItemsPostResponse201TypeCategory
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201TypeCategory
- Schema ID: schema:anon/7bec86085841edc45a00ddec396f7ec3b38afdd5

### Enum

Values: Quality, Safety, Commissioning, Warranty, Work to Complete

## RestV10ObservationsItemsPostResponse201TypeNameTranslations
- Role: nested
- Parent: RestV10ObservationsItemsPostResponse201DataObject
- Schema Name: RestV10ObservationsItemsPostResponse201TypeNameTranslations
- Schema ID: schema:anon/229660b074b507639b35d78a538d9d89aac60909

### Fields

| Field | Type |
|------|------|
| `en` | `string` |
| `es` | `string` |
| `fr-CA` | `string` |
| `en-AU` | `string` |
