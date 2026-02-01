# RestV11ChangeEventsIdGetResponse200DataObject

## RestV11ChangeEventsIdGetResponse200DataObject
- Role: parent
- Schema Name: RestV11ChangeEventsIdGetResponse200
- Schema ID: schema:anon/b170ddb5d885f2654be3fa7ffb9cfa5d78bfc49d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `number` | `string` |
| `title` | `string` |
| `description` | `string` |
| `scope` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `deleted_at` | `string` |
| `comments_enabled` | `bool` |
| `deletable` | `bool` |
| `in_recycle_bin` | `bool` |
| `project_id` | `int` |
| `company_id` | `int` |
| `status` | `RestV11ChangeEventsIdGetResponse200Status` |
| `event_origin` | `RestV11ChangeEventsIdGetResponse200EventOrigin` |
| `change_type` | `RestV11ChangeEventsIdGetResponse200ChangeType` |
| `change_reason` | `RestV11ChangeEventsIdGetResponse200ChangeReason` |
| `prime_contract_for_estimates` | `RestV11ChangeEventsIdGetResponse200PrimeContractForEstimates` |
| `attachments` | `RestV11ChangeEventsIdGetResponse200AttachmentsItem[]` |
| `external_data` | `RestV11ChangeEventsIdGetResponse200ExternalData` |
| `created_by` | `RestV11ChangeEventsIdGetResponse200CreatedBy` |
| `custom_fields` | `RestV11ChangeEventsIdGetResponse200CustomFields` |
| `change_items` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItem[]` |
| `markup_items` | `RestV11ChangeEventsIdGetResponse200MarkupItemsItem[]` |
| `production_quantities` | `RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItem[]` |
| `notes` | `object` |
| `currency_configuration` | `RestV11ChangeEventsIdGetResponse200CurrencyConfiguration` |
| `source` | `RestV11ChangeEventsIdGetResponse200Source` |

### Nested Types
- `RestV11ChangeEventsIdGetResponse200AttachmentsItem`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItem`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetCode`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetCodeSegmentItemsItem`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetCodeSegmentItemsItemSegment`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetCodeSegmentItemsItemSegmentStructure`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpact`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetChange`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetChangeAdjustmentLineItem`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetChangeStatus`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetModification`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetModificationTransferFrom`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetModificationTransferTo`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactEstimate`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactEstimateCalculationStrategy`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactEstimateTransfer`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactSourceOfBudgetRom`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactSourceOfLatestBudgetImpact`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactSourceOfStage`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpact`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactChangeOrderPackage`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactChangeOrderPackageContractType`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactChangeOrderPackageLineItem`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactChangeOrderPackageType`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactCommitment`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactCommitmentContractType`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactCommitmentCurrencyConfiguration`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactCommitmentLineItem`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactCommitmentType`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactContract`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactContractConfirmed`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactContractConfirmedContractType`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactContractProposed`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactContractProposedContractType`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactEstimate`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactEstimateCalculationStrategy`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactNonCommitment`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactRequestForQuote`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactRequestForQuoteStatus`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactSourceOfLatestCost`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactSourceOfStage`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactVendor`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactVendorConfirmed`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactVendorProposed`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCurrencyConfiguration`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemLatestCostValues`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemLatestCostValuesCalculationStrategy`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemLatestRevenueValues`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemLatestRevenueValuesCalculationStrategy`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpact`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrder`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrderCurrencyConfiguration`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrderLineItem`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrderPackage`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrderPackageLineItem`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrderType`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactEstimate`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactEstimateCalculationStrategy`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactSourceOfLatestPrice`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactSourceOfRevenueRom`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactSourceOfStage`
- `RestV11ChangeEventsIdGetResponse200ChangeItemsItemSource`
- `RestV11ChangeEventsIdGetResponse200ChangeReason`
- `RestV11ChangeEventsIdGetResponse200ChangeType`
- `RestV11ChangeEventsIdGetResponse200CreatedBy`
- `RestV11ChangeEventsIdGetResponse200CurrencyConfiguration`
- `RestV11ChangeEventsIdGetResponse200CustomFields`
- `RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldBooleanDefinitionId}`
- `RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldDecimalDefinitionId}`
- `RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}`
- `RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem`
- `RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}`
- `RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value`
- `RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldStringDefinitionId}`
- `RestV11ChangeEventsIdGetResponse200EventOrigin`
- `RestV11ChangeEventsIdGetResponse200ExternalData`
- `RestV11ChangeEventsIdGetResponse200MarkupItemsItem`
- `RestV11ChangeEventsIdGetResponse200MarkupItemsItemRevenue`
- `RestV11ChangeEventsIdGetResponse200PrimeContractForEstimates`
- `RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItem`
- `RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemBudgetChange`
- `RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemBudgetChangeProductionQuantity`
- `RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemEstimate`
- `RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemPrimeChangeOrder`
- `RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemPrimeChangeOrderProductionQuantity`
- `RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemPrimeChangeOrderType`
- `RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemProductionCode`
- `RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemProductionCodeCostCode`
- `RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemProductionCodeSubJob`
- `RestV11ChangeEventsIdGetResponse200Source`
- `RestV11ChangeEventsIdGetResponse200Status`

## RestV11ChangeEventsIdGetResponse200AttachmentsItem
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200AttachmentsItem
- Schema ID: schema:anon/d18d3b9dc65c54fe7d7e4207095f60cbc5df9809
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `url` | `string` |
| `filename` | `string` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItem
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItem
- Schema ID: schema:anon/6c76508ccc9b9b420664865ddeacf7fa9e7e76d0
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `budget_code` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetCode` |
| `budget_impact` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpact` |
| `cost_impact` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpact` |
| `created_at` | `string` |
| `currency_configuration` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCurrencyConfiguration` |
| `deletable` | `bool` |
| `deleted_at` | `string` |
| `description` | `string` |
| `editable` | `bool` |
| `event_id` | `int` |
| `event_number` | `string` |
| `event_title` | `string` |
| `id` | `int` |
| `item_type` | `string` |
| `latest_cost_values` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemLatestCostValues` |
| `latest_revenue_values` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemLatestRevenueValues` |
| `line_aging` | `int` |
| `notes` | `object` |
| `revenue_impact` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpact` |
| `source` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemSource` |
| `updated_at` | `string` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetCode
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetCode
- Schema ID: schema:anon/6355672510c6aa3381c0d525f9942be80a2dd300
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `flat_code` | `string` |
| `description` | `string` |
| `segment_items` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetCodeSegmentItemsItem[]` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetCodeSegmentItemsItem
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetCodeSegmentItemsItem
- Schema ID: schema:anon/89d016886228f63fa0772725792f97691ac29a03
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `code` | `string` |
| `name` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `parent_id` | `int` |
| `path_ids` | `int[]` |
| `path_code` | `string` |
| `is_parent` | `bool` |
| `path_codes` | `string[]` |
| `path_names` | `string[]` |
| `in_use` | `bool` |
| `segment` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetCodeSegmentItemsItemSegment` |
| `status` | `string` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetCodeSegmentItemsItemSegment
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetCodeSegmentItemsItemSegment
- Schema ID: schema:anon/68b6bfdf75240af7235639d0a029bb129381733f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `type` | `string` |
| `position` | `int` |
| `delimiter` | `string` |
| `required` | `bool` |
| `segment_items_count` | `int` |
| `project_can_modify_origin_project` | `bool` |
| `project_can_delete_origin_company` | `bool` |
| `structure` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetCodeSegmentItemsItemSegmentStructure` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `wbs_pattern_id` | `int` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetCodeSegmentItemsItemSegmentStructure
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetCodeSegmentItemsItemSegmentStructure
- Schema ID: schema:anon/3b31c829ab7b03472fa73a63a427f7fb0a027310

