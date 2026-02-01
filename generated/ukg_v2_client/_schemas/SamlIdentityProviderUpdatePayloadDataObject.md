# SamlIdentityProviderUpdatePayloadDataObject

## SamlIdentityProviderUpdatePayloadDataObject
- Role: parent
- Schema Name: SamlIdentityProviderUpdatePayload
- Schema ID: schema:definitions/SamlIdentityProviderUpdatePayload
- Primary Key: EntityId

### Fields

| Field | Type |
|------|------|
| `activated` | `bool` |
| `enable_sp_session` | `bool` |
| `entity_id` | `string` |
| `name` | `string` |
| `next_logout_url` | `string` |
| `scope` | `SamlIdentityProviderBaseScope` |
| `sso_endpoint` | `string` |
| `workflow_type` | `SamlIdentityProviderBaseWorkflowType` |
| `x509_certificate` | `string` |

### Nested Types
- `SamlIdentityProviderBaseScope`
- `SamlIdentityProviderBaseWorkflowType`

## SamlIdentityProviderBaseScope
- Role: nested
- Parent: SamlIdentityProviderUpdatePayloadDataObject
- Schema Name: SamlIdentityProviderBaseScope
- Schema ID: schema:anon/1d05f72b2e1ad71094b5be98b9124c1f23ff04f8

### Enum

Values: employee, manager

## SamlIdentityProviderBaseWorkflowType
- Role: nested
- Parent: SamlIdentityProviderUpdatePayloadDataObject
- Schema Name: SamlIdentityProviderBaseWorkflowType
- Schema ID: schema:anon/fb7ddeacbe32677a4677ae29f11c0aed5d0071ec

### Enum

Values: IdP initiated, SP initiated
