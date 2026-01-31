# SignatureTypeFullDataObject

## SignatureTypeFullDataObject
- Role: parent
- Schema Name: SignatureTypeFull
- Schema ID: schema:definitions/SignatureTypeFull
- Primary Key: Id

### Fields
- `id`: `string`
- `backend_code`: `BackendCodeEnum`
- `display_in_ui`: `bool`
- `title`: `string`
- `localized_title`: `LocalizedString[]`
- `description`: `string`
- `localized_description`: `LocalizedString[]`
- `default_sms_notification`: `SmsNotificationSettings`
- `two_factor_auth_settings`: `2FASettings`
- `include_signer_link`: `bool`
- `storage_profile`: `StorageProfileEnum`
- `signer_can_reject`: `bool`
- `delegation`: `bool`
- `template_id`: `string`
- `external_authentication`: `bool`
- `docusign_settings`: `DocusignSettings`
- `docusign_provider`: `string`
- `docusign_protect_and_sign_settings`: `DocusignProtectAndSignSettings`
- `display_terms_on_signature_portal`: `bool`
- `updated_at`: `string`
