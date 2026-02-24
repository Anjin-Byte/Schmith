# Project

## Project

- Schema ID: `schema:anon/5f73a94ea7e0da8536413eff0a02b7972592a9f4`
- Kind: unknown

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `AccountingProjectNumber` | `schema:types/string` |
| `Active` | `schema:types/boolean` |
| `ActualStartDate` | `schema:types/date` |
| `Address` | `schema:types/string` |
| `City` | `schema:types/string` |
| `Company` | `ProjectCompany` |
| `CompletionDate` | `schema:types/date` |
| `CountryCode` | `schema:types/string` |
| `County` | `schema:types/string` |
| `CreatedAt` | `schema:types/datetime` |
| `CreatedBy` | `NormalCreatedBy` |
| `CustomFields` | `NormalCustomFields` |
| `DeliveryMethod` | `DeliveryMethod` |
| `Description` | `schema:types/string` |
| `DesignatedMarketArea` | `schema:types/string` |
| `DisplayName` | `schema:types/string` |
| `EstimatedValue` | `schema:types/string` |
| `IsDemo` | `schema:types/boolean` |
| `Latitude` | `schema:types/number` |
| `Longitude` | `schema:types/number` |
| `Name` | `schema:types/string` |
| `OriginCode` | `schema:types/string` |
| `OriginData` | `schema:types/string` |
| `OriginId` | `schema:types/string` |
| `OwnersProjectId` | `schema:types/integer` |
| `ParentJobId` | `schema:types/integer` |
| `Phone` | `schema:types/string` |
| `PhotoId` | `schema:types/integer` |
| `ProjectBidTypeId` | `schema:types/integer` |
| `ProjectNumber` | `schema:types/string` |
| `ProjectOwnerTypeId` | `schema:types/integer` |
| `ProjectRegionId` | `schema:types/integer` |
| `ProjectStage` | `ProjectStage` |
| `ProjectTemplate` | `ProjectTemplate` |
| `ProjectType` | `ProjectType` |
| `ProjectedFinishDate` | `schema:types/date` |
| `Sector` | `ProjectSector` |
| `SquareFeet` | `schema:types/integer` |
| `StartDate` | `schema:types/date` |
| `StateCode` | `schema:types/string` |
| `StoreNumber` | `schema:types/string` |
| `TimeZone` | `schema:types/string` |
| `TotalValue` | `schema:types/string` |
| `UpdatedAt` | `schema:types/datetime` |
| `WorkScope` | `WorkScope` |
| `Zip` | `schema:types/string` |
| `Departments` | `ProjectDepartment[]` |
| `DictionaryType` | `schema:types/string` |
| `EstimatedCompletionDate` | `schema:types/date` |
| `EstimatedStartDate` | `schema:types/date` |
| `Flag` | `ExtendedFlag` |
| `InboundEmail` | `schema:types/string` |
| `LogoUrl` | `schema:types/string` |
| `Office` | `ProjectOffice` |
| `PersistentMessage` | `ProjectPersistentMessage` |
| `Program` | `ProjectProgram` |
| `ProjectBidType` | `ProjectBidType` |
| `ProjectOwnerType` | `ProjectOwnerType` |
| `ProjectRegion` | `ProjectRegion` |
| `PublicNotes` | `schema:types/string` |
| `StandardCostCodeListId` | `schema:types/integer` |
| `TzName` | `schema:types/string` |
| `WarrantyEndDate` | `schema:types/date` |
| `WarrantyStartDate` | `schema:types/date` |
| `ProjectSectorId` | `schema:types/integer` |

---

## Nested Types

### Compact

- Schema ID: `schema:anon/973f0e9b3a4471ece6d73469cc08c597dd4bb4c3`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |

### DeliveryMethod

The delivery method of a project.

- Schema ID: `schema:anon/2d5286e10993019339ae42f68c288ad74a7dddc4`
- Kind: string

### Enum Values

- `construction_management_at_risk_cmar`
- `construction_manager_as_agent_owners_rep`
- `design_bid_build_dbb`
- `design_build_db`
- `indefinite_delivery_indefinite_quantity_idiq`
- `integrated_project_delivery`
- `multi_prime`
- `public_private_partnership_p3`
- `other`
- `None`

### Extended

