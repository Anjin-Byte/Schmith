# RestV20CompaniesCompanyIdUsersBulkAddPostResponse207DataObject

## RestV20CompaniesCompanyIdUsersBulkAddPostResponse207DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdUsersBulkAddPostResponse207
- Schema ID: schema:anon/d0954257af92972fe73a2b65e41c7fbf0821796f

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdUsersBulkAddPostResponse207DataItem[]` |
| `errors` | `RestV20CompaniesCompanyIdUsersBulkAddPostResponse207ErrorsItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdUsersBulkAddPostResponse207DataItem`
- `RestV20CompaniesCompanyIdUsersBulkAddPostResponse207DataItemEntitiesItem`
- `RestV20CompaniesCompanyIdUsersBulkAddPostResponse207DataItemEntitiesItemProjectsItem`
- `RestV20CompaniesCompanyIdUsersBulkAddPostResponse207ErrorsItem`
- `RestV20CompaniesCompanyIdUsersBulkAddPostResponse207ErrorsItemErrorsItem`

## RestV20CompaniesCompanyIdUsersBulkAddPostResponse207DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkAddPostResponse207DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkAddPostResponse207DataItem
- Schema ID: schema:anon/34358a154f694f7e96d1302cf57b5d965bb6efff

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV20CompaniesCompanyIdUsersBulkAddPostResponse207DataItemEntitiesItem[]` |

## RestV20CompaniesCompanyIdUsersBulkAddPostResponse207DataItemEntitiesItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkAddPostResponse207DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkAddPostResponse207DataItemEntitiesItem
- Schema ID: schema:anon/722c6685e836a93d2cd8c3ddc26b2f4f735e07ea

### Fields

| Field | Type |
|------|------|
| `userId` | `string` |
| `projects` | `RestV20CompaniesCompanyIdUsersBulkAddPostResponse207DataItemEntitiesItemProjectsItem[]` |

## RestV20CompaniesCompanyIdUsersBulkAddPostResponse207DataItemEntitiesItemProjectsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkAddPostResponse207DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkAddPostResponse207DataItemEntitiesItemProjectsItem
- Schema ID: schema:anon/2fcdb2eb61897bcc662ab8fbf5715eac1db10880

### Fields

| Field | Type |
|------|------|
| `projectId` | `string` |
| `message` | `string` |

## RestV20CompaniesCompanyIdUsersBulkAddPostResponse207ErrorsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkAddPostResponse207DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkAddPostResponse207ErrorsItem
- Schema ID: schema:anon/d96f552f07508578ba0a73a13dd942afbf2e84a3

### Fields

| Field | Type |
|------|------|
| `userId` | `string` |
| `errors` | `RestV20CompaniesCompanyIdUsersBulkAddPostResponse207ErrorsItemErrorsItem[]` |

## RestV20CompaniesCompanyIdUsersBulkAddPostResponse207ErrorsItemErrorsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkAddPostResponse207DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkAddPostResponse207ErrorsItemErrorsItem
- Schema ID: schema:anon/98cfc701c45d468222e9231dcb677a5d1a79278f

### Fields

| Field | Type |
|------|------|
| `projectId` | `string` |
| `message` | `string` |
