# RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200DataObject

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200
- Schema ID: schema:anon/15bf7a90238785aa2e22dd76a44b380ca175e5a6

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItem[]` |
| `errors` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200ErrorsItem[]` |

### Nested Types
- `Anonymous_88ecc10dBillerType`
- `Anonymous_88ecc10dLineItemTypesItem`
- `Anonymous_88ecc10dLineItemTypesItemBaseType`
- `Anonymous_88ecc10dParent`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItem`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItem`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemCompany`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemCostCode`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemCurrencyConfiguration`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemExtendedType`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemHolder`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemProject`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemWbsCode`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200ErrorsItem`
- `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200ErrorsItem_7abdf4Errors`

## Anonymous_88ecc10dBillerType
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200DataObject
- Schema Name: Anonymous_88ecc10dBillerType
- Schema ID: schema:anon/6ce4c07d2fb83b79d4fcb225c5c9c05691bcdc4d

### Enum

Values: Project, SubJob

## Anonymous_88ecc10dLineItemTypesItem
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200DataObject
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
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200DataObject
- Schema Name: Anonymous_88ecc10dLineItemTypesItemBaseType
- Schema ID: schema:anon/c1a066154239ac3e29e59285e26bd77f996807bf

### Enum

Values: equipment, materials, commitment, owner_cost, professional_services, other

## Anonymous_88ecc10dParent
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200DataObject
- Schema Name: Anonymous_88ecc10dParent
- Schema ID: schema:anon/44768f5b771296b189deec792bd565b414bae19b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItem
- Schema ID: schema:anon/c3c12698390c3df03d1570b109c98a4033eae6e6
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `amount` | `string` |
| `company` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemCompany` |
| `cost_code` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemCostCode` |
| `created_at` | `string` |
| `description` | `string` |
| `extended_type` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemExtendedType` |
| `holder` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemHolder` |
| `line_item_type` | `Anonymous_88ecc10dLineItemTypesItem` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `position` | `int` |
| `project` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemProject` |
| `quantity` | `string` |
| `tax_code_id` | `int` |
| `total_amount` | `string` |
| `extended_amount` | `string` |
| `unit_cost` | `string` |
| `uom` | `string` |
| `updated_at` | `string` |
| `wbs_code` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemWbsCode` |
| `change_event_line_item` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItem` |
| `currency_configuration` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemCurrencyConfiguration` |

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItem
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItem
- Schema ID: schema:anon/f9543f1bbfdf314c862e503b9f869af182ce5035
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `cost_rom` | `string` |
| `revenue_rom` | `string` |
| `event_id` | `int` |
| `cost_code` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemCostCode` |
| `line_item_type` | `Anonymous_88ecc10dLineItemTypesItem` |

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemCompany
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemCompany
- Schema ID: schema:anon/7506dfd51b896d40480f35941478e1635f103a08
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemCostCode
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemCostCode
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

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemCurrencyConfiguration
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemCurrencyConfiguration
- Schema ID: schema:anon/f884a729d35e590d8f5a68a341a5a0587ffe2382

### Fields

| Field | Type |
|------|------|
| `currency_iso_code` | `string` |

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemExtendedType
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemExtendedType
- Schema ID: schema:anon/0f0412b6cdbbc2bf5f5f0c9441a89be7fecab7b7

### Enum

Values: manual, calculated

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemHolder
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemHolder
- Schema ID: schema:anon/40ac2a57a69f9c0efad2088ff408a8b12fc3a20b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `holder_type` | `string` |

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemProject
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemProject
- Schema ID: schema:anon/a6af6eb0e462865bcb4d406febc45b2f69ca396e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemWbsCode
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemWbsCode
- Schema ID: schema:anon/6d1bf58d026ff2d4fe9fd85909b71472fba16aa4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `flat_code` | `string` |
| `description` | `string` |

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200ErrorsItem
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200ErrorsItem
- Schema ID: schema:anon/4ee8c8ac5bf7f787715d3df53840414a27c96cc8
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `amount` | `string` |
| `company` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemCompany` |
| `cost_code` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemCostCode` |
| `created_at` | `string` |
| `description` | `string` |
| `extended_type` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemExtendedType` |
| `holder` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemHolder` |
| `line_item_type` | `Anonymous_88ecc10dLineItemTypesItem` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `position` | `int` |
| `project` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemProject` |
| `quantity` | `string` |
| `tax_code_id` | `int` |
| `total_amount` | `string` |
| `extended_amount` | `string` |
| `unit_cost` | `string` |
| `uom` | `string` |
| `updated_at` | `string` |
| `change_event_line_item` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItem` |
| `errors` | `RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200ErrorsItem_7abdf4Errors` |

## RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatchResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
