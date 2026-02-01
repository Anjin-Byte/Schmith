# RestV10FilesIdPatchResponse409DataObject

## RestV10FilesIdPatchResponse409DataObject
- Role: parent
- Schema Name: RestV10FilesIdPatchResponse409
- Schema ID: schema:anon/93668c30e3c34f33df50dfc2ebb1701b21692ac4

### Fields

| Field | Type |
|------|------|
| `errors` | `RestV10FilesIdPatchResponse409Errors` |
| `error_type` | `string` |
| `file` | `RestV10FilesIdPatchResponse409File` |

### Nested Types
- `RestV10FilesIdPatchResponse409Errors`
- `RestV10FilesIdPatchResponse409File`
- `RestV10FilesIdPatchResponse409FileCheckedOutBy`
- `RestV10FilesIdPatchResponse409FileCustomFields`
- `RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldStringDefinitionId}`
- `RestV10FilesIdPatchResponse409FileFileVersionsItem`

## RestV10FilesIdPatchResponse409Errors
- Role: nested
- Parent: RestV10FilesIdPatchResponse409DataObject
- Schema Name: RestV10FilesIdPatchResponse409Errors
- Schema ID: schema:anon/72fbc9380819109e9457a2fcfe92d44171baad9a

### Fields

| Field | Type |
|------|------|
| `base` | `string[]` |

## RestV10FilesIdPatchResponse409File
- Role: nested
- Parent: RestV10FilesIdPatchResponse409DataObject
- Schema Name: RestV10FilesIdPatchResponse409File
- Schema ID: schema:anon/a9134e72b337b019175e4d723356282ce9576094
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
| `checked_out_by` | `RestV10FilesIdPatchResponse409FileCheckedOutBy` |
| `file_type` | `string` |
| `file_versions` | `RestV10FilesIdPatchResponse409FileFileVersionsItem[]` |
| `legacy_id` | `int` |
| `is_deleted` | `bool` |
| `custom_fields` | `RestV10FilesIdPatchResponse409FileCustomFields` |

## RestV10FilesIdPatchResponse409FileCheckedOutBy
- Role: nested
- Parent: RestV10FilesIdPatchResponse409DataObject
- Schema Name: RestV10FilesIdPatchResponse409FileCheckedOutBy
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10FilesIdPatchResponse409FileCustomFields
- Role: nested
- Parent: RestV10FilesIdPatchResponse409DataObject
- Schema Name: RestV10FilesIdPatchResponse409FileCustomFields
- Schema ID: schema:anon/18c858aabec7b2c6828e2c316ea32d80e8f6c1be

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV10FilesIdPatchResponse409DataObject
- Schema Name: RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/d7aaf7e4245f8b5e58720e73973a9fdbdbc7839e

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV10FilesIdPatchResponse409DataObject
- Schema Name: RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/8178757753fe7302f7d5443936cb13b481bd73ff

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV10FilesIdPatchResponse409DataObject
- Schema Name: RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/d50bbe7063fb38ebfcc50625f772776d0020e2f7

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV10FilesIdPatchResponse409DataObject
- Schema Name: RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/98dfbe72f61b8f25de0fb5b18d6fa8d9a4ec580a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV10FilesIdPatchResponse409DataObject
- Schema Name: RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/33d4a72922e5630c3242f8b04f6ee313e990b793

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV10FilesIdPatchResponse409DataObject
- Schema Name: RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/87cff48788164388a7c8910cf94ab26c21bee6e1
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV10FilesIdPatchResponse409DataObject
- Schema Name: RestV10FilesIdPatchResponse409FileCustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/8c3d88cb61be32fb0e8459abd64e13d194ffdb10

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |

## RestV10FilesIdPatchResponse409FileFileVersionsItem
- Role: nested
- Parent: RestV10FilesIdPatchResponse409DataObject
- Schema Name: RestV10FilesIdPatchResponse409FileFileVersionsItem
- Schema ID: schema:anon/71e8c663025fe3602d1203c533197f4144a33ea5

### Fields
