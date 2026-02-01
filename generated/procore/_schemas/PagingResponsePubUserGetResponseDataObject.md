# PagingResponsePubUserGetResponseDataObject

## PagingResponsePubUserGetResponseDataObject
- Role: parent
- Schema Name: PagingResponsePubUserGetResponse
- Schema ID: schema:components/PagingResponsePubUserGetResponse

### Fields

| Field | Type |
|------|------|
| `offset` | `int` |
| `limit` | `int` |
| `total` | `int` |
| `data` | `PubUserGetResponse[]` |
| `orderData` | `PagingOrderDataResponse[]` |
| `prev` | `string` |
| `next` | `string` |

### Nested Types
- `PagingOrderDataResponse`
- `PagingOrderDataResponseOrderdirection`
- `PubUserGetResponse`
- `PubUserGetResponseUsercompanyrole`

## PagingOrderDataResponse
- Role: nested
- Parent: PagingResponsePubUserGetResponseDataObject
- Schema Name: PagingOrderDataResponse
- Schema ID: schema:components/PagingOrderDataResponse

### Fields

| Field | Type |
|------|------|
| `orderBy` | `string` |
| `orderDirection` | `PagingOrderDataResponseOrderdirection` |

## PagingOrderDataResponseOrderdirection
- Role: nested
- Parent: PagingResponsePubUserGetResponseDataObject
- Schema Name: PagingOrderDataResponseOrderdirection
- Schema ID: schema:anon/d005f4d343e3145c9082cdbedab65effe3da2980

### Enum

Values: ASC, DESC

## PubUserGetResponse
- Role: nested
- Parent: PagingResponsePubUserGetResponseDataObject
- Schema Name: PubUserGetResponse
- Schema ID: schema:components/PubUserGetResponse

### Fields

| Field | Type |
|------|------|
| `userEmail` | `string` |
| `firstName` | `string` |
| `lastName` | `string` |
| `title` | `string` |
| `userId` | `int` |
| `userLastLogin` | `string` |
| `userCompanyRole` | `PubUserGetResponseUsercompanyrole` |

## PubUserGetResponseUsercompanyrole
- Role: nested
- Parent: PagingResponsePubUserGetResponseDataObject
- Schema Name: PubUserGetResponseUsercompanyrole
- Schema ID: schema:anon/13c38b99624adde11456c3cc928d62a2c62e9967

### Enum

Values: admin, team, collaborator
