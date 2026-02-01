# RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200DataObject

## RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200
- Schema ID: schema:anon/84d2029894ba50068907f6e56bf19a15d89aaa94

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200EntitiesItem[]` |
| `errors` | `RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200ErrorsItem[]` |

### Nested Types
- `RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200EntitiesItem`
- `RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200EntitiesItemStatus`
- `RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200ErrorsItem`
- `RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200ErrorsItem_7abdf4Errors`

## RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200EntitiesItem
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
| `status` | `RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200EntitiesItemStatus` |
| `vendor_id` | `int` |
| `additional_insured` | `string` |
| `division_template` | `string` |
| `insurance_sets` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |

## RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200EntitiesItemStatus
- Role: nested
- Parent: RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200EntitiesItemStatus
- Schema ID: schema:anon/af9f24f4c36804acb56f82269917a4a96c533739

### Enum

Values: compliant, compliant_in_progress, expired, non_compliant, non_compliant_in_progress, undecided, unregistered

## RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200ErrorsItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200ErrorsItem
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
| `status` | `RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200EntitiesItemStatus` |
| `vendor_id` | `int` |
| `additional_insured` | `string` |
| `division_template` | `string` |
| `insurance_sets` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `errors` | `RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200ErrorsItem_7abdf4Errors` |

## RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdInsurancesSyncPatchResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
