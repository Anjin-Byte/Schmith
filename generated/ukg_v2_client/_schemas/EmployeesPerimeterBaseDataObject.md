# EmployeesPerimeterBaseDataObject

## EmployeesPerimeterBaseDataObject
- Role: parent
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

### Nested Types
- `CustomFieldFilterRule`
- `CustomFieldFilterRuleOperatorItem`
- `EmployeesPerimeterBaseOperator`

## CustomFieldFilterRule
- Role: nested
- Parent: EmployeesPerimeterBaseDataObject
- Schema Name: CustomFieldFilterRule
- Schema ID: schema:definitions/CustomFieldFilterRule
- Primary Key: CustomFieldId

### Fields

| Field | Type |
|------|------|
| `custom_field_id` | `string` |
| `operator` | `CustomFieldFilterRuleOperatorItem` |
| `value` | `string` |

## CustomFieldFilterRuleOperatorItem
- Role: nested
- Parent: EmployeesPerimeterBaseDataObject
- Schema Name: CustomFieldFilterRuleOperatorItem
- Schema ID: schema:anon/b89353968483881566a17091aa85441d29825efb

### Enum

Values: =, !=, <=, <, >=, >

## EmployeesPerimeterBaseOperator
- Role: nested
- Parent: EmployeesPerimeterBaseDataObject
- Schema Name: EmployeesPerimeterBaseOperator
- Schema ID: schema:anon/62bc992a0d5496dc75fdaeee1de43be7a94f91c1

### Enum

Values: =, <=
