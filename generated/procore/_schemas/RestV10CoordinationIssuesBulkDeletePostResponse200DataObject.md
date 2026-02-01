# RestV10CoordinationIssuesBulkDeletePostResponse200DataObject

## RestV10CoordinationIssuesBulkDeletePostResponse200DataObject
- Role: parent
- Schema Name: RestV10CoordinationIssuesBulkDeletePostResponse200
- Schema ID: schema:anon/84a49f4ad2bf1a60f5a9b689bf20dae0ad5fa0eb

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10CoordinationIssuesBulkDeletePostResponse200EntitiesItem[]` |
| `errors` | `RestV10CoordinationIssuesBulkDeletePostResponse200ErrorsItem[]` |

### Nested Types
- `RestV10CoordinationIssuesBulkDeletePostResponse200EntitiesItem`
- `RestV10CoordinationIssuesBulkDeletePostResponse200ErrorsItem`
- `RestV10CoordinationIssuesBulkDeletePostResponse200ErrorsItemErrors`

## RestV10CoordinationIssuesBulkDeletePostResponse200EntitiesItem
- Role: nested
- Parent: RestV10CoordinationIssuesBulkDeletePostResponse200DataObject
- Schema Name: RestV10CoordinationIssuesBulkDeletePostResponse200EntitiesItem
- Schema ID: schema:anon/a0d83163c65d125d4046220449e7246b806c6e19
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV10CoordinationIssuesBulkDeletePostResponse200ErrorsItem
- Role: nested
- Parent: RestV10CoordinationIssuesBulkDeletePostResponse200DataObject
- Schema Name: RestV10CoordinationIssuesBulkDeletePostResponse200ErrorsItem
- Schema ID: schema:anon/7abdf4f55a4d2c36a8a9be6450ac089d3cedf818

### Fields

| Field | Type |
|------|------|
| `errors` | `RestV10CoordinationIssuesBulkDeletePostResponse200ErrorsItemErrors` |

## RestV10CoordinationIssuesBulkDeletePostResponse200ErrorsItemErrors
- Role: nested
- Parent: RestV10CoordinationIssuesBulkDeletePostResponse200DataObject
- Schema Name: RestV10CoordinationIssuesBulkDeletePostResponse200ErrorsItemErrors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
