# RestV10MeetingAttendeeRecordsPostResponse201DataObject

## RestV10MeetingAttendeeRecordsPostResponse201DataObject
- Role: parent
- Schema Name: RestV10MeetingAttendeeRecordsPostResponse201
- Schema ID: schema:anon/ded147c1318664ba0a6e3a5f53e1c926146a7865
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `meeting_id` | `int` |
| `status` | `RestV10MeetingAttendeeRecordsPostResponse201Status` |
| `login_information` | `RestV10MeetingAttendeeRecordsPostResponse201LoginInformation` |

### Nested Types
- `RestV10MeetingAttendeeRecordsPostResponse201LoginInformation`
- `RestV10MeetingAttendeeRecordsPostResponse201Status`

## RestV10MeetingAttendeeRecordsPostResponse201LoginInformation
- Role: nested
- Parent: RestV10MeetingAttendeeRecordsPostResponse201DataObject
- Schema Name: RestV10MeetingAttendeeRecordsPostResponse201LoginInformation
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10MeetingAttendeeRecordsPostResponse201Status
- Role: nested
- Parent: RestV10MeetingAttendeeRecordsPostResponse201DataObject
- Schema Name: RestV10MeetingAttendeeRecordsPostResponse201Status
- Schema ID: schema:anon/0076dedd3f292252ed528f356563d3fddd66e699

### Enum

Values: Present, Absent, For Distribution Only, Conference
