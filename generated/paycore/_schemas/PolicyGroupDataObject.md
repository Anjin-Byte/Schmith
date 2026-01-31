# PolicyGroupDataObject

## PolicyGroupDataObject
- Role: parent
- Schema Name: PolicyGroup
- Schema ID: schema:components/PolicyGroup

### Fields

| Field | Type |
|------|------|
| `policyGroupId` | `string` |
| `policyGroupName` | `string` |
| `policies` | `Policy[]` |

### Nested Types
- `Policy`

## Policy
- Role: nested
- Parent: PolicyGroupDataObject
- Schema Name: Policy
- Schema ID: schema:components/Policy

### Fields

| Field | Type |
|------|------|
| `policyName` | `string` |
| `policyType` | `string` |
