# RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject

## RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Role: parent
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201
- Schema ID: schema:anon/8d43ef5cef521d7573fed3c736369c456b97df6b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `list_template_id` | `int` |
| `list_template_name` | `string` |
| `number` | `int` |
| `status` | `RestV11ProjectsProjectIdChecklistListsPostResponse201Status` |
| `location` | `RestV11ProjectsProjectIdChecklistListsPostResponse201Location` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `closed_at` | `string` |
| `drawing_ids` | `int[]` |
| `current_drawing_revision_ids` | `int[]` |
| `description` | `string` |
| `deleted` | `bool` |
| `due_at` | `string` |
| `identifier` | `string` |
| `inspection_date` | `string` |
| `inspection_type` | `RestV11ProjectsProjectIdChecklistListsPostResponse201InspectionType` |
| `private` | `bool` |
| `created_by` | `RestV11ProjectsProjectIdChecklistListsPostResponse201CreatedBy` |
| `closed_by` | `RestV11ProjectsProjectIdChecklistListsPostResponse201ClosedBy` |
| `responsible_contractor` | `RestV11ProjectsProjectIdChecklistListsPostResponse201ResponsibleContractor` |
| `point_of_contact` | `RestV11ProjectsProjectIdChecklistListsPostResponse201ClosedBy` |
| `trade` | `RestV11ProjectsProjectIdChecklistListsPostResponse201Trade` |
| `inspectors` | `RestV11ProjectsProjectIdChecklistListsPostResponse201CreatedBy[]` |
| `distribution_members` | `RestV11ProjectsProjectIdChecklistListsPostResponse201CreatedBy[]` |
| `signature_requests` | `RestV11ProjectsProjectIdChecklistListsPostResponse201SignatureRequestsItem[]` |
| `managed_equipment_id` | `int` |
| `specification_section` | `RestV11ProjectsProjectIdChecklistListsPostResponse201SpecificationSection` |
| `attachments` | `RestV11ProjectsProjectIdChecklistListsPostResponse201AttachmentsItem[]` |
| `conforming_item_count` | `int` |
| `deficient_item_count` | `int` |
| `not_applicable_item_count` | `int` |
| `neutral_item_count` | `int` |
| `inspected_item_count` | `int` |
| `observations_count` | `int` |
| `closed_observations_count` | `int` |
| `item_count` | `int` |
| `respondable_item_count` | `int` |
| `custom_fields` | `RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFields` |
| `template_id` | `int` |
| `overdue` | `bool` |
| `reinspected_by_id` | `string` |
| `reinspected_from_id` | `string` |

### Nested Types
- `RestV11ProjectsProjectIdChecklistListsPostResponse201AttachmentsItem`
- `RestV11ProjectsProjectIdChecklistListsPostResponse201ClosedBy`
- `RestV11ProjectsProjectIdChecklistListsPostResponse201CreatedBy`
- `RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFields`
- `RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}`
- `RestV11ProjectsProjectIdChecklistListsPostResponse201InspectionType`
- `RestV11ProjectsProjectIdChecklistListsPostResponse201Location`
- `RestV11ProjectsProjectIdChecklistListsPostResponse201ResponsibleContractor`
- `RestV11ProjectsProjectIdChecklistListsPostResponse201SignatureRequestsItem`
- `RestV11ProjectsProjectIdChecklistListsPostResponse201SignatureRequestsItemSignatory`
- `RestV11ProjectsProjectIdChecklistListsPostResponse201SignatureRequestsItemSignature`
- `RestV11ProjectsProjectIdChecklistListsPostResponse201SignatureRequestsItemSignatureAttachment`
- `RestV11ProjectsProjectIdChecklistListsPostResponse201SpecificationSection`
- `RestV11ProjectsProjectIdChecklistListsPostResponse201Status`
- `RestV11ProjectsProjectIdChecklistListsPostResponse201Trade`

## RestV11ProjectsProjectIdChecklistListsPostResponse201AttachmentsItem
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201AttachmentsItem
- Schema ID: schema:anon/e762019c2e26006695cdb42c88a23e4a268865f1
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `thumbnail_url` | `string` |
| `name` | `string` |
| `filename` | `string` |
| `content_type` | `string` |
| `viewable_document_id` | `int` |

