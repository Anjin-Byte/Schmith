# RestV10PotentialChangeOrdersSyncPatchResponse200DataObject

## RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200
- Schema ID: schema:anon/b51a11ca423d6a77e6a06e37dae946d6b7938b8b

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItem[]` |
| `errors` | `RestV10PotentialChangeOrdersSyncPatchResponse200ErrorsItem[]` |

### Nested Types
- `Anonymous_88ecc10dBillerType`
- `Anonymous_88ecc10dLineItemTypesItem`
- `Anonymous_88ecc10dLineItemTypesItemBaseType`
- `Anonymous_88ecc10dParent`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItem`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemAccountingMethod`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemAttachmentsItem`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCreator`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCurrencyConfiguration`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFields`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldStringDefinitionId}`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItem`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemCostCode`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItem`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItemCurrencyConfiguration`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItemMarkup`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItemMarkupDestinationCostCode`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItemMarkupDestinationSubJob`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemStatus`
- `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemVendor`
- `RestV10PotentialChangeOrdersSyncPatchResponse200ErrorsItem`
- `RestV10PotentialChangeOrdersSyncPatchResponse200ErrorsItem_7abdf4Errors`

## Anonymous_88ecc10dBillerType
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: Anonymous_88ecc10dBillerType
- Schema ID: schema:anon/6ce4c07d2fb83b79d4fcb225c5c9c05691bcdc4d

### Enum

Values: Project, SubJob

## Anonymous_88ecc10dLineItemTypesItem
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: Anonymous_88ecc10dLineItemTypesItem
- Schema ID: schema:anon/b78a87f17b509f5904f1a9e8b840af217e95b3fc
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `code` | `string` |
| `base_type` | `Anonymous_88ecc10dLineItemTypesItemBaseType` |
| `origin_data` | `string` |
| `origin_id` | `string` |

## Anonymous_88ecc10dLineItemTypesItemBaseType
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: Anonymous_88ecc10dLineItemTypesItemBaseType
- Schema ID: schema:anon/c1a066154239ac3e29e59285e26bd77f996807bf

### Enum

Values: equipment, materials, commitment, owner_cost, professional_services, other

