# RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataObject

## RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200
- Schema ID: schema:anon/d0ddd8099c364c8d6d4ff3f95ce8d668232e587b

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200Data` |

### Nested Types
- `RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200Data`
- `RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataError`
- `RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataStatus`
- `RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataSubOperationsItem`
- `RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataSubOperationsItemError`
- `RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataSubOperationsItemStatus`

## RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200Data
- Role: nested
- Parent: RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200Data
- Schema ID: schema:anon/973ce930b10259bdfdbe8391f4342ec47a36590b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `operation_type` | `string` |
| `started_at` | `string` |
| `completed_at` | `string` |
| `status` | `RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataStatus` |
| `error` | `RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataError` |
| `result` | `object` |
| `context` | `object` |
| `created_by_id` | `string` |
| `sub_operations` | `RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataSubOperationsItem[]` |

## RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataError
- Role: nested
- Parent: RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataError
- Schema ID: schema:anon/1f493fdae564aaecf81c96b038067c84f6a5c513

### Fields

| Field | Type |
|------|------|
| `message` | `string` |

## RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataStatus
- Role: nested
- Parent: RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataStatus
- Schema ID: schema:anon/578cd0f1de41867e8228c6dcd4527ecfdc1adae0

### Enum

Values: created, in_progress, done, failed

## RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataSubOperationsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataSubOperationsItem
- Schema ID: schema:anon/f2262cafca63bb7874ca78050f104384be2ed36a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `sub_operation_type` | `string` |
| `started_at` | `string` |
| `completed_at` | `string` |
| `status` | `RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataSubOperationsItemStatus` |
| `error` | `RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataSubOperationsItemError` |
| `result` | `object` |
| `context` | `object` |

## RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataSubOperationsItemError
- Role: nested
- Parent: RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataSubOperationsItemError
- Schema ID: schema:anon/abb1e0a580342a9592ed71906ea561fdf6bd2b8a

### Fields

| Field | Type |
|------|------|
| `message` | `string` |

## RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataSubOperationsItemStatus
- Role: nested
- Parent: RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdAsyncOperationsOperationIdGetResponse200DataSubOperationsItemStatus
- Schema ID: schema:anon/2f1c5e1c078348808625a1f23d1fcd7acfd8d6bb

### Enum

Values: created, enqueued, in_progress, done, failed, retry, partial_done
