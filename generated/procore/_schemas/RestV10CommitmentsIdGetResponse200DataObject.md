# RestV10CommitmentsIdGetResponse200DataObject

## RestV10CommitmentsIdGetResponse200DataObject
- Role: parent
- Schema Name: RestV10CommitmentsIdGetResponse200
- Schema ID: schema:anon/f3071c9ceec0c0d00c0f8d503cc03d60a13db1db
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `double` |
| `title` | `string` |
| `number` | `string` |
| `status` | `RestV10CommitmentsIdGetResponse200Status` |
| `description` | `string` |
| `executed` | `bool` |
| `delivery_date` | `string` |
| `created_at` | `string` |
| `private` | `bool` |
| `vendor` | `RestV10CommitmentsIdGetResponse200Vendor` |
| `accounting_method` | `RestV10CommitmentsIdGetResponse200AccountingMethod` |
| `actual_completion_date` | `string` |
| `allow_comments` | `bool` |
| `allow_markups` | `bool` |
| `allow_payment_applications` | `bool` |
| `allow_payments` | `bool` |
| `allow_redistributions` | `bool` |
| `approved_change_orders` | `string` |
| `bill_to` | `string` |
| `budget_line_item_id` | `int` |
| `contract_estimated_completion_date` | `string` |
| `contract_start_date` | `string` |
| `contract_termination_date` | `string` |
| `deleted_at` | `string` |
| `display_materials_retainage` | `bool` |
| `display_stored_materials` | `bool` |
| `display_work_retainage` | `bool` |
| `exclusions` | `string` |
| `grand_total` | `string` |
| `inclusions` | `string` |
| `line_items_extended_total` | `string` |
| `line_items_total` | `string` |
| `payment_terms` | `string` |
| `pending_change_orders` | `string` |
| `pending_revised_contract` | `string` |
| `percentage_paid` | `string` |
| `position` | `int` |
| `remaining_balance_outstanding` | `string` |
| `requisition_number` | `string` |
| `retainage_percent` | `string` |
| `revised_contract` | `string` |
| `ship_to` | `string` |
| `ship_via` | `string` |
| `signed_contract_received_date` | `string` |
| `total_payments` | `string` |
| `total_draw_requests_amount` | `string` |
| `type` | `RestV10CommitmentsIdGetResponse200Type` |
| `updated_at` | `string` |
| `architect` | `RestV10CommitmentsIdGetResponse200Architect` |
| `assigned_to` | `RestV10CommitmentsIdGetResponse200Architect` |
| `attachments` | `RestV10CommitmentsIdGetResponse200AttachmentsItem[]` |
| `change_order_packages` | `RestV10CommitmentsIdGetResponse200ChangeOrderPackagesItem[]` |
| `change_order_requests` | `Anonymous_61b18072[][]` |
| `contractor` | `RestV10CommitmentsIdGetResponse200Vendor` |
| `cost_code` | `RestV10CommitmentsIdGetResponse200CostCode` |
| `created_by` | `RestV10CommitmentsIdGetResponse200Architect` |
| `line_items` | `RestV10CommitmentsIdGetResponse200LineItemsItem[]` |
| `potential_change_orders` | `RestV10CommitmentsIdGetResponse200PotentialChangeOrdersItem[]` |
| `payments_issued` | `RestV10CommitmentsIdGetResponse200PaymentsIssuedItem[]` |
| `received_from` | `RestV10CommitmentsIdGetResponse200Architect` |

### Nested Types
- `Anonymous_61b18072`
- `Anonymous_61b18072Status`
- `Anonymous_88ecc10dBillerType`
- `Anonymous_88ecc10dLineItemTypesItem`
- `Anonymous_88ecc10dLineItemTypesItemBaseType`
- `Anonymous_88ecc10dParent`
- `RestV10CommitmentsIdGetResponse200AccountingMethod`
- `RestV10CommitmentsIdGetResponse200Architect`
- `RestV10CommitmentsIdGetResponse200AttachmentsItem`
- `RestV10CommitmentsIdGetResponse200ChangeOrderPackagesItem`
- `RestV10CommitmentsIdGetResponse200ChangeOrderPackagesItemStatus`
- `RestV10CommitmentsIdGetResponse200CostCode`
- `RestV10CommitmentsIdGetResponse200LineItemsItem`
- `RestV10CommitmentsIdGetResponse200LineItemsItemChangeEventLineItem`
- `RestV10CommitmentsIdGetResponse200LineItemsItemCompany`
- `RestV10CommitmentsIdGetResponse200LineItemsItemExtendedType`
- `RestV10CommitmentsIdGetResponse200LineItemsItemHolder`
- `RestV10CommitmentsIdGetResponse200LineItemsItemProject`
- `RestV10CommitmentsIdGetResponse200PaymentsIssuedItem`
- `RestV10CommitmentsIdGetResponse200PotentialChangeOrdersItem`
- `RestV10CommitmentsIdGetResponse200PotentialChangeOrdersItemStatus`
- `RestV10CommitmentsIdGetResponse200Status`
- `RestV10CommitmentsIdGetResponse200Type`
- `RestV10CommitmentsIdGetResponse200Vendor`

