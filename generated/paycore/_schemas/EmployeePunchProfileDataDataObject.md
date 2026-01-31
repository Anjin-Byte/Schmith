# EmployeePunchProfileDataDataObject

## EmployeePunchProfileDataDataObject
- Role: parent
- Schema Name: EmployeePunchProfileData
- Schema ID: schema:components/EmployeePunchProfileData

### Fields
- `punchProfileId`: `string`
- `hasAllDeparmentsSelected`: `bool`
- `hasAllWorkLocationsSelected`: `bool`
- `hasAllActivityTypesSelected`: `bool`
- `hasDetailPunch`: `bool`
- `departments`: `Department4[]`
- `workLocations`: `PunchProfileWorkLocation[]`
- `laborProfile`: `LaborProfile2`
- `activityTypes`: `ActivityTypeBasic[]`

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
- `activityTypeId`: `string`
- `activityName`: `string`

## Department4
- Role: nested
- Parent: EmployeePunchProfileDataDataObject
- Schema Name: Department4
- Schema ID: schema:components/Department4

### Fields
- `departmentId`: `string`
- `departmentName`: `string`

## LaborCategory
- Role: nested
- Parent: EmployeePunchProfileDataDataObject
- Schema Name: LaborCategory
- Schema ID: schema:components/LaborCategory

### Fields
- `laborCategoryId`: `string`
- `laborCategoryName`: `string`
- `laborCodes`: `LaborCode7[]`

## LaborCode7
- Role: nested
- Parent: EmployeePunchProfileDataDataObject
- Schema Name: LaborCode7
- Schema ID: schema:components/LaborCode7

### Fields
- `laborCodeId`: `string`
- `laborCodeName`: `string`

## LaborProfile2
- Role: nested
- Parent: EmployeePunchProfileDataDataObject
- Schema Name: LaborProfile2
- Schema ID: schema:components/LaborProfile2

### Fields
- `laborProfileId`: `string`
- `laborProfileName`: `string`
- `laborCategories`: `LaborCategory[]`

## PunchProfileWorkLocation
- Role: nested
- Parent: EmployeePunchProfileDataDataObject
- Schema Name: PunchProfileWorkLocation
- Schema ID: schema:components/PunchProfileWorkLocation

### Fields
- `workLocationId`: `string`
- `workLocationName`: `string`
