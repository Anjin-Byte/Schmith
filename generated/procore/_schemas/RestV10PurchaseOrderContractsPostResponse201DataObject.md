# RestV10PurchaseOrderContractsPostResponse201DataObject

## RestV10PurchaseOrderContractsPostResponse201DataObject
- Role: parent
- Schema Name: RestV10PurchaseOrderContractsPostResponse201
- Schema ID: schema:anon/452416dab29c71f23e15b691b3f950765d098b34
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `accounting_method` | `RestV10PurchaseOrderContractsPostResponse201AccountingMethod` |
| `approval_letter_date` | `string` |
| `approved_change_orders` | `string` |
| `assignee` | `RestV10PurchaseOrderContractsPostResponse201Assignee` |
| `attachments` | `RestV10PurchaseOrderContractsPostResponse201Attachments` |
| `bill_to_address` | `string` |
| `change_order_packages` | `RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItem[]` |
| `change_order_requests` | `RestV10PurchaseOrderContractsPostResponse201ChangeOrderRequestsItem[]` |
| `contract_date` | `string` |
| `created_at` | `string` |
| `created_by_id` | `int` |
| `deleted_at` | `string` |
| `delivery_date` | `string` |
| `description` | `string` |
| `draft_change_orders_amount` | `string` |
| `executed` | `bool` |
| `execution_date` | `string` |
| `grand_total` | `string` |
| `invoice_contacts` | `RestV10PurchaseOrderContractsPostResponse201InvoiceContactsItem[]` |
| `issued_on_date` | `string` |
| `letter_of_intent_date` | `string` |
| `line_items` | `RestV10PurchaseOrderContractsPostResponse201LineItemsItem[]` |
| `number` | `string` |
| `origin_code` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `payment_terms` | `string` |
| `payments_issued` | `RestV10PurchaseOrderContractsPostResponse201PaymentsIssuedItem[]` |
| `pending_change_orders` | `string` |
| `pending_revised_contract` | `string` |
| `percentage_paid` | `string` |
| `potential_change_orders` | `Anonymous_a465348f[][]` |
| `private` | `bool` |
| `project` | `RestV10PurchaseOrderContractsPostResponse201LineItemsItemProject` |
| `remaining_balance_outstanding` | `string` |
| `requisitions_are_enabled` | `bool` |
| `retainage_percent` | `string` |
| `returned_date` | `string` |
| `revised_contract` | `string` |
| `ship_to_address` | `string` |
| `ship_via` | `string` |
| `show_line_items_to_non_admins` | `bool` |
| `signed_contract_received_date` | `string` |
| `status` | `RestV10PurchaseOrderContractsPostResponse201Status` |
| `title` | `string` |
| `total_draw_requests_amount` | `string` |
| `total_payments` | `string` |
| `total_requisitions_amount` | `string` |
| `updated_at` | `string` |
| `vendor` | `RestV10PurchaseOrderContractsPostResponse201Vendor` |
| `currency_configuration` | `RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration` |

### Nested Types
- `Anonymous_88ecc10dBillerType`
- `Anonymous_88ecc10dLineItemTypesItem`
- `Anonymous_88ecc10dLineItemTypesItemBaseType`
- `Anonymous_88ecc10dParent`
- `Anonymous_a465348f`
- `RestV10PurchaseOrderContractsPostResponse201AccountingMethod`
- `RestV10PurchaseOrderContractsPostResponse201Assignee`
- `RestV10PurchaseOrderContractsPostResponse201Attachments`
- `RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItem`
- `RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration`
- `RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItemStatus`
- `RestV10PurchaseOrderContractsPostResponse201ChangeOrderRequestsItem`
- `RestV10PurchaseOrderContractsPostResponse201InvoiceContactsItem`
- `RestV10PurchaseOrderContractsPostResponse201LineItemsItem`
- `RestV10PurchaseOrderContractsPostResponse201LineItemsItemChangeEventLineItem`
- `RestV10PurchaseOrderContractsPostResponse201LineItemsItemCompany`
- `RestV10PurchaseOrderContractsPostResponse201LineItemsItemCostCode`
- `RestV10PurchaseOrderContractsPostResponse201LineItemsItemExtendedType`
- `RestV10PurchaseOrderContractsPostResponse201LineItemsItemHolder`
- `RestV10PurchaseOrderContractsPostResponse201LineItemsItemProject`
- `RestV10PurchaseOrderContractsPostResponse201LineItemsItemWbsCode`
- `RestV10PurchaseOrderContractsPostResponse201PaymentsIssuedItem`
- `RestV10PurchaseOrderContractsPostResponse201Status`
- `RestV10PurchaseOrderContractsPostResponse201Vendor`

