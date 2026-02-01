# UserBulkOperationStatusDataObject

## UserBulkOperationStatusDataObject
- Role: parent
- Schema Name: UserBulkOperationStatus
- Schema ID: schema:definitions/UserBulkOperationStatus

### Fields

| Field | Type |
|------|------|
| `summary` | `UserBulkOperationStatusSummary` |
| `results` | `UserBulkOperationStatusResultsItem[]` |

### Nested Types
- `CustomFieldFilterRule`
- `CustomFieldFilterRuleOperator`
- `EmployeesPerimeterBase`
- `EmployeesPerimeterBaseOperator`
- `ProfileBase`
- `UserBulkOperationStatusResultsItem`
- `UserBulkOperationStatusSummary`
- `UserFull`

## CustomFieldFilterRule
- Role: nested
- Parent: UserBulkOperationStatusDataObject
- Schema Name: CustomFieldFilterRule
- Schema ID: schema:definitions/CustomFieldFilterRule
- Primary Key: CustomFieldId

### Fields

| Field | Type |
|------|------|
| `custom_field_id` | `string` |
| `operator` | `CustomFieldFilterRuleOperator` |
| `value` | `string` |

## CustomFieldFilterRuleOperator
- Role: nested
- Parent: UserBulkOperationStatusDataObject
- Schema Name: CustomFieldFilterRuleOperator
- Schema ID: schema:anon/b89353968483881566a17091aa85441d29825efb

### Enum

Values: =, !=, <=, <, >=, >

## EmployeesPerimeterBase
- Role: nested
- Parent: UserBulkOperationStatusDataObject
- Schema Name: EmployeesPerimeterBase
- Schema ID: schema:definitions/EmployeesPerimeterBase
- Primary Key: OrganizationId

### Fields

| Field | Type |
|------|------|
| `operator` | `EmployeesPerimeterBaseOperator` |
| `organization_id` | `string` |
| `organization_group_id` | `string` |
| `custom_field_filters` | `CustomFieldFilterRule[]` |

## EmployeesPerimeterBaseOperator
- Role: nested
- Parent: UserBulkOperationStatusDataObject
- Schema Name: EmployeesPerimeterBaseOperator
- Schema ID: schema:anon/62bc992a0d5496dc75fdaeee1de43be7a94f91c1

### Enum

Values: =, <=

## ProfileBase
- Role: nested
- Parent: UserBulkOperationStatusDataObject
- Schema Name: ProfileBase
- Schema ID: schema:definitions/ProfileBase
- Primary Key: RoleId

### Fields

| Field | Type |
|------|------|
| `role_id` | `string` |
| `employees_perimeter` | `EmployeesPerimeterBase` |

## UserBulkOperationStatusResultsItem
- Role: nested
- Parent: UserBulkOperationStatusDataObject
- Schema Name: UserBulkOperationStatusResultsItem
- Schema ID: schema:anon/0c52d65c16a36ed6c66a62de28d422b8df2e4d4e

### Fields

| Field | Type |
|------|------|
| `index` | `int` |
| `status` | `string` |
| `message` | `string` |
| `Result` | `UserFull` |

## UserBulkOperationStatusSummary
- Role: nested
- Parent: UserBulkOperationStatusDataObject
- Schema Name: UserBulkOperationStatusSummary
- Schema ID: schema:anon/39fe882738081e4d32998aa911bf3bb8a42da006

### Fields

| Field | Type |
|------|------|
| `total` | `int` |
| `processed` | `int` |
| `success` | `int` |
| `failed` | `int` |
| `status` | `string` |

## UserFull
- Role: nested
- Parent: UserBulkOperationStatusDataObject
- Schema Name: UserFull
- Schema ID: schema:definitions/UserFull
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `external_id` | `string` |
| `firstname` | `string` |
| `lastname` | `string` |
| `middlename` | `string` |
| `email` | `string` |
| `language` | `string` |
| `timezone` | `string` |
| `mobile_phone_number` | `string` |
| `profiles` | `ProfileBase[]` |
| `id` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