### Enum

Values: tiered, flat

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpact
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpact
- Schema ID: schema:anon/a707ea39468e8ffd72b4cf4d20ffd395ddd2858c

### Fields

| Field | Type |
|------|------|
| `budget_change` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetChange` |
| `budget_modification` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetModification` |
| `estimate` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactEstimate` |
| `source_of_latest_budget_impact` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactSourceOfLatestBudgetImpact` |
| `source_of_stage` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactSourceOfStage` |
| `source_of_budget_rom` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactSourceOfBudgetRom` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetChange
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetChange
- Schema ID: schema:anon/4b67076da1f61e81e0c7c27824808ebbd27739d9
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `adjustment_line_item` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetChangeAdjustmentLineItem` |
| `days_in_stage` | `int` |
| `id` | `int` |
| `in_status_since` | `string` |
| `number` | `int` |
| `status` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetChangeStatus` |
| `title` | `string` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetChangeAdjustmentLineItem
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetChangeAdjustmentLineItem
- Schema ID: schema:anon/350c27cdedb9d96651c392113c5a9dbd7743674c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `amount` | `string` |
| `id` | `int` |
| `number` | `int` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetChangeStatus
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetChangeStatus
- Schema ID: schema:anon/9feb3d246b56349acb9862a80cbe9f5cb0811e61

