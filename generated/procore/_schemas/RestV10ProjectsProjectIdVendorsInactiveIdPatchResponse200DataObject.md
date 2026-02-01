# RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200DataObject

## RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200
- Schema ID: schema:anon/0f057c1000651e3f521b4e7c0b82db9c5751e02c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `abbreviated_name` | `string` |
| `address` | `string` |
| `attachments` | `RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200AttachmentsItem[]` |
| `authorized_bidder` | `bool` |
| `business_id` | `string` |
| `business_phone` | `string` |
| `business_register` | `RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200BusinessRegister` |
| `city` | `string` |
| `company` | `string` |
| `company_vendor` | `bool` |
| `contact_count` | `int` |
| `country_code` | `string` |
| `created_at` | `string` |
| `email_address` | `string` |
| `fax_number` | `string` |
| `is_active` | `bool` |
| `is_connected` | `bool` |
| `labor_union` | `string` |
| `license_number` | `string` |
| `logo` | `string` |
| `mobile_phone` | `string` |
| `non_union_prevailing_wage` | `bool` |
| `notes` | `string` |
| `origin_code` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `prequalified` | `bool` |
| `primary_contact` | `RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200PrimaryContact` |
| `state_code` | `string` |
| `synced_to_erp` | `bool` |
| `trade_name` | `string` |
| `union_member` | `bool` |
| `updated_at` | `string` |
| `vendor_group` | `RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200VendorGroup` |
| `website` | `string` |
| `zip` | `string` |

### Nested Types
- `RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200AttachmentsItem`
- `RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200BusinessRegister`
- `RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200BusinessRegisterVerificationStatus`
- `RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200PrimaryContact`
- `RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200VendorGroup`

## RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200AttachmentsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200AttachmentsItem
- Schema ID: schema:anon/9db8b0487ffdc4ed217bad0fc75f0ca36767226c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `name` | `string` |
| `filename` | `string` |

## RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200BusinessRegister
- Role: nested
- Parent: RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200BusinessRegister
- Schema ID: schema:anon/0aba60ae7a6125cc82d556760b8f56e14b14b6a1
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `type` | `string` |
| `identifier` | `string` |
| `verified_at` | `string` |
| `verification_status` | `RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200BusinessRegisterVerificationStatus` |

## RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200BusinessRegisterVerificationStatus
- Role: nested
- Parent: RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200BusinessRegisterVerificationStatus
- Schema ID: schema:anon/179c6745c7487d14fc1af11391fcbadcd645701e

### Enum

Values: active, cancelled, does_not_exist, None

## RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200PrimaryContact
- Role: nested
- Parent: RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200PrimaryContact
- Schema ID: schema:anon/b1fafaa18c765e6ef03da47217b9230818488c1a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `first_name` | `string` |
| `last_name` | `string` |
| `business_phone` | `string` |
| `business_phone_extension` | `int` |
| `fax_number` | `string` |
| `mobile_phone` | `string` |
| `email_address` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200VendorGroup
- Role: nested
- Parent: RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdVendorsInactiveIdPatchResponse200VendorGroup
- Schema ID: schema:anon/0a3a236ec9ee3450002de71a90cdbed4c54b8792
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
