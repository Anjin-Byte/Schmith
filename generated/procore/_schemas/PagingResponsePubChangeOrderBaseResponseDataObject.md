# PagingResponsePubChangeOrderBaseResponseDataObject

## PagingResponsePubChangeOrderBaseResponseDataObject
- Role: parent
- Schema Name: PagingResponsePubChangeOrderBaseResponse
- Schema ID: schema:components/PagingResponsePubChangeOrderBaseResponse

### Fields

| Field | Type |
|------|------|
| `offset` | `int` |
| `limit` | `int` |
| `total` | `int` |
| `data` | `PubChangeOrderBaseResponse[]` |
| `orderData` | `PagingOrderDataResponse[]` |
| `prev` | `string` |
| `next` | `string` |

### Nested Types
- `PagingOrderDataResponse`
- `PagingOrderDataResponseOrderdirection`
- `PubChangeOrderBaseResponse`
- `PubChangeOrderBaseResponseStatus`

## PagingOrderDataResponse
- Role: nested
- Parent: PagingResponsePubChangeOrderBaseResponseDataObject
- Schema Name: PagingOrderDataResponse
- Schema ID: schema:components/PagingOrderDataResponse

### Fields

| Field | Type |
|------|------|
| `orderBy` | `string` |
| `orderDirection` | `PagingOrderDataResponseOrderdirection` |

## PagingOrderDataResponseOrderdirection
- Role: nested
- Parent: PagingResponsePubChangeOrderBaseResponseDataObject
- Schema Name: PagingOrderDataResponseOrderdirection
- Schema ID: schema:anon/d005f4d343e3145c9082cdbedab65effe3da2980

### Enum

Values: ASC, DESC

## PubChangeOrderBaseResponse
- Role: nested
- Parent: PagingResponsePubChangeOrderBaseResponseDataObject
- Schema Name: PubChangeOrderBaseResponse
- Schema ID: schema:components/PubChangeOrderBaseResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `title` | `string` |
| `changeOrderNumber` | `int` |
| `changeOrderValue` | `double` |
| `reason` | `string` |
| `contractId` | `int` |
| `dateApproved` | `string` |
| `dateCreated` | `string` |
| `dateUpdated` | `string` |
| `status` | `PubChangeOrderBaseResponseStatus` |
| `description` | `string` |
| `changeOrderCode` | `string` |

## PubChangeOrderBaseResponseStatus
- Role: nested
- Parent: PagingResponsePubChangeOrderBaseResponseDataObject
- Schema Name: PubChangeOrderBaseResponseStatus
- Schema ID: schema:anon/1353e159f3139f31dfbb5a96623dcf1f1d192b82

### Enum

Values: pending, approved, rejected, closed, potential, reviewed
