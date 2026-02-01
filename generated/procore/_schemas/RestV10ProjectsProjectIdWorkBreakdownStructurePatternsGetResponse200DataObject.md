# RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGetResponse200DataObject

## RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGetResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGetResponse200
- Schema ID: schema:anon/f158b7d3bffe8cab9e443360e133755f353fcd80
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `description` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `is_project_level_ordered` | `bool` |
| `segments` | `RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGetResponse200SegmentsItem[]` |

### Nested Types
- `RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGetResponse200SegmentsItem`
- `RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGetResponse200SegmentsItemStructure`

## RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGetResponse200SegmentsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGetResponse200SegmentsItem
- Schema ID: schema:anon/2904ccee78703c006050ac7c247c2cbb1fde4f1c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `type` | `string` |
| `name` | `string` |
| `position` | `int` |
| `segment_items_count` | `int` |
| `required` | `bool` |
| `delimiter` | `string` |
| `project_can_modify_origin_project` | `bool` |
| `project_can_delete_origin_company` | `bool` |
| `structure` | `RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGetResponse200SegmentsItemStructure` |
| `selectable_tiers` | `bool` |
| `is_included_in_project_pattern` | `bool` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `wbs_pattern_id` | `int` |

## RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGetResponse200SegmentsItemStructure
- Role: nested
- Parent: RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGetResponse200SegmentsItemStructure
- Schema ID: schema:anon/81738cd7ab4ac1046c3763c45b0cfaec62c47d57

### Enum

Values: tiered, flat
