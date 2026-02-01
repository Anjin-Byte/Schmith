# RestV10RequestedChangesGetResponse200DataObject

## RestV10RequestedChangesGetResponse200DataObject
- Role: parent
- Schema Name: RestV10RequestedChangesGetResponse200
- Schema ID: schema:anon/7cc0bb2726581be0d18ab239b50cfe15cfb174b1

### Fields

| Field | Type |
|------|------|
| `requested_changes` | `RestV10RequestedChangesGetResponse200RequestedChangesItem[]` |

### Nested Types
- `RestV10RequestedChangesGetResponse200RequestedChangesItem`
- `RestV10RequestedChangesGetResponse200RequestedChangesItemStatus`
- `RestV10RequestedChangesGetResponse200RequestedChangesItemStatusNotLocalized`

## RestV10RequestedChangesGetResponse200RequestedChangesItem
- Role: nested
- Parent: RestV10RequestedChangesGetResponse200DataObject
- Schema Name: RestV10RequestedChangesGetResponse200RequestedChangesItem
- Schema ID: schema:anon/12e9b64795d6b98e75e60c37f244e70a5b7035de
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `requested_by` | `string` |
| `change_requested` | `string` |
| `reason` | `string` |
| `status` | `RestV10RequestedChangesGetResponse200RequestedChangesItemStatus` |
| `status_not_localized` | `RestV10RequestedChangesGetResponse200RequestedChangesItemStatusNotLocalized` |
| `notes` | `string` |

## RestV10RequestedChangesGetResponse200RequestedChangesItemStatus
- Role: nested
- Parent: RestV10RequestedChangesGetResponse200DataObject
- Schema Name: RestV10RequestedChangesGetResponse200RequestedChangesItemStatus
- Schema ID: schema:anon/59ddf52d3a440b3352ed2296f665fadafab5e633

### Enum

Values: Approved, Rejected, Pending

## RestV10RequestedChangesGetResponse200RequestedChangesItemStatusNotLocalized
- Role: nested
- Parent: RestV10RequestedChangesGetResponse200DataObject
- Schema Name: RestV10RequestedChangesGetResponse200RequestedChangesItemStatusNotLocalized
- Schema ID: schema:anon/c242e8970f2ef4ac6ee3d98d0ad5f939b72912e1

### Enum

Values: approved, rejected, pending
