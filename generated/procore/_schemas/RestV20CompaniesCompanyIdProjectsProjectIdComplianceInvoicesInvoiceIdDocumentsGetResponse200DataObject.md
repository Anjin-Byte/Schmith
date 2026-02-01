# RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200
- Schema ID: schema:anon/a2467c608a3f7a9492e1ac4d455aec9698cf27d8

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200Data` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200Data`
- `RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200DataComplianceDocumentProstoreFilesItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200DataComplianceDocumentProstoreFilesItemData`
- `RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200DataComplianceDocumentProstoreFilesItemDataProstoreFile`

## RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200Data
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200Data
- Schema ID: schema:anon/52da21df490ded2c6e009e6a7904038a2fbfd69d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |
| `status` | `string` |
| `document_type` | `string` |
| `notes` | `string` |
| `effective_at` | `string` |
| `expires_at` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `reviewed_at` | `string` |
| `created_by_id` | `string` |
| `created_by` | `string` |
| `updated_by_id` | `string` |
| `updated_by` | `string` |
| `reviewed_by_id` | `string` |
| `reviewed_by` | `string` |
| `reviewer_notes` | `string` |
| `compliance_document_prostore_files` | `RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200DataComplianceDocumentProstoreFilesItem[]` |

## RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200DataComplianceDocumentProstoreFilesItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200DataComplianceDocumentProstoreFilesItem
- Schema ID: schema:anon/dfd472622bac903ea91b8585aad4b48589223ffb

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200DataComplianceDocumentProstoreFilesItemData` |

## RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200DataComplianceDocumentProstoreFilesItemData
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200DataComplianceDocumentProstoreFilesItemData
- Schema ID: schema:anon/d855de334942c4babecb544c4985ec52de5dbdaf
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `compliance_document_id` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `created_by_id` | `string` |
| `created_by` | `string` |
| `updated_by_id` | `string` |
| `updated_by` | `string` |
| `prostore_file` | `RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200DataComplianceDocumentProstoreFilesItemDataProstoreFile` |

## RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200DataComplianceDocumentProstoreFilesItemDataProstoreFile
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdComplianceInvoicesInvoiceIdDocumentsGetResponse200DataComplianceDocumentProstoreFilesItemDataProstoreFile
- Schema ID: schema:anon/8d49aec9b83051f07cb0ea1e19c00bcd609101a2
- Primary Key: ProstoreFileId

### Fields

| Field | Type |
|------|------|
| `prostore_file_id` | `string` |
| `name` | `string` |
| `content_type` | `string` |
| `url` | `string` |
| `uuid` | `string` |
