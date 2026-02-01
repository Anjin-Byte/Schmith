# RestV10TaxTypesSyncPatchResponse200DataObject

## RestV10TaxTypesSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10TaxTypesSyncPatchResponse200
- Schema ID: schema:anon/56d6287937ad0ac46bc1fdfca135da22041b3eea

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10TaxTypesSyncPatchResponse200EntitiesItem[]` |
| `errors` | `RestV10TaxTypesSyncPatchResponse200ErrorsItem[]` |

### Nested Types
- `RestV10TaxTypesSyncPatchResponse200EntitiesItem`
- `RestV10TaxTypesSyncPatchResponse200ErrorsItem`
- `RestV10TaxTypesSyncPatchResponse200ErrorsItem_7abdf4Errors`

## RestV10TaxTypesSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10TaxTypesSyncPatchResponse200DataObject
- Schema Name: RestV10TaxTypesSyncPatchResponse200EntitiesItem
- Schema ID: schema:anon/5ecc691a2178101cc0a1a894ff98bcb29880441d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `description` | `string` |
| `name` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |

## RestV10TaxTypesSyncPatchResponse200ErrorsItem
- Role: nested
- Parent: RestV10TaxTypesSyncPatchResponse200DataObject
- Schema Name: RestV10TaxTypesSyncPatchResponse200ErrorsItem
- Schema ID: schema:anon/ba48ac205d9d73bfa66d3163343e3f419e59b358
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `description` | `string` |
| `name` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `errors` | `RestV10TaxTypesSyncPatchResponse200ErrorsItem_7abdf4Errors` |

## RestV10TaxTypesSyncPatchResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10TaxTypesSyncPatchResponse200DataObject
- Schema Name: RestV10TaxTypesSyncPatchResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
