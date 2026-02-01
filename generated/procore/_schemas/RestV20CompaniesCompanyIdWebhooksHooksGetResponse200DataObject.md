# RestV20CompaniesCompanyIdWebhooksHooksGetResponse200DataObject

## RestV20CompaniesCompanyIdWebhooksHooksGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdWebhooksHooksGetResponse200
- Schema ID: schema:anon/9c24515ac07d3f25cdd23ed248dbb8842ffc7f34

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdWebhooksHooksGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdWebhooksHooksGetResponse200DataItem`
- `RestV20CompaniesCompanyIdWebhooksHooksGetResponse200DataItemDestinationHeaders`
- `RestV20CompaniesCompanyIdWebhooksHooksGetResponse200DataItemStatus`

## RestV20CompaniesCompanyIdWebhooksHooksGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdWebhooksHooksGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWebhooksHooksGetResponse200DataItem
- Schema ID: schema:anon/5dea1ea13a3c50b9082ff8cf124e0dfb3b8ddb80
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `status` | `RestV20CompaniesCompanyIdWebhooksHooksGetResponse200DataItemStatus` |
| `payload_version` | `string` |
| `namespace` | `string` |
| `destination_headers` | `RestV20CompaniesCompanyIdWebhooksHooksGetResponse200DataItemDestinationHeaders` |
| `destination_url` | `string` |
| `trigger_count` | `int` |
| `company_id` | `string` |
| `project_id` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV20CompaniesCompanyIdWebhooksHooksGetResponse200DataItemDestinationHeaders
- Role: nested
- Parent: RestV20CompaniesCompanyIdWebhooksHooksGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWebhooksHooksGetResponse200DataItemDestinationHeaders
- Schema ID: schema:anon/7bec2ce0e306af770e44491f31e1b2a6b25bfee3

### Fields

| Field | Type |
|------|------|
| `Authorization` | `string` |

## RestV20CompaniesCompanyIdWebhooksHooksGetResponse200DataItemStatus
- Role: nested
- Parent: RestV20CompaniesCompanyIdWebhooksHooksGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWebhooksHooksGetResponse200DataItemStatus
- Schema ID: schema:anon/0182e139a2ad57f40f5e427830772f6b5876b8d1

### Enum

Values: active, disabled
