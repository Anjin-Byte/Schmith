# RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200DataObject

## RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200
- Schema ID: schema:anon/027d5190b06d535965babaef9dd627ae6d6deced
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `private` | `bool` |
| `subject` | `string` |
| `emails` | `RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200EmailsItem[]` |

### Nested Types
- `RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200EmailsItem`
- `RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200EmailsItemAttachmentsItem`
- `RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200EmailsItemBccDistributionItem`
- `RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200EmailsItemLoginInformation`

## RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200EmailsItem
- Role: nested
- Parent: RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200DataObject
- Schema Name: RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200EmailsItem
- Schema ID: schema:anon/3a4bab3ce3bbf8b981acb01f08b3f96aae6854fc
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `communication_id` | `int` |
| `private` | `bool` |
| `attachments` | `RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200EmailsItemAttachmentsItem[]` |
| `bcc_distribution` | `RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200EmailsItemBccDistributionItem[]` |
| `body` | `string` |
| `sanitized_body_html` | `string` |
| `cc_distribution` | `RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200EmailsItemBccDistributionItem[]` |
| `distribution` | `RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200EmailsItemBccDistributionItem[]` |
| `email_sent_at` | `string` |
| `login_information` | `RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200EmailsItemLoginInformation` |

## RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200EmailsItemAttachmentsItem
- Role: nested
- Parent: RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200DataObject
- Schema Name: RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200EmailsItemAttachmentsItem
- Schema ID: schema:anon/3d14e06ab61e286bff65efd4ec4bcd4cfcae88dc
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `url` | `string` |

## RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200EmailsItemBccDistributionItem
- Role: nested
- Parent: RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200DataObject
- Schema Name: RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200EmailsItemBccDistributionItem
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

## RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200EmailsItemLoginInformation
- Role: nested
- Parent: RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200DataObject
- Schema Name: RestV10ProjectProjectIdEmailCommunicationsIdGetResponse200EmailsItemLoginInformation
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
