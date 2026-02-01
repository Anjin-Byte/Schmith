# RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataObject

## RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207
- Schema ID: schema:anon/50ba814e8d17d7cf897eb3e4dda4ab2e1dd14f20

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataItem`
- `RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataItemEntitiesItem`
- `RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataItemEntitiesItemProjectsItem`
- `RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataItemErrorsItem`
- `RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataItemErrorsItemErrorsItem`

## RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataItem
- Schema ID: schema:anon/d985afa3d081ea9e7d75750e8a330b57b8fcdaad

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataItemEntitiesItem[]` |
| `errors` | `RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataItemErrorsItem[]` |

## RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataItemEntitiesItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataItemEntitiesItem
- Schema ID: schema:anon/a428add439337e15006a0d1afac0f9ef7202a3a4

### Fields

| Field | Type |
|------|------|
| `userId` | `string` |
| `projects` | `RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataItemEntitiesItemProjectsItem[]` |

## RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataItemEntitiesItemProjectsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataItemEntitiesItemProjectsItem
- Schema ID: schema:anon/863d72042bcfef43495ad388549acd6ed80a0de0

### Fields

| Field | Type |
|------|------|
| `projectId` | `string` |
| `message` | `string` |

## RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataItemErrorsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataItemErrorsItem
- Schema ID: schema:anon/50fe840f51f47480ea5ed95dbd5666c7705dbbb2

### Fields

| Field | Type |
|------|------|
| `userId` | `string` |
| `errors` | `RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataItemErrorsItemErrorsItem[]` |

## RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataItemErrorsItemErrorsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkUpdateProjectDetailsPatchResponse207DataItemErrorsItemErrorsItem
- Schema ID: schema:anon/402255be4ca651d238cad6b8abee177b9b24900d

### Fields

| Field | Type |
|------|------|
| `projectId` | `string` |
| `message` | `string` |
