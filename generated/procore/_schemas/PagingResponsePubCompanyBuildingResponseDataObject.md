# PagingResponsePubCompanyBuildingResponseDataObject

## PagingResponsePubCompanyBuildingResponseDataObject
- Role: parent
- Schema Name: PagingResponsePubCompanyBuildingResponse
- Schema ID: schema:components/PagingResponsePubCompanyBuildingResponse

### Fields

| Field | Type |
|------|------|
| `offset` | `int` |
| `limit` | `int` |
| `total` | `int` |
| `data` | `PubCompanyBuildingResponse[]` |
| `orderData` | `PagingOrderDataResponse[]` |
| `prev` | `string` |
| `next` | `string` |

### Nested Types
- `PagingOrderDataResponse`
- `PagingOrderDataResponseOrderdirection`
- `PubCompanyBuildingResponse`

## PagingOrderDataResponse
- Role: nested
- Parent: PagingResponsePubCompanyBuildingResponseDataObject
- Schema Name: PagingOrderDataResponse
- Schema ID: schema:components/PagingOrderDataResponse

### Fields

| Field | Type |
|------|------|
| `orderBy` | `string` |
| `orderDirection` | `PagingOrderDataResponseOrderdirection` |

## PagingOrderDataResponseOrderdirection
- Role: nested
- Parent: PagingResponsePubCompanyBuildingResponseDataObject
- Schema Name: PagingOrderDataResponseOrderdirection
- Schema ID: schema:anon/d005f4d343e3145c9082cdbedab65effe3da2980

### Enum

Values: ASC, DESC

## PubCompanyBuildingResponse
- Role: nested
- Parent: PagingResponsePubCompanyBuildingResponseDataObject
- Schema Name: PubCompanyBuildingResponse
- Schema ID: schema:components/PubCompanyBuildingResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `companyId` | `int` |
| `buildingName` | `string` |
| `market` | `string` |
| `sqFt` | `double` |
| `streetAddress` | `string` |
| `city` | `string` |
| `region` | `string` |
| `postalCode` | `string` |
| `country` | `string` |
| `lat` | `double` |
| `lng` | `double` |
| `assetManager` | `string` |
| `entityName` | `string` |
| `accountsPayableEmail` | `string` |
| `buildingDesc` | `string` |
| `buildingCode` | `string` |
| `archivedFlag` | `bool` |
| `normalizeAddressFlag` | `bool` |
| `dateCreated` | `string` |
| `dateUpdated` | `string` |
| `subMarket` | `string` |
| `localeLevel1` | `string` |
| `localeLevel2` | `string` |
| `localeLevel3` | `string` |
| `portfolio` | `string` |
