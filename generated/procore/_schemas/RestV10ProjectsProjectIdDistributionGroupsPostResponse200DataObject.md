# RestV10ProjectsProjectIdDistributionGroupsPostResponse200DataObject

## RestV10ProjectsProjectIdDistributionGroupsPostResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdDistributionGroupsPostResponse200
- Schema ID: schema:anon/f9c772f6b568e8c36a5c3d3424193d7b97f2b6df
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `description` | `string` |
| `name` | `string` |
| `users` | `RestV10ProjectsProjectIdDistributionGroupsPostResponse200UsersItem[]` |

### Nested Types
- `RestV10ProjectsProjectIdDistributionGroupsPostResponse200UsersItem`

## RestV10ProjectsProjectIdDistributionGroupsPostResponse200UsersItem
- Role: nested
- Parent: RestV10ProjectsProjectIdDistributionGroupsPostResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDistributionGroupsPostResponse200UsersItem
- Schema ID: schema:anon/083aa8287566ef7b95c7c1c56376d445c11f05a8
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `company_name` | `string` |
| `login` | `string` |
| `imageUrl` | `string` |
| `initials` | `string` |
| `job_title` | `string` |
