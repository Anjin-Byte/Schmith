# CustomerContactBodyDataObject

## CustomerContactBodyDataObject
- Role: parent
- Schema Name: CustomerContactBody
- Schema ID: schema:types/typ.CustomerContactBody
- Primary Key: Fname

### Fields

| Field | Type |
|------|------|
| `prefix` | `string` |
| `fname` | `string` |
| `lname` | `string` |
| `suffix` | `string` |
| `contact_type` | `string` |
| `dob` | `string` |
| `anniversary` | `string` |
| `job_title` | `string` |
| `department` | `string` |
| `is_primary` | `bool` |
| `phones` | `CustomerPhoneBody[]` |
| `emails` | `CustomerEmailBody[]` |

### Nested Types
- `CustomerEmailBody`
- `CustomerPhoneBody`

## CustomerEmailBody
- Role: nested
- Parent: CustomerContactBodyDataObject
- Schema Name: CustomerEmailBody
- Schema ID: schema:types/typ.CustomerEmailBody
- Primary Key: Email

### Fields

| Field | Type |
|------|------|
| `email` | `string` |
| `class` | `string` |
| `types_accepted` | `string` |

## CustomerPhoneBody
- Role: nested
- Parent: CustomerContactBodyDataObject
- Schema Name: CustomerPhoneBody
- Schema ID: schema:types/typ.CustomerPhoneBody
- Primary Key: Phone

### Fields

| Field | Type |
|------|------|
| `phone` | `string` |
| `ext` | `int` |
| `type` | `string` |
