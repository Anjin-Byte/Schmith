# EventBaseDataObject

## EventBaseDataObject
- Role: parent
- Schema Name: EventBase
- Schema ID: schema:definitions/EventBase
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `type` | `string` |
| `name` | `string` |
| `created_at` | `string` |
| `actor` | `EventActor` |
| `data` | `object` |

### Nested Types
- `EventActor`

## EventActor
- Role: nested
- Parent: EventBaseDataObject
- Schema Name: EventActor
- Schema ID: schema:definitions/EventActor
- Primary Key: Type

### Fields

| Field | Type |
|------|------|
| `type` | `TypeEnum` |
| `name` | `string` |
| `data` | `object` |
