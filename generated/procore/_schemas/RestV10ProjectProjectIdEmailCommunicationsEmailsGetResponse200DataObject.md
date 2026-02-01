# RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200DataObject

## RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200
- Schema ID: schema:anon/d1e58a35ecf5e3c45dd559bb7e8dbcdadc07ba0b

### Fields

| Field | Type |
|------|------|
| `emails` | `RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200EmailsItem[]` |
| `total` | `int` |
| `new_communication_email` | `string` |

### Nested Types
- `RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200EmailsItem`
- `RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200EmailsItemAttachmentsItem`
- `RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200EmailsItemBccDistributionItem`
- `RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200EmailsItemLoginInformation`

## RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200EmailsItem
- Role: nested
- Parent: RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200DataObject
- Schema Name: RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200EmailsItem
- Schema ID: schema:anon/615110bad7e8e567d3190311238b2410983fdb65
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `communication_id` | `int` |
| `subject` | `string` |
| `private` | `bool` |
| `attachments` | `RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200EmailsItemAttachmentsItem[]` |
| `bcc_distribution` | `RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200EmailsItemBccDistributionItem[]` |
| `body` | `string` |
| `sanitized_body_html` | `string` |
| `cc_distribution` | `RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200EmailsItemBccDistributionItem[]` |
| `distribution` | `RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200EmailsItemBccDistributionItem[]` |
| `email_sent_at` | `string` |
| `login_information` | `RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200EmailsItemLoginInformation` |

## RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200EmailsItemAttachmentsItem
- Role: nested
- Parent: RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200DataObject
- Schema Name: RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200EmailsItemAttachmentsItem
- Schema ID: schema:anon/2d3aa4ac69969735b70ffda3f00a0e2640501a0f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `url` | `string` |

## RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200EmailsItemBccDistributionItem
- Role: nested
- Parent: RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200DataObject
- Schema Name: RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200EmailsItemBccDistributionItem
- Schema ID: schema:anon/6089a88369282cb3f840dc079d6602ef7d0760df
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `company_name` | `string` |
| `locale` | `string` |
| `login` | `string` |
| `name` | `string` |
| `avatar` | `string` |
| `initials` | `string` |

## RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200EmailsItemLoginInformation
- Role: nested
- Parent: RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200DataObject
- Schema Name: RestV10ProjectProjectIdEmailCommunicationsEmailsGetResponse200EmailsItemLoginInformation
- Schema ID: schema:anon/46cc4d82fb0ae05a50d85f5aa77d52335f7e8a2d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `company_name` | `string` |
| `locale` | `string` |
| `login` | `string` |
| `name` | `string` |
| `avatar` | `string` |
| `initials` | `string` |