## Anonymous_61b18072
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: Anonymous_61b18072
- Schema ID: schema:anon/61b180729e9da2a7ef3b6293c35f734d27233f34
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
| `status` | `Anonymous_61b18072Status` |
| `title` | `string` |
| `change_order_package_id` | `int` |
| `updated_at` | `string` |

## Anonymous_61b18072Status
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: Anonymous_61b18072Status
- Schema ID: schema:anon/5b89f75b59f65acdfdc32f08e622b0fbb79dc552

### Enum

Values: draft, not_pricing, pricing, pending, revised, proceeding, not_proceeding, no_charge, approved, rejected, void

## Anonymous_88ecc10dBillerType
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: Anonymous_88ecc10dBillerType
- Schema ID: schema:anon/6ce4c07d2fb83b79d4fcb225c5c9c05691bcdc4d

### Enum

Values: Project, SubJob

## Anonymous_88ecc10dLineItemTypesItem
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
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
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: Anonymous_88ecc10dLineItemTypesItemBaseType
- Schema ID: schema:anon/c1a066154239ac3e29e59285e26bd77f996807bf

### Enum

Values: equipment, materials, commitment, owner_cost, professional_services, other

## Anonymous_88ecc10dParent
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: Anonymous_88ecc10dParent
- Schema ID: schema:anon/44768f5b771296b189deec792bd565b414bae19b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV10CommitmentsIdGetResponse200AccountingMethod
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: RestV10CommitmentsIdGetResponse200AccountingMethod
- Schema ID: schema:anon/e1055d906a991a78b8abbae1161941e7d6036bb9

### Enum

Values: amount, unit

## RestV10CommitmentsIdGetResponse200Architect
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: RestV10CommitmentsIdGetResponse200Architect
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10CommitmentsIdGetResponse200AttachmentsItem
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: RestV10CommitmentsIdGetResponse200AttachmentsItem
- Schema ID: schema:anon/c337dee3df228286468f0ff6d8c4852152f75cf4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |

## RestV10CommitmentsIdGetResponse200ChangeOrderPackagesItem
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: RestV10CommitmentsIdGetResponse200ChangeOrderPackagesItem
- Schema ID: schema:anon/cd6f86362f7a9b6e0b0ef60df53066fb4b454c1d
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
| `status` | `RestV10CommitmentsIdGetResponse200ChangeOrderPackagesItemStatus` |
| `updated_at` | `string` |

## RestV10CommitmentsIdGetResponse200ChangeOrderPackagesItemStatus
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: RestV10CommitmentsIdGetResponse200ChangeOrderPackagesItemStatus
- Schema ID: schema:anon/7647971bd104dc6a401bbd43cf5295134c065be9

### Enum

Values: draft, not_pricing, pricing, pending, revised, proceeding, not_proceeding, no_charge, approved, rejected, void

## RestV10CommitmentsIdGetResponse200CostCode
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: RestV10CommitmentsIdGetResponse200CostCode
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

## RestV10CommitmentsIdGetResponse200LineItemsItem
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: RestV10CommitmentsIdGetResponse200LineItemsItem
- Schema ID: schema:anon/45c350126febb5c491b72d192c63f12a363ae4f0
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `amount` | `string` |
| `company` | `RestV10CommitmentsIdGetResponse200LineItemsItemCompany` |
| `cost_code` | `RestV10CommitmentsIdGetResponse200CostCode` |
| `created_at` | `string` |
| `description` | `string` |
| `extended_type` | `RestV10CommitmentsIdGetResponse200LineItemsItemExtendedType` |
| `holder` | `RestV10CommitmentsIdGetResponse200LineItemsItemHolder` |
| `line_item_type` | `Anonymous_88ecc10dLineItemTypesItem` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `position` | `int` |
| `project` | `RestV10CommitmentsIdGetResponse200LineItemsItemProject` |
| `quantity` | `string` |
| `tax_code_id` | `int` |
| `total_amount` | `string` |
| `extended_amount` | `string` |
| `unit_cost` | `string` |
| `uom` | `string` |
| `updated_at` | `string` |
| `change_event_line_item` | `RestV10CommitmentsIdGetResponse200LineItemsItemChangeEventLineItem` |

