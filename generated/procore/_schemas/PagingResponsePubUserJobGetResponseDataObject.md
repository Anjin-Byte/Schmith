# PagingResponsePubUserJobGetResponseDataObject

## PagingResponsePubUserJobGetResponseDataObject
- Role: parent
- Schema Name: PagingResponsePubUserJobGetResponse
- Schema ID: schema:components/PagingResponsePubUserJobGetResponse

### Fields

| Field | Type |
|------|------|
| `offset` | `int` |
| `limit` | `int` |
| `total` | `int` |
| `data` | `PubUserJobGetResponse[]` |
| `orderData` | `PagingOrderDataResponse[]` |
| `prev` | `string` |
| `next` | `string` |

### Nested Types
- `PagingOrderDataResponse`
- `PagingOrderDataResponseOrderdirection`
- `PubUserJobGetResponse`
- `PubUserJobGetResponseUserjobrole`

## PagingOrderDataResponse
- Role: nested
- Parent: PagingResponsePubUserJobGetResponseDataObject
- Schema Name: PagingOrderDataResponse
- Schema ID: schema:components/PagingOrderDataResponse

### Fields

| Field | Type |
|------|------|
| `orderBy` | `string` |
| `orderDirection` | `PagingOrderDataResponseOrderdirection` |

## PagingOrderDataResponseOrderdirection
- Role: nested
- Parent: PagingResponsePubUserJobGetResponseDataObject
- Schema Name: PagingOrderDataResponseOrderdirection
- Schema ID: schema:anon/d005f4d343e3145c9082cdbedab65effe3da2980

### Enum

Values: ASC, DESC

## PubUserJobGetResponse
- Role: nested
- Parent: PagingResponsePubUserJobGetResponseDataObject
- Schema Name: PubUserJobGetResponse
- Schema ID: schema:components/PubUserJobGetResponse

### Fields

| Field | Type |
|------|------|
| `userEmail` | `string` |
| `firstName` | `string` |
| `lastName` | `string` |
| `title` | `string` |
| `userId` | `int` |
| `userLastLogin` | `string` |
| `jobId` | `int` |
| `userJobRole` | `PubUserJobGetResponseUserjobrole` |

## PubUserJobGetResponseUserjobrole
- Role: nested
- Parent: PagingResponsePubUserJobGetResponseDataObject
- Schema Name: PubUserJobGetResponseUserjobrole
- Schema ID: schema:anon/55df94d215c00f01c9d89f9e33494439ab87b7a3

### Enum

Values: admin, collaborator
