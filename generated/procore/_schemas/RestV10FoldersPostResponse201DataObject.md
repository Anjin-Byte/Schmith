# RestV10FoldersPostResponse201DataObject

## RestV10FoldersPostResponse201DataObject
- Role: parent
- Schema Name: RestV10FoldersPostResponse201
- Schema ID: schema:anon/bc4cc67bf34c1d0cbfc740e556480fda5d9a9942
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `parent_id` | `int` |
| `private` | `bool` |
| `updated_at` | `string` |
| `is_tracked` | `bool` |
| `tracked_folder` | `object` |
| `name_with_path` | `string` |
| `folders` | `object[]` |
| `files` | `RestV10FoldersPostResponse201FoldersItem[]` |
| `read_only` | `bool` |
| `is_deleted` | `bool` |
| `is_recycle_bin` | `bool` |
| `has_children` | `bool` |
| `has_children_files` | `bool` |
| `has_children_folders` | `bool` |
| `custom_fields` | `RestV10FoldersPostResponse201CustomFields` |

### Nested Types
- `RestV10FoldersPostResponse201CustomFields`
- `RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}`

## RestV10FoldersPostResponse201CustomFields
- Role: nested
- Parent: RestV10FoldersPostResponse201DataObject
- Schema Name: RestV10FoldersPostResponse201CustomFields
- Schema ID: schema:anon/18c858aabec7b2c6828e2c316ea32d80e8f6c1be

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV10FoldersPostResponse201DataObject
- Schema Name: RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/d7aaf7e4245f8b5e58720e73973a9fdbdbc7839e

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV10FoldersPostResponse201DataObject
- Schema Name: RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/8178757753fe7302f7d5443936cb13b481bd73ff

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV10FoldersPostResponse201DataObject
- Schema Name: RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/d50bbe7063fb38ebfcc50625f772776d0020e2f7

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV10FoldersPostResponse201DataObject
- Schema Name: RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/98dfbe72f61b8f25de0fb5b18d6fa8d9a4ec580a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV10FoldersPostResponse201DataObject
- Schema Name: RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/33d4a72922e5630c3242f8b04f6ee313e990b793

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV10FoldersPostResponse201DataObject
- Schema Name: RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/87cff48788164388a7c8910cf94ab26c21bee6e1
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV10FoldersPostResponse201DataObject
- Schema Name: RestV10FoldersPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/8c3d88cb61be32fb0e8459abd64e13d194ffdb10

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |
