# RestV10PrimeContractGetResponse200DataObject

## RestV10PrimeContractGetResponse200DataObject
- Role: parent
- Schema Name: RestV10PrimeContractGetResponse200
- Schema ID: schema:anon/dcc107d69ad60083aa896cc42726b824a0c0ce12
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `accounting_method` | `RestV10PrimeContractGetResponse200AccountingMethod` |
| `actual_completion_date` | `string` |
| `allow_comments` | `bool` |
| `allow_markups` | `bool` |
| `allow_payment_applications` | `bool` |
| `allow_payments` | `bool` |
| `allow_redistributions` | `bool` |
| `approval_letter_date` | `string` |
| `approved_change_orders` | `string` |
| `bill_to` | `string` |
| `budget_line_item_id` | `int` |
| `contract_date` | `string` |
| `contract_estimated_completion_date` | `string` |
| `contract_start_date` | `string` |
| `contract_termination_date` | `string` |
| `created_at` | `string` |
| `deleted_at` | `string` |
| `delivery_date` | `string` |
| `description` | `string` |
| `display_materials_retainage` | `bool` |
| `display_stored_materials` | `bool` |
| `display_work_retainage` | `bool` |
| `draft_change_orders_amount` | `string` |
| `exclusions` | `string` |
| `executed` | `bool` |
| `execution_date` | `string` |
| `grand_total` | `string` |
| `inclusions` | `string` |
| `issued_on_date` | `string` |
| `letter_of_intent_date` | `string` |
| `line_items_extended_total` | `string` |
| `line_items_total` | `string` |
| `number` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `outstanding_balance` | `string` |
| `owner_invoices_amount` | `string` |
| `payment_terms` | `string` |
| `pending_change_orders_amount` | `string` |
| `pending_revised_contract_amount` | `string` |
| `percentage_paid` | `string` |
| `position` | `int` |
| `private` | `bool` |
| `requisition_number` | `string` |
| `retainage_percent` | `string` |
| `returned_date` | `string` |
| `revised_contract_amount` | `string` |
| `ship_to` | `string` |
| `ship_via` | `string` |
| `signed_contract_received_date` | `string` |
| `show_line_items_to_non_admins` | `bool` |
| `status` | `RestV10PrimeContractGetResponse200Status` |
| `title` | `string` |
| `total_payments` | `string` |
| `type` | `string` |
| `updated_at` | `string` |
| `original_substantial_completion_date` | `string` |
| `substantial_completion_date` | `string` |
| `architect` | `RestV10PrimeContractGetResponse200Architect` |
| `assigned_to` | `RestV10PrimeContractGetResponse200Architect` |
| `attachments` | `RestV10PrimeContractGetResponse200AttachmentsItem[]` |
| `change_order_packages` | `RestV10PrimeContractGetResponse200ChangeOrderPackagesItem[]` |
| `change_order_requests` | `Anonymous_6b35da09[][]` |
| `contractor` | `RestV10PrimeContractGetResponse200Contractor` |
| `cost_code` | `RestV10PrimeContractGetResponse200CostCode` |
| `created_by` | `RestV10PrimeContractGetResponse200Architect` |
| `line_items` | `RestV10PrimeContractGetResponse200LineItemsItem[]` |
| `potential_change_orders` | `RestV10PrimeContractGetResponse200PotentialChangeOrdersItem[]` |
| `payments_received` | `RestV10PrimeContractGetResponse200PaymentsReceivedItem[]` |
| `received_from` | `RestV10PrimeContractGetResponse200Architect` |
| `vendor` | `RestV10PrimeContractGetResponse200Contractor` |
| `currency_configuration` | `RestV10PrimeContractGetResponse200ChangeOrderPackagesItemCurrencyConfiguration` |

