# PagingResponsePubAccountingCodeDataObject

## PagingResponsePubAccountingCodeDataObject
- Role: parent
- Schema Name: PagingResponsePubAccountingCode
- Schema ID: schema:components/PagingResponsePubAccountingCode

### Fields

| Field | Type |
|------|------|
| `offset` | `int` |
| `limit` | `int` |
| `total` | `int` |
| `data` | `PubAccountingCode[]` |
| `orderData` | `PagingOrderDataResponse[]` |
| `prev` | `string` |
| `next` | `string` |

### Nested Types
- `PagingOrderDataResponse`
- `PagingOrderDataResponseOrderdirection`
- `PubAccountingCode`

## PagingOrderDataResponse
- Role: nested
- Parent: PagingResponsePubAccountingCodeDataObject
- Schema Name: PagingOrderDataResponse
- Schema ID: schema:components/PagingOrderDataResponse

### Fields

| Field | Type |
|------|------|
| `orderBy` | `string` |
| `orderDirection` | `PagingOrderDataResponseOrderdirection` |

## PagingOrderDataResponseOrderdirection
- Role: nested
- Parent: PagingResponsePubAccountingCodeDataObject
- Schema Name: PagingOrderDataResponseOrderdirection
- Schema ID: schema:anon/d005f4d343e3145c9082cdbedab65effe3da2980

### Enum

Values: ASC, DESC

## PubAccountingCode
- Role: nested
- Parent: PagingResponsePubAccountingCodeDataObject
- Schema Name: PubAccountingCode
- Schema ID: schema:components/PubAccountingCode
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |
| `accountCode` | `string` |
| `costCode` | `string` |
| `costCategoryCode` | `string` |
| `costListCode` | `string` |
| `phaseCode` | `string` |
| `jobType` | `string` |
| `entityCode` | `string` |
