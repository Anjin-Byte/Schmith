# RestV10GenericToolItemsIdGetResponse200DataObject

## RestV10GenericToolItemsIdGetResponse200DataObject
- Role: parent
- Schema Name: RestV10GenericToolItemsIdGetResponse200
- Schema ID: schema:anon/dd47c31d3d2f148639338dcc66dd9b04e5b4bc98
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `closed_at` | `string` |
| `created_at` | `string` |
| `description` | `string` |
| `due_date` | `string` |
| `issued_at` | `string` |
| `origin_generic_tool_item_id` | `int` |
| `origin_rfi_id` | `int` |
| `position` | `string` |
| `private` | `bool` |
| `schedule_impact` | `string` |
| `updated_at` | `string` |
| `cost_impact` | `string` |
| `status` | `string` |
| `title` | `string` |
| `created_by` | `RestV10GenericToolItemsIdGetResponse200CreatedBy` |
| `received_from` | `RestV10GenericToolItemsIdGetResponse200CreatedBy` |
| `location` | `RestV10GenericToolItemsIdGetResponse200Location` |
| `cost_code` | `RestV10GenericToolItemsIdGetResponse200CostCode` |
| `specification_section` | `RestV10GenericToolItemsIdGetResponse200SpecificationSection` |
| `sub_job` | `RestV10GenericToolItemsIdGetResponse200SubJob` |
| `tasks` | `RestV10GenericToolItemsIdGetResponse200TasksItem[]` |
| `trade` | `RestV10GenericToolItemsIdGetResponse200Trade` |
| `trades` | `RestV10GenericToolItemsIdGetResponse200TradesItem[]` |
| `generic_tool` | `RestV10GenericToolItemsIdGetResponse200GenericTool` |
| `attachments` | `RestV10GenericToolItemsIdGetResponse200AttachmentsItem[]` |
| `distribution_members` | `RestV10GenericToolItemsIdGetResponse200CreatedBy[]` |
| `assignees` | `RestV10GenericToolItemsIdGetResponse200CreatedBy[]` |
| `custom_fields` | `RestV10GenericToolItemsIdGetResponse200CustomFields` |

### Nested Types
- `RestV10GenericToolItemsIdGetResponse200AttachmentsItem`
- `RestV10GenericToolItemsIdGetResponse200CostCode`
- `RestV10GenericToolItemsIdGetResponse200CreatedBy`
- `RestV10GenericToolItemsIdGetResponse200CustomFields`
- `RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldStringDefinitionId}`
- `RestV10GenericToolItemsIdGetResponse200GenericTool`
- `RestV10GenericToolItemsIdGetResponse200Location`
- `RestV10GenericToolItemsIdGetResponse200SpecificationSection`
- `RestV10GenericToolItemsIdGetResponse200SubJob`
- `RestV10GenericToolItemsIdGetResponse200TasksItem`
- `RestV10GenericToolItemsIdGetResponse200Trade`
- `RestV10GenericToolItemsIdGetResponse200TradesItem`

## RestV10GenericToolItemsIdGetResponse200AttachmentsItem
- Role: nested
- Parent: RestV10GenericToolItemsIdGetResponse200DataObject
- Schema Name: RestV10GenericToolItemsIdGetResponse200AttachmentsItem
- Schema ID: schema:anon/c337dee3df228286468f0ff6d8c4852152f75cf4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |

## RestV10GenericToolItemsIdGetResponse200CostCode
- Role: nested
- Parent: RestV10GenericToolItemsIdGetResponse200DataObject
- Schema Name: RestV10GenericToolItemsIdGetResponse200CostCode
- Schema ID: schema:anon/fdee572d8e009136c7d8995546423f39ff079b5f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `full_code` | `string` |
| `name` | `string` |

