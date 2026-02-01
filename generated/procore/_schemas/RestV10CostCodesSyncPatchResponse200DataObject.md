# RestV10CostCodesSyncPatchResponse200DataObject

## RestV10CostCodesSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10CostCodesSyncPatchResponse200
- Schema ID: schema:anon/f00c5bb8e7cf334214a01468391b3b6d4b01aabb

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10CostCodesSyncPatchResponse200EntitiesItem[]` |
| `errors` | `RestV10CostCodesSyncPatchResponse200ErrorsItem[]` |

### Nested Types
- `Anonymous_88ecc10dBillerType`
- `Anonymous_88ecc10dLineItemTypesItem`
- `Anonymous_88ecc10dLineItemTypesItemBaseType`
- `Anonymous_88ecc10dParent`
- `RestV10CostCodesSyncPatchResponse200EntitiesItem`
- `RestV10CostCodesSyncPatchResponse200ErrorsItem`
- `RestV10CostCodesSyncPatchResponse200ErrorsItem_7abdf4Errors`

## Anonymous_88ecc10dBillerType
- Role: nested
- Parent: RestV10CostCodesSyncPatchResponse200DataObject
- Schema Name: Anonymous_88ecc10dBillerType
- Schema ID: schema:anon/6ce4c07d2fb83b79d4fcb225c5c9c05691bcdc4d

### Enum

Values: Project, SubJob

## Anonymous_88ecc10dLineItemTypesItem
- Role: nested
- Parent: RestV10CostCodesSyncPatchResponse200DataObject
- Schema Name: Anonymous_88ecc10dLineItemTypesItem
- Schema ID: schema:anon/b78a87f17b509f5904f1a9e8b840af217e95b3fc
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `code` | `string` |
| `base_type` | `Anonymous_88ecc10dLineItemTypesItemBaseType` |
| `origin_data` | `string` |
| `origin_id` | `string` |

## Anonymous_88ecc10dLineItemTypesItemBaseType
- Role: nested
- Parent: RestV10CostCodesSyncPatchResponse200DataObject
- Schema Name: Anonymous_88ecc10dLineItemTypesItemBaseType
- Schema ID: schema:anon/c1a066154239ac3e29e59285e26bd77f996807bf

### Enum

Values: equipment, materials, commitment, owner_cost, professional_services, other

## Anonymous_88ecc10dParent
- Role: nested
- Parent: RestV10CostCodesSyncPatchResponse200DataObject
- Schema Name: Anonymous_88ecc10dParent
- Schema ID: schema:anon/44768f5b771296b189deec792bd565b414bae19b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV10CostCodesSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10CostCodesSyncPatchResponse200DataObject
- Schema Name: RestV10CostCodesSyncPatchResponse200EntitiesItem
- Schema ID: schema:anon/0206b2ed9969f712f046725bad7cccce1c5e6790

### Fields

## RestV10CostCodesSyncPatchResponse200ErrorsItem
- Role: nested
- Parent: RestV10CostCodesSyncPatchResponse200DataObject
- Schema Name: RestV10CostCodesSyncPatchResponse200ErrorsItem
- Schema ID: schema:anon/a13ef1dca014a8482ab03d0601c4a2f1e17bcca4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `full_code` | `string` |
| `name` | `string` |
| `biller` | `string` |
| `biller_id` | `int` |
| `biller_type` | `Anonymous_88ecc10dBillerType` |
| `budgeted` | `bool` |
| `code` | `string` |
| `created_at` | `string` |
| `deleted_at` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `parent` | `Anonymous_88ecc10dParent` |
| `position` | `int` |
| `sortable_code` | `string` |
| `standard_cost_code_id` | `int` |
| `standard_cost_code_list_id` | `int` |
| `updated_at` | `string` |
| `line_item_types` | `Anonymous_88ecc10dLineItemTypesItem[]` |
| `errors` | `RestV10CostCodesSyncPatchResponse200ErrorsItem_7abdf4Errors` |

## RestV10CostCodesSyncPatchResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10CostCodesSyncPatchResponse200DataObject
- Schema Name: RestV10CostCodesSyncPatchResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
