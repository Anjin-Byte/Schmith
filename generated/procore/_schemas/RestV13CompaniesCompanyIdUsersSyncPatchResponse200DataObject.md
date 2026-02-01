# RestV13CompaniesCompanyIdUsersSyncPatchResponse200DataObject

## RestV13CompaniesCompanyIdUsersSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV13CompaniesCompanyIdUsersSyncPatchResponse200
- Schema ID: schema:anon/43459097540f64feb75537b3b9ecda7c08396d9b

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV13CompaniesCompanyIdUsersSyncPatchResponse200EntitiesItem[]` |
| `errors` | `RestV13CompaniesCompanyIdUsersSyncPatchResponse200ErrorsItem[]` |

### Nested Types
- `RestV13CompaniesCompanyIdUsersSyncPatchResponse200EntitiesItem`
- `RestV13CompaniesCompanyIdUsersSyncPatchResponse200EntitiesItemVendor`
- `RestV13CompaniesCompanyIdUsersSyncPatchResponse200ErrorsItem`
- `RestV13CompaniesCompanyIdUsersSyncPatchResponse200ErrorsItem_7abdf4Errors`

## RestV13CompaniesCompanyIdUsersSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV13CompaniesCompanyIdUsersSyncPatchResponse200DataObject
- Schema Name: RestV13CompaniesCompanyIdUsersSyncPatchResponse200EntitiesItem
- Schema ID: schema:anon/a1e6901250192dbd1d71b8f55ca9c402eae85676
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `address` | `string` |
| `avatar` | `string` |
| `business_id` | `string` |
| `business_phone` | `string` |
| `business_phone_extension` | `int` |
| `city` | `string` |
| `country_code` | `string` |
| `email_address` | `string` |
| `email_signature` | `string` |
| `employee_id` | `string` |
| `fax_number` | `string` |
| `first_name` | `string` |
| `id` | `int` |
| `initials` | `string` |
| `is_active` | `bool` |
| `is_employee` | `bool` |
| `is_insurance_manager` | `bool` |
| `job_title` | `string` |
| `last_login_at` | `string` |
| `last_name` | `string` |
| `mobile_phone` | `string` |
| `name` | `string` |
| `notes` | `string` |
| `state_code` | `string` |
| `zip` | `string` |
| `locale` | `string` |
| `origin_id` | `string` |
| `origin_data` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `vendor` | `RestV13CompaniesCompanyIdUsersSyncPatchResponse200EntitiesItemVendor` |
| `work_classification_id` | `int` |
| `default_permission_template_id` | `int` |
| `company_permission_template_id` | `int` |

## RestV13CompaniesCompanyIdUsersSyncPatchResponse200EntitiesItemVendor
- Role: nested
- Parent: RestV13CompaniesCompanyIdUsersSyncPatchResponse200DataObject
- Schema Name: RestV13CompaniesCompanyIdUsersSyncPatchResponse200EntitiesItemVendor
- Schema ID: schema:anon/a2bd23c1f732dcacd0e94f939f77f837b9fee62a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV13CompaniesCompanyIdUsersSyncPatchResponse200ErrorsItem
- Role: nested
- Parent: RestV13CompaniesCompanyIdUsersSyncPatchResponse200DataObject
- Schema Name: RestV13CompaniesCompanyIdUsersSyncPatchResponse200ErrorsItem
- Schema ID: schema:anon/e973bc767ec756b2ed28b042c58575ab208a7497

### Fields

| Field | Type |
|------|------|
| `errors` | `RestV13CompaniesCompanyIdUsersSyncPatchResponse200ErrorsItem_7abdf4Errors` |

## RestV13CompaniesCompanyIdUsersSyncPatchResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV13CompaniesCompanyIdUsersSyncPatchResponse200DataObject
- Schema Name: RestV13CompaniesCompanyIdUsersSyncPatchResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
