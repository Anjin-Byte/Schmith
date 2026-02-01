# RestV10TodosSyncPatchResponse200DataObject

## RestV10TodosSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10TodosSyncPatchResponse200
- Schema ID: schema:anon/9572edfff0b24432ecd961bba48f7bba0d3fa229

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10TodosSyncPatchResponse200EntitiesItem[]` |
| `errors` | `RestV10TodosSyncPatchResponse200ErrorsItem[]` |

### Nested Types
- `RestV10TodosSyncPatchResponse200EntitiesItem`
- `RestV10TodosSyncPatchResponse200EntitiesItemAssignment`
- `RestV10TodosSyncPatchResponse200ErrorsItem`
- `RestV10TodosSyncPatchResponse200ErrorsItem_7abdf4Errors`

## RestV10TodosSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10TodosSyncPatchResponse200DataObject
- Schema Name: RestV10TodosSyncPatchResponse200EntitiesItem
- Schema ID: schema:anon/89b0e6d4509db735673e9b924d9442472575e9ab
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `assignment` | `RestV10TodosSyncPatchResponse200EntitiesItemAssignment` |
| `color` | `string` |
| `created_by` | `RestV10TodosSyncPatchResponse200EntitiesItemAssignment` |
| `description` | `string` |
| `finish_datetime` | `string` |
| `full_outline_path` | `string` |
| `milestone` | `bool` |
| `name` | `string` |
| `percentage` | `int` |
| `private` | `bool` |
| `start_datetime` | `string` |
| `task_name` | `string` |
| `updated_at` | `string` |

## RestV10TodosSyncPatchResponse200EntitiesItemAssignment
- Role: nested
- Parent: RestV10TodosSyncPatchResponse200DataObject
- Schema Name: RestV10TodosSyncPatchResponse200EntitiesItemAssignment
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV10TodosSyncPatchResponse200ErrorsItem
- Role: nested
- Parent: RestV10TodosSyncPatchResponse200DataObject
- Schema Name: RestV10TodosSyncPatchResponse200ErrorsItem
- Schema ID: schema:anon/179c765840014191ecb43ccb79e0bcc62f727b83
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `assignment` | `RestV10TodosSyncPatchResponse200EntitiesItemAssignment` |
| `color` | `string` |
| `created_by` | `RestV10TodosSyncPatchResponse200EntitiesItemAssignment` |
| `description` | `string` |
| `finish_datetime` | `string` |
| `full_outline_path` | `string` |
| `milestone` | `bool` |
| `name` | `string` |
| `percentage` | `int` |
| `private` | `bool` |
| `start_datetime` | `string` |
| `task_name` | `string` |
| `updated_at` | `string` |
| `errors` | `RestV10TodosSyncPatchResponse200ErrorsItem_7abdf4Errors` |

## RestV10TodosSyncPatchResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10TodosSyncPatchResponse200DataObject
- Schema Name: RestV10TodosSyncPatchResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
