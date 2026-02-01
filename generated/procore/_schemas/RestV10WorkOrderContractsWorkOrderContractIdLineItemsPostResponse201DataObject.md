# RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201DataObject

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201DataObject
- Role: parent
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201
- Schema ID: schema:anon/b81b1760f91d4e0c5c27b203e99cf6f7a447b996
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `amount` | `string` |
| `company` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201Company` |
| `cost_code` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCode` |
| `created_at` | `string` |
| `description` | `string` |
| `extended_type` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201ExtendedType` |
| `holder` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201Holder` |
| `line_item_type` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeLineItemTypesItem` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `position` | `int` |
| `project` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201Project` |
| `quantity` | `string` |
| `tax_code_id` | `int` |
| `total_amount` | `string` |
| `extended_amount` | `string` |
| `unit_cost` | `string` |
| `uom` | `string` |
| `wbs_code` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201WbsCode` |
| `updated_at` | `string` |
| `change_event_line_item` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201ChangeEventLineItem` |
| `currency_configuration` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201ChangeEventLineItemCurrencyConfiguration` |

### Nested Types
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201ChangeEventLineItem`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201ChangeEventLineItemCostCode`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201ChangeEventLineItemCurrencyConfiguration`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201Company`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCode`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeBillerType`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeLineItemTypesItem`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeLineItemTypesItemBaseType`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeParent`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201ExtendedType`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201Holder`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201Project`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201WbsCode`

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201ChangeEventLineItem
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201ChangeEventLineItem
- Schema ID: schema:anon/f9336236ec4b56bd8b0732e7acfee5769bc733e2
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `cost_rom` | `string` |
| `revenue_rom` | `string` |
| `event_id` | `int` |
| `cost_code` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201ChangeEventLineItemCostCode` |
| `line_item_type` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeLineItemTypesItem` |
| `currency_configuration` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201ChangeEventLineItemCurrencyConfiguration` |

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201ChangeEventLineItemCostCode
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201ChangeEventLineItemCostCode
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
| `biller_type` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeBillerType` |
| `budgeted` | `bool` |
| `code` | `string` |
| `created_at` | `string` |
| `deleted_at` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `parent` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeParent` |
| `position` | `int` |
| `sortable_code` | `string` |
| `standard_cost_code_id` | `int` |
| `standard_cost_code_list_id` | `int` |
| `updated_at` | `string` |
| `line_item_types` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeLineItemTypesItem[]` |

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201ChangeEventLineItemCurrencyConfiguration
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201ChangeEventLineItemCurrencyConfiguration
- Schema ID: schema:anon/f884a729d35e590d8f5a68a341a5a0587ffe2382

### Fields

| Field | Type |
|------|------|
| `currency_iso_code` | `string` |

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201Company
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201Company
- Schema ID: schema:anon/7506dfd51b896d40480f35941478e1635f103a08
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCode
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCode
- Schema ID: schema:anon/88ecc10dd2b540f87216e2652b4007e369dbcea6
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `biller` | `string` |
| `biller_id` | `int` |
| `biller_type` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeBillerType` |
| `budgeted` | `bool` |
| `code` | `string` |
| `created_at` | `string` |
| `deleted_at` | `string` |
| `full_code` | `string` |
| `name` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `parent` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeParent` |
| `position` | `int` |
| `sortable_code` | `string` |
| `standard_cost_code_id` | `int` |
| `standard_cost_code_list_id` | `int` |
| `updated_at` | `string` |
| `line_item_types` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeLineItemTypesItem[]` |

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeBillerType
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeBillerType
- Schema ID: schema:anon/6ce4c07d2fb83b79d4fcb225c5c9c05691bcdc4d

### Enum

Values: Project, SubJob

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeLineItemTypesItem
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeLineItemTypesItem
- Schema ID: schema:anon/b78a87f17b509f5904f1a9e8b840af217e95b3fc
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `code` | `string` |
| `base_type` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeLineItemTypesItemBaseType` |
| `origin_data` | `string` |
| `origin_id` | `string` |

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeLineItemTypesItemBaseType
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeLineItemTypesItemBaseType
- Schema ID: schema:anon/c1a066154239ac3e29e59285e26bd77f996807bf

### Enum

Values: equipment, materials, commitment, owner_cost, professional_services, other

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeParent
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201CostCodeParent
- Schema ID: schema:anon/44768f5b771296b189deec792bd565b414bae19b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201ExtendedType
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201ExtendedType
- Schema ID: schema:anon/0f0412b6cdbbc2bf5f5f0c9441a89be7fecab7b7

### Enum

Values: manual, calculated

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201Holder
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201Holder
- Schema ID: schema:anon/40ac2a57a69f9c0efad2088ff408a8b12fc3a20b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `holder_type` | `string` |

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201Project
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201Project
- Schema ID: schema:anon/a6af6eb0e462865bcb4d406febc45b2f69ca396e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201WbsCode
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsPostResponse201WbsCode
- Schema ID: schema:anon/6d1bf58d026ff2d4fe9fd85909b71472fba16aa4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `flat_code` | `string` |
| `description` | `string` |
