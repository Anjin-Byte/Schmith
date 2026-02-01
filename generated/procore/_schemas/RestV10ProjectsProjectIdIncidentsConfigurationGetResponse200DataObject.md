# RestV10ProjectsProjectIdIncidentsConfigurationGetResponse200DataObject

## RestV10ProjectsProjectIdIncidentsConfigurationGetResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdIncidentsConfigurationGetResponse200
- Schema ID: schema:anon/ef555a955caaa944807a30d6a3b97e7513b40a3a
- Primary Key: ProjectId

### Fields

| Field | Type |
|------|------|
| `project_id` | `int` |
| `private_by_default` | `bool` |
| `default_distribution` | `RestV10ProjectsProjectIdIncidentsConfigurationGetResponse200DefaultDistributionItem[]` |

### Nested Types
- `RestV10ProjectsProjectIdIncidentsConfigurationGetResponse200DefaultDistributionItem`

## RestV10ProjectsProjectIdIncidentsConfigurationGetResponse200DefaultDistributionItem
- Role: nested
- Parent: RestV10ProjectsProjectIdIncidentsConfigurationGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdIncidentsConfigurationGetResponse200DefaultDistributionItem
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |
