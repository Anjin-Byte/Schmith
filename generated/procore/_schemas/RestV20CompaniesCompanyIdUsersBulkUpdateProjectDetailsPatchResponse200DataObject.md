# RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse200DataObject

## RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse200
- Schema ID: schema:anon/060f95647ac5b1fcf76854126d63bceca7b0aadb

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse200DataItem`
- `RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse200DataItemEntitiesItem`
- `RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse200DataItemEntitiesItemProjectsItem`

## RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse200DataItem
- Schema ID: schema:anon/30aaa05a784cc8835103e84fa410f6f957f5e6c8

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse200DataItemEntitiesItem[]` |

## RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse200DataItemEntitiesItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse200DataItemEntitiesItem
- Schema ID: schema:anon/222154e93ba5616158820a1efbd4d8e42014ae88

### Fields

| Field | Type |
|------|------|
| `userId` | `string` |
| `projects` | `RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse200DataItemEntitiesItemProjectsItem[]` |

## RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse200DataItemEntitiesItemProjectsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse200DataItemEntitiesItemProjectsItem
- Schema ID: schema:anon/89ccc6927314848d68eb692c77c90552df7cc425

### Fields

| Field | Type |
|------|------|
| `projectId` | `string` |
| `message` | `string[]` |
