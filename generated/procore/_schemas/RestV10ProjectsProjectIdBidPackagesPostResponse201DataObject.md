# RestV10ProjectsProjectIdBidPackagesPostResponse201DataObject

## RestV10ProjectsProjectIdBidPackagesPostResponse201DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdBidPackagesPostResponse201
- Schema ID: schema:anon/52dea7e9d173141e201fbc179c1631ff3ab8b919
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `accept_post_due_submissions` | `bool` |
| `accounting_method` | `string` |
| `allow_bidder_sum` | `bool` |
| `project_currency_iso_code` | `string` |
| `project_currency_display` | `string` |
| `anticipated_award_date` | `string` |
| `bidding_countdown_email_days` | `int` |
| `bid_docs_manifest` | `RestV10ProjectsProjectIdBidPackagesPostResponse201BidDocsManifest` |
| `bid_due_date` | `string` |
| `bid_email_message` | `string` |
| `bid_emails_include_link_to_bidding_documents` | `bool` |
| `bid_submission_confirmation` | `string` |
| `bid_web_message` | `string` |
| `blind_bidding` | `bool` |
| `created_by` | `RestV10ProjectsProjectIdBidPackagesPostResponse201CreatedBy` |
| `distribution_members` | `RestV10ProjectsProjectIdBidPackagesPostResponse201DistributionMembersItem[]` |
| `display_project_name` | `bool` |
| `bid_form_sections_enabled` | `bool` |
| `flexible_response_types_enabled` | `bool` |
| `distribution_member_ids` | `int[]` |
| `enable_countdown_emails` | `bool` |
| `enable_prebid_rfi_deadline` | `bool` |
| `enable_prebid_walkthrough` | `bool` |
| `has_any_bid_invited` | `bool` |
| `has_bids_sent_nda` | `bool` |
| `has_no_nda_activity` | `bool` |
| `nda_invited_bids_with_activity_count` | `int` |
| `attachments_zip_streaming_url` | `string` |
| `hidden` | `bool` |
| `id` | `int` |
| `links` | `RestV10ProjectsProjectIdBidPackagesPostResponse201Links` |
| `lump_sum_bidding` | `bool` |
| `manager` | `RestV10ProjectsProjectIdBidPackagesPostResponse201Manager` |
| `nda_attachments` | `RestV10ProjectsProjectIdBidPackagesPostResponse201NdaAttachmentsItem[]` |
| `number` | `int` |
| `open` | `bool` |
| `point_of_contact` | `RestV10ProjectsProjectIdBidPackagesPostResponse201PointOfContact` |
| `point_of_contact_login_id` | `int` |
| `pre_bid_rfi_deadline_date` | `string` |
| `pre_bid_walk_through_date` | `string` |
| `pre_bid_walk_through_notes` | `string` |
| `project_id` | `int` |
| `project_image_url` | `string` |
| `project_latitude` | `string` |
| `project_location` | `string` |
| `project_longitude` | `string` |
| `project_name` | `string` |
| `require_nda` | `bool` |
| `sealed` | `bool` |
| `show_bid_info` | `bool` |
| `submitted_bids_count` | `int` |
| `title` | `string` |
| `enable_public_discovery` | `bool` |
| `primary_slug_with_ids` | `string` |
| `pre_bid_meeting_location` | `string` |
| `pre_bid_meeting_date` | `string` |
| `pre_bid_meeting_online_link` | `string` |
| `pre_bid_meeting_notes` | `string` |
| `public_project_funding_source` | `string` |
| `show_location_for_nda_projects` | `bool` |
| `public_bid_opening_details_date` | `string` |
| `public_bid_opening_details_location` | `string` |
| `public_bid_opening_details_online_link` | `string` |
| `trades_and_services` | `RestV10ProjectsProjectIdBidPackagesPostResponse201TradesAndServicesItem[]` |
| `business_classifications` | `RestV10ProjectsProjectIdBidPackagesPostResponse201BusinessClassificationsItem[]` |
| `lock_unit_fields_base_bid` | `bool` |
| `lock_quantity_fields_base_bid` | `bool` |
| `lock_unit_fields_alternates` | `bool` |
| `lock_quantity_fields_alternates` | `bool` |
| `has_pdm_documents` | `bool` |

### Nested Types
- `RestV10ProjectsProjectIdBidPackagesPostResponse201BidDocsManifest`
- `RestV10ProjectsProjectIdBidPackagesPostResponse201BusinessClassificationsItem`
- `RestV10ProjectsProjectIdBidPackagesPostResponse201CreatedBy`
- `RestV10ProjectsProjectIdBidPackagesPostResponse201DistributionMembersItem`
- `RestV10ProjectsProjectIdBidPackagesPostResponse201Links`
- `RestV10ProjectsProjectIdBidPackagesPostResponse201Manager`
- `RestV10ProjectsProjectIdBidPackagesPostResponse201ManagerVendor`
- `RestV10ProjectsProjectIdBidPackagesPostResponse201NdaAttachmentsItem`
- `RestV10ProjectsProjectIdBidPackagesPostResponse201PointOfContact`
- `RestV10ProjectsProjectIdBidPackagesPostResponse201TradesAndServicesItem`

