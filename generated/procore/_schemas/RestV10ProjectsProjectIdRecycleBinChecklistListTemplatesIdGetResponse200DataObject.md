# RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200DataObject

## RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200
- Schema ID: schema:anon/7081355c650402161f6e6a3f51e9e5b3f50a3dde
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `synced_to` | `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SyncedTo` |
| `company_description` | `string` |
| `description` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `alternative_response_set_id` | `int` |
| `sections` | `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItem[]` |
| `inspection_type` | `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200InspectionType` |
| `trade` | `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200Trade` |
| `created_by` | `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200CreatedBy` |
| `company_attachments` | `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200CompanyAttachmentsItem[]` |
| `attachments` | `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200CompanyAttachmentsItem[]` |
| `response_set` | `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200ResponseSet` |

### Nested Types
- `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200CompanyAttachmentsItem`
- `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200CreatedBy`
- `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200InspectionType`
- `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200ResponseSet`
- `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItem`
- `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemItemsItem`
- `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemItemsItemResponseSet`
- `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemItemsItemResponseSetResponsesItem`
- `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemItemsItemResponseSetResponsesItemCorrespondingStatus`
- `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemItemsItemType`
- `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemSyncedTo`
- `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SyncedTo`
- `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200Trade`

## RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200CompanyAttachmentsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200CompanyAttachmentsItem
- Schema ID: schema:anon/c337dee3df228286468f0ff6d8c4852152f75cf4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |

## RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200CreatedBy
- Role: nested
- Parent: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200CreatedBy
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200InspectionType
- Role: nested
- Parent: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200InspectionType
- Schema ID: schema:anon/70a0a25824ff22a885740aacb4ba4ce02f429403
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `audit_transaction_timestamp` | `string` |
| `source_id` | `int` |
| `deleted_at` | `string` |
| `company_id` | `int` |
| `is_deletable` | `bool` |

## RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200ResponseSet
- Role: nested
- Parent: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200ResponseSet
- Schema ID: schema:anon/400810763760edf8ad2bb5e75920e17bbaa17e0a

### Fields

| Field | Type |
|------|------|
| `conforming_response` | `string` |
| `deficient_response` | `string` |
| `global` | `bool` |

## RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItem
- Schema ID: schema:anon/63d26bdd9c29fec8694bf7525a8510af02279ea9
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `position` | `int` |
| `items` | `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemItemsItem[]` |
| `synced_to` | `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemSyncedTo` |

## RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemItemsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemItemsItem
- Schema ID: schema:anon/0caf7bfb71d7661d2a29a1d8e6fda950084499ff
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `position` | `int` |
| `section_id` | `int` |
| `details` | `string` |
| `response_set` | `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemItemsItemResponseSet` |
| `response_type_id` | `int` |
| `type` | `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemItemsItemType` |

## RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemItemsItemResponseSet
- Role: nested
- Parent: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemItemsItemResponseSet
- Schema ID: schema:anon/847535af4ffef3558b79ad8539fa4126aedbba64
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `responses` | `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemItemsItemResponseSetResponsesItem[]` |

## RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemItemsItemResponseSetResponsesItem
- Role: nested
- Parent: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemItemsItemResponseSetResponsesItem
- Schema ID: schema:anon/642ea45d87a42b1e990b95c4ea0635cc56cf8328
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `item_status_id` | `int` |
| `name` | `string` |
| `corresponding_status` | `RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemItemsItemResponseSetResponsesItemCorrespondingStatus` |

## RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemItemsItemResponseSetResponsesItemCorrespondingStatus
- Role: nested
- Parent: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemItemsItemResponseSetResponsesItemCorrespondingStatus
- Schema ID: schema:anon/4052ef8599e05a33d45ffb52a43059c98bdf7b05

### Enum

Values: yes, no, n/a

## RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemItemsItemType
- Role: nested
- Parent: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemItemsItemType
- Schema ID: schema:anon/8b78fdbc8c80dc85688d34e0dfcf60a7b8510979
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `category` | `string` |
| `name` | `string` |

## RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemSyncedTo
- Role: nested
- Parent: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SectionsItemSyncedTo
- Schema ID: schema:anon/8483611571be36d9e74d30b85f708804d64e7b07
- Primary Key: CompanyId

### Fields

| Field | Type |
|------|------|
| `company_id` | `int` |
| `list_template_id` | `int` |

## RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SyncedTo
- Role: nested
- Parent: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200SyncedTo
- Schema ID: schema:anon/4833af108c554ec58a29de6d388a343b2d7a6838
- Primary Key: CompanyId

### Fields

| Field | Type |
|------|------|
| `company_id` | `int` |
| `list_template_id` | `int` |

## RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200Trade
- Role: nested
- Parent: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdRecycleBinChecklistListTemplatesIdGetResponse200Trade
- Schema ID: schema:anon/0e620c9e9f0fde9c200045e654e3ffe421c5d5f5
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `active` | `bool` |
| `updated_at` | `string` |
