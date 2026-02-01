# RestV20CompaniesCompanyIdUsersBulkAddPostResponse200DataObject

## RestV20CompaniesCompanyIdUsersBulkAddPostResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdUsersBulkAddPostResponse200
- Schema ID: schema:anon/e61968afdeba9e1672d5d7bf774a818437df9cfd

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdUsersBulkAddPostResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdUsersBulkAddPostResponse200DataItem`
- `RestV20CompaniesCompanyIdUsersBulkAddPostResponse200DataItemEntitiesItem`
- `RestV20CompaniesCompanyIdUsersBulkAddPostResponse200DataItemEntitiesItemProjectsItem`

## RestV20CompaniesCompanyIdUsersBulkAddPostResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkAddPostResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkAddPostResponse200DataItem
- Schema ID: schema:anon/193da5c6d54ce68cb691926fe8963e4e294b8aa1

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV20CompaniesCompanyIdUsersBulkAddPostResponse200DataItemEntitiesItem[]` |

## RestV20CompaniesCompanyIdUsersBulkAddPostResponse200DataItemEntitiesItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkAddPostResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkAddPostResponse200DataItemEntitiesItem
- Schema ID: schema:anon/722c6685e836a93d2cd8c3ddc26b2f4f735e07ea

### Fields

| Field | Type |
|------|------|
| `userId` | `string` |
| `projects` | `RestV20CompaniesCompanyIdUsersBulkAddPostResponse200DataItemEntitiesItemProjectsItem[]` |

## RestV20CompaniesCompanyIdUsersBulkAddPostResponse200DataItemEntitiesItemProjectsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkAddPostResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkAddPostResponse200DataItemEntitiesItemProjectsItem
- Schema ID: schema:anon/2fcdb2eb61897bcc662ab8fbf5715eac1db10880

### Fields

| Field | Type |
|------|------|
| `projectId` | `string` |
| `message` | `string` |
