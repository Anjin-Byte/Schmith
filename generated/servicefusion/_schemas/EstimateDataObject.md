# EstimateDataObject

## EstimateDataObject
- Role: parent
- Schema Name: Estimate
- Schema ID: schema:types/typ.Estimate

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `number` | `string` |
| `description` | `string` |
| `tech_notes` | `string` |
| `customer_payment_terms` | `string` |
| `payment_status` | `string` |
| `taxes_fees_total` | `double` |
| `total` | `double` |
| `due_total` | `double` |
| `cost_total` | `double` |
| `duration` | `int` |
| `time_frame_promised_start` | `string` |
| `time_frame_promised_end` | `string` |
| `start_date` | `DateTime` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |
| `customer_id` | `int` |
| `customer_name` | `string` |
| `parent_customer` | `string` |
| `status` | `string` |
| `sub_status` | `string` |
| `contact_first_name` | `string` |
| `contact_last_name` | `string` |
| `street_1` | `string` |
| `street_2` | `string` |
| `city` | `string` |
| `state_prov` | `string` |
| `postal_code` | `string` |
| `location_name` | `string` |
| `is_gated` | `bool` |
| `gate_instructions` | `string` |
| `category` | `string` |
| `source` | `string` |
| `payment_type` | `string` |
| `project` | `string` |
| `phase` | `string` |
| `po_number` | `string` |
| `contract` | `string` |
| `note_to_customer` | `string` |
| `opportunity_rating` | `int` |
| `opportunity_owner` | `string` |
| `agents` | `Agent[]` |
| `custom_fields` | `CustomField[]` |
| `pictures` | `Document[]` |
| `documents` | `Document[]` |
| `equipment` | `Equipment[]` |
| `techs_assigned` | `AssignedTech[]` |
| `tasks` | `JobTask[]` |
| `notes` | `JobNote[]` |
| `products` | `JobProduct[]` |
| `services` | `JobService[]` |
| `other_charges` | `JobOtherCharge[]` |
| `payments` | `Payment[]` |
| `signatures` | `JobSignature[]` |
| `printable_work_order` | `PrintableWorkOrder[]` |
| `tags` | `JobTag[]` |

### Nested Types
- `Agent`
- `AssignedTech`
- `CustomField`
- `Document`
- `Equipment`
- `JobNote`
- `JobOtherCharge`
- `JobProduct`
- `JobService`
- `JobSignature`
- `JobTag`
- `JobTask`
- `Payment`
- `PrintableWorkOrder`

## Agent
- Role: nested
- Parent: EstimateDataObject
- Schema Name: Agent
- Schema ID: schema:types/typ.Agent

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `first_name` | `string` |
| `last_name` | `string` |

## AssignedTech
- Role: nested
- Parent: EstimateDataObject
- Schema Name: AssignedTech
- Schema ID: schema:types/typ.AssignedTech

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `first_name` | `string` |
| `last_name` | `string` |

## CustomField
- Role: nested
- Parent: EstimateDataObject
- Schema Name: CustomField
- Schema ID: schema:types/typ.CustomField

### Fields

| Field | Type |
|------|------|
| `name` | `string` |
| `value` | `object` |
| `type` | `string` |
| `group` | `string` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |
| `is_required` | `bool` |

## Document
- Role: nested
- Parent: EstimateDataObject
- Schema Name: Document
- Schema ID: schema:types/typ.Document

### Fields

| Field | Type |
|------|------|
| `name` | `string` |
| `file_location` | `string` |
| `doc_type` | `string` |
| `comment` | `string` |
| `sort` | `int` |
| `is_private` | `bool` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |
| `customer_doc_id` | `int` |

## Equipment
- Role: nested
- Parent: EstimateDataObject
- Schema Name: Equipment
- Schema ID: schema:types/typ.Equipment

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `type` | `string` |
| `make` | `string` |
| `model` | `string` |
| `sku` | `string` |
| `serial_number` | `string` |
| `location` | `string` |
| `notes` | `string` |
| `extended_warranty_provider` | `string` |
| `is_extended_warranty` | `bool` |
| `extended_warranty_date` | `DateTime` |
| `warranty_date` | `DateTime` |
| `install_date` | `DateTime` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |
| `customer_id` | `int` |
| `customer` | `string` |
| `customer_location` | `string` |
| `custom_fields` | `CustomField[]` |

## JobNote
- Role: nested
- Parent: EstimateDataObject
- Schema Name: JobNote
- Schema ID: schema:types/typ.JobNote

