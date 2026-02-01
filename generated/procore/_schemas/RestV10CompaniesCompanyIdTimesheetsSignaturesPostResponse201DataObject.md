# RestV10CompaniesCompanyIdTimesheetsSignaturesPostResponse201DataObject

## RestV10CompaniesCompanyIdTimesheetsSignaturesPostResponse201DataObject
- Role: parent
- Schema Name: RestV10CompaniesCompanyIdTimesheetsSignaturesPostResponse201
- Schema ID: schema:anon/b47158c114ea748df4b65ed45d1666176d65265d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `signature_text` | `string` |
| `file_name` | `string` |
| `url` | `string` |
| `medium_thumbnail_url` | `string` |
| `large_thumbnail_url` | `string` |
| `created_by` | `RestV10CompaniesCompanyIdTimesheetsSignaturesPostResponse201CreatedBy` |

### Nested Types
- `RestV10CompaniesCompanyIdTimesheetsSignaturesPostResponse201CreatedBy`

## RestV10CompaniesCompanyIdTimesheetsSignaturesPostResponse201CreatedBy
- Role: nested
- Parent: RestV10CompaniesCompanyIdTimesheetsSignaturesPostResponse201DataObject
- Schema Name: RestV10CompaniesCompanyIdTimesheetsSignaturesPostResponse201CreatedBy
- Schema ID: schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |
