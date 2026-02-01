# RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataObject

## RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200
- Schema ID: schema:anon/8997f7b468d57ba64b9a108904b6a7444d5158be

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItem`
- `RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItemDeliveryAttemptsItem`
- `RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItemPayload`
- `RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItemPayloadEventType`
- `RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItemPayloadMetadata`
- `RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItemStatus`

## RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItem
- Schema ID: schema:anon/916bfb1523e59dee35b44c24b23ac638b2f6a143
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `status` | `RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItemStatus` |
| `payload` | `RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItemPayload` |
| `delivery_attempts` | `RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItemDeliveryAttemptsItem[]` |

## RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItemDeliveryAttemptsItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItemDeliveryAttemptsItem
- Schema ID: schema:anon/e9a7c0fea2589b8231d13d56450e71c3a1fad8c8
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `success` | `bool` |
| `response_status` | `int` |
| `response_body` | `string` |
| `response_headers` | `object` |
| `started_at` | `string` |
| `completed_at` | `string` |

## RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItemPayload
- Role: nested
- Parent: RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItemPayload
- Schema ID: schema:anon/7280ad1050778023d0dc4c4092f335ace34fd787
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `ulid` | `string` |
| `timestamp` | `string` |
| `metadata` | `RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItemPayloadMetadata` |
| `user_id` | `int` |
| `company_id` | `int` |
| `project_id` | `int` |
| `api_version` | `string` |
| `event_type` | `RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItemPayloadEventType` |
| `resource_name` | `string` |
| `resource_id` | `int` |

## RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItemPayloadEventType
- Role: nested
- Parent: RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItemPayloadEventType
- Schema ID: schema:anon/82c585975a4c85204eed3cc489eff22c21a55bcd

### Enum

Values: create, update, delete

## RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItemPayloadMetadata
- Role: nested
- Parent: RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItemPayloadMetadata
- Schema ID: schema:anon/6fab9bd338076fd6e11fe3b7400920f019a474d5
- Primary Key: SourceUserId

### Fields

| Field | Type |
|------|------|
| `source_user_id` | `int` |
| `source_company_id` | `int` |
| `source_project_id` | `int` |
| `source_application_id` | `string` |
| `source_operation_id` | `string` |

## RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItemStatus
- Role: nested
- Parent: RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWebhooksHooksHookIdDeliveriesGetResponse200DataItemStatus
- Schema ID: schema:anon/f951dea8b3e124df12ae30369379a75a044b13d0

### Enum

Values: delivered, failed, discarded, enqueued, retrying
