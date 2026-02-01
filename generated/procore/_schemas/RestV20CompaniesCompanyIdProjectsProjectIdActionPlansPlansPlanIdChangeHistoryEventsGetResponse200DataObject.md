# RestV20CompaniesCompanyIdProjectsProjectIdActionPlansPlansPlanIdChangeHistoryEventsGetResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdActionPlansPlansPlanIdChangeHistoryEventsGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdActionPlansPlansPlanIdChangeHistoryEventsGetResponse200
- Schema ID: schema:anon/d439dd29354156ad62add94b2a2e1afbf87d70e4

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdActionPlansPlansPlanIdChangeHistoryEventsGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdActionPlansPlansPlanIdChangeHistoryEventsGetResponse200DataItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdActionPlansPlansPlanIdChangeHistoryEventsGetResponse200DataItemUser`

## RestV20CompaniesCompanyIdProjectsProjectIdActionPlansPlansPlanIdChangeHistoryEventsGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdActionPlansPlansPlanIdChangeHistoryEventsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdActionPlansPlansPlanIdChangeHistoryEventsGetResponse200DataItem
- Schema ID: schema:anon/57273708136181e72a25eb048f4881327c704ed7
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `plan_id` | `string` |
| `event_type` | `string` |
| `event_data` | `object` |
| `user` | `RestV20CompaniesCompanyIdProjectsProjectIdActionPlansPlansPlanIdChangeHistoryEventsGetResponse200DataItemUser` |
| `timestamp` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdActionPlansPlansPlanIdChangeHistoryEventsGetResponse200DataItemUser
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdActionPlansPlansPlanIdChangeHistoryEventsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdActionPlansPlansPlanIdChangeHistoryEventsGetResponse200DataItemUser
- Schema ID: schema:anon/99401da756191be158839294cf26cc40b0feeca0
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `login` | `string` |
| `name` | `string` |
