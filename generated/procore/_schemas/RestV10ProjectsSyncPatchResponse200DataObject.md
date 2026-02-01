# RestV10ProjectsSyncPatchResponse200DataObject

## RestV10ProjectsSyncPatchResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsSyncPatchResponse200
- Schema ID: schema:anon/fea7ad39cf1b3cedc3630d2206e5a75f33e8c339

### Fields

| Field | Type |
|------|------|
| `entities` | `RestV10ProjectsSyncPatchResponse200EntitiesItem[]` |
| `errors` | `RestV10ProjectsSyncPatchResponse200ErrorsItem[]` |

### Nested Types
- `RestV10ProjectsSyncPatchResponse200EntitiesItem`
- `RestV10ProjectsSyncPatchResponse200EntitiesItemDeliveryMethod`
- `RestV10ProjectsSyncPatchResponse200EntitiesItemDepartmentsItem`
- `RestV10ProjectsSyncPatchResponse200EntitiesItemFlag`
- `RestV10ProjectsSyncPatchResponse200EntitiesItemOffice`
- `RestV10ProjectsSyncPatchResponse200EntitiesItemPriority`
- `RestV10ProjectsSyncPatchResponse200EntitiesItemProgram`
- `RestV10ProjectsSyncPatchResponse200EntitiesItemProjectStage`
- `RestV10ProjectsSyncPatchResponse200EntitiesItemProjectType`
- `RestV10ProjectsSyncPatchResponse200EntitiesItemSector`
- `RestV10ProjectsSyncPatchResponse200EntitiesItemWorkScope`
- `RestV10ProjectsSyncPatchResponse200ErrorsItem`
- `RestV10ProjectsSyncPatchResponse200ErrorsItem_7abdf4Errors`

## RestV10ProjectsSyncPatchResponse200EntitiesItem
- Role: nested
- Parent: RestV10ProjectsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsSyncPatchResponse200EntitiesItem
- Schema ID: schema:anon/1e323aae7f8096a1b82fb7c19fe6936ef8b9f8e2
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `logo_url` | `string` |
| `name` | `string` |
| `display_name` | `string` |
| `project_number` | `string` |
| `address` | `string` |
| `city` | `string` |
| `state_code` | `string` |
| `country_code` | `string` |
| `zip` | `string` |
| `time_zone` | `string` |
| `latitude` | `double` |
| `longitude` | `double` |
| `description` | `string` |
| `square_feet` | `int` |
| `start_date` | `string` |
| `completion_date` | `string` |
| `total_value` | `string` |
| `store_number` | `string` |
| `accounting_project_number` | `string` |
| `designated_market_area` | `string` |
| `warranty_start_date` | `string` |
| `warranty_end_date` | `string` |
| `active` | `bool` |
| `flag` | `RestV10ProjectsSyncPatchResponse200EntitiesItemFlag` |
| `phone` | `string` |
| `public_notes` | `string` |
| `actual_start_date` | `string` |
| `projected_finish_date` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `origin_id` | `string` |
| `origin_data` | `string` |
| `origin_code` | `string` |
| `estimated_start_date` | `string` |
| `estimated_completion_date` | `string` |
| `estimated_value` | `string` |
| `office` | `RestV10ProjectsSyncPatchResponse200EntitiesItemOffice` |
| `project_bid_type_id` | `int` |
| `project_owner_type_id` | `int` |
| `project_region_id` | `int` |
| `project_stage` | `RestV10ProjectsSyncPatchResponse200EntitiesItemProjectStage` |
| `project_type` | `RestV10ProjectsSyncPatchResponse200EntitiesItemProjectType` |
| `program` | `RestV10ProjectsSyncPatchResponse200EntitiesItemProgram` |
| `departments` | `RestV10ProjectsSyncPatchResponse200EntitiesItemDepartmentsItem[]` |
| `sector` | `RestV10ProjectsSyncPatchResponse200EntitiesItemSector` |
| `work_scope` | `RestV10ProjectsSyncPatchResponse200EntitiesItemWorkScope` |
| `delivery_method` | `RestV10ProjectsSyncPatchResponse200EntitiesItemDeliveryMethod` |
| `estimated_budget` | `double` |
| `priority` | `RestV10ProjectsSyncPatchResponse200EntitiesItemPriority` |
| `project_sector_id` | `int` |

## RestV10ProjectsSyncPatchResponse200EntitiesItemDeliveryMethod
- Role: nested
- Parent: RestV10ProjectsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsSyncPatchResponse200EntitiesItemDeliveryMethod
- Schema ID: schema:anon/2d5286e10993019339ae42f68c288ad74a7dddc4

### Enum

Values: construction_management_at_risk_cmar, construction_manager_as_agent_owners_rep, design_bid_build_dbb, design_build_db, indefinite_delivery_indefinite_quantity_idiq, integrated_project_delivery, multi_prime, public_private_partnership_p3, other, None

## RestV10ProjectsSyncPatchResponse200EntitiesItemDepartmentsItem
- Role: nested
- Parent: RestV10ProjectsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsSyncPatchResponse200EntitiesItemDepartmentsItem
- Schema ID: schema:anon/cba7c064adfce08f1c4da0367d2465f4cb163851
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsSyncPatchResponse200EntitiesItemFlag
- Role: nested
- Parent: RestV10ProjectsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsSyncPatchResponse200EntitiesItemFlag
- Schema ID: schema:anon/c15eabcdf89ed39f707b08060de6bf8d5742cdc7

