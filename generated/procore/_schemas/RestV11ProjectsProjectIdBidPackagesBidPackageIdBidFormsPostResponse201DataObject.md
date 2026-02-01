# RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201DataObject

## RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201DataObject
- Role: parent
- Schema Name: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201
- Schema ID: schema:anon/08fee848a0d39b306f39c743bd45c3990a94c5fb
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `title` | `string` |
| `proposal_id` | `int` |
| `base_bid` | `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItem[]` |
| `alternates` | `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201AlternatesItem[]` |

### Nested Types
- `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201AlternatesItem`
- `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItem`
- `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemBidFormItemsItem`
- `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemBidFormItemsItemCostCode`
- `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemBidFormItemsItemItemType`
- `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemBidFormItemsItemResponseType`
- `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemSubSectionsItem`

## RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201AlternatesItem
- Role: nested
- Parent: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201AlternatesItem
- Schema ID: schema:anon/5aff659eaf2b63da421b37d689ba4ca6a15a52de
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `title` | `string` |
| `position` | `int` |
| `header` | `bool` |
| `bid_form_items` | `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemBidFormItemsItem[]` |
| `sub_sections` | `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemSubSectionsItem[]` |

## RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItem
- Role: nested
- Parent: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItem
- Schema ID: schema:anon/9e269e7fccd9b80a74db234fd86366f1bb492f51
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `title` | `string` |
| `position` | `int` |
| `header` | `bool` |
| `bid_form_items` | `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemBidFormItemsItem[]` |
| `sub_sections` | `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemSubSectionsItem[]` |

## RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemBidFormItemsItem
- Role: nested
- Parent: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemBidFormItemsItem
- Schema ID: schema:anon/420bb6540b6a017f8861968db1ff68fdb0eee44c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `cost_code` | `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemBidFormItemsItemCostCode` |
| `description` | `string` |
| `position` | `int` |
| `subject` | `string` |
| `item_type` | `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemBidFormItemsItemItemType` |
| `response_type` | `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemBidFormItemsItemResponseType` |
| `layer_id` | `int` |

## RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemBidFormItemsItemCostCode
- Role: nested
- Parent: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemBidFormItemsItemCostCode
- Schema ID: schema:anon/0b92a413c077bef2316d42527f6a798fb31f7087
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `full_code` | `string` |

## RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemBidFormItemsItemItemType
- Role: nested
- Parent: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemBidFormItemsItemItemType
- Schema ID: schema:anon/4d4ec510b91624c1f939b7c653a27bb7a3216dec

### Enum

Values: cost_code, plain_text

## RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemBidFormItemsItemResponseType
- Role: nested
- Parent: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemBidFormItemsItemResponseType
- Schema ID: schema:anon/3af8b9d9652553c0bd769a8a3d2629d70b889dbd

### Enum

Values: amount, unit, include_exclude

## RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemSubSectionsItem
- Role: nested
- Parent: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201DataObject
- Schema Name: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemSubSectionsItem
- Schema ID: schema:anon/8c01e887aed467b9fc7dc08e8de8d4bd5955e280
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `title` | `string` |
| `position` | `int` |
| `bid_form_items` | `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsPostResponse201BaseBidItemBidFormItemsItem[]` |
