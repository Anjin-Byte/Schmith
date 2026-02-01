# RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200DataObject

## RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200
- Schema ID: schema:anon/80e3e87862895999a63841fba8fc8bb22bd744c1
- Primary Key: UpdatedById

### Fields

| Field | Type |
|------|------|
| `updated_at` | `string` |
| `updated_by_id` | `int` |
| `compliance_status` | `RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200ComplianceStatus` |
| `compliance_notes` | `string` |
| `insurance_status` | `RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceStatus` |
| `insurance_notes` | `string` |
| `derived_insurance_status` | `string` |
| `insurance_documents` | `RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceDocumentsItem[]` |
| `derived_compliance_status` | `string` |
| `compliance_documents` | `RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200ComplianceDocumentsItem[]` |
| `insurance_requirements_not_created` | `RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceRequirementsNotCreatedItem[]` |
| `compliance_requirements_not_created` | `RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200ComplianceRequirementsNotCreatedItem[]` |

### Nested Types
- `RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200ComplianceDocumentsItem`
- `RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200ComplianceRequirementsNotCreatedItem`
- `RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200ComplianceStatus`
- `RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceDocumentsItem`
- `RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceDocumentsItemAttachmentsItem`
- `RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceDocumentsItemLevel`
- `RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceRequirementsNotCreatedItem`
- `RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceStatus`

## RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200ComplianceDocumentsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200ComplianceDocumentsItem
- Schema ID: schema:anon/bb67f90ba16f9980ee41dd627b46de3dd5d98483
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `notes` | `string` |
| `type` | `string` |
| `status` | `string` |
| `effective_at` | `string` |
| `expires_at` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `attachments` | `RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceDocumentsItemAttachmentsItem[]` |

## RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200ComplianceRequirementsNotCreatedItem
- Role: nested
- Parent: RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200ComplianceRequirementsNotCreatedItem
- Schema ID: schema:anon/e144a26a18a75c140ca5d4ef1716f02577f7623b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `type` | `string` |
| `status` | `string` |

## RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200ComplianceStatus
- Role: nested
- Parent: RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200ComplianceStatus
- Schema ID: schema:anon/57d6212c289a392d8831f73cccbe4d9ee69d5c81

### Enum

Values: compliant, not_compliant, not_required

## RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceDocumentsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceDocumentsItem
- Schema ID: schema:anon/d2c95af45acb9ea67c9495c5349302d53db00333
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `insurance_type` | `string` |
| `level` | `RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceDocumentsItemLevel` |
| `status` | `string` |
| `effective_at` | `string` |
| `expires_at` | `string` |
| `attachments` | `RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceDocumentsItemAttachmentsItem[]` |

## RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceDocumentsItemAttachmentsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceDocumentsItemAttachmentsItem
- Schema ID: schema:anon/d0283012a3527ac89601c80ffff08c6ec497babc
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `filename` | `string` |
| `content_type` | `string` |
| `url` | `string` |

## RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceDocumentsItemLevel
- Role: nested
- Parent: RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceDocumentsItemLevel
- Schema ID: schema:anon/266596e015ea2001e847cce15f6a45faf51188a7

### Enum

Values: company, project

## RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceRequirementsNotCreatedItem
- Role: nested
- Parent: RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceRequirementsNotCreatedItem
- Schema ID: schema:anon/94e64c2f119d665d7220965aea9f5e66420e011d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `level` | `string` |
| `status` | `string` |

## RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceStatus
- Role: nested
- Parent: RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdWorkOrderContractsContractIdComplianceGetResponse200InsuranceStatus
- Schema ID: schema:anon/a70432e49e9c8652ca76e4c23a7b6c953d4c7248

### Enum

Values: compliant, not_compliant, not_required
