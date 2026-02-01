# RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201
- Schema ID: schema:anon/f6ee8e644fb41d7946b291762765a1123101a427

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201Data` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201Data`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrence`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceAvailableResponseOptionsItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceNotificationRecipientsItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceNotificationRecipientsItemCompany`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceResponseOccurrencesItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceResponseOccurrencesItemAssignee`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceResponseOccurrencesItemAssigneeCompany`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceResponseOccurrencesItemAttachmentsItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceResponseOccurrencesItemSelectedResponseOption`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceStepHistoriesItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceStepHistoriesItemDetailsItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceStepHistoriesItemDetailsItemFieldsItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataResponsibleGroupMembershipsItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataResponsibleGroupMembershipsItemAssigneesItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataWorkflowManager`
- `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataWorkflowManagerCompany`

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201Data
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201Data
- Schema ID: schema:anon/9b24c4c16e3640ba999555c924f5947a8e7e0f34
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `tool_type` | `string` |
| `tool_subtype` | `string` |
| `item_id` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `started_at` | `string` |
| `ended_at` | `string` |
| `current_step_occurrence` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrence` |
| `workflow_manager` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataWorkflowManager` |
| `responsible_group_memberships` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataResponsibleGroupMembershipsItem[]` |
| `all_assignees` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceNotificationRecipientsItem[]` |
| `template_version_id` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrence
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrence
- Schema ID: schema:anon/aa2f867bdac674a98b2a77f5b3a977505c330b60
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `step_uuid` | `string` |
| `name` | `string` |
| `started_at` | `string` |
| `overdue_at` | `string` |
| `step_histories` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceStepHistoriesItem[]` |
| `available_response_options` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceAvailableResponseOptionsItem[]` |
| `notification_recipients` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceNotificationRecipientsItem[]` |
| `response_occurrences` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceResponseOccurrencesItem[]` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceAvailableResponseOptionsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceAvailableResponseOptionsItem
- Schema ID: schema:anon/4ed6738abc06a139d0df792a1a80f41bddc1a494
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `response_type` | `string` |
| `name` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceNotificationRecipientsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceNotificationRecipientsItem
- Schema ID: schema:anon/12c62ae13b4a6573d75a3028c558ce33a3b7a0bd
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |
| `login` | `string` |
| `company` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceNotificationRecipientsItemCompany` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceNotificationRecipientsItemCompany
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceNotificationRecipientsItemCompany
- Schema ID: schema:anon/a4abaeac776994400a8a7bdd99925ba5b0ae9086

### Fields

| Field | Type |
|------|------|
| `name` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceResponseOccurrencesItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceResponseOccurrencesItem
- Schema ID: schema:anon/be6bd31914d03c705c5123f9327a65fa666e94d8

### Fields

| Field | Type |
|------|------|
| `submitted_at` | `string` |
| `selected_response_option` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceResponseOccurrencesItemSelectedResponseOption` |
| `comment` | `string` |
| `attachments` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceResponseOccurrencesItemAttachmentsItem[]` |
| `assignee` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceResponseOccurrencesItemAssignee` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceResponseOccurrencesItemAssignee
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceResponseOccurrencesItemAssignee
- Schema ID: schema:anon/4e9bcc26d3fa5a425849ac1c21287f5ffb6c5d44
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `login` | `string` |
| `name` | `string` |
| `company` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceResponseOccurrencesItemAssigneeCompany` |
| `required` | `bool` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceResponseOccurrencesItemAssigneeCompany
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceResponseOccurrencesItemAssigneeCompany
- Schema ID: schema:anon/536568a86058d6cea011c06502b8e2162cbada6d

### Fields

| Field | Type |
|------|------|
| `name` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceResponseOccurrencesItemAttachmentsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceResponseOccurrencesItemAttachmentsItem
- Schema ID: schema:anon/5652733484945025c609f4df9516ece94372a35f

### Fields

| Field | Type |
|------|------|
| `name` | `string` |
| `url` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceResponseOccurrencesItemSelectedResponseOption
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceResponseOccurrencesItemSelectedResponseOption
- Schema ID: schema:anon/6614d833a9bab7a9ecf3e21f8b3e45095513e108
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `response_type` | `string` |
| `name` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceStepHistoriesItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceStepHistoriesItem
- Schema ID: schema:anon/70c5d18b61dc707d3a4a4bed6ccad8a6ecc543e5

### Fields

| Field | Type |
|------|------|
| `title` | `string` |
| `subtitle` | `string` |
| `created_at` | `string` |
| `icon` | `string` |
| `details` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceStepHistoriesItemDetailsItem[]` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceStepHistoriesItemDetailsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceStepHistoriesItemDetailsItem
- Schema ID: schema:anon/5a38179fab2e06e7eea22863102bb0a346c5c527

### Fields

| Field | Type |
|------|------|
| `title` | `string` |
| `description` | `string` |
| `subtitle` | `string` |
| `icon` | `string` |
| `fields` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceStepHistoriesItemDetailsItemFieldsItem[]` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceStepHistoriesItemDetailsItemFieldsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataCurrentStepOccurrenceStepHistoriesItemDetailsItemFieldsItem
- Schema ID: schema:anon/a9458574f477efd6de79c6f3c77250eeefc8d9aa

### Fields

| Field | Type |
|------|------|
| `label` | `string` |
| `value` | `string` |
| `type` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataResponsibleGroupMembershipsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataResponsibleGroupMembershipsItem
- Schema ID: schema:anon/9e407bd20b31eda77cacaa376a7b8d9fadc564bf

### Fields

| Field | Type |
|------|------|
| `responsible_group_uuid` | `string` |
| `assignees` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataResponsibleGroupMembershipsItemAssigneesItem[]` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataResponsibleGroupMembershipsItemAssigneesItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataResponsibleGroupMembershipsItemAssigneesItem
- Schema ID: schema:anon/4da2a274265f282fa96973adbd1e052475b01c62
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |
| `login` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataWorkflowManager
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataWorkflowManager
- Schema ID: schema:anon/815187ebbedf0e2e48f76d21085acecddfb76e09
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `login` | `string` |
| `name` | `string` |
| `company` | `RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataWorkflowManagerCompany` |

## RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataWorkflowManagerCompany
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdWorkflowsInstancesPostResponse201DataWorkflowManagerCompany
- Schema ID: schema:anon/57ce472e3196601e806400c771d1dee26ad7d105

### Fields

| Field | Type |
|------|------|
| `name` | `string` |
