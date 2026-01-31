# EmployeePunchProfileDataDataObject

## EmployeePunchProfileDataDataObject
- Role: parent
- Schema Name: EmployeePunchProfileData
- Schema ID: schema:components/EmployeePunchProfileData

### Fields

| Field | Type |
|------|------|
| `punchProfileId` | `string` |
| `hasAllDeparmentsSelected` | `bool` |
| `hasAllWorkLocationsSelected` | `bool` |
| `hasAllActivityTypesSelected` | `bool` |
| `hasDetailPunch` | `bool` |
| `departments` | `Department4[]` |
| `workLocations` | `PunchProfileWorkLocation[]` |
| `laborProfile` | `LaborProfile2` |
| `activityTypes` | `ActivityTypeBasic[]` |

### Nested Types
- `ActivityTypeBasic`
- `Department4`
- `LaborCategory`
- `LaborCode7`
- `LaborProfile2`
- `PunchProfileWorkLocation`

## ActivityTypeBasic
- Role: nested
- Parent: EmployeePunchProfileDataDataObject
- Schema Name: ActivityTypeBasic
- Schema ID: schema:components/ActivityTypeBasic

### Fields

| Field | Type |
|------|------|
| `activityTypeId` | `string` |
| `activityName` | `string` |

## Department4
- Role: nested
- Parent: EmployeePunchProfileDataDataObject
- Schema Name: Department4
- Schema ID: schema:components/Department4

### Fields

| Field | Type |
|------|------|
| `departmentId` | `string` |
| `departmentName` | `string` |

## LaborCategory
- Role: nested
- Parent: EmployeePunchProfileDataDataObject
- Schema Name: LaborCategory
- Schema ID: schema:components/LaborCategory

### Fields

| Field | Type |
|------|------|
| `laborCategoryId` | `string` |
| `laborCategoryName` | `string` |
| `laborCodes` | `LaborCode7[]` |

## LaborCode7
- Role: nested
- Parent: EmployeePunchProfileDataDataObject
- Schema Name: LaborCode7
- Schema ID: schema:components/LaborCode7

### Fields

| Field | Type |
|------|------|
| `laborCodeId` | `string` |
| `laborCodeName` | `string` |

## LaborProfile2
- Role: nested
- Parent: EmployeePunchProfileDataDataObject
- Schema Name: LaborProfile2
- Schema ID: schema:components/LaborProfile2

### Fields

| Field | Type |
|------|------|
| `laborProfileId` | `string` |
| `laborProfileName` | `string` |
| `laborCategories` | `LaborCategory[]` |

## PunchProfileWorkLocation
- Role: nested
- Parent: EmployeePunchProfileDataDataObject
- Schema Name: PunchProfileWorkLocation
- Schema ID: schema:components/PunchProfileWorkLocation

### Fields

| Field | Type |
|------|------|
| `workLocationId` | `string` |
| `workLocationName` | `string` |
