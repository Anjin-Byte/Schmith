# RestV10FoldersGetResponse200DataObject

## RestV10FoldersGetResponse200DataObject
- Role: parent
- Schema Name: RestV10FoldersGetResponse200
- Schema ID: schema:anon/cc3be3ae933c5f8e1da34219cfe931990af73a41
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
| `folders` | `RestV10FoldersGetResponse200FoldersItem[]` |
| `files` | `RestV10FoldersGetResponse200FilesItem[]` |
| `read_only` | `bool` |
| `is_deleted` | `bool` |
| `is_recycle_bin` | `bool` |
| `has_children` | `bool` |
| `has_children_files` | `bool` |
| `has_children_folders` | `bool` |
| `custom_fields` | `RestV10FoldersGetResponse200FoldersItemCustomFields` |

### Nested Types
- `RestV10FoldersGetResponse200FilesItem`
- `RestV10FoldersGetResponse200FilesItemCheckedOutBy`
- `RestV10FoldersGetResponse200FilesItemFileVersionsItem`
- `RestV10FoldersGetResponse200FoldersItem`
- `RestV10FoldersGetResponse200FoldersItemCustomFields`
- `RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldStringDefinitionId}`

## RestV10FoldersGetResponse200FilesItem
- Role: nested
- Parent: RestV10FoldersGetResponse200DataObject
- Schema Name: RestV10FoldersGetResponse200FilesItem
- Schema ID: schema:anon/1ac9f038ee409424fce1ad5a2a917e5c17d0dae5
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
| `tracked_folder` | `RestV10FoldersGetResponse200TrackedFolder` |
| `checked_out_by` | `RestV10FoldersGetResponse200FilesItemCheckedOutBy` |
| `file_type` | `string` |
| `file_versions` | `RestV10FoldersGetResponse200FilesItemFileVersionsItem[]` |
| `legacy_id` | `int` |
| `is_deleted` | `bool` |
| `custom_fields` | `RestV10FoldersGetResponse200FoldersItemCustomFields` |

## RestV10FoldersGetResponse200FilesItemCheckedOutBy
- Role: nested
- Parent: RestV10FoldersGetResponse200DataObject
- Schema Name: RestV10FoldersGetResponse200FilesItemCheckedOutBy
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10FoldersGetResponse200FilesItemFileVersionsItem
- Role: nested
- Parent: RestV10FoldersGetResponse200DataObject
- Schema Name: RestV10FoldersGetResponse200FilesItemFileVersionsItem
- Schema ID: schema:anon/815ad0810f99e957b0db32f0ed04dd1a4ef0291d

### Fields

## RestV10FoldersGetResponse200FoldersItem
- Role: nested
- Parent: RestV10FoldersGetResponse200DataObject
- Schema Name: RestV10FoldersGetResponse200FoldersItem
- Schema ID: schema:anon/851b6f2bf4fe60bc70f5969dd1aca67608738280
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
| `tracked_folder` | `RestV10FoldersGetResponse200TrackedFolder` |
| `name_with_path` | `string` |
| `folders` | `object[]` |
| `files` | `RestV10FoldersGetResponse200FoldersItemFoldersItem[]` |
| `read_only` | `bool` |
| `is_deleted` | `bool` |
| `is_recycle_bin` | `bool` |
| `has_children` | `bool` |
| `has_children_files` | `bool` |
| `has_children_folders` | `bool` |
| `custom_fields` | `RestV10FoldersGetResponse200FoldersItemCustomFields` |

## RestV10FoldersGetResponse200FoldersItemCustomFields
- Role: nested
- Parent: RestV10FoldersGetResponse200DataObject
- Schema Name: RestV10FoldersGetResponse200FoldersItemCustomFields
- Schema ID: schema:anon/18c858aabec7b2c6828e2c316ea32d80e8f6c1be

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV10FoldersGetResponse200DataObject
- Schema Name: RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/d7aaf7e4245f8b5e58720e73973a9fdbdbc7839e

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV10FoldersGetResponse200DataObject
- Schema Name: RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/8178757753fe7302f7d5443936cb13b481bd73ff

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV10FoldersGetResponse200DataObject
- Schema Name: RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/d50bbe7063fb38ebfcc50625f772776d0020e2f7

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV10FoldersGetResponse200DataObject
- Schema Name: RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/98dfbe72f61b8f25de0fb5b18d6fa8d9a4ec580a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV10FoldersGetResponse200DataObject
- Schema Name: RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/33d4a72922e5630c3242f8b04f6ee313e990b793

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV10FoldersGetResponse200DataObject
- Schema Name: RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/87cff48788164388a7c8910cf94ab26c21bee6e1
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV10FoldersGetResponse200DataObject
- Schema Name: RestV10FoldersGetResponse200FoldersItemCustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/8c3d88cb61be32fb0e8459abd64e13d194ffdb10

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |
