# RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataObject

## RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207
- Schema ID: schema:anon/1acabc60f2350b0a02f61eb2a24814ccdc28a970

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataItem`
- `RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataItemEntitiesItem`
- `RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataItemEntitiesItemProjectsItem`
- `RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataItemErrorsItem`
- `RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataItemErrorsItemErrorsItem`

## RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataItem
- Schema ID: schema:anon/bbd0c36158e204364e5377eb4b21cc983c8ee901

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataItemEntitiesItem[]` |
| `errors` | `RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataItemErrorsItem[]` |

## RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataItemEntitiesItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataItemEntitiesItem
- Schema ID: schema:anon/34a13b865fb109580ddab330cadc70f2c8b1b142

### Fields

| Field | Type |
|------|------|
| `userId` | `string` |
| `projects` | `RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataItemEntitiesItemProjectsItem[]` |

## RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataItemEntitiesItemProjectsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataItemEntitiesItemProjectsItem
- Schema ID: schema:anon/b4e100907a99ff7653ed8c9d1d6ada6b64eb8878

### Fields

| Field | Type |
|------|------|
| `projectId` | `string` |
| `message` | `string` |

## RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataItemErrorsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataItemErrorsItem
- Schema ID: schema:anon/161f988e7d45caead3fbf246a8dd942496408f8d

### Fields

| Field | Type |
|------|------|
| `userId` | `string` |
| `errors` | `RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataItemErrorsItemErrorsItem[]` |

## RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataItemErrorsItemErrorsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataObject
- Schema Name: RestV20CompaniesCompanyIdUsersBulkRemoveProjectDetailsPatchResponse207DataItemErrorsItemErrorsItem
- Schema ID: schema:anon/1136af239a36dbbace907f86087a8950b17659a4

### Fields

| Field | Type |
|------|------|
| `projectId` | `string` |
| `message` | `string` |
