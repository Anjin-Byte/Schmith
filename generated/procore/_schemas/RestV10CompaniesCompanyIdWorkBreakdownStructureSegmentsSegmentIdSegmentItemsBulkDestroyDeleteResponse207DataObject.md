# RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDeleteResponse207DataObject

## RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDeleteResponse207DataObject
- Role: parent
- Schema Name: RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDeleteResponse207
- Schema ID: schema:anon/deefe9f6b46587e7aea72814560325c3949a7757

### Fields

| Field | Type |
|------|------|
| `successes` | `int[]` |
| `failures` | `RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDeleteResponse207FailuresItem[]` |

### Nested Types
- `RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDeleteResponse207FailuresItem`

## RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDeleteResponse207FailuresItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDeleteResponse207DataObject
- Schema Name: RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDeleteResponse207FailuresItem
- Schema ID: schema:anon/3fa8fa92a12f9b362eec5f3e74c1b575988eb4b8
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `error` | `string` |
