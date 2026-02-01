# RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201DataObject

## RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201
- Schema ID: schema:anon/9a82b603ff6f21850abcbb524dcbdd14c78bae32

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItem[]` |

### Nested Types
- `RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItem`
- `RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemCostCode`
- `RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemCreatedBy`
- `RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemCrew`
- `RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemCrewEmployeesItem`
- `RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemLocation`
- `RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemSubJob`

## RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItem
- Role: nested
- Parent: RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItem
- Schema ID: schema:anon/1f279f4568d75463ab688146afdeeb6d2b8caa12
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `description` | `string` |
| `unit_of_measure` | `string` |
| `quantity` | `double` |
| `timesheet_id` | `int` |
| `location` | `RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemLocation` |
| `crew` | `RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemCrew` |
| `sub_job` | `RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemSubJob` |
| `updated_at` | `string` |
| `created_at` | `string` |
| `cost_code` | `RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemCostCode` |
| `deleted_at` | `string` |
| `created_by` | `RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemCreatedBy` |
| `date` | `string` |

## RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemCostCode
- Role: nested
- Parent: RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemCostCode
- Schema ID: schema:anon/28452926f132954e8ecd68311996fce9970a48a6

### Fields

## RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemCreatedBy
- Role: nested
- Parent: RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemCreatedBy
- Schema ID: schema:anon/9894030e050b85a91be5dd39e508c057fc4243e5
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemCrew
- Role: nested
- Parent: RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemCrew
- Schema ID: schema:anon/0d3bbebb4e82dca70ea54506bfba795c4b1563af
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `project_id` | `int` |
| `company_id` | `int` |
| `employees` | `RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemCrewEmployeesItem[]` |
| `created_by` | `RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemCrewEmployeesItem` |
| `lead` | `RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemCrewEmployeesItem` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemCrewEmployeesItem
- Role: nested
- Parent: RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemCrewEmployeesItem
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemLocation
- Role: nested
- Parent: RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemLocation
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

## RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemSubJob
- Role: nested
- Parent: RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostResponse201EntitiesItemSubJob
- Schema ID: schema:anon/229af8c0e497a1de396824ecd8e0e29f8b4d8e5b

### Fields
