# RestV10BimModelRevisionPlansBatchPostResponse200DataObject

## RestV10BimModelRevisionPlansBatchPostResponse200DataObject
- Role: parent
- Schema Name: RestV10BimModelRevisionPlansBatchPostResponse200
- Schema ID: schema:anon/52027fb18a5826e08439e4783ca602acaaebc842

### Fields

| Field | Type |
|------|------|
| `bim_model_revision_plans` | `RestV10BimModelRevisionPlansBatchPostResponse200BimModelRevisionPlansItem[]` |
| `errors` | `RestV10BimModelRevisionPlansBatchPostResponse200ErrorsItem[]` |

### Nested Types
- `RestV10BimModelRevisionPlansBatchPostResponse200BimModelRevisionPlansItem`
- `RestV10BimModelRevisionPlansBatchPostResponse200ErrorsItem`
- `RestV10BimModelRevisionPlansBatchPostResponse200ErrorsItem_7abdf4Errors`

## RestV10BimModelRevisionPlansBatchPostResponse200BimModelRevisionPlansItem
- Role: nested
- Parent: RestV10BimModelRevisionPlansBatchPostResponse200DataObject
- Schema Name: RestV10BimModelRevisionPlansBatchPostResponse200BimModelRevisionPlansItem
- Schema ID: schema:anon/14b0f6dcd7d20af5bfb43774a12274f29ff628b7

### Fields

## RestV10BimModelRevisionPlansBatchPostResponse200ErrorsItem
- Role: nested
- Parent: RestV10BimModelRevisionPlansBatchPostResponse200DataObject
- Schema Name: RestV10BimModelRevisionPlansBatchPostResponse200ErrorsItem
- Schema ID: schema:anon/992ad8c68a42d4ae50cb83c6c5c00f2f6d79a6aa
- Primary Key: BimModelRevisionId

### Fields

| Field | Type |
|------|------|
| `bim_model_revision_id` | `int` |
| `bim_plan_id` | `int` |
| `errors` | `RestV10BimModelRevisionPlansBatchPostResponse200ErrorsItem_7abdf4Errors` |

## RestV10BimModelRevisionPlansBatchPostResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10BimModelRevisionPlansBatchPostResponse200DataObject
- Schema Name: RestV10BimModelRevisionPlansBatchPostResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
