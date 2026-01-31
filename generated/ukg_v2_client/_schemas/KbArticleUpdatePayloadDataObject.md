# KbArticleUpdatePayloadDataObject

## KbArticleUpdatePayloadDataObject
- Role: parent
- Schema Name: KbArticleUpdatePayload
- Schema ID: schema:definitions/KbArticleUpdatePayload

### Fields
- `localized_tags`: `object[]`
- `localized_search_keywords`: `LocalizedString[]`
- `featured_on_employee_homepage`: `bool`
- `once_on_employee_homepage`: `bool`
- `permanent_on_employee_homepage`: `bool`
- `versions`: `KbArticleVersion[]`
- `categories_ids`: `string[]`
- `expiration_date`: `string`
- `scheduled_publication_date`: `string`
- `status`: `StatusEnum`
- `accessible_by_hr`: `bool`
- `accessible_by_employee`: `bool`
- `employees_perimeters`: `EmployeesPerimeterBase[]`
- `role_restrictions`: `object[]`
- `slug`: `string`
