# PubContractResponseDataObject

## PubContractResponseDataObject
- Role: parent
- Schema Name: PubContractResponse
- Schema ID: schema:components/PubContractResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `currencyCode` | `PubContractResponseCurrencycode` |
| `baseCurrencyCode` | `PubContractResponseCurrencycode` |
| `fxRate` | `double` |
| `isFxConverted` | `bool` |
| `id` | `int` |
| `label` | `string` |
| `budget` | `double` |
| `awardedValue` | `double` |
| `dateAwarded` | `string` |
| `companyVendorId` | `int` |
| `companyVendorName` | `string` |
| `jobId` | `int` |
| `costScheduleId` | `int` |
| `invoiceRetainageEnabledFlag` | `bool` |
| `invoiceRetainagePct` | `double` |
| `status` | `PubContractResponseStatus` |
| `dateCreated` | `string` |
| `dateUpdated` | `string` |
| `dateApproved` | `string` |
| `contractCode` | `string` |
| `purchaseOrderCode` | `string` |
| `awardedBy` | `int` |
| `lastUpdatedBy` | `int` |
| `bidroomId` | `int` |
| `breakdownEnabled` | `bool` |
| `sharedWithVendor` | `bool` |
| `sentToAccountingFlag` | `bool` |
| `sentToAccountingTimestamp` | `string` |
| `sentToAccountingUserId` | `int` |
| `vendorTeam` | `int[]` |
| `ownerTeam` | `int[]` |
| `approvalWorkflow` | `ApprovalWorkflowResponse` |
| `costDetails` | `PubCostDetailResponse[]` |

### Nested Types
- `ApprovalWorkflowItemResponse`
- `ApprovalWorkflowItemResponseStatus`
- `ApprovalWorkflowResponse`
- `ApprovalWorkflowResponseStatus`
- `PubAccountingCodeResponse`
- `PubContractResponseCurrencycode`
- `PubContractResponseStatus`
- `PubCostDetailResponse`

## ApprovalWorkflowItemResponse
- Role: nested
- Parent: PubContractResponseDataObject
- Schema Name: ApprovalWorkflowItemResponse
- Schema ID: schema:components/ApprovalWorkflowItemResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `approvalWorkflowId` | `int` |
| `status` | `ApprovalWorkflowItemResponseStatus` |
| `approvalUserId` | `int` |
| `ordinal` | `int` |
| `comment` | `string` |
| `statusDate` | `string` |
| `userId` | `int` |
| `firstName` | `string` |
| `lastName` | `string` |

## ApprovalWorkflowItemResponseStatus
- Role: nested
- Parent: PubContractResponseDataObject
- Schema Name: ApprovalWorkflowItemResponseStatus
- Schema ID: schema:anon/12281169ae29eabab242b3fd278c8272916b5d00

### Enum

Values: pending, approved, rejected

## ApprovalWorkflowResponse
- Role: nested
- Parent: PubContractResponseDataObject
- Schema Name: ApprovalWorkflowResponse
- Schema ID: schema:components/ApprovalWorkflowResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `status` | `ApprovalWorkflowResponseStatus` |
| `publishedUserId` | `int` |
| `firstName` | `string` |
| `lastName` | `string` |
| `dateCreated` | `string` |
| `approvalWorkflowItems` | `ApprovalWorkflowItemResponse[]` |

## ApprovalWorkflowResponseStatus
- Role: nested
- Parent: PubContractResponseDataObject
- Schema Name: ApprovalWorkflowResponseStatus
- Schema ID: schema:anon/13ab6cdf8ff5de14ef09152b0a5acd89901563f7

### Enum

Values: pending, approved, canceled, rejected

## PubAccountingCodeResponse
- Role: nested
- Parent: PubContractResponseDataObject
- Schema Name: PubAccountingCodeResponse
- Schema ID: schema:components/PubAccountingCodeResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |
| `accountCode` | `string` |
| `jobType` | `string` |
| `phaseCode` | `string` |
| `entityCode` | `string` |
| `costCategory` | `string` |
| `costList` | `string` |
| `costCode` | `string` |

## PubContractResponseCurrencycode
- Role: nested
- Parent: PubContractResponseDataObject
- Schema Name: PubContractResponseCurrencycode
- Schema ID: schema:anon/1d75d23dce4cf517a0e64ef4822b59408a327762

### Enum

Values: AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CUC, CUP, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GGP, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, IMP, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KMF, KPW, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SPL, SRD, STN, SVC, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TVD, TWD, TZS, UAH, UGX, USD, UYU, UZS, VEF, VND, VUV, WST, XAF, XCD, XDR, XOF, XPF, YER, ZAR, ZMW, ZWD

## PubContractResponseStatus
- Role: nested
- Parent: PubContractResponseDataObject
- Schema Name: PubContractResponseStatus
- Schema ID: schema:anon/500613f04f15954056fcc8e00fdabd25b285811b

### Enum

Values: potential, closed, open, approved, pending

## PubCostDetailResponse
- Role: nested
- Parent: PubContractResponseDataObject
- Schema Name: PubCostDetailResponse
- Schema ID: schema:components/PubCostDetailResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `costScheduleId` | `int` |
| `cost` | `double` |
| `label` | `string` |
| `accountingCode` | `PubAccountingCodeResponse` |
| `dateCreated` | `string` |
| `dateUpdated` | `string` |
