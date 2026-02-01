# RestV10SubmittalLogsIdGetResponse200DataObject

## RestV10SubmittalLogsIdGetResponse200DataObject
- Role: parent
- Schema Name: RestV10SubmittalLogsIdGetResponse200
- Schema ID: schema:anon/524f765bed060230b8eee0e00c10d5f94c9d585a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `title` | `string` |
| `number` | `string` |
| `formatted_number` | `string` |
| `revision` | `string` |
| `private` | `bool` |
| `received_date` | `string` |
| `issue_date` | `string` |
| `submit_by` | `string` |
| `due_date` | `string` |
| `type` | `string` |
| `description` | `string` |
| `status` | `string` |
| `closed` | `bool` |
| `created_by` | `RestV10SubmittalLogsIdGetResponse200CreatedBy` |
| `received_from` | `RestV10SubmittalLogsIdGetResponse200ReceivedFrom` |
| `approvers` | `RestV10SubmittalLogsIdGetResponse200ApproversItem[]` |
| `distribution_members` | `RestV10SubmittalLogsIdGetResponse200ApproversItemLoginInformation[]` |
| `ball_in_court` | `RestV10SubmittalLogsIdGetResponse200ApproversItemLoginInformation[]` |
| `location` | `RestV10SubmittalLogsIdGetResponse200Location` |
| `specification_section` | `RestV10SubmittalLogsIdGetResponse200SpecificationSection` |
| `attachments` | `RestV10SubmittalLogsIdGetResponse200ApproversItemAttachmentsItem[]` |
| `distribution_info` | `RestV10SubmittalLogsIdGetResponse200DistributionInfo` |
| `submittal_package` | `RestV10SubmittalLogsIdGetResponse200SubmittalPackage` |

### Nested Types
- `RestV10SubmittalLogsIdGetResponse200ApproversItem`
- `RestV10SubmittalLogsIdGetResponse200ApproversItemAttachmentsItem`
- `RestV10SubmittalLogsIdGetResponse200ApproversItemLoginInformation`
- `RestV10SubmittalLogsIdGetResponse200CreatedBy`
- `RestV10SubmittalLogsIdGetResponse200DistributionInfo`
- `RestV10SubmittalLogsIdGetResponse200Location`
- `RestV10SubmittalLogsIdGetResponse200ReceivedFrom`
- `RestV10SubmittalLogsIdGetResponse200SpecificationSection`
- `RestV10SubmittalLogsIdGetResponse200SubmittalPackage`

## RestV10SubmittalLogsIdGetResponse200ApproversItem
- Role: nested
- Parent: RestV10SubmittalLogsIdGetResponse200DataObject
- Schema Name: RestV10SubmittalLogsIdGetResponse200ApproversItem
- Schema ID: schema:anon/6eef1a849646d53bae6ad179f335395f57ca3a00
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `login_information` | `RestV10SubmittalLogsIdGetResponse200ApproversItemLoginInformation` |
| `id` | `int` |
| `response` | `string` |
| `sent_date` | `string` |
| `returned_date` | `string` |
| `due_date` | `string` |
| `days_to_respond` | `int` |
| `comment` | `string` |
| `distributed` | `int[]` |
| `attachments` | `RestV10SubmittalLogsIdGetResponse200ApproversItemAttachmentsItem[]` |

## RestV10SubmittalLogsIdGetResponse200ApproversItemAttachmentsItem
- Role: nested
- Parent: RestV10SubmittalLogsIdGetResponse200DataObject
- Schema Name: RestV10SubmittalLogsIdGetResponse200ApproversItemAttachmentsItem
- Schema ID: schema:anon/c337dee3df228286468f0ff6d8c4852152f75cf4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |

## RestV10SubmittalLogsIdGetResponse200ApproversItemLoginInformation
- Role: nested
- Parent: RestV10SubmittalLogsIdGetResponse200DataObject
- Schema Name: RestV10SubmittalLogsIdGetResponse200ApproversItemLoginInformation
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10SubmittalLogsIdGetResponse200CreatedBy
- Role: nested
- Parent: RestV10SubmittalLogsIdGetResponse200DataObject
- Schema Name: RestV10SubmittalLogsIdGetResponse200CreatedBy
- Schema ID: schema:anon/699c9a55bf570e9a7e76594242ce0323403fcd79
- Primary Key: LoginId

### Fields

| Field | Type |
|------|------|
| `name` | `string` |
| `login` | `string` |
| `login_id` | `int` |

## RestV10SubmittalLogsIdGetResponse200DistributionInfo
- Role: nested
- Parent: RestV10SubmittalLogsIdGetResponse200DataObject
- Schema Name: RestV10SubmittalLogsIdGetResponse200DistributionInfo
- Schema ID: schema:anon/5acca03ea774e3127f04a8208f97a88bc933f609
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `message` | `string` |
| `distributed_date` | `string` |
| `distributed_by` | `RestV10SubmittalLogsIdGetResponse200ApproversItemLoginInformation` |
| `distributed_to` | `RestV10SubmittalLogsIdGetResponse200ApproversItemLoginInformation[]` |
| `final_attachments` | `RestV10SubmittalLogsIdGetResponse200ApproversItemAttachmentsItem[]` |

## RestV10SubmittalLogsIdGetResponse200Location
- Role: nested
- Parent: RestV10SubmittalLogsIdGetResponse200DataObject
- Schema Name: RestV10SubmittalLogsIdGetResponse200Location
- Schema ID: schema:anon/7d4098f2df6d84102332d015429ec5ed48bef6c6
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `node_name` | `string` |
| `parent_id` | `int` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV10SubmittalLogsIdGetResponse200ReceivedFrom
- Role: nested
- Parent: RestV10SubmittalLogsIdGetResponse200DataObject
- Schema Name: RestV10SubmittalLogsIdGetResponse200ReceivedFrom
- Schema ID: schema:anon/3b52070df9d0795800389e6ee0e7a156a7923447
- Primary Key: LoginId

### Fields

| Field | Type |
|------|------|
| `name` | `string` |
| `login` | `string` |
| `login_id` | `int` |

## RestV10SubmittalLogsIdGetResponse200SpecificationSection
- Role: nested
- Parent: RestV10SubmittalLogsIdGetResponse200DataObject
- Schema Name: RestV10SubmittalLogsIdGetResponse200SpecificationSection
- Schema ID: schema:anon/0be24eb5392eecca425896a45a5bc9c76a111cea
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `description` | `string` |
| `section` | `string` |

## RestV10SubmittalLogsIdGetResponse200SubmittalPackage
- Role: nested
- Parent: RestV10SubmittalLogsIdGetResponse200DataObject
- Schema Name: RestV10SubmittalLogsIdGetResponse200SubmittalPackage
- Schema ID: schema:anon/be61b6357570b1e6a83a82defd84603a5633ef30
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `title` | `string` |
| `created_by` | `RestV10SubmittalLogsIdGetResponse200ApproversItemLoginInformation` |
| `description` | `string` |
| `attachments` | `RestV10SubmittalLogsIdGetResponse200ApproversItemAttachmentsItem[]` |
