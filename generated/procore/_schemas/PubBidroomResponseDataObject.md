# PubBidroomResponseDataObject

## PubBidroomResponseDataObject
- Role: parent
- Schema Name: PubBidroomResponse
- Schema ID: schema:components/PubBidroomResponse

### Fields

| Field | Type |
|------|------|
| `currencyCode` | `PubBidroomResponseCurrencycode` |
| `baseCurrencyCode` | `PubBidroomResponseCurrencycode` |
| `fxRate` | `double` |
| `isFxConverted` | `bool` |
| `bidroomId` | `int` |
| `bidroomName` | `string` |
| `bidformId` | `int` |
| `contractId` | `int` |
| `bidders` | `PubBidderResponse[]` |
| `jobId` | `int` |

### Nested Types
- `PubBidderResponse`
- `PubBidroomResponseCurrencycode`
- `UserResponse`

## PubBidderResponse
- Role: nested
- Parent: PubBidroomResponseDataObject
- Schema Name: PubBidderResponse
- Schema ID: schema:components/PubBidderResponse

### Fields

| Field | Type |
|------|------|
| `companyName` | `string` |
| `vendorTeam` | `UserResponse[]` |
| `totalBid` | `double` |

## PubBidroomResponseCurrencycode
- Role: nested
- Parent: PubBidroomResponseDataObject
- Schema Name: PubBidroomResponseCurrencycode
- Schema ID: schema:anon/1d75d23dce4cf517a0e64ef4822b59408a327762

### Enum

Values: AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CUC, CUP, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GGP, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, IMP, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KMF, KPW, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SPL, SRD, STN, SVC, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TVD, TWD, TZS, UAH, UGX, USD, UYU, UZS, VEF, VND, VUV, WST, XAF, XCD, XDR, XOF, XPF, YER, ZAR, ZMW, ZWD

## UserResponse
- Role: nested
- Parent: PubBidroomResponseDataObject
- Schema Name: UserResponse
- Schema ID: schema:components/UserResponse

### Fields

| Field | Type |
|------|------|
| `userId` | `int` |
| `firstName` | `string` |
| `lastName` | `string` |
| `email` | `string` |
| `thumbUrl` | `string` |
