# RestV10BimPlansBatchPostResponse200DataObject

## RestV10BimPlansBatchPostResponse200DataObject
- Role: parent
- Schema Name: RestV10BimPlansBatchPostResponse200
- Schema ID: schema:anon/3b0febdbe62a67ca7b43fd3d97ef297b615e2e42

### Fields

| Field | Type |
|------|------|
| `bim_plans` | `RestV10BimPlansBatchPostResponse200BimPlansItem[]` |
| `errors` | `RestV10BimPlansBatchPostResponse200ErrorsItem[]` |

### Nested Types
- `RestV10BimPlansBatchPostResponse200BimPlansItem`
- `RestV10BimPlansBatchPostResponse200ErrorsItem`
- `RestV10BimPlansBatchPostResponse200ErrorsItem_7abdf4Errors`

## RestV10BimPlansBatchPostResponse200BimPlansItem
- Role: nested
- Parent: RestV10BimPlansBatchPostResponse200DataObject
- Schema Name: RestV10BimPlansBatchPostResponse200BimPlansItem
- Schema ID: schema:anon/b1657c075aa4e7bb5f4e82d4633261c0cf192654

### Fields

## RestV10BimPlansBatchPostResponse200ErrorsItem
- Role: nested
- Parent: RestV10BimPlansBatchPostResponse200DataObject
- Schema Name: RestV10BimPlansBatchPostResponse200ErrorsItem
- Schema ID: schema:anon/d0b7ead914778134d49421866967b4fda39b4b0f

### Fields

| Field | Type |
|------|------|
| `errors` | `RestV10BimPlansBatchPostResponse200ErrorsItem_7abdf4Errors` |

## RestV10BimPlansBatchPostResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10BimPlansBatchPostResponse200DataObject
- Schema Name: RestV10BimPlansBatchPostResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
