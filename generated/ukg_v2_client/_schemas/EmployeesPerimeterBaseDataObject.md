# EmployeesPerimeterBaseDataObject

## EmployeesPerimeterBaseDataObject
- Role: parent
- Schema Name: EmployeesPerimeterBase
- Schema ID: schema:definitions/EmployeesPerimeterBase
- Primary Key: Operator

### Fields

| Field | Type |
|------|------|
| `operator` | `OperatorEnum` |
| `organization_id` | `string` |
| `organization_group_id` | `string` |
| `custom_field_filters` | `CustomFieldFilterRule[]` |

### Nested Types
- `CustomFieldFilterRule`

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
| `operator` | `OperatorEnum` |
| `value` | `string` |
