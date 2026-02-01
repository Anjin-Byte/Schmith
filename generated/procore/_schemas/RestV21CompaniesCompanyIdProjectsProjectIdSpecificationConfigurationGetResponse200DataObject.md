# RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200DataObject

## RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200DataObject
- Role: parent
- Schema Name: RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200
- Schema ID: schema:anon/4c51f4d6bf90765b6ce45597eff47484cc9091a4

### Fields

| Field | Type |
|------|------|
| `data` | `RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200Data` |

### Nested Types
- `RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200Data`
- `RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200DataSettings`
- `RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200DataSpecificationSubscribers`
- `RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200DataSpecificationSubscribersUsersItem`

## RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200Data
- Role: nested
- Parent: RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200DataObject
- Schema Name: RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200Data
- Schema ID: schema:anon/0bb5cf6b8476faff032ad6442cc5e340aab72dd8

### Fields

| Field | Type |
|------|------|
| `settings` | `RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200DataSettings` |
| `specification_subscribers` | `RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200DataSpecificationSubscribers` |

## RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200DataSettings
- Role: nested
- Parent: RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200DataObject
- Schema Name: RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200DataSettings
- Schema ID: schema:anon/25d2b21e30550bc609b059d98a8b1c72e41656ee

### Fields

| Field | Type |
|------|------|
| `specification_revisions_ordered_by_letter_first` | `bool` |
| `specification_by_area_enabled` | `bool` |
| `specification_by_area_editable` | `bool` |

## RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200DataSpecificationSubscribers
- Role: nested
- Parent: RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200DataObject
- Schema Name: RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200DataSpecificationSubscribers
- Schema ID: schema:anon/975dea192993ebf76b78ec2901faa151885c7633

### Fields

| Field | Type |
|------|------|
| `users` | `RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200DataSpecificationSubscribersUsersItem[]` |

## RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200DataSpecificationSubscribersUsersItem
- Role: nested
- Parent: RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200DataObject
- Schema Name: RestV21CompaniesCompanyIdProjectsProjectIdSpecificationConfigurationGetResponse200DataSpecificationSubscribersUsersItem
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
