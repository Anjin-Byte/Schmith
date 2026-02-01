# RestV10ProjectsProjectIdWorkOrderContractsContractIdCompliancePatchResponse200DataObject

## RestV10ProjectsProjectIdWorkOrderContractsContractIdCompliancePatchResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdWorkOrderContractsContractIdCompliancePatchResponse200
- Schema ID: schema:anon/d4879e2cfb374c4e19395a4b11f09eb253c689ef
- Primary Key: UpdatedById

### Fields

| Field | Type |
|------|------|
| `updated_at` | `string` |
| `updated_by_id` | `int` |
| `compliance_status` | `RestV10ProjectsProjectIdWorkOrderContractsContractIdCompliancePatchResponse200ComplianceStatus` |
| `compliance_notes` | `string` |
| `insurance_status` | `RestV10ProjectsProjectIdWorkOrderContractsContractIdCompliancePatchResponse200InsuranceStatus` |
| `insurance_notes` | `string` |

### Nested Types
- `RestV10ProjectsProjectIdWorkOrderContractsContractIdCompliancePatchResponse200ComplianceStatus`
- `RestV10ProjectsProjectIdWorkOrderContractsContractIdCompliancePatchResponse200InsuranceStatus`

## RestV10ProjectsProjectIdWorkOrderContractsContractIdCompliancePatchResponse200ComplianceStatus
- Role: nested
- Parent: RestV10ProjectsProjectIdWorkOrderContractsContractIdCompliancePatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdWorkOrderContractsContractIdCompliancePatchResponse200ComplianceStatus
- Schema ID: schema:anon/57d6212c289a392d8831f73cccbe4d9ee69d5c81

### Enum

Values: compliant, not_compliant, not_required

## RestV10ProjectsProjectIdWorkOrderContractsContractIdCompliancePatchResponse200InsuranceStatus
- Role: nested
- Parent: RestV10ProjectsProjectIdWorkOrderContractsContractIdCompliancePatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdWorkOrderContractsContractIdCompliancePatchResponse200InsuranceStatus
- Schema ID: schema:anon/a70432e49e9c8652ca76e4c23a7b6c953d4c7248

### Enum

Values: compliant, not_compliant, not_required
