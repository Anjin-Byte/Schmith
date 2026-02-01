# RestV10WorkOrderContractsPostResponse201DataObject

## RestV10WorkOrderContractsPostResponse201DataObject
- Role: parent
- Schema Name: RestV10WorkOrderContractsPostResponse201
- Schema ID: schema:anon/90548db77b32a30de2dc2b8500e94612673bec29
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `accounting_method` | `RestV10WorkOrderContractsPostResponse201AccountingMethod` |
| `actual_completion_date` | `string` |
| `approval_letter_date` | `string` |
| `approved_change_orders` | `string` |
| `attachments` | `RestV10WorkOrderContractsPostResponse201AttachmentsItem[]` |
| `change_order_packages` | `RestV10WorkOrderContractsPostResponse201ChangeOrderPackagesItem[]` |
| `change_order_requests` | `Anonymous_6b35da09[][]` |
| `contract_date` | `string` |
| `contract_start_date` | `string` |
| `contract_estimated_completion_date` | `string` |
| `created_at` | `string` |
| `created_by_id` | `int` |
| `deleted_at` | `string` |
| `description` | `string` |
| `draft_change_orders_amount` | `string` |
| `exclusions` | `string` |
| `executed` | `bool` |
| `execution_date` | `string` |
| `grand_total` | `string` |
| `id` | `int` |
| `inclusions` | `string` |
| `invoice_contacts` | `RestV10WorkOrderContractsPostResponse201InvoiceContactsItem[]` |
| `issued_on_date` | `string` |
| `letter_of_intent_date` | `string` |
| `line_items` | `RestV10WorkOrderContractsPostResponse201LineItemsItem[]` |
| `number` | `string` |
| `origin_data` | `string` |
| `origin_code` | `string` |
| `origin_id` | `string` |
| `payments_issued` | `RestV10WorkOrderContractsPostResponse201PaymentsIssuedItem[]` |
| `pending_change_orders` | `string` |
| `pending_revised_contract` | `string` |
| `percentage_paid` | `string` |
| `potential_change_orders` | `RestV10WorkOrderContractsPostResponse201PotentialChangeOrdersItem[]` |
| `private` | `bool` |
| `project` | `RestV10WorkOrderContractsPostResponse201LineItemsItemProject` |
| `remaining_balance_outstanding` | `string` |
| `requisitions_are_enabled` | `bool` |
| `retainage_percent` | `string` |
| `returned_date` | `string` |
| `revised_contract` | `string` |
| `signed_contract_received_date` | `string` |
| `show_line_items_to_non_admins` | `bool` |
| `status` | `RestV10WorkOrderContractsPostResponse201Status` |
| `title` | `string` |
| `total_draw_requests_amount` | `string` |
| `total_payments` | `string` |
| `total_requisitions_amount` | `string` |
| `updated_at` | `string` |
| `vendor` | `RestV10WorkOrderContractsPostResponse201Vendor` |
| `currency_configuration` | `RestV10WorkOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration` |

### Nested Types
- `Anonymous_6b35da09`
- `Anonymous_6b35da09Status`
- `Anonymous_88ecc10dBillerType`
- `Anonymous_88ecc10dLineItemTypesItem`
- `Anonymous_88ecc10dLineItemTypesItemBaseType`
- `Anonymous_88ecc10dParent`
- `RestV10WorkOrderContractsPostResponse201AccountingMethod`
- `RestV10WorkOrderContractsPostResponse201AttachmentsItem`
- `RestV10WorkOrderContractsPostResponse201ChangeOrderPackagesItem`
- `RestV10WorkOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration`
- `RestV10WorkOrderContractsPostResponse201ChangeOrderPackagesItemStatus`
- `RestV10WorkOrderContractsPostResponse201InvoiceContactsItem`
- `RestV10WorkOrderContractsPostResponse201LineItemsItem`
- `RestV10WorkOrderContractsPostResponse201LineItemsItemChangeEventLineItem`
- `RestV10WorkOrderContractsPostResponse201LineItemsItemCompany`
- `RestV10WorkOrderContractsPostResponse201LineItemsItemCostCode`
- `RestV10WorkOrderContractsPostResponse201LineItemsItemExtendedType`
- `RestV10WorkOrderContractsPostResponse201LineItemsItemHolder`
- `RestV10WorkOrderContractsPostResponse201LineItemsItemProject`
- `RestV10WorkOrderContractsPostResponse201LineItemsItemWbsCode`
- `RestV10WorkOrderContractsPostResponse201PaymentsIssuedItem`
- `RestV10WorkOrderContractsPostResponse201PotentialChangeOrdersItem`
- `RestV10WorkOrderContractsPostResponse201PotentialChangeOrdersItemStatus`
- `RestV10WorkOrderContractsPostResponse201Status`
- `RestV10WorkOrderContractsPostResponse201Vendor`

