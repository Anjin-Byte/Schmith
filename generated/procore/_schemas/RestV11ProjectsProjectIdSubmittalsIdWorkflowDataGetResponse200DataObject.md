# RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGetResponse200DataObject

## RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGetResponse200DataObject
- Role: parent
- Schema Name: RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGetResponse200
- Schema ID: schema:anon/d14797b89021759f30e205bf00db84d6a9c85979

### Fields

| Field | Type |
|------|------|
| `steps` | `RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGetResponse200StepsItem[]` |
| `approvers` | `RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGetResponse200ApproversItem[]` |
| `attachments` | `RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGetResponse200AttachmentsItem[]` |

### Nested Types
- `RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGetResponse200ApproversItem`
- `RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGetResponse200AttachmentsItem`
- `RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGetResponse200StepsItem`

## RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGetResponse200ApproversItem
- Role: nested
- Parent: RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGetResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGetResponse200ApproversItem
- Schema ID: schema:anon/fa56e78574a0c7c4d212ae70d82154b12c90cc33
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `attachment_ids` | `int[]` |
| `company_name` | `string` |
| `name` | `string` |
| `days_to_respond` | `int` |
| `response_required` | `bool` |

## RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGetResponse200AttachmentsItem
- Role: nested
- Parent: RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGetResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGetResponse200AttachmentsItem
- Schema ID: schema:anon/81298605040706b801fe8f1a73f436e315df426f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `approver_id` | `int` |
| `approver_marked_up_at` | `string` |
| `can_carry_forward` | `bool` |
| `download_url` | `string` |
| `has_failed` | `bool` |
| `is_originating_attachment` | `bool` |
| `is_processing` | `bool` |
| `last_marked_up_at` | `string` |
| `last_marked_up_by` | `string` |
| `name` | `string` |
| `viewer_type` | `string` |
| `viewer_url` | `string` |

## RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGetResponse200StepsItem
- Role: nested
- Parent: RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGetResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGetResponse200StepsItem
- Schema ID: schema:anon/6612211442cee0c942424880c831eeb673e420f0
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `approver_ids` | `int[]` |
| `number` | `int` |