### Nested Types
- `Anonymous_6b35da09`
- `Anonymous_6b35da09Status`
- `Anonymous_88ecc10dBillerType`
- `Anonymous_88ecc10dLineItemTypesItem`
- `Anonymous_88ecc10dLineItemTypesItemBaseType`
- `Anonymous_88ecc10dParent`
- `RestV10PrimeContractGetResponse200AccountingMethod`
- `RestV10PrimeContractGetResponse200Architect`
- `RestV10PrimeContractGetResponse200AttachmentsItem`
- `RestV10PrimeContractGetResponse200ChangeOrderPackagesItem`
- `RestV10PrimeContractGetResponse200ChangeOrderPackagesItemCurrencyConfiguration`
- `RestV10PrimeContractGetResponse200ChangeOrderPackagesItemStatus`
- `RestV10PrimeContractGetResponse200Contractor`
- `RestV10PrimeContractGetResponse200CostCode`
- `RestV10PrimeContractGetResponse200LineItemsItem`
- `RestV10PrimeContractGetResponse200LineItemsItemChangeEventLineItem`
- `RestV10PrimeContractGetResponse200LineItemsItemCompany`
- `RestV10PrimeContractGetResponse200LineItemsItemExtendedType`
- `RestV10PrimeContractGetResponse200LineItemsItemHolder`
- `RestV10PrimeContractGetResponse200LineItemsItemProject`
- `RestV10PrimeContractGetResponse200LineItemsItemWbsCode`
- `RestV10PrimeContractGetResponse200PaymentsReceivedItem`
- `RestV10PrimeContractGetResponse200PotentialChangeOrdersItem`
- `RestV10PrimeContractGetResponse200PotentialChangeOrdersItemStatus`
- `RestV10PrimeContractGetResponse200Status`

## Anonymous_6b35da09
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: Anonymous_6b35da09
- Schema ID: schema:anon/6b35da097abd92a68ff334352e695ceba1e262f6
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `created_at` | `string` |
| `deleted_at` | `string` |
| `due_date` | `string` |
| `invoiced_date` | `string` |
| `number` | `string` |
| `paid_date` | `string` |
| `status` | `Anonymous_6b35da09Status` |
| `title` | `string` |
| `updated_at` | `string` |
| `currency_configuration` | `RestV10PrimeContractGetResponse200ChangeOrderPackagesItemCurrencyConfiguration` |

## Anonymous_6b35da09Status
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: Anonymous_6b35da09Status
- Schema ID: schema:anon/5b89f75b59f65acdfdc32f08e622b0fbb79dc552

### Enum

Values: draft, not_pricing, pricing, pending, revised, proceeding, not_proceeding, no_charge, approved, rejected, void

## Anonymous_88ecc10dBillerType
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: Anonymous_88ecc10dBillerType
- Schema ID: schema:anon/6ce4c07d2fb83b79d4fcb225c5c9c05691bcdc4d

### Enum

Values: Project, SubJob

## Anonymous_88ecc10dLineItemTypesItem
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
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
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: Anonymous_88ecc10dLineItemTypesItemBaseType
- Schema ID: schema:anon/c1a066154239ac3e29e59285e26bd77f996807bf

### Enum

Values: equipment, materials, commitment, owner_cost, professional_services, other

## Anonymous_88ecc10dParent
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: Anonymous_88ecc10dParent
- Schema ID: schema:anon/44768f5b771296b189deec792bd565b414bae19b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV10PrimeContractGetResponse200AccountingMethod
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: RestV10PrimeContractGetResponse200AccountingMethod
- Schema ID: schema:anon/e1055d906a991a78b8abbae1161941e7d6036bb9

### Enum

Values: amount, unit

## RestV10PrimeContractGetResponse200Architect
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: RestV10PrimeContractGetResponse200Architect
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10PrimeContractGetResponse200AttachmentsItem
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: RestV10PrimeContractGetResponse200AttachmentsItem
- Schema ID: schema:anon/c337dee3df228286468f0ff6d8c4852152f75cf4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |

