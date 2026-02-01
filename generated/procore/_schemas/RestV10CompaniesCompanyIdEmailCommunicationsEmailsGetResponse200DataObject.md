# RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200DataObject

## RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200DataObject
- Role: parent
- Schema Name: RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200
- Schema ID: schema:anon/2fe9d6e5521708faa0d60d4f020193eca6080472

### Fields

| Field | Type |
|------|------|
| `communication_threads` | `RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200CommunicationThreadsItem[]` |
| `total` | `int` |
| `new_communication_email` | `string` |

### Nested Types
- `RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200CommunicationThreadsItem`
- `RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200CommunicationThreadsItemAttachmentsItem`
- `RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200CommunicationThreadsItemBccDistributionItem`
- `RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200CommunicationThreadsItemLoginInformation`

## RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200CommunicationThreadsItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200CommunicationThreadsItem
- Schema ID: schema:anon/615110bad7e8e567d3190311238b2410983fdb65
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `communication_id` | `int` |
| `subject` | `string` |
| `private` | `bool` |
| `attachments` | `RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200CommunicationThreadsItemAttachmentsItem[]` |
| `bcc_distribution` | `RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200CommunicationThreadsItemBccDistributionItem[]` |
| `body` | `string` |
| `sanitized_body_html` | `string` |
| `cc_distribution` | `RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200CommunicationThreadsItemBccDistributionItem[]` |
| `distribution` | `RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200CommunicationThreadsItemBccDistributionItem[]` |
| `email_sent_at` | `string` |
| `login_information` | `RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200CommunicationThreadsItemLoginInformation` |

## RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200CommunicationThreadsItemAttachmentsItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200CommunicationThreadsItemAttachmentsItem
- Schema ID: schema:anon/2d3aa4ac69969735b70ffda3f00a0e2640501a0f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `url` | `string` |

## RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200CommunicationThreadsItemBccDistributionItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200CommunicationThreadsItemBccDistributionItem
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

## RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200CommunicationThreadsItemLoginInformation
- Role: nested
- Parent: RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdEmailCommunicationsEmailsGetResponse200CommunicationThreadsItemLoginInformation
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
