# RestV11PunchItemsPostResponse201DataObject

## RestV11PunchItemsPostResponse201DataObject
- Role: parent
- Schema Name: RestV11PunchItemsPostResponse201
- Schema ID: schema:anon/4a9600660ab5293595de9ba7fcdb8a071bc3b599
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `ball_in_court` | `RestV11PunchItemsPostResponse201BallInCourtItem[]` |
| `comments` | `RestV11PunchItemsPostResponse201CommentsItem[]` |
| `created_at` | `string` |
| `closed_at` | `string` |
| `deleted_at` | `string` |
| `description` | `string` |
| `due_date` | `string` |
| `name` | `string` |
| `schedule_risk` | `string` |
| `schedule_risk_reason` | `string` |
| `position` | `int` |
| `priority` | `string` |
| `private` | `bool` |
| `status` | `RestV11PunchItemsPostResponse201Status` |
| `updated_at` | `string` |
| `date_initiated` | `string` |
| `schedule_impact` | `RestV11PunchItemsPostResponse201ScheduleImpact` |
| `schedule_impact_days` | `int` |
| `reference` | `string` |
| `cost_impact` | `RestV11PunchItemsPostResponse201CostImpact` |
| `cost_impact_amount` | `int` |
| `can_email` | `bool` |
| `drawing_ids` | `int[]` |
| `current_drawing_revision_ids` | `int[]` |
| `distribution_members` | `RestV11PunchItemsPostResponse201DistributionMembersItem[]` |
| `location` | `RestV11PunchItemsPostResponse201Location` |
| `trade` | `RestV11PunchItemsPostResponse201Trade` |
| `created_by` | `RestV11PunchItemsPostResponse201CreatedBy` |
| `closed_by` | `RestV11PunchItemsPostResponse201ClosedBy` |
| `punch_item_manager` | `RestV11PunchItemsPostResponse201PunchItemManager` |
| `final_approver` | `RestV11PunchItemsPostResponse201FinalApprover` |
| `punch_item_type` | `RestV11PunchItemsPostResponse201PunchItemType` |
| `cost_code` | `RestV11PunchItemsPostResponse201CostCode` |
| `assignments` | `RestV11PunchItemsPostResponse201AssignmentsItem[]` |
| `rich_text_description` | `string` |
| `attachments` | `RestV11PunchItemsPostResponse201AttachmentsItem[]` |
| `images` | `RestV11PunchItemsPostResponse201AttachmentsItem[]` |
| `web_images` | `RestV11PunchItemsPostResponse201AttachmentsItem[]` |
| `workflow_status` | `RestV11PunchItemsPostResponse201WorkflowStatus` |
| `download_all_attachments_uuid` | `string` |
| `custom_fields` | `RestV11PunchItemsPostResponse201CustomFields` |

### Nested Types
- `RestV11PunchItemsPostResponse201AssignmentsItem`
- `RestV11PunchItemsPostResponse201AssignmentsItemAttachmentsItem`
- `RestV11PunchItemsPostResponse201AssignmentsItemLoginInformation`
- `RestV11PunchItemsPostResponse201AttachmentsItem`
- `RestV11PunchItemsPostResponse201BallInCourtItem`
- `RestV11PunchItemsPostResponse201ClosedBy`
- `RestV11PunchItemsPostResponse201CommentsItem`
- `RestV11PunchItemsPostResponse201CommentsItemCreator`
- `RestV11PunchItemsPostResponse201CostCode`
- `RestV11PunchItemsPostResponse201CostImpact`
- `RestV11PunchItemsPostResponse201CreatedBy`
- `RestV11PunchItemsPostResponse201CustomFields`
- `RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}`
- `RestV11PunchItemsPostResponse201DistributionMembersItem`
- `RestV11PunchItemsPostResponse201FinalApprover`
- `RestV11PunchItemsPostResponse201Location`
- `RestV11PunchItemsPostResponse201PunchItemManager`
- `RestV11PunchItemsPostResponse201PunchItemType`
- `RestV11PunchItemsPostResponse201ScheduleImpact`
- `RestV11PunchItemsPostResponse201Status`
- `RestV11PunchItemsPostResponse201Trade`
- `RestV11PunchItemsPostResponse201WorkflowStatus`

## RestV11PunchItemsPostResponse201AssignmentsItem
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201AssignmentsItem
- Schema ID: schema:anon/b459a2dde809801fe974f5be013db1f3ea5fe8cd
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `approved` | `bool` |
| `comment` | `string` |
| `notified_at` | `string` |
| `ready_for_review_at` | `string` |
| `work_not_accepted_at` | `string` |
| `formatted_status` | `string` |
| `updated_at` | `string` |
| `login_information` | `RestV11PunchItemsPostResponse201AssignmentsItemLoginInformation` |
| `attachments` | `RestV11PunchItemsPostResponse201AssignmentsItemAttachmentsItem[]` |

