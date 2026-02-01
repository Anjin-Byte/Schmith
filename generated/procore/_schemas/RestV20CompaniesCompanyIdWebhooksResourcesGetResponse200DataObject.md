# RestV20CompaniesCompanyIdWebhooksResourcesGetResponse200DataObject

## RestV20CompaniesCompanyIdWebhooksResourcesGetResponse200DataObject
- Role: parent
- Schema Name: RestV20CompaniesCompanyIdWebhooksResourcesGetResponse200
- Schema ID: schema:anon/51ca281c3de079201710058e9abfa180780be053

### Fields

| Field | Type |
|------|------|
| `data` | `RestV20CompaniesCompanyIdWebhooksResourcesGetResponse200DataItem[]` |

### Nested Types
- `RestV20CompaniesCompanyIdWebhooksResourcesGetResponse200DataItem`
- `RestV20CompaniesCompanyIdWebhooksResourcesGetResponse200DataItemPayloadVersion`

## RestV20CompaniesCompanyIdWebhooksResourcesGetResponse200DataItem
- Role: nested
- Parent: RestV20CompaniesCompanyIdWebhooksResourcesGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWebhooksResourcesGetResponse200DataItem
- Schema ID: schema:anon/203f136d40529adf7fb24863bb98306096fba769

### Fields

| Field | Type |
|------|------|
| `category` | `string` |
| `tool` | `string` |
| `name` | `string` |
| `payload_version` | `RestV20CompaniesCompanyIdWebhooksResourcesGetResponse200DataItemPayloadVersion` |
| `actions` | `string[]` |

## RestV20CompaniesCompanyIdWebhooksResourcesGetResponse200DataItemPayloadVersion
- Role: nested
- Parent: RestV20CompaniesCompanyIdWebhooksResourcesGetResponse200DataObject
- Schema Name: RestV20CompaniesCompanyIdWebhooksResourcesGetResponse200DataItemPayloadVersion
- Schema ID: schema:anon/48dfb2e4001e00f48ac87079cc1dfc3952870b85

### Enum

Values: v4.0, v3.0, v2.0
