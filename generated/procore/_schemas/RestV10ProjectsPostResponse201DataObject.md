# RestV10ProjectsPostResponse201DataObject

## RestV10ProjectsPostResponse201DataObject
- Role: parent
- Schema Name: RestV10ProjectsPostResponse201
- Schema ID: schema:anon/71a8f74879db861a61d2794546a5750bf18587bc
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `logo_id` | `int` |
| `logo_url` | `string` |
| `name` | `string` |
| `is_demo` | `bool` |
| `template` | `bool` |
| `display_name` | `string` |
| `project_number` | `string` |
| `address` | `string` |
| `city` | `string` |
| `state_code` | `string` |
| `country_code` | `string` |
| `zip` | `string` |
| `time_zone` | `string` |
| `tz_name` | `string` |
| `latitude` | `double` |
| `longitude` | `double` |
| `county` | `string` |
| `parent_job_id` | `int` |
| `parent_job` | `RestV10ProjectsPostResponse201ParentJob` |
| `from_project_template_id` | `int` |
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
| `flag` | `RestV10ProjectsPostResponse201Flag` |
| `locale` | `RestV10ProjectsPostResponse201Locale` |
| `phone` | `string` |
| `public_notes` | `string` |
| `actual_start_date` | `string` |
| `projected_finish_date` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `origin_id` | `string` |
| `origin_data` | `string` |
| `origin_code` | `string` |
| `standard_cost_code_list_id` | `int` |
| `is_erp_integrated` | `bool` |
| `owners_project_id` | `int` |
| `photo_id` | `int` |
| `photo_url` | `string` |
| `inbound_email` | `string` |
| `inbound_email_address` | `string` |
| `estimated_start_date` | `string` |
| `estimated_completion_date` | `string` |
| `estimated_value` | `string` |
| `code` | `string` |
| `sector` | `RestV10ProjectsPostResponse201Sector` |
| `work_scope` | `RestV10ProjectsPostResponse201WorkScope` |
| `delivery_method` | `RestV10ProjectsPostResponse201DeliveryMethod` |
| `created_by` | `RestV10ProjectsPostResponse201CreatedBy` |
| `persistent_message` | `RestV10ProjectsPostResponse201PersistentMessage` |
| `office` | `RestV10ProjectsPostResponse201Office` |
| `project_bid_type_id` | `int` |
| `project_bid_type` | `RestV10ProjectsPostResponse201ProjectBidType` |
| `project_owner_type_id` | `int` |
| `project_owner_type` | `RestV10ProjectsPostResponse201ProjectOwnerType` |
| `project_region_id` | `int` |
| `project_region` | `RestV10ProjectsPostResponse201ProjectRegion` |
| `project_stage_id` | `int` |
| `project_stage` | `RestV10ProjectsPostResponse201ProjectStage` |
| `project_type` | `RestV10ProjectsPostResponse201ProjectType` |
| `program` | `RestV10ProjectsPostResponse201Program` |
| `departments` | `RestV10ProjectsPostResponse201DepartmentsItem[]` |
| `company` | `RestV10ProjectsPostResponse201Company` |
| `dictionary_type` | `string` |
| `custom_fields` | `RestV10ProjectsPostResponse201CustomFields` |
| `project_sector_id` | `int` |

### Nested Types
- `RestV10ProjectsPostResponse201Company`
- `RestV10ProjectsPostResponse201CreatedBy`
- `RestV10ProjectsPostResponse201CustomFields`
- `RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}`
- `RestV10ProjectsPostResponse201DeliveryMethod`
- `RestV10ProjectsPostResponse201DepartmentsItem`
- `RestV10ProjectsPostResponse201Flag`
- `RestV10ProjectsPostResponse201Locale`
- `RestV10ProjectsPostResponse201Office`
- `RestV10ProjectsPostResponse201OfficeLogo`
- `RestV10ProjectsPostResponse201ParentJob`
- `RestV10ProjectsPostResponse201PersistentMessage`
- `RestV10ProjectsPostResponse201Program`
- `RestV10ProjectsPostResponse201ProjectBidType`
- `RestV10ProjectsPostResponse201ProjectOwnerType`
- `RestV10ProjectsPostResponse201ProjectRegion`
- `RestV10ProjectsPostResponse201ProjectStage`
- `RestV10ProjectsPostResponse201ProjectType`
- `RestV10ProjectsPostResponse201Sector`
- `RestV10ProjectsPostResponse201WorkScope`

