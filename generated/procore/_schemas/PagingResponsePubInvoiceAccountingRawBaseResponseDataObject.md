# PagingResponsePubInvoiceAccountingRawBaseResponseDataObject

## PagingResponsePubInvoiceAccountingRawBaseResponseDataObject
- Role: parent
- Schema Name: PagingResponsePubInvoiceAccountingRawBaseResponse
- Schema ID: schema:components/PagingResponsePubInvoiceAccountingRawBaseResponse

### Fields

| Field | Type |
|------|------|
| `offset` | `int` |
| `limit` | `int` |
| `total` | `int` |
| `data` | `PubInvoiceAccountingRawBaseResponse[]` |
| `orderData` | `PagingOrderDataResponse[]` |
| `prev` | `string` |
| `next` | `string` |

### Nested Types
- `PagingOrderDataResponse`
- `PagingOrderDataResponseOrderdirection`
- `PubInvoiceAccountingRawBaseResponse`
- `PubInvoiceAccountingRawBaseResponseStatus`
- `PubInvoiceAccountingRawBaseResponseType`

## PagingOrderDataResponse
- Role: nested
- Parent: PagingResponsePubInvoiceAccountingRawBaseResponseDataObject
- Schema Name: PagingOrderDataResponse
- Schema ID: schema:components/PagingOrderDataResponse

### Fields

| Field | Type |
|------|------|
| `orderBy` | `string` |
| `orderDirection` | `PagingOrderDataResponseOrderdirection` |

## PagingOrderDataResponseOrderdirection
- Role: nested
- Parent: PagingResponsePubInvoiceAccountingRawBaseResponseDataObject
- Schema Name: PagingOrderDataResponseOrderdirection
- Schema ID: schema:anon/d005f4d343e3145c9082cdbedab65effe3da2980

### Enum

Values: ASC, DESC

## PubInvoiceAccountingRawBaseResponse
- Role: nested
- Parent: PagingResponsePubInvoiceAccountingRawBaseResponseDataObject
- Schema Name: PubInvoiceAccountingRawBaseResponse
- Schema ID: schema:components/PubInvoiceAccountingRawBaseResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `invoiceNumber` | `string` |
| `amount` | `double` |
| `valueOrig` | `double` |
| `type` | `PubInvoiceAccountingRawBaseResponseType` |
| `buildingCode` | `string` |
| `jobCode` | `string` |
| `vendorCode` | `string` |
| `invoiceDate` | `string` |
| `period` | `string` |
| `source` | `string` |
| `status` | `PubInvoiceAccountingRawBaseResponseStatus` |
| `contractCode` | `string` |
| `costCode` | `string` |
| `costCodeName` | `string` |
| `description` | `string` |
| `invoiceCode` | `string` |
| `dateCreated` | `string` |
| `dateUpdated` | `string` |

## PubInvoiceAccountingRawBaseResponseStatus
- Role: nested
- Parent: PagingResponsePubInvoiceAccountingRawBaseResponseDataObject
- Schema Name: PubInvoiceAccountingRawBaseResponseStatus
- Schema ID: schema:anon/fd59d309968793604d7575cab61f7b300fc8fbe7

### Enum

Values: PENDING, POSTED, RELEASED, PAID, UNUSED, VOID, REVERSED, DELETED

## PubInvoiceAccountingRawBaseResponseType
- Role: nested
- Parent: PagingResponsePubInvoiceAccountingRawBaseResponseDataObject
- Schema Name: PubInvoiceAccountingRawBaseResponseType
- Schema ID: schema:anon/cd432c5c6bd43aaa070aa268d1f585a78a335e25

### Enum

Values: YARDI_INVOICE, MRI_INVOICE, GENERIC_ACCOUNTING_INVOICE, IBS_INVOICE_DETAIL, IBS_CONTRACT_DETAIL, JDE_INVOICE, MRI_JOURNAL_ENTRY, YARDI_JOURNAL_ENTRY, PUB_API_INVOICE
