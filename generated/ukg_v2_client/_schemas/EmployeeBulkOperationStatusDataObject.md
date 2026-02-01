# EmployeeBulkOperationStatusDataObject

## EmployeeBulkOperationStatusDataObject
- Role: parent
- Schema Name: EmployeeBulkOperationStatus
- Schema ID: schema:definitions/EmployeeBulkOperationStatus

### Fields

| Field | Type |
|------|------|
| `summary` | `Anonymous_39fe8827` |
| `results` | `Anonymous_b1e7cfcd[]` |

### Nested Types
- `Anonymous_39fe8827`
- `Anonymous_b1e7cfcd`
- `EmployeeComputedFieldsProfileStatus`
- `EmployeeFull`

## Anonymous_39fe8827
- Role: nested
- Parent: EmployeeBulkOperationStatusDataObject
- Schema Name: Anonymous_39fe8827
- Schema ID: schema:anon/39fe882738081e4d32998aa911bf3bb8a42da006

### Fields

| Field | Type |
|------|------|
| `total` | `int` |
| `processed` | `int` |
| `success` | `int` |
| `failed` | `int` |
| `status` | `string` |

## Anonymous_b1e7cfcd
- Role: nested
- Parent: EmployeeBulkOperationStatusDataObject
- Schema Name: Anonymous_b1e7cfcd
- Schema ID: schema:anon/b1e7cfcd7f50fa70605feb2b00b7756d178cec94

### Fields

| Field | Type |
|------|------|
| `index` | `int` |
| `status` | `string` |
| `message` | `string` |
| `Result` | `EmployeeFull` |

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
