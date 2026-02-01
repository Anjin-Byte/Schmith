# RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGetResponse200DataObject

## RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGetResponse200DataObject
- Role: parent
- Schema Name: RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGetResponse200
- Schema ID: schema:anon/94ebdf1bc0b52c186d8bbe75ca0f3e5402f6bbe1

### Fields

| Field | Type |
|------|------|
| `pdf_template` | `RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGetResponse200PdfTemplate` |
| `meetings` | `RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGetResponse200MeetingsItem[]` |

### Nested Types
- `RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGetResponse200MeetingsItem`
- `RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGetResponse200PdfTemplate`

## RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGetResponse200MeetingsItem
- Role: nested
- Parent: RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGetResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGetResponse200MeetingsItem
- Schema ID: schema:anon/78f3f23ab3c9e109ed3045194f23adfd51615d2a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `xml` | `string` |

## RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGetResponse200PdfTemplate
- Role: nested
- Parent: RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGetResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGetResponse200PdfTemplate
- Schema ID: schema:anon/6cc36535708c18449ef1f104e9c19edf999c84bd

### Fields

| Field | Type |
|------|------|
| `uuid` | `string` |
| `pdf_filename` | `string` |
| `name` | `string` |
| `url` | `string` |
| `storage_type` | `string` |
