# RestV10ChangeOrderPackagesPostResponse201DataObject

## RestV10ChangeOrderPackagesPostResponse201DataObject
- Role: parent
- Schema Name: RestV10ChangeOrderPackagesPostResponse201
- Schema ID: schema:anon/fb871be3f35d6c5ca6ac9ef86e2edf638733fdeb
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
| `status` | `RestV10ChangeOrderPackagesPostResponse201Status` |
| `title` | `string` |
| `type` | `RestV10ChangeOrderPackagesPostResponse201Type` |
| `updated_at` | `string` |
| `creator` | `RestV10ChangeOrderPackagesPostResponse201Creator` |
| `designated_reviewer` | `RestV10ChangeOrderPackagesPostResponse201Creator` |
| `reviewer` | `RestV10ChangeOrderPackagesPostResponse201Creator` |
| `attachments` | `RestV10ChangeOrderPackagesPostResponse201AttachmentsItem[]` |
| `line_items` | `RestV10ChangeOrderPackagesPostResponse201LineItemsItem[]` |
| `currency_configuration` | `RestV10ChangeOrderPackagesPostResponse201CurrencyConfiguration` |
| `custom_fields` | `RestV10ChangeOrderPackagesPostResponse201CustomFields` |

### Nested Types
- `RestV10ChangeOrderPackagesPostResponse201AttachmentsItem`
- `RestV10ChangeOrderPackagesPostResponse201Creator`
- `RestV10ChangeOrderPackagesPostResponse201CurrencyConfiguration`
- `RestV10ChangeOrderPackagesPostResponse201CustomFields`
- `RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}`
- `RestV10ChangeOrderPackagesPostResponse201LineItemsItem`
- `RestV10ChangeOrderPackagesPostResponse201LineItemsItemCostCode`
- `RestV10ChangeOrderPackagesPostResponse201LineItemsItemHolder`
- `RestV10ChangeOrderPackagesPostResponse201LineItemsItemLineItemType`
- `RestV10ChangeOrderPackagesPostResponse201LineItemsItemLineItemTypeBaseType`
- `RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItem`
- `RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItemCurrencyConfiguration`
- `RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItemMarkup`
- `RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItemMarkupDestinationCostCode`
- `RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItemMarkupDestinationSubJob`
- `RestV10ChangeOrderPackagesPostResponse201LineItemsItemWbsCode`
- `RestV10ChangeOrderPackagesPostResponse201Status`
- `RestV10ChangeOrderPackagesPostResponse201Type`

## RestV10ChangeOrderPackagesPostResponse201AttachmentsItem
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201AttachmentsItem
- Schema ID: schema:anon/0fed82b2ab013163afe0e50420982438fd21bbb8
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `url` | `string` |
| `filename` | `string` |

## RestV10ChangeOrderPackagesPostResponse201Creator
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201Creator
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10ChangeOrderPackagesPostResponse201CurrencyConfiguration
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201CurrencyConfiguration
- Schema ID: schema:anon/7f07e441f0e7f9329466802e7e43f41196c8bcb0

### Fields

| Field | Type |
|------|------|
| `base_currency_iso_code` | `string` |
| `currency_iso_code` | `string` |

## RestV10ChangeOrderPackagesPostResponse201CustomFields
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201CustomFields
- Schema ID: schema:anon/fbbbdf310d374c7df5714c86d51abac7a107e10a

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/990ff11816957d5e13e8054a3b4018ca5a889aae

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/2ca25eca8308998fe557ed8b7c6a2efae4b3c787

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/8ac6165387eee0f8b62fd6116b007679069365e9

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/e3d6cf7b64c48c5d41072f1f551520b2e5e9c56d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/3a3c35d457351cba94d43fe7ae5875cdca53185f

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/bfeb38dd91125f9638d7a4d955a8a35669e8d683
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/3e79a4fea4c4a312821d65e59e171469329ba818

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |

