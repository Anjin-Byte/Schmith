# SignerFullDataObject

## SignerFullDataObject
- Role: parent
- Schema Name: SignerFull
- Schema ID: schema:definitions/SignerFull
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `type` | `SignerBaseType` |
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

### Nested Types
- `SignaturePosition`
- `SignaturePositionUnit`
- `SignerBaseType`
- `SignerState`
- `TwoFactorAuthenticationMethod`

## SignaturePosition
- Role: nested
- Parent: SignerFullDataObject
- Schema Name: SignaturePosition
- Schema ID: schema:definitions/SignaturePosition

### Fields

| Field | Type |
|------|------|
| `page` | `int` |
| `unit` | `SignaturePositionUnit` |
| `x` | `double` |
| `y` | `double` |
| `width` | `double` |
| `height` | `double` |

## SignaturePositionUnit
- Role: nested
- Parent: SignerFullDataObject
- Schema Name: SignaturePositionUnit
- Schema ID: schema:anon/27002a2e7ea816d4d0cae24173ff27461c6937e0

### Enum

Values: cm, inch, pt

## SignerBaseType
- Role: nested
- Parent: SignerFullDataObject
- Schema Name: SignerBaseType
- Schema ID: schema:anon/2b360fd31e8c89122e3db638daa1ac4b28b81830

### Enum

Values: organization, user, employee, external

## SignerState
- Role: nested
- Parent: SignerFullDataObject
- Schema Name: SignerState
- Schema ID: schema:definitions/SignerState

### Enum

Values: pending, in_progress, signed, rejected, error, done, delivered, delayed

## TwoFactorAuthenticationMethod
- Role: nested
- Parent: SignerFullDataObject
- Schema Name: TwoFactorAuthenticationMethod
- Schema ID: schema:definitions/TwoFactorAuthenticationMethod

### Fields

| Field | Type |
|------|------|
| `sms` | `bool` |
| `email` | `bool` |
