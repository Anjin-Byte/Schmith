# RestV10ProjectsProjectIdInsurancesSyncPatchResponse200DataObject

## RestV10ProjectsProjectIdInsurancesSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdInsurancesSyncPatchResponse200
- Schema ID: schema:anon/69f2f2335faa5f500909010ec86095fe873e0138

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10ProjectsProjectIdInsurancesSyncPatchResponse200EntitiesItem[]` |
| `errors` | `RestV10ProjectsProjectIdInsurancesSyncPatchResponse200ErrorsItem[]` |

### Nested Types
- `RestV10ProjectsProjectIdInsurancesSyncPatchResponse200EntitiesItem`
- `RestV10ProjectsProjectIdInsurancesSyncPatchResponse200EntitiesItemStatus`
- `RestV10ProjectsProjectIdInsurancesSyncPatchResponse200ErrorsItem`
- `RestV10ProjectsProjectIdInsurancesSyncPatchResponse200ErrorsItem_7abdf4Errors`

## RestV10ProjectsProjectIdInsurancesSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10ProjectsProjectIdInsurancesSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdInsurancesSyncPatchResponse200EntitiesItem
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
| `status` | `RestV10ProjectsProjectIdInsurancesSyncPatchResponse200EntitiesItemStatus` |
| `vendor_id` | `int` |
| `additional_insured` | `string` |
| `division_template` | `string` |
| `insurance_sets` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |

## RestV10ProjectsProjectIdInsurancesSyncPatchResponse200EntitiesItemStatus
- Role: nested
- Parent: RestV10ProjectsProjectIdInsurancesSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdInsurancesSyncPatchResponse200EntitiesItemStatus
- Schema ID: schema:anon/af9f24f4c36804acb56f82269917a4a96c533739

### Enum

Values: compliant, compliant_in_progress, expired, non_compliant, non_compliant_in_progress, undecided, unregistered

## RestV10ProjectsProjectIdInsurancesSyncPatchResponse200ErrorsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdInsurancesSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdInsurancesSyncPatchResponse200ErrorsItem
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
| `status` | `RestV10ProjectsProjectIdInsurancesSyncPatchResponse200EntitiesItemStatus` |
| `vendor_id` | `int` |
| `additional_insured` | `string` |
| `division_template` | `string` |
| `insurance_sets` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `errors` | `RestV10ProjectsProjectIdInsurancesSyncPatchResponse200ErrorsItem_7abdf4Errors` |

## RestV10ProjectsProjectIdInsurancesSyncPatchResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10ProjectsProjectIdInsurancesSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdInsurancesSyncPatchResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
