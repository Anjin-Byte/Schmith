# RestV10SpecificationSectionRevisionsIdGetResponse200DataObject

## RestV10SpecificationSectionRevisionsIdGetResponse200DataObject
- Role: parent
- Schema Name: RestV10SpecificationSectionRevisionsIdGetResponse200
- Schema ID: schema:anon/feb33012036dbdfeef8086f280caf3fbf1400798
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `source_id` | `int` |
| `name` | `string` |
| `section_id` | `int` |
| `section_name` | `string` |
| `source_create_time` | `string` |
| `source_update_time` | `string` |
| `url` | `string` |
| `custom_fields` | `RestV10SpecificationSectionRevisionsIdGetResponse200CustomFields` |

### Nested Types
- `RestV10SpecificationSectionRevisionsIdGetResponse200CustomFields`
- `RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldStringDefinitionId}`

## RestV10SpecificationSectionRevisionsIdGetResponse200CustomFields
- Role: nested
- Parent: RestV10SpecificationSectionRevisionsIdGetResponse200DataObject
- Schema Name: RestV10SpecificationSectionRevisionsIdGetResponse200CustomFields
- Schema ID: schema:anon/18c858aabec7b2c6828e2c316ea32d80e8f6c1be

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV10SpecificationSectionRevisionsIdGetResponse200DataObject
- Schema Name: RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/d7aaf7e4245f8b5e58720e73973a9fdbdbc7839e

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV10SpecificationSectionRevisionsIdGetResponse200DataObject
- Schema Name: RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/8178757753fe7302f7d5443936cb13b481bd73ff

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV10SpecificationSectionRevisionsIdGetResponse200DataObject
- Schema Name: RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/d50bbe7063fb38ebfcc50625f772776d0020e2f7

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV10SpecificationSectionRevisionsIdGetResponse200DataObject
- Schema Name: RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/98dfbe72f61b8f25de0fb5b18d6fa8d9a4ec580a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV10SpecificationSectionRevisionsIdGetResponse200DataObject
- Schema Name: RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/33d4a72922e5630c3242f8b04f6ee313e990b793

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV10SpecificationSectionRevisionsIdGetResponse200DataObject
- Schema Name: RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/87cff48788164388a7c8910cf94ab26c21bee6e1
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV10SpecificationSectionRevisionsIdGetResponse200DataObject
- Schema Name: RestV10SpecificationSectionRevisionsIdGetResponse200CustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/8c3d88cb61be32fb0e8459abd64e13d194ffdb10

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |
