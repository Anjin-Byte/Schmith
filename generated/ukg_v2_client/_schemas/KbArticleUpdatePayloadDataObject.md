# KbArticleUpdatePayloadDataObject

## KbArticleUpdatePayloadDataObject
- Role: parent
- Schema Name: KbArticleUpdatePayload
- Schema ID: schema:definitions/KbArticleUpdatePayload

### Fields

| Field | Type |
|------|------|
| `slug` | `string` |
| `localized_tags` | `KbLocalizedTagsLocalizedTagsItem[]` |
| `localized_search_keywords` | `LocalizedString[]` |
| `featured_on_employee_homepage` | `bool` |
| `once_on_employee_homepage` | `bool` |
| `permanent_on_employee_homepage` | `bool` |
| `versions` | `KbArticleVersion[]` |
| `categories_ids` | `string[]` |
| `expiration_date` | `string` |
| `scheduled_publication_date` | `string` |
| `status` | `KbArticleBaseStatus` |
| `accessible_by_hr` | `bool` |
| `accessible_by_employee` | `bool` |
| `employees_perimeters` | `EmployeesPerimeterBase[]` |
| `role_restrictions` | `KbArticleBaseRoleRestrictionsItem[]` |

### Nested Types
- `CustomFieldFilterRule`
- `CustomFieldFilterRuleOperator`
- `EmployeesPerimeterBase`
- `EmployeesPerimeterBaseOperator`
- `KbArticleBaseRoleRestrictionsItem`
- `KbArticleBaseStatus`
- `KbArticleVersion`
- `KbLocalizedTagsLocalizedTagsItem`
- `LocalizedString`

## CustomFieldFilterRule
- Role: nested
- Parent: KbArticleUpdatePayloadDataObject
- Schema Name: CustomFieldFilterRule
- Schema ID: schema:definitions/CustomFieldFilterRule
- Primary Key: CustomFieldId

### Fields

| Field | Type |
|------|------|
| `custom_field_id` | `string` |
| `operator` | `CustomFieldFilterRuleOperator` |
| `value` | `string` |

## CustomFieldFilterRuleOperator
- Role: nested
- Parent: KbArticleUpdatePayloadDataObject
- Schema Name: CustomFieldFilterRuleOperator
- Schema ID: schema:anon/b89353968483881566a17091aa85441d29825efb

### Enum

Values: =, !=, <=, <, >=, >

## EmployeesPerimeterBase
- Role: nested
- Parent: KbArticleUpdatePayloadDataObject
- Schema Name: EmployeesPerimeterBase
- Schema ID: schema:definitions/EmployeesPerimeterBase
- Primary Key: OrganizationId

### Fields

| Field | Type |
|------|------|
| `operator` | `EmployeesPerimeterBaseOperator` |
| `organization_id` | `string` |
| `organization_group_id` | `string` |
| `custom_field_filters` | `CustomFieldFilterRule[]` |

## EmployeesPerimeterBaseOperator
- Role: nested
- Parent: KbArticleUpdatePayloadDataObject
- Schema Name: EmployeesPerimeterBaseOperator
- Schema ID: schema:anon/62bc992a0d5496dc75fdaeee1de43be7a94f91c1

### Enum

Values: =, <=

## KbArticleBaseRoleRestrictionsItem
- Role: nested
- Parent: KbArticleUpdatePayloadDataObject
- Schema Name: KbArticleBaseRoleRestrictionsItem
- Schema ID: schema:anon/cbcd60e0defd1088b9363273e505c0249931d345
- Primary Key: RoleId

### Fields

| Field | Type |
|------|------|
| `role_id` | `string` |
| `role_name` | `string` |

## KbArticleBaseStatus
- Role: nested
- Parent: KbArticleUpdatePayloadDataObject
- Schema Name: KbArticleBaseStatus
- Schema ID: schema:anon/e37f3bbd184e14499f9222bf4665a4a6812c017b

### Enum

Values: published, draft, scheduled

## KbArticleVersion
- Role: nested
- Parent: KbArticleUpdatePayloadDataObject
- Schema Name: KbArticleVersion
- Schema ID: schema:definitions/KbArticleVersion
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `language_code` | `string` |
| `title` | `string` |
| `body` | `string` |
| `creator_id` | `string` |
| `updator_id` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |

## KbLocalizedTagsLocalizedTagsItem
- Role: nested
- Parent: KbArticleUpdatePayloadDataObject
- Schema Name: KbLocalizedTagsLocalizedTagsItem
- Schema ID: schema:anon/8ad3c99675a69b3c6f879dd3269c96aef54fb16a

### Fields

| Field | Type |
|------|------|
| `language_code` | `string` |
| `values` | `string[]` |

## LocalizedString
- Role: nested
- Parent: KbArticleUpdatePayloadDataObject
- Schema Name: LocalizedString
- Schema ID: schema:definitions/LocalizedString

### Fields

| Field | Type |
|------|------|
| `language_code` | `string` |
| `value` | `string` |
