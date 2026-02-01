# RestV11ChangeEventsNewGetResponse200DataObject

## RestV11ChangeEventsNewGetResponse200DataObject
- Role: parent
- Schema Name: RestV11ChangeEventsNewGetResponse200
- Schema ID: schema:anon/e8646da8cc6994ca81ba3367046b8e6fd607a724
- Primary Key: CompanyId

### Fields

| Field | Type |
|------|------|
| `company_id` | `int` |
| `project_id` | `int` |
| `number` | `string` |
| `scope` | `string` |
| `status` | `RestV11ChangeEventsNewGetResponse200Status` |
| `event_origin` | `RestV11ChangeEventsNewGetResponse200EventOrigin` |
| `change_type` | `RestV11ChangeEventsNewGetResponse200ChangeType` |
| `prime_contract_for_estimates` | `RestV11ChangeEventsNewGetResponse200PrimeContractForEstimates` |

### Nested Types
- `RestV11ChangeEventsNewGetResponse200ChangeType`
- `RestV11ChangeEventsNewGetResponse200EventOrigin`
- `RestV11ChangeEventsNewGetResponse200PrimeContractForEstimates`
- `RestV11ChangeEventsNewGetResponse200Status`

## RestV11ChangeEventsNewGetResponse200ChangeType
- Role: nested
- Parent: RestV11ChangeEventsNewGetResponse200DataObject
- Schema Name: RestV11ChangeEventsNewGetResponse200ChangeType
- Schema ID: schema:anon/67d4093adb8397a1da3b834908452a706a220ab4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV11ChangeEventsNewGetResponse200EventOrigin
- Role: nested
- Parent: RestV11ChangeEventsNewGetResponse200DataObject
- Schema Name: RestV11ChangeEventsNewGetResponse200EventOrigin
- Schema ID: schema:anon/637540762dd81351f5d80dbb521d39009c3af85c
- Primary Key: OriginId

### Fields

| Field | Type |
|------|------|
| `origin_id` | `int` |
| `origin_type` | `string` |

## RestV11ChangeEventsNewGetResponse200PrimeContractForEstimates
- Role: nested
- Parent: RestV11ChangeEventsNewGetResponse200DataObject
- Schema Name: RestV11ChangeEventsNewGetResponse200PrimeContractForEstimates
- Schema ID: schema:anon/b9dbf838f4d563ea11015de9377df7bb9230aaa4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV11ChangeEventsNewGetResponse200Status
- Role: nested
- Parent: RestV11ChangeEventsNewGetResponse200DataObject
- Schema Name: RestV11ChangeEventsNewGetResponse200Status
- Schema ID: schema:anon/8d76c3e40eb6cb3ddba51d153d7df4614f3d7ddf
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
