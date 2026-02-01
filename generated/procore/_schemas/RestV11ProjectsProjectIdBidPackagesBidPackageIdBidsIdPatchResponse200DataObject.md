# RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200DataObject

## RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200DataObject
- Role: parent
- Schema Name: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200
- Schema ID: schema:anon/077f6b4f15b03d7e4e6be75529a021349ec0ac1a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `bid_package_id` | `int` |
| `bid_package_title` | `string` |
| `bid_form_title` | `string` |
| `awarded` | `bool` |
| `bidders_can_add_line_items` | `bool` |
| `bid_status` | `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200BidStatus` |
| `company_id` | `int` |
| `invitation_last_sent_at` | `string` |
| `is_bidder_committed` | `bool` |
| `lump_sum_amount` | `double` |
| `lump_sum_enabled` | `bool` |
| `submitted` | `bool` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `due_date` | `string` |
| `bidder_comments` | `string` |
| `show_bid_in_estimating` | `bool` |
| `bid_amount` | `string` |
| `bid_requester` | `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200BidRequester` |
| `deleted_at` | `string` |
| `bidder_notes` | `string` |
| `attachments_count` | `int` |
| `recipient_ids` | `int[]` |
| `recipient_list` | `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200RecipientListItem[]` |
| `recipient_list_with_email_and_number` | `string[]` |
| `mailto` | `string` |
| `bidder_inclusion` | `string` |
| `bidder_exclusion` | `string` |
| `bid_convertible_to_subcontract` | `bool` |
| `bid_convertible_to_purchase_order` | `bool` |
| `contract_button_disabled_reason` | `string` |
| `po_button_disabled_reason` | `string` |
| `links` | `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200Links` |
| `vendor` | `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200Vendor` |
| `project` | `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200Project` |
| `bid_items` | `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200BidItemsItem[]` |
| `cost_codes` | `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200CostCodesItem[]` |
| `attachments` | `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200AttachmentsItem[]` |
| `attachments_zip_streaming_url` | `string` |

### Nested Types
- `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200AttachmentsItem`
- `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200BidItemsItem`
- `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200BidRequester`
- `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200BidStatus`
- `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200CostCodesItem`
- `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200Links`
- `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200Project`
- `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200RecipientListItem`
- `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200Vendor`

## RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200AttachmentsItem
- Role: nested
- Parent: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200AttachmentsItem
- Schema ID: schema:anon/92256cccf4ca11f101361189189503c42ce974d3
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `item_type` | `string` |
| `prostore_file_id` | `int` |
| `url` | `string` |
| `name` | `string` |

## RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200BidItemsItem
- Role: nested
- Parent: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200BidItemsItem
- Schema ID: schema:anon/02135667e249fe3e32cf3a892d59b09bc16b3889
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `amount` | `double` |
| `bid_form_item_id` | `int` |
| `cost_code_id` | `int` |
| `cost_code_name` | `string` |
| `cost_code_number` | `string` |
| `id` | `int` |
| `included` | `bool` |
| `quantity` | `string` |
| `unit_cost` | `string` |
| `uom` | `string` |

## RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200BidRequester
- Role: nested
- Parent: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200BidRequester
- Schema ID: schema:anon/db682a40f36d2e0ceb9ba84a7757c8f4420432c0

### Fields

| Field | Type |
|------|------|
| `company` | `string` |
| `contact` | `string` |
| `company_address` | `string` |
| `company_phone` | `string` |
| `company_website` | `string` |
| `email_address` | `string` |
| `first_name` | `string` |
| `last_name` | `string` |
| `mobile_phone` | `string` |
| `vendor_address` | `string` |
| `business_phone` | `string` |
| `fax_number` | `string` |

## RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200BidStatus
- Role: nested
- Parent: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200BidStatus
- Schema ID: schema:anon/28625af38d480a595241491ff75b6b9db04d3f13

### Enum

Values: not_invited, undecided, will_not_bid, will_bid, submitted, awarded

## RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200CostCodesItem
- Role: nested
- Parent: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200CostCodesItem
- Schema ID: schema:anon/7a7d890c7fa0b0fc15a34087ae7717936b876e3d
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200Links
- Role: nested
- Parent: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200Links
- Schema ID: schema:anon/d7de26e3d706fc502871950a53cb91eeee9cf6da

### Fields

| Field | Type |
|------|------|
| `uploads` | `string` |
| `cost_codes` | `string` |
| `bid_pdf` | `string` |

## RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200Project
- Role: nested
- Parent: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200Project
- Schema ID: schema:anon/ef073db795fb35af5e9adfeacca37be6b28529ac

### Fields

| Field | Type |
|------|------|
| `name` | `string` |
| `address` | `string` |

## RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200RecipientListItem
- Role: nested
- Parent: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200RecipientListItem
- Schema ID: schema:anon/ec1eca46719ca08bb392e7fed0f39034636155bf

### Fields

| Field | Type |
|------|------|
| `first` | `string` |
| `last` | `string` |
| `email` | `string` |
| `numbers` | `string` |

## RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200Vendor
- Role: nested
- Parent: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200DataObject
- Schema Name: RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchResponse200Vendor
- Schema ID: schema:anon/96e2ed9a2451026b89a9afd8780a2f448a5ea216
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `avatar_url` | `string` |
| `trades` | `string` |
| `address` | `string` |
| `business_phone` | `string` |