### Enum

Values: approved, draft, under_review, void

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetModification
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetModification
- Schema ID: schema:anon/955816d17a144dd1a260e7934d5e9739eb5253d3
- Primary Key: BudgetModificationId

### Fields

| Field | Type |
|------|------|
| `budget_modification_id` | `int` |
| `amount` | `string` |
| `notes` | `string` |
| `transfer_from` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetModificationTransferFrom` |
| `transfer_to` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetModificationTransferTo` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetModificationTransferFrom
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetModificationTransferFrom
- Schema ID: schema:anon/952e43abb00c9c63e9825a064713c5349cf0a222
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetModificationTransferTo
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactBudgetModificationTransferTo
- Schema ID: schema:anon/e1b401db61ec68fbb9b97cdefe0cb567e968cc9e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactEstimate
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactEstimate
- Schema ID: schema:anon/6712e06c8861094fab909674eb4e896b00ed060e

### Fields

| Field | Type |
|------|------|
| `amount` | `string` |
| `amount_project_currency` | `string` |
| `auto_balance` | `bool` |
| `calculation_strategy` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactEstimateCalculationStrategy` |
| `quantity` | `string` |
| `transfer` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactEstimateTransfer` |
| `unit_cost` | `string` |
| `unit_cost_project_currency` | `string` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactEstimateCalculationStrategy
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactEstimateCalculationStrategy
- Schema ID: schema:anon/761c04b2531dfb1898b43d3da23fe2d6cc3d938a

### Enum

Values: automatic, manual

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactEstimateTransfer
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactEstimateTransfer
- Schema ID: schema:anon/f0fd627c83399f17aaf425682add95bcbd2eb8fd

### Fields