## RestV10PrimeContractGetResponse200ChangeOrderPackagesItem
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: RestV10PrimeContractGetResponse200ChangeOrderPackagesItem
- Schema ID: schema:anon/e831ab1f6a3e3d06b6cb97aa47baa08991ccf1d8
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `contract_id` | `int` |
| `created_at` | `string` |
| `deleted_at` | `string` |
| `due_date` | `string` |
| `invoiced_date` | `string` |
| `number` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `paid_date` | `string` |
| `reviewed_at` | `string` |
| `title` | `string` |
| `status` | `RestV10PrimeContractGetResponse200ChangeOrderPackagesItemStatus` |
| `updated_at` | `string` |
| `currency_configuration` | `RestV10PrimeContractGetResponse200ChangeOrderPackagesItemCurrencyConfiguration` |

## RestV10PrimeContractGetResponse200ChangeOrderPackagesItemCurrencyConfiguration
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: RestV10PrimeContractGetResponse200ChangeOrderPackagesItemCurrencyConfiguration
- Schema ID: schema:anon/604508c10ceb4d00db265015715c4f3c345909ea

### Fields

| Field | Type |
|------|------|
| `base_currency_iso_code` | `string` |
| `currency_iso_code` | `string` |

## RestV10PrimeContractGetResponse200ChangeOrderPackagesItemStatus
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: RestV10PrimeContractGetResponse200ChangeOrderPackagesItemStatus
- Schema ID: schema:anon/7647971bd104dc6a401bbd43cf5295134c065be9

### Enum

Values: draft, not_pricing, pricing, pending, revised, proceeding, not_proceeding, no_charge, approved, rejected, void

## RestV10PrimeContractGetResponse200Contractor
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: RestV10PrimeContractGetResponse200Contractor
- Schema ID: schema:anon/2b6fa06571868b6fe9370397176acbf74e3356b2
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10PrimeContractGetResponse200CostCode
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: RestV10PrimeContractGetResponse200CostCode
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

## RestV10PrimeContractGetResponse200LineItemsItem
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: RestV10PrimeContractGetResponse200LineItemsItem
- Schema ID: schema:anon/7931e012412b92fba58498b886f10a43fec3ad63
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `amount` | `string` |
| `company` | `RestV10PrimeContractGetResponse200LineItemsItemCompany` |
| `wbs_code` | `RestV10PrimeContractGetResponse200LineItemsItemWbsCode` |
| `cost_code` | `RestV10PrimeContractGetResponse200CostCode` |
| `created_at` | `string` |
| `description` | `string` |
| `extended_type` | `RestV10PrimeContractGetResponse200LineItemsItemExtendedType` |
| `holder` | `RestV10PrimeContractGetResponse200LineItemsItemHolder` |
| `line_item_type` | `Anonymous_88ecc10dLineItemTypesItem` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `position` | `int` |
| `project` | `RestV10PrimeContractGetResponse200LineItemsItemProject` |
| `quantity` | `string` |
| `tax_code_id` | `int` |
| `total_amount` | `string` |
| `extended_amount` | `string` |
| `unit_cost` | `string` |
| `uom` | `string` |
| `updated_at` | `string` |
| `change_event_line_item` | `RestV10PrimeContractGetResponse200LineItemsItemChangeEventLineItem` |
| `currency_configuration` | `RestV10PrimeContractGetResponse200ChangeOrderPackagesItemCurrencyConfiguration` |

## RestV10PrimeContractGetResponse200LineItemsItemChangeEventLineItem
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: RestV10PrimeContractGetResponse200LineItemsItemChangeEventLineItem
- Schema ID: schema:anon/a24aa0a8f1c0d531444ee0edbfe708bf2f5dc432
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `cost_rom` | `string` |
| `revenue_rom` | `string` |
| `event_id` | `int` |
| `cost_code` | `RestV10PrimeContractGetResponse200CostCode` |
| `line_item_type` | `Anonymous_88ecc10dLineItemTypesItem` |
| `currency_configuration` | `RestV10PrimeContractGetResponse200ChangeOrderPackagesItemCurrencyConfiguration` |

