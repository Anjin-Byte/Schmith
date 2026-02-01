# RestV20CompaniesCompanyIdProjectStatusSnapshotsBudgetViewsGetResponse200DataObject

## RestV20CompaniesCompanyIdProjectStatusSnapshotsBudgetViewsGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectStatusSnapshotsBudgetViewsGetResponse200
- Schema ID: schema:anon/98449295828de89466c995f45aa7157386c03810

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectStatusSnapshotsBudgetViewsGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectStatusSnapshotsBudgetViewsGetResponse200DataItem`
- `RestV20CompaniesCompanyIdProjectStatusSnapshotsBudgetViewsGetResponse200DataItemCreatedBy`

## RestV20CompaniesCompanyIdProjectStatusSnapshotsBudgetViewsGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectStatusSnapshotsBudgetViewsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectStatusSnapshotsBudgetViewsGetResponse200DataItem
- Schema ID: schema:anon/8fd3e4ea81ce0fe65f9c0e61fd52332aea354262
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |
| `created_by` | `RestV20CompaniesCompanyIdProjectStatusSnapshotsBudgetViewsGetResponse200DataItemCreatedBy` |
| `created_at` | `string` |

## RestV20CompaniesCompanyIdProjectStatusSnapshotsBudgetViewsGetResponse200DataItemCreatedBy
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectStatusSnapshotsBudgetViewsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectStatusSnapshotsBudgetViewsGetResponse200DataItemCreatedBy
- Schema ID: schema:anon/b502539f8628f683a9732f41732ec7d90d4b7a36
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |
