# RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200DataObject

## RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200
- Schema ID: schema:anon/c2ac0185de38e60b640b9809047a9af0b47ccb21
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `drawing_date` | `string` |
| `received_date` | `string` |
| `revision_number` | `string` |
| `floorplan` | `bool` |
| `current` | `bool` |
| `drawing_id` | `int` |
| `drawing_set` | `RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200DrawingSet` |
| `ordered_revision_ids` | `int[]` |
| `custom_fields` | `RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFields` |

### Nested Types
- `RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFields`
- `RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldStringDefinitionId}`
- `RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200DrawingSet`

## RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFields
- Role: nested
- Parent: RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFields
- Schema ID: schema:anon/9b37a2ef5ea5308a365e67b3ffcec6a0041afb45

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/d7aaf7e4245f8b5e58720e73973a9fdbdbc7839e

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/8178757753fe7302f7d5443936cb13b481bd73ff

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/d50bbe7063fb38ebfcc50625f772776d0020e2f7

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/98dfbe72f61b8f25de0fb5b18d6fa8d9a4ec580a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/33d4a72922e5630c3242f8b04f6ee313e990b793

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/87cff48788164388a7c8910cf94ab26c21bee6e1
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200CustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/8c3d88cb61be32fb0e8459abd64e13d194ffdb10

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |

## RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200DrawingSet
- Role: nested
- Parent: RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDrawingRevisionsIdPatchResponse200DrawingSet
- Schema ID: schema:anon/ce5723cbf75802443ae9ca324246eb951b131281
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
