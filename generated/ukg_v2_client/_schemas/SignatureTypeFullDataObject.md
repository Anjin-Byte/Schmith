# SignatureTypeFullDataObject

## SignatureTypeFullDataObject
- Role: parent
- Schema Name: SignatureTypeFull
- Schema ID: schema:definitions/SignatureTypeFull
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `backend_code` | `SignatureTypePayloadBackendCode` |
| `display_in_ui` | `bool` |
| `title` | `string` |
| `localized_title` | `LocalizedString[]` |
| `description` | `string` |
| `localized_description` | `LocalizedString[]` |
| `default_sms_notification` | `SmsNotificationSettings` |
| `two_factor_auth_settings` | `2FASettings` |
| `include_signer_link` | `bool` |
| `storage_profile` | `SignatureTypePayloadStorageProfile` |
| `signer_can_reject` | `bool` |
| `delegation` | `bool` |
| `template_id` | `string` |
| `external_authentication` | `bool` |
| `docusign_settings` | `DocusignSettings` |
| `docusign_provider` | `string` |
| `docusign_protect_and_sign_settings` | `DocusignProtectAndSignSettings` |
| `display_terms_on_signature_portal` | `bool` |
| `updated_at` | `string` |

### Nested Types
- `2FASettings`
- `2FASettingsMode`
- `DocusignProtectAndSignSettings`
- `DocusignSettings`
- `LocalizedString`
- `SignatureTypePayloadBackendCode`
- `SignatureTypePayloadStorageProfile`
- `SmsNotificationSettings`

## 2FASettings
- Role: nested
- Parent: SignatureTypeFullDataObject
- Schema Name: 2FASettings
- Schema ID: schema:definitions/2FASettings

### Fields

| Field | Type |
|------|------|
| `mode` | `2FASettingsMode` |
| `value_user` | `bool` |
| `value_employee` | `bool` |
| `value_guest` | `bool` |

## 2FASettingsMode
- Role: nested
- Parent: SignatureTypeFullDataObject
- Schema Name: 2FASettingsMode
- Schema ID: schema:anon/9970d86896c3c76fd11109bdecf721d29e51eb6d

### Enum

Values: sms, email

## DocusignProtectAndSignSettings
- Role: nested
- Parent: SignatureTypeFullDataObject
- Schema Name: DocusignProtectAndSignSettings
- Schema ID: schema:definitions/DocusignProtectAndSignSettings
- Primary Key: AppId

### Fields

| Field | Type |
|------|------|
| `app_id` | `string` |
| `server_id` | `string` |
| `spare_id` | `string` |

## DocusignSettings
- Role: nested
- Parent: SignatureTypeFullDataObject
- Schema Name: DocusignSettings
- Schema ID: schema:definitions/DocusignSettings
- Primary Key: AccountId

### Fields

| Field | Type |
|------|------|
| `root_url` | `string` |
| `username` | `string` |
| `password` | `string` |
| `integrator_key` | `string` |
| `account_id` | `string` |

## LocalizedString
- Role: nested
- Parent: SignatureTypeFullDataObject
- Schema Name: LocalizedString
- Schema ID: schema:definitions/LocalizedString

### Fields

| Field | Type |
|------|------|
| `language_code` | `string` |
| `value` | `string` |

## SignatureTypePayloadBackendCode
- Role: nested
- Parent: SignatureTypeFullDataObject
- Schema Name: SignatureTypePayloadBackendCode
- Schema ID: schema:anon/60af20961278fb80f49cbabf38e72e6deeba3c2e

### Enum

Values: docusign, docusign_protect_and_sign, adobesign

## SignatureTypePayloadStorageProfile
- Role: nested
- Parent: SignatureTypeFullDataObject
- Schema Name: SignatureTypePayloadStorageProfile
- Schema ID: schema:anon/01a117cfabdc02f2bbcd3fd98cb4aba6f40887c6

### Enum

Values: peopledoc-sae, fr-cdc

## SmsNotificationSettings
- Role: nested
- Parent: SignatureTypeFullDataObject
- Schema Name: SmsNotificationSettings
- Schema ID: schema:definitions/SmsNotificationSettings

### Fields

| Field | Type |
|------|------|
| `user` | `bool` |
| `employee` | `bool` |
| `guest` | `bool` |
