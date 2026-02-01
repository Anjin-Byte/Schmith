# RestV10CompaniesCompanyIdUomsSyncPatchResponse200DataObject

## RestV10CompaniesCompanyIdUomsSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10CompaniesCompanyIdUomsSyncPatchResponse200
- Schema ID: schema:anon/84e8687d654e3cf39d2496960b475f8ee93d2c2c

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10CompaniesCompanyIdUomsSyncPatchResponse200EntitiesItem[]` |
| `errors` | `RestV10CompaniesCompanyIdUomsSyncPatchResponse200ErrorsItem[]` |

### Nested Types
- `RestV10CompaniesCompanyIdUomsSyncPatchResponse200EntitiesItem`
- `RestV10CompaniesCompanyIdUomsSyncPatchResponse200EntitiesItemUomCategory`
- `RestV10CompaniesCompanyIdUomsSyncPatchResponse200ErrorsItem`
- `RestV10CompaniesCompanyIdUomsSyncPatchResponse200ErrorsItem_7abdf4Errors`

## RestV10CompaniesCompanyIdUomsSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdUomsSyncPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdUomsSyncPatchResponse200EntitiesItem
- Schema ID: schema:anon/24a5b0134c59b3f7bfe25f14126442fcf3bc58ec
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `is_standard` | `bool` |
| `name` | `string` |
| `description` | `string` |
| `uom_category` | `RestV10CompaniesCompanyIdUomsSyncPatchResponse200EntitiesItemUomCategory` |

## RestV10CompaniesCompanyIdUomsSyncPatchResponse200EntitiesItemUomCategory
- Role: nested
- Parent: RestV10CompaniesCompanyIdUomsSyncPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdUomsSyncPatchResponse200EntitiesItemUomCategory
- Schema ID: schema:anon/d167ca1ef39c3f402181d129853584c4a6ebb87d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10CompaniesCompanyIdUomsSyncPatchResponse200ErrorsItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdUomsSyncPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdUomsSyncPatchResponse200ErrorsItem
- Schema ID: schema:anon/73f52fc730647af16140d0da8da9adbd62a2dc84
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `is_standard` | `bool` |
| `name` | `string` |
| `description` | `string` |
| `uom_category` | `RestV10CompaniesCompanyIdUomsSyncPatchResponse200EntitiesItemUomCategory` |
| `errors` | `RestV10CompaniesCompanyIdUomsSyncPatchResponse200ErrorsItem_7abdf4Errors` |

## RestV10CompaniesCompanyIdUomsSyncPatchResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10CompaniesCompanyIdUomsSyncPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdUomsSyncPatchResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