| Field | Type |
|------|------|
| `amount` | `string` |
| `from_wbs_code` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetCode` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactSourceOfBudgetRom
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactSourceOfBudgetRom
- Schema ID: schema:anon/42332da8830d4f5193f626a05ecf0b0dc591393f

### Enum

Values: automatic, manual, quantity_by_unit_cost

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactSourceOfLatestBudgetImpact
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactSourceOfLatestBudgetImpact
- Schema ID: schema:anon/49a7a2b0a2ab9b8d51e4c8f3d8d9dfa85987e692

### Enum

Values: budget_change, estimate

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactSourceOfStage
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetImpactSourceOfStage
- Schema ID: schema:anon/a199d37efad311b1d1364a6975200bef0dfec640

### Enum

Values: estimate, budget_change

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpact
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpact
- Schema ID: schema:anon/f7ff3871cc98e6537536acdad4c6ad82d0c1ac6d

### Fields

| Field | Type |
|------|------|
| `change_order_package` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactChangeOrderPackage` |
| `commitment` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactCommitment` |
| `contract` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactContract` |
| `estimate` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactEstimate` |
| `non_commitment` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactNonCommitment` |
| `request_for_quote` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactRequestForQuote` |
| `source_of_latest_cost` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactSourceOfLatestCost` |
| `source_of_stage` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactSourceOfStage` |
| `vendor` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactVendor` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactChangeOrderPackage
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactChangeOrderPackage
- Schema ID: schema:anon/a021c68c23559d958a9bc0561e95ed2adf0e2eb4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `contract_type` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactChangeOrderPackageContractType` |
| `days_in_stage` | `int` |
| `id` | `int` |
| `in_status_since` | `string` |
| `line_item` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactChangeOrderPackageLineItem` |
| `number` | `string` |
| `status` | `string` |
| `title` | `string` |
| `type` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactChangeOrderPackageType` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactChangeOrderPackageContractType
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactChangeOrderPackageContractType
- Schema ID: schema:anon/68e08698d50f7a4e0581d0db2d3d5ece47a557de

### Enum

Values: purchase_order_contract, work_order_contract

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactChangeOrderPackageLineItem
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactChangeOrderPackageLineItem
- Schema ID: schema:anon/7bc1567554d3c894df348d6428770f219cab55a4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `amount` | `string` |
| `amount_project_currency` | `string` |
| `id` | `int` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactChangeOrderPackageType
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactChangeOrderPackageType
- Schema ID: schema:anon/e9bec10f163b1bd0f8c554834c485e41eee5cd77

### Enum

Values: change_order_package

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactCommitment
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactCommitment
- Schema ID: schema:anon/2e278673b3a37eafde62d10441f6d8ff39196d06
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `contract_type` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactCommitmentContractType` |
| `currency_configuration` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactCommitmentCurrencyConfiguration` |
| `days_in_stage` | `int` |
| `id` | `int` |
| `in_status_since` | `string` |
| `line_item` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactCommitmentLineItem` |
| `number` | `string` |
| `status` | `string` |
| `title` | `string` |
| `type` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactCommitmentType` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactCommitmentContractType
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactCommitmentContractType
- Schema ID: schema:anon/f85d7677eb595874f55fba5458c40875c517c39e

### Enum

Values: purchase_order_contract, work_order_contract

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactCommitmentCurrencyConfiguration
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactCommitmentCurrencyConfiguration
- Schema ID: schema:anon/ba9d4cd22cf95923b41eb454359827e7f18f2b2e

### Fields

| Field | Type |
|------|------|
| `base_currency_iso_code` | `string` |
| `currency_exchange_rate` | `string` |
| `currency_iso_code` | `string` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactCommitmentLineItem
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactCommitmentLineItem
- Schema ID: schema:anon/b2c678b6511fc6f1c6031ebb79e68db783dd0e0e
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `amount` | `string` |
| `amount_project_currency` | `string` |
| `id` | `int` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactCommitmentType
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactCommitmentType
- Schema ID: schema:anon/3a51641b9ccc6931ee6b5a009ed12b6109738ad5

### Enum

Values: potential_change_order, change_order_package, contract

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactContract
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactContract
- Schema ID: schema:anon/3dac5b5338ba66bd932483b94d4eeb7db160bc2e

### Fields

| Field | Type |
|------|------|
| `proposed` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactContractProposed` |
| `confirmed` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactContractConfirmed` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactContractConfirmed
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactContractConfirmed
- Schema ID: schema:anon/a92589f40d2bf1971b8491ec153011fb5f2436e6
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `contract_type` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactContractConfirmedContractType` |
| `number` | `string` |
| `status` | `string` |
| `title` | `string` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactContractConfirmedContractType
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactContractConfirmedContractType
- Schema ID: schema:anon/228dac25544c7a8a9fe655d40bde577d54ed503d

### Enum

Values: purchase_order_contract, work_order_contract

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactContractProposed
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactContractProposed
- Schema ID: schema:anon/f1149cf9644696b0c679b0044c43b5b5faceace0
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `contract_type` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactContractProposedContractType` |
| `number` | `string` |
| `status` | `string` |
| `title` | `string` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactContractProposedContractType
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactContractProposedContractType
- Schema ID: schema:anon/b6cc22c8ad3a07cfc7629e97fb23a1342d661584

### Enum

Values: purchase_order_contract, work_order_contract

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactEstimate
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactEstimate
- Schema ID: schema:anon/104d3beada82474274215d787cfa47e047e27868

### Fields

| Field | Type |
|------|------|
| `amount` | `string` |
| `calculation_strategy` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactEstimateCalculationStrategy` |
| `quantity` | `string` |
| `unit_cost` | `string` |
| `unit_of_measure` | `string` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactEstimateCalculationStrategy
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactEstimateCalculationStrategy
- Schema ID: schema:anon/a10e7a8f6a9ee6b97ecf52a321fac3bcdbf84cf2

### Enum

Values: automatic, manual

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactNonCommitment
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactNonCommitment
- Schema ID: schema:anon/f2aac78772c818d817806e4974669218b6bc6061

### Fields

| Field | Type |
|------|------|
| `amount` | `string` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactRequestForQuote
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactRequestForQuote
- Schema ID: schema:anon/06699c115197c93ea9f352fb55f5be8b795673a0
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `days_in_stage` | `int` |
| `id` | `int` |
| `in_status_since` | `string` |
| `latest_quote_amount` | `string` |
| `number` | `string` |
| `status` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactRequestForQuoteStatus` |
| `title` | `string` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactRequestForQuoteStatus
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactRequestForQuoteStatus
- Schema ID: schema:anon/247a4d9b869126892c96a2850dfea57a44ec536c

### Enum

Values: closed, out_for_pricing, pending_final_approval, revise_and_resubmit, under_review, withdrawn

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactSourceOfLatestCost
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactSourceOfLatestCost
- Schema ID: schema:anon/4571f9c0d78f4f187c6e62cd39a0877a6e5d6896

### Enum

Values: commitment, estimate, latest_quote, non_commitment

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactSourceOfStage
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactSourceOfStage
- Schema ID: schema:anon/5cf8798d35b952c496410f9fb36df9625187515e

### Enum

Values: estimate, non-commitment, commitment, change_order_package, latest_quote

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactVendor
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactVendor
- Schema ID: schema:anon/371e4ed54facfe891316c16a0178866bf0c3fc48

### Fields

| Field | Type |
|------|------|
| `confirmed` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactVendorConfirmed` |
| `proposed` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactVendorProposed` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactVendorConfirmed
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactVendorConfirmed
- Schema ID: schema:anon/0f798c3e9f5474eba65d4bd3bc7e0cee691eebcd
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactVendorProposed
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactVendorProposed
- Schema ID: schema:anon/b3eb1da6a93cdabca1d12967615418aedbfc2e3f
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemCurrencyConfiguration
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemCurrencyConfiguration
- Schema ID: schema:anon/434938764231cff0df328bed520626e289350915

### Fields

| Field | Type |
|------|------|
| `currency_iso_code` | `string` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemLatestCostValues
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemLatestCostValues
- Schema ID: schema:anon/1c4c91a08ab0329cbd674529b36f536a9eb11683

### Fields

| Field | Type |
|------|------|
| `amount` | `string` |
| `amount_project_currency` | `string` |
| `calculation_strategy` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemLatestCostValuesCalculationStrategy` |
| `quantity` | `string` |
| `unit_cost` | `string` |
| `unit_cost_project_currency` | `string` |
| `unit_of_measure` | `string` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemLatestCostValuesCalculationStrategy
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemLatestCostValuesCalculationStrategy
- Schema ID: schema:anon/5068e9b7c408778d9f424f8849d4cf9d07b1dbb2

### Enum

Values: automatic, manual

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemLatestRevenueValues
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemLatestRevenueValues
- Schema ID: schema:anon/af858c7f004cf77b4c6bdbf7bf1a396a624d173e

### Fields

