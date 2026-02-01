# RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationDistributionGroupsGetResponse200DataObject

## RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationDistributionGroupsGetResponse200DataObject
- Role: parent
- Schema Name: RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationDistributionGroupsGetResponse200
- Schema ID: schema:anon/70279dbf17b15d17d3a7730501d48e2c182e0223

### Fields

| Field | Type |
|------|------|
| `data` | `RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationDistributionGroupsGetResponse200DataItem[]` |

### Nested Types
- `RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationDistributionGroupsGetResponse200DataItem`
- `RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationDistributionGroupsGetResponse200DataItemUsersItem`

## RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationDistributionGroupsGetResponse200DataItem
- Role: nested
- Parent: RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationDistributionGroupsGetResponse200DataObject
- Schema Name: RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationDistributionGroupsGetResponse200DataItem
- Schema ID: schema:anon/82ffc61e8fced4a0bfc2daa65a38a2c376c97144
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |
| `description` | `string` |
| `users` | `RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationDistributionGroupsGetResponse200DataItemUsersItem[]` |

## RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationDistributionGroupsGetResponse200DataItemUsersItem
- Role: nested
- Parent: RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationDistributionGroupsGetResponse200DataObject
- Schema Name: RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationDistributionGroupsGetResponse200DataItemUsersItem
- Schema ID: schema:anon/3a637753b644da562fe2cdc949d855b9a85f7d72
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `company_name` | `string` |
| `locale` | `string` |
| `login` | `string` |
| `name` | `string` |
