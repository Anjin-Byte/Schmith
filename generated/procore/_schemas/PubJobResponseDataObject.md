# PubJobResponseDataObject

## PubJobResponseDataObject
- Role: parent
- Schema Name: PubJobResponse
- Schema ID: schema:components/PubJobResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `currencyCode` | `PubJobResponseCurrencycode` |
| `baseCurrencyCode` | `PubJobResponseCurrencycode` |
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
| `forecast` | `double` |
| `remaining` | `double` |
| `variance` | `double` |
| `committed` | `double` |
| `approvedInvoices` | `double` |
| `pendingInvoices` | `double` |
| `awardedValue` | `double` |
| `holds` | `double` |
| `paidToDate` | `double` |
| `pendingChangeOrders` | `double` |
| `approvedChangeOrders` | `double` |
| `jobItems` | `PubJobItemResponse[]` |
| `jobItemSections` | `PubJobItemSectionResponse[]` |

### Nested Types
- `PubJobItemResponse`
- `PubJobItemSectionResponse`
- `PubJobResponseCurrencycode`

## PubJobItemResponse
- Role: nested
- Parent: PubJobResponseDataObject
- Schema Name: PubJobItemResponse
- Schema ID: schema:components/PubJobItemResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `costItem` | `string` |
| `forecast` | `double` |
| `remaining` | `double` |
| `invoiced` | `double` |
| `committed` | `double` |
| `holds` | `double` |
| `pendingChangeOrders` | `double` |
| `pendingInvoices` | `double` |
| `ordinal` | `int` |
| `bidroomId` | `int` |
| `contractId` | `int` |
| `sectionId` | `int` |
| `budget` | `double` |
| `paidToDate` | `double` |

## PubJobItemSectionResponse
- Role: nested
- Parent: PubJobResponseDataObject
- Schema Name: PubJobItemSectionResponse
- Schema ID: schema:components/PubJobItemSectionResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `ordinal` | `int` |
| `section` | `string` |

## PubJobResponseCurrencycode
- Role: nested
- Parent: PubJobResponseDataObject
- Schema Name: PubJobResponseCurrencycode
- Schema ID: schema:anon/1d75d23dce4cf517a0e64ef4822b59408a327762

### Enum

Values: AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CUC, CUP, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GGP, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, IMP, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KMF, KPW, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SPL, SRD, STN, SVC, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TVD, TWD, TZS, UAH, UGX, USD, UYU, UZS, VEF, VND, VUV, WST, XAF, XCD, XDR, XOF, XPF, YER, ZAR, ZMW, ZWD
