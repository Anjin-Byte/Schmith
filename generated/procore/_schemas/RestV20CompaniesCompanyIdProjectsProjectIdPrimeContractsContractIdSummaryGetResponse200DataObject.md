# RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsContractIdSummaryGetResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsContractIdSummaryGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsContractIdSummaryGetResponse200
- Schema ID: schema:anon/83158c488722b07ee0a5a27b0456e782ffead7ca

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsContractIdSummaryGetResponse200Data` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsContractIdSummaryGetResponse200Data`
- `RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsContractIdSummaryGetResponse200DataCurrencyConfiguration`

## RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsContractIdSummaryGetResponse200Data
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsContractIdSummaryGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsContractIdSummaryGetResponse200Data
- Schema ID: schema:anon/89538d69752b94674615f1b5579eb661ed6a1675

### Fields

| Field | Type |
|------|------|
| `approved_change_total` | `string` |
| `pending_revised_change_total` | `string` |
| `draft_change_total` | `string` |
| `total_invoices_amount` | `string` |
| `total_payments_amount` | `string` |
| `currency_configuration` | `RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsContractIdSummaryGetResponse200DataCurrencyConfiguration` |

## RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsContractIdSummaryGetResponse200DataCurrencyConfiguration
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsContractIdSummaryGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdPrimeContractsContractIdSummaryGetResponse200DataCurrencyConfiguration
- Schema ID: schema:anon/e4e1fa1e1bb8e98b96d752142b16de5a3e4283d9

### Fields

| Field | Type |
|------|------|
| `currency_iso_code` | `string` |