## RestV10ChangeOrderPackagesPostResponse201LineItemsItem
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201LineItemsItem
- Schema ID: schema:anon/37bfa4cd6c0d7430d252499e988367234df58afa
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
| `cost_code` | `RestV10ChangeOrderPackagesPostResponse201LineItemsItemCostCode` |
| `wbs_code` | `RestV10ChangeOrderPackagesPostResponse201LineItemsItemWbsCode` |
| `unit_cost` | `string` |
| `holder` | `RestV10ChangeOrderPackagesPostResponse201LineItemsItemHolder` |
| `line_item_type` | `RestV10ChangeOrderPackagesPostResponse201LineItemsItemLineItemType` |
| `markup_line_items` | `RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItem[]` |
| `currency_configuration` | `RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItemCurrencyConfiguration` |

## RestV10ChangeOrderPackagesPostResponse201LineItemsItemCostCode
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201LineItemsItemCostCode
- Schema ID: schema:anon/c6616e03e73149ad3d0a3b24fecc3556727855fb
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `full_code` | `string` |
| `name` | `string` |

## RestV10ChangeOrderPackagesPostResponse201LineItemsItemHolder
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201LineItemsItemHolder
- Schema ID: schema:anon/40ac2a57a69f9c0efad2088ff408a8b12fc3a20b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `holder_type` | `string` |

## RestV10ChangeOrderPackagesPostResponse201LineItemsItemLineItemType
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201LineItemsItemLineItemType
- Schema ID: schema:anon/a1618cbf38b22ff994694464569e37edcfaf29f7
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `code` | `string` |
| `base_type` | `RestV10ChangeOrderPackagesPostResponse201LineItemsItemLineItemTypeBaseType` |
| `origin_data` | `string` |
| `origin_id` | `string` |

## RestV10ChangeOrderPackagesPostResponse201LineItemsItemLineItemTypeBaseType
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201LineItemsItemLineItemTypeBaseType
- Schema ID: schema:anon/c1a066154239ac3e29e59285e26bd77f996807bf

### Enum

Values: equipment, materials, commitment, owner_cost, professional_services, other

## RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItem
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItem
- Schema ID: schema:anon/eae7ea864070a3567c31453fba4e3c3d6303e037
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `amount` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `markup` | `RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItemMarkup` |
| `currency_configuration` | `RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItemCurrencyConfiguration` |

## RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItemCurrencyConfiguration
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItemCurrencyConfiguration
- Schema ID: schema:anon/f884a729d35e590d8f5a68a341a5a0587ffe2382

### Fields

| Field | Type |
|------|------|
| `currency_iso_code` | `string` |

## RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItemMarkup
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItemMarkup
- Schema ID: schema:anon/412aa883d3806eaf55fef977d582bdfda9338ba2
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
| `destination_cost_code` | `RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItemMarkupDestinationCostCode` |
| `destination_line_item_type` | `RestV10ChangeOrderPackagesPostResponse201LineItemsItemLineItemType` |
| `desitination_budget_line_item_id` | `int` |
| `destination_sub_job` | `RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItemMarkupDestinationSubJob` |

## RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItemMarkupDestinationCostCode
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItemMarkupDestinationCostCode
- Schema ID: schema:anon/0a4f1f6df5359e0efedd35132d91824a441f39e9

### Fields

## RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItemMarkupDestinationSubJob
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201LineItemsItemMarkupLineItemsItemMarkupDestinationSubJob
- Schema ID: schema:anon/229af8c0e497a1de396824ecd8e0e29f8b4d8e5b

### Fields

## RestV10ChangeOrderPackagesPostResponse201LineItemsItemWbsCode
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201LineItemsItemWbsCode
- Schema ID: schema:anon/6d1bf58d026ff2d4fe9fd85909b71472fba16aa4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `flat_code` | `string` |
| `description` | `string` |

## RestV10ChangeOrderPackagesPostResponse201Status
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201Status
- Schema ID: schema:anon/5b89f75b59f65acdfdc32f08e622b0fbb79dc552

### Enum

Values: draft, not_pricing, pricing, pending, revised, proceeding, not_proceeding, no_charge, approved, rejected, void

## RestV10ChangeOrderPackagesPostResponse201Type
- Role: nested
- Parent: RestV10ChangeOrderPackagesPostResponse201DataObject
- Schema Name: RestV10ChangeOrderPackagesPostResponse201Type
- Schema ID: schema:anon/86e203cb7fbb29e7ba35e485b7c926e28067f644

### Enum

Values: PrimeContractChangeOrder, CommitmentContractChangeOrder, ChangeOrderPackage
