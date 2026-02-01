# RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGetResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGetResponse200
- Schema ID: schema:anon/add8d21ab31e2a669c6302939840287728af5d1d

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGetResponse200DataItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGetResponse200DataItemBudgetChangeStatus`
- `RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGetResponse200DataItemType`

## RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGetResponse200DataItem
- Schema ID: schema:anon/dcbbd0f28121514ff85150d58a89f55e9c58e64f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `adjustment_number` | `int` |
| `wbs_code_id` | `string` |
| `amount` | `double` |
| `uom` | `string` |
| `quantity` | `double` |
| `description` | `string` |
| `type` | `RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGetResponse200DataItemType` |
| `budget_change_number` | `string` |
| `budget_change_status` | `RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGetResponse200DataItemBudgetChangeStatus` |
| `budget_change_name` | `string` |
| `budget_change_id` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGetResponse200DataItemBudgetChangeStatus
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGetResponse200DataItemBudgetChangeStatus
- Schema ID: schema:anon/3b9d3ee731645d69e2f139157c244043be334d5f

### Enum

Values: approved, draft, under_review, void

## RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGetResponse200DataItemType
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGetResponse200DataItemType
- Schema ID: schema:anon/2e50175e3e0e53374d99ccd37d9462c2ec380650

### Enum

Values: change_event, budget_change
