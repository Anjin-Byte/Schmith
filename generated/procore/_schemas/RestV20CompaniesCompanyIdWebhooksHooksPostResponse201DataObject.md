# RestV20CompaniesCompanyIdWebhooksHooksPostResponse201DataObject

## RestV20CompaniesCompanyIdWebhooksHooksPostResponse201DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdWebhooksHooksPostResponse201
- Schema ID: schema:anon/afed14fb5809859c4e008ade895f25ac0e230036

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdWebhooksHooksPostResponse201Data` |

### Nested Types
- `RestV20CompaniesCompanyIdWebhooksHooksPostResponse201Data`
- `RestV20CompaniesCompanyIdWebhooksHooksPostResponse201DataDestinationHeaders`
- `RestV20CompaniesCompanyIdWebhooksHooksPostResponse201DataStatus`

## RestV20CompaniesCompanyIdWebhooksHooksPostResponse201Data
- Role: nested
- Parent: RestV20CompaniesCompanyIdWebhooksHooksPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdWebhooksHooksPostResponse201Data
- Schema ID: schema:anon/5dea1ea13a3c50b9082ff8cf124e0dfb3b8ddb80
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `status` | `RestV20CompaniesCompanyIdWebhooksHooksPostResponse201DataStatus` |
| `payload_version` | `string` |
| `namespace` | `string` |
| `destination_headers` | `RestV20CompaniesCompanyIdWebhooksHooksPostResponse201DataDestinationHeaders` |
| `destination_url` | `string` |
| `trigger_count` | `int` |
| `company_id` | `string` |
| `project_id` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV20CompaniesCompanyIdWebhooksHooksPostResponse201DataDestinationHeaders
- Role: nested
- Parent: RestV20CompaniesCompanyIdWebhooksHooksPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdWebhooksHooksPostResponse201DataDestinationHeaders
- Schema ID: schema:anon/7bec2ce0e306af770e44491f31e1b2a6b25bfee3

### Fields

| Field | Type |
|------|------|
| `Authorization` | `string` |

## RestV20CompaniesCompanyIdWebhooksHooksPostResponse201DataStatus
- Role: nested
- Parent: RestV20CompaniesCompanyIdWebhooksHooksPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdWebhooksHooksPostResponse201DataStatus
- Schema ID: schema:anon/0182e139a2ad57f40f5e427830772f6b5876b8d1

### Enum

Values: active, disabled