## RestV10ProjectsPostResponse201Company
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201Company
- Schema ID: schema:anon/44fad40c3bd0ca8446dda114879975dee61768bf
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsPostResponse201CreatedBy
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201CreatedBy
- Schema ID: schema:anon/05e77aa2c5b0ae16984d391ae1269bda6f0dbb76
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `login` | `string` |

## RestV10ProjectsPostResponse201CustomFields
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201CustomFields
- Schema ID: schema:anon/18c858aabec7b2c6828e2c316ea32d80e8f6c1be

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/d7aaf7e4245f8b5e58720e73973a9fdbdbc7839e

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/8178757753fe7302f7d5443936cb13b481bd73ff

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/d50bbe7063fb38ebfcc50625f772776d0020e2f7

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/98dfbe72f61b8f25de0fb5b18d6fa8d9a4ec580a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/33d4a72922e5630c3242f8b04f6ee313e990b793

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/87cff48788164388a7c8910cf94ab26c21bee6e1
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201CustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/8c3d88cb61be32fb0e8459abd64e13d194ffdb10

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |

## RestV10ProjectsPostResponse201DeliveryMethod
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201DeliveryMethod
- Schema ID: schema:anon/2d5286e10993019339ae42f68c288ad74a7dddc4

### Enum

Values: construction_management_at_risk_cmar, construction_manager_as_agent_owners_rep, design_bid_build_dbb, design_build_db, indefinite_delivery_indefinite_quantity_idiq, integrated_project_delivery, multi_prime, public_private_partnership_p3, other, None

## RestV10ProjectsPostResponse201DepartmentsItem
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201DepartmentsItem
- Schema ID: schema:anon/cba7c064adfce08f1c4da0367d2465f4cb163851
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsPostResponse201Flag
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201Flag
- Schema ID: schema:anon/c15eabcdf89ed39f707b08060de6bf8d5742cdc7

### Enum

Values: Red, Yellow, Green, None

## RestV10ProjectsPostResponse201Locale
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201Locale
- Schema ID: schema:anon/ca907187419227bc6d7abdd414131a80ef032426

### Enum

Values: de-DE, en, en-AE, en-AU, en-CA, en-GB, en-SG, en-US-x-owner, en-US-x-sc, en-budget, en-owner, es, es-419, es-ES, fr-CA, fr-FR, ja-JP, ko, pl-PL, pseudo, pt-BR, th-TH, zh-SG

## RestV10ProjectsPostResponse201Office
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201Office
- Schema ID: schema:anon/4888405f8eb8bc9cc61a62d653341cb557bc6b4f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `address` | `string` |
| `city` | `string` |
| `state_code` | `string` |
| `country_code` | `string` |
| `zip` | `string` |
| `phone` | `string` |
| `fax` | `string` |
| `division` | `string` |
| `logo` | `RestV10ProjectsPostResponse201OfficeLogo` |

## RestV10ProjectsPostResponse201OfficeLogo
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201OfficeLogo
- Schema ID: schema:anon/fad6be341c2104a22008505693024de15cff6b6f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `url` | `string` |

## RestV10ProjectsPostResponse201ParentJob
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201ParentJob
- Schema ID: schema:anon/317f9f3d1e5b5ad20e63b4ae4ad34b1b57dc2088
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsPostResponse201PersistentMessage
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201PersistentMessage
- Schema ID: schema:anon/d9d7ef3939e5ea674cbff4e5f28cee3808ce2756

### Fields

