# RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataObject

## RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200
- Schema ID: schema:anon/acd798d584ee5ff3e54e26fc31fb105ca48c0a49

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItem`
- `RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemApprovalStatus`
- `RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemColumnTotalsItem`
- `RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemCreatedBy`
- `RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemCurrencyConfiguration`
- `RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemProject`
- `RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemStatus`

## RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItem
- Schema ID: schema:anon/f9a9cd6338edcd537462782dc25c26c8cec31ad8
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |
| `description` | `string` |
| `approval_status` | `RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemApprovalStatus` |
| `status` | `RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemStatus` |
| `created_by` | `RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemCreatedBy` |
| `created_at` | `string` |
| `project` | `RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemProject` |
| `currency_configuration` | `RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemCurrencyConfiguration` |
| `column_totals` | `RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemColumnTotalsItem[]` |

## RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemApprovalStatus
- Role: nested
- Parent: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemApprovalStatus
- Schema ID: schema:anon/1ae476602232fdb85b0ce618fafae50df5170263

### Enum

Values: approved, under_review, custom

## RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemColumnTotalsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemColumnTotalsItem
- Schema ID: schema:anon/6a079bedd289ef74de091e69cb52b3d0a7f1758c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `total` | `double` |
| `budget_column_id` | `string` |

## RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemCreatedBy
- Role: nested
- Parent: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemCreatedBy
- Schema ID: schema:anon/8f0c20dddf11f535205b809b7021f36fda059de0
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `display` | `string` |

## RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemCurrencyConfiguration
- Role: nested
- Parent: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemCurrencyConfiguration
- Schema ID: schema:anon/19a340b659a9972e27004d8f22acfa77a35f9fd3

### Fields

| Field | Type |
|------|------|
| `currency_iso_code` | `string` |

## RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemProject
- Role: nested
- Parent: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemProject
- Schema ID: schema:anon/648c531e281ec334aad0764484f502d0a195a8e7
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |

## RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemStatus
- Role: nested
- Parent: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdBudgetViewsBudgetViewIdProjectStatusSnapshotsGetResponse200DataItemStatus
- Schema ID: schema:anon/634f497cd0adbf099964e4a343b81f4340a90cd2

### Fields