| Field | Type |
|------|------|
| `amount` | `string` |
| `amount_project_currency` | `string` |
| `calculation_strategy` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemLatestRevenueValuesCalculationStrategy` |
| `quantity` | `string` |
| `unit_cost` | `string` |
| `unit_cost_project_currency` | `string` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemLatestRevenueValuesCalculationStrategy
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemLatestRevenueValuesCalculationStrategy
- Schema ID: schema:anon/bcff784258c844d6044464a2495c194a0671a0c3

### Enum

Values: automatic, manual

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpact
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpact
- Schema ID: schema:anon/ba0bd77f33c915129708924ce7682519c384c2f2

### Fields

| Field | Type |
|------|------|
| `estimate` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactEstimate` |
| `change_order` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrder` |
| `change_order_package` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrderPackage` |
| `source_of_latest_price` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactSourceOfLatestPrice` |
| `source_of_revenue_rom` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactSourceOfRevenueRom` |
| `source_of_stage` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactSourceOfStage` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrder
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrder
- Schema ID: schema:anon/fe2662f847b5f4cf75adc800896443ee2846bbea
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `contract_id` | `int` |
| `currency_configuration` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrderCurrencyConfiguration` |
| `days_in_stage` | `int` |
| `id` | `int` |
| `in_status_since` | `string` |
| `line_item` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrderLineItem` |
| `number` | `string` |
| `status` | `string` |
| `title` | `string` |
| `type` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrderType` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrderCurrencyConfiguration
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrderCurrencyConfiguration
- Schema ID: schema:anon/6b1db0783ba537d5ce8b1e8fcdf5462338541765

### Fields

| Field | Type |
|------|------|
| `base_currency_iso_code` | `string` |
| `currency_exchange_rate` | `string` |
| `currency_iso_code` | `string` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrderLineItem
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrderLineItem
- Schema ID: schema:anon/61a29d72226171f1320d99239587b03971de5711
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `amount` | `string` |
| `amount_project_currency` | `string` |
| `id` | `int` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrderPackage
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrderPackage
- Schema ID: schema:anon/06076e0a2f53d9967c10dfc5d6855d96733bef06
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `contract_id` | `int` |
| `days_in_stage` | `int` |
| `id` | `int` |
| `in_status_since` | `string` |
| `line_item` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrderPackageLineItem` |
| `number` | `string` |
| `status` | `string` |
| `title` | `string` |
| `type` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemCostImpactChangeOrderPackageType` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrderPackageLineItem
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrderPackageLineItem
- Schema ID: schema:anon/5efa70d22cc706805aaa9d539fb79edc0ac9b776
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `amount` | `string` |
| `id` | `int` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrderType
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactChangeOrderType
- Schema ID: schema:anon/a7535e9a96286507a6cedab6481b6a9acc5c03d0

### Enum

Values: potential_change_order, change_order_package

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactEstimate
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactEstimate
- Schema ID: schema:anon/00ec64282828a8cd19955a8fb508b568a6875bd3

### Fields

