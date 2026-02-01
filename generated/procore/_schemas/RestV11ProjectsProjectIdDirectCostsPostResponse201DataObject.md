# RestV11ProjectsProjectIdDirectCostsPostResponse201DataObject

## RestV11ProjectsProjectIdDirectCostsPostResponse201DataObject
- Role: parent
- Schema Name: RestV11ProjectsProjectIdDirectCostsPostResponse201
- Schema ID: schema:anon/364ab912c83f397c92dcd46d1b0a442218e071b4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `attachments` | `RestV11ProjectsProjectIdDirectCostsPostResponse201AttachmentsItem[]` |
| `attachments_count` | `int` |
| `company` | `RestV11ProjectsProjectIdDirectCostsPostResponse201Company` |
| `created_at` | `string` |
| `deleted_at` | `string` |
| `description` | `string` |
| `direct_cost_type` | `RestV11ProjectsProjectIdDirectCostsPostResponse201DirectCostType` |
| `employee` | `RestV11ProjectsProjectIdDirectCostsPostResponse201Employee` |
| `invoice_number` | `string` |
| `direct_cost_date` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `grand_total` | `string` |
| `line_items_count` | `int` |
| `payment_date` | `string` |
| `project` | `RestV11ProjectsProjectIdDirectCostsPostResponse201Project` |
| `received_date` | `string` |
| `status` | `RestV11ProjectsProjectIdDirectCostsPostResponse201Status` |
| `terms` | `string` |
| `updated_at` | `string` |
| `vendor` | `RestV11ProjectsProjectIdDirectCostsPostResponse201Vendor` |
| `vendor_id` | `int` |
| `vendor_name` | `string` |
| `currency_configuration` | `RestV11ProjectsProjectIdDirectCostsPostResponse201CurrencyConfiguration` |
| `line_items` | `RestV11ProjectsProjectIdDirectCostsPostResponse201LineItemsItem[]` |

### Nested Types
- `Anonymous_88ecc10dBillerType`
- `Anonymous_88ecc10dLineItemTypesItem`
- `Anonymous_88ecc10dLineItemTypesItemBaseType`
- `Anonymous_88ecc10dParent`
- `RestV11ProjectsProjectIdDirectCostsPostResponse201AttachmentsItem`
- `RestV11ProjectsProjectIdDirectCostsPostResponse201Company`
- `RestV11ProjectsProjectIdDirectCostsPostResponse201CurrencyConfiguration`
- `RestV11ProjectsProjectIdDirectCostsPostResponse201DirectCostType`
- `RestV11ProjectsProjectIdDirectCostsPostResponse201Employee`
- `RestV11ProjectsProjectIdDirectCostsPostResponse201LineItemsItem`
- `RestV11ProjectsProjectIdDirectCostsPostResponse201LineItemsItemCostCode`
- `RestV11ProjectsProjectIdDirectCostsPostResponse201LineItemsItemCurrencyConfiguration`
- `RestV11ProjectsProjectIdDirectCostsPostResponse201LineItemsItemExtendedType`
- `RestV11ProjectsProjectIdDirectCostsPostResponse201LineItemsItemWbsCode`
- `RestV11ProjectsProjectIdDirectCostsPostResponse201Project`
- `RestV11ProjectsProjectIdDirectCostsPostResponse201Status`
- `RestV11ProjectsProjectIdDirectCostsPostResponse201Vendor`

## Anonymous_88ecc10dBillerType
- Role: nested
- Parent: RestV11ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: Anonymous_88ecc10dBillerType
- Schema ID: schema:anon/6ce4c07d2fb83b79d4fcb225c5c9c05691bcdc4d

### Enum

Values: Project, SubJob

## Anonymous_88ecc10dLineItemTypesItem
- Role: nested
- Parent: RestV11ProjectsProjectIdDirectCostsPostResponse201DataObject
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
- Parent: RestV11ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: Anonymous_88ecc10dLineItemTypesItemBaseType
- Schema ID: schema:anon/c1a066154239ac3e29e59285e26bd77f996807bf

### Enum

Values: equipment, materials, commitment, owner_cost, professional_services, other

## Anonymous_88ecc10dParent
- Role: nested
- Parent: RestV11ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: Anonymous_88ecc10dParent
- Schema ID: schema:anon/44768f5b771296b189deec792bd565b414bae19b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV11ProjectsProjectIdDirectCostsPostResponse201AttachmentsItem
- Role: nested
- Parent: RestV11ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdDirectCostsPostResponse201AttachmentsItem
- Schema ID: schema:anon/c337dee3df228286468f0ff6d8c4852152f75cf4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |

