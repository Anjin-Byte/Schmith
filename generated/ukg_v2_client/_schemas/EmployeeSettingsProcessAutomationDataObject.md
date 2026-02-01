# EmployeeSettingsProcessAutomationDataObject

## EmployeeSettingsProcessAutomationDataObject
- Role: parent
- Schema Name: EmployeeSettingsProcessAutomation
- Schema ID: schema:definitions/EmployeeSettingsProcessAutomation
- Primary Key: EmployeeId

### Fields

| Field | Type |
|------|------|
| `employee_id` | `string` |
| `onboarding` | `EmployeeSettingsProcessAutomationOnboarding` |

### Nested Types
- `EmployeeSettingsProcessAutomationOnboarding`

## EmployeeSettingsProcessAutomationOnboarding
- Role: nested
- Parent: EmployeeSettingsProcessAutomationDataObject
- Schema Name: EmployeeSettingsProcessAutomationOnboarding
- Schema ID: schema:anon/d29703d577a7ab59f6c0f19f7a24de171bb75928

### Fields

| Field | Type |
|------|------|
| `welcome_message` | `string` |
| `welcome_file_filename` | `string` |
| `welcome_file_title` | `string` |