## RestV10CommitmentsIdGetResponse200LineItemsItemChangeEventLineItem
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: RestV10CommitmentsIdGetResponse200LineItemsItemChangeEventLineItem
- Schema ID: schema:anon/f9543f1bbfdf314c862e503b9f869af182ce5035
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `cost_rom` | `string` |
| `revenue_rom` | `string` |
| `event_id` | `int` |
| `cost_code` | `RestV10CommitmentsIdGetResponse200CostCode` |
| `line_item_type` | `Anonymous_88ecc10dLineItemTypesItem` |

## RestV10CommitmentsIdGetResponse200LineItemsItemCompany
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: RestV10CommitmentsIdGetResponse200LineItemsItemCompany
- Schema ID: schema:anon/7506dfd51b896d40480f35941478e1635f103a08
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10CommitmentsIdGetResponse200LineItemsItemExtendedType
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: RestV10CommitmentsIdGetResponse200LineItemsItemExtendedType
- Schema ID: schema:anon/0f0412b6cdbbc2bf5f5f0c9441a89be7fecab7b7

### Enum

Values: manual, calculated

## RestV10CommitmentsIdGetResponse200LineItemsItemHolder
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: RestV10CommitmentsIdGetResponse200LineItemsItemHolder
- Schema ID: schema:anon/40ac2a57a69f9c0efad2088ff408a8b12fc3a20b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `holder_type` | `string` |

## RestV10CommitmentsIdGetResponse200LineItemsItemProject
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: RestV10CommitmentsIdGetResponse200LineItemsItemProject
- Schema ID: schema:anon/a6af6eb0e462865bcb4d406febc45b2f69ca396e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10CommitmentsIdGetResponse200PaymentsIssuedItem
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: RestV10CommitmentsIdGetResponse200PaymentsIssuedItem
- Schema ID: schema:anon/2d7786674296a437e405abe455ef204c3202116e
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
| `attachments` | `RestV10CommitmentsIdGetResponse200AttachmentsItem[]` |
| `origin_id` | `string` |
| `origin_data` | `string` |

## RestV10CommitmentsIdGetResponse200PotentialChangeOrdersItem
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: RestV10CommitmentsIdGetResponse200PotentialChangeOrdersItem
- Schema ID: schema:anon/4773d7901262997962f66cefb71f5642945482b7
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
| `status` | `RestV10CommitmentsIdGetResponse200PotentialChangeOrdersItemStatus` |
| `updated_at` | `string` |

## RestV10CommitmentsIdGetResponse200PotentialChangeOrdersItemStatus
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: RestV10CommitmentsIdGetResponse200PotentialChangeOrdersItemStatus
- Schema ID: schema:anon/040325f659a99c24f8ddefcc40f91fff5f803b12

### Enum

Values: draft, not_pricing, pricing, pending, revised, proceeding, not_proceeding, no_charge, approved, rejected, void

## RestV10CommitmentsIdGetResponse200Status
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: RestV10CommitmentsIdGetResponse200Status
- Schema ID: schema:anon/b29f337874d0806efc909b377ebc7090284aa2e4

### Enum

Values: Draft, Out For Bid, Out For Signature, Approved, Complete, Terminated, Void

## RestV10CommitmentsIdGetResponse200Type
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: RestV10CommitmentsIdGetResponse200Type
- Schema ID: schema:anon/6c629cb4a9428f535f930407a62526b2cede8300

### Enum

Values: WorkOrderContract, PurchaseOrderContract

## RestV10CommitmentsIdGetResponse200Vendor
- Role: nested
- Parent: RestV10CommitmentsIdGetResponse200DataObject
- Schema Name: RestV10CommitmentsIdGetResponse200Vendor
- Schema ID: schema:anon/2b6fa06571868b6fe9370397176acbf74e3356b2
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
