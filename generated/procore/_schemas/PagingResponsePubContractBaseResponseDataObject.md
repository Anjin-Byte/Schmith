# PagingResponsePubContractBaseResponseDataObject

## PagingResponsePubContractBaseResponseDataObject
- Role: parent
- Schema Name: PagingResponsePubContractBaseResponse
- Schema ID: schema:components/PagingResponsePubContractBaseResponse

### Fields

| Field | Type |
|------|------|
| `offset` | `int` |
| `limit` | `int` |
| `total` | `int` |
| `data` | `PubContractBaseResponse[]` |
| `orderData` | `PagingOrderDataResponse[]` |
| `prev` | `string` |
| `next` | `string` |

### Nested Types
- `PagingOrderDataResponse`
- `PagingOrderDataResponseOrderdirection`
- `PubContractBaseResponse`
- `PubContractBaseResponseCurrencycode`
- `PubContractBaseResponseStatus`

## PagingOrderDataResponse
- Role: nested
- Parent: PagingResponsePubContractBaseResponseDataObject
- Schema Name: PagingOrderDataResponse
- Schema ID: schema:components/PagingOrderDataResponse

### Fields

| Field | Type |
|------|------|
| `orderBy` | `string` |
| `orderDirection` | `PagingOrderDataResponseOrderdirection` |

## PagingOrderDataResponseOrderdirection
- Role: nested
- Parent: PagingResponsePubContractBaseResponseDataObject
- Schema Name: PagingOrderDataResponseOrderdirection
- Schema ID: schema:anon/d005f4d343e3145c9082cdbedab65effe3da2980

### Enum

Values: ASC, DESC

## PubContractBaseResponse
- Role: nested
- Parent: PagingResponsePubContractBaseResponseDataObject
- Schema Name: PubContractBaseResponse
- Schema ID: schema:components/PubContractBaseResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `currencyCode` | `PubContractBaseResponseCurrencycode` |
| `baseCurrencyCode` | `PubContractBaseResponseCurrencycode` |
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
| `status` | `PubContractBaseResponseStatus` |
| `dateCreated` | `string` |
| `dateUpdated` | `string` |
| `dateApproved` | `string` |
| `contractCode` | `string` |
| `purchaseOrderCode` | `string` |

## PubContractBaseResponseCurrencycode
- Role: nested
- Parent: PagingResponsePubContractBaseResponseDataObject
- Schema Name: PubContractBaseResponseCurrencycode
- Schema ID: schema:anon/1d75d23dce4cf517a0e64ef4822b59408a327762

### Enum

Values: AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CUC, CUP, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GGP, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, IMP, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KMF, KPW, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SPL, SRD, STN, SVC, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TVD, TWD, TZS, UAH, UGX, USD, UYU, UZS, VEF, VND, VUV, WST, XAF, XCD, XDR, XOF, XPF, YER, ZAR, ZMW, ZWD

## PubContractBaseResponseStatus
- Role: nested
- Parent: PagingResponsePubContractBaseResponseDataObject
- Schema Name: PubContractBaseResponseStatus
- Schema ID: schema:anon/500613f04f15954056fcc8e00fdabd25b285811b

### Enum

Values: potential, closed, open, approved, pending