## Anonymous_88ecc10dBillerType
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: Anonymous_88ecc10dBillerType
- Schema ID: schema:anon/6ce4c07d2fb83b79d4fcb225c5c9c05691bcdc4d

### Enum

Values: Project, SubJob

## Anonymous_88ecc10dLineItemTypesItem
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
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
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: Anonymous_88ecc10dLineItemTypesItemBaseType
- Schema ID: schema:anon/c1a066154239ac3e29e59285e26bd77f996807bf

### Enum

Values: equipment, materials, commitment, owner_cost, professional_services, other

## Anonymous_88ecc10dParent
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: Anonymous_88ecc10dParent
- Schema ID: schema:anon/44768f5b771296b189deec792bd565b414bae19b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## Anonymous_a465348f
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: Anonymous_a465348f
- Schema ID: schema:anon/a465348fb070acff2e83c0a6085fce5eb7fcca16
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `contract_id` | `int` |
| `created_at` | `string` |
| `due_date` | `string` |
| `invoiced_date` | `string` |
| `number` | `string` |
| `paid_date` | `string` |
| `reviewed_at` | `string` |
| `status` | `RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItemStatus` |
| `title` | `string` |
| `change_order_request_title` | `string` |
| `change_order_package_title` | `string` |
| `potential_change_order_acronym_number` | `string` |
| `change_order_request_acronym_number` | `string` |
| `change_order_package_acronym_number` | `string` |
| `change_order_tiers` | `int` |
| `updated_at` | `string` |
| `currency_configuration` | `RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration` |

## RestV10PurchaseOrderContractsPostResponse201AccountingMethod
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: RestV10PurchaseOrderContractsPostResponse201AccountingMethod
- Schema ID: schema:anon/e1055d906a991a78b8abbae1161941e7d6036bb9

### Enum

Values: amount, unit

## RestV10PurchaseOrderContractsPostResponse201Assignee
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: RestV10PurchaseOrderContractsPostResponse201Assignee
- Schema ID: schema:anon/aeae5c1d29301753eab0ee2db614e9e887f7cf40
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV10PurchaseOrderContractsPostResponse201Attachments
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: RestV10PurchaseOrderContractsPostResponse201Attachments
- Schema ID: schema:anon/c337dee3df228286468f0ff6d8c4852152f75cf4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |

## RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItem
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItem
- Schema ID: schema:anon/c0e0905c5ed405dd737888ce76b661f17a08f166
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
| `origin_code` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `paid_date` | `string` |
| `reviewed_at` | `string` |
| `signed_change_order_received_date` | `string` |
| `status` | `RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItemStatus` |
| `title` | `string` |
| `updated_at` | `string` |
| `currency_configuration` | `RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration` |

## RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration
- Schema ID: schema:anon/604508c10ceb4d00db265015715c4f3c345909ea

### Fields

| Field | Type |
|------|------|
| `base_currency_iso_code` | `string` |
| `currency_iso_code` | `string` |

## RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItemStatus
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItemStatus
- Schema ID: schema:anon/5b89f75b59f65acdfdc32f08e622b0fbb79dc552

### Enum

Values: draft, not_pricing, pricing, pending, revised, proceeding, not_proceeding, no_charge, approved, rejected, void

## RestV10PurchaseOrderContractsPostResponse201ChangeOrderRequestsItem
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: RestV10PurchaseOrderContractsPostResponse201ChangeOrderRequestsItem
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
| `status` | `RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItemStatus` |
| `title` | `string` |
| `updated_at` | `string` |
| `currency_configuration` | `RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration` |

## RestV10PurchaseOrderContractsPostResponse201InvoiceContactsItem
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: RestV10PurchaseOrderContractsPostResponse201InvoiceContactsItem
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
| `currency_configuration` | `RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration` |

