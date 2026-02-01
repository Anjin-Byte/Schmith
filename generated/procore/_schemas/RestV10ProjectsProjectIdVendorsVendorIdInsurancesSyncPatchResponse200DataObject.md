# RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200DataObject

## RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200
- Schema ID: schema:anon/b218657422bbe417ce32b524ae96add0003d9bb2

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200EntitiesItem[]` |
| `errors` | `RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200ErrorsItem[]` |

### Nested Types
- `RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200EntitiesItem`
- `RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200EntitiesItemStatus`
- `RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200ErrorsItem`
- `RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200ErrorsItem_7abdf4Errors`

## RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200EntitiesItem
- Schema ID: schema:anon/ad4559875436b8dce5a25bfcdd0e6ce3b4bf4f3e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `effective_date` | `string` |
| `enable_expired_insurance_notifications` | `bool` |
| `exempt` | `bool` |
| `expiration_date` | `string` |
| `info_received` | `bool` |
| `insurance_provider` | `string` |
| `insurance_type` | `string` |
| `limit` | `string` |
| `notes` | `string` |
| `policy_number` | `string` |
| `status` | `RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200EntitiesItemStatus` |
| `vendor_id` | `int` |
| `additional_insured` | `string` |
| `division_template` | `string` |
| `insurance_sets` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |

## RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200EntitiesItemStatus
- Role: nested
- Parent: RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200EntitiesItemStatus
- Schema ID: schema:anon/af9f24f4c36804acb56f82269917a4a96c533739

### Enum

Values: compliant, compliant_in_progress, expired, non_compliant, non_compliant_in_progress, undecided, unregistered

## RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200ErrorsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200ErrorsItem
- Schema ID: schema:anon/8e24058a0bb5b754bab392ec3151607541670f71
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `effective_date` | `string` |
| `enable_expired_insurance_notifications` | `bool` |
| `exempt` | `bool` |
| `expiration_date` | `string` |
| `info_received` | `bool` |
| `insurance_provider` | `string` |
| `insurance_type` | `string` |
| `limit` | `string` |
| `notes` | `string` |
| `policy_number` | `string` |
| `status` | `RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200EntitiesItemStatus` |
| `vendor_id` | `int` |
| `additional_insured` | `string` |
| `division_template` | `string` |
| `insurance_sets` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `errors` | `RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200ErrorsItem_7abdf4Errors` |

## RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdVendorsVendorIdInsurancesSyncPatchResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
