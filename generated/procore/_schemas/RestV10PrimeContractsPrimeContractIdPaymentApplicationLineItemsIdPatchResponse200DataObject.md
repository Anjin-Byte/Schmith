# RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatchResponse200DataObject

## RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatchResponse200
- Schema ID: schema:anon/0c140f18ea31292872353a363fc247a47d09a879
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `balance_to_finish` | `string` |
| `materials_presently_stored` | `string` |
| `scheduled_value` | `string` |
| `total_completed_and_stored_to_date` | `string` |
| `total_completed_and_stored_to_date_percent` | `string` |
| `work_completed_from_previous_application` | `string` |
| `work_completed_this_period` | `string` |
| `description_of_work` | `string` |
| `item_number` | `int` |
| `cost_code` | `RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatchResponse200CostCode` |
| `wbs_code` | `RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatchResponse200WbsCode` |
| `scheduled_unit_price` | `string` |
| `scheduled_quantity` | `string` |
| `total_completed_and_stored_to_date_quantity` | `string` |
| `work_completed_this_period_quantity` | `string` |
| `work_completed_from_previous_application_quantity` | `string` |
| `work_completed_retainage_currently_retained` | `string` |
| `work_completed_retainage_from_previous_application` | `string` |
| `work_completed_retainage_released_this_period` | `string` |
| `work_completed_retainage_retained_this_period` | `string` |
| `work_completed_retainage_percent_this_period` | `string` |
| `materials_stored_retainage_currently_retained` | `string` |
| `materials_stored_retainage_from_previous_application` | `string` |
| `materials_stored_retainage_released_this_period` | `string` |
| `materials_stored_retainage_retained_this_period` | `string` |
| `materials_stored_retainage_percent_this_period` | `string` |
| `total_retainage_currently_retained` | `string` |
| `total_retainage_from_previous_application` | `string` |
| `type` | `string` |

### Nested Types
- `Anonymous_88ecc10dBillerType`
- `Anonymous_88ecc10dLineItemTypesItem`
- `Anonymous_88ecc10dLineItemTypesItemBaseType`
- `Anonymous_88ecc10dParent`
- `RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatchResponse200CostCode`
- `RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatchResponse200WbsCode`

## Anonymous_88ecc10dBillerType
- Role: nested
- Parent: RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatchResponse200DataObject
- Schema Name: Anonymous_88ecc10dBillerType
- Schema ID: schema:anon/6ce4c07d2fb83b79d4fcb225c5c9c05691bcdc4d

### Enum

Values: Project, SubJob

## Anonymous_88ecc10dLineItemTypesItem
- Role: nested
- Parent: RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatchResponse200DataObject
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
- Parent: RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatchResponse200DataObject
- Schema Name: Anonymous_88ecc10dLineItemTypesItemBaseType
- Schema ID: schema:anon/c1a066154239ac3e29e59285e26bd77f996807bf

### Enum

Values: equipment, materials, commitment, owner_cost, professional_services, other

## Anonymous_88ecc10dParent
- Role: nested
- Parent: RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatchResponse200DataObject
- Schema Name: Anonymous_88ecc10dParent
- Schema ID: schema:anon/44768f5b771296b189deec792bd565b414bae19b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatchResponse200CostCode
- Role: nested
- Parent: RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatchResponse200DataObject
- Schema Name: RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatchResponse200CostCode
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

## RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatchResponse200WbsCode
- Role: nested
- Parent: RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatchResponse200DataObject
- Schema Name: RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatchResponse200WbsCode
- Schema ID: schema:anon/0e476e301e89bfd687fa24e17a2f531f70529ffc
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `flat_code` | `string` |
| `description` | `string` |
