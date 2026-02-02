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
| `data` | `JsonElement` |

### Nested Types
- `EventActor`
- `EventActorType`

## EventActor
- Role: nested
- Parent: EventBaseDataObject
- Schema Name: EventActor
- Schema ID: schema:definitions/EventActor

### Fields

| Field | Type |
|------|------|
| `type` | `EventActorType` |
| `name` | `string` |
| `data` | `JsonElement` |

## EventActorType
- Role: nested
- Parent: EventBaseDataObject
- Schema Name: EventActorType
- Schema ID: schema:anon/81cb7f1d9d8dc3887763ce93ffd50cf032fd9511

### Enum

Values: user, employee, application, system
