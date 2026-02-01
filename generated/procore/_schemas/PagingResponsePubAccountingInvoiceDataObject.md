# PagingResponsePubAccountingInvoiceDataObject

## PagingResponsePubAccountingInvoiceDataObject
- Role: parent
- Schema Name: PagingResponsePubAccountingInvoice
- Schema ID: schema:components/PagingResponsePubAccountingInvoice

### Fields

| Field | Type |
|------|------|
| `offset` | `int` |
| `limit` | `int` |
| `total` | `int` |
| `data` | `PubAccountingInvoice[]` |
| `orderData` | `PagingOrderDataResponse[]` |
| `prev` | `string` |
| `next` | `string` |

### Nested Types
- `PagingOrderDataResponse`
- `PagingOrderDataResponseOrderdirection`
- `PubAccountingInvoice`
- `PubAccountingInvoiceDetail`
- `PubAccountingInvoiceDetailStatus`
- `PubAccountingInvoiceStatus`

## PagingOrderDataResponse
- Role: nested
- Parent: PagingResponsePubAccountingInvoiceDataObject
- Schema Name: PagingOrderDataResponse
- Schema ID: schema:components/PagingOrderDataResponse

### Fields

| Field | Type |
|------|------|
| `orderBy` | `string` |
| `orderDirection` | `PagingOrderDataResponseOrderdirection` |

## PagingOrderDataResponseOrderdirection
- Role: nested
- Parent: PagingResponsePubAccountingInvoiceDataObject
- Schema Name: PagingOrderDataResponseOrderdirection
- Schema ID: schema:anon/d005f4d343e3145c9082cdbedab65effe3da2980

### Enum

Values: ASC, DESC

## PubAccountingInvoice
- Role: nested
- Parent: PagingResponsePubAccountingInvoiceDataObject
- Schema Name: PubAccountingInvoice
- Schema ID: schema:components/PubAccountingInvoice
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `invoiceNumber` | `string` |
| `amount` | `double` |
| `valueOrig` | `double` |
| `buildingCode` | `string` |
| `jobCode` | `string` |
| `vendorCode` | `string` |
| `contractCode` | `string` |
| `invoiceDate` | `string` |
| `period` | `string` |
| `status` | `PubAccountingInvoiceStatus` |
| `source` | `string` |
| `costCode` | `string` |
| `costCodeName` | `string` |
| `costCategoryCode` | `string` |
| `checkNumber` | `string` |
| `description` | `string` |
| `details` | `PubAccountingInvoiceDetail[]` |

## PubAccountingInvoiceDetail
- Role: nested
- Parent: PagingResponsePubAccountingInvoiceDataObject
- Schema Name: PubAccountingInvoiceDetail
- Schema ID: schema:components/PubAccountingInvoiceDetail

### Fields

| Field | Type |
|------|------|
| `lineItem` | `string` |
| `categoryCode` | `string` |
| `accountCode` | `string` |
| `checkNumber` | `string` |
| `checkDate` | `string` |
| `checkPeriod` | `string` |
| `paymentMethod` | `string` |
| `retention` | `double` |
| `reference` | `string` |
| `status` | `PubAccountingInvoiceDetailStatus` |

## PubAccountingInvoiceDetailStatus
- Role: nested
- Parent: PagingResponsePubAccountingInvoiceDataObject
- Schema Name: PubAccountingInvoiceDetailStatus
- Schema ID: schema:anon/5ee1c00d8df2e117c693e9e4ac95d030084e2f70

### Enum

Values: PENDING, POSTED, RELEASED, PAID, UNUSED, VOID, REVERSED, DELETED

## PubAccountingInvoiceStatus
- Role: nested
- Parent: PagingResponsePubAccountingInvoiceDataObject
- Schema Name: PubAccountingInvoiceStatus
- Schema ID: schema:anon/fd59d309968793604d7575cab61f7b300fc8fbe7

### Enum

Values: PENDING, POSTED, RELEASED, PAID, UNUSED, VOID, REVERSED, DELETED
