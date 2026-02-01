# PagingResponsePubJobBaseResponseDataObject

## PagingResponsePubJobBaseResponseDataObject
- Role: parent
- Schema Name: PagingResponsePubJobBaseResponse
- Schema ID: schema:components/PagingResponsePubJobBaseResponse

### Fields

| Field | Type |
|------|------|
| `offset` | `int` |
| `limit` | `int` |
| `total` | `int` |
| `data` | `PubJobBaseResponse[]` |
| `orderData` | `PagingOrderDataResponse[]` |
| `prev` | `string` |
| `next` | `string` |

### Nested Types
- `PagingOrderDataResponse`
- `PagingOrderDataResponseOrderdirection`
- `PubJobBaseResponse`
- `PubJobBaseResponseCurrencycode`

## PagingOrderDataResponse
- Role: nested
- Parent: PagingResponsePubJobBaseResponseDataObject
- Schema Name: PagingOrderDataResponse
- Schema ID: schema:components/PagingOrderDataResponse

### Fields

| Field | Type |
|------|------|
| `orderBy` | `string` |
| `orderDirection` | `PagingOrderDataResponseOrderdirection` |

## PagingOrderDataResponseOrderdirection
- Role: nested
- Parent: PagingResponsePubJobBaseResponseDataObject
- Schema Name: PagingOrderDataResponseOrderdirection
- Schema ID: schema:anon/d005f4d343e3145c9082cdbedab65effe3da2980

### Enum

Values: ASC, DESC

## PubJobBaseResponse
- Role: nested
- Parent: PagingResponsePubJobBaseResponseDataObject
- Schema Name: PubJobBaseResponse
- Schema ID: schema:components/PubJobBaseResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `currencyCode` | `PubJobBaseResponseCurrencycode` |
| `baseCurrencyCode` | `PubJobBaseResponseCurrencycode` |
| `fxRate` | `double` |
| `isFxConverted` | `bool` |
| `id` | `int` |
| `userIds` | `int[]` |
| `buildingName` | `string` |
| `title` | `string` |
| `jobType` | `string` |
| `description` | `string` |
| `sqFt` | `double` |
| `companyBuildingId` | `int` |
| `dateCreated` | `string` |
| `dateUpdated` | `string` |
| `stage` | `string` |
| `startDate` | `string` |
| `endDate` | `string` |
| `numUnits` | `int` |
| `budget` | `double` |
| `jobCode` | `string` |
| `pmUserId` | `int` |
| `pmUserEmailAddress` | `string` |
| `archivedFlag` | `bool` |

## PubJobBaseResponseCurrencycode
- Role: nested
- Parent: PagingResponsePubJobBaseResponseDataObject
- Schema Name: PubJobBaseResponseCurrencycode
- Schema ID: schema:anon/1d75d23dce4cf517a0e64ef4822b59408a327762

### Enum

Values: AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CUC, CUP, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GGP, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, IMP, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KMF, KPW, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SPL, SRD, STN, SVC, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TVD, TWD, TZS, UAH, UGX, USD, UYU, UZS, VEF, VND, VUV, WST, XAF, XCD, XDR, XOF, XPF, YER, ZAR, ZMW, ZWD