## RestV10ProjectsProjectIdBidPackagesPostResponse201BidDocsManifest
- Role: nested
- Parent: RestV10ProjectsProjectIdBidPackagesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdBidPackagesPostResponse201BidDocsManifest
- Schema ID: schema:anon/eab5040c5461d4fbd677f2238aaa62e282c469f6
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `streaming_url` | `string` |

## RestV10ProjectsProjectIdBidPackagesPostResponse201BusinessClassificationsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdBidPackagesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdBidPackagesPostResponse201BusinessClassificationsItem
- Schema ID: schema:anon/8363570528ebf5461d0e7e76ed6ef48734d978df

### Fields

| Field | Type |
|------|------|
| `classification_name` | `string` |
| `classification_abbreviation` | `string` |
| `classification_key` | `string` |

## RestV10ProjectsProjectIdBidPackagesPostResponse201CreatedBy
- Role: nested
- Parent: RestV10ProjectsProjectIdBidPackagesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdBidPackagesPostResponse201CreatedBy
- Schema ID: schema:anon/24c4856dc8a5de80c5d45a10e67bac063f7aeeaf

### Fields

| Field | Type |
|------|------|
| `email` | `string` |
| `first` | `string` |
| `last` | `string` |
| `numbers` | `string` |

## RestV10ProjectsProjectIdBidPackagesPostResponse201DistributionMembersItem
- Role: nested
- Parent: RestV10ProjectsProjectIdBidPackagesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdBidPackagesPostResponse201DistributionMembersItem
- Schema ID: schema:anon/80d12b88805355bab01b54822850ccc9d9c6a396

### Fields

| Field | Type |
|------|------|
| `email` | `string` |
| `first` | `string` |
| `last` | `string` |
| `numbers` | `string` |

## RestV10ProjectsProjectIdBidPackagesPostResponse201Links
- Role: nested
- Parent: RestV10ProjectsProjectIdBidPackagesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdBidPackagesPostResponse201Links
- Schema ID: schema:anon/1028cc0ee682db4e6ab1efe97064325482db8408

### Fields

| Field | Type |
|------|------|
| `add_vendor` | `string` |
| `analyticsEventsPath` | `string` |
| `attach_documents` | `string` |
| `bid_list` | `string` |
| `bid_packages` | `string` |
| `bid_packages_by_project` | `string` |
| `bulk_create_bids` | `string` |
| `cost_codes` | `string` |
| `overview` | `string` |
| `permission_templates` | `string` |
| `submit` | `string` |
| `trades` | `string` |
| `vendors` | `string` |

## RestV10ProjectsProjectIdBidPackagesPostResponse201Manager
- Role: nested
- Parent: RestV10ProjectsProjectIdBidPackagesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdBidPackagesPostResponse201Manager
- Schema ID: schema:anon/404e1304773aa8320b46e9185116c8c320f631c1
- Primary Key: LoginInformationId

### Fields

| Field | Type |
|------|------|
| `login_information_id` | `int` |
| `contact_id` | `int` |
| `name` | `string` |
| `email` | `string` |
| `job_title` | `string` |
| `invited` | `bool` |
| `vendor` | `RestV10ProjectsProjectIdBidPackagesPostResponse201ManagerVendor` |

## RestV10ProjectsProjectIdBidPackagesPostResponse201ManagerVendor
- Role: nested
- Parent: RestV10ProjectsProjectIdBidPackagesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdBidPackagesPostResponse201ManagerVendor
- Schema ID: schema:anon/ce046f07b431eac5de4098de031cfb521bf929ad
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |

## RestV10ProjectsProjectIdBidPackagesPostResponse201NdaAttachmentsItem
- Role: nested
- Parent: RestV10ProjectsProjectIdBidPackagesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdBidPackagesPostResponse201NdaAttachmentsItem
- Schema ID: schema:anon/6e09d785772aebdd628b61f526ab9d7479fdf332
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `item_type` | `string` |
| `item_id` | `string` |
| `prostore_file_id` | `string` |
| `url` | `string` |
| `name` | `string` |

## RestV10ProjectsProjectIdBidPackagesPostResponse201PointOfContact
- Role: nested
- Parent: RestV10ProjectsProjectIdBidPackagesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdBidPackagesPostResponse201PointOfContact
- Schema ID: schema:anon/22df0f599676e51004f1a54d11abeeb11d13753d

### Fields

| Field | Type |
|------|------|
| `email` | `string` |
| `first` | `string` |
| `last` | `string` |
| `numbers` | `string` |

## RestV10ProjectsProjectIdBidPackagesPostResponse201TradesAndServicesItem
- Role: nested
- Parent: RestV10ProjectsProjectIdBidPackagesPostResponse201DataObject
- Schema Name: RestV10ProjectsProjectIdBidPackagesPostResponse201TradesAndServicesItem
- Schema ID: schema:anon/908cc474732319823301c4c884fe107b5365b5e9

### Fields

| Field | Type |
|------|------|
| `trade_level` | `string` |
| `trade_path` | `string` |
| `trade_key` | `string` |
