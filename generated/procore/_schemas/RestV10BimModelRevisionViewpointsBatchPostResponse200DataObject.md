# RestV10BimModelRevisionViewpointsBatchPostResponse200DataObject

## RestV10BimModelRevisionViewpointsBatchPostResponse200DataObject
- Role: parent
- Schema Name: RestV10BimModelRevisionViewpointsBatchPostResponse200
- Schema ID: schema:anon/2c16b6d345e2e8c2431bf943a2d30734ade102ac

### Fields

| Field | Type |
|------|------|
| `bim_model_revision_viewpoints` | `RestV10BimModelRevisionViewpointsBatchPostResponse200BimModelRevisionViewpointsItem[]` |
| `errors` | `RestV10BimModelRevisionViewpointsBatchPostResponse200ErrorsItem[]` |

### Nested Types
- `RestV10BimModelRevisionViewpointsBatchPostResponse200BimModelRevisionViewpointsItem`
- `RestV10BimModelRevisionViewpointsBatchPostResponse200ErrorsItem`
- `RestV10BimModelRevisionViewpointsBatchPostResponse200ErrorsItem_7abdf4Errors`

## RestV10BimModelRevisionViewpointsBatchPostResponse200BimModelRevisionViewpointsItem
- Role: nested
- Parent: RestV10BimModelRevisionViewpointsBatchPostResponse200DataObject
- Schema Name: RestV10BimModelRevisionViewpointsBatchPostResponse200BimModelRevisionViewpointsItem
- Schema ID: schema:anon/fa38dca6ad441b424d03aa01a431894dea328690
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `bim_model_revision_id` | `int` |
| `bim_viewpoint_id` | `int` |
| `primary` | `bool` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV10BimModelRevisionViewpointsBatchPostResponse200ErrorsItem
- Role: nested
- Parent: RestV10BimModelRevisionViewpointsBatchPostResponse200DataObject
- Schema Name: RestV10BimModelRevisionViewpointsBatchPostResponse200ErrorsItem
- Schema ID: schema:anon/69fdbd610400c940a8fe0f4a13a388018e20427c
- Primary Key: BimModelRevisionId

### Fields

| Field | Type |
|------|------|
| `bim_model_revision_id` | `int` |
| `bim_viewpoint_id` | `int` |
| `primary` | `bool` |
| `errors` | `RestV10BimModelRevisionViewpointsBatchPostResponse200ErrorsItem_7abdf4Errors` |

## RestV10BimModelRevisionViewpointsBatchPostResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10BimModelRevisionViewpointsBatchPostResponse200DataObject
- Schema Name: RestV10BimModelRevisionViewpointsBatchPostResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
