# RestV10CompaniesCompanyIdBidPackagesGetResponse200DataObject

## RestV10CompaniesCompanyIdBidPackagesGetResponse200DataObject
- Role: parent
- Schema Name: RestV10CompaniesCompanyIdBidPackagesGetResponse200
- Schema ID: schema:anon/07c471c8d903b398fe46b5724eda54305e873392

### Fields

| Field | Type |
|------|------|
| `bidPackages` | `RestV10CompaniesCompanyIdBidPackagesGetResponse200BidpackagesItem[]` |

### Nested Types
- `RestV10CompaniesCompanyIdBidPackagesGetResponse200BidpackagesItem`
- `RestV10CompaniesCompanyIdBidPackagesGetResponse200BidpackagesItemLinks`

## RestV10CompaniesCompanyIdBidPackagesGetResponse200BidpackagesItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdBidPackagesGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdBidPackagesGetResponse200BidpackagesItem
- Schema ID: schema:anon/f683b0a5e4566530b83a49658aa652d2e8b15505
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `project_id` | `int` |
| `bid_due_date` | `string` |
| `number` | `int` |
| `title` | `string` |
| `project_name` | `string` |
| `project_location` | `string` |
| `accounting_method` | `string` |
| `formatted_bid_due_date` | `string` |
| `links` | `RestV10CompaniesCompanyIdBidPackagesGetResponse200BidpackagesItemLinks` |
| `allow_bidder_sum` | `bool` |
| `accept_post_due_submissions` | `bool` |
| `sealed` | `bool` |
| `bid_invites_sent_count` | `double` |
| `bids_received_count` | `double` |
| `enable_prebid_walkthrough` | `bool` |
| `enable_prebid_rfi_deadline` | `bool` |
| `pre_bid_rfi_deadline_date` | `string` |
| `formatted_bid_web_message` | `string` |
| `formatted_bid_email_message` | `string` |
| `formatted_pre_bid_walk_through_notes` | `string` |
| `has_bid_docs` | `bool` |
| `user_bid_id` | `int` |

## RestV10CompaniesCompanyIdBidPackagesGetResponse200BidpackagesItemLinks
- Role: nested
- Parent: RestV10CompaniesCompanyIdBidPackagesGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdBidPackagesGetResponse200BidpackagesItemLinks
- Schema ID: schema:anon/fec8ad234c2e13b51ee1f540d75d385bf9aad21b

### Fields

| Field | Type |
|------|------|
| `self` | `string` |
| `bid` | `string` |
| `bid_pdf` | `string` |
| `bid_list` | `string` |
| `emails` | `string` |
| `addendums` | `string` |
| `files` | `string` |