- Schema ID: `schema:anon/a671f47985168df4f8ff328e1b13d9610e2f459e`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `AccountingProjectNumber` | `schema:types/string` |
| `Active` | `schema:types/boolean` |
| `ActualStartDate` | `schema:types/date` |
| `Address` | `schema:types/string` |
| `City` | `schema:types/string` |
| `Company` | `ProjectCompany` |
| `CompletionDate` | `schema:types/date` |
| `CountryCode` | `schema:types/string` |
| `County` | `schema:types/string` |
| `CreatedAt` | `schema:types/datetime` |
| `CustomFields` | `NormalCustomFields` |
| `Departments` | `ProjectDepartment[]` |
| `Description` | `schema:types/string` |
| `DesignatedMarketArea` | `schema:types/string` |
| `DictionaryType` | `schema:types/string` |
| `DisplayName` | `schema:types/string` |
| `EstimatedCompletionDate` | `schema:types/date` |
| `EstimatedStartDate` | `schema:types/date` |
| `EstimatedValue` | `schema:types/string` |
| `Flag` | `ExtendedFlag` |
| `InboundEmail` | `schema:types/string` |
| `Latitude` | `schema:types/number` |
| `LogoUrl` | `schema:types/string` |
| `Longitude` | `schema:types/number` |
| `Name` | `schema:types/string` |
| `Office` | `ProjectOffice` |
| `OriginCode` | `schema:types/string` |
| `OriginData` | `schema:types/string` |
| `OriginId` | `schema:types/string` |
| `OwnersProjectId` | `schema:types/integer` |
| `ParentJobId` | `schema:types/integer` |
| `PersistentMessage` | `ProjectPersistentMessage` |
| `Phone` | `schema:types/string` |
| `PhotoId` | `schema:types/integer` |
| `Program` | `ProjectProgram` |
| `ProjectBidType` | `ProjectBidType` |
| `ProjectNumber` | `schema:types/string` |
| `ProjectOwnerType` | `ProjectOwnerType` |
| `ProjectOwnerTypeId` | `schema:types/integer` |
| `ProjectRegion` | `ProjectRegion` |
| `ProjectRegionId` | `schema:types/integer` |
| `ProjectStage` | `ProjectStage` |
| `ProjectType` | `ProjectType` |
| `ProjectedFinishDate` | `schema:types/date` |
| `PublicNotes` | `schema:types/string` |
| `SquareFeet` | `schema:types/integer` |
| `StandardCostCodeListId` | `schema:types/integer` |
| `StartDate` | `schema:types/date` |
| `StateCode` | `schema:types/string` |
| `StoreNumber` | `schema:types/string` |
| `TimeZone` | `schema:types/string` |
| `TotalValue` | `schema:types/string` |
| `TzName` | `schema:types/string` |
| `UpdatedAt` | `schema:types/datetime` |
| `WarrantyEndDate` | `schema:types/date` |
| `WarrantyStartDate` | `schema:types/date` |
| `Zip` | `schema:types/string` |
| `ProjectSectorId` | `schema:types/integer` |

### ExtendedFlag

Project flag

- Schema ID: `schema:anon/a47c617b041274b4f3fb8bd712b9a63da9027d5c`
- Kind: string

### Enum Values

- `Red`
- `Yellow`
- `Green`
- `None`

### FieldLovEntryValue

- Schema ID: `schema:anon/87cff48788164388a7c8910cf94ab26c21bee6e1`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Label` | `schema:types/string` |

### LovEntriesValueNestedItem

- Schema ID: `schema:anon/98dfbe72f61b8f25de0fb5b18d6fa8d9a4ec580a`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Label` | `schema:types/string` |

### Normal

