# PolicyGroupDataObject

## PolicyGroupDataObject
- Role: parent
- Schema Name: PolicyGroup
- Schema ID: schema:components/PolicyGroup

### Fields
- `policyGroupId`: `string`
- `policyGroupName`: `string`
- `policies`: `Policy[]`

### Nested Types
- `Policy`

## Policy
- Role: nested
- Parent: PolicyGroupDataObject
- Schema Name: Policy
- Schema ID: schema:components/Policy

### Fields
- `policyName`: `string`
- `policyType`: `string`
