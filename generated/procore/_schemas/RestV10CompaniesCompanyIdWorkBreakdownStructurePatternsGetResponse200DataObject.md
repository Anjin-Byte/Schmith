# RestV10CompaniesCompanyIdWorkBreakdownStructurePatternsGetResponse200DataObject

## RestV10CompaniesCompanyIdWorkBreakdownStructurePatternsGetResponse200DataObject
- Role: parent
- Schema Name: RestV10CompaniesCompanyIdWorkBreakdownStructurePatternsGetResponse200
- Schema ID: schema:anon/c9ea0acee092e749e429027f69cfd8814eeb9119
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `description` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `segments` | `RestV10CompaniesCompanyIdWorkBreakdownStructurePatternsGetResponse200SegmentsItem[]` |

### Nested Types
- `RestV10CompaniesCompanyIdWorkBreakdownStructurePatternsGetResponse200SegmentsItem`
- `RestV10CompaniesCompanyIdWorkBreakdownStructurePatternsGetResponse200SegmentsItemStructure`

## RestV10CompaniesCompanyIdWorkBreakdownStructurePatternsGetResponse200SegmentsItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdWorkBreakdownStructurePatternsGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdWorkBreakdownStructurePatternsGetResponse200SegmentsItem
- Schema ID: schema:anon/bd698f62df197908f64cbe5c58bece6f4611a5d9
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
| `structure` | `RestV10CompaniesCompanyIdWorkBreakdownStructurePatternsGetResponse200SegmentsItemStructure` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `wbs_pattern_id` | `int` |

## RestV10CompaniesCompanyIdWorkBreakdownStructurePatternsGetResponse200SegmentsItemStructure
- Role: nested
- Parent: RestV10CompaniesCompanyIdWorkBreakdownStructurePatternsGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdWorkBreakdownStructurePatternsGetResponse200SegmentsItemStructure
- Schema ID: schema:anon/81738cd7ab4ac1046c3763c45b0cfaec62c47d57

### Enum

Values: tiered, flat
