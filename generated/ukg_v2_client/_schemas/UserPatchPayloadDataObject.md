# UserPatchPayloadDataObject

## UserPatchPayloadDataObject
- Role: parent
- Schema Name: UserPatchPayload
- Schema ID: schema:definitions/UserPatchPayload
- Primary Key: ExternalId

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
| `saml_token` | `string` |

### Nested Types
- `CustomFieldFilterRule`
- `CustomFieldFilterRuleOperator`
- `EmployeesPerimeterBase`
- `EmployeesPerimeterBaseOperator`
- `ProfileBase`

## CustomFieldFilterRule
- Role: nested
- Parent: UserPatchPayloadDataObject
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
- Parent: UserPatchPayloadDataObject
- Schema Name: CustomFieldFilterRuleOperator
- Schema ID: schema:anon/b89353968483881566a17091aa85441d29825efb

### Enum

Values: =, !=, <=, <, >=, >

## EmployeesPerimeterBase
- Role: nested
- Parent: UserPatchPayloadDataObject
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
- Parent: UserPatchPayloadDataObject
- Schema Name: EmployeesPerimeterBaseOperator
- Schema ID: schema:anon/62bc992a0d5496dc75fdaeee1de43be7a94f91c1

### Enum

Values: =, <=

## ProfileBase
- Role: nested
- Parent: UserPatchPayloadDataObject
- Schema Name: ProfileBase
- Schema ID: schema:definitions/ProfileBase
- Primary Key: RoleId

### Fields

| Field | Type |
|------|------|
| `role_id` | `string` |
| `employees_perimeter` | `EmployeesPerimeterBase` |