## RestV11PunchItemsPostResponse201AssignmentsItemAttachmentsItem
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201AssignmentsItemAttachmentsItem
- Schema ID: schema:anon/e0bbc4cb3d5d191bbeabf48932b35a64ffe82e1d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |
| `viewable` | `bool` |
| `can_be_viewed` | `bool` |

## RestV11PunchItemsPostResponse201AssignmentsItemLoginInformation
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201AssignmentsItemLoginInformation
- Schema ID: schema:anon/4db0e1bdd29f3ffb8ceadecdec49cc1160b068b4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |
| `active` | `bool` |

## RestV11PunchItemsPostResponse201AttachmentsItem
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201AttachmentsItem
- Schema ID: schema:anon/c337dee3df228286468f0ff6d8c4852152f75cf4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |

## RestV11PunchItemsPostResponse201BallInCourtItem
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201BallInCourtItem
- Schema ID: schema:anon/200d0b2e08d6546987011bf1cba3e123b0872d1c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `locale` | `string` |

## RestV11PunchItemsPostResponse201ClosedBy
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201ClosedBy
- Schema ID: schema:anon/3322dff059e1b6815b3e1009cccb600f96ed1e2d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `login` | `string` |
| `company_name` | `string` |

## RestV11PunchItemsPostResponse201CommentsItem
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201CommentsItem
- Schema ID: schema:anon/b748b6891eaee30bdbc8536c37988e1ce3498374
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `body` | `string` |
| `creator` | `RestV11PunchItemsPostResponse201CommentsItemCreator` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV11PunchItemsPostResponse201CommentsItemCreator
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201CommentsItemCreator
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV11PunchItemsPostResponse201CostCode
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201CostCode
- Schema ID: schema:anon/7a7d890c7fa0b0fc15a34087ae7717936b876e3d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV11PunchItemsPostResponse201CostImpact
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201CostImpact
- Schema ID: schema:anon/e51587e9e785cfca2b38fc8144355aa33b6cc24a

### Enum

Values: yes_known, yes_unknown, no_impact, tbd, n_a

## RestV11PunchItemsPostResponse201CreatedBy
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201CreatedBy
- Schema ID: schema:anon/922bdbb4cae6627341bd009bddcec08c746f5c4b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `login` | `string` |
| `company_name` | `string` |

## RestV11PunchItemsPostResponse201CustomFields
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201CustomFields
- Schema ID: schema:anon/18c858aabec7b2c6828e2c316ea32d80e8f6c1be

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/d7aaf7e4245f8b5e58720e73973a9fdbdbc7839e

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/8178757753fe7302f7d5443936cb13b481bd73ff

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/d50bbe7063fb38ebfcc50625f772776d0020e2f7

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/98dfbe72f61b8f25de0fb5b18d6fa8d9a4ec580a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/33d4a72922e5630c3242f8b04f6ee313e990b793

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/87cff48788164388a7c8910cf94ab26c21bee6e1
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/8c3d88cb61be32fb0e8459abd64e13d194ffdb10

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |

## RestV11PunchItemsPostResponse201DistributionMembersItem
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201DistributionMembersItem
- Schema ID: schema:anon/a59e8ec47d9891a3c3c4912dd3615aa9c58b186f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |
| `company_name` | `string` |

## RestV11PunchItemsPostResponse201FinalApprover
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201FinalApprover
- Schema ID: schema:anon/77fb8a60f53b32c4550659e7afd480604331c6fc
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `login` | `string` |
| `company_name` | `string` |

## RestV11PunchItemsPostResponse201Location
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201Location
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

## RestV11PunchItemsPostResponse201PunchItemManager
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201PunchItemManager
- Schema ID: schema:anon/01e467fe48c90997229c35fa04e9e627e7695baa
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `login` | `string` |
| `company_name` | `string` |

## RestV11PunchItemsPostResponse201PunchItemType
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201PunchItemType
- Schema ID: schema:anon/e187c02f218826e6f4a4263cc94c269b4c96a589
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV11PunchItemsPostResponse201ScheduleImpact
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201ScheduleImpact
- Schema ID: schema:anon/51cbbe09b337d04cb2a602101a3c642730613fd2

### Enum

Values: yes_known, yes_unknown, no_impact, tbd, n_a

## RestV11PunchItemsPostResponse201Status
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201Status
- Schema ID: schema:anon/a3dd1516e44bbc34559eebe10fd262747ff21fe1

### Enum

Values: Open, Closed, Overdue, Pending

## RestV11PunchItemsPostResponse201Trade
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201Trade
- Schema ID: schema:anon/0dc5e552de3604c2a1edbab95ae258e0afaa1167
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `active` | `bool` |
| `updated_at` | `string` |

## RestV11PunchItemsPostResponse201WorkflowStatus
- Role: nested
- Parent: RestV11PunchItemsPostResponse201DataObject
- Schema Name: RestV11PunchItemsPostResponse201WorkflowStatus
- Schema ID: schema:anon/35728ffc24c5d621ebe9d160bad0994ff6842912

### Enum

Values: draft, initiated, in_dispute, work_required, ready_for_review, work_not_accepted, ready_to_close, not_accepted_by_creator, closed
