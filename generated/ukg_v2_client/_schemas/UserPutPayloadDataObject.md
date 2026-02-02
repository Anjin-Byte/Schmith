# UserPutPayloadDataObject

## UserPutPayloadDataObject
- Role: parent
- Schema Name: UserPutPayload
- Schema ID: schema:definitions/UserPutPayload
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
- `CustomFieldFilterRuleOperatorItemItem`
- `EmployeesPerimeterBase`
- `EmployeesPerimeterBaseOperatorItem`
- `ProfileBase`
- `ProfileUpdateParams`

## CustomFieldFilterRule
- Role: nested
- Parent: UserPutPayloadDataObject
- Schema Name: CustomFieldFilterRule
- Schema ID: schema:definitions/CustomFieldFilterRule
- Primary Key: CustomFieldId

### Fields

| Field | Type |
|------|------|
| `custom_field_id` | `string` |
| `operator` | `CustomFieldFilterRuleOperatorItemItem` |
| `value` | `string` |

## CustomFieldFilterRuleOperatorItemItem
- Role: nested
- Parent: UserPutPayloadDataObject
- Schema Name: CustomFieldFilterRuleOperatorItemItem
- Schema ID: schema:anon/b89353968483881566a17091aa85441d29825efb

### Enum

Values: =, !=, <=, <, >=, >

## EmployeesPerimeterBase
- Role: nested
- Parent: UserPutPayloadDataObject
- Schema Name: EmployeesPerimeterBase
- Schema ID: schema:definitions/EmployeesPerimeterBase
- Primary Key: OrganizationId

### Fields

| Field | Type |
|------|------|
| `operator` | `EmployeesPerimeterBaseOperatorItem` |
| `organization_id` | `string` |
| `organization_group_id` | `string` |
| `custom_field_filters` | `CustomFieldFilterRule[]` |

## EmployeesPerimeterBaseOperatorItem
- Role: nested
- Parent: UserPutPayloadDataObject
- Schema Name: EmployeesPerimeterBaseOperatorItem
- Schema ID: schema:anon/62bc992a0d5496dc75fdaeee1de43be7a94f91c1

### Enum

Values: =, <=

## ProfileBase
- Role: nested
- Parent: UserPutPayloadDataObject
- Schema Name: ProfileBase
- Schema ID: schema:definitions/ProfileBase
- Primary Key: RoleId

### Fields

| Field | Type |
|------|------|
| `role_id` | `string` |
| `employees_perimeter` | `EmployeesPerimeterBase` |

## ProfileUpdateParams
- Role: nested
- Parent: UserPutPayloadDataObject
- Schema Name: ProfileUpdateParams
- Schema ID: schema:definitions/ProfileUpdateParams
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `role_id` | `string` |
| `employees_perimeter` | `EmployeesPerimeterBase` |
| `id` | `string` |
