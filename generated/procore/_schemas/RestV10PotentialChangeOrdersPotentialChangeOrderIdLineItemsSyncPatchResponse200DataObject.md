# RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200DataObject

## RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200
- Schema ID: schema:anon/50b94b8d4576fd79f5e66ee0405b92c7ec2af744

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItem[]` |
| `errors` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200ErrorsItem[]` |

### Nested Types
- `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItem`
- `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItem`
- `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItemCostCode`
- `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItemCurrencyConfiguration`
- `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCompany`
- `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCode`
- `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeBillerType`
- `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeLineItemTypesItem`
- `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeLineItemTypesItemBaseType`
- `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeParent`
- `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemExtendedType`
- `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemHolder`
- `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemProject`
- `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemWbsCode`
- `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200ErrorsItem`
- `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200ErrorsItem_7abdf4Errors`

## RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItem
- Schema ID: schema:anon/b81b1760f91d4e0c5c27b203e99cf6f7a447b996
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `amount` | `string` |
| `company` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCompany` |
| `cost_code` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCode` |
| `created_at` | `string` |
| `description` | `string` |
| `extended_type` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemExtendedType` |
| `holder` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemHolder` |
| `line_item_type` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeLineItemTypesItem` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `position` | `int` |
| `project` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemProject` |
| `quantity` | `string` |
| `tax_code_id` | `int` |
| `total_amount` | `string` |
| `extended_amount` | `string` |
| `unit_cost` | `string` |
| `uom` | `string` |
| `wbs_code` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemWbsCode` |
| `updated_at` | `string` |
| `change_event_line_item` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItem` |
| `currency_configuration` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItemCurrencyConfiguration` |

## RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItem
- Role: nested
- Parent: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItem
- Schema ID: schema:anon/f9336236ec4b56bd8b0732e7acfee5769bc733e2
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `cost_rom` | `string` |
| `revenue_rom` | `string` |
| `event_id` | `int` |
| `cost_code` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItemCostCode` |
| `line_item_type` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeLineItemTypesItem` |
| `currency_configuration` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItemCurrencyConfiguration` |

## RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItemCostCode
- Role: nested
- Parent: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItemCostCode
- Schema ID: schema:anon/7b94f1df2e808d88fd5afc25464a20b4905f7763
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `full_code` | `string` |
| `name` | `string` |
| `biller` | `string` |
| `biller_id` | `int` |
| `biller_type` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeBillerType` |
| `budgeted` | `bool` |
| `code` | `string` |
| `created_at` | `string` |
| `deleted_at` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `parent` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeParent` |
| `position` | `int` |
| `sortable_code` | `string` |
| `standard_cost_code_id` | `int` |
| `standard_cost_code_list_id` | `int` |
| `updated_at` | `string` |
| `line_item_types` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeLineItemTypesItem[]` |

## RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItemCurrencyConfiguration
- Role: nested
- Parent: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItemCurrencyConfiguration
- Schema ID: schema:anon/f884a729d35e590d8f5a68a341a5a0587ffe2382

### Fields

| Field | Type |
|------|------|
| `currency_iso_code` | `string` |

## RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCompany
- Role: nested
- Parent: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCompany
- Schema ID: schema:anon/7506dfd51b896d40480f35941478e1635f103a08
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCode
- Role: nested
- Parent: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCode
- Schema ID: schema:anon/88ecc10dd2b540f87216e2652b4007e369dbcea6
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `biller` | `string` |
| `biller_id` | `int` |
| `biller_type` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeBillerType` |
| `budgeted` | `bool` |
| `code` | `string` |
| `created_at` | `string` |
| `deleted_at` | `string` |
| `full_code` | `string` |
| `name` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `parent` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeParent` |
| `position` | `int` |
| `sortable_code` | `string` |
| `standard_cost_code_id` | `int` |
| `standard_cost_code_list_id` | `int` |
| `updated_at` | `string` |
| `line_item_types` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeLineItemTypesItem[]` |

## RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeBillerType
- Role: nested
- Parent: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeBillerType
- Schema ID: schema:anon/6ce4c07d2fb83b79d4fcb225c5c9c05691bcdc4d

### Enum

Values: Project, SubJob

## RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeLineItemTypesItem
- Role: nested
- Parent: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeLineItemTypesItem
- Schema ID: schema:anon/b78a87f17b509f5904f1a9e8b840af217e95b3fc
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `code` | `string` |
| `base_type` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeLineItemTypesItemBaseType` |
| `origin_data` | `string` |
| `origin_id` | `string` |

## RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeLineItemTypesItemBaseType
- Role: nested
- Parent: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeLineItemTypesItemBaseType
- Schema ID: schema:anon/c1a066154239ac3e29e59285e26bd77f996807bf

### Enum

Values: equipment, materials, commitment, owner_cost, professional_services, other

## RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeParent
- Role: nested
- Parent: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemCostCodeParent
- Schema ID: schema:anon/44768f5b771296b189deec792bd565b414bae19b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemExtendedType
- Role: nested
- Parent: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemExtendedType
- Schema ID: schema:anon/0f0412b6cdbbc2bf5f5f0c9441a89be7fecab7b7

### Enum

Values: manual, calculated

## RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemHolder
- Role: nested
- Parent: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemHolder
- Schema ID: schema:anon/40ac2a57a69f9c0efad2088ff408a8b12fc3a20b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `holder_type` | `string` |

## RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemProject
- Role: nested
- Parent: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemProject
- Schema ID: schema:anon/a6af6eb0e462865bcb4d406febc45b2f69ca396e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemWbsCode
- Role: nested
- Parent: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200EntitiesItemWbsCode
- Schema ID: schema:anon/6d1bf58d026ff2d4fe9fd85909b71472fba16aa4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `flat_code` | `string` |
| `description` | `string` |

## RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200ErrorsItem
- Role: nested
- Parent: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200ErrorsItem
- Schema ID: schema:anon/94dc10820e7a8de563c8f217acd6a626f1490097

### Fields

| Field | Type |
|------|------|
| `errors` | `RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200ErrorsItem_7abdf4Errors` |

## RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10PotentialChangeOrdersPotentialChangeOrderIdLineItemsSyncPatchResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
