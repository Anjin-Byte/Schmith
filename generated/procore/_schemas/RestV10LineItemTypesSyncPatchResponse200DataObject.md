# RestV10LineItemTypesSyncPatchResponse200DataObject

## RestV10LineItemTypesSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10LineItemTypesSyncPatchResponse200
- Schema ID: schema:anon/2f00aeb364cd17b4181ce4228e23fa97bf006b54

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10LineItemTypesSyncPatchResponse200EntitiesItem[]` |
| `errors` | `object[]` |

### Nested Types
- `RestV10LineItemTypesSyncPatchResponse200EntitiesItem`
- `RestV10LineItemTypesSyncPatchResponse200EntitiesItemBaseType`

## RestV10LineItemTypesSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10LineItemTypesSyncPatchResponse200DataObject
- Schema Name: RestV10LineItemTypesSyncPatchResponse200EntitiesItem
- Schema ID: schema:anon/2b16f1d37a6e318fa008e57062a3b593fa0a7f51
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `code` | `string` |
| `base_type` | `RestV10LineItemTypesSyncPatchResponse200EntitiesItemBaseType` |
| `origin_data` | `string` |
| `origin_id` | `string` |

## RestV10LineItemTypesSyncPatchResponse200EntitiesItemBaseType
- Role: nested
- Parent: RestV10LineItemTypesSyncPatchResponse200DataObject
- Schema Name: RestV10LineItemTypesSyncPatchResponse200EntitiesItemBaseType
- Schema ID: schema:anon/c1a066154239ac3e29e59285e26bd77f996807bf

### Enum

Values: equipment, materials, commitment, owner_cost, professional_services, other