## RestV11ProjectsProjectIdChecklistListsPostResponse201ClosedBy
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201ClosedBy
- Schema ID: schema:anon/0a03023ef02b99e04c81d4bcbc9985f628b98c90
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV11ProjectsProjectIdChecklistListsPostResponse201CreatedBy
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201CreatedBy
- Schema ID: schema:anon/121288c30b14d925f7a9c37e3dca7d3325344ec8
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFields
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFields
- Schema ID: schema:anon/18c858aabec7b2c6828e2c316ea32d80e8f6c1be

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/d7aaf7e4245f8b5e58720e73973a9fdbdbc7839e

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/8178757753fe7302f7d5443936cb13b481bd73ff

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/d50bbe7063fb38ebfcc50625f772776d0020e2f7

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/98dfbe72f61b8f25de0fb5b18d6fa8d9a4ec580a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/33d4a72922e5630c3242f8b04f6ee313e990b793

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/87cff48788164388a7c8910cf94ab26c21bee6e1
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/8c3d88cb61be32fb0e8459abd64e13d194ffdb10

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |

## RestV11ProjectsProjectIdChecklistListsPostResponse201InspectionType
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201InspectionType
- Schema ID: schema:anon/15da4226f759b9f46fc09f42313ac0c4ff7037ec
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV11ProjectsProjectIdChecklistListsPostResponse201Location
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201Location
- Schema ID: schema:anon/fcdb22ec610a1ec2dd2ff4829048cc5fa0fe7810
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `code` | `string` |
| `node_name` | `string` |
| `parent_id` | `int` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV11ProjectsProjectIdChecklistListsPostResponse201ResponsibleContractor
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201ResponsibleContractor
- Schema ID: schema:anon/0656959b3860a779f0714e8e902477950c3e845c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV11ProjectsProjectIdChecklistListsPostResponse201SignatureRequestsItem
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201SignatureRequestsItem
- Schema ID: schema:anon/5526373e76eab4fc250e547022f0756a31b2025c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `signatory` | `RestV11ProjectsProjectIdChecklistListsPostResponse201SignatureRequestsItemSignatory` |
| `signature` | `RestV11ProjectsProjectIdChecklistListsPostResponse201SignatureRequestsItemSignature` |

## RestV11ProjectsProjectIdChecklistListsPostResponse201SignatureRequestsItemSignatory
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201SignatureRequestsItemSignatory
- Schema ID: schema:anon/803a12c7aea5299f4d566a8c46509c126a7db6c0

### Fields

## RestV11ProjectsProjectIdChecklistListsPostResponse201SignatureRequestsItemSignature
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201SignatureRequestsItemSignature
- Schema ID: schema:anon/e17ab36cd0a497676e8401d8f5440e9bb85ec741
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `captured_by` | `RestV11ProjectsProjectIdChecklistListsPostResponse201SignatureRequestsItemSignatory` |
| `captured_at` | `string` |
| `attachment` | `RestV11ProjectsProjectIdChecklistListsPostResponse201SignatureRequestsItemSignatureAttachment` |

## RestV11ProjectsProjectIdChecklistListsPostResponse201SignatureRequestsItemSignatureAttachment
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201SignatureRequestsItemSignatureAttachment
- Schema ID: schema:anon/1e0429c6f88905c0a0f1e29d76452254d44b0f24
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |
| `name` | `string` |
| `attached_to_item_id` | `int` |
| `attached_to_item_type` | `string` |
| `viewer_url` | `string` |

## RestV11ProjectsProjectIdChecklistListsPostResponse201SpecificationSection
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201SpecificationSection
- Schema ID: schema:anon/32dd8778c06830b33d3514a593851e3d96adeba6
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `current_revision_id` | `int` |
| `description` | `string` |
| `section` | `string` |
| `latest_revision_url` | `string` |

## RestV11ProjectsProjectIdChecklistListsPostResponse201Status
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201Status
- Schema ID: schema:anon/a8d0bbe690af9f70566800b8a131470934ecf0f2

### Enum

Values: Open, In Review, Closed

## RestV11ProjectsProjectIdChecklistListsPostResponse201Trade
- Role: nested
- Parent: RestV11ProjectsProjectIdChecklistListsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdChecklistListsPostResponse201Trade
- Schema ID: schema:anon/0e620c9e9f0fde9c200045e654e3ffe421c5d5f5
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `active` | `bool` |
| `updated_at` | `string` |
