# RestV10CompaniesCompanyIdTimesheetsPatchResponse200DataObject

## RestV10CompaniesCompanyIdTimesheetsPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10CompaniesCompanyIdTimesheetsPatchResponse200
- Schema ID: schema:anon/b07d6799ab95d94e42d127b0f653dbbd73f66145

### Fields

| Field | Type |
|------|------|
| `updated_timecard_entries` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItem[]` |

### Nested Types
- `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItem`
- `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemParty`
- `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimecardTimeType`
- `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatus`
- `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusCreatedBy`
- `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItem`
- `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCostCode`
- `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCrew`
- `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFields`
- `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldStringDefinitionId}`
- `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemLocation`
- `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemTimecardTimeType`

## RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdTimesheetsPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItem
- Schema ID: schema:anon/d14f0b611233e6c3ff17055a617ed46855b576c2
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `created_at` | `string` |
| `date` | `string` |
| `deleted_at` | `string` |
| `description` | `string` |
| `billable` | `bool` |
| `hours` | `string` |
| `updated_at` | `string` |
| `timecard_type` | `string` |
| `cost_code` | `string` |
| `origin_id` | `int` |
| `origin_data` | `string` |
| `timesheet_status` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatus` |
| `full_cost_code` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCostCode` |
| `created_by` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusCreatedBy` |
| `login_information` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusCreatedBy` |
| `party` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemParty` |
| `timecard_time_type` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimecardTimeType` |
| `line_item_type_id` | `int` |

## RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemParty
- Role: nested
- Parent: RestV10CompaniesCompanyIdTimesheetsPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemParty
- Schema ID: schema:anon/c2b1d340229e56b6ddbcd4f0909fcc8ef8e85a38
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimecardTimeType
- Role: nested
- Parent: RestV10CompaniesCompanyIdTimesheetsPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimecardTimeType
- Schema ID: schema:anon/07a28097fee5efba93d7d5f2d717be8dc5ed0e7c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `abbreviated_time_type` | `string` |
| `company_id` | `int` |
| `global` | `bool` |
| `time_type` | `string` |

## RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatus
- Role: nested
- Parent: RestV10CompaniesCompanyIdTimesheetsPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatus
- Schema ID: schema:anon/5a3e75626f19a642b3dd8c1b57919ccf91231c04
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `date` | `string` |
| `number` | `int` |
| `created_by` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusCreatedBy` |
| `name` | `string` |
| `status` | `string` |
| `timecard_entries` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItem[]` |

## RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusCreatedBy
- Role: nested
- Parent: RestV10CompaniesCompanyIdTimesheetsPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusCreatedBy
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdTimesheetsPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItem
- Schema ID: schema:anon/8e05c6971c0b55549192a2836f0c6be376d63842
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `created_at` | `string` |
| `date` | `string` |
| `deleted_at` | `string` |
| `description` | `string` |
| `hours` | `string` |
| `updated_at` | `string` |
| `time_in` | `string` |
| `time_out` | `string` |
| `injured` | `bool` |
| `lunch_time` | `int` |
| `billable` | `bool` |
| `origin_id` | `int` |
| `origin_data` | `string` |
| `crew` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCrew` |
| `custom_fields` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFields` |
| `cost_code` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCostCode` |
| `created_by` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusCreatedBy` |
| `login_information` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusCreatedBy` |
| `location` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemLocation` |
| `timecard_time_type` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemTimecardTimeType` |

## RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCostCode
- Role: nested
- Parent: RestV10CompaniesCompanyIdTimesheetsPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCostCode
- Schema ID: schema:anon/7a7d890c7fa0b0fc15a34087ae7717936b876e3d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCrew
- Role: nested
- Parent: RestV10CompaniesCompanyIdTimesheetsPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCrew
- Schema ID: schema:anon/1b84fbeda50b5c7abe4576ef5c771c87841511b4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFields
- Role: nested
- Parent: RestV10CompaniesCompanyIdTimesheetsPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFields
- Schema ID: schema:anon/18c858aabec7b2c6828e2c316ea32d80e8f6c1be

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV10CompaniesCompanyIdTimesheetsPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/d7aaf7e4245f8b5e58720e73973a9fdbdbc7839e

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV10CompaniesCompanyIdTimesheetsPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/8178757753fe7302f7d5443936cb13b481bd73ff

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV10CompaniesCompanyIdTimesheetsPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/d50bbe7063fb38ebfcc50625f772776d0020e2f7

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdTimesheetsPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/98dfbe72f61b8f25de0fb5b18d6fa8d9a4ec580a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV10CompaniesCompanyIdTimesheetsPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/33d4a72922e5630c3242f8b04f6ee313e990b793

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV10CompaniesCompanyIdTimesheetsPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/87cff48788164388a7c8910cf94ab26c21bee6e1
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV10CompaniesCompanyIdTimesheetsPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemCustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/8c3d88cb61be32fb0e8459abd64e13d194ffdb10

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |

## RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemLocation
- Role: nested
- Parent: RestV10CompaniesCompanyIdTimesheetsPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemLocation
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

## RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemTimecardTimeType
- Role: nested
- Parent: RestV10CompaniesCompanyIdTimesheetsPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdTimesheetsPatchResponse200UpdatedTimecardEntriesItemTimesheetStatusTimecardEntriesItemTimecardTimeType
- Schema ID: schema:anon/d0ae5ca4b3cddf12b06c7e9622896a55c019f807
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `time_type` | `string` |
| `abbreviated_time_type` | `string` |
| `global` | `bool` |
