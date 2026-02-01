# RestV10ChangeOrderPackagesIdGetResponse200DataObject

## RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Role: parent
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200
- Schema ID: schema:anon/892b404c4d1bcc65d153d7dca3df71085712c1ad
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `contract_id` | `int` |
| `created_at` | `string` |
| `deleted_at` | `string` |
| `description` | `string` |
| `due_date` | `string` |
| `executed` | `bool` |
| `grand_total` | `string` |
| `invoiced_date` | `string` |
| `number` | `string` |
| `origin_code` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `paid_date` | `string` |
| `position` | `int` |
| `private` | `bool` |
| `review_notes` | `string` |
| `reviewed_at` | `string` |
| `revised_substantial_completion_date` | `string` |
| `revision` | `int` |
| `schedule_impact_amount` | `int` |
| `signed_change_order_received_date` | `string` |
| `status` | `RestV10ChangeOrderPackagesIdGetResponse200Status` |
| `title` | `string` |
| `type` | `RestV10ChangeOrderPackagesIdGetResponse200Type` |
| `updated_at` | `string` |
| `creator` | `RestV10ChangeOrderPackagesIdGetResponse200Creator` |
| `designated_reviewer` | `RestV10ChangeOrderPackagesIdGetResponse200Creator` |
| `reviewer` | `RestV10ChangeOrderPackagesIdGetResponse200Creator` |
| `attachments` | `RestV10ChangeOrderPackagesIdGetResponse200AttachmentsItem[]` |
| `line_items` | `RestV10ChangeOrderPackagesIdGetResponse200LineItemsItem[]` |
| `currency_configuration` | `RestV10ChangeOrderPackagesIdGetResponse200CurrencyConfiguration` |
| `custom_fields` | `RestV10ChangeOrderPackagesIdGetResponse200CustomFields` |

### Nested Types
- `Anonymous_88ecc10dBillerType`
- `Anonymous_88ecc10dLineItemTypesItem`
- `Anonymous_88ecc10dLineItemTypesItemBaseType`
- `Anonymous_88ecc10dParent`
- `RestV10ChangeOrderPackagesIdGetResponse200AttachmentsItem`
- `RestV10ChangeOrderPackagesIdGetResponse200Creator`
- `RestV10ChangeOrderPackagesIdGetResponse200CurrencyConfiguration`
- `RestV10ChangeOrderPackagesIdGetResponse200CustomFields`
- `RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldStringDefinitionId}`
- `RestV10ChangeOrderPackagesIdGetResponse200LineItemsItem`
- `RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemCostCode`
- `RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemHolder`
- `RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItem`
- `RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItemCurrencyConfiguration`
- `RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItemMarkup`
- `RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItemMarkupDestinationCostCode`
- `RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItemMarkupDestinationSubJob`
- `RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemWbsCode`
- `RestV10ChangeOrderPackagesIdGetResponse200Status`
- `RestV10ChangeOrderPackagesIdGetResponse200Type`

## Anonymous_88ecc10dBillerType
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: Anonymous_88ecc10dBillerType
- Schema ID: schema:anon/6ce4c07d2fb83b79d4fcb225c5c9c05691bcdc4d

### Enum

Values: Project, SubJob

## Anonymous_88ecc10dLineItemTypesItem
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
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
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: Anonymous_88ecc10dLineItemTypesItemBaseType
- Schema ID: schema:anon/c1a066154239ac3e29e59285e26bd77f996807bf

### Enum

Values: equipment, materials, commitment, owner_cost, professional_services, other

## Anonymous_88ecc10dParent
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: Anonymous_88ecc10dParent
- Schema ID: schema:anon/44768f5b771296b189deec792bd565b414bae19b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV10ChangeOrderPackagesIdGetResponse200AttachmentsItem
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200AttachmentsItem
- Schema ID: schema:anon/0fed82b2ab013163afe0e50420982438fd21bbb8
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `url` | `string` |
| `filename` | `string` |

## RestV10ChangeOrderPackagesIdGetResponse200Creator
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200Creator
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10ChangeOrderPackagesIdGetResponse200CurrencyConfiguration
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200CurrencyConfiguration
- Schema ID: schema:anon/7f07e441f0e7f9329466802e7e43f41196c8bcb0

### Fields

