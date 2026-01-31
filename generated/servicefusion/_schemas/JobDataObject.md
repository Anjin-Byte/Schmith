# JobDataObject

## JobDataObject
- Role: parent
- Schema Name: Job
- Schema ID: schema:types/typ.Job

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `number` | `string` |
| `check_number` | `string` |
| `priority` | `string` |
| `description` | `string` |
| `tech_notes` | `string` |
| `completion_notes` | `string` |
| `payment_status` | `string` |
| `taxes_fees_total` | `double` |
| `drive_labor_total` | `double` |
| `billable_expenses_total` | `double` |
| `total` | `double` |
| `payments_deposits_total` | `double` |
| `due_total` | `double` |
| `cost_total` | `double` |
| `duration` | `int` |
| `time_frame_promised_start` | `string` |
| `time_frame_promised_end` | `string` |
| `start_date` | `DateTime` |
| `end_date` | `DateTime` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |
| `closed_at` | `DateTime` |
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
| `customer_payment_terms` | `string` |
| `project` | `string` |
| `phase` | `string` |
| `po_number` | `string` |
| `contract` | `string` |
| `note_to_customer` | `string` |
| `called_in_by` | `string` |
| `is_requires_follow_up` | `bool` |
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
| `labor_charges` | `JobLaborCharge[]` |
| `expenses` | `JobExpense[]` |
| `payments` | `Payment[]` |
| `invoices` | `Invoice[]` |
| `signatures` | `JobSignature[]` |
| `printable_work_order` | `PrintableWorkOrder[]` |
| `visits` | `JobVisit[]` |

### Nested Types
- `Agent`
- `AssignedTech`
- `CustomField`
- `Document`
- `Equipment`
- `Invoice`
- `JobExpense`
- `JobLaborCharge`
- `JobNote`
- `JobOtherCharge`
- `JobProduct`
- `JobService`
- `JobSignature`
- `JobTask`
- `JobVisit`
- `Payment`
- `PrintableWorkOrder`

## Agent
- Role: nested
- Parent: JobDataObject
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
- Parent: JobDataObject
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
- Parent: JobDataObject
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
- Parent: JobDataObject
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
- Parent: JobDataObject
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

## Invoice
- Role: nested
- Parent: JobDataObject
- Schema Name: Invoice
- Schema ID: schema:types/typ.Invoice

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `number` | `int` |
| `currency` | `string` |
| `po_number` | `string` |
| `terms` | `string` |
| `customer_message` | `string` |
| `notes` | `string` |
| `pay_online_url` | `string` |
| `qbo_invoice_no` | `int` |
| `qbo_sync_token` | `int` |
| `qbo_synced_date` | `DateTime` |
| `qbo_id` | `int` |
| `qbd_id` | `string` |
| `total` | `double` |
| `is_paid` | `bool` |
| `date` | `DateTime` |
| `mail_send_date` | `DateTime` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |
| `customer` | `string` |
| `customer_contact` | `string` |
| `payment_terms` | `string` |
| `bill_to_customer_id` | `int` |
| `bill_to_customer_location_id` | `int` |
| `bill_to_customer_contact_id` | `int` |
| `bill_to_email_id` | `int` |
| `bill_to_phone_id` | `int` |

## JobExpense
- Role: nested
- Parent: JobDataObject
- Schema Name: JobExpense
- Schema ID: schema:types/typ.JobExpense

### Fields

| Field | Type |
|------|------|
| `purchased_from` | `string` |
| `notes` | `string` |
| `amount` | `double` |
| `is_billable` | `bool` |
| `date` | `DateTime` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |
| `user` | `string` |
| `category` | `string` |
| `qbo_class_id` | `int` |
| `qbd_class_id` | `int` |

## JobLaborCharge
- Role: nested
- Parent: JobDataObject
- Schema Name: JobLaborCharge
- Schema ID: schema:types/typ.JobLaborCharge

### Fields

| Field | Type |
|------|------|
| `drive_time` | `int` |
| `drive_time_rate` | `double` |
| `drive_time_cost` | `double` |
| `drive_time_start` | `string` |
| `drive_time_end` | `string` |
| `is_drive_time_billed` | `bool` |
| `labor_time` | `int` |
| `labor_time_rate` | `double` |
| `labor_time_cost` | `double` |
| `labor_time_start` | `string` |
| `labor_time_end` | `string` |
| `labor_date` | `DateTime` |
| `is_labor_time_billed` | `bool` |
| `total` | `double` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |
| `is_status_generated` | `bool` |
| `user` | `string` |
| `visit_id` | `int` |
| `qbo_class_id` | `int` |
| `qbd_class_id` | `int` |

## JobNote
- Role: nested
- Parent: JobDataObject
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
- Parent: JobDataObject
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
- Parent: JobDataObject
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
- Parent: JobDataObject
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
- Parent: JobDataObject
- Schema Name: JobSignature
- Schema ID: schema:types/typ.JobSignature

### Fields

| Field | Type |
|------|------|
| `type` | `string` |
| `file_name` | `string` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |

## JobTask
- Role: nested
- Parent: JobDataObject
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

## JobVisit
- Role: nested
- Parent: JobDataObject
- Schema Name: JobVisit
- Schema ID: schema:types/typ.JobVisit

### Fields

| Field | Type |
|------|------|
| `notes_for_techs` | `string` |
| `time_frame_promised_start` | `string` |
| `time_frame_promised_end` | `string` |
| `duration` | `int` |
| `is_text_notified` | `bool` |
| `is_voice_notified` | `bool` |
| `start_date` | `DateTime` |
| `techs_assigned` | `object[]` |

## Payment
- Role: nested
- Parent: JobDataObject
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
- Parent: JobDataObject
- Schema Name: PrintableWorkOrder
- Schema ID: schema:types/typ.PrintableWorkOrder

### Fields

| Field | Type |
|------|------|
| `name` | `string` |
| `url` | `string` |
