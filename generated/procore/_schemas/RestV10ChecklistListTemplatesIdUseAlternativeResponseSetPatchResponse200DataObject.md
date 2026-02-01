# RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200DataObject

## RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200
- Schema ID: schema:anon/f32a8827756f151919e1800ffccd081a4c2d6a17
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `description` | `string` |
| `company_description` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `inspection_type` | `RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200InspectionType` |
| `alternative_response_set_id` | `int` |
| `response_set` | `RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200ResponseSet` |
| `location` | `RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200Location` |
| `trade` | `RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200Trade` |
| `created_by` | `RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200CreatedBy` |
| `attachments` | `RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200AttachmentsItem[]` |
| `sections` | `RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200SectionsItem[]` |

### Nested Types
- `RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200AttachmentsItem`
- `RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200CreatedBy`
- `RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200InspectionType`
- `RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200Location`
- `RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200ResponseSet`
- `RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200SectionsItem`
- `RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200SectionsItemItemsItem`
- `RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200SectionsItemItemsItemStatus`
- `RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200Trade`

## RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200AttachmentsItem
- Role: nested
- Parent: RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200DataObject
- Schema Name: RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200AttachmentsItem
- Schema ID: schema:anon/c337dee3df228286468f0ff6d8c4852152f75cf4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |

## RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200CreatedBy
- Role: nested
- Parent: RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200DataObject
- Schema Name: RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200CreatedBy
- Schema ID: schema:anon/121288c30b14d925f7a9c37e3dca7d3325344ec8
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200InspectionType
- Role: nested
- Parent: RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200DataObject
- Schema Name: RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200InspectionType
- Schema ID: schema:anon/0862efed6866dc6d14cf411898e45017c6264764
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200Location
- Role: nested
- Parent: RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200DataObject
- Schema Name: RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200Location
- Schema ID: schema:anon/83764bdea4a801c741ebd221ca2efda41a6b4a5b
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

## RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200ResponseSet
- Role: nested
- Parent: RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200DataObject
- Schema Name: RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200ResponseSet
- Schema ID: schema:anon/aec14814553850d7366c1c8f5208ca450a921b35

### Fields

| Field | Type |
|------|------|
| `conforming_response` | `string` |
| `deficient_response` | `string` |
| `global` | `bool` |

## RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200SectionsItem
- Role: nested
- Parent: RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200DataObject
- Schema Name: RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200SectionsItem
- Schema ID: schema:anon/66fa5b6b235ca93afd19db4b2d7f79c2c61e52f4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `position` | `int` |
| `items` | `RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200SectionsItemItemsItem[]` |

## RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200SectionsItemItemsItem
- Role: nested
- Parent: RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200DataObject
- Schema Name: RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200SectionsItemItemsItem
- Schema ID: schema:anon/f6b064977bc667bcdabc07c262dfbc8fa59eb1dd
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `status` | `RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200SectionsItemItemsItemStatus` |
| `section_id` | `int` |
| `position` | `int` |

## RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200SectionsItemItemsItemStatus
- Role: nested
- Parent: RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200DataObject
- Schema Name: RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200SectionsItemItemsItemStatus
- Schema ID: schema:anon/6a900c1c970095cb1c98c7e28cac9b230776556f

### Enum

Values: yes, no, n/a, none

## RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200Trade
- Role: nested
- Parent: RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200DataObject
- Schema Name: RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchResponse200Trade
- Schema ID: schema:anon/0dc5e552de3604c2a1edbab95ae258e0afaa1167
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `active` | `bool` |
| `updated_at` | `string` |
