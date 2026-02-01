# RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsSummaryGetResponse200DataObject

## RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsSummaryGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsSummaryGetResponse200
- Schema ID: schema:anon/24f28bbe3d26f9f4a248ab00357c9bbee7dd0365

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsSummaryGetResponse200Data` |

### Nested Types
- `RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsSummaryGetResponse200Data`
- `RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsSummaryGetResponse200DataCurrencyConfiguration`
- `RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsSummaryGetResponse200DataGrandTotalItem`

## RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsSummaryGetResponse200Data
- Role: nested
- Parent: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsSummaryGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsSummaryGetResponse200Data
- Schema ID: schema:anon/c35589cab60bc29efd4ea7baf1758648ce44ab8c
- Primary Key: CompanyId

### Fields

| Field | Type |
|------|------|
| `company_id` | `string` |
| `currency_configuration` | `RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsSummaryGetResponse200DataCurrencyConfiguration` |
| `grand_total` | `RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsSummaryGetResponse200DataGrandTotalItem[]` |

## RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsSummaryGetResponse200DataCurrencyConfiguration
- Role: nested
- Parent: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsSummaryGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsSummaryGetResponse200DataCurrencyConfiguration
- Schema ID: schema:anon/696e33e42daa9c16bf93c84d6ce1de4db47d4342

### Fields

| Field | Type |
|------|------|
| `currency_iso_code` | `string` |

## RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsSummaryGetResponse200DataGrandTotalItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsSummaryGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsSummaryGetResponse200DataGrandTotalItem
- Schema ID: schema:anon/74c2c4a26770ca495935ebf085af056555f43abe
- Primary Key: BudgetColumnId

### Fields

| Field | Type |
|------|------|
| `budget_column_id` | `string` |
| `total` | `double` |
