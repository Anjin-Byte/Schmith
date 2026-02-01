# RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200
- Schema ID: schema:anon/d3bedc12008ef5a8cac5577c6e3ee3bdab587a57

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemApprovalStatus`
- `RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemColumnTotalsItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemColumnTotalsItemComparison`
- `RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemCreatedBy`
- `RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemCurrencyConfiguration`
- `RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemStatus`

## RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItem
- Schema ID: schema:anon/bbc0754b0689b53006b2154a5ca55a6de69cb00e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |
| `description` | `string` |
| `approval_status` | `RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemApprovalStatus` |
| `status` | `RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemStatus` |
| `created_by` | `RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemCreatedBy` |
| `created_at` | `string` |
| `currency_configuration` | `RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemCurrencyConfiguration` |
| `column_totals` | `RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemColumnTotalsItem[]` |

## RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemApprovalStatus
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemApprovalStatus
- Schema ID: schema:anon/582451309c29ca6eebc921556dbb7f9d9d86115c

### Enum

Values: approved, under_review, custom

## RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemColumnTotalsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemColumnTotalsItem
- Schema ID: schema:anon/d5a153f2d64cfe39adc1b8afe0590799df0d6a05
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `total` | `string` |
| `budget_column_id` | `string` |
| `comparison` | `RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemColumnTotalsItemComparison` |

## RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemColumnTotalsItemComparison
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemColumnTotalsItemComparison
- Schema ID: schema:anon/de39a4c0e58eb0300e960fabf7417f6c6407f1f1

### Fields

| Field | Type |
|------|------|
| `value` | `string` |
| `delta` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemCreatedBy
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemCreatedBy
- Schema ID: schema:anon/b8d6f5cfd8a98f8aa119092518d6d13626672081
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `display` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemCurrencyConfiguration
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemCurrencyConfiguration
- Schema ID: schema:anon/19a340b659a9972e27004d8f22acfa77a35f9fd3

### Fields

| Field | Type |
|------|------|
| `currency_iso_code` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemStatus
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdBudgetViewBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemStatus
- Schema ID: schema:anon/634f497cd0adbf099964e4a343b81f4340a90cd2

### Fields
