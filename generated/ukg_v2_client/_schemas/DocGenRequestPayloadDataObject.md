# DocGenRequestPayloadDataObject

## DocGenRequestPayloadDataObject
- Role: parent
- Schema Name: DocGenRequestPayload
- Schema ID: schema:definitions/DocGenRequestPayload
- Primary Key: DocumentGenerationTemplateId

### Fields

| Field | Type |
|------|------|
| `fields` | `DatasetField[]` |
| `document_generation_template_id` | `string` |
| `document_generation_template_version` | `int` |
| `output_format` | `DocGenRequestPayloadNestedOutputFormat` |
| `context` | `string` |
| `signature_field_generation` | `bool` |
| `fragment_fields` | `DocGenRequestPayloadNestedFragmentFields` |
| `email_recipients` | `EmailRecipient[]` |
| `employee_id` | `string` |
| `document_type_id` | `string` |

### Nested Types
- `DatasetField`
- `DatasetFieldTypeTypeItem`
- `DocGenRequestPayloadNestedFragmentFields`
- `DocGenRequestPayloadNestedOutputFormat`
- `EmailRecipient`
- `FieldsetField`

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
| `type` | `DatasetFieldTypeTypeItem` |

## DatasetFieldTypeTypeItem
- Role: nested
- Parent: DocGenRequestPayloadDataObject
- Schema Name: DatasetFieldTypeTypeItem
- Schema ID: schema:anon/07b949304bddf335c6eb4571c1c40044809b0b32

### Enum

Values: date

## DocGenRequestPayloadNestedFragmentFields
- Role: nested
- Parent: DocGenRequestPayloadDataObject
- Schema Name: DocGenRequestPayloadNestedFragmentFields
- Schema ID: schema:anon/c24fa5366979853fcc8ab7c4162223ac879e70fa

### Fields

| Field | Type |
|------|------|
| `fragment_placeholder_1` | `FieldsetField[]` |
| `fragment_placeholder_n` | `FieldsetField[]` |

## DocGenRequestPayloadNestedOutputFormat
- Role: nested
- Parent: DocGenRequestPayloadDataObject
- Schema Name: DocGenRequestPayloadNestedOutputFormat
- Schema ID: schema:anon/0fe27827f01ac397db786a6def5abdd521979845

### Enum

Values: DOC, DOCX, ODT, PDF

## EmailRecipient
- Role: nested
- Parent: DocGenRequestPayloadDataObject
- Schema Name: EmailRecipient
- Schema ID: schema:definitions/EmailRecipient

### Fields

| Field | Type |
|------|------|
| `firstname` | `string` |
| `lastname` | `string` |
| `email` | `string` |
| `language` | `string` |

## FieldsetField
- Role: nested
- Parent: DocGenRequestPayloadDataObject
- Schema Name: FieldsetField
- Schema ID: schema:definitions/FieldsetField

### Fields

| Field | Type |
|------|------|
| `slug` | `string` |
