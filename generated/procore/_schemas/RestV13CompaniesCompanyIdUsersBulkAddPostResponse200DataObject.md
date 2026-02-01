# RestV13CompaniesCompanyIdUsersBulkAddPostResponse200DataObject

## RestV13CompaniesCompanyIdUsersBulkAddPostResponse200DataObject
- Role: parent
- Schema Name: RestV13CompaniesCompanyIdUsersBulkAddPostResponse200
- Schema ID: schema:anon/821dd37420be80e654eec432f4e6109cd3f1a8d7

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV13CompaniesCompanyIdUsersBulkAddPostResponse200EntitiesItem[]` |

### Nested Types
- `RestV13CompaniesCompanyIdUsersBulkAddPostResponse200EntitiesItem`
- `RestV13CompaniesCompanyIdUsersBulkAddPostResponse200EntitiesItemProjectsItem`

## RestV13CompaniesCompanyIdUsersBulkAddPostResponse200EntitiesItem
- Role: nested
- Parent: RestV13CompaniesCompanyIdUsersBulkAddPostResponse200DataObject
- Schema Name: RestV13CompaniesCompanyIdUsersBulkAddPostResponse200EntitiesItem
- Schema ID: schema:anon/722c6685e836a93d2cd8c3ddc26b2f4f735e07ea

### Fields

| Field | Type |
|------|------|
| `userId` | `string` |
| `projects` | `RestV13CompaniesCompanyIdUsersBulkAddPostResponse200EntitiesItemProjectsItem[]` |

## RestV13CompaniesCompanyIdUsersBulkAddPostResponse200EntitiesItemProjectsItem
- Role: nested
- Parent: RestV13CompaniesCompanyIdUsersBulkAddPostResponse200DataObject
- Schema Name: RestV13CompaniesCompanyIdUsersBulkAddPostResponse200EntitiesItemProjectsItem
- Schema ID: schema:anon/2fcdb2eb61897bcc662ab8fbf5715eac1db10880

### Fields

| Field | Type |
|------|------|
| `projectId` | `string` |
| `message` | `string` |