### Enum

Values: Red, Yellow, Green, None

## RestV10ProjectsSyncPatchResponse200EntitiesItemOffice
- Role: nested
- Parent: RestV10ProjectsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsSyncPatchResponse200EntitiesItemOffice
- Schema ID: schema:anon/bb715b2adc925537b78260e598f3dfc15021bee3
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsSyncPatchResponse200EntitiesItemPriority
- Role: nested
- Parent: RestV10ProjectsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsSyncPatchResponse200EntitiesItemPriority
- Schema ID: schema:anon/a52a2418e1e928507b745e48bce5f523b61ec848

### Enum

Values: low, medium, high

## RestV10ProjectsSyncPatchResponse200EntitiesItemProgram
- Role: nested
- Parent: RestV10ProjectsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsSyncPatchResponse200EntitiesItemProgram
- Schema ID: schema:anon/6693599ba4845721c63864d45cf4fcf489871ea5
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsSyncPatchResponse200EntitiesItemProjectStage
- Role: nested
- Parent: RestV10ProjectsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsSyncPatchResponse200EntitiesItemProjectStage
- Schema ID: schema:anon/8c899adfe2a52fbaea1abce9d125a827b2b33cf6
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsSyncPatchResponse200EntitiesItemProjectType
- Role: nested
- Parent: RestV10ProjectsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsSyncPatchResponse200EntitiesItemProjectType
- Schema ID: schema:anon/d45eded8a4a46298ca3ad48a64555bc5156433ce
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsSyncPatchResponse200EntitiesItemSector
- Role: nested
- Parent: RestV10ProjectsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsSyncPatchResponse200EntitiesItemSector
- Schema ID: schema:anon/ced8f6167fe30f4f4c940766c58ca730c2028f4d

### Enum

Values: agriculture, airport, alcohol_establishment, amusement_park, animal_health_veterinary, animal_lodging, assembly, auto_parts_store, auto_service, auto_vehicle_terminal, automobile_retail, aviation, bank, bar_tavern, battery_energy_storage, behavioral_health, big_box_store, bowling_alley, brewery, bridges, business_park, campground, car_wash, casino, casino_hotel, cemetery, city_hall_operations, civil_infrastructure, college_university, commercial, convenience_store, convention_center, courthouse, cultural, dam, data_center, daycare_pre_k, dealership, death, dental, department_store, distillery, distribution_warehouse, district_operations, drug_store, dry_storage, educational, electrical_substation, elementary_school, energy, energy_distribution, energy_production, energy_storage, entertainment, entertainment_production, environmentally_controlled, event_space, fast_food_restaurant, fire_station, funeral_home, gas_station, golf, government, government_buildings, grocery_store, gym_athletic_studio, hangar, hazardous_storage, health_care, high_school, hospital, hospitality, hotel, hydro_power, individual_space, indoor, industrial, institutional, jail_prison, k_12, library, liquor_store, lodging, manufacturing, medical_center, medical_office_building_mob, middle_school, military_naval, miscellaneous_pavement, mixed_use, movie_theater, multifamily, museum, nuclear_power_plant, office, office_retail, oil_gas_mining, outdoor, outpatient_care, park, parking_garage, parking_lot, performing_arts, personal_service, pipe_line, playground, police_station, pool_swim_facility, post_office, production, psychiatric_hospital, public_safety, race_track, railway_terminal, railways, recreation, rehab_facility, religious_institution, research_development, reservoir, residential, residential_office_retail, residential_retail, restaurant, retail, roads_highways, runway_taxiway, rv_park, self_storage, senior_housing, sewer_systems, shopping_center_mall, sidewalk_walkways, single_family, solar_power, specialist_office, specialty_store, sports_courts, sports_fields, stadium_arena, storage, street_lights, student_housing, telecommunication, telecommunication_lines, terminal, trailer_park, transportation, transportation_terminals, tunnel, urgent_care, waste_collection, waste_infrastructure, waste_processing, waste_water, water_distribution, water_infrastructure, water_retention, water_treatment_plant_wwtp, wind_power, winery, winter_sports, zoo_aquarium, None

## RestV10ProjectsSyncPatchResponse200EntitiesItemWorkScope
- Role: nested
- Parent: RestV10ProjectsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsSyncPatchResponse200EntitiesItemWorkScope
- Schema ID: schema:anon/6ce6588dfbd0c90f2533f1b6a3079e5092153e95

### Enum

Values: new_construction, renovation_alteration, maintenance_service, None

## RestV10ProjectsSyncPatchResponse200ErrorsItem
- Role: nested
- Parent: RestV10ProjectsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsSyncPatchResponse200ErrorsItem
- Schema ID: schema:anon/6d43fa73813c19ceee0aab81186c82a4db989d4b

### Fields

| Field | Type |
|------|------|
| `errors` | `RestV10ProjectsSyncPatchResponse200ErrorsItem_7abdf4Errors` |

## RestV10ProjectsSyncPatchResponse200ErrorsItem_7abdf4Errors
- Role: nested
- Parent: RestV10ProjectsSyncPatchResponse200DataObject
- Schema Name: RestV10ProjectsSyncPatchResponse200ErrorsItem_7abdf4Errors
- Schema ID: schema:anon/6e80d68169409a1f3f35565d9efca5f938183297

### Fields

| Field | Type |
|------|------|
| `field_name` | `string[]` |
