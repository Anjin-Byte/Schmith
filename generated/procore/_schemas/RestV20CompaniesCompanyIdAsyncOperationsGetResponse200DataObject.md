# RestV20CompaniesCompanyIdAsyncOperationsGetResponse200DataObject

## RestV20CompaniesCompanyIdAsyncOperationsGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdAsyncOperationsGetResponse200
- Schema ID: schema:anon/43429e2263e431e39cd71b03ec87e0424f27163d

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdAsyncOperationsGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdAsyncOperationsGetResponse200DataItem`
- `RestV20CompaniesCompanyIdAsyncOperationsGetResponse200DataItemError`
- `RestV20CompaniesCompanyIdAsyncOperationsGetResponse200DataItemStatus`

## RestV20CompaniesCompanyIdAsyncOperationsGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdAsyncOperationsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdAsyncOperationsGetResponse200DataItem
- Schema ID: schema:anon/1b41226f022c8a01b8e81d28658d05161034dd39
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `operation_type` | `string` |
| `started_at` | `string` |
| `completed_at` | `string` |
| `status` | `RestV20CompaniesCompanyIdAsyncOperationsGetResponse200DataItemStatus` |
| `error` | `RestV20CompaniesCompanyIdAsyncOperationsGetResponse200DataItemError` |
| `result` | `object` |
| `context` | `object` |
| `created_by_id` | `string` |

## RestV20CompaniesCompanyIdAsyncOperationsGetResponse200DataItemError
- Role: nested
- Parent: RestV20CompaniesCompanyIdAsyncOperationsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdAsyncOperationsGetResponse200DataItemError
- Schema ID: schema:anon/1f493fdae564aaecf81c96b038067c84f6a5c513

### Fields

| Field | Type |
|------|------|
| `message` | `string` |

## RestV20CompaniesCompanyIdAsyncOperationsGetResponse200DataItemStatus
- Role: nested
- Parent: RestV20CompaniesCompanyIdAsyncOperationsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdAsyncOperationsGetResponse200DataItemStatus
- Schema ID: schema:anon/578cd0f1de41867e8228c6dcd4527ecfdc1adae0

### Enum

Values: created, in_progress, done, failed
