# DistributionBaseDataObject

## DistributionBaseDataObject
- Role: parent
- Schema Name: DistributionBase
- Schema ID: schema:definitions/DistributionBase
- Primary Key: DistributionTypeId

### Fields

| Field | Type |
|------|------|
| `name` | `string` |
| `distribution_type_id` | `string` |
| `distribution_project_id` | `string` |
| `file_id` | `string` |
| `distribution_error` | `DistributionError` |

### Nested Types
- `DistributionError`
- `DistributionErrorErrorType`

## DistributionError
- Role: nested
- Parent: DistributionBaseDataObject
- Schema Name: DistributionError
- Schema ID: schema:definitions/DistributionError
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `message` | `string` |
| `error_type` | `DistributionErrorErrorType` |
| `code` | `string` |
| `created_at` | `string` |

## DistributionErrorErrorType
- Role: nested
- Parent: DistributionBaseDataObject
- Schema Name: DistributionErrorErrorType
- Schema ID: schema:anon/461dbb693cb764f81757f8554a9e436541412fd0

### Enum

Values: external, internal
