# RestV10ProjectsProjectIdUsersPostResponse201DataObject

## RestV10ProjectsProjectIdUsersPostResponse201DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdUsersPostResponse201
- Schema ID: schema:anon/a268f8b46f1ff3dd7ceafd6c34b7989cd5e8745b
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
| `name` | `string` |
| `id` | `int` |
| `initials` | `string` |
| `is_active` | `bool` |
| `is_employee` | `bool` |
| `is_insurance_manager` | `bool` |
| `job_title` | `string` |
| `last_login_at` | `string` |
| `last_name` | `string` |
| `mobile_phone` | `string` |
| `notes` | `string` |
| `state_code` | `string` |
| `zip` | `string` |
| `default_permission_template_id` | `int` |
| `company_permission_template_id` | `int` |
| `origin_id` | `string` |
| `origin_data` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `work_classification_id` | `int` |
| `vendor` | `RestV10ProjectsProjectIdUsersPostResponse201Vendor` |

### Nested Types
- `RestV10ProjectsProjectIdUsersPostResponse201Vendor`

## RestV10ProjectsProjectIdUsersPostResponse201Vendor
- Role: nested
- Parent: RestV10ProjectsProjectIdUsersPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdUsersPostResponse201Vendor
- Schema ID: schema:anon/a2bd23c1f732dcacd0e94f939f77f837b9fee62a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