| Field | Type |
|------|------|
| `base_currency_iso_code` | `string` |
| `currency_iso_code` | `string` |

## RestV10ChangeOrderPackagesIdGetResponse200CustomFields
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200CustomFields
- Schema ID: schema:anon/fbbbdf310d374c7df5714c86d51abac7a107e10a

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/990ff11816957d5e13e8054a3b4018ca5a889aae

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/2ca25eca8308998fe557ed8b7c6a2efae4b3c787

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/8ac6165387eee0f8b62fd6116b007679069365e9

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/e3d6cf7b64c48c5d41072f1f551520b2e5e9c56d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/3a3c35d457351cba94d43fe7ae5875cdca53185f

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/bfeb38dd91125f9638d7a4d955a8a35669e8d683
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200CustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/3e79a4fea4c4a312821d65e59e171469329ba818

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |

## RestV10ChangeOrderPackagesIdGetResponse200LineItemsItem
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200LineItemsItem
- Schema ID: schema:anon/e8ae7305d81d3d13204faaaa197a83503c8b0a82
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `position` | `int` |
| `description` | `string` |
| `quantity` | `string` |
| `uom` | `string` |
| `total_amount` | `string` |
| `extended_amount` | `string` |
| `unit_cost` | `string` |
| `cost_code` | `RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemCostCode` |
| `wbs_code` | `RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemWbsCode` |
| `holder` | `RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemHolder` |
| `line_item_type` | `Anonymous_88ecc10dLineItemTypesItem` |
| `markup_line_items` | `RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItem[]` |
| `currency_configuration` | `RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItemCurrencyConfiguration` |

## RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemCostCode
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemCostCode
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

## RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemHolder
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemHolder
- Schema ID: schema:anon/40ac2a57a69f9c0efad2088ff408a8b12fc3a20b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `holder_type` | `string` |

## RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItem
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItem
- Schema ID: schema:anon/246b186f44c206131b65987ab495ad6dd6d31574
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `amount` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `markup` | `RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItemMarkup` |
| `currency_configuration` | `RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItemCurrencyConfiguration` |

## RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItemCurrencyConfiguration
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItemCurrencyConfiguration
- Schema ID: schema:anon/f884a729d35e590d8f5a68a341a5a0587ffe2382

### Fields

| Field | Type |
|------|------|
| `currency_iso_code` | `string` |

## RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItemMarkup
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItemMarkup
- Schema ID: schema:anon/62cd6c63ae7c6cfc20d9d9e886cc973e6b6268d7
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
| `wbs_code_id` | `int` |
| `destination_cost_code` | `RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItemMarkupDestinationCostCode` |
| `destination_line_item_type` | `Anonymous_88ecc10dLineItemTypesItem` |
| `desitination_budget_line_item_id` | `int` |
| `destination_sub_job` | `RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItemMarkupDestinationSubJob` |

## RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItemMarkupDestinationCostCode
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItemMarkupDestinationCostCode
- Schema ID: schema:anon/0a4f1f6df5359e0efedd35132d91824a441f39e9

### Fields

## RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItemMarkupDestinationSubJob
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemMarkupLineItemsItemMarkupDestinationSubJob
- Schema ID: schema:anon/229af8c0e497a1de396824ecd8e0e29f8b4d8e5b

### Fields

## RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemWbsCode
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200LineItemsItemWbsCode
- Schema ID: schema:anon/6d1bf58d026ff2d4fe9fd85909b71472fba16aa4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `flat_code` | `string` |
| `description` | `string` |

## RestV10ChangeOrderPackagesIdGetResponse200Status
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200Status
- Schema ID: schema:anon/5b89f75b59f65acdfdc32f08e622b0fbb79dc552

### Enum

Values: draft, not_pricing, pricing, pending, revised, proceeding, not_proceeding, no_charge, approved, rejected, void

## RestV10ChangeOrderPackagesIdGetResponse200Type
- Role: nested
- Parent: RestV10ChangeOrderPackagesIdGetResponse200DataObject
- Schema Name: RestV10ChangeOrderPackagesIdGetResponse200Type
- Schema ID: schema:anon/86e203cb7fbb29e7ba35e485b7c926e28067f644

### Enum

Values: PrimeContractChangeOrder, CommitmentContractChangeOrder, ChangeOrderPackage
