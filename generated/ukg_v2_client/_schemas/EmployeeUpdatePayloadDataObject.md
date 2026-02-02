# EmployeeUpdatePayloadDataObject

## EmployeeUpdatePayloadDataObject
- Role: parent
- Schema Name: EmployeeUpdatePayload
- Schema ID: schema:definitions/EmployeeUpdatePayload
- Primary Key: ExternalId

### Fields

| Field | Type |
|------|------|
| `external_id` | `string` |
| `firstname` | `string` |
| `lastname` | `string` |
| `email` | `string` |
| `language` | `string` |
| `maidenname` | `string` |
| `middlename` | `string` |
| `country` | `string` |
| `starting_date` | `string` |
| `mobile_phone_number` | `string` |
| `birth_date` | `string` |
| `address1` | `string` |
| `address2` | `string` |
| `address3` | `string` |
| `zip_code` | `string` |
| `city` | `string` |
| `state` | `string` |
| `registration_references` | `RegistrationReferenceBase[]` |
| `custom_fields` | `CustomField[]` |
| `saml_token` | `string` |

### Nested Types
- `CustomField`
- `RegistrationReferenceBase`

## CustomField
- Role: nested
- Parent: EmployeeUpdatePayloadDataObject
- Schema Name: CustomField
- Schema ID: schema:definitions/CustomField

### Fields

| Field | Type |
|------|------|
| `code` | `string` |
| `value` | `string` |

## RegistrationReferenceBase
- Role: nested
- Parent: EmployeeUpdatePayloadDataObject
- Schema Name: RegistrationReferenceBase
- Schema ID: schema:definitions/RegistrationReferenceBase
- Primary Key: OrganizationId

### Fields

| Field | Type |
|------|------|
| `organization_id` | `string` |
| `employee_number` | `string` |
| `active` | `bool` |
| `departure_date` | `string` |
