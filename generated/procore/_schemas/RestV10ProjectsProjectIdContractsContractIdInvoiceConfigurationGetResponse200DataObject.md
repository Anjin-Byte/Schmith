# RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGetResponse200DataObject

## RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGetResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGetResponse200
- Schema ID: schema:anon/815961355fe740efbc2e05efd31ca1502c569fa9
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `separate_billing_for_stored_materials` | `bool` |
| `stored_materials_billing_method` | `string` |
| `contract_id` | `int` |
| `project_id` | `int` |
| `company_id` | `int` |
| `ssr_enabled` | `bool` |
| `move_materials_to_previous_work_completed` | `bool` |
| `retainage_rule_set` | `RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGetResponse200RetainageRuleSet` |

### Nested Types
- `RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGetResponse200RetainageRuleSet`
- `RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGetResponse200RetainageRuleSetRetainageRulesItem`

## RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGetResponse200RetainageRuleSet
- Role: nested
- Parent: RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGetResponse200RetainageRuleSet
- Schema ID: schema:anon/1f225e1c15373700e6c5e1c51b8bf081a1a21d4a
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `contract_id` | `int` |
| `name` | `string` |
| `retainage_rules` | `RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGetResponse200RetainageRuleSetRetainageRulesItem[]` |

## RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGetResponse200RetainageRuleSetRetainageRulesItem
- Role: nested
- Parent: RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGetResponse200RetainageRuleSetRetainageRulesItem
- Schema ID: schema:anon/ef51c7fb2da683aa7373426b690986fe5ef01101

### Fields
