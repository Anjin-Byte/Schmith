# RestV10ProjectsGetResponsedefaultDataObject

## RestV10ProjectsGetResponsedefaultDataObject
- Role: parent
- Schema Name: RestV10ProjectsGetResponsedefault
- Schema ID: schema:anon/6ac5b0992860452da4dae2cd26ae5e254d3ad712

### Fields

| Field | Type |
|------|------|
| `error` | `RestV10ProjectsGetResponsedefaultError` |

### Nested Types
- `RestV10ProjectsGetResponsedefaultError`
- `RestV10ProjectsGetResponsedefaultErrorDetailsItem`

## RestV10ProjectsGetResponsedefaultError
- Role: nested
- Parent: RestV10ProjectsGetResponsedefaultDataObject
- Schema Name: RestV10ProjectsGetResponsedefaultError
- Schema ID: schema:anon/c0554aa0bb8998919136a0ae344ad20f8c41160e

### Fields

| Field | Type |
|------|------|
| `code` | `string` |
| `message` | `string` |
| `details` | `RestV10ProjectsGetResponsedefaultErrorDetailsItem[]` |

## RestV10ProjectsGetResponsedefaultErrorDetailsItem
- Role: nested
- Parent: RestV10ProjectsGetResponsedefaultDataObject
- Schema Name: RestV10ProjectsGetResponsedefaultErrorDetailsItem
- Schema ID: schema:anon/84b9b797c06fcdd844054d0b6897399f784dcf0e

### Fields

| Field | Type |
|------|------|
| `code` | `string` |
| `message` | `string` |
| `source` | `string` |
