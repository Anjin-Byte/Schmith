# RestV20ProjectsProjectIdDocumentsGetResponse200DataObject

## RestV20ProjectsProjectIdDocumentsGetResponse200DataObject
- Role: parent
- Schema Name: RestV20ProjectsProjectIdDocumentsGetResponse200
- Schema ID: schema:anon/4a0cdad008de0ebdda415a736643bbb4f212374e

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20ProjectsProjectIdDocumentsGetResponse200DataItem[]` |

### Nested Types
- `RestV20ProjectsProjectIdDocumentsGetResponse200DataItem`
- `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemChildren`
- `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCreatedBy`
- `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFields`
- `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldStringDefinitionId}`
- `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemDocumentType`
- `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemFile`
- `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemFileCheckedOutBy`
- `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemFileCurrentVersion`
- `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemPrivateParent`

## RestV20ProjectsProjectIdDocumentsGetResponse200DataItem
- Role: nested
- Parent: RestV20ProjectsProjectIdDocumentsGetResponse200DataObject
- Schema Name: RestV20ProjectsProjectIdDocumentsGetResponse200DataItem
- Schema ID: schema:anon/94b68aee2032ac56f6dc8d49e6b6269759f5d3b4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |
| `parent_id` | `string` |
| `created_at` | `string` |
| `created_by` | `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCreatedBy` |
| `updated_at` | `string` |
| `read_only` | `bool` |
| `is_deleted` | `bool` |
| `is_recycle_bin` | `bool` |
| `document_type` | `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemDocumentType` |
| `is_tracked` | `bool` |
| `private` | `bool` |
| `private_parent` | `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemPrivateParent` |
| `tracked_folder` | `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemPrivateParent` |
| `file` | `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemFile` |
| `children` | `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemChildren` |
| `custom_fields` | `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFields` |

## RestV20ProjectsProjectIdDocumentsGetResponse200DataItemChildren
- Role: nested
- Parent: RestV20ProjectsProjectIdDocumentsGetResponse200DataObject
- Schema Name: RestV20ProjectsProjectIdDocumentsGetResponse200DataItemChildren
- Schema ID: schema:anon/583e0e20f8f90649ec4bcafeac362b87512cebef

### Fields

| Field | Type |
|------|------|
| `has_children` | `bool` |
| `has_children_files` | `bool` |
| `has_children_folders` | `bool` |

## RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCreatedBy
- Role: nested
- Parent: RestV20ProjectsProjectIdDocumentsGetResponse200DataObject
- Schema Name: RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCreatedBy
- Schema ID: schema:anon/5dcaef214c2dd91e4f2b272465390b81ea7a68d7

### Fields

## RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFields
- Role: nested
- Parent: RestV20ProjectsProjectIdDocumentsGetResponse200DataObject
- Schema Name: RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFields
- Schema ID: schema:anon/ffb17af20f748f4ecb1a7db57df7acee86239c93

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV20ProjectsProjectIdDocumentsGetResponse200DataObject
- Schema Name: RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/990ff11816957d5e13e8054a3b4018ca5a889aae

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV20ProjectsProjectIdDocumentsGetResponse200DataObject
- Schema Name: RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/b42f64543b85bfbcb27305db4d99a0be8f995586

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |

## RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV20ProjectsProjectIdDocumentsGetResponse200DataObject
- Schema Name: RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/d1e172003e134af41e6a51c8046c5a17f33564ad

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV20ProjectsProjectIdDocumentsGetResponse200DataObject
- Schema Name: RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/ad6904eddf33a677edcace4bba5918b9d07dfbff
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `label` | `string` |

## RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV20ProjectsProjectIdDocumentsGetResponse200DataObject
- Schema Name: RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/233491d569c1955ef00d165ff29a8cb3168ae8c5

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV20ProjectsProjectIdDocumentsGetResponse200DataObject
- Schema Name: RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/6bd49b3a26602ca8b67dc5189b31c78af2107bcc
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `label` | `string` |

## RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV20ProjectsProjectIdDocumentsGetResponse200DataObject
- Schema Name: RestV20ProjectsProjectIdDocumentsGetResponse200DataItemCustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/3e79a4fea4c4a312821d65e59e171469329ba818

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |

## RestV20ProjectsProjectIdDocumentsGetResponse200DataItemDocumentType
- Role: nested
- Parent: RestV20ProjectsProjectIdDocumentsGetResponse200DataObject
- Schema Name: RestV20ProjectsProjectIdDocumentsGetResponse200DataItemDocumentType
- Schema ID: schema:anon/d228fd904ae99f89a9eae678926709aa556acc10

### Enum

Values: file, folder

## RestV20ProjectsProjectIdDocumentsGetResponse200DataItemFile
- Role: nested
- Parent: RestV20ProjectsProjectIdDocumentsGetResponse200DataObject
- Schema Name: RestV20ProjectsProjectIdDocumentsGetResponse200DataItemFile
- Schema ID: schema:anon/2d886f7b8025ba14b86bb67a1f6dadc42af73c76

### Fields

| Field | Type |
|------|------|
| `checked_out_by` | `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemFileCheckedOutBy` |
| `checked_out_until` | `string` |
| `current_version` | `RestV20ProjectsProjectIdDocumentsGetResponse200DataItemFileCurrentVersion` |
| `description` | `string` |
| `file_type` | `string` |

## RestV20ProjectsProjectIdDocumentsGetResponse200DataItemFileCheckedOutBy
- Role: nested
- Parent: RestV20ProjectsProjectIdDocumentsGetResponse200DataObject
- Schema Name: RestV20ProjectsProjectIdDocumentsGetResponse200DataItemFileCheckedOutBy
- Schema ID: schema:anon/ead64bcba07d1071ab8f1a5e2d189e01ef843f87

### Fields

| Field | Type |
|------|------|
| `company_name` | `string` |

## RestV20ProjectsProjectIdDocumentsGetResponse200DataItemFileCurrentVersion
- Role: nested
- Parent: RestV20ProjectsProjectIdDocumentsGetResponse200DataObject
- Schema Name: RestV20ProjectsProjectIdDocumentsGetResponse200DataItemFileCurrentVersion
- Schema ID: schema:anon/65e345297fc336e6319a0d3e65892a57de0fd52a

### Fields

## RestV20ProjectsProjectIdDocumentsGetResponse200DataItemPrivateParent
- Role: nested
- Parent: RestV20ProjectsProjectIdDocumentsGetResponse200DataObject
- Schema Name: RestV20ProjectsProjectIdDocumentsGetResponse200DataItemPrivateParent
- Schema ID: schema:anon/39da484f43b4f32808c38d2c67c641b653299af0
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |
