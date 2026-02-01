# PubInvoiceResponseDataObject

## PubInvoiceResponseDataObject
- Role: parent
- Schema Name: PubInvoiceResponse
- Schema ID: schema:components/PubInvoiceResponse
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
| `status` | `PubInvoiceResponseStatus` |
| `invoiceNumber` | `int` |
| `invoiceNumberAlphanumeric` | `string` |
| `periodStart` | `string` |
| `periodEnd` | `string` |
| `reason` | `string` |
| `isReleaseRetentionInvoice` | `bool` |
| `isCreatedByVendor` | `bool` |
| `dateApproved` | `string` |
| `invoiceCode` | `string` |
| `invoiceDetails` | `PubInvoiceDetailResponse[]` |

### Nested Types
- `PubInvoiceDetailResponse`
- `PubInvoiceResponseStatus`

## PubInvoiceDetailResponse
- Role: nested
- Parent: PubInvoiceResponseDataObject
- Schema Name: PubInvoiceDetailResponse
- Schema ID: schema:components/PubInvoiceDetailResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `costDetailId` | `int` |
| `invoiceAmount` | `double` |
| `retainage` | `double` |
| `retainageRelease` | `double` |
| `label` | `string` |
| `dateCreated` | `string` |
| `dateUpdated` | `string` |

## PubInvoiceResponseStatus
- Role: nested
- Parent: PubInvoiceResponseDataObject
- Schema Name: PubInvoiceResponseStatus
- Schema ID: schema:anon/ba27824ebdb9cfe0f2a4d626c06e741c56aeb6d9

### Enum

Values: pending, approved, rejected, reviewed
