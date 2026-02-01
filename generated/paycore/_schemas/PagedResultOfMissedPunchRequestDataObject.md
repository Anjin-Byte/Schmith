# PagedResultOfMissedPunchRequestDataObject

## PagedResultOfMissedPunchRequestDataObject
- Role: parent
- Schema Name: PagedResultOfMissedPunchRequest
- Schema ID: schema:components/PagedResultOfMissedPunchRequest

### Fields

| Field | Type |
|------|------|
| `hasMoreResults` | `bool` |
| `continuationToken` | `string` |
| `additionalResultsUrl` | `string` |
| `records` | `MissedPunchRequest[]` |

### Nested Types
- `LaborCode3`
- `MissedPunchRequest`
- `PunchStatusType`

## LaborCode3
- Role: nested
- Parent: PagedResultOfMissedPunchRequestDataObject
- Schema Name: LaborCode3
- Schema ID: schema:components/LaborCode3

### Fields

| Field | Type |
|------|------|
| `laborCategoryId` | `string` |
| `laborCodeId` | `string` |

## MissedPunchRequest
- Role: nested
- Parent: PagedResultOfMissedPunchRequestDataObject
- Schema Name: MissedPunchRequest
- Schema ID: schema:components/MissedPunchRequest

### Fields

| Field | Type |
|------|------|
| `employeeId` | `string` |
| `punchId` | `string` |
| `punchRefId` | `string` |
| `punchDateTime` | `string` |
| `punchStatusType` | `PunchStatusType` |
| `isTransfer` | `bool` |
| `activityTypeId` | `string` |
| `departmentId` | `string` |
| `note` | `string` |
| `laborCodes` | `LaborCode3[]` |
| `workLocationId` | `string` |

## PunchStatusType
- Role: nested
- Parent: PagedResultOfMissedPunchRequestDataObject
- Schema Name: PunchStatusType
- Schema ID: schema:components/PunchStatusType

### Enum

Values: Auto, In, Out, Transfer
Names: Auto, In, Out, Transfer
