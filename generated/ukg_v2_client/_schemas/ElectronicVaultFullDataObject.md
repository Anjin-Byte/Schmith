# ElectronicVaultFullDataObject

## ElectronicVaultFullDataObject
- Role: parent
- Schema Name: ElectronicVaultFull
- Schema ID: schema:definitions/ElectronicVaultFull
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `electronic_vault_subscription_enabled` | `bool` |
| `paper_documents_distribution_enabled` | `bool` |
| `electronic_documents_distribution_enabled` | `bool` |
| `electronic_payslips_opted_out` | `bool` |
| `id` | `string` |
| `electronic_vault_id` | `string` |
| `electronic_vault_state` | `ElectronicVaultOptionsComputedFieldsElectronicVaultState` |
| `electronic_payslips_choice_updated_at` | `string` |
| `electronic_payslips_choice_origin` | `ElectronicVaultOptionsComputedFieldsElectronicPayslipsChoiceOrigin` |

### Nested Types
- `ElectronicVaultOptionsComputedFieldsElectronicPayslipsChoiceOrigin`
- `ElectronicVaultOptionsComputedFieldsElectronicVaultState`

## ElectronicVaultOptionsComputedFieldsElectronicPayslipsChoiceOrigin
- Role: nested
- Parent: ElectronicVaultFullDataObject
- Schema Name: ElectronicVaultOptionsComputedFieldsElectronicPayslipsChoiceOrigin
- Schema ID: schema:anon/855aaad6f78bb50aea3213fc3b97f2db52cebbdc

### Enum

Values: mypeopledoc, peopledoc

## ElectronicVaultOptionsComputedFieldsElectronicVaultState
- Role: nested
- Parent: ElectronicVaultFullDataObject
- Schema Name: ElectronicVaultOptionsComputedFieldsElectronicVaultState
- Schema ID: schema:anon/248fbeab8e9d9f6c8f5d218cec765ac4d5d495e5

### Enum

Values: activated, not_activated, not_available, pending_deletion, deleted