## RestV10PrimeContractGetResponse200LineItemsItemCompany
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: RestV10PrimeContractGetResponse200LineItemsItemCompany
- Schema ID: schema:anon/7506dfd51b896d40480f35941478e1635f103a08
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10PrimeContractGetResponse200LineItemsItemExtendedType
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: RestV10PrimeContractGetResponse200LineItemsItemExtendedType
- Schema ID: schema:anon/0f0412b6cdbbc2bf5f5f0c9441a89be7fecab7b7

### Enum

Values: manual, calculated

## RestV10PrimeContractGetResponse200LineItemsItemHolder
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: RestV10PrimeContractGetResponse200LineItemsItemHolder
- Schema ID: schema:anon/40ac2a57a69f9c0efad2088ff408a8b12fc3a20b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `holder_type` | `string` |

## RestV10PrimeContractGetResponse200LineItemsItemProject
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: RestV10PrimeContractGetResponse200LineItemsItemProject
- Schema ID: schema:anon/a6af6eb0e462865bcb4d406febc45b2f69ca396e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10PrimeContractGetResponse200LineItemsItemWbsCode
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: RestV10PrimeContractGetResponse200LineItemsItemWbsCode
- Schema ID: schema:anon/6d1bf58d026ff2d4fe9fd85909b71472fba16aa4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `flat_code` | `string` |
| `description` | `string` |

## RestV10PrimeContractGetResponse200PaymentsReceivedItem
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: RestV10PrimeContractGetResponse200PaymentsReceivedItem
- Schema ID: schema:anon/ca4c4d680ecb5e84ed9530f2421baab8d2fe3a0b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `amount` | `string` |
| `check_number` | `string` |
| `created_at` | `string` |
| `date` | `string` |
| `draw_request_number` | `int` |
| `invoice_number` | `string` |
| `notes` | `string` |
| `payment_number` | `int` |
| `attachments` | `RestV10PrimeContractGetResponse200AttachmentsItem[]` |
| `origin_id` | `string` |
| `origin_data` | `string` |
| `currency_configuration` | `RestV10PrimeContractGetResponse200ChangeOrderPackagesItemCurrencyConfiguration` |

## RestV10PrimeContractGetResponse200PotentialChangeOrdersItem
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: RestV10PrimeContractGetResponse200PotentialChangeOrdersItem
- Schema ID: schema:anon/c2252ffb6a07b8a490b40131380a1e16a54d4de2
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `created_at` | `string` |
| `deleted_at` | `string` |
| `due_date` | `string` |
| `invoiced_date` | `string` |
| `number` | `string` |
| `paid_date` | `string` |
| `reviewed_at` | `string` |
| `title` | `string` |
| `status` | `RestV10PrimeContractGetResponse200PotentialChangeOrdersItemStatus` |
| `updated_at` | `string` |
| `currency_configuration` | `RestV10PrimeContractGetResponse200ChangeOrderPackagesItemCurrencyConfiguration` |

## RestV10PrimeContractGetResponse200PotentialChangeOrdersItemStatus
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: RestV10PrimeContractGetResponse200PotentialChangeOrdersItemStatus
- Schema ID: schema:anon/040325f659a99c24f8ddefcc40f91fff5f803b12

### Enum

Values: draft, not_pricing, pricing, pending, revised, proceeding, not_proceeding, no_charge, approved, rejected, void

## RestV10PrimeContractGetResponse200Status
- Role: nested
- Parent: RestV10PrimeContractGetResponse200DataObject
- Schema Name: RestV10PrimeContractGetResponse200Status
- Schema ID: schema:anon/ba0788b6df2ef6e8e9103fa4eef4613fd890beaa

### Enum

Values: Draft, Out For Bid, Out For Signature, Approved, Complete, Terminated
