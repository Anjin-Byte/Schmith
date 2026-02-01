# EmployeeBulkOperationStatusDataObject

## EmployeeBulkOperationStatusDataObject
- Role: parent
- Schema Name: EmployeeBulkOperationStatus
- Schema ID: schema:definitions/EmployeeBulkOperationStatus

### Fields

| Field | Type |
|------|------|
| `summary` | `EmployeeBulkOperationStatusSummary` |
| `results` | `EmployeeBulkOperationStatusResultsItem[]` |

### Nested Types
- `EmployeeBulkOperationStatusResultsItem`
- `EmployeeBulkOperationStatusSummary`
- `EmployeeComputedFieldsProfileStatus`
- `EmployeeFull`

## EmployeeBulkOperationStatusResultsItem
- Role: nested
- Parent: EmployeeBulkOperationStatusDataObject
- Schema Name: EmployeeBulkOperationStatusResultsItem
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

## EmployeeComputedFieldsProfileStatus
- Role: nested
- Parent: EmployeeBulkOperationStatusDataObject
- Schema Name: EmployeeComputedFieldsProfileStatus
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
| `status` | `EmployeeComputedFieldsProfileStatus` |
| `id` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
