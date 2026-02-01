# MissedPunchRequest2DataObject

## MissedPunchRequest2DataObject
- Role: parent
- Schema Name: MissedPunchRequest2
- Schema ID: schema:components/MissedPunchRequest2

### Fields

| Field | Type |
|------|------|
| `employeeId` | `string` |
| `punchId` | `string` |
| `punchRefId` | `string` |
| `status` | `MissedPunchRequestStatus` |
| `note` | `string` |
| `reasonCodeId` | `string` |
| `workLocationId` | `string` |

### Nested Types
- `MissedPunchRequestStatus`

## MissedPunchRequestStatus
- Role: nested
- Parent: MissedPunchRequest2DataObject
- Schema Name: MissedPunchRequestStatus
- Schema ID: schema:components/MissedPunchRequestStatus

### Enum

Values: Approve, Deny
Names: Approve, Deny
