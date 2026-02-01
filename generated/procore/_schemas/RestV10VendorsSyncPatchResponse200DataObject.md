# RestV10VendorsSyncPatchResponse200DataObject

## RestV10VendorsSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10VendorsSyncPatchResponse200
- Schema ID: schema:anon/a180a18a80d4f80127808d921fb15b02a492192c

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10VendorsSyncPatchResponse200EntitiesItem[]` |
| `errors` | `RestV10VendorsSyncPatchResponse200ErrorsItem[]` |

### Nested Types
- `RestV10VendorsSyncPatchResponse200EntitiesItem`
- `RestV10VendorsSyncPatchResponse200ErrorsItem`
- `RestV10VendorsSyncPatchResponse200ErrorsItem_7abdf4Errors`

## RestV10VendorsSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10VendorsSyncPatchResponse200DataObject
- Schema Name: RestV10VendorsSyncPatchResponse200EntitiesItem
- Schema ID: schema:anon/69773db6838627a08703ab77cce0b372360b3968

### Fields

## RestV10VendorsSyncPatchResponse200ErrorsItem
- Role: nested
- Parent: RestV10VendorsSyncPatchResponse200DataObject
- Schema Name: RestV10VendorsSyncPatchResponse200ErrorsItem
- Schema ID: schema:anon/e49f0b48f288eebffa752b847ba6d75a11c90508
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `errors` | `RestV10VendorsSyncPatchResponse200ErrorsItem_7abdf4Errors` |

## RestV10VendorsSyncPatchResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10VendorsSyncPatchResponse200DataObject
- Schema Name: RestV10VendorsSyncPatchResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
