# RestV10FilesPostResponse201DataObject

## RestV10FilesPostResponse201DataObject
- Role: parent
- Schema Name: RestV10FilesPostResponse201
- Schema ID: schema:anon/17bb880c084d5eaa910ba5f60c4f5de2419e1829
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `parent_id` | `int` |
| `size` | `int` |
| `description` | `string` |
| `updated_at` | `string` |
| `created_at` | `string` |
| `checked_out_until` | `string` |
| `name_with_path` | `string` |
| `private` | `bool` |
| `is_tracked` | `bool` |
| `tracked_folder` | `object` |
| `checked_out_by` | `RestV10FilesPostResponse201CheckedOutBy` |
| `file_type` | `string` |
| `file_versions` | `RestV10FilesPostResponse201FileVersionsItem[]` |
| `legacy_id` | `int` |
| `is_deleted` | `bool` |
| `custom_fields` | `RestV10FilesPostResponse201CustomFields` |

### Nested Types
- `RestV10FilesPostResponse201CheckedOutBy`
- `RestV10FilesPostResponse201CustomFields`
- `RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}`
- `RestV10FilesPostResponse201FileVersionsItem`

## RestV10FilesPostResponse201CheckedOutBy
- Role: nested
- Parent: RestV10FilesPostResponse201DataObject
- Schema Name: RestV10FilesPostResponse201CheckedOutBy
- Schema ID: schema:anon/43e8f94f9cda073fd9587b85933ddac45ea39d71
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10FilesPostResponse201CustomFields
- Role: nested
- Parent: RestV10FilesPostResponse201DataObject
- Schema Name: RestV10FilesPostResponse201CustomFields
- Schema ID: schema:anon/18c858aabec7b2c6828e2c316ea32d80e8f6c1be

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV10FilesPostResponse201DataObject
- Schema Name: RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/d7aaf7e4245f8b5e58720e73973a9fdbdbc7839e

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV10FilesPostResponse201DataObject
- Schema Name: RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/8178757753fe7302f7d5443936cb13b481bd73ff

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV10FilesPostResponse201DataObject
- Schema Name: RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/d50bbe7063fb38ebfcc50625f772776d0020e2f7

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV10FilesPostResponse201DataObject
- Schema Name: RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/98dfbe72f61b8f25de0fb5b18d6fa8d9a4ec580a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV10FilesPostResponse201DataObject
- Schema Name: RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/33d4a72922e5630c3242f8b04f6ee313e990b793

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV10FilesPostResponse201DataObject
- Schema Name: RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/87cff48788164388a7c8910cf94ab26c21bee6e1
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV10FilesPostResponse201DataObject
- Schema Name: RestV10FilesPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/8c3d88cb61be32fb0e8459abd64e13d194ffdb10

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |

## RestV10FilesPostResponse201FileVersionsItem
- Role: nested
- Parent: RestV10FilesPostResponse201DataObject
- Schema Name: RestV10FilesPostResponse201FileVersionsItem
- Schema ID: schema:anon/1d00265fe7c9f50855b9dc8660089c1a3fe6d764

### Fields