## RestV10GenericToolItemsIdGetResponse200CreatedBy
- Role: nested
- Parent: RestV10GenericToolItemsIdGetResponse200DataObject
- Schema Name: RestV10GenericToolItemsIdGetResponse200CreatedBy
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10GenericToolItemsIdGetResponse200CustomFields
- Role: nested
- Parent: RestV10GenericToolItemsIdGetResponse200DataObject
- Schema Name: RestV10GenericToolItemsIdGetResponse200CustomFields
- Schema ID: schema:anon/fbbbdf310d374c7df5714c86d51abac7a107e10a

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV10GenericToolItemsIdGetResponse200DataObject
- Schema Name: RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/990ff11816957d5e13e8054a3b4018ca5a889aae

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV10GenericToolItemsIdGetResponse200DataObject
- Schema Name: RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/2ca25eca8308998fe557ed8b7c6a2efae4b3c787

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV10GenericToolItemsIdGetResponse200DataObject
- Schema Name: RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/8ac6165387eee0f8b62fd6116b007679069365e9

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV10GenericToolItemsIdGetResponse200DataObject
- Schema Name: RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/e3d6cf7b64c48c5d41072f1f551520b2e5e9c56d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV10GenericToolItemsIdGetResponse200DataObject
- Schema Name: RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/3a3c35d457351cba94d43fe7ae5875cdca53185f

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV10GenericToolItemsIdGetResponse200DataObject
- Schema Name: RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/bfeb38dd91125f9638d7a4d955a8a35669e8d683
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV10GenericToolItemsIdGetResponse200DataObject
- Schema Name: RestV10GenericToolItemsIdGetResponse200CustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/3e79a4fea4c4a312821d65e59e171469329ba818

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |

## RestV10GenericToolItemsIdGetResponse200GenericTool
- Role: nested
- Parent: RestV10GenericToolItemsIdGetResponse200DataObject
- Schema Name: RestV10GenericToolItemsIdGetResponse200GenericTool
- Schema ID: schema:anon/d77156749ab6046ccf42a0011c85b6f238e4e010
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `title` | `string` |

## RestV10GenericToolItemsIdGetResponse200Location
- Role: nested
- Parent: RestV10GenericToolItemsIdGetResponse200DataObject
- Schema Name: RestV10GenericToolItemsIdGetResponse200Location
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

## RestV10GenericToolItemsIdGetResponse200SpecificationSection
- Role: nested
- Parent: RestV10GenericToolItemsIdGetResponse200DataObject
- Schema Name: RestV10GenericToolItemsIdGetResponse200SpecificationSection
- Schema ID: schema:anon/7254f8a63e9666c7fdb2fdab13f18af2f0814643
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `number` | `string` |
| `description` | `string` |
| `label` | `string` |
| `current_revision_id` | `int` |

## RestV10GenericToolItemsIdGetResponse200SubJob
- Role: nested
- Parent: RestV10GenericToolItemsIdGetResponse200DataObject
- Schema Name: RestV10GenericToolItemsIdGetResponse200SubJob
- Schema ID: schema:anon/7dd282cd63470b0862e954f50e02db4c9995d6b5
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `Code` | `string` |

## RestV10GenericToolItemsIdGetResponse200TasksItem
- Role: nested
- Parent: RestV10GenericToolItemsIdGetResponse200DataObject
- Schema Name: RestV10GenericToolItemsIdGetResponse200TasksItem
- Schema ID: schema:anon/c0000c9b027ca0b4a58fdddb6b525e155dc78511
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `task_name` | `string` |
| `key` | `string` |

## RestV10GenericToolItemsIdGetResponse200Trade
- Role: nested
- Parent: RestV10GenericToolItemsIdGetResponse200DataObject
- Schema Name: RestV10GenericToolItemsIdGetResponse200Trade
- Schema ID: schema:anon/0dc5e552de3604c2a1edbab95ae258e0afaa1167
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `active` | `bool` |
| `updated_at` | `string` |

## RestV10GenericToolItemsIdGetResponse200TradesItem
- Role: nested
- Parent: RestV10GenericToolItemsIdGetResponse200DataObject
- Schema Name: RestV10GenericToolItemsIdGetResponse200TradesItem
- Schema ID: schema:anon/f842162c63df2a7cbd86609327c8cca44230dad6
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `active` | `bool` |
| `updated_at` | `string` |
