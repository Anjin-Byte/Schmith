# RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdCategoriesCategoryIdPostResponse200DataObject

## RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdCategoriesCategoryIdPostResponse200DataObject
- Role: parent
- Schema Name: RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdCategoriesCategoryIdPostResponse200
- Schema ID: schema:anon/bb1d7ea54c618b32112e21ddbe1d8d2ba5d0c700

### Fields

| Field | Type |
|------|------|
| `categories` | `RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdCategoriesCategoryIdPostResponse200CategoriesItem[]` |

### Nested Types
- `RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdCategoriesCategoryIdPostResponse200CategoriesItem`
- `RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdCategoriesCategoryIdPostResponse200CategoriesItemSubcategoriesItem`

## RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdCategoriesCategoryIdPostResponse200CategoriesItem
- Role: nested
- Parent: RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdCategoriesCategoryIdPostResponse200DataObject
- Schema Name: RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdCategoriesCategoryIdPostResponse200CategoriesItem
- Schema ID: schema:anon/e95a982720c4c0159b8d5645bacc49afea02ca66
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |
| `subcategories` | `RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdCategoriesCategoryIdPostResponse200CategoriesItemSubcategoriesItem[]` |

## RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdCategoriesCategoryIdPostResponse200CategoriesItemSubcategoriesItem
- Role: nested
- Parent: RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdCategoriesCategoryIdPostResponse200DataObject
- Schema Name: RestV10WorkforcePlanningV2CompaniesCompanyIdProjectsProjectIdCategoriesCategoryIdPostResponse200CategoriesItemSubcategoriesItem
- Schema ID: schema:anon/94980f24aeb71b509e77e20e4a3a1a8f57fcdfc9
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |
