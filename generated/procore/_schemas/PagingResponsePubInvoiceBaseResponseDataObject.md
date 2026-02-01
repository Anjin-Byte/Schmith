# PagingResponsePubInvoiceBaseResponseDataObject

## PagingResponsePubInvoiceBaseResponseDataObject
- Role: parent
- Schema Name: PagingResponsePubInvoiceBaseResponse
- Schema ID: schema:components/PagingResponsePubInvoiceBaseResponse

### Fields

| Field | Type |
|------|------|
| `offset` | `int` |
| `limit` | `int` |
| `total` | `int` |
| `data` | `PubInvoiceBaseResponse[]` |
| `orderData` | `PagingOrderDataResponse[]` |
| `prev` | `string` |
| `next` | `string` |

### Nested Types
- `PagingOrderDataResponse`
- `PagingOrderDataResponseOrderdirection`
- `PubInvoiceBaseResponse`
- `PubInvoiceBaseResponseStatus`

## PagingOrderDataResponse
- Role: nested
- Parent: PagingResponsePubInvoiceBaseResponseDataObject
- Schema Name: PagingOrderDataResponse
- Schema ID: schema:components/PagingOrderDataResponse

### Fields

| Field | Type |
|------|------|
| `orderBy` | `string` |
| `orderDirection` | `PagingOrderDataResponseOrderdirection` |

## PagingOrderDataResponseOrderdirection
- Role: nested
- Parent: PagingResponsePubInvoiceBaseResponseDataObject
- Schema Name: PagingOrderDataResponseOrderdirection
- Schema ID: schema:anon/d005f4d343e3145c9082cdbedab65effe3da2980

### Enum

Values: ASC, DESC

## PubInvoiceBaseResponse
- Role: nested
- Parent: PagingResponsePubInvoiceBaseResponseDataObject
- Schema Name: PubInvoiceBaseResponse
- Schema ID: schema:components/PubInvoiceBaseResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `invoiceValue` | `double` |
| `title` | `string` |
| `dateIssued` | `string` |
| `contractId` | `int` |
| `dateCreated` | `string` |
| `dateUpdated` | `string` |
| `description` | `string` |
| `status` | `PubInvoiceBaseResponseStatus` |
| `invoiceNumber` | `int` |
| `invoiceNumberAlphanumeric` | `string` |
| `periodStart` | `string` |
| `periodEnd` | `string` |
| `reason` | `string` |
| `isReleaseRetentionInvoice` | `bool` |
| `isCreatedByVendor` | `bool` |
| `dateApproved` | `string` |
| `invoiceCode` | `string` |

## PubInvoiceBaseResponseStatus
- Role: nested
- Parent: PagingResponsePubInvoiceBaseResponseDataObject
- Schema Name: PubInvoiceBaseResponseStatus
- Schema ID: schema:anon/ba27824ebdb9cfe0f2a4d626c06e741c56aeb6d9

### Enum

Values: pending, approved, rejected, reviewed