## Anonymous_6b35da09
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
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
| `currency_configuration` | `RestV10WorkOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration` |

## Anonymous_6b35da09Status
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: Anonymous_6b35da09Status
- Schema ID: schema:anon/5b89f75b59f65acdfdc32f08e622b0fbb79dc552

### Enum

Values: draft, not_pricing, pricing, pending, revised, proceeding, not_proceeding, no_charge, approved, rejected, void

## Anonymous_88ecc10dBillerType
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: Anonymous_88ecc10dBillerType
- Schema ID: schema:anon/6ce4c07d2fb83b79d4fcb225c5c9c05691bcdc4d

### Enum

Values: Project, SubJob

## Anonymous_88ecc10dLineItemTypesItem
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
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
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: Anonymous_88ecc10dLineItemTypesItemBaseType
- Schema ID: schema:anon/c1a066154239ac3e29e59285e26bd77f996807bf

### Enum

Values: equipment, materials, commitment, owner_cost, professional_services, other

## Anonymous_88ecc10dParent
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: Anonymous_88ecc10dParent
- Schema ID: schema:anon/44768f5b771296b189deec792bd565b414bae19b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV10WorkOrderContractsPostResponse201AccountingMethod
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsPostResponse201AccountingMethod
- Schema ID: schema:anon/e1055d906a991a78b8abbae1161941e7d6036bb9

### Enum

Values: amount, unit

## RestV10WorkOrderContractsPostResponse201AttachmentsItem
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsPostResponse201AttachmentsItem
- Schema ID: schema:anon/c337dee3df228286468f0ff6d8c4852152f75cf4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |

## RestV10WorkOrderContractsPostResponse201ChangeOrderPackagesItem
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsPostResponse201ChangeOrderPackagesItem
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
| `status` | `RestV10WorkOrderContractsPostResponse201ChangeOrderPackagesItemStatus` |
| `updated_at` | `string` |
| `currency_configuration` | `RestV10WorkOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration` |

## RestV10WorkOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration
- Schema ID: schema:anon/604508c10ceb4d00db265015715c4f3c345909ea

### Fields

| Field | Type |
|------|------|
| `base_currency_iso_code` | `string` |
| `currency_iso_code` | `string` |

## RestV10WorkOrderContractsPostResponse201ChangeOrderPackagesItemStatus
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsPostResponse201ChangeOrderPackagesItemStatus
- Schema ID: schema:anon/7647971bd104dc6a401bbd43cf5295134c065be9

### Enum

Values: draft, not_pricing, pricing, pending, revised, proceeding, not_proceeding, no_charge, approved, rejected, void

## RestV10WorkOrderContractsPostResponse201InvoiceContactsItem
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsPostResponse201InvoiceContactsItem
- Schema ID: schema:anon/7b2510e11ea2164ebb34127057ba3860dd829287
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `business_phone` | `string` |
| `business_phone_extension` | `int` |
| `email` | `string` |
| `fax_number` | `string` |
| `job_title` | `string` |
| `login_information_id` | `int` |
| `mobile_phone` | `string` |
| `name` | `string` |
| `vendor_name` | `string` |
| `currency_configuration` | `RestV10WorkOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration` |

## RestV10WorkOrderContractsPostResponse201LineItemsItem
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsPostResponse201LineItemsItem
- Schema ID: schema:anon/7931e012412b92fba58498b886f10a43fec3ad63
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `amount` | `string` |
| `company` | `RestV10WorkOrderContractsPostResponse201LineItemsItemCompany` |
| `wbs_code` | `RestV10WorkOrderContractsPostResponse201LineItemsItemWbsCode` |
| `cost_code` | `RestV10WorkOrderContractsPostResponse201LineItemsItemCostCode` |
| `created_at` | `string` |
| `description` | `string` |
| `extended_type` | `RestV10WorkOrderContractsPostResponse201LineItemsItemExtendedType` |
| `holder` | `RestV10WorkOrderContractsPostResponse201LineItemsItemHolder` |
| `line_item_type` | `Anonymous_88ecc10dLineItemTypesItem` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `position` | `int` |
| `project` | `RestV10WorkOrderContractsPostResponse201LineItemsItemProject` |
| `quantity` | `string` |
| `tax_code_id` | `int` |
| `total_amount` | `string` |
| `extended_amount` | `string` |
| `unit_cost` | `string` |
| `uom` | `string` |
| `updated_at` | `string` |
| `change_event_line_item` | `RestV10WorkOrderContractsPostResponse201LineItemsItemChangeEventLineItem` |
| `currency_configuration` | `RestV10WorkOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration` |

