# RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200DataObject

## RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200DataObject
- Role: parent
- Schema Name: RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200
- Schema ID: schema:anon/ad201b7ce1b06488ec077cabb54547ad1475d865
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `title` | `string` |
| `proposal_id` | `int` |
| `lock_unit_fields_base_bid` | `bool` |
| `lock_quantity_fields_base_bid` | `bool` |
| `lock_unit_fields_alternates` | `bool` |
| `lock_quantity_fields_alternates` | `bool` |
| `base_bid` | `RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItem[]` |
| `alternates` | `RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200AlternatesItem[]` |

### Nested Types
- `RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200AlternatesItem`
- `RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItem`
- `RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemBidFormItemsItem`
- `RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemBidFormItemsItemCostCode`
- `RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemBidFormItemsItemItemType`
- `RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemBidFormItemsItemResponseType`
- `RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemSubSectionsItem`

## RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200AlternatesItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200AlternatesItem
- Schema ID: schema:anon/5aff659eaf2b63da421b37d689ba4ca6a15a52de
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `title` | `string` |
| `position` | `int` |
| `header` | `bool` |
| `bid_form_items` | `RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemBidFormItemsItem[]` |
| `sub_sections` | `RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemSubSectionsItem[]` |

## RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItem
- Schema ID: schema:anon/9e269e7fccd9b80a74db234fd86366f1bb492f51
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `title` | `string` |
| `position` | `int` |
| `header` | `bool` |
| `bid_form_items` | `RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemBidFormItemsItem[]` |
| `sub_sections` | `RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemSubSectionsItem[]` |

## RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemBidFormItemsItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemBidFormItemsItem
- Schema ID: schema:anon/420bb6540b6a017f8861968db1ff68fdb0eee44c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `cost_code` | `RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemBidFormItemsItemCostCode` |
| `description` | `string` |
| `position` | `int` |
| `subject` | `string` |
| `item_type` | `RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemBidFormItemsItemItemType` |
| `response_type` | `RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemBidFormItemsItemResponseType` |
| `layer_id` | `int` |

## RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemBidFormItemsItemCostCode
- Role: nested
- Parent: RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemBidFormItemsItemCostCode
- Schema ID: schema:anon/0b92a413c077bef2316d42527f6a798fb31f7087
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `full_code` | `string` |

## RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemBidFormItemsItemItemType
- Role: nested
- Parent: RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemBidFormItemsItemItemType
- Schema ID: schema:anon/4d4ec510b91624c1f939b7c653a27bb7a3216dec

### Enum

Values: cost_code, plain_text

## RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemBidFormItemsItemResponseType
- Role: nested
- Parent: RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemBidFormItemsItemResponseType
- Schema ID: schema:anon/3af8b9d9652553c0bd769a8a3d2629d70b889dbd

### Enum

Values: amount, unit, include_exclude

## RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemSubSectionsItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemSubSectionsItem
- Schema ID: schema:anon/8c01e887aed467b9fc7dc08e8de8d4bd5955e280
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `title` | `string` |
| `position` | `int` |
| `bid_form_items` | `RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGetResponse200BaseBidItemBidFormItemsItem[]` |
