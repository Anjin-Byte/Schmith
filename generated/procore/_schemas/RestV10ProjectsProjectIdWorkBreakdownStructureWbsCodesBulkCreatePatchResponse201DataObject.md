# RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201DataObject

## RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201
- Schema ID: schema:anon/2ff3f64e390cecb4f1b172b33e08dd6ffc5062ba

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201EntitiesItem[]` |
| `errors` | `object[]` |

### Nested Types
- `RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201EntitiesItem`
- `RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201EntitiesItemSegmentItemsItem`
- `RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201EntitiesItemSegmentItemsItemSegment`
- `RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201EntitiesItemSegmentItemsItemSegmentStructure`

## RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201EntitiesItem
- Role: nested
- Parent: RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201EntitiesItem
- Schema ID: schema:anon/236e884b00ef1902e4c9ff53f80270a4e7ab0395
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `flat_code` | `string` |
| `flat_name` | `string` |
| `description` | `string` |
| `status` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `segment_items` | `RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201EntitiesItemSegmentItemsItem[]` |
| `wbs_pattern_id` | `int` |

## RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201EntitiesItemSegmentItemsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201EntitiesItemSegmentItemsItem
- Schema ID: schema:anon/89d016886228f63fa0772725792f97691ac29a03
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `code` | `string` |
| `name` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `parent_id` | `int` |
| `path_ids` | `int[]` |
| `path_code` | `string` |
| `is_parent` | `bool` |
| `path_codes` | `string[]` |
| `path_names` | `string[]` |
| `in_use` | `bool` |
| `segment` | `RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201EntitiesItemSegmentItemsItemSegment` |
| `status` | `string` |

## RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201EntitiesItemSegmentItemsItemSegment
- Role: nested
- Parent: RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201EntitiesItemSegmentItemsItemSegment
- Schema ID: schema:anon/68b6bfdf75240af7235639d0a029bb129381733f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `type` | `string` |
| `position` | `int` |
| `delimiter` | `string` |
| `required` | `bool` |
| `segment_items_count` | `int` |
| `project_can_modify_origin_project` | `bool` |
| `project_can_delete_origin_company` | `bool` |
| `structure` | `RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201EntitiesItemSegmentItemsItemSegmentStructure` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `wbs_pattern_id` | `int` |

## RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201EntitiesItemSegmentItemsItemSegmentStructure
- Role: nested
- Parent: RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatchResponse201EntitiesItemSegmentItemsItemSegmentStructure
- Schema ID: schema:anon/3b31c829ab7b03472fa73a63a427f7fb0a027310

### Enum

Values: tiered, flat