- Schema ID: `schema:anon/7b9535dab8c8fec38cd093c1739be40297d3b975`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `AccountingProjectNumber` | `schema:types/string` |
| `Active` | `schema:types/boolean` |
| `ActualStartDate` | `schema:types/date` |
| `Address` | `schema:types/string` |
| `City` | `schema:types/string` |
| `Company` | `ProjectCompany` |
| `CompletionDate` | `schema:types/date` |
| `CountryCode` | `schema:types/string` |
| `County` | `schema:types/string` |
| `CreatedAt` | `schema:types/datetime` |
| `CreatedBy` | `NormalCreatedBy` |
| `CustomFields` | `NormalCustomFields` |
| `DeliveryMethod` | `DeliveryMethod` |
| `Description` | `schema:types/string` |
| `DesignatedMarketArea` | `schema:types/string` |
| `DisplayName` | `schema:types/string` |
| `EstimatedValue` | `schema:types/string` |
| `IsDemo` | `schema:types/boolean` |
| `Latitude` | `schema:types/number` |
| `Longitude` | `schema:types/number` |
| `Name` | `schema:types/string` |
| `OriginCode` | `schema:types/string` |
| `OriginData` | `schema:types/string` |
| `OriginId` | `schema:types/string` |
| `OwnersProjectId` | `schema:types/integer` |
| `ParentJobId` | `schema:types/integer` |
| `Phone` | `schema:types/string` |
| `PhotoId` | `schema:types/integer` |
| `ProjectBidTypeId` | `schema:types/integer` |
| `ProjectNumber` | `schema:types/string` |
| `ProjectOwnerTypeId` | `schema:types/integer` |
| `ProjectRegionId` | `schema:types/integer` |
| `ProjectStage` | `ProjectStage` |
| `ProjectTemplate` | `ProjectTemplate` |
| `ProjectType` | `ProjectType` |
| `ProjectedFinishDate` | `schema:types/date` |
| `Sector` | `ProjectSector` |
| `SquareFeet` | `schema:types/integer` |
| `StartDate` | `schema:types/date` |
| `StateCode` | `schema:types/string` |
| `StoreNumber` | `schema:types/string` |
| `TimeZone` | `schema:types/string` |
| `TotalValue` | `schema:types/string` |
| `UpdatedAt` | `schema:types/datetime` |
| `WorkScope` | `WorkScope` |
| `Zip` | `schema:types/string` |

### NormalCreatedBy

Login Information

- Schema ID: `schema:anon/05e77aa2c5b0ae16984d391ae1269bda6f0dbb76`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |
| `Login` | `schema:types/string` |

### NormalCustomFields

- Schema ID: `schema:anon/18c858aabec7b2c6828e2c316ea32d80e8f6c1be`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `CustomFieldString` | `NormalCustomFieldsCustomFieldString` |
| `CustomFieldDecimal` | `NormalCustomFieldsCustomFieldDecimal` |
| `CustomFieldBoolean` | `NormalCustomFieldsCustomFieldBoolean` |
| `CustomFieldLovEntry` | `NormalCustomFieldsCustomFieldLovEntry` |
| `CustomFieldLovEntries` | `NormalCustomFieldsCustomFieldLovEntries` |

### NormalCustomFieldsCustomFieldBoolean

- Schema ID: `schema:anon/d7aaf7e4245f8b5e58720e73973a9fdbdbc7839e`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `DataType` | `schema:types/string` |
| `Value` | `schema:types/boolean` |

### NormalCustomFieldsCustomFieldDecimal

- Schema ID: `schema:anon/8178757753fe7302f7d5443936cb13b481bd73ff`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `DataType` | `schema:types/string` |
| `Value` | `schema:types/number` |

### NormalCustomFieldsCustomFieldLovEntries

- Schema ID: `schema:anon/d50bbe7063fb38ebfcc50625f772776d0020e2f7`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `DataType` | `schema:types/string` |
| `Value` | `LovEntriesValueNestedItem[]` |

### NormalCustomFieldsCustomFieldLovEntry

- Schema ID: `schema:anon/33d4a72922e5630c3242f8b04f6ee313e990b793`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `DataType` | `schema:types/string` |
| `Value` | `FieldLovEntryValue` |

### NormalCustomFieldsCustomFieldString

- Schema ID: `schema:anon/8c3d88cb61be32fb0e8459abd64e13d194ffdb10`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `DataType` | `schema:types/string` |
| `Value` | `schema:types/string` |

### ProjectBidType

- Schema ID: `schema:anon/e6a057fd37044b72f06dab7871de94b8013faadb`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |

### ProjectCompany

- Schema ID: `schema:anon/447aa00ce726996f3d96efd9ae8ab1a24c1e98bd`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |

### ProjectDepartment

- Schema ID: `schema:anon/3137a8973bb9ae5434e6b2dd1f1a5c60a4b9cf75`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |

### ProjectOffice

- Schema ID: `schema:anon/ac4d0310f0ee1ff9cb42b719739224c9cad98435`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |

### ProjectOwnerType

- Schema ID: `schema:anon/c4b29441f96ed3994aa0c195c7723a881bbe00e2`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |

### ProjectPersistentMessage

