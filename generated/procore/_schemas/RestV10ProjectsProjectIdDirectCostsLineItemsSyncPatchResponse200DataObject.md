# RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200DataObject

## RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200
- Schema ID: schema:anon/0c20f86b812c88f2a57b7cb8ea84952b5c048bf4

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItem[]` |
| `errors` | `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200ErrorsItem[]` |

### Nested Types
- `Anonymous_88ecc10dBillerType`
- `Anonymous_88ecc10dLineItemTypesItem`
- `Anonymous_88ecc10dLineItemTypesItemBaseType`
- `Anonymous_88ecc10dParent`
- `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItem`
- `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItem`
- `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemCompany`
- `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemCostCode`
- `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemCurrencyConfiguration`
- `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemExtendedType`
- `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemHolder`
- `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemProject`
- `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemWbsCode`
- `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200ErrorsItem`
- `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200ErrorsItem_7abdf4Errors`

## Anonymous_88ecc10dBillerType
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200DataObject
- Schema Name: Anonymous_88ecc10dBillerType
- Schema ID: schema:anon/6ce4c07d2fb83b79d4fcb225c5c9c05691bcdc4d

### Enum

Values: Project, SubJob

## Anonymous_88ecc10dLineItemTypesItem
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200DataObject
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
- Parent: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200DataObject
- Schema Name: Anonymous_88ecc10dLineItemTypesItemBaseType
- Schema ID: schema:anon/c1a066154239ac3e29e59285e26bd77f996807bf

### Enum

Values: equipment, materials, commitment, owner_cost, professional_services, other

## Anonymous_88ecc10dParent
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200DataObject
- Schema Name: Anonymous_88ecc10dParent
- Schema ID: schema:anon/44768f5b771296b189deec792bd565b414bae19b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItem
- Schema ID: schema:anon/0b8eefe24f7bde2e62f03ac9e942084c12e592cf
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `amount` | `string` |
| `company` | `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemCompany` |
| `cost_code` | `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemCostCode` |
| `created_at` | `string` |
| `description` | `string` |
| `extended_type` | `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemExtendedType` |
| `holder` | `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemHolder` |
| `line_item_type` | `Anonymous_88ecc10dLineItemTypesItem` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `position` | `int` |
| `project` | `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemProject` |
| `quantity` | `string` |
| `tax_code_id` | `int` |
| `total_amount` | `string` |
| `extended_amount` | `string` |
| `unit_cost` | `string` |
| `uom` | `string` |
| `updated_at` | `string` |
| `change_event_line_item` | `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItem` |
| `wbs_code` | `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemWbsCode` |
| `currency_configuration` | `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemCurrencyConfiguration` |

## RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItem
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemChangeEventLineItem
- Schema ID: schema:anon/f9543f1bbfdf314c862e503b9f869af182ce5035
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `cost_rom` | `string` |
| `revenue_rom` | `string` |
| `event_id` | `int` |
| `cost_code` | `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemCostCode` |
| `line_item_type` | `Anonymous_88ecc10dLineItemTypesItem` |

## RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemCompany
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemCompany
- Schema ID: schema:anon/7506dfd51b896d40480f35941478e1635f103a08
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemCostCode
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemCostCode
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

## RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemCurrencyConfiguration
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemCurrencyConfiguration
- Schema ID: schema:anon/604508c10ceb4d00db265015715c4f3c345909ea

### Fields

| Field | Type |
|------|------|
| `base_currency_iso_code` | `string` |
| `currency_iso_code` | `string` |

## RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemExtendedType
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemExtendedType
- Schema ID: schema:anon/0f0412b6cdbbc2bf5f5f0c9441a89be7fecab7b7

### Enum

Values: manual, calculated

## RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemHolder
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemHolder
- Schema ID: schema:anon/de467b57d6b5f88f05794994bf5dea5a8dcdc207
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `holder_type` | `string` |

## RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemProject
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemProject
- Schema ID: schema:anon/a6af6eb0e462865bcb4d406febc45b2f69ca396e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemWbsCode
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200EntitiesItemWbsCode
- Schema ID: schema:anon/6d1bf58d026ff2d4fe9fd85909b71472fba16aa4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `flat_code` | `string` |
| `description` | `string` |

## RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200ErrorsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200ErrorsItem
- Schema ID: schema:anon/94dc10820e7a8de563c8f217acd6a626f1490097

### Fields

| Field | Type |
|------|------|
| `errors` | `RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200ErrorsItem_7abdf4Errors` |

## RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDirectCostsLineItemsSyncPatchResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
