# RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchResponse200DataObject

## RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchResponse200
- Schema ID: schema:anon/b4aba982f0e32dabffa7b03238b9230afa5c2a5c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `cost_code_id` | `int` |
| `item_type` | `string` |
| `line_item_id` | `int` |
| `description_of_work` | `string` |
| `scheduled_value` | `string` |
| `work_completed_from_previous_application` | `string` |
| `work_completed_this_period` | `string` |
| `materials_presently_stored` | `string` |
| `total_completed_and_stored_to_date` | `string` |
| `total_completed_and_stored_to_date_percent` | `string` |
| `work_completed_retainage_from_previous_application` | `string` |
| `work_completed_retainage_retained_this_period` | `string` |
| `work_completed_retainage_percent_this_period` | `string` |
| `ssr_manual_override` | `bool` |
| `materials_stored_retainage_currently_retained` | `string` |
| `materials_stored_retainage_percent_this_period` | `string` |
| `work_completed_retainage_released_this_period` | `string` |
| `materials_stored_retainage_released_this_period` | `string` |
| `scheduled_quantity` | `string` |
| `scheduled_unit_price` | `string` |
| `work_completed_this_period_quantity` | `string` |
| `work_completed_from_previous_application_quantity` | `string` |
| `change_order_package_id` | `int` |
| `subcontractor_claimed_amount` | `string` |
| `comment` | `string` |
| `status` | `string` |
| `wbs_code` | `RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchResponse200WbsCode` |
| `position` | `int` |
| `currency_configuration` | `RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchResponse200CurrencyConfiguration` |
| `materials_moved` | `string` |
| `materials_retainage_retained_moved` | `string` |

### Nested Types
- `RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchResponse200CurrencyConfiguration`
- `RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchResponse200WbsCode`

## RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchResponse200CurrencyConfiguration
- Role: nested
- Parent: RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchResponse200DataObject
- Schema Name: RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchResponse200CurrencyConfiguration
- Schema ID: schema:anon/23f26b11fba4e7760b01f44eb6196766282f8116

### Fields

| Field | Type |
|------|------|
| `currency_iso_code` | `string` |

## RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchResponse200WbsCode
- Role: nested
- Parent: RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchResponse200DataObject
- Schema Name: RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchResponse200WbsCode
- Schema ID: schema:anon/6d1bf58d026ff2d4fe9fd85909b71472fba16aa4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `flat_code` | `string` |
| `description` | `string` |