## RestV10WorkOrderContractsPostResponse201LineItemsItemChangeEventLineItem
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsPostResponse201LineItemsItemChangeEventLineItem
- Schema ID: schema:anon/a24aa0a8f1c0d531444ee0edbfe708bf2f5dc432
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `cost_rom` | `string` |
| `revenue_rom` | `string` |
| `event_id` | `int` |
| `cost_code` | `RestV10WorkOrderContractsPostResponse201LineItemsItemCostCode` |
| `line_item_type` | `Anonymous_88ecc10dLineItemTypesItem` |
| `currency_configuration` | `RestV10WorkOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration` |

## RestV10WorkOrderContractsPostResponse201LineItemsItemCompany
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsPostResponse201LineItemsItemCompany
- Schema ID: schema:anon/7506dfd51b896d40480f35941478e1635f103a08
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10WorkOrderContractsPostResponse201LineItemsItemCostCode
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsPostResponse201LineItemsItemCostCode
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

## RestV10WorkOrderContractsPostResponse201LineItemsItemExtendedType
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsPostResponse201LineItemsItemExtendedType
- Schema ID: schema:anon/0f0412b6cdbbc2bf5f5f0c9441a89be7fecab7b7

### Enum

Values: manual, calculated

## RestV10WorkOrderContractsPostResponse201LineItemsItemHolder
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsPostResponse201LineItemsItemHolder
- Schema ID: schema:anon/40ac2a57a69f9c0efad2088ff408a8b12fc3a20b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `holder_type` | `string` |

## RestV10WorkOrderContractsPostResponse201LineItemsItemProject
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsPostResponse201LineItemsItemProject
- Schema ID: schema:anon/a6af6eb0e462865bcb4d406febc45b2f69ca396e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10WorkOrderContractsPostResponse201LineItemsItemWbsCode
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsPostResponse201LineItemsItemWbsCode
- Schema ID: schema:anon/6d1bf58d026ff2d4fe9fd85909b71472fba16aa4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `flat_code` | `string` |
| `description` | `string` |

## RestV10WorkOrderContractsPostResponse201PaymentsIssuedItem
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsPostResponse201PaymentsIssuedItem
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
| `attachments` | `RestV10WorkOrderContractsPostResponse201AttachmentsItem[]` |
| `origin_id` | `string` |
| `origin_data` | `string` |
| `currency_configuration` | `RestV10WorkOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration` |

## RestV10WorkOrderContractsPostResponse201PotentialChangeOrdersItem
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsPostResponse201PotentialChangeOrdersItem
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
| `status` | `RestV10WorkOrderContractsPostResponse201PotentialChangeOrdersItemStatus` |
| `updated_at` | `string` |
| `currency_configuration` | `RestV10WorkOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration` |

## RestV10WorkOrderContractsPostResponse201PotentialChangeOrdersItemStatus
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsPostResponse201PotentialChangeOrdersItemStatus
- Schema ID: schema:anon/040325f659a99c24f8ddefcc40f91fff5f803b12

### Enum

Values: draft, not_pricing, pricing, pending, revised, proceeding, not_proceeding, no_charge, approved, rejected, void

## RestV10WorkOrderContractsPostResponse201Status
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsPostResponse201Status
- Schema ID: schema:anon/ec57ee2287ebb5fbd8538772ebb398f7a9e1051d

### Enum

Values: Draft, Out For Bid, Out For Signature, Approved, Complete, Terminated, Void

## RestV10WorkOrderContractsPostResponse201Vendor
- Role: nested
- Parent: RestV10WorkOrderContractsPostResponse201DataObject
- Schema Name: RestV10WorkOrderContractsPostResponse201Vendor
- Schema ID: schema:anon/f5c7992ebdf0f719addc1b14eef9f0b4d21d8926
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `company` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