## RestV11ProjectsProjectIdDirectCostsPostResponse201Company
- Role: nested
- Parent: RestV11ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdDirectCostsPostResponse201Company
- Schema ID: schema:anon/7506dfd51b896d40480f35941478e1635f103a08
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV11ProjectsProjectIdDirectCostsPostResponse201CurrencyConfiguration
- Role: nested
- Parent: RestV11ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdDirectCostsPostResponse201CurrencyConfiguration
- Schema ID: schema:anon/f6ce55d0c5c1f6e8e4601dd4acd240abd5260bef

### Fields

| Field | Type |
|------|------|
| `currency_iso_code` | `string` |
| `currency_exchange_rate` | `string` |
| `base_currency_iso_code` | `string` |

## RestV11ProjectsProjectIdDirectCostsPostResponse201DirectCostType
- Role: nested
- Parent: RestV11ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdDirectCostsPostResponse201DirectCostType
- Schema ID: schema:anon/bb72991481f1872de70f6d554a7751ef3558918e

### Enum

Values: invoice, expense, payroll

## RestV11ProjectsProjectIdDirectCostsPostResponse201Employee
- Role: nested
- Parent: RestV11ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdDirectCostsPostResponse201Employee
- Schema ID: schema:anon/8530528315133d74fc3a99d06b50a136aa519422
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV11ProjectsProjectIdDirectCostsPostResponse201LineItemsItem
- Role: nested
- Parent: RestV11ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdDirectCostsPostResponse201LineItemsItem
- Schema ID: schema:anon/543c525325808eac9669b786baa9763867f23a42
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `amount` | `string` |
| `company` | `RestV11ProjectsProjectIdDirectCostsPostResponse201Company` |
| `cost_code` | `RestV11ProjectsProjectIdDirectCostsPostResponse201LineItemsItemCostCode` |
| `created_at` | `string` |
| `currency_configuration` | `RestV11ProjectsProjectIdDirectCostsPostResponse201LineItemsItemCurrencyConfiguration` |
| `description` | `string` |
| `extended_type` | `RestV11ProjectsProjectIdDirectCostsPostResponse201LineItemsItemExtendedType` |
| `line_item_type` | `Anonymous_88ecc10dLineItemTypesItem` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `position` | `int` |
| `quantity` | `string` |
| `tax_code_id` | `int` |
| `total_amount` | `string` |
| `extended_amount` | `string` |
| `unit_cost` | `string` |
| `uom` | `string` |
| `updated_at` | `string` |
| `wbs_code` | `RestV11ProjectsProjectIdDirectCostsPostResponse201LineItemsItemWbsCode` |
| `ref` | `string` |

## RestV11ProjectsProjectIdDirectCostsPostResponse201LineItemsItemCostCode
- Role: nested
- Parent: RestV11ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdDirectCostsPostResponse201LineItemsItemCostCode
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

## RestV11ProjectsProjectIdDirectCostsPostResponse201LineItemsItemCurrencyConfiguration
- Role: nested
- Parent: RestV11ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdDirectCostsPostResponse201LineItemsItemCurrencyConfiguration
- Schema ID: schema:anon/604508c10ceb4d00db265015715c4f3c345909ea

### Fields

| Field | Type |
|------|------|
| `base_currency_iso_code` | `string` |
| `currency_iso_code` | `string` |

## RestV11ProjectsProjectIdDirectCostsPostResponse201LineItemsItemExtendedType
- Role: nested
- Parent: RestV11ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdDirectCostsPostResponse201LineItemsItemExtendedType
- Schema ID: schema:anon/0f0412b6cdbbc2bf5f5f0c9441a89be7fecab7b7

### Enum

Values: manual, calculated

## RestV11ProjectsProjectIdDirectCostsPostResponse201LineItemsItemWbsCode
- Role: nested
- Parent: RestV11ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdDirectCostsPostResponse201LineItemsItemWbsCode
- Schema ID: schema:anon/6d1bf58d026ff2d4fe9fd85909b71472fba16aa4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `flat_code` | `string` |
| `description` | `string` |

## RestV11ProjectsProjectIdDirectCostsPostResponse201Project
- Role: nested
- Parent: RestV11ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdDirectCostsPostResponse201Project
- Schema ID: schema:anon/a6af6eb0e462865bcb4d406febc45b2f69ca396e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV11ProjectsProjectIdDirectCostsPostResponse201Status
- Role: nested
- Parent: RestV11ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdDirectCostsPostResponse201Status
- Schema ID: schema:anon/8da70385007d7e3ca99257bbe19b9baff2888939

### Enum

Values: draft, pending, revise_and_resubmit, approved

## RestV11ProjectsProjectIdDirectCostsPostResponse201Vendor
- Role: nested
- Parent: RestV11ProjectsProjectIdDirectCostsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdDirectCostsPostResponse201Vendor
- Schema ID: schema:anon/84c244671e471755e3ea5d82534f282f7e17dace
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
