# RestV13CompaniesCompanyIdUsersPostResponse201DataObject

## RestV13CompaniesCompanyIdUsersPostResponse201DataObject
- Role: parent
- Schema Name: RestV13CompaniesCompanyIdUsersPostResponse201
- Schema ID: schema:anon/42cf3e394ff6614a95c3364217b5b50f81abde7e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `address` | `string` |
| `add_to_new_projects` | `bool` |
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
| `origin_id` | `string` |
| `origin_data` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `vendor` | `RestV13CompaniesCompanyIdUsersPostResponse201Vendor` |
| `work_classification_id` | `int` |
| `default_permission_template_id` | `int` |
| `company_permission_template_id` | `int` |

### Nested Types
- `RestV13CompaniesCompanyIdUsersPostResponse201Vendor`

## RestV13CompaniesCompanyIdUsersPostResponse201Vendor
- Role: nested
- Parent: RestV13CompaniesCompanyIdUsersPostResponse201DataObject
- Schema Name: RestV13CompaniesCompanyIdUsersPostResponse201Vendor
- Schema ID: schema:anon/a2bd23c1f732dcacd0e94f939f77f837b9fee62a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
