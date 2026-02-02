# ImportCreatePayloadDataObject

## ImportCreatePayloadDataObject
- Role: parent
- Schema Name: ImportCreatePayload
- Schema ID: schema:definitions/ImportCreatePayload

### Fields

| Field | Type |
|------|------|
| `type` | `ImportBaseType` |
| `creator` | `string` |
| `uploaded_file` | `DocumentFileId` |

### Nested Types
- `DocumentFileId`
- `ImportBaseType`

## DocumentFileId
- Role: nested
- Parent: ImportCreatePayloadDataObject
- Schema Name: DocumentFileId
- Schema ID: schema:definitions/DocumentFileId
- Primary Key: FileId

### Fields

| Field | Type |
|------|------|
| `filename` | `string` |
| `file_id` | `string` |

## ImportBaseType
- Role: nested
- Parent: ImportCreatePayloadDataObject
- Schema Name: ImportBaseType
- Schema ID: schema:anon/0e325a09191808a827013f95b158266db695cc5c

### Enum

Values: employee, manager, organization
