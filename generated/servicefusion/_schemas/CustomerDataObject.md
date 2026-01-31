# CustomerDataObject

## CustomerDataObject
- Role: parent
- Schema Name: Customer
- Schema ID: schema:types/typ.Customer

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `customer_name` | `string` |
| `fully_qualified_name` | `string` |
| `parent_customer` | `string` |
| `account_number` | `string` |
| `account_balance` | `double` |
| `private_notes` | `string` |
| `public_notes` | `string` |
| `credit_rating` | `string` |
| `labor_charge_type` | `string` |
| `labor_charge_default_rate` | `double` |
| `last_serviced_date` | `DateTime` |
| `is_bill_for_drive_time` | `bool` |
| `is_vip` | `bool` |
| `referral_source` | `string` |
| `agent` | `string` |
| `discount` | `double` |
| `discount_type` | `string` |
| `payment_type` | `string` |
| `payment_terms` | `string` |
| `assigned_contract` | `string` |
| `industry` | `string` |
| `is_taxable` | `bool` |
| `tax_item_name` | `string` |
| `qbo_sync_token` | `int` |
| `qbo_currency` | `string` |
| `qbo_id` | `int` |
| `qbd_id` | `string` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |
| `contacts` | `CustomerContact[]` |
| `locations` | `CustomerLocation[]` |
| `custom_fields` | `CustomField[]` |

### Nested Types
- `CustomField`
- `CustomerContact`
- `CustomerEmail`
- `CustomerLocation`
- `CustomerPhone`

## CustomField
- Role: nested
- Parent: CustomerDataObject
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

## CustomerContact
- Role: nested
- Parent: CustomerDataObject
- Schema Name: CustomerContact
- Schema ID: schema:types/typ.CustomerContact

### Fields

| Field | Type |
|------|------|
| `prefix` | `string` |
| `fname` | `string` |
| `lname` | `string` |
| `suffix` | `string` |
| `contact_type` | `string` |
| `dob` | `string` |
| `anniversary` | `string` |
| `job_title` | `string` |
| `department` | `string` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |
| `is_primary` | `bool` |
| `phones` | `CustomerPhone[]` |
| `emails` | `CustomerEmail[]` |

## CustomerEmail
- Role: nested
- Parent: CustomerDataObject
- Schema Name: CustomerEmail
- Schema ID: schema:types/typ.CustomerEmail

### Fields

| Field | Type |
|------|------|
| `email` | `string` |
| `class` | `string` |
| `types_accepted` | `string` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |

## CustomerLocation
- Role: nested
- Parent: CustomerDataObject
- Schema Name: CustomerLocation
- Schema ID: schema:types/typ.CustomerLocation

### Fields

| Field | Type |
|------|------|
| `street_1` | `string` |
| `street_2` | `string` |
| `city` | `string` |
| `state_prov` | `string` |
| `postal_code` | `string` |
| `country` | `string` |
| `nickname` | `string` |
| `gate_instructions` | `string` |
| `latitude` | `double` |
| `longitude` | `double` |
| `location_type` | `string` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |
| `is_primary` | `bool` |
| `is_gated` | `bool` |
| `is_bill_to` | `bool` |
| `customer_contact` | `string` |

## CustomerPhone
- Role: nested
- Parent: CustomerDataObject
- Schema Name: CustomerPhone
- Schema ID: schema:types/typ.CustomerPhone

### Fields

| Field | Type |
|------|------|
| `phone` | `string` |
| `ext` | `int` |
| `type` | `string` |
| `created_at` | `DateTime` |
| `updated_at` | `DateTime` |
| `is_mobile` | `bool` |
