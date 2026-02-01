# RestV10PotentialChangeOrdersPostResponse201DataObject

## RestV10PotentialChangeOrdersPostResponse201DataObject
- Role: parent
- Schema Name: RestV10PotentialChangeOrdersPostResponse201
- Schema ID: schema:anon/a8058ff821356878dcd5ff5957a540b07b10965b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `accounting_method` | `RestV10PotentialChangeOrdersPostResponse201AccountingMethod` |
| `change_order_request_id` | `int` |
| `commitment_change_event_id` | `int` |
| `contract_id` | `int` |
| `created_at` | `string` |
| `creator` | `RestV10PotentialChangeOrdersPostResponse201Creator` |
| `description` | `string` |
| `due_date` | `string` |
| `field_change` | `bool` |
| `grand_total` | `string` |
| `invoiced_date` | `string` |
| `line_items` | `object[]` |
| `line_items_extended_total` | `string` |
| `line_items_total` | `string` |
| `number` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `paid` | `bool` |
| `paid_date` | `string` |
| `position` | `int` |
| `prime_change_event_id` | `int` |
| `private` | `bool` |
| `revision` | `int` |
| `schedule_impact_amount` | `int` |
| `status` | `RestV10PotentialChangeOrdersPostResponse201Status` |
| `title` | `string` |
| `updated_at` | `string` |
| `vendor` | `RestV10PotentialChangeOrdersPostResponse201Vendor` |
| `void` | `bool` |
| `currency_configuration` | `RestV10PotentialChangeOrdersPostResponse201CurrencyConfiguration` |
| `custom_fields` | `RestV10PotentialChangeOrdersPostResponse201CustomFields` |

### Nested Types
- `RestV10PotentialChangeOrdersPostResponse201AccountingMethod`
- `RestV10PotentialChangeOrdersPostResponse201Creator`
- `RestV10PotentialChangeOrdersPostResponse201CurrencyConfiguration`
- `RestV10PotentialChangeOrdersPostResponse201CustomFields`
- `RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}`
- `RestV10PotentialChangeOrdersPostResponse201Status`
- `RestV10PotentialChangeOrdersPostResponse201Vendor`

## RestV10PotentialChangeOrdersPostResponse201AccountingMethod
- Role: nested
- Parent: RestV10PotentialChangeOrdersPostResponse201DataObject
- Schema Name: RestV10PotentialChangeOrdersPostResponse201AccountingMethod
- Schema ID: schema:anon/c100ba6d1f058db804fef3de62502c74d40b71da

### Enum

Values: amount, unit

## RestV10PotentialChangeOrdersPostResponse201Creator
- Role: nested
- Parent: RestV10PotentialChangeOrdersPostResponse201DataObject
- Schema Name: RestV10PotentialChangeOrdersPostResponse201Creator
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10PotentialChangeOrdersPostResponse201CurrencyConfiguration
- Role: nested
- Parent: RestV10PotentialChangeOrdersPostResponse201DataObject
- Schema Name: RestV10PotentialChangeOrdersPostResponse201CurrencyConfiguration
- Schema ID: schema:anon/604508c10ceb4d00db265015715c4f3c345909ea

### Fields

| Field | Type |
|------|------|
| `base_currency_iso_code` | `string` |
| `currency_iso_code` | `string` |

## RestV10PotentialChangeOrdersPostResponse201CustomFields
- Role: nested
- Parent: RestV10PotentialChangeOrdersPostResponse201DataObject
- Schema Name: RestV10PotentialChangeOrdersPostResponse201CustomFields
- Schema ID: schema:anon/fbbbdf310d374c7df5714c86d51abac7a107e10a

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV10PotentialChangeOrdersPostResponse201DataObject
- Schema Name: RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/990ff11816957d5e13e8054a3b4018ca5a889aae

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV10PotentialChangeOrdersPostResponse201DataObject
- Schema Name: RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/2ca25eca8308998fe557ed8b7c6a2efae4b3c787

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV10PotentialChangeOrdersPostResponse201DataObject
- Schema Name: RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/8ac6165387eee0f8b62fd6116b007679069365e9

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV10PotentialChangeOrdersPostResponse201DataObject
- Schema Name: RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/e3d6cf7b64c48c5d41072f1f551520b2e5e9c56d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV10PotentialChangeOrdersPostResponse201DataObject
- Schema Name: RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/3a3c35d457351cba94d43fe7ae5875cdca53185f

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV10PotentialChangeOrdersPostResponse201DataObject
- Schema Name: RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/bfeb38dd91125f9638d7a4d955a8a35669e8d683
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV10PotentialChangeOrdersPostResponse201DataObject
- Schema Name: RestV10PotentialChangeOrdersPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/3e79a4fea4c4a312821d65e59e171469329ba818

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |

## RestV10PotentialChangeOrdersPostResponse201Status
- Role: nested
- Parent: RestV10PotentialChangeOrdersPostResponse201DataObject
- Schema Name: RestV10PotentialChangeOrdersPostResponse201Status
- Schema ID: schema:anon/5b89f75b59f65acdfdc32f08e622b0fbb79dc552

### Enum

Values: draft, not_pricing, pricing, pending, revised, proceeding, not_proceeding, no_charge, approved, rejected, void

## RestV10PotentialChangeOrdersPostResponse201Vendor
- Role: nested
- Parent: RestV10PotentialChangeOrdersPostResponse201DataObject
- Schema Name: RestV10PotentialChangeOrdersPostResponse201Vendor
- Schema ID: schema:anon/2b6fa06571868b6fe9370397176acbf74e3356b2
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
