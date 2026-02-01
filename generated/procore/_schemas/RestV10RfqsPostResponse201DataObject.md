# RestV10RfqsPostResponse201DataObject

## RestV10RfqsPostResponse201DataObject
- Role: parent
- Schema Name: RestV10RfqsPostResponse201
- Schema ID: schema:anon/7143c342ddbb1ad2b899845bb1b86a1d1753109f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `commitment_contract_id` | `int` |
| `created_at` | `string` |
| `description` | `string` |
| `due_date` | `string` |
| `estimated_amount` | `double` |
| `estimated_schedule_impact` | `int` |
| `estimated_status` | `RestV10RfqsPostResponse201EstimatedStatus` |
| `intent_to_quote` | `bool` |
| `number` | `string` |
| `original_quote` | `double` |
| `position` | `int` |
| `private` | `bool` |
| `prostore_file_ids` | `int[]` |
| `status` | `RestV10RfqsPostResponse201Status` |
| `title` | `string` |
| `updated_at` | `string` |
| `specification_section` | `RestV10RfqsPostResponse201SpecificationSection` |
| `created_by` | `RestV10RfqsPostResponse201CreatedBy` |
| `assigned` | `RestV10RfqsPostResponse201CreatedBy` |
| `location` | `RestV10RfqsPostResponse201Location` |
| `cost_code` | `RestV10RfqsPostResponse201CostCode` |
| `currency_configuration` | `RestV10RfqsPostResponse201CurrencyConfiguration` |

### Nested Types
- `Anonymous_88ecc10dBillerType`
- `Anonymous_88ecc10dLineItemTypesItem`
- `Anonymous_88ecc10dLineItemTypesItemBaseType`
- `Anonymous_88ecc10dParent`
- `RestV10RfqsPostResponse201CostCode`
- `RestV10RfqsPostResponse201CreatedBy`
- `RestV10RfqsPostResponse201CurrencyConfiguration`
- `RestV10RfqsPostResponse201EstimatedStatus`
- `RestV10RfqsPostResponse201Location`
- `RestV10RfqsPostResponse201SpecificationSection`
- `RestV10RfqsPostResponse201Status`

## Anonymous_88ecc10dBillerType
- Role: nested
- Parent: RestV10RfqsPostResponse201DataObject
- Schema Name: Anonymous_88ecc10dBillerType
- Schema ID: schema:anon/6ce4c07d2fb83b79d4fcb225c5c9c05691bcdc4d

### Enum

Values: Project, SubJob

## Anonymous_88ecc10dLineItemTypesItem
- Role: nested
- Parent: RestV10RfqsPostResponse201DataObject
- Schema Name: Anonymous_88ecc10dLineItemTypesItem
- Schema ID: schema:anon/b78a87f17b509f5904f1a9e8b840af217e95b3fc
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `code` | `string` |
| `base_type` | `Anonymous_88ecc10dLineItemTypesItemBaseType` |
| `origin_data` | `string` |
| `origin_id` | `string` |

## Anonymous_88ecc10dLineItemTypesItemBaseType
- Role: nested
- Parent: RestV10RfqsPostResponse201DataObject
- Schema Name: Anonymous_88ecc10dLineItemTypesItemBaseType
- Schema ID: schema:anon/c1a066154239ac3e29e59285e26bd77f996807bf

### Enum

Values: equipment, materials, commitment, owner_cost, professional_services, other

## Anonymous_88ecc10dParent
- Role: nested
- Parent: RestV10RfqsPostResponse201DataObject
- Schema Name: Anonymous_88ecc10dParent
- Schema ID: schema:anon/44768f5b771296b189deec792bd565b414bae19b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV10RfqsPostResponse201CostCode
- Role: nested
- Parent: RestV10RfqsPostResponse201DataObject
- Schema Name: RestV10RfqsPostResponse201CostCode
- Schema ID: schema:anon/7b94f1df2e808d88fd5afc25464a20b4905f7763
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `full_code` | `string` |
| `name` | `string` |
| `biller` | `string` |
| `biller_id` | `int` |
| `biller_type` | `Anonymous_88ecc10dBillerType` |
| `budgeted` | `bool` |
| `code` | `string` |
| `created_at` | `string` |
| `deleted_at` | `string` |
| `origin_data` | `string` |
| `origin_id` | `string` |
| `parent` | `Anonymous_88ecc10dParent` |
| `position` | `int` |
| `sortable_code` | `string` |
| `standard_cost_code_id` | `int` |
| `standard_cost_code_list_id` | `int` |
| `updated_at` | `string` |
| `line_item_types` | `Anonymous_88ecc10dLineItemTypesItem[]` |

## RestV10RfqsPostResponse201CreatedBy
- Role: nested
- Parent: RestV10RfqsPostResponse201DataObject
- Schema Name: RestV10RfqsPostResponse201CreatedBy
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10RfqsPostResponse201CurrencyConfiguration
- Role: nested
- Parent: RestV10RfqsPostResponse201DataObject
- Schema Name: RestV10RfqsPostResponse201CurrencyConfiguration
- Schema ID: schema:anon/604508c10ceb4d00db265015715c4f3c345909ea

### Fields

| Field | Type |
|------|------|
| `base_currency_iso_code` | `string` |
| `currency_iso_code` | `string` |

## RestV10RfqsPostResponse201EstimatedStatus
- Role: nested
- Parent: RestV10RfqsPostResponse201DataObject
- Schema Name: RestV10RfqsPostResponse201EstimatedStatus
- Schema ID: schema:anon/114721f2104991ff06a343266786174cc15c5768

### Enum

Values: rom, final

## RestV10RfqsPostResponse201Location
- Role: nested
- Parent: RestV10RfqsPostResponse201DataObject
- Schema Name: RestV10RfqsPostResponse201Location
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

## RestV10RfqsPostResponse201SpecificationSection
- Role: nested
- Parent: RestV10RfqsPostResponse201DataObject
- Schema Name: RestV10RfqsPostResponse201SpecificationSection
- Schema ID: schema:anon/39c64db7687c559ef8ec9df853de72b09a549e4e
- Primary Key: SpecificationSectionId

### Fields

| Field | Type |
|------|------|
| `specification_section_id` | `int` |
| `spec_section_description` | `string` |
| `spec_section_number` | `string` |

## RestV10RfqsPostResponse201Status
- Role: nested
- Parent: RestV10RfqsPostResponse201DataObject
- Schema Name: RestV10RfqsPostResponse201Status
- Schema ID: schema:anon/2e1d2ea57e6cf3695a3127ca4a32ff76c02255bf

### Enum

Values: out_for_pricing, revise_and_resubmit, under_review, pending_final_approval, closed, withdrawn
