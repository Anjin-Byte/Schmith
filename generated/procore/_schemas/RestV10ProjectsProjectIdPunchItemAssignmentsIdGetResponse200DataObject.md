# RestV10ProjectsProjectIdPunchItemAssignmentsIdGetResponse200DataObject

## RestV10ProjectsProjectIdPunchItemAssignmentsIdGetResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdPunchItemAssignmentsIdGetResponse200
- Schema ID: schema:anon/ceea2a994733748a409a495958b8a40dc0cc7ecb
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `approved` | `bool` |
| `status` | `string` |
| `name` | `string` |
| `comment` | `string` |
| `login_information_id` | `int` |
| `login_information_name` | `string` |
| `login_information` | `RestV10ProjectsProjectIdPunchItemAssignmentsIdGetResponse200LoginInformation` |
| `attachments` | `RestV10ProjectsProjectIdPunchItemAssignmentsIdGetResponse200AttachmentsItem[]` |
| `vendor` | `RestV10ProjectsProjectIdPunchItemAssignmentsIdGetResponse200Vendor` |
| `notified_at` | `string` |
| `responded_at` | `string` |
| `manager_accepted_at` | `string` |
| `user_name` | `string` |
| `updated_at` | `string` |

### Nested Types
- `RestV10ProjectsProjectIdPunchItemAssignmentsIdGetResponse200AttachmentsItem`
- `RestV10ProjectsProjectIdPunchItemAssignmentsIdGetResponse200LoginInformation`
- `RestV10ProjectsProjectIdPunchItemAssignmentsIdGetResponse200Vendor`

## RestV10ProjectsProjectIdPunchItemAssignmentsIdGetResponse200AttachmentsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdPunchItemAssignmentsIdGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdPunchItemAssignmentsIdGetResponse200AttachmentsItem
- Schema ID: schema:anon/c337dee3df228286468f0ff6d8c4852152f75cf4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |

## RestV10ProjectsProjectIdPunchItemAssignmentsIdGetResponse200LoginInformation
- Role: nested
- Parent: RestV10ProjectsProjectIdPunchItemAssignmentsIdGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdPunchItemAssignmentsIdGetResponse200LoginInformation
- Schema ID: schema:anon/69d60ce51ee453f45e146188c33556f77fd6a99d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |
| `company_name` | `string` |

## RestV10ProjectsProjectIdPunchItemAssignmentsIdGetResponse200Vendor
- Role: nested
- Parent: RestV10ProjectsProjectIdPunchItemAssignmentsIdGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdPunchItemAssignmentsIdGetResponse200Vendor
- Schema ID: schema:anon/bdbc967ef89c11cac60241a5dcf6df780325d1d8
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
