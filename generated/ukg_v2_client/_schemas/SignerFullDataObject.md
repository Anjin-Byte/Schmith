# SignerFullDataObject

## SignerFullDataObject
- Role: parent
- Schema Name: SignerFull
- Schema ID: schema:definitions/SignerFull
- Primary Key: FirstName

### Fields

| Field | Type |
|------|------|
| `type` | `TypeEnum` |
| `signature_positions` | `SignaturePosition[]` |
| `user_id` | `string` |
| `employee_id` | `string` |
| `first_name` | `string` |
| `last_name` | `string` |
| `language` | `string` |
| `email_address` | `string` |
| `mobile_phone_number` | `string` |
| `signature_process_id` | `string` |
| `signing_order` | `int` |
| `access_code` | `string` |
| `sms_notification` | `bool` |
| `two_factor_auth` | `TwoFactorAuthenticationMethod` |
| `message` | `string` |
| `send_signed_document` | `bool` |
| `signing_url` | `string` |
| `id` | `string` |
| `signed_at` | `string` |
| `state` | `SignerState` |
