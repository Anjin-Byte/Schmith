# RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataObject

## RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200
- Schema ID: schema:anon/a73754391ea2bc83af1d3f41ab471a1ec7cecc4e

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200Data` |

### Nested Types
- `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200Data`
- `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCurrentStepApproversItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCurrentStepApproversItemUser`
- `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}`
- `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldBooleanDefinitionId}`
- `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldDecimalDefinitionId}`
- `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldLovEntriesDefinitionId}`
- `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldLovEntryDefinitionId}`
- `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldStringDefinitionId}`
- `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataWorkflowStep`

## RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200Data
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200Data
- Schema ID: schema:anon/2297deecd412f53bb696f3d92bda33b8f722f308
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `actual_delivery_date` | `string` |
| `bic_due_date` | `string` |
| `confirmed_delivery_date` | `string` |
| `closed_at` | `string` |
| `cost_code_id` | `string` |
| `current_step_approvers` | `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCurrentStepApproversItem[]` |
| `current_step_returned_date` | `string` |
| `current_step_sent_date` | `string` |
| `custom_textarea_1` | `string` |
| `custom_textfield_1` | `string` |
| `description` | `string` |
| `design_team_review_time` | `int` |
| `distribution_member_ids` | `int[]` |
| `due_date` | `string` |
| `internal_review_time` | `int` |
| `issue_date` | `string` |
| `lead_time` | `int` |
| `location_id` | `string` |
| `number` | `string` |
| `private` | `bool` |
| `received_date` | `string` |
| `received_from_id` | `string` |
| `required_on_site_date` | `string` |
| `responsible_contractor_id` | `string` |
| `revision` | `string` |
| `scheduled_task_key` | `string` |
| `scheduled_task_id` | `string` |
| `specification_section_id` | `string` |
| `status_id` | `string` |
| `sub_job_id` | `string` |
| `submit_by` | `string` |
| `submittal_manager_id` | `string` |
| `submittal_package_id` | `string` |
| `title` | `string` |
| `type` | `string` |
| `workflow_step` | `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataWorkflowStep` |
| `custom_field_%{custom_field_definition_id}` | `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}` |

## RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCurrentStepApproversItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCurrentStepApproversItem
- Schema ID: schema:anon/42aa74f42c877e23c3248ce910db37b0b1a9f760
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `response_required` | `bool` |
| `user` | `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCurrentStepApproversItemUser` |

## RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCurrentStepApproversItemUser
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCurrentStepApproversItemUser
- Schema ID: schema:anon/8b16be3dc90100d9211c750bfb4edfd1cb4820d1
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}
- Schema ID: schema:anon/945ccf10451f1e4837da89c9064f5fe7f0c5b2d8

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldLovEntriesDefinitionId}` |

## RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/d7aaf7e4245f8b5e58720e73973a9fdbdbc7839e

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/8178757753fe7302f7d5443936cb13b481bd73ff

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/11942ee21babd79c37fa67ef23c50643a350a663

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/3512bc5ce3954295effa720ff5602c3d1076df0b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `label` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/3e34a2fbca2d3c7cf85c26f1acb7e30b1c73cf5f

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/b07f73fdf1f25cd338033e3db7d8098ffe3052d1
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `label` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataCustomField%{customFieldDefinitionId}CustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/8c3d88cb61be32fb0e8459abd64e13d194ffdb10

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |

## RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataWorkflowStep
- Role: nested
- Parent: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdProjectsProjectIdSubmittalsGetResponse200DataWorkflowStep
- Schema ID: schema:anon/98b313127d745be896e97f613a232561f6d5295e

### Fields

| Field | Type |
|------|------|
| `current_step` | `int` |
| `total_steps` | `int` |
| `days_late` | `int` |