## RestV10PurchaseOrderContractsPostResponse201LineItemsItem
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: RestV10PurchaseOrderContractsPostResponse201LineItemsItem
- Schema ID: schema:anon/7931e012412b92fba58498b886f10a43fec3ad63
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `amount` | `string` |
| `company` | `RestV10PurchaseOrderContractsPostResponse201LineItemsItemCompany` |
| `wbs_code` | `RestV10PurchaseOrderContractsPostResponse201LineItemsItemWbsCode` |
| `cost_code` | `RestV10PurchaseOrderContractsPostResponse201LineItemsItemCostCode` |
| `created_at` | `string` |
| `description` | `string` |
| `extended_type` | `RestV10PurchaseOrderContractsPostResponse201LineItemsItemExtendedType` |
| `holder` | `RestV10PurchaseOrderContractsPostResponse201LineItemsItemHolder` |
| `line_item_type` | `Anonymous_88ecc10dLineItemTypesItem` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `position` | `int` |
| `project` | `RestV10PurchaseOrderContractsPostResponse201LineItemsItemProject` |
| `quantity` | `string` |
| `tax_code_id` | `int` |
| `total_amount` | `string` |
| `extended_amount` | `string` |
| `unit_cost` | `string` |
| `uom` | `string` |
| `updated_at` | `string` |
| `change_event_line_item` | `RestV10PurchaseOrderContractsPostResponse201LineItemsItemChangeEventLineItem` |
| `currency_configuration` | `RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration` |

## RestV10PurchaseOrderContractsPostResponse201LineItemsItemChangeEventLineItem
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: RestV10PurchaseOrderContractsPostResponse201LineItemsItemChangeEventLineItem
- Schema ID: schema:anon/a24aa0a8f1c0d531444ee0edbfe708bf2f5dc432
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `cost_rom` | `string` |
| `revenue_rom` | `string` |
| `event_id` | `int` |
| `cost_code` | `RestV10PurchaseOrderContractsPostResponse201LineItemsItemCostCode` |
| `line_item_type` | `Anonymous_88ecc10dLineItemTypesItem` |
| `currency_configuration` | `RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration` |

## RestV10PurchaseOrderContractsPostResponse201LineItemsItemCompany
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: RestV10PurchaseOrderContractsPostResponse201LineItemsItemCompany
- Schema ID: schema:anon/7506dfd51b896d40480f35941478e1635f103a08
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10PurchaseOrderContractsPostResponse201LineItemsItemCostCode
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: RestV10PurchaseOrderContractsPostResponse201LineItemsItemCostCode
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

## RestV10PurchaseOrderContractsPostResponse201LineItemsItemExtendedType
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: RestV10PurchaseOrderContractsPostResponse201LineItemsItemExtendedType
- Schema ID: schema:anon/0f0412b6cdbbc2bf5f5f0c9441a89be7fecab7b7

### Enum

Values: manual, calculated

## RestV10PurchaseOrderContractsPostResponse201LineItemsItemHolder
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: RestV10PurchaseOrderContractsPostResponse201LineItemsItemHolder
- Schema ID: schema:anon/40ac2a57a69f9c0efad2088ff408a8b12fc3a20b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `holder_type` | `string` |

## RestV10PurchaseOrderContractsPostResponse201LineItemsItemProject
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: RestV10PurchaseOrderContractsPostResponse201LineItemsItemProject
- Schema ID: schema:anon/a6af6eb0e462865bcb4d406febc45b2f69ca396e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10PurchaseOrderContractsPostResponse201LineItemsItemWbsCode
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: RestV10PurchaseOrderContractsPostResponse201LineItemsItemWbsCode
- Schema ID: schema:anon/6d1bf58d026ff2d4fe9fd85909b71472fba16aa4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `flat_code` | `string` |
| `description` | `string` |

## RestV10PurchaseOrderContractsPostResponse201PaymentsIssuedItem
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: RestV10PurchaseOrderContractsPostResponse201PaymentsIssuedItem
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
| `attachments` | `RestV10PurchaseOrderContractsPostResponse201Attachments[]` |
| `origin_id` | `string` |
| `origin_data` | `string` |
| `currency_configuration` | `RestV10PurchaseOrderContractsPostResponse201ChangeOrderPackagesItemCurrencyConfiguration` |

## RestV10PurchaseOrderContractsPostResponse201Status
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: RestV10PurchaseOrderContractsPostResponse201Status
- Schema ID: schema:anon/7bc47b8fc64636104cb4714bc5d9c3f2a3dd9258

### Enum

Values: Draft, Processing, Submitted, Partially Received, Received, Approved, Closed

## RestV10PurchaseOrderContractsPostResponse201Vendor
- Role: nested
- Parent: RestV10PurchaseOrderContractsPostResponse201DataObject
- Schema Name: RestV10PurchaseOrderContractsPostResponse201Vendor
- Schema ID: schema:anon/f5c7992ebdf0f719addc1b14eef9f0b4d21d8926
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `company` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