### Fields

| Field | Type |
|------|------|
| `notes` | `string` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |

## JobOtherCharge
- Role: nested
- Parent: EstimateDataObject
- Schema Name: JobOtherCharge
- Schema ID: schema:types/typ.JobOtherCharge

### Fields

| Field | Type |
|------|------|
| `name` | `string` |
| `rate` | `double` |
| `total` | `double` |
| `charge_index` | `int` |
| `parent_index` | `int` |
| `is_percentage` | `bool` |
| `is_discount` | `bool` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |
| `other_charge` | `string` |
| `applies_to` | `string` |
| `service_list_id` | `int` |
| `other_charge_id` | `int` |
| `pattern_row_id` | `int` |
| `qbo_class_id` | `int` |
| `qbd_class_id` | `int` |

## JobProduct
- Role: nested
- Parent: EstimateDataObject
- Schema Name: JobProduct
- Schema ID: schema:types/typ.JobProduct

### Fields

| Field | Type |
|------|------|
| `name` | `string` |
| `description` | `string` |
| `multiplier` | `int` |
| `rate` | `double` |
| `total` | `double` |
| `cost` | `double` |
| `actual_cost` | `double` |
| `item_index` | `int` |
| `parent_index` | `int` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |
| `is_show_rate_items` | `bool` |
| `tax` | `string` |
| `product` | `string` |
| `product_list_id` | `int` |
| `warehouse_id` | `int` |
| `pattern_row_id` | `int` |
| `qbo_class_id` | `int` |
| `qbd_class_id` | `int` |

## JobService
- Role: nested
- Parent: EstimateDataObject
- Schema Name: JobService
- Schema ID: schema:types/typ.JobService

### Fields

| Field | Type |
|------|------|
| `name` | `string` |
| `description` | `string` |
| `multiplier` | `int` |
| `rate` | `double` |
| `total` | `double` |
| `cost` | `double` |
| `actual_cost` | `double` |
| `item_index` | `int` |
| `parent_index` | `int` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |
| `is_show_rate_items` | `bool` |
| `tax` | `string` |
| `service` | `string` |
| `service_list_id` | `int` |
| `service_rate_id` | `int` |
| `pattern_row_id` | `int` |
| `qbo_class_id` | `int` |
| `qbd_class_id` | `int` |

## JobSignature
- Role: nested
- Parent: EstimateDataObject
- Schema Name: JobSignature
- Schema ID: schema:types/typ.JobSignature

### Fields

| Field | Type |
|------|------|
| `type` | `string` |
| `file_name` | `string` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |

## JobTag
- Role: nested
- Parent: EstimateDataObject
- Schema Name: JobTag
- Schema ID: schema:types/typ.JobTag

### Fields

| Field | Type |
|------|------|
| `tag` | `string` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |

## JobTask
- Role: nested
- Parent: EstimateDataObject
- Schema Name: JobTask
- Schema ID: schema:types/typ.JobTask

### Fields

| Field | Type |
|------|------|
| `type` | `string` |
| `description` | `string` |
| `start_time` | `string` |
| `start_date` | `DateTime` |
| `end_date` | `DateTime` |
| `is_completed` | `bool` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |

## Payment
- Role: nested
- Parent: EstimateDataObject
- Schema Name: Payment
- Schema ID: schema:types/typ.Payment

### Fields

| Field | Type |
|------|------|
| `transaction_type` | `string` |
| `transaction_token` | `string` |
| `transaction_id` | `string` |
| `payment_transaction_id` | `int` |
| `original_transaction_id` | `int` |
| `apply_to` | `string` |
| `amount` | `double` |
| `memo` | `string` |
| `authorization_code` | `string` |
| `bill_to_street_address` | `string` |
| `bill_to_postal_code` | `string` |
| `bill_to_country` | `string` |
| `reference_number` | `string` |
| `is_resync_qbo` | `bool` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |
| `received_on` | `DateTime` |
| `qbo_synced_date` | `DateTime` |
| `qbo_id` | `int` |
| `qbd_id` | `string` |
| `customer` | `string` |
| `type` | `string` |
| `invoice_id` | `int` |
| `gateway_id` | `int` |
| `receipt_id` | `string` |

## PrintableWorkOrder
- Role: nested
- Parent: EstimateDataObject
- Schema Name: PrintableWorkOrder
- Schema ID: schema:types/typ.PrintableWorkOrder

### Fields

| Field | Type |
|------|------|
| `name` | `string` |
| `url` | `string` |
