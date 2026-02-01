# PubInvoiceAccountingRawResponseDataObject

## PubInvoiceAccountingRawResponseDataObject
- Role: parent
- Schema Name: PubInvoiceAccountingRawResponse
- Schema ID: schema:components/PubInvoiceAccountingRawResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `invoiceNumber` | `string` |
| `amount` | `double` |
| `valueOrig` | `double` |
| `type` | `PubInvoiceAccountingRawResponseType` |
| `buildingCode` | `string` |
| `jobCode` | `string` |
| `vendorCode` | `string` |
| `invoiceDate` | `string` |
| `period` | `string` |
| `source` | `string` |
| `status` | `PubInvoiceAccountingRawResponseStatus` |
| `contractCode` | `string` |
| `costCode` | `string` |
| `costCodeName` | `string` |
| `description` | `string` |
| `invoiceCode` | `string` |
| `dateCreated` | `string` |
| `dateUpdated` | `string` |
| `details` | `PubInvoiceAccountingDetailRawResponse[]` |

### Nested Types
- `PubInvoiceAccountingDetailRawResponse`
- `PubInvoiceAccountingRawResponseStatus`
- `PubInvoiceAccountingRawResponseType`

## PubInvoiceAccountingDetailRawResponse
- Role: nested
- Parent: PubInvoiceAccountingRawResponseDataObject
- Schema Name: PubInvoiceAccountingDetailRawResponse
- Schema ID: schema:components/PubInvoiceAccountingDetailRawResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `lineItem` | `string` |
| `accountCode` | `string` |
| `costCode` | `string` |
| `categoryCode` | `string` |
| `status` | `PubInvoiceAccountingRawResponseStatus` |
| `checkNumber` | `string` |
| `checkDate` | `string` |
| `checkPeriod` | `string` |
| `paymentMethod` | `string` |
| `amount` | `double` |
| `retentionAmount` | `double` |
| `reference` | `string` |
| `dateCreated` | `string` |
| `dateUpdated` | `string` |

## PubInvoiceAccountingRawResponseStatus
- Role: nested
- Parent: PubInvoiceAccountingRawResponseDataObject
- Schema Name: PubInvoiceAccountingRawResponseStatus
- Schema ID: schema:anon/fd59d309968793604d7575cab61f7b300fc8fbe7

### Enum

Values: PENDING, POSTED, RELEASED, PAID, UNUSED, VOID, REVERSED, DELETED

## PubInvoiceAccountingRawResponseType
- Role: nested
- Parent: PubInvoiceAccountingRawResponseDataObject
- Schema Name: PubInvoiceAccountingRawResponseType
- Schema ID: schema:anon/cd432c5c6bd43aaa070aa268d1f585a78a335e25

### Enum

Values: YARDI_INVOICE, MRI_INVOICE, GENERIC_ACCOUNTING_INVOICE, IBS_INVOICE_DETAIL, IBS_CONTRACT_DETAIL, JDE_INVOICE, MRI_JOURNAL_ENTRY, YARDI_JOURNAL_ENTRY, PUB_API_INVOICE
