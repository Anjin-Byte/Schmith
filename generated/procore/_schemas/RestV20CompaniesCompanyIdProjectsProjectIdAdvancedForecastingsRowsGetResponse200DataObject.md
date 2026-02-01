# RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetResponse200
- Schema ID: schema:anon/9d252916c0f8b0500d9ff3a0f8e709271fee34b8

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetResponse200DataItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetResponse200DataItemCurve`
- `RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetResponse200DataItemPeriodsItem`

## RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetResponse200DataItem
- Schema ID: schema:anon/2621c8f59751bc8246d96a8dd8b04dc87203b328
- Primary Key: BudgetLineItemId

### Fields

| Field | Type |
|------|------|
| `budget_line_item_id` | `string` |
| `wbs_code_id` | `string` |
| `start_date` | `string` |
| `end_date` | `string` |
| `curve` | `RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetResponse200DataItemCurve` |
| `forecast_to_complete` | `double` |
| `periods` | `RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetResponse200DataItemPeriodsItem[]` |

## RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetResponse200DataItemCurve
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetResponse200DataItemCurve
- Schema ID: schema:anon/147e3b021ff8ce521e2f91d6c174fde2cd8ee8e1

### Enum

Values: bell, back_loaded, front_loaded, linear, manual

## RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetResponse200DataItemPeriodsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetResponse200DataItemPeriodsItem
- Schema ID: schema:anon/25688379bd9217f52ec959421343d38fb596f33c

### Fields

| Field | Type |
|------|------|
| `period_date` | `string` |
| `amount` | `double` |
