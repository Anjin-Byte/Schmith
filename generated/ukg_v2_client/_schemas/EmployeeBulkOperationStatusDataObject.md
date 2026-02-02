# EmployeeBulkOperationStatusDataObject

## EmployeeBulkOperationStatusDataObject
- Role: parent
- Schema Name: EmployeeBulkOperationStatus
- Schema ID: schema:definitions/EmployeeBulkOperationStatus

### Fields

| Field | Type |
|------|------|
| `summary` | `EmployeeBulkOperationStatusSummary` |
| `results` | `EmployeeBulkOperationStatusResultsNestedItem[]` |

### Nested Types
- `CustomField`
- `CustomFieldComputedFieldsForEmployee`
- `EmployeeBulkOperationStatusResultsNestedItem`
- `EmployeeBulkOperationStatusSummary`
- `EmployeeComputedFieldsProfileStatusItem`
- `EmployeeFull`
- `RegistrationReferenceBase`
- `RegistrationReferenceFull`

## CustomField
- Role: nested
- Parent: EmployeeBulkOperationStatusDataObject
- Schema Name: CustomField
- Schema ID: schema:definitions/CustomField

### Fields

| Field | Type |
|------|------|
| `code` | `string` |
| `value` | `string` |

## CustomFieldComputedFieldsForEmployee
- Role: nested
- Parent: EmployeeBulkOperationStatusDataObject
- Schema Name: CustomFieldComputedFieldsForEmployee
- Schema ID: schema:definitions/CustomFieldComputedFieldsForEmployee

### Fields

| Field | Type |
|------|------|
| `label` | `string` |

## EmployeeBulkOperationStatusResultsNestedItem
- Role: nested
- Parent: EmployeeBulkOperationStatusDataObject
- Schema Name: EmployeeBulkOperationStatusResultsNestedItem
- Schema ID: schema:anon/b1e7cfcd7f50fa70605feb2b00b7756d178cec94

### Fields

| Field | Type |
|------|------|
| `index` | `int` |
| `status` | `string` |
| `message` | `string` |
| `Result` | `EmployeeFull` |

## EmployeeBulkOperationStatusSummary
- Role: nested
- Parent: EmployeeBulkOperationStatusDataObject
- Schema Name: EmployeeBulkOperationStatusSummary
- Schema ID: schema:anon/39fe882738081e4d32998aa911bf3bb8a42da006

### Fields

| Field | Type |
|------|------|
| `total` | `int` |
| `processed` | `int` |
| `success` | `int` |
| `failed` | `int` |
| `status` | `string` |

## EmployeeComputedFieldsProfileStatusItem
- Role: nested
- Parent: EmployeeBulkOperationStatusDataObject
- Schema Name: EmployeeComputedFieldsProfileStatusItem
- Schema ID: schema:anon/95b3056d977de9e6d053e7dbc04860fae8aa59ac

### Enum

Values: pre_hired, active, terminated

## EmployeeFull
- Role: nested
- Parent: EmployeeBulkOperationStatusDataObject
- Schema Name: EmployeeFull
- Schema ID: schema:definitions/EmployeeFull
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `external_id` | `string` |
| `firstname` | `string` |
| `lastname` | `string` |
| `email` | `string` |
| `language` | `string` |
| `maidenname` | `string` |
| `middlename` | `string` |
| `country` | `string` |
| `starting_date` | `string` |
| `mobile_phone_number` | `string` |
| `birth_date` | `string` |
| `address1` | `string` |
| `address2` | `string` |
| `address3` | `string` |
| `zip_code` | `string` |
| `city` | `string` |
| `state` | `string` |
| `registration_references` | `RegistrationReferenceBase[]` |
| `custom_fields` | `CustomField[]` |
| `status` | `EmployeeComputedFieldsProfileStatusItem` |
| `id` | `string` |
| `terminated` | `bool` |
| `departure_date` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RegistrationReferenceBase
- Role: nested
- Parent: EmployeeBulkOperationStatusDataObject
- Schema Name: RegistrationReferenceBase
- Schema ID: schema:definitions/RegistrationReferenceBase
- Primary Key: OrganizationId

### Fields

| Field | Type |
|------|------|
| `organization_id` | `string` |
| `employee_number` | `string` |
| `active` | `bool` |
| `departure_date` | `string` |

## RegistrationReferenceFull
- Role: nested
- Parent: EmployeeBulkOperationStatusDataObject
- Schema Name: RegistrationReferenceFull
- Schema ID: schema:definitions/RegistrationReferenceFull
- Primary Key: OrganizationId

### Fields

| Field | Type |
|------|------|
| `organization_id` | `string` |
| `employee_number` | `string` |
| `active` | `bool` |
| `departure_date` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
