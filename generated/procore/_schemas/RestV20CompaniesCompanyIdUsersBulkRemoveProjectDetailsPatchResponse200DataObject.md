# RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse200DataObject

## RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse200
- Schema ID: schema:anon/f44759ae7d834c058b9ba20e1e6e3b1027c87b75

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse200DataItem`
- `RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse200DataItemEntitiesItem`
- `RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse200DataItemEntitiesItemProjectsItem`

## RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse200DataItem
- Schema ID: schema:anon/cbf573d38743679c140a704fdd5079e64af354e4

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse200DataItemEntitiesItem[]` |

## RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse200DataItemEntitiesItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse200DataItemEntitiesItem
- Schema ID: schema:anon/977fcaa1456137b0298657adae26516dc3e4e0d5

### Fields

| Field | Type |
|------|------|
| `userId` | `string` |
| `projects` | `RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse200DataItemEntitiesItemProjectsItem[]` |

## RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse200DataItemEntitiesItemProjectsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse200DataItemEntitiesItemProjectsItem
- Schema ID: schema:anon/b4e100907a99ff7653ed8c9d1d6ada6b64eb8878

### Fields

| Field | Type |
|------|------|
| `projectId` | `string` |
| `message` | `string` |
