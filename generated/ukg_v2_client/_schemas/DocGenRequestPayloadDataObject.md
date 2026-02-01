# DocGenRequestPayloadDataObject

## DocGenRequestPayloadDataObject
- Role: parent
- Schema Name: DocGenRequestPayload
- Schema ID: schema:definitions/DocGenRequestPayload

### Fields

| Field | Type |
|------|------|
| `fields` | `DatasetField[]` |

### Nested Types
- `DatasetField`
- `DatasetFieldTypeType`

## DatasetField
- Role: nested
- Parent: DocGenRequestPayloadDataObject
- Schema Name: DatasetField
- Schema ID: schema:definitions/DatasetField

### Fields

| Field | Type |
|------|------|
| `slug` | `string` |
| `value` | `string` |
| `type` | `DatasetFieldTypeType` |

## DatasetFieldTypeType
- Role: nested
- Parent: DocGenRequestPayloadDataObject
- Schema Name: DatasetFieldTypeType
- Schema ID: schema:anon/07b949304bddf335c6eb4571c1c40044809b0b32

### Enum

Values: date