## Anonymous_88ecc10dParent
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: Anonymous_88ecc10dParent
- Schema ID: schema:anon/44768f5b771296b189deec792bd565b414bae19b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItem
- Schema ID: schema:anon/19d889477964ebcb768179e9f626d64c0a472fd6
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `accounting_method` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemAccountingMethod` |
| `change_order_change_reason_id` | `int` |
| `change_order_request_id` | `int` |
| `commitment_change_event_id` | `int` |
| `contract_id` | `int` |
| `created_at` | `string` |
| `creator` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCreator` |
| `deleted_at` | `string` |
| `description` | `string` |
| `designated_reviewer` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCreator` |
| `due_date` | `string` |
| `field_change` | `bool` |
| `grand_total` | `string` |
| `invoiced_date` | `string` |
| `attachments` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemAttachmentsItem[]` |
| `line_items` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItem[]` |
| `line_items_extended_total` | `string` |
| `line_items_total` | `string` |
| `location_id` | `int` |
| `number` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `paid` | `bool` |
| `paid_date` | `string` |
| `position` | `int` |
| `prime_change_event_id` | `int` |
| `private` | `bool` |
| `reason` | `string` |
| `received_from` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCreator` |
| `reference` | `string` |
| `request_for_quote_id` | `int` |
| `reviewed_at` | `string` |
| `reviewer` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCreator` |
| `revision` | `int` |
| `schedule_impact_amount` | `int` |
| `status` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemStatus` |
| `title` | `string` |
| `updated_at` | `string` |
| `vendor` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemVendor` |
| `void` | `bool` |
| `currency_configuration` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCurrencyConfiguration` |
| `custom_fields` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFields` |

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemAccountingMethod
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemAccountingMethod
- Schema ID: schema:anon/c100ba6d1f058db804fef3de62502c74d40b71da

### Enum

Values: amount, unit

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemAttachmentsItem
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemAttachmentsItem
- Schema ID: schema:anon/0fed82b2ab013163afe0e50420982438fd21bbb8
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `url` | `string` |
| `filename` | `string` |

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCreator
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCreator
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCurrencyConfiguration
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCurrencyConfiguration
- Schema ID: schema:anon/604508c10ceb4d00db265015715c4f3c345909ea

### Fields

| Field | Type |
|------|------|
| `base_currency_iso_code` | `string` |
| `currency_iso_code` | `string` |

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFields
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFields
- Schema ID: schema:anon/fbbbdf310d374c7df5714c86d51abac7a107e10a

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/990ff11816957d5e13e8054a3b4018ca5a889aae

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/2ca25eca8308998fe557ed8b7c6a2efae4b3c787

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/8ac6165387eee0f8b62fd6116b007679069365e9

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/e3d6cf7b64c48c5d41072f1f551520b2e5e9c56d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/3a3c35d457351cba94d43fe7ae5875cdca53185f

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/bfeb38dd91125f9638d7a4d955a8a35669e8d683
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemCustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/3e79a4fea4c4a312821d65e59e171469329ba818

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItem
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItem
- Schema ID: schema:anon/8cbc5b45b3fec2e588d77617f40e0d120e2e3b71
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `position` | `int` |
| `description` | `string` |
| `quantity` | `double` |
| `uom` | `string` |
| `total_amount` | `string` |
| `extended_amount` | `string` |
| `cost_code_id` | `int` |
| `tax_code_id` | `int` |
| `unit_cost` | `double` |
| `cost_code` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemCostCode` |
| `line_item_type` | `Anonymous_88ecc10dLineItemTypesItem` |
| `markup_line_items` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItem[]` |
| `currency_configuration` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItemCurrencyConfiguration` |

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemCostCode
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemCostCode
- Schema ID: schema:anon/7b94f1df2e808d88fd5afc25464a20b4905f7763
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `full_code` | `string` |
| `name` | `string` |
| `biller` | `string` |
| `biller_id` | `int` |
| `biller_type` | `Anonymous_88ecc10dBillerType` |
| `budgeted` | `bool` |
| `code` | `string` |
| `created_at` | `string` |
| `deleted_at` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `parent` | `Anonymous_88ecc10dParent` |
| `position` | `int` |
| `sortable_code` | `string` |
| `standard_cost_code_id` | `int` |
| `standard_cost_code_list_id` | `int` |
| `updated_at` | `string` |
| `line_item_types` | `Anonymous_88ecc10dLineItemTypesItem[]` |

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItem
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItem
- Schema ID: schema:anon/4132b55c4fc618aee5065e328b82082d007e317a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `amount` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `markup` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItemMarkup` |
| `currency_configuration` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItemCurrencyConfiguration` |

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItemCurrencyConfiguration
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItemCurrencyConfiguration
- Schema ID: schema:anon/f884a729d35e590d8f5a68a341a5a0587ffe2382

### Fields

| Field | Type |
|------|------|
| `currency_iso_code` | `string` |

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItemMarkup
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItemMarkup
- Schema ID: schema:anon/8c38239d46fbd7bb5cecd10598ee18977a2bfe35
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `position` | `int` |
| `markup_set` | `string` |
| `name` | `string` |
| `percentage` | `string` |
| `compounds_markups_above` | `bool` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `destination_cost_code` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItemMarkupDestinationCostCode` |
| `destination_line_item_type` | `Anonymous_88ecc10dLineItemTypesItem` |
| `desitination_budget_line_item_id` | `int` |
| `destination_sub_job` | `RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItemMarkupDestinationSubJob` |

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItemMarkupDestinationCostCode
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItemMarkupDestinationCostCode
- Schema ID: schema:anon/fdee572d8e009136c7d8995546423f39ff079b5f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `full_code` | `string` |
| `name` | `string` |

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItemMarkupDestinationSubJob
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemLineItemsItemMarkupLineItemsItemMarkupDestinationSubJob
- Schema ID: schema:anon/229af8c0e497a1de396824ecd8e0e29f8b4d8e5b

### Fields

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemStatus
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemStatus
- Schema ID: schema:anon/5b89f75b59f65acdfdc32f08e622b0fbb79dc552

### Enum

Values: draft, not_pricing, pricing, pending, revised, proceeding, not_proceeding, no_charge, approved, rejected, void

## RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemVendor
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200EntitiesItemVendor
- Schema ID: schema:anon/2b6fa06571868b6fe9370397176acbf74e3356b2
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10PotentialChangeOrdersSyncPatchResponse200ErrorsItem
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200ErrorsItem
- Schema ID: schema:anon/0d8056362885c68903b74068357e9a2fe03ebdfb

### Fields

| Field | Type |
|------|------|
| `errors` | `RestV10PotentialChangeOrdersSyncPatchResponse200ErrorsItem_7abdf4Errors` |

## RestV10PotentialChangeOrdersSyncPatchResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10PotentialChangeOrdersSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersSyncPatchResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
