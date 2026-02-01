# OauthTokenInfoGetResponse200DataObject

## OauthTokenInfoGetResponse200DataObject
- Role: parent
- Schema Name: OauthTokenInfoGetResponse200
- Schema ID: schema:anon/4c4198819f480ae651b28c724e014b1bf1506675
- Primary Key: ResourceOwnerId

### Fields

| Field | Type |
|------|------|
| `resource_owner_id` | `int` |
| `scopes` | `string[]` |
| `expires_in_seconds` | `int` |
| `application` | `OauthTokenInfoGetResponse200Application` |
| `created_at` | `int` |

### Nested Types
- `OauthTokenInfoGetResponse200Application`

## OauthTokenInfoGetResponse200Application
- Role: nested
- Parent: OauthTokenInfoGetResponse200DataObject
- Schema Name: OauthTokenInfoGetResponse200Application
- Schema ID: schema:anon/15f330a253a7d8d1dce4f35bd5b634dde87b449c

### Fields

| Field | Type |
|------|------|
| `uid` | `string` |
