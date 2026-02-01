# RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGetResponse200DataObject

## RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGetResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGetResponse200
- Schema ID: schema:anon/ad5bca5e742413c60f643c94ca8eb002d34f1e46
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `attachment` | `RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGetResponse200Attachment` |
| `captured_at` | `string` |
| `captured_by` | `RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGetResponse200CapturedBy` |

### Nested Types
- `RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGetResponse200Attachment`
- `RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGetResponse200CapturedBy`
- `RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGetResponse200CapturedByVendor`

## RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGetResponse200Attachment
- Role: nested
- Parent: RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGetResponse200Attachment
- Schema ID: schema:anon/8b3c324b018f85a6ac64c40f140c8fd0d89ff5c8
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `content_type` | `string` |
| `name` | `string` |
| `url` | `string` |

## RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGetResponse200CapturedBy
- Role: nested
- Parent: RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGetResponse200CapturedBy
- Schema ID: schema:anon/643a569a9732fa84fb0d9986fe57bfcfc54c9d00
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `first_name` | `string` |
| `last_name` | `string` |
| `name` | `string` |
| `user_id` | `int` |
| `is_employee` | `bool` |
| `employee_id` | `string` |
| `login` | `string` |
| `updated_at` | `string` |
| `vendor` | `RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGetResponse200CapturedByVendor` |

## RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGetResponse200CapturedByVendor
- Role: nested
- Parent: RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGetResponse200CapturedByVendor
- Schema ID: schema:anon/cb28499d89e5cab77b31252a93314da12c8f4741
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