| Field | Type |
|------|------|
| `quantity` | `string` |
| `unit_cost` | `string` |
| `unit_cost_project_currency` | `string` |
| `amount` | `string` |
| `amount_project_currency` | `string` |
| `calculation_strategy` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactEstimateCalculationStrategy` |

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactEstimateCalculationStrategy
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactEstimateCalculationStrategy
- Schema ID: schema:anon/01f58e1381364eb940e9219dd1eecc67849a120f

### Enum

Values: automatic, manual

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactSourceOfLatestPrice
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactSourceOfLatestPrice
- Schema ID: schema:anon/cf109296526de28420329b81009cce6fb1edfca4

### Enum

Values: change_order, estimate

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactSourceOfRevenueRom
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactSourceOfRevenueRom
- Schema ID: schema:anon/0a9c5f7ec4f19a0ae600e9e87dd0bcc75e8ea7c7

### Enum

Values: automatic, latest_cost, manual, no_revenue_expected

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactSourceOfStage
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemRevenueImpactSourceOfStage
- Schema ID: schema:anon/1a3747a5846505fbd7b6b925dac72163d96f4faf

### Enum

Values: estimate, change_order, change_order_package

## RestV11ChangeEventsIdGetResponse200ChangeItemsItemSource
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeItemsItemSource
- Schema ID: schema:anon/1f707e190f4cbbee3547a534c63a979f8a5f5d70

### Enum

Values: change_event, budget_change, field_initiated_change_orders

## RestV11ChangeEventsIdGetResponse200ChangeReason
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeReason
- Schema ID: schema:anon/2deece25e5fffa267460d6a311bdadc790373138
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `change_reason` | `string` |

## RestV11ChangeEventsIdGetResponse200ChangeType
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ChangeType
- Schema ID: schema:anon/96e8662e46338489e973d988e2d21f970e844871
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `abbreviation` | `string` |

## RestV11ChangeEventsIdGetResponse200CreatedBy
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200CreatedBy
- Schema ID: schema:anon/5bba7d5ae51c6ca8461b8beff3117c4ccd65d1a4
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `login` | `string` |
| `name` | `string` |

## RestV11ChangeEventsIdGetResponse200CurrencyConfiguration
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200CurrencyConfiguration
- Schema ID: schema:anon/570d4724c1bbedcc5827002fa1ca7ca044684471

### Fields

| Field | Type |
|------|------|
| `currency_iso_code` | `string` |

## RestV11ChangeEventsIdGetResponse200CustomFields
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200CustomFields
- Schema ID: schema:anon/fbbbdf310d374c7df5714c86d51abac7a107e10a

### Fields

| Field | Type |
|------|------|
| `custom_field_%{custom_field_string_definition_id}` | `RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldStringDefinitionId}` |
| `custom_field_%{custom_field_decimal_definition_id}` | `RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldDecimalDefinitionId}` |
| `custom_field_%{custom_field_boolean_definition_id}` | `RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldBooleanDefinitionId}` |
| `custom_field_%{custom_field_lov_entry_definition_id}` | `RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}` |
| `custom_field_%{custom_field_lov_entries_definition_id}` | `RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}` |

## RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldBooleanDefinitionId}
- Schema ID: schema:anon/990ff11816957d5e13e8054a3b4018ca5a889aae

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `bool` |

## RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldDecimalDefinitionId}
- Schema ID: schema:anon/2ca25eca8308998fe557ed8b7c6a2efae4b3c787

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `double` |

## RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}
- Schema ID: schema:anon/8ac6165387eee0f8b62fd6116b007679069365e9

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem[]` |

## RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntriesDefinitionId}ValueItem
- Schema ID: schema:anon/e3d6cf7b64c48c5d41072f1f551520b2e5e9c56d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}
- Schema ID: schema:anon/3a3c35d457351cba94d43fe7ae5875cdca53185f

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value` |

## RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldLovEntryDefinitionId}Value
- Schema ID: schema:anon/bfeb38dd91125f9638d7a4d955a8a35669e8d683
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |

## RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldStringDefinitionId}
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200CustomFieldsCustomField%{customFieldStringDefinitionId}
- Schema ID: schema:anon/3e79a4fea4c4a312821d65e59e171469329ba818

### Fields

| Field | Type |
|------|------|
| `data_type` | `string` |
| `value` | `string` |

## RestV11ChangeEventsIdGetResponse200EventOrigin
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200EventOrigin
- Schema ID: schema:anon/d5f155586cd149b6423476fdd2b6818d6f6144d3
- Primary Key: OriginId

### Fields

| Field | Type |
|------|------|
| `origin_id` | `int` |
| `origin_type` | `string` |
| `display_name` | `string` |
| `web_page_url` | `string` |

## RestV11ChangeEventsIdGetResponse200ExternalData
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ExternalData
- Schema ID: schema:anon/233b22b69cabb9a15f6ad813cbd66793ad6f1e06
- Primary Key: OriginId

### Fields

| Field | Type |
|------|------|
| `origin_id` | `string` |
| `origin_data` | `string` |

## RestV11ChangeEventsIdGetResponse200MarkupItemsItem
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200MarkupItemsItem
- Schema ID: schema:anon/1d6893afcdc88d460bba243b580744a67592584b
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `event_id` | `int` |
| `item_type` | `string` |
| `wbs_code` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetCode` |
| `revenue` | `RestV11ChangeEventsIdGetResponse200MarkupItemsItemRevenue` |

## RestV11ChangeEventsIdGetResponse200MarkupItemsItemRevenue
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200MarkupItemsItemRevenue
- Schema ID: schema:anon/88e493be684f9115191c82eb61069ad97c56f605
- Primary Key: EstimateAmount

### Fields

