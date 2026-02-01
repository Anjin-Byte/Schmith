# RestV10ChecklistPossibleInspectorsGetResponse200DataObject

## RestV10ChecklistPossibleInspectorsGetResponse200DataObject
- Role: parent
- Schema Name: RestV10ChecklistPossibleInspectorsGetResponse200
- Schema ID: schema:anon/b3a6a95ec8dc820176379206966a7d215cc37085

### Fields

| Field | Type |
|------|------|
| `people` | `RestV10ChecklistPossibleInspectorsGetResponse200PeopleItem[]` |

### Nested Types
- `RestV10ChecklistPossibleInspectorsGetResponse200PeopleItem`
- `RestV10ChecklistPossibleInspectorsGetResponse200PeopleItemCompany`

## RestV10ChecklistPossibleInspectorsGetResponse200PeopleItem
- Role: nested
- Parent: RestV10ChecklistPossibleInspectorsGetResponse200DataObject
- Schema Name: RestV10ChecklistPossibleInspectorsGetResponse200PeopleItem
- Schema ID: schema:anon/031997004799dbab9f497cf5c076330da926fdbe
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |
| `company` | `RestV10ChecklistPossibleInspectorsGetResponse200PeopleItemCompany` |

## RestV10ChecklistPossibleInspectorsGetResponse200PeopleItemCompany
- Role: nested
- Parent: RestV10ChecklistPossibleInspectorsGetResponse200DataObject
- Schema Name: RestV10ChecklistPossibleInspectorsGetResponse200PeopleItemCompany
- Schema ID: schema:anon/cffbc82fd64e4d54a985ec2fcd96d45f1ef53b59
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
