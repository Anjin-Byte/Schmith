# RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201DataObject

## RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201
- Schema ID: schema:anon/c5877dfe7bcefe7c31311e76ed67505bd94372ec
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `contract_id` | `int` |
| `created_at` | `string` |
| `description` | `string` |
| `due_date` | `string` |
| `executed` | `bool` |
| `grand_total` | `string` |
| `invoiced_date` | `string` |
| `number` | `string` |
| `paid_date` | `string` |
| `private` | `bool` |
| `review_notes` | `string` |
| `reviewed_at` | `string` |
| `revised_substantial_completion_date` | `string` |
| `revision` | `int` |
| `schedule_impact_amount` | `int` |
| `signature_required` | `bool` |
| `signed_change_order_received_date` | `string` |
| `status` | `string` |
| `title` | `string` |
| `type` | `string` |
| `updated_at` | `string` |
| `created_by` | `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CreatedBy` |
| `designated_reviewer` | `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201DesignatedReviewer` |
| `reviewed_by` | `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201ReviewedBy` |
| `attachments` | `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201AttachmentsItem[]` |
| `custom_fields` | `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFields` |
| `currency_configuration` | `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CurrencyConfiguration` |

### Nested Types
- `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201AttachmentsItem`
- `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CreatedBy`
- `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CurrencyConfiguration`
- `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFields`
- `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}`
- `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201DesignatedReviewer`
- `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201ReviewedBy`

## RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201AttachmentsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201AttachmentsItem
- Schema ID: schema:anon/40d37556818abfc15e6d30a1c73461a73c2ffbb4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `name` | `string` |

## RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CreatedBy
- Role: nested
- Parent: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CreatedBy
- Schema ID: schema:anon/777a65997bd958c5bd93d2d7dab0bd5467a89717
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CurrencyConfiguration
- Role: nested
- Parent: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CurrencyConfiguration
- Schema ID: schema:anon/7f07e441f0e7f9329466802e7e43f41196c8bcb0

### Fields

| Field | Type |
|------|------|
| `base_currency_iso_code` | `string` |
| `currency_iso_code` | `string` |

## RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFields
- Role: nested
- Parent: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFields
- Schema ID: schema:anon/fbbbdf310d374c7df5714c86d51abac7a107e10a

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/990ff11816957d5e13e8054a3b4018ca5a889aae

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/2ca25eca8308998fe557ed8b7c6a2efae4b3c787

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/8ac6165387eee0f8b62fd6116b007679069365e9

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/e3d6cf7b64c48c5d41072f1f551520b2e5e9c56d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/3a3c35d457351cba94d43fe7ae5875cdca53185f

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/bfeb38dd91125f9638d7a4d955a8a35669e8d683
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/3e79a4fea4c4a312821d65e59e171469329ba818

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |

## RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201DesignatedReviewer
- Role: nested
- Parent: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201DesignatedReviewer
- Schema ID: schema:anon/26726a19441ca704f44fe4eb32f1ff69a1a9ea41
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201ReviewedBy
- Role: nested
- Parent: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdPrimeChangeOrderBatchesPostResponse201ReviewedBy
- Schema ID: schema:anon/aca1688614d67e0fa8f2edd35e845f165d66de1f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