| Field | Type |
|------|------|
| `estimate_amount` | `string` |
| `change_order_amount` | `string` |
| `latest_price_amount` | `string` |

## RestV11ChangeEventsIdGetResponse200PrimeContractForEstimates
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200PrimeContractForEstimates
- Schema ID: schema:anon/03c6fac8430897457996b060fd8a519cd96bfe06
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `number` | `string` |
| `name` | `string` |

## RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItem
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItem
- Schema ID: schema:anon/587004f6188db17109d339a7b927dfdaf68f27ff
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `event_id` | `int` |
| `item_type` | `string` |
| `estimate` | `RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemEstimate` |
| `production_code` | `RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemProductionCode` |
| `budget_change` | `RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemBudgetChange` |
| `disabled_fields` | `string[]` |
| `prime_change_order` | `RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemPrimeChangeOrder` |

## RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemBudgetChange
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemBudgetChange
- Schema ID: schema:anon/2457f1bce603252b9bb07b1aabc6c4ea21f521cb
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `number` | `int` |
| `title` | `string` |
| `description` | `string` |
| `status` | `string` |
| `production_quantity` | `RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemBudgetChangeProductionQuantity` |

## RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemBudgetChangeProductionQuantity
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemBudgetChangeProductionQuantity
- Schema ID: schema:anon/08c6ebfa696aed96d36228f60cadd04e60871004
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `unit_of_measure` | `string` |
| `quantity` | `string` |

## RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemEstimate
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemEstimate
- Schema ID: schema:anon/3758a3c390f1ffae5ee6657c6622fc47023f7d28

### Fields

| Field | Type |
|------|------|
| `quantity` | `string` |
| `unit_of_measure` | `string` |

## RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemPrimeChangeOrder
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemPrimeChangeOrder
- Schema ID: schema:anon/21ed3583353d1b6a727b389c639113ee1883b007
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `type` | `RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemPrimeChangeOrderType` |
| `number` | `int` |
| `title` | `string` |
| `description` | `string` |
| `status` | `string` |
| `contract_id` | `int` |
| `production_quantity` | `RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemPrimeChangeOrderProductionQuantity` |

## RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemPrimeChangeOrderProductionQuantity
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemPrimeChangeOrderProductionQuantity
- Schema ID: schema:anon/0b76a158e61bef0d236643ebe6311a7e3e7f62c7
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `unit_of_measure` | `string` |
| `quantity` | `string` |

## RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemPrimeChangeOrderType
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemPrimeChangeOrderType
- Schema ID: schema:anon/d20255607cc50a8bc98aff25c032523214d43014

### Enum

Values: potential_change_order, change_order_package

## RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemProductionCode
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemProductionCode
- Schema ID: schema:anon/ffe8636df7a237fbffe1b2cbb4e4799d5ad5218e
- Primary Key: CostCode

### Fields

| Field | Type |
|------|------|
| `cost_code` | `RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemProductionCodeCostCode` |
| `sub_job` | `RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemProductionCodeSubJob` |
| `wbs_code` | `RestV11ChangeEventsIdGetResponse200ChangeItemsItemBudgetCode` |

## RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemProductionCodeCostCode
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemProductionCodeCostCode
- Schema ID: schema:anon/cdeeaeda0b7517fe90496812151ef42eaa3e6211
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `description` | `string` |

## RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemProductionCodeSubJob
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200ProductionQuantitiesItemProductionCodeSubJob
- Schema ID: schema:anon/7a094ddc49c036ddb614bb5bfd8e085a00142332
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV11ChangeEventsIdGetResponse200Source
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200Source
- Schema ID: schema:anon/d1bad7db6cfa5ae56d19193fb61fe52a48ecceec

### Enum

Values: budget_change, field_initiated_change_orders

## RestV11ChangeEventsIdGetResponse200Status
- Role: nested
- Parent: RestV11ChangeEventsIdGetResponse200DataObject
- Schema Name: RestV11ChangeEventsIdGetResponse200Status
- Schema ID: schema:anon/10e6f4a96cd8008a3830fbb902a2b9f45d4b2052
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `mapped_to_status` | `string` |
