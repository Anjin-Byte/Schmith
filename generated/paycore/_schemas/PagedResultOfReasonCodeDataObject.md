# PagedResultOfReasonCodeDataObject

## PagedResultOfReasonCodeDataObject
- Role: parent
- Schema Name: PagedResultOfReasonCode
- Schema ID: schema:components/PagedResultOfReasonCode

### Fields

| Field | Type |
|------|------|
| `hasMoreResults` | `bool` |
| `continuationToken` | `string` |
| `additionalResultsUrl` | `string` |
| `records` | `ReasonCode[]` |

### Nested Types
- `ReasonCode`

## ReasonCode
- Role: nested
- Parent: PagedResultOfReasonCodeDataObject
- Schema Name: ReasonCode
- Schema ID: schema:components/ReasonCode

### Fields

| Field | Type |
|------|------|
| `reasonCodeId` | `string` |
| `reasonCodeName` | `string` |
| `effectiveStartDate` | `string` |
| `effectiveEndDate` | `string` |
