# RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200DataObject

## RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200DataObject
- Role: parent
- Schema Name: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200
- Schema ID: schema:anon/e4cf001eb598ba8eb4236b8c662fbaa081f02752
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `date` | `string` |
| `number` | `int` |
| `created_by` | `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200CreatedBy` |
| `name` | `string` |
| `status` | `string` |
| `timecard_entries` | `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItem[]` |

### Nested Types
- `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200CreatedBy`
- `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItem`
- `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCostCode`
- `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCrew`
- `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFields`
- `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldStringDefinitionId}`
- `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemLocation`
- `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemTimecardTimeType`

## RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200CreatedBy
- Role: nested
- Parent: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200CreatedBy
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItem
- Role: nested
- Parent: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItem
- Schema ID: schema:anon/bec319389a4ae7e1faf450cc470f20ac379221c7
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
| `crew` | `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCrew` |
| `cost_code` | `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCostCode` |
| `created_by` | `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200CreatedBy` |
| `login_information` | `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200CreatedBy` |
| `location` | `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemLocation` |
| `timecard_time_type` | `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemTimecardTimeType` |
| `wbs_code_id` | `int` |
| `custom_fields` | `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFields` |

## RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCostCode
- Role: nested
- Parent: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCostCode
- Schema ID: schema:anon/7a7d890c7fa0b0fc15a34087ae7717936b876e3d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCrew
- Role: nested
- Parent: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCrew
- Schema ID: schema:anon/1b84fbeda50b5c7abe4576ef5c771c87841511b4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFields
- Role: nested
- Parent: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFields
- Schema ID: schema:anon/18c858aabec7b2c6828e2c316ea32d80e8f6c1be

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/d7aaf7e4245f8b5e58720e73973a9fdbdbc7839e

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/8178757753fe7302f7d5443936cb13b481bd73ff

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/d50bbe7063fb38ebfcc50625f772776d0020e2f7

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/98dfbe72f61b8f25de0fb5b18d6fa8d9a4ec580a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/33d4a72922e5630c3242f8b04f6ee313e990b793

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/87cff48788164388a7c8910cf94ab26c21bee6e1
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemCustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/8c3d88cb61be32fb0e8459abd64e13d194ffdb10

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |

## RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemLocation
- Role: nested
- Parent: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemLocation
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

## RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemTimecardTimeType
- Role: nested
- Parent: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchResponse200TimecardEntriesItemTimecardTimeType
- Schema ID: schema:anon/624e5b84c1ef324765d2f2603c1fb9e89c850e60
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `time_type` | `string` |
| `abbreviated_time_type` | `string` |
| `global` | `bool` |
