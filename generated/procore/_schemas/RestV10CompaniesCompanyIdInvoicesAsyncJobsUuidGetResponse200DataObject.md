# RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGetResponse200DataObject

## RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGetResponse200DataObject
- Role: parent
- Schema Name: RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGetResponse200
- Schema ID: schema:anon/232fb4eb3a4abe16e063a1a73d30ffff6f4e0ab6
- Primary Key: CompanyId

### Fields

| Field | Type |
|------|------|
| `uuid` | `string` |
| `company_id` | `int` |
| `created_by_id` | `int` |
| `status` | `RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGetResponse200Status` |
| `result` | `RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGetResponse200Result` |
| `created_at` | `string` |
| `updated_at` | `string` |

### Nested Types
- `RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGetResponse200Result`
- `RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGetResponse200Status`

## RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGetResponse200Result
- Role: nested
- Parent: RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGetResponse200Result
- Schema ID: schema:anon/d9392eecf0b1198806da04b10670dc5802818ee1

### Fields

## RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGetResponse200Status
- Role: nested
- Parent: RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGetResponse200Status
- Schema ID: schema:anon/1c5b3a997261a366655b1e3f1d0f5e9866823a59

### Enum

Values: pending, in_progress, completed, failed
