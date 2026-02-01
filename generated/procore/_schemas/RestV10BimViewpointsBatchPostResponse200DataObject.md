# RestV10BimViewpointsBatchPostResponse200DataObject

## RestV10BimViewpointsBatchPostResponse200DataObject
- Role: parent
- Schema Name: RestV10BimViewpointsBatchPostResponse200
- Schema ID: schema:anon/c9c085b131adcafb57bf97dc2c893edaf7afdd7e

### Fields

| Field | Type |
|------|------|
| `bim_viewpoints` | `RestV10BimViewpointsBatchPostResponse200BimViewpointsItem[]` |
| `errors` | `RestV10BimViewpointsBatchPostResponse200ErrorsItem[]` |

### Nested Types
- `RestV10BimViewpointsBatchPostResponse200BimViewpointsItem`
- `RestV10BimViewpointsBatchPostResponse200ErrorsItem`
- `RestV10BimViewpointsBatchPostResponse200ErrorsItem_7abdf4Errors`

## RestV10BimViewpointsBatchPostResponse200BimViewpointsItem
- Role: nested
- Parent: RestV10BimViewpointsBatchPostResponse200DataObject
- Schema Name: RestV10BimViewpointsBatchPostResponse200BimViewpointsItem
- Schema ID: schema:anon/1714b690b22180547743f397cc7c73d5f47f0b6d

### Fields

## RestV10BimViewpointsBatchPostResponse200ErrorsItem
- Role: nested
- Parent: RestV10BimViewpointsBatchPostResponse200DataObject
- Schema Name: RestV10BimViewpointsBatchPostResponse200ErrorsItem
- Schema ID: schema:anon/e0c2e22a136abf801137eb488de1745065c3081f

### Fields

| Field | Type |
|------|------|
| `errors` | `RestV10BimViewpointsBatchPostResponse200ErrorsItem_7abdf4Errors` |

## RestV10BimViewpointsBatchPostResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10BimViewpointsBatchPostResponse200DataObject
- Schema Name: RestV10BimViewpointsBatchPostResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
