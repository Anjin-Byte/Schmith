# ProcessTemplateDataObject

## ProcessTemplateDataObject
- Role: parent
- Schema Name: ProcessTemplate
- Schema ID: schema:definitions/ProcessTemplate
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `title` | `string` |
| `public_title` | `string` |
| `description` | `string` |
| `created_at` | `string` |
| `created_by` | `Anonymous_0d7385a1` |
| `updated_at` | `string` |
| `updated_by` | `Anonymous_ab9b1eb9` |
| `automatic_archiving` | `bool` |
| `restrictions` | `ProcessTemplateRestriction[]` |

### Nested Types
- `Anonymous_0d7385a1`
- `Anonymous_0d7385a1Origin`
- `Anonymous_ab9b1eb9`
- `Anonymous_ab9b1eb9Origin`
- `Organization`
- `OrganizationOperator`
- `ProcessTemplateRestriction`

## Anonymous_0d7385a1
- Role: nested
- Parent: ProcessTemplateDataObject
- Schema Name: Anonymous_0d7385a1
- Schema ID: schema:anon/0d7385a1fd0dee8a6a8af687eef3daccb05b6bdf
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `origin` | `Anonymous_0d7385a1Origin` |
| `id` | `string` |

## Anonymous_0d7385a1Origin
- Role: nested
- Parent: ProcessTemplateDataObject
- Schema Name: Anonymous_0d7385a1Origin
- Schema ID: schema:anon/0aaefd2bf3798a1d9f1532a5c42d9b2c45bad2ad

### Enum

Values: application, user

## Anonymous_ab9b1eb9
- Role: nested
- Parent: ProcessTemplateDataObject
- Schema Name: Anonymous_ab9b1eb9
- Schema ID: schema:anon/ab9b1eb99565d72ba3964883bdfd91eb98d86676
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `origin` | `Anonymous_ab9b1eb9Origin` |
| `id` | `string` |

## Anonymous_ab9b1eb9Origin
- Role: nested
- Parent: ProcessTemplateDataObject
- Schema Name: Anonymous_ab9b1eb9Origin
- Schema ID: schema:anon/9b842f7b316392d1701e64835e16e2d91781271c

### Enum

Values: application, user

## Organization
- Role: nested
- Parent: ProcessTemplateDataObject
- Schema Name: Organization
- Schema ID: schema:definitions/Organization
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `operator` | `OrganizationOperator` |

## OrganizationOperator
- Role: nested
- Parent: ProcessTemplateDataObject
- Schema Name: OrganizationOperator
- Schema ID: schema:anon/194956ec5ec1aa6b913c3da0fea7e3642f6f7534

### Enum

Values: =, <=

## ProcessTemplateRestriction
- Role: nested
- Parent: ProcessTemplateDataObject
- Schema Name: ProcessTemplateRestriction
- Schema ID: schema:definitions/ProcessTemplateRestriction

### Fields

| Field | Type |
|------|------|
| `organizations` | `Organization[]` |
