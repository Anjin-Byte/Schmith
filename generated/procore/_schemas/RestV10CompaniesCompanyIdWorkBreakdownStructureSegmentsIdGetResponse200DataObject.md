# RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdGetResponse200DataObject

## RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdGetResponse200DataObject
- Role: parent
- Schema Name: RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdGetResponse200
- Schema ID: schema:anon/9b78705d787b56ca22da2a265b3821e9e74816ae
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
| `structure` | `RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdGetResponse200Structure` |
| `selectable_tiers` | `bool` |
| `is_included_in_project_pattern` | `bool` |
| `tiered` | `bool` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `wbs_pattern_id` | `int` |

### Nested Types
- `RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdGetResponse200Structure`

## RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdGetResponse200Structure
- Role: nested
- Parent: RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdGetResponse200Structure
- Schema ID: schema:anon/81738cd7ab4ac1046c3763c45b0cfaec62c47d57

### Enum

Values: tiered, flat