- Schema ID: `schema:anon/4305775e16482206f3024738cb10f39b59e6f4d8`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Message` | `schema:types/string` |
| `Title` | `schema:types/string` |

### ProjectProgram

- Schema ID: `schema:anon/78d1c0e6f72cac7652dcebc22cb8e2266f59a2ff`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |

### ProjectRegion

- Schema ID: `schema:anon/29df026d3b9f81dcd169691aaaa24450f43b4917`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |

### ProjectSector

The sector of a project.

- Schema ID: `schema:anon/ced8f6167fe30f4f4c940766c58ca730c2028f4d`
- Kind: string

### Enum Values

- `agriculture`
- `airport`
- `alcohol_establishment`
- `amusement_park`
- `animal_health_veterinary`
- `animal_lodging`
- `assembly`
- `auto_parts_store`
- `auto_service`
- `auto_vehicle_terminal`
- `automobile_retail`
- `aviation`
- `bank`
- `bar_tavern`
- `battery_energy_storage`
- `behavioral_health`
- `big_box_store`
- `bowling_alley`
- `brewery`
- `bridges`
- `business_park`
- `campground`
- `car_wash`
- `casino`
- `casino_hotel`
- `cemetery`
- `city_hall_operations`
- `civil_infrastructure`
- `college_university`
- `commercial`
- `convenience_store`
- `convention_center`
- `courthouse`
- `cultural`
- `dam`
- `data_center`
- `daycare_pre_k`
- `dealership`
- `death`
- `dental`
- `department_store`
- `distillery`
- `distribution_warehouse`
- `district_operations`
- `drug_store`
- `dry_storage`
- `educational`
- `electrical_substation`
- `elementary_school`
- `energy`
- `energy_distribution`
- `energy_production`
- `energy_storage`
- `entertainment`
- `entertainment_production`
- `environmentally_controlled`
- `event_space`
- `fast_food_restaurant`
- `fire_station`
- `funeral_home`
- `gas_station`
- `golf`
- `government`
- `government_buildings`
- `grocery_store`
- `gym_athletic_studio`
- `hangar`
- `hazardous_storage`
- `health_care`
- `high_school`
- `hospital`
- `hospitality`
- `hotel`
- `hydro_power`
- `individual_space`
- `indoor`
- `industrial`
- `institutional`
- `jail_prison`
- `k_12`
- `library`
- `liquor_store`
- `lodging`
- `manufacturing`
- `medical_center`
- `medical_office_building_mob`
- `middle_school`
- `military_naval`
- `miscellaneous_pavement`
- `mixed_use`
- `movie_theater`
- `multifamily`
- `museum`
- `nuclear_power_plant`
- `office`
- `office_retail`
- `oil_gas_mining`
- `outdoor`
- `outpatient_care`
- `park`
- `parking_garage`
- `parking_lot`
- `performing_arts`
- `personal_service`
- `pipe_line`
- `playground`
- `police_station`
- `pool_swim_facility`
- `post_office`
- `production`
- `psychiatric_hospital`
- `public_safety`
- `race_track`
- `railway_terminal`
- `railways`
- `recreation`
- `rehab_facility`
- `religious_institution`
- `research_development`
- `reservoir`
- `residential`
- `residential_office_retail`
- `residential_retail`
- `restaurant`
- `retail`
- `roads_highways`
- `runway_taxiway`
- `rv_park`
- `self_storage`
- `senior_housing`
- `sewer_systems`
- `shopping_center_mall`
- `sidewalk_walkways`
- `single_family`
- `solar_power`
- `specialist_office`
- `specialty_store`
- `sports_courts`
- `sports_fields`
- `stadium_arena`
- `storage`
- `street_lights`
- `student_housing`
- `telecommunication`
- `telecommunication_lines`
- `terminal`
- `trailer_park`
- `transportation`
- `transportation_terminals`
- `tunnel`
- `urgent_care`
- `waste_collection`
- `waste_infrastructure`
- `waste_processing`
- `waste_water`
- `water_distribution`
- `water_infrastructure`
- `water_retention`
- `water_treatment_plant_wwtp`
- `wind_power`
- `winery`
- `winter_sports`
- `zoo_aquarium`
- `None`

### ProjectStage

- Schema ID: `schema:anon/8c899adfe2a52fbaea1abce9d125a827b2b33cf6`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |

### ProjectTemplate

- Schema ID: `schema:anon/bbf610d9ab62f52cc5e4ceb092c7f686406e0347`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |

### ProjectType

- Schema ID: `schema:anon/ba23caaeefb129110eef9092899ec4df45a005e6`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |

### WorkScope

The work scope of a project.

- Schema ID: `schema:anon/6ce6588dfbd0c90f2533f1b6a3079e5092153e95`
- Kind: string

### Enum Values

- `new_construction`
- `renovation_alteration`
- `maintenance_service`
- `None`
