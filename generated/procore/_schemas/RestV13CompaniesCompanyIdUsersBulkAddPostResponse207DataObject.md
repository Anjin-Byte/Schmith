# RestV13CompaniesCompanyIdUsersBulkAddPostResponse207DataObject

## RestV13CompaniesCompanyIdUsersBulkAddPostResponse207DataObject
- Role: parent
- Schema Name: RestV13CompaniesCompanyIdUsersBulkAddPostResponse207
- Schema ID: schema:anon/e96f10f6d6d79dfab3f3e517f33895922e1d2795

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV13CompaniesCompanyIdUsersBulkAddPostResponse207EntitiesItem[]` |
| `errors` | `RestV13CompaniesCompanyIdUsersBulkAddPostResponse207ErrorsItem[]` |

### Nested Types
- `RestV13CompaniesCompanyIdUsersBulkAddPostResponse207EntitiesItem`
- `RestV13CompaniesCompanyIdUsersBulkAddPostResponse207EntitiesItemProjectsItem`
- `RestV13CompaniesCompanyIdUsersBulkAddPostResponse207ErrorsItem`
- `RestV13CompaniesCompanyIdUsersBulkAddPostResponse207ErrorsItemErrorsItem`

## RestV13CompaniesCompanyIdUsersBulkAddPostResponse207EntitiesItem
- Role: nested
- Parent: RestV13CompaniesCompanyIdUsersBulkAddPostResponse207DataObject
- Schema Name: RestV13CompaniesCompanyIdUsersBulkAddPostResponse207EntitiesItem
- Schema ID: schema:anon/722c6685e836a93d2cd8c3ddc26b2f4f735e07ea

### Fields

| Field | Type |
|------|------|
| `userId` | `string` |
| `projects` | `RestV13CompaniesCompanyIdUsersBulkAddPostResponse207EntitiesItemProjectsItem[]` |

## RestV13CompaniesCompanyIdUsersBulkAddPostResponse207EntitiesItemProjectsItem
- Role: nested
- Parent: RestV13CompaniesCompanyIdUsersBulkAddPostResponse207DataObject
- Schema Name: RestV13CompaniesCompanyIdUsersBulkAddPostResponse207EntitiesItemProjectsItem
- Schema ID: schema:anon/2fcdb2eb61897bcc662ab8fbf5715eac1db10880

### Fields

| Field | Type |
|------|------|
| `projectId` | `string` |
| `message` | `string` |

## RestV13CompaniesCompanyIdUsersBulkAddPostResponse207ErrorsItem
- Role: nested
- Parent: RestV13CompaniesCompanyIdUsersBulkAddPostResponse207DataObject
- Schema Name: RestV13CompaniesCompanyIdUsersBulkAddPostResponse207ErrorsItem
- Schema ID: schema:anon/d96f552f07508578ba0a73a13dd942afbf2e84a3

### Fields

| Field | Type |
|------|------|
| `userId` | `string` |
| `errors` | `RestV13CompaniesCompanyIdUsersBulkAddPostResponse207ErrorsItemErrorsItem[]` |

## RestV13CompaniesCompanyIdUsersBulkAddPostResponse207ErrorsItemErrorsItem
- Role: nested
- Parent: RestV13CompaniesCompanyIdUsersBulkAddPostResponse207DataObject
- Schema Name: RestV13CompaniesCompanyIdUsersBulkAddPostResponse207ErrorsItemErrorsItem
- Schema ID: schema:anon/98cfc701c45d468222e9231dcb677a5d1a79278f

### Fields

| Field | Type |
|------|------|
| `projectId` | `string` |
| `message` | `string` |
