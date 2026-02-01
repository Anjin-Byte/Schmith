# FormidableCreatePayloadDataObject

## FormidableCreatePayloadDataObject
- Role: parent
- Schema Name: FormidableCreatePayload
- Schema ID: schema:definitions/FormidableCreatePayload

### Fields

| Field | Type |
|------|------|
| `title` | `string` |
| `description` | `string` |
| `fields` | `FormidableField[]` |
| `conditions` | `FormidableConditionalRule[]` |

### Nested Types
- `FormidableConditionalRule`
- `FormidableConditionalRuleAction`
- `FormidableConditionalRuleTest`
- `FormidableConditionalRuleTestOperator`
- `FormidableField`
- `FormidableFieldItems`
- `FormidableFieldTypeId`
- `FormidableFieldValidation`
- `FormidableFieldValidationType`

## FormidableConditionalRule
- Role: nested
- Parent: FormidableCreatePayloadDataObject
- Schema Name: FormidableConditionalRule
- Schema ID: schema:definitions/FormidableConditionalRule

### Fields

| Field | Type |
|------|------|
| `fields_ids` | `string[]` |
| `action` | `FormidableConditionalRuleAction` |
| `tests` | `FormidableConditionalRuleTest[]` |

## FormidableConditionalRuleAction
- Role: nested
- Parent: FormidableCreatePayloadDataObject
- Schema Name: FormidableConditionalRuleAction
- Schema ID: schema:anon/d5f114e0b3fa376dd19b5f7ffa612552f55c2dc5

### Enum

Values: display_iff

## FormidableConditionalRuleTest
- Role: nested
- Parent: FormidableCreatePayloadDataObject
- Schema Name: FormidableConditionalRuleTest
- Schema ID: schema:definitions/FormidableConditionalRuleTest
- Primary Key: FieldId

### Fields

| Field | Type |
|------|------|
| `field_id` | `string` |
| `operator` | `FormidableConditionalRuleTestOperator` |
| `values` | `FormidableFieldDefaultsItem[]` |

## FormidableConditionalRuleTestOperator
- Role: nested
- Parent: FormidableCreatePayloadDataObject
- Schema Name: FormidableConditionalRuleTestOperator
- Schema ID: schema:anon/b40f96ef930b4fc9ef8697311f51c1d6fd3aa307

### Enum

Values: eq

## FormidableField
- Role: nested
- Parent: FormidableCreatePayloadDataObject
- Schema Name: FormidableField
- Schema ID: schema:definitions/FormidableField
- Primary Key: TypeId

### Fields

| Field | Type |
|------|------|
| `type_id` | `FormidableFieldTypeId` |
| `slug` | `string` |
| `name` | `string` |
| `required` | `bool` |
| `items` | `FormidableFieldItems[]` |
| `description` | `string` |
| `content` | `string` |
| `validations` | `FormidableFieldValidation[]` |
| `button_selection` | `bool` |
| `multiple_selection` | `bool` |
| `placeholder` | `string` |
| `defaults` | `object[]` |
| `dataset_id` | `string` |

## FormidableFieldItems
- Role: nested
- Parent: FormidableCreatePayloadDataObject
- Schema Name: FormidableFieldItems
- Schema ID: schema:definitions/FormidableFieldItems

### Fields

| Field | Type |
|------|------|
| `value` | `string` |
| `label` | `string` |

## FormidableFieldTypeId
- Role: nested
- Parent: FormidableCreatePayloadDataObject
- Schema Name: FormidableFieldTypeId
- Schema ID: schema:anon/057fa3bc81021a3b35bd8a0331e97db7749eef73

### Enum

Values: short_text, number, date, dropdown, multiple_answer, single_answer, long_text, checkbox, email, title, separator, dataset, instruction, file

## FormidableFieldValidation
- Role: nested
- Parent: FormidableCreatePayloadDataObject
- Schema Name: FormidableFieldValidation
- Schema ID: schema:definitions/FormidableFieldValidation
- Primary Key: Value

### Fields

| Field | Type |
|------|------|
| `type` | `FormidableFieldValidationType` |
| `value` | `string` |
| `message` | `string` |

## FormidableFieldValidationType
- Role: nested
- Parent: FormidableCreatePayloadDataObject
- Schema Name: FormidableFieldValidationType
- Schema ID: schema:anon/94bbaf27be1d81f66a680870754e99c30d4923c8

### Enum

Values: MAXLENGTH, MINLENGTH, EQ, NEQ, GT, GTE, LT, LTE, IS_AGE_UNDER, IS_AGE_ABOVE, IS_DATE_IN_THE_FUTURE, REGEXP
