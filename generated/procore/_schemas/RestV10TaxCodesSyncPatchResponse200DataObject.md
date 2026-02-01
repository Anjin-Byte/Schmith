# RestV10TaxCodesSyncPatchResponse200DataObject

## RestV10TaxCodesSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10TaxCodesSyncPatchResponse200
- Schema ID: schema:anon/633f4ff2dbc11d3541d2e5b8f21c7d0c32261cbf

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10TaxCodesSyncPatchResponse200EntitiesItem[]` |
| `errors` | `RestV10TaxCodesSyncPatchResponse200ErrorsItem[]` |

### Nested Types
- `RestV10TaxCodesSyncPatchResponse200EntitiesItem`
- `RestV10TaxCodesSyncPatchResponse200ErrorsItem`
- `RestV10TaxCodesSyncPatchResponse200ErrorsItem_7abdf4Errors`

## RestV10TaxCodesSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10TaxCodesSyncPatchResponse200DataObject
- Schema Name: RestV10TaxCodesSyncPatchResponse200EntitiesItem
- Schema ID: schema:anon/52df9a976fb4b1864577c79124e0283f79ba8c49
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `code` | `string` |
| `description` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `rate1` | `double` |
| `archived` | `bool` |
| `default_tax_code` | `bool` |

## RestV10TaxCodesSyncPatchResponse200ErrorsItem
- Role: nested
- Parent: RestV10TaxCodesSyncPatchResponse200DataObject
- Schema Name: RestV10TaxCodesSyncPatchResponse200ErrorsItem
- Schema ID: schema:anon/21dde99a0be202958c65d82618f375e651007f10
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `code` | `string` |
| `description` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `rate1` | `double` |
| `archived` | `bool` |
| `default_tax_code` | `bool` |
| `errors` | `RestV10TaxCodesSyncPatchResponse200ErrorsItem_7abdf4Errors` |

## RestV10TaxCodesSyncPatchResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10TaxCodesSyncPatchResponse200DataObject
- Schema Name: RestV10TaxCodesSyncPatchResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
