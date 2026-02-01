# PagingResponsePubCompanyVendorResponseDataObject

## PagingResponsePubCompanyVendorResponseDataObject
- Role: parent
- Schema Name: PagingResponsePubCompanyVendorResponse
- Schema ID: schema:components/PagingResponsePubCompanyVendorResponse

### Fields

| Field | Type |
|------|------|
| `offset` | `int` |
| `limit` | `int` |
| `total` | `int` |
| `data` | `PubCompanyVendorResponse[]` |
| `orderData` | `PagingOrderDataResponse[]` |
| `prev` | `string` |
| `next` | `string` |

### Nested Types
- `PagingOrderDataResponse`
- `PagingOrderDataResponseOrderdirection`
- `PubCompanyVendorContactPhoneNumberResponse`
- `PubCompanyVendorContactPhoneNumberResponsePhonetype`
- `PubCompanyVendorContactResponse`
- `PubCompanyVendorResponse`

## PagingOrderDataResponse
- Role: nested
- Parent: PagingResponsePubCompanyVendorResponseDataObject
- Schema Name: PagingOrderDataResponse
- Schema ID: schema:components/PagingOrderDataResponse

### Fields

| Field | Type |
|------|------|
| `orderBy` | `string` |
| `orderDirection` | `PagingOrderDataResponseOrderdirection` |

## PagingOrderDataResponseOrderdirection
- Role: nested
- Parent: PagingResponsePubCompanyVendorResponseDataObject
- Schema Name: PagingOrderDataResponseOrderdirection
- Schema ID: schema:anon/d005f4d343e3145c9082cdbedab65effe3da2980

### Enum

Values: ASC, DESC

## PubCompanyVendorContactPhoneNumberResponse
- Role: nested
- Parent: PagingResponsePubCompanyVendorResponseDataObject
- Schema Name: PubCompanyVendorContactPhoneNumberResponse
- Schema ID: schema:components/PubCompanyVendorContactPhoneNumberResponse

### Fields

| Field | Type |
|------|------|
| `phoneNumber` | `string` |
| `phoneType` | `PubCompanyVendorContactPhoneNumberResponsePhonetype` |

## PubCompanyVendorContactPhoneNumberResponsePhonetype
- Role: nested
- Parent: PagingResponsePubCompanyVendorResponseDataObject
- Schema Name: PubCompanyVendorContactPhoneNumberResponsePhonetype
- Schema ID: schema:anon/4b0d5310d0c74e79dbf00b4fb5b8893e343c9b08

### Enum

Values: Office, Mobile, Home, Fax, Other

## PubCompanyVendorContactResponse
- Role: nested
- Parent: PagingResponsePubCompanyVendorResponseDataObject
- Schema Name: PubCompanyVendorContactResponse
- Schema ID: schema:components/PubCompanyVendorContactResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `companyVendorId` | `int` |
| `userId` | `int` |
| `firstName` | `string` |
| `lastName` | `string` |
| `emailAddress` | `string` |
| `phoneNumbers` | `PubCompanyVendorContactPhoneNumberResponse[]` |
| `title` | `string` |
| `primaryContactFlag` | `bool` |
| `dateCreated` | `string` |
| `dateUpdated` | `string` |

## PubCompanyVendorResponse
- Role: nested
- Parent: PagingResponsePubCompanyVendorResponseDataObject
- Schema Name: PubCompanyVendorResponse
- Schema ID: schema:components/PubCompanyVendorResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `vendorCode` | `string` |
| `companyId` | `int` |
| `vendorCompanyId` | `int` |
| `companyName` | `string` |
| `vendorType` | `string` |
| `address1` | `string` |
| `address2` | `string` |
| `city` | `string` |
| `region` | `string` |
| `postalCode` | `string` |
| `country` | `string` |
| `lat` | `double` |
| `lng` | `double` |
| `website` | `string` |
| `comments` | `string` |
| `isMbeCertified` | `bool` |
| `isWbeCertified` | `bool` |
| `isLeedCertified` | `bool` |
| `isUnion` | `bool` |
| `isNonUnion` | `bool` |
| `isCompanyContact` | `bool` |
| `insuranceExpiryDate` | `string` |
| `wsibExpiryDate` | `string` |
| `vendorContacts` | `PubCompanyVendorContactResponse[]` |
| `dateCreated` | `string` |
| `dateUpdated` | `string` |