| Field | Type |
|------|------|
| `title` | `string` |
| `message` | `string` |

## RestV10ProjectsPostResponse201Program
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201Program
- Schema ID: schema:anon/6693599ba4845721c63864d45cf4fcf489871ea5
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsPostResponse201ProjectBidType
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201ProjectBidType
- Schema ID: schema:anon/95e3238f0ffdb5dc015b66fc60c64f9c689cc2ce
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsPostResponse201ProjectOwnerType
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201ProjectOwnerType
- Schema ID: schema:anon/98f58a4f19e1dd172f347f56af7d0d2649561375
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsPostResponse201ProjectRegion
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201ProjectRegion
- Schema ID: schema:anon/fda6101a4c67039217d26bf2a56f5ed4aa3d0f1c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsPostResponse201ProjectStage
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201ProjectStage
- Schema ID: schema:anon/8c899adfe2a52fbaea1abce9d125a827b2b33cf6
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsPostResponse201ProjectType
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201ProjectType
- Schema ID: schema:anon/d45eded8a4a46298ca3ad48a64555bc5156433ce
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsPostResponse201Sector
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201Sector
- Schema ID: schema:anon/ced8f6167fe30f4f4c940766c58ca730c2028f4d

### Enum

Values: agriculture, airport, alcohol_establishment, amusement_park, animal_health_veterinary, animal_lodging, assembly, auto_parts_store, auto_service, auto_vehicle_terminal, automobile_retail, aviation, bank, bar_tavern, battery_energy_storage, behavioral_health, big_box_store, bowling_alley, brewery, bridges, business_park, campground, car_wash, casino, casino_hotel, cemetery, city_hall_operations, civil_infrastructure, college_university, commercial, convenience_store, convention_center, courthouse, cultural, dam, data_center, daycare_pre_k, dealership, death, dental, department_store, distillery, distribution_warehouse, district_operations, drug_store, dry_storage, educational, electrical_substation, elementary_school, energy, energy_distribution, energy_production, energy_storage, entertainment, entertainment_production, environmentally_controlled, event_space, fast_food_restaurant, fire_station, funeral_home, gas_station, golf, government, government_buildings, grocery_store, gym_athletic_studio, hangar, hazardous_storage, health_care, high_school, hospital, hospitality, hotel, hydro_power, individual_space, indoor, industrial, institutional, jail_prison, k_12, library, liquor_store, lodging, manufacturing, medical_center, medical_office_building_mob, middle_school, military_naval, miscellaneous_pavement, mixed_use, movie_theater, multifamily, museum, nuclear_power_plant, office, office_retail, oil_gas_mining, outdoor, outpatient_care, park, parking_garage, parking_lot, performing_arts, personal_service, pipe_line, playground, police_station, pool_swim_facility, post_office, production, psychiatric_hospital, public_safety, race_track, railway_terminal, railways, recreation, rehab_facility, religious_institution, research_development, reservoir, residential, residential_office_retail, residential_retail, restaurant, retail, roads_highways, runway_taxiway, rv_park, self_storage, senior_housing, sewer_systems, shopping_center_mall, sidewalk_walkways, single_family, solar_power, specialist_office, specialty_store, sports_courts, sports_fields, stadium_arena, storage, street_lights, student_housing, telecommunication, telecommunication_lines, terminal, trailer_park, transportation, transportation_terminals, tunnel, urgent_care, waste_collection, waste_infrastructure, waste_processing, waste_water, water_distribution, water_infrastructure, water_retention, water_treatment_plant_wwtp, wind_power, winery, winter_sports, zoo_aquarium, None

## RestV10ProjectsPostResponse201WorkScope
- Role: nested
- Parent: RestV10ProjectsPostResponse201DataObject
- Schema Name: RestV10ProjectsPostResponse201WorkScope
- Schema ID: schema:anon/6ce6588dfbd0c90f2533f1b6a3079e5092153e95

### Enum

Values: new_construction, renovation_alteration, maintenance_service, None
