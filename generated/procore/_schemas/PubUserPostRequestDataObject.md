# PubUserPostRequestDataObject

## PubUserPostRequestDataObject
- Role: parent
- Schema Name: PubUserPostRequest
- Schema ID: schema:components/PubUserPostRequest

### Fields

| Field | Type |
|------|------|
| `userEmail` | `string` |
| `firstName` | `string` |
| `lastName` | `string` |
| `title` | `string` |
| `userCompanyRole` | `PubUserPostRequestUsercompanyrole` |
| `sendNotification` | `bool` |

### Nested Types
- `PubUserPostRequestUsercompanyrole`

## PubUserPostRequestUsercompanyrole
- Role: nested
- Parent: PubUserPostRequestDataObject
- Schema Name: PubUserPostRequestUsercompanyrole
- Schema ID: schema:anon/13c38b99624adde11456c3cc928d62a2c62e9967

### Enum

Values: admin, team, collaborator
