# TaskTemplatesDataObject

## TaskTemplatesDataObject
- Role: parent
- Schema Name: TaskTemplates
- Schema ID: schema:definitions/TaskTemplates
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `type` | `TaskTemplatesType` |
| `name` | `string` |
| `description` | `string` |
| `process_template_id` | `string` |
| `assigned_to` | `TaskTemplatesAssignedTo` |
| `depends_on_id` | `string` |
| `fetch_previous_data` | `bool` |
| `role_id` | `string` |

### Nested Types
- `TaskTemplatesAssignedTo`
- `TaskTemplatesType`

## TaskTemplatesAssignedTo
- Role: nested
- Parent: TaskTemplatesDataObject
- Schema Name: TaskTemplatesAssignedTo
- Schema ID: schema:anon/3c734967a8ec04138d53e679e95e4a3943c81225

### Enum

Values: users, employee

## TaskTemplatesType
- Role: nested
- Parent: TaskTemplatesDataObject
- Schema Name: TaskTemplatesType
- Schema ID: schema:anon/8a28ac285e30a4f43d1d16a5b199c7ac2f1f35ed

### Enum

Values: acknowledgment, basic, fill_form, fill_pdf, signature, validation
