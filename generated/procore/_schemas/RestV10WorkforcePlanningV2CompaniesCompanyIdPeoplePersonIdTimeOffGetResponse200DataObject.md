# RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200DataObject

## RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200DataObject
- Role: parent
- Schema Name: RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200
- Schema ID: schema:anon/76b62fe918c1185fd1517f12faf4dddcc4432e6b

### Fields

| Field | Type |
|------|------|
| `data` | `RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200DataItem[]` |
| `pagination` | `RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200Pagination` |

### Nested Types
- `RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200DataItem`
- `RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200DataItemInstancesItem`
- `RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200DataItemRepeat`
- `RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200Pagination`

## RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200DataItem
- Role: nested
- Parent: RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200DataObject
- Schema Name: RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200DataItem
- Schema ID: schema:anon/86b024495387b83bca8220b8ebe7ec2a433dd50c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `person_id` | `string` |
| `company_id` | `string` |
| `start_day` | `string` |
| `end_day` | `string` |
| `is_paid` | `bool` |
| `reason` | `string` |
| `repeat` | `RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200DataItemRepeat` |
| `repeat_end_day` | `string` |
| `cadence` | `int` |
| `apply_to_saturday` | `bool` |
| `apply_to_sunday` | `bool` |
| `batch_start_time` | `string` |
| `batch_end_time` | `string` |
| `instances` | `RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200DataItemInstancesItem[]` |

## RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200DataItemInstancesItem
- Role: nested
- Parent: RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200DataObject
- Schema Name: RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200DataItemInstancesItem
- Schema ID: schema:anon/5a1ae214bdd84ceb5660f6ae72dab576fdc084c2
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `start_day` | `string` |
| `end_day` | `string` |

## RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200DataItemRepeat
- Role: nested
- Parent: RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200DataObject
- Schema Name: RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200DataItemRepeat
- Schema ID: schema:anon/abb8f888f98ef7f8a7b7450cc835f35c4890ecf2

### Enum

Values: never, weekly, monthly, yearly

## RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200Pagination
- Role: nested
- Parent: RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200DataObject
- Schema Name: RestV10WorkforcePlanningV2CompaniesCompanyIdPeoplePersonIdTimeOffGetResponse200Pagination
- Schema ID: schema:anon/d057c3bc1cf71a867d560d2bb1ac6a74afad1c30

### Fields

| Field | Type |
|------|------|
| `limit` | `int` |
| `next_starting_after` | `string` |
| `previous_starting_before` | `string` |
| `total_possible` | `int` |
