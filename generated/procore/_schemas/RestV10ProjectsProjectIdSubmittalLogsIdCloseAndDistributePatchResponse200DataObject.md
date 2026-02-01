# RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DataObject

## RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200
- Schema ID: schema:anon/ed398de4fee67cd580d161c37475cab8f4b0545c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `message` | `string` |
| `submittal_description` | `string` |
| `sent_at` | `string` |
| `distributed_by` | `RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedBy` |
| `distributed_to` | `RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedBy[]` |
| `distributed_attachments` | `RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedAttachmentsItem[]` |
| `download_all_attachments_url` | `string` |
| `submittal_distributed_attachments` | `RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedAttachmentsItem[]` |
| `download_all_submittal_distributed_attachments_url` | `string` |
| `message_distributed_attachments` | `RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedAttachmentsItem[]` |
| `download_all_message_distributed_attachments_url` | `string` |
| `distributed_responses` | `RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedResponsesItem[]` |

### Nested Types
- `RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedAttachmentsItem`
- `RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedBy`
- `RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedResponsesItem`
- `RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedResponsesItemSubmittalResponse`

## RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedAttachmentsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedAttachmentsItem
- Schema ID: schema:anon/c337dee3df228286468f0ff6d8c4852152f75cf4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |

## RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedBy
- Role: nested
- Parent: RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedBy
- Schema ID: schema:anon/4a9f30724ebffd25faed9570540aab0aa83263f0
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedResponsesItem
- Role: nested
- Parent: RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedResponsesItem
- Schema ID: schema:anon/b6f3de2538719fbf4076e82fe3319c037ee3c828
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `comment` | `string` |
| `distributed_attachments` | `RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedAttachmentsItem[]` |
| `response_name` | `string` |
| `submittal_response` | `RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedResponsesItemSubmittalResponse` |
| `submittal_response_id` | `int` |
| `submittal_approver_id` | `int` |
| `user_id` | `int` |
| `user` | `RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedBy` |

## RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedResponsesItemSubmittalResponse
- Role: nested
- Parent: RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchResponse200DistributedResponsesItemSubmittalResponse
- Schema ID: schema:anon/94ca6e850de21e5519119cd5d423d9300a396f12

### Fields
