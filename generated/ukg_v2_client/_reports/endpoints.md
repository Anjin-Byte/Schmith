# Endpoint Response Coverage: ukg_v2_client

## Summary

| Metric | Count |
|--------|-------|
| Total endpoints | 333 |
| Total response schemas | 147 |
| Mapped response schemas | 48 |
| Unmapped response schemas | 99 |

## Endpoint Responses

| Method | Path | Response Schema | DataObject | Mapping |
|--------|------|-----------------|-----------|---------|
| `GET` | `/custom_fields` | `schema:anon/ef8a93997d834fc0787d5023a82362d99e83839f` | `` | `missing` |
| `GET` | `/custom_fields/{id}` | `schema:definitions/CustomFieldFull` | `CustomFieldFullDataObject` | `root` |
| `PUT` | `/custom_fields/{id}` | `schema:definitions/CustomFieldFull` | `CustomFieldFullDataObject` | `root` |
| `PUT` | `/custom_fields/{id}` | `schema:definitions/CustomFieldFull` | `CustomFieldFullDataObject` | `root` |
| `PUT` | `/custom_fields/{id}` | `schema:definitions/Error` | `` | `missing` |
| `PUT` | `/custom_fields/{id}` | `schema:definitions/CustomFieldFull` | `CustomFieldFullDataObject` | `root` |
| `PATCH` | `/custom_fields/{id}` | `schema:definitions/CustomFieldFull` | `CustomFieldFullDataObject` | `root` |
| `PATCH` | `/custom_fields/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/custom_fields/{id}` | `schema:definitions/Error` | `` | `missing` |
| `PATCH` | `/custom_fields/{id}` | `schema:definitions/CustomFieldFull` | `CustomFieldFullDataObject` | `root` |
| `PUT` | `/employees/{id}` | `schema:definitions/EmployeeFull` | `EmployeeFull` | `nested_only` |
| `PUT` | `/employees/{id}` | `schema:definitions/EmployeeFull` | `EmployeeFull` | `nested_only` |
| `PUT` | `/employees/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/employees/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/employees/{id}` | `schema:definitions/Error` | `` | `missing` |
| `PATCH` | `/employees/{id}` | `schema:definitions/EmployeeFull` | `EmployeeFull` | `nested_only` |
| `PATCH` | `/employees/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/employees/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/employees/{id}` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/employees/{id}` | `schema:definitions/EmployeeFull` | `EmployeeFull` | `nested_only` |
| `GET` | `/employees/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/employees` | `schema:anon/3043869d9d959dbd70c0572f1c48f37687317660` | `` | `missing` |
| `GET` | `/employees` | `schema:definitions/Error` | `` | `missing` |
| `POST` | `/employees` | `schema:anon/3043869d9d959dbd70c0572f1c48f37687317660` | `` | `missing` |
| `POST` | `/employees` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/employees` | `schema:definitions/Error` | `` | `missing` |
| `PATCH` | `/employees/bulk` | `schema:definitions/EmployeeBulkOperationResult` | `EmployeeBulkOperationResultDataObject` | `root` |
| `PATCH` | `/employees/bulk` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/employees/bulk` | `schema:definitions/EmployeeBulkOperationResult` | `EmployeeBulkOperationResultDataObject` | `root` |
| `PUT` | `/employees/bulk` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/employees/bulk` | `schema:definitions/EmployeeBulkOperationResult` | `EmployeeBulkOperationResultDataObject` | `root` |
| `POST` | `/employees/bulk` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/employees/bulk/{request_id}` | `schema:definitions/EmployeeBulkOperationStatus` | `EmployeeBulkOperationStatusDataObject` | `root` |
| `GET` | `/employees/bulk/{request_id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/employees/{id}/electronic_vault_invite` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/employees/{id}/electronic_vault_invite` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/employees/{id}/portal_invite` | `schema:definitions/Error` | `` | `missing` |
| `POST` | `/employees/{id}/portal_invite` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `DELETE` | `/employees/{id}/electronic_vault_link` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `DELETE` | `/employees/{id}/electronic_vault_link` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/employees/by_external_id/{external_id}` | `schema:definitions/EmployeeFull` | `EmployeeFull` | `nested_only` |
| `PUT` | `/employees/by_external_id/{external_id}` | `schema:definitions/EmployeeFull` | `EmployeeFull` | `nested_only` |
| `PUT` | `/employees/by_external_id/{external_id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/employees/by_external_id/{external_id}` | `schema:definitions/Error` | `` | `missing` |
| `POST` | `/employees/{id}/electronic_vault_documents` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/employees/{id}/electronic_vault_documents` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/employee_subscriptions` | `schema:anon/aa0cfc068e025c28d6d580b4397375e997e965bd` | `` | `missing` |
| `GET` | `/employee_subscriptions/{id}` | `schema:definitions/EmployeeSubscriptionFull` | `` | `missing` |
| `GET` | `/electronic_vault_options` | `schema:anon/c194bdf2ca6aa88d63a9f86b63ae43f3e0ad2674` | `` | `missing` |
| `PATCH` | `/electronic_vault_options/{id}` | `schema:definitions/ElectronicVaultFull` | `ElectronicVaultFullDataObject` | `root` |
| `PATCH` | `/electronic_vault_options/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/electronic_vault_options/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/electronic_vault_options/{id}` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/electronic_vault_options/{id}` | `schema:definitions/ElectronicVaultFull` | `ElectronicVaultFullDataObject` | `root` |
| `GET` | `/electronic_vault_options/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/roles` | `schema:anon/713127302efd3e065589fb6ffc2c924ea6dfa3d8` | `` | `missing` |
| `PUT` | `/roles/{id}` | `schema:definitions/RoleFull` | `RoleFullDataObject` | `root` |
| `PUT` | `/roles/{id}` | `schema:definitions/RoleFull` | `RoleFullDataObject` | `root` |
| `PUT` | `/roles/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/roles/{id}` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/roles/{id}` | `schema:definitions/RoleFull` | `RoleFullDataObject` | `root` |
| `GET` | `/roles/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/roles/{role_id}/permissions/core` | `schema:definitions/CorePermissionsGet` | `CorePermissionsGetDataObject` | `root` |
| `PUT` | `/roles/{role_id}/permissions/core` | `schema:definitions/CorePermissionsFull` | `CorePermissionsFullDataObject` | `root` |
| `PUT` | `/roles/{role_id}/permissions/core` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/roles/{role_id}/permissions/efm` | `schema:definitions/EFMPermissionsFull` | `EFMPermissionsFullDataObject` | `root` |
| `GET` | `/users` | `schema:anon/c8499daacd0b84ab9982b5a6f1c38a7171d8f366` | `` | `missing` |
| `GET` | `/users` | `schema:definitions/Error` | `` | `missing` |
| `POST` | `/users` | `schema:definitions/UserFull` | `UserFullDataObject` | `root` |
| `POST` | `/users` | `schema:definitions/Error` | `` | `missing` |
| `HEAD` | `/users` | `schema:definitions/Error` | `` | `missing` |
| `PUT` | `/users/{id}` | `schema:definitions/UserFull` | `UserFullDataObject` | `root` |
| `PUT` | `/users/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/users/{id}` | `schema:definitions/Error` | `` | `missing` |
| `PUT` | `/users/{id}` | `schema:definitions/RateLimitErrors` | `` | `missing` |
| `PATCH` | `/users/{id}` | `schema:definitions/UserFull` | `UserFullDataObject` | `root` |
| `PATCH` | `/users/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/users/{id}` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/users/{id}` | `schema:definitions/UserFull` | `UserFullDataObject` | `root` |
| `POST` | `/users/bulk` | `schema:definitions/UserBulkOperationResult` | `UserBulkOperationResultDataObject` | `root` |
| `POST` | `/users/bulk` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/users/bulk` | `schema:definitions/UserBulkOperationResult` | `UserBulkOperationResultDataObject` | `root` |
| `PUT` | `/users/bulk` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/users/bulk` | `schema:definitions/UserBulkOperationResult` | `UserBulkOperationResultDataObject` | `root` |
| `PATCH` | `/users/bulk` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/users/bulk/{request_id}` | `schema:definitions/UserBulkOperationStatus` | `UserBulkOperationStatusDataObject` | `root` |
| `GET` | `/users/bulk/{request_id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/users/{id}/invite` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/users/{id}/invite` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/employee_document_types` | `schema:anon/aa296d5d3ced8247f5b49d4c0ca0bc5840c26f62` | `` | `missing` |
| `PUT` | `/employee_document_types/{id}` | `schema:definitions/EmployeeDocumentTypeFull` | `` | `missing` |
| `PUT` | `/employee_document_types/{id}` | `schema:definitions/EmployeeDocumentTypeFull` | `` | `missing` |
| `PUT` | `/employee_document_types/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/employee_document_types/{id}` | `schema:definitions/Error` | `` | `missing` |
| `PATCH` | `/employee_document_types/{id}` | `schema:definitions/EmployeeDocumentTypeFull` | `` | `missing` |
| `PATCH` | `/employee_document_types/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/employee_document_types/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/employee_document_types/{id}` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/employee_document_types/{id}` | `schema:definitions/EmployeeDocumentTypeFull` | `` | `missing` |
| `GET` | `/employee_document_types/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/company_document_types` | `schema:anon/784c9c2066d6295cc3b049eacb69d4815eea3400` | `` | `missing` |
| `PUT` | `/company_document_types/{id}` | `schema:definitions/CompanyDocumentTypeFull` | `` | `missing` |
| `PUT` | `/company_document_types/{id}` | `schema:definitions/CompanyDocumentTypeFull` | `` | `missing` |
| `PUT` | `/company_document_types/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/company_document_types/{id}` | `schema:definitions/Error` | `` | `missing` |
| `PATCH` | `/company_document_types/{id}` | `schema:definitions/CompanyDocumentTypeFull` | `` | `missing` |
| `PATCH` | `/company_document_types/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/company_document_types/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/company_document_types/{id}` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/company_document_types/{id}` | `schema:definitions/CompanyDocumentTypeFull` | `` | `missing` |
| `GET` | `/company_document_types/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/employee_folders` | `schema:anon/a6dc079ddf9eff65144267392e407e1f5ead40cc` | `` | `missing` |
| `GET` | `/employee_folders/{id}` | `schema:anon/a6dc079ddf9eff65144267392e407e1f5ead40cc` | `` | `missing` |
| `GET` | `/company_folders` | `schema:anon/a6dc079ddf9eff65144267392e407e1f5ead40cc` | `` | `missing` |
| `GET` | `/company_folders/{id}` | `schema:anon/a6dc079ddf9eff65144267392e407e1f5ead40cc` | `` | `missing` |
| `GET` | `/organizations` | `schema:anon/c33cf55f8516018dfec2345eadb6c3b8a504c947` | `` | `missing` |
| `GET` | `/organizations` | `schema:definitions/Error` | `` | `missing` |
| `HEAD` | `/organizations` | `schema:definitions/Error` | `` | `missing` |
| `PUT` | `/organizations/{id}` | `schema:definitions/OrganizationFull` | `` | `missing` |
| `PUT` | `/organizations/{id}` | `schema:definitions/OrganizationFull` | `` | `missing` |
| `PUT` | `/organizations/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/organizations/{id}` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/organizations/{id}` | `schema:definitions/OrganizationFull` | `` | `missing` |
| `GET` | `/organizations/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/organizations/{id}` | `schema:definitions/OrganizationFull` | `` | `missing` |
| `PATCH` | `/organizations/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/organizations/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/organizations/{id}` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/organization_groups` | `schema:anon/d66080a6d8906ee35e18b5732d6197fe03d5a6ef` | `` | `missing` |
| `GET` | `/organization_groups` | `schema:definitions/Error` | `` | `missing` |
| `PUT` | `/organization_groups/{id}` | `schema:definitions/OrganizationGroupFull` | `` | `missing` |
| `PUT` | `/organization_groups/{id}` | `schema:definitions/OrganizationGroupFull` | `` | `missing` |
| `PUT` | `/organization_groups/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/organization_groups/{id}` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/organization_groups/{id}` | `schema:definitions/OrganizationGroupFull` | `` | `missing` |
| `GET` | `/organization_groups/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/organization_groups/{id}` | `schema:definitions/OrganizationGroupFull` | `` | `missing` |
| `PATCH` | `/organization_groups/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/organization_groups/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/organization_groups/{id}` | `schema:definitions/Error` | `` | `missing` |
| `POST` | `/document` | `schema:definitions/DocumentFileId` | `DocumentFileId` | `nested_only` |
| `POST` | `/document` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/redirection_urls` | `schema:definitions/RedirectionUrls` | `RedirectionUrlsDataObject` | `root` |
| `GET` | `/employee_documents` | `schema:anon/b0c37f04150f97e8cac6df1a54929b8a5cfb8bd0` | `` | `missing` |
| `POST` | `/employee_documents` | `schema:definitions/EmployeeDocumentFull` | `EmployeeDocumentFullDataObject` | `root` |
| `POST` | `/employee_documents` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/employee_documents` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/employee_documents` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/employee_documents/{id}/file` | `schema:anon/4ef0966440754d94ecce66468691d81fe9b2a120` | `` | `missing` |
| `GET` | `/employee_documents/{id}/file` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/employee_documents/{id}/duplicate` | `schema:anon/510932133ea32afb1165548fc5d46b15720f18ef` | `` | `missing` |
| `GET` | `/employee_documents/{id}/duplicate` | `schema:anon/510932133ea32afb1165548fc5d46b15720f18ef` | `` | `missing` |
| `GET` | `/employee_documents/{id}/duplicate` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/employee_documents/{id}/duplicate` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/employee_documents/{id}/duplicate` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/employee_documents/{id}/duplicate` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/employee_documents/{id}/preview` | `schema:anon/f467c82983edfab75b39cfdd081102de6b3498b9` | `` | `missing` |
| `GET` | `/employee_documents/{id}/preview` | `schema:anon/f467c82983edfab75b39cfdd081102de6b3498b9` | `` | `missing` |
| `GET` | `/employee_documents/{id}/preview` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/employee_documents/{id}/preview` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/employee_documents/{id}/preview` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/employee_documents/{id}/preview` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/employee_documents/{id}/receipt` | `schema:anon/25ce8149912273a869f2c4e931666e01bdb86bbf` | `` | `missing` |
| `GET` | `/employee_documents/{id}/receipt` | `schema:anon/25ce8149912273a869f2c4e931666e01bdb86bbf` | `` | `missing` |
| `GET` | `/employee_documents/{id}/receipt` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/employee_documents/{id}/receipt` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/employee_documents/{id}/expiration/update` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/employee_documents/{id}` | `schema:definitions/EmployeeDocumentFull` | `EmployeeDocumentFullDataObject` | `root` |
| `GET` | `/employee_documents/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `DELETE` | `/employee_documents/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/employee_documents/{id}` | `schema:definitions/EmployeeDocumentFull` | `EmployeeDocumentFullDataObject` | `root` |
| `PUT` | `/employee_documents/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/employee_documents/{id}` | `schema:definitions/Error` | `` | `missing` |
| `PATCH` | `/employee_documents/{id}` | `schema:definitions/EmployeeDocumentFull` | `EmployeeDocumentFullDataObject` | `root` |
| `PATCH` | `/employee_documents/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/employee_documents/{id}` | `schema:definitions/Error` | `` | `missing` |
| `PUT` | `/employee_documents/{id}/trash` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/employee_documents/{id}/untrash` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/employee_documents/{id}/expire` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/employee_documents/search` | `schema:anon/b0c37f04150f97e8cac6df1a54929b8a5cfb8bd0` | `` | `missing` |
| `GET` | `/company_documents` | `schema:anon/c071e6cecd79b1e634f7dc4aafb3e664234a67e8` | `` | `missing` |
| `POST` | `/company_documents` | `schema:definitions/CompanyDocumentFull` | `CompanyDocumentFullDataObject` | `root` |
| `POST` | `/company_documents` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/company_documents` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/company_documents` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/company_documents/{id}` | `schema:definitions/CompanyDocumentFull` | `CompanyDocumentFullDataObject` | `root` |
| `GET` | `/company_documents/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `DELETE` | `/company_documents/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/company_documents/{id}` | `schema:definitions/CompanyDocumentFull` | `CompanyDocumentFullDataObject` | `root` |
| `PUT` | `/company_documents/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/company_documents/{id}` | `schema:definitions/Error` | `` | `missing` |
| `PATCH` | `/company_documents/{id}` | `schema:definitions/CompanyDocumentFull` | `CompanyDocumentFullDataObject` | `root` |
| `PATCH` | `/company_documents/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/company_documents/{id}` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/company_documents/{id}/file` | `schema:anon/4ef0966440754d94ecce66468691d81fe9b2a120` | `` | `missing` |
| `GET` | `/company_documents/{id}/file` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `HEAD` | `/company_documents/{id}/file` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/company_documents/{id}/duplicate` | `schema:anon/510932133ea32afb1165548fc5d46b15720f18ef` | `` | `missing` |
| `GET` | `/company_documents/{id}/duplicate` | `schema:anon/510932133ea32afb1165548fc5d46b15720f18ef` | `` | `missing` |
| `GET` | `/company_documents/{id}/duplicate` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/company_documents/{id}/duplicate` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/company_documents/{id}/duplicate` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/company_documents/{id}/duplicate` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/company_documents/{id}/preview` | `schema:anon/f467c82983edfab75b39cfdd081102de6b3498b9` | `` | `missing` |
| `GET` | `/company_documents/{id}/preview` | `schema:anon/f467c82983edfab75b39cfdd081102de6b3498b9` | `` | `missing` |
| `GET` | `/company_documents/{id}/preview` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/company_documents/{id}/preview` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/company_documents/{id}/preview` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/company_documents/{id}/preview` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/company_documents/{id}/receipt` | `schema:anon/25ce8149912273a869f2c4e931666e01bdb86bbf` | `` | `missing` |
| `GET` | `/company_documents/{id}/receipt` | `schema:anon/25ce8149912273a869f2c4e931666e01bdb86bbf` | `` | `missing` |
| `GET` | `/company_documents/{id}/receipt` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/company_documents/{id}/receipt` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/company_documents/{id}/trash` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/company_documents/{id}/untrash` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/company_documents/{id}/expire` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/uploads` | `schema:definitions/UploadDocument` | `` | `missing` |
| `POST` | `/uploads` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/uploads/{id}/text_occurrences` | `schema:anon/a7d973accdf4c2c2660945da290d177c9b727cd0` | `` | `missing` |
| `POST` | `/uploads/{id}/text_occurrences` | `schema:definitions/Error` | `` | `missing` |
| `POST` | `/uploads/{id}/text_occurrences` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/uploads/{id}/text_occurrences` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/signature_processes` | `schema:anon/574132e6e898a6dde6c146408dacf2510e9fe68f` | `` | `missing` |
| `POST` | `/signature_processes` | `schema:definitions/SignatureProcessFull` | `SignatureProcessFullDataObject` | `root` |
| `POST` | `/signature_processes` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/signature_processes` | `schema:definitions/Error` | `` | `missing` |
| `POST` | `/signature_processes/cancel` | `schema:anon/574132e6e898a6dde6c146408dacf2510e9fe68f` | `` | `missing` |
| `POST` | `/signature_processes/cancel` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/signature_processes/{id}` | `schema:definitions/SignatureProcessFull` | `SignatureProcessFullDataObject` | `root` |
| `PUT` | `/signature_processes/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/signature_processes/{id}` | `schema:definitions/Error` | `` | `missing` |
| `PATCH` | `/signature_processes/{id}` | `schema:definitions/SignatureProcessFull` | `SignatureProcessFullDataObject` | `root` |
| `PATCH` | `/signature_processes/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/signature_processes/{id}` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/signature_processes/{id}` | `schema:definitions/SignatureProcessFull` | `SignatureProcessFullDataObject` | `root` |
| `GET` | `/signature_processes/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `DELETE` | `/signature_processes/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `DELETE` | `/signature_processes/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/signature_processes/{id}/preview` | `schema:anon/4ef0966440754d94ecce66468691d81fe9b2a120` | `` | `missing` |
| `GET` | `/signature_processes/{id}/preview` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/signature_processes/{id}/file` | `schema:anon/4ef0966440754d94ecce66468691d81fe9b2a120` | `` | `missing` |
| `GET` | `/signature_processes/{id}/file` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/signature_processes/{id}/archive` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/signature_processes/{id}/archive` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/signature_processes/{id}/send` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/signature_processes/{id}/send` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/signature_types` | `schema:anon/dadb9bfad9410c9ba708c98acf88909c6e0730ab` | `` | `missing` |
| `GET` | `/signature_types/{id}` | `schema:definitions/SignatureTypeFull` | `SignatureTypeFullDataObject` | `root` |
| `GET` | `/signature_types/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/signers` | `schema:anon/bb4cf25bfe441228ba77915ab5cb2edad954dbd4` | `` | `missing` |
| `POST` | `/signers` | `schema:definitions/SignerFull` | `SignerFullDataObject` | `root` |
| `POST` | `/signers` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/signers` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/signers` | `schema:definitions/Error` | `` | `missing` |
| `POST` | `/signers/remind` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/signers/remind` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/signers/{id}` | `schema:definitions/SignerFull` | `SignerFullDataObject` | `root` |
| `GET` | `/signers/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `DELETE` | `/signers/{id}` | `schema:definitions/BaseError` | `` | `missing` |
| `PATCH` | `/signers/{id}` | `schema:definitions/SignerFull` | `SignerFullDataObject` | `root` |
| `PATCH` | `/signers/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/signers/{id}` | `schema:definitions/Error` | `` | `missing` |
| `PUT` | `/signers/{id}` | `schema:definitions/SignerFull` | `SignerFullDataObject` | `root` |
| `PUT` | `/signers/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/signers/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/signers/{id}` | `schema:definitions/Error` | `` | `missing` |
| `POST` | `/signers/{id}/remind` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/signers/{id}/remind` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/inbox_items` | `schema:anon/c6e719439cb16efc1d588734262fa68b3656ea68` | `` | `missing` |
| `POST` | `/inbox_items` | `schema:definitions/InboxItemFull` | `InboxItemFullDataObject` | `root` |
| `POST` | `/inbox_items` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/inbox_items` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/inbox_items/{id}` | `schema:definitions/InboxItemFull` | `InboxItemFullDataObject` | `root` |
| `GET` | `/inbox_items/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/imports` | `schema:definitions/ImportFull` | `ImportFullDataObject` | `root` |
| `POST` | `/imports` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/imports` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/imports` | `schema:anon/b20d699cf7b14746324dbd42bf959b87d0a930ec` | `` | `missing` |
| `GET` | `/imports/{id}` | `schema:definitions/ImportFull` | `ImportFullDataObject` | `root` |
| `GET` | `/imports/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/imports/{id}/source` | `schema:anon/f19a35a40a7859425a63281011673eb6c82b360f` | `` | `missing` |
| `GET` | `/imports/{id}/source` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/imports/{id}/report` | `schema:anon/f19a35a40a7859425a63281011673eb6c82b360f` | `` | `missing` |
| `GET` | `/imports/{id}/report` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/imports/{id}/report` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/imports/{id}/errors_report` | `schema:anon/f19a35a40a7859425a63281011673eb6c82b360f` | `` | `missing` |
| `GET` | `/imports/{id}/errors_report` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/imports/{id}/errors_report` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/dataset_imports` | `schema:definitions/DatasetImportFull` | `DatasetImportFullDataObject` | `root` |
| `POST` | `/dataset_imports` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/dataset_imports` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/dataset_imports` | `schema:anon/12e4c29a4d55d063dc86bebeaf38bf8fdab962e5` | `` | `missing` |
| `GET` | `/dataset_imports/{id}` | `schema:definitions/DatasetImportFull` | `DatasetImportFullDataObject` | `root` |
| `GET` | `/dataset_imports/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/dataset_imports/{id}/source` | `schema:anon/f19a35a40a7859425a63281011673eb6c82b360f` | `` | `missing` |
| `GET` | `/dataset_imports/{id}/source` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/dataset_imports/{id}/report` | `schema:anon/f19a35a40a7859425a63281011673eb6c82b360f` | `` | `missing` |
| `GET` | `/dataset_imports/{id}/report` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/processes` | `schema:definitions/ProcessFull` | `` | `missing` |
| `POST` | `/processes` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/processes` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/processes` | `schema:anon/4fda8799c92e57c81aff0b5fec0301de1a3a79c5` | `` | `missing` |
| `GET` | `/processes/{id}` | `schema:definitions/ProcessFull` | `` | `missing` |
| `GET` | `/processes/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `DELETE` | `/processes/{id}` | `schema:definitions/BaseError` | `` | `missing` |
| `PUT` | `/processes/{id}/publish` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/processes/{id}/post_process_action#shared_inboxes` | `schema:definitions/ProcessPostActionSharedPayload` | `` | `missing` |
| `POST` | `/processes/{id}/post_process_action#shared_inboxes` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/processes/{id}/post_process_action#shared_inboxes` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/processes/{id}/post_process_action#shared_inboxes` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/processes/{id}/post_process_action#shared_inboxes` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/processes/{id}/post_process_action#user_inboxes` | `schema:definitions/ProcessPostActionUserPayload` | `` | `missing` |
| `POST` | `/processes/{id}/post_process_action#user_inboxes` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/processes/{id}/post_process_action#user_inboxes` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/processes/{id}/post_process_action#user_inboxes` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/processes/{id}/post_process_action#user_inboxes` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/process_templates` | `schema:anon/810ccd9b714002635c36ac4a9a1b0991dc0fd449` | `` | `missing` |
| `GET` | `/process_templates/{id}` | `schema:definitions/ProcessTemplate` | `ProcessTemplateDataObject` | `root` |
| `GET` | `/process_templates/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/process_templates/{id}` | `schema:definitions/ProcessTemplate` | `ProcessTemplateDataObject` | `root` |
| `PUT` | `/process_templates/{id}` | `schema:definitions/ProcessTemplate` | `ProcessTemplateDataObject` | `root` |
| `PUT` | `/process_templates/{id}` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/process_templates/{process_template_id}/task_templates` | `schema:anon/49e966dbb2286958e7bd268f2b7f00e279570463` | `` | `missing` |
| `GET` | `/process_templates/{process_template_id}/task_templates` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/process_templates/{process_template_id}/task_templates/{id}#acknowledgment` | `schema:definitions/AcknowledgmentTaskTemplates` | `` | `missing` |
| `GET` | `/process_templates/{process_template_id}/task_templates/{id}#acknowledgment` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#acknowledgment` | `schema:definitions/AcknowledgmentTaskTemplates` | `` | `missing` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#acknowledgment` | `schema:definitions/AcknowledgmentTaskTemplates` | `` | `missing` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#acknowledgment` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#acknowledgment` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/process_templates/{process_template_id}/task_templates/{id}#basic` | `schema:definitions/BasicTaskTemplates` | `` | `missing` |
| `GET` | `/process_templates/{process_template_id}/task_templates/{id}#basic` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#basic` | `schema:definitions/BasicTaskTemplates` | `` | `missing` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#basic` | `schema:definitions/BasicTaskTemplates` | `` | `missing` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#basic` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#basic` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/process_templates/{process_template_id}/task_templates/{id}#fill_form` | `schema:definitions/FillFormTaskTemplates` | `` | `missing` |
| `GET` | `/process_templates/{process_template_id}/task_templates/{id}#fill_form` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#fill_form` | `schema:definitions/FillFormTaskTemplates` | `` | `missing` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#fill_form` | `schema:definitions/FillFormTaskTemplates` | `` | `missing` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#fill_form` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#fill_form` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/process_templates/{process_template_id}/task_templates/{id}#fill_pdf` | `schema:definitions/FillPdfTaskTemplates` | `` | `missing` |
| `GET` | `/process_templates/{process_template_id}/task_templates/{id}#fill_pdf` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#fill_pdf` | `schema:definitions/FillPdfTaskTemplates` | `` | `missing` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#fill_pdf` | `schema:definitions/FillPdfTaskTemplates` | `` | `missing` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#fill_pdf` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#fill_pdf` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/process_templates/{process_template_id}/task_templates/{id}#signature` | `schema:definitions/SignatureTaskTemplates` | `` | `missing` |
| `GET` | `/process_templates/{process_template_id}/task_templates/{id}#signature` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#signature` | `schema:definitions/SignatureTaskTemplates` | `` | `missing` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#signature` | `schema:definitions/SignatureTaskTemplates` | `` | `missing` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#signature` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#signature` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/process_templates/{process_template_id}/task_templates/{id}#validation` | `schema:definitions/ValidationTaskTemplates` | `` | `missing` |
| `GET` | `/process_templates/{process_template_id}/task_templates/{id}#validation` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#validation` | `schema:definitions/ValidationTaskTemplates` | `` | `missing` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#validation` | `schema:definitions/ValidationTaskTemplates` | `` | `missing` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#validation` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/process_templates/{process_template_id}/task_templates/{id}#validation` | `schema:definitions/Error` | `` | `missing` |
| `DELETE` | `/process_templates/{process_template_id}/task_templates/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `DELETE` | `/process_templates/{process_template_id}/task_templates/{id}` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/process_pdf_templates` | `schema:anon/0943141efa0200182a6c0bb0d6b9444b716abe26` | `` | `missing` |
| `GET` | `/process_pdf_templates/{id}` | `schema:definitions/PdfTemplateDetail` | `` | `missing` |
| `GET` | `/process_pdf_templates/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/process_pdf_templates/{id}` | `schema:definitions/PdfTemplateDetail` | `` | `missing` |
| `PUT` | `/process_pdf_templates/{id}` | `schema:definitions/PdfTemplateDetail` | `` | `missing` |
| `PUT` | `/process_pdf_templates/{id}` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/tasks` | `schema:anon/d14f6e39b9c2423c40bdac150f0e9a1cbaa65bc2` | `` | `missing` |
| `PATCH` | `/tasks/{id}#acknowledgment` | `schema:definitions/AckTaskPayload` | `` | `missing` |
| `PATCH` | `/tasks/{id}#acknowledgment` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/tasks/{id}#acknowledgment` | `schema:definitions/AckTaskPayload` | `` | `missing` |
| `GET` | `/tasks/{id}#acknowledgment` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/tasks/{id}#basic` | `schema:definitions/BasicTaskPayload` | `` | `missing` |
| `PATCH` | `/tasks/{id}#basic` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/tasks/{id}#basic` | `schema:definitions/BasicTaskPayload` | `` | `missing` |
| `GET` | `/tasks/{id}#basic` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/tasks/{id}#signature` | `schema:definitions/SignatureTaskPayload` | `` | `missing` |
| `PATCH` | `/tasks/{id}#signature` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/tasks/{id}#signature` | `schema:definitions/SignatureTaskPayload` | `` | `missing` |
| `GET` | `/tasks/{id}#signature` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/tasks/{id}#fill_form` | `schema:definitions/FillFormTaskPayload` | `` | `missing` |
| `PATCH` | `/tasks/{id}#fill_form` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/tasks/{id}#fill_form` | `schema:definitions/FillFormTaskPayload` | `` | `missing` |
| `GET` | `/tasks/{id}#fill_form` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/tasks/{id}#fill_pdf` | `schema:definitions/FillPdfTaskPayload` | `` | `missing` |
| `PATCH` | `/tasks/{id}#fill_pdf` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/tasks/{id}#fill_pdf` | `schema:definitions/FillPdfTaskPayload` | `` | `missing` |
| `GET` | `/tasks/{id}#fill_pdf` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/tasks/{id}#validation` | `schema:definitions/ValidationTaskPayload` | `` | `missing` |
| `PATCH` | `/tasks/{id}#validation` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/tasks/{id}#validation` | `schema:definitions/ValidationTaskPayload` | `` | `missing` |
| `GET` | `/tasks/{id}#validation` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/tasks/{id}/files` | `schema:definitions/TaskFileResource` | `TaskFileResourceDataObject` | `root` |
| `POST` | `/tasks/{id}/files` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/tasks/{id}/files/{file_id}` | `schema:definitions/TaskFileResource` | `TaskFileResourceDataObject` | `root` |
| `GET` | `/tasks/{id}/files/{file_id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `DELETE` | `/tasks/{id}/files/{file_id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/tasks/{id}/files/{file_id}` | `schema:definitions/TaskFileResource` | `TaskFileResourceDataObject` | `root` |
| `PATCH` | `/tasks/{id}/files/{file_id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/tasks/{id}/files/{file_id}/download` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/tasks/{id}/workingfiles/{file_id}` | `schema:anon/4ef0966440754d94ecce66468691d81fe9b2a120` | `` | `missing` |
| `GET` | `/tasks/{id}/workingfiles/{file_id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/tasks/{id}/fill` | `schema:definitions/TaskFull` | `` | `missing` |
| `POST` | `/tasks/{id}/fill` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/tasks/{id}/fill` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/employee_settings/{employee_id}/process_automation` | `schema:definitions/EmployeeSettingsProcessAutomation` | `EmployeeSettingsProcessAutomationDataObject` | `root` |
| `GET` | `/employee_settings/{employee_id}/process_automation` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/employee_settings/{employee_id}/process_automation/welcome_file` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/kb_categories` | `schema:anon/6585ded45263b3acb3c85a031b33d07ddb5838ce` | `` | `missing` |
| `GET` | `/kb_categories/{id}` | `schema:definitions/KbCategoryFull` | `KbCategoryFullDataObject` | `root` |
| `GET` | `/kb_categories/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `DELETE` | `/kb_categories/{id}` | `schema:definitions/KbCategoryDeletionError` | `` | `missing` |
| `DELETE` | `/kb_categories/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `DELETE` | `/kb_categories/{id}` | `schema:definitions/Error` | `` | `missing` |
| `PATCH` | `/kb_categories/{id}` | `schema:definitions/KbCategoryFull` | `KbCategoryFullDataObject` | `root` |
| `PATCH` | `/kb_categories/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/kb_categories/{id}` | `schema:definitions/Error` | `` | `missing` |
| `PUT` | `/kb_categories/{id}` | `schema:anon/6585ded45263b3acb3c85a031b33d07ddb5838ce` | `` | `missing` |
| `PUT` | `/kb_categories/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/kb_categories/{id}` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/article_resources/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/article_documents/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/kb_articles` | `schema:anon/888d6facb4aefdffb6ce9cb24b8f6dbf3ebf2b94` | `` | `missing` |
| `GET` | `/kb_articles` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/kb_articles/images` | `schema:definitions/KbArticleImage` | `` | `missing` |
| `POST` | `/kb_articles/images` | `schema:definitions/Error` | `` | `missing` |
| `POST` | `/kb_articles/images` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/kb_articles/{id}` | `schema:definitions/KbArticleFull` | `` | `missing` |
| `GET` | `/kb_articles/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/kb_articles/{id}` | `schema:definitions/KbArticleFull` | `` | `missing` |
| `PUT` | `/kb_articles/{id}` | `schema:definitions/KbArticleFull` | `` | `missing` |
| `PUT` | `/kb_articles/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/kb_articles/{id}` | `schema:definitions/Error` | `` | `missing` |
| `PUT` | `/kb_articles/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `DELETE` | `/kb_articles/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `DELETE` | `/kb_articles/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/kb_articles/{id}` | `schema:definitions/KbArticleFull` | `` | `missing` |
| `PATCH` | `/kb_articles/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/kb_articles/{id}` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/kb_tags` | `schema:anon/64b27ab8c3c56801e744779c2582279b8bd7eb40` | `` | `missing` |
| `GET` | `/kb_tags` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/requests` | `schema:anon/775063622faa0c3238bbe8e30f977893a59e85f0` | `` | `missing` |
| `GET` | `/requests` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/requests` | `schema:definitions/RequestFullWithAttachments` | `RequestFullWithAttachmentsDataObject` | `root` |
| `POST` | `/requests` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/requests/{id}/comments` | `schema:anon/c4ab9b52f95636e64eb20c166044935588f1c435` | `` | `missing` |
| `GET` | `/requests/{id}/comments` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/requests/{id}/comments` | `schema:definitions/RequestComment` | `RequestCommentDataObject` | `root` |
| `POST` | `/requests/{id}/comments` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `HEAD` | `/requests/{id}/comments/{comment_id}/attachments/{attachment_id}/preview` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/requests/{id}/comments/{comment_id}/attachments/{attachment_id}/preview/{page}` | `schema:anon/4ef0966440754d94ecce66468691d81fe9b2a120` | `` | `missing` |
| `GET` | `/requests/{id}/comments/{comment_id}/attachments/{attachment_id}/preview/{page}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/requests/{id}` | `schema:definitions/RequestFullWithAttachments` | `RequestFullWithAttachmentsDataObject` | `root` |
| `GET` | `/requests/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `DELETE` | `/requests/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/requests/{id}` | `schema:definitions/RequestFullWithAttachments` | `RequestFullWithAttachmentsDataObject` | `root` |
| `PATCH` | `/requests/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/requests/{id}` | `schema:definitions/Forbidden` | `ForbiddenDataObject` | `root` |
| `PATCH` | `/requests/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/requests/{id}` | `schema:definitions/Error` | `` | `missing` |
| `DELETE` | `/requests/{id}/files/{file_id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/requests/{id}/files/{file_id}/download` | `schema:anon/4ef0966440754d94ecce66468691d81fe9b2a120` | `` | `missing` |
| `GET` | `/requests/{id}/files/{file_id}/download` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `HEAD` | `/requests/{id}/files/{file_id}/preview` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/requests/{id}/files/{file_id}/preview/{page}` | `schema:anon/4ef0966440754d94ecce66468691d81fe9b2a120` | `` | `missing` |
| `GET` | `/requests/{id}/files/{file_id}/preview/{page}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `DELETE` | `/requests/{id}/attachments/{attachment_id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/requests/{id}/attachments/{attachment_id}/download` | `schema:anon/4ef0966440754d94ecce66468691d81fe9b2a120` | `` | `missing` |
| `GET` | `/requests/{id}/attachments/{attachment_id}/download` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `HEAD` | `/requests/{id}/attachments/{attachment_id}/preview` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/requests/{id}/attachments/{attachment_id}/preview/{page}` | `schema:anon/4ef0966440754d94ecce66468691d81fe9b2a120` | `` | `missing` |
| `GET` | `/requests/{id}/attachments/{attachment_id}/preview/{page}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/requests/{id}/pdf` | `schema:anon/4ef0966440754d94ecce66468691d81fe9b2a120` | `` | `missing` |
| `GET` | `/requests/{id}/pdf` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/requests/{id}/assignees` | `schema:anon/3bfb95c39dd9c9740e366c2a0f63f7597632a6cc` | `` | `missing` |
| `GET` | `/requests/{id}/macros` | `schema:anon/1f57037e5c42b4db439332c55f0a1c6802ae7a84` | `` | `missing` |
| `GET` | `/requests/{id}/macros` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/requests/{id}/macros` | `schema:definitions/Forbidden` | `ForbiddenDataObject` | `root` |
| `POST` | `/requests/{id}/macros` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/requests/{id}/linked_requests` | `schema:anon/775063622faa0c3238bbe8e30f977893a59e85f0` | `` | `missing` |
| `GET` | `/requests/{id}/linked_requests` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/requests/{id}/linked_requests` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/request_forms` | `schema:anon/089ee1bd66e109c974975933f2010b60b1ccab71` | `` | `missing` |
| `GET` | `/request_forms` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/request_forms/{id}` | `schema:definitions/RequestFormFull` | `` | `missing` |
| `GET` | `/request_forms/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/request_forms/{id}` | `schema:definitions/RequestFormPatch` | `` | `missing` |
| `PATCH` | `/request_forms/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/request_forms/{id}` | `schema:definitions/Error` | `` | `missing` |
| `PUT` | `/request_forms/{id}` | `schema:definitions/RequestFormPut` | `` | `missing` |
| `PUT` | `/request_forms/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/request_forms/{id}` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/client` | `schema:definitions/CoreClientFull` | `` | `missing` |
| `POST` | `/platform_updates` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/platform_updates` | `schema:definitions/Error` | `` | `missing` |
| `POST` | `/distribution_projects` | `schema:definitions/DistributionProjectFull` | `` | `missing` |
| `POST` | `/distribution_projects` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/distribution_projects` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/distribution_projects` | `schema:anon/906cd7d087081a0d824839e56dd6cb2fef2bfdb9` | `` | `missing` |
| `GET` | `/distribution_projects` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/distribution_projects/{id}` | `schema:definitions/DistributionProjectFull` | `` | `missing` |
| `GET` | `/distribution_projects/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/distribution_projects/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/distributions` | `schema:definitions/DistributionFull` | `` | `missing` |
| `POST` | `/distributions` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/distributions` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/distributions` | `schema:anon/373db6efdc978baa34136c20670e74cb22fc3cbc` | `` | `missing` |
| `GET` | `/distributions/{id}` | `schema:definitions/DistributionFull` | `` | `missing` |
| `GET` | `/distributions/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/distributions/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/distributions/{id}/report` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/distributions/{id}/report` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/tokens` | `schema:definitions/TokenFull` | `` | `missing` |
| `POST` | `/tokens` | `schema:definitions/OAuthError` | `` | `missing` |
| `POST` | `/tokens` | `schema:definitions/OAuthError` | `` | `missing` |
| `POST` | `/revoke_token` | `schema:definitions/OAuthError` | `` | `missing` |
| `POST` | `/document_generations` | `schema:definitions/DocGenFullWithErrors` | `` | `missing` |
| `DELETE` | `/document_generations/{id}` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generations/{id}` | `schema:definitions/DocGenFull` | `DocGenFullDataObject` | `root` |
| `GET` | `/document_generations/{id}` | `schema:definitions/BaseError` | `` | `missing` |
| `HEAD` | `/document_generations/{id}/file` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generations/{id}/file` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generations/{id}/preview` | `schema:anon/4ef0966440754d94ecce66468691d81fe9b2a120` | `` | `missing` |
| `GET` | `/document_generations/{id}/preview` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generations/{id}/preview/{page}` | `schema:anon/4ef0966440754d94ecce66468691d81fe9b2a120` | `` | `missing` |
| `GET` | `/document_generations/{id}/preview/{page}` | `schema:definitions/BaseError` | `` | `missing` |
| `POST` | `/document_generations/{id}/email` | `schema:definitions/DocGenFullWithErrors` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/{number}/doc_fields` | `schema:definitions/FormidableCreatePayload` | `FormidableCreatePayloadDataObject` | `root` |
| `GET` | `/document_generation_templates/{id}/versions/{number}/doc_fields` | `schema:definitions/BaseError` | `` | `missing` |
| `PUT` | `/document_generation_templates/{id}/versions/{number}/doc_fields` | `schema:definitions/FormidableCreatePayload` | `FormidableCreatePayloadDataObject` | `root` |
| `PUT` | `/document_generation_templates/{id}/versions/{number}/doc_fields` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generation_templates` | `schema:anon/b06a702c0cc5b75c38a2f13547adf26fae995cd8` | `` | `missing` |
| `POST` | `/document_generation_templates` | `schema:definitions/DocGenTemplate` | `DocGenTemplateDataObject` | `root` |
| `POST` | `/document_generation_templates` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `DELETE` | `/document_generation_templates/{id}` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}` | `schema:definitions/DocGenTemplate` | `DocGenTemplateDataObject` | `root` |
| `GET` | `/document_generation_templates/{id}` | `schema:definitions/BaseError` | `` | `missing` |
| `PATCH` | `/document_generation_templates/{id}` | `schema:definitions/DocGenTemplate` | `DocGenTemplateDataObject` | `root` |
| `PATCH` | `/document_generation_templates/{id}` | `schema:definitions/BaseError` | `` | `missing` |
| `PUT` | `/document_generation_templates/{id}` | `schema:definitions/DocGenTemplate` | `DocGenTemplateDataObject` | `root` |
| `PUT` | `/document_generation_templates/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/document_generation_templates/{id}` | `schema:definitions/BaseError` | `` | `missing` |
| `POST` | `/document_generation_templates/{id}/file` | `schema:definitions/DocGenTemplateVersion` | `DocGenTemplateVersionDataObject` | `root` |
| `POST` | `/document_generation_templates/{id}/file` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/document_generation_templates/{id}/file` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/fragment_usages` | `schema:anon/04f3aee7230e3fba1c509255862123dfc9f22cd2` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/fragment_usages` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions` | `schema:anon/6e85c5ca7ec2767e831b3fa8eaec108d8fee8a8c` | `` | `missing` |
| `DELETE` | `/document_generation_templates/{id}/versions/{number}` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/{number}` | `schema:definitions/DocGenTemplateVersion` | `DocGenTemplateVersionDataObject` | `root` |
| `GET` | `/document_generation_templates/{id}/versions/{number}` | `schema:definitions/BaseError` | `` | `missing` |
| `PUT` | `/document_generation_templates/{id}/versions/{number}` | `schema:definitions/DocGenTemplateVersion` | `DocGenTemplateVersionDataObject` | `root` |
| `PUT` | `/document_generation_templates/{id}/versions/{number}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/document_generation_templates/{id}/versions/{number}` | `schema:definitions/DocGenTemplateVersionFull` | `DocGenTemplateVersionFullDataObject` | `root` |
| `PATCH` | `/document_generation_templates/{id}/versions/{number}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `HEAD` | `/document_generation_templates/{id}/versions/{number}/file` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/{number}/file` | `schema:definitions/BaseError` | `` | `missing` |
| `HEAD` | `/document_generation_templates/{id}/versions/active/file` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/active/file` | `schema:definitions/BaseError` | `` | `missing` |
| `HEAD` | `/document_generation_templates/{id}/versions/latest/file` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/latest/file` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/{number}/fields` | `schema:definitions/FieldSet` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/{number}/fields` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/active/fields` | `schema:definitions/FieldSet` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/active/fields` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/latest/fields` | `schema:definitions/FieldSet` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/latest/fields` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/{number}/preview` | `schema:anon/4ef0966440754d94ecce66468691d81fe9b2a120` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/{number}/preview` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/active/preview` | `schema:anon/4ef0966440754d94ecce66468691d81fe9b2a120` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/active/preview` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/latest/preview` | `schema:anon/4ef0966440754d94ecce66468691d81fe9b2a120` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/latest/preview` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/{number}/preview/{page}` | `schema:anon/4ef0966440754d94ecce66468691d81fe9b2a120` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/{number}/preview/{page}` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/active/preview/{page}` | `schema:anon/4ef0966440754d94ecce66468691d81fe9b2a120` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/active/preview/{page}` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/latest/preview/{page}` | `schema:anon/4ef0966440754d94ecce66468691d81fe9b2a120` | `` | `missing` |
| `GET` | `/document_generation_templates/{id}/versions/latest/preview/{page}` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generations/syntax_migration/status` | `schema:definitions/DocGenMigrationCampaign` | `DocGenMigrationCampaignDataObject` | `root` |
| `PUT` | `/document_generations/syntax_migration/status` | `schema:definitions/DocGenMigrationCampaign` | `DocGenMigrationCampaignDataObject` | `root` |
| `POST` | `/document_generations/syntax_migration/restart` | `schema:definitions/DocGenMigrationCampaign` | `DocGenMigrationCampaignDataObject` | `root` |
| `POST` | `/document_generations/syntax_migration/restart` | `schema:definitions/BaseError` | `` | `missing` |
| `POST` | `/document_generations/syntax_migration/restart` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generations/syntax_migration/list` | `schema:anon/775ab4200a85248650330620627c3191895b6b8f` | `` | `missing` |
| `POST` | `/document_generations/syntax_migration/{id}` | `schema:definitions/DocGenTemplateVersionFull` | `DocGenTemplateVersionFullDataObject` | `root` |
| `POST` | `/document_generations/syntax_migration/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/document_generations/syntax_migration/{id}` | `schema:definitions/BaseError` | `` | `missing` |
| `POST` | `/document_generations/syntax_migration/{id}` | `schema:definitions/BaseError` | `` | `missing` |
| `POST` | `/document_generations/syntax_migration/{id}` | `schema:definitions/BaseError` | `` | `missing` |
| `POST` | `/document_generation_campaigns` | `schema:definitions/DocGenCampaignResponse` | `DocGenCampaignResponseDataObject` | `root` |
| `GET` | `/document_generation_campaigns` | `schema:anon/ac6d1dc118b25a7ed1b92b83b08dd27fe2febb2f` | `` | `missing` |
| `POST` | `/document_generation_campaigns/csv` | `schema:definitions/CsvCampaign` | `` | `missing` |
| `POST` | `/document_generation_campaigns/csv` | `schema:definitions/BaseError` | `` | `missing` |
| `POST` | `/document_generation_campaigns/csv` | `schema:definitions/BaseError` | `` | `missing` |
| `POST` | `/document_generation_campaigns/csv` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generation_campaigns/{id}` | `schema:definitions/DocGenCampaignResponse` | `DocGenCampaignResponseDataObject` | `root` |
| `GET` | `/document_generation_campaigns/{id}/file` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generation_campaigns/{id}/file` | `schema:definitions/BaseError` | `` | `missing` |
| `GET` | `/document_generation_requests/{id}/status` | `schema:definitions/DocGenRequestStatusResponse` | `DocGenRequestStatusResponseDataObject` | `root` |
| `GET` | `/document_generation_requests` | `schema:anon/0b6db8ffe97262bfb8d32aa75ed908d16f3913e6` | `` | `missing` |
| `POST` | `/saml/identity_providers` | `schema:definitions/SamlIdentityProviderFull` | `SamlIdentityProviderFullDataObject` | `root` |
| `POST` | `/saml/identity_providers` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/saml/identity_providers` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/saml/identity_providers` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/saml/identity_providers` | `schema:anon/7848fbf9d588bc0223492736dd5178fcfacc18aa` | `` | `missing` |
| `GET` | `/saml/identity_providers/{id}` | `schema:definitions/SamlIdentityProviderFull` | `SamlIdentityProviderFullDataObject` | `root` |
| `GET` | `/saml/identity_providers/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/saml/identity_providers/{id}` | `schema:definitions/SamlIdentityProviderFull` | `SamlIdentityProviderFullDataObject` | `root` |
| `PATCH` | `/saml/identity_providers/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PATCH` | `/saml/identity_providers/{id}` | `schema:definitions/Error` | `` | `missing` |
| `PUT` | `/saml/identity_providers/{id}` | `schema:definitions/SamlIdentityProviderFull` | `SamlIdentityProviderFullDataObject` | `root` |
| `PUT` | `/saml/identity_providers/{id}` | `schema:definitions/SamlIdentityProviderFull` | `SamlIdentityProviderFullDataObject` | `root` |
| `PUT` | `/saml/identity_providers/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/saml/identity_providers/{id}` | `schema:definitions/Error` | `` | `missing` |
| `DELETE` | `/saml/identity_providers/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/events` | `schema:anon/05f5b629ed8097ca7cddfd668e515f1e85181448` | `` | `missing` |
| `GET` | `/roles/{role_id}/permissions/audit` | `schema:definitions/AuditPermissionsFull` | `AuditPermissionsFullDataObject` | `root` |
| `PUT` | `/roles/{role_id}/permissions/audit` | `schema:definitions/AuditPermissionsFull` | `AuditPermissionsFullDataObject` | `root` |
| `PUT` | `/roles/{role_id}/permissions/audit` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/events/{id}` | `schema:definitions/EventBase` | `EventBaseDataObject` | `root` |
| `GET` | `/events/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/events/export` | `schema:anon/2edaec8241dcf7c871fc19b8b6f92bae66cfaf10` | `` | `missing` |
| `GET` | `/events/export` | `schema:anon/2edaec8241dcf7c871fc19b8b6f92bae66cfaf10` | `` | `missing` |
| `GET` | `/events/filters/actions` | `schema:anon/08ade60f52657cdad656585770b0ed0603dfa5a4` | `` | `missing` |
| `GET` | `/webhooks` | `schema:anon/80021de2832ff47b51d3143a1ab9f9d6d0782bb9` | `` | `missing` |
| `POST` | `/webhooks` | `schema:definitions/WebhookFull` | `` | `missing` |
| `POST` | `/webhooks` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/webhooks/{id}` | `schema:definitions/WebhookFull` | `` | `missing` |
| `PUT` | `/webhooks/{id}` | `schema:definitions/WebhookFull` | `` | `missing` |
| `PUT` | `/webhooks/{id}` | `schema:definitions/Error` | `` | `missing` |
| `POST` | `/webhooks/{id}/refresh_signature_key` | `schema:definitions/WebhookFull` | `` | `missing` |
| `POST` | `/webhooks/{id}/tests` | `schema:definitions/WebhookFull` | `` | `missing` |
| `GET` | `/roles/{role_id}/permissions/webhook` | `schema:definitions/WebhookPermissionsFull` | `WebhookPermissionsFullDataObject` | `root` |
| `PUT` | `/roles/{role_id}/permissions/webhook` | `schema:definitions/WebhookPermissionsFull` | `WebhookPermissionsFullDataObject` | `root` |
| `PUT` | `/roles/{role_id}/permissions/webhook` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/settings/core` | `schema:definitions/CoreSettingsFull` | `` | `missing` |
| `GET` | `/settings/process_automation` | `schema:definitions/ProcessAutomationSettingsFull` | `ProcessAutomationSettingsFullDataObject` | `root` |
| `GET` | `/settings/knowledge_base` | `schema:definitions/KnowledgeBaseSettings` | `KnowledgeBaseSettingsDataObject` | `root` |
| `GET` | `/settings/case_management` | `schema:definitions/CaseManagementSettings` | `CaseManagementSettingsDataObject` | `root` |
| `GET` | `/datasets` | `schema:anon/ecc811652a928c2fe8ecf0bfeab4342ce84786be` | `` | `missing` |
| `GET` | `/datasets` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/datasets/{id}` | `schema:definitions/DatasetFull` | `DatasetFullDataObject` | `root` |
| `GET` | `/datasets/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/datasets/{id}` | `schema:definitions/DatasetFull` | `DatasetFullDataObject` | `root` |
| `PUT` | `/datasets/{id}` | `schema:definitions/DatasetFull` | `DatasetFullDataObject` | `root` |
| `PUT` | `/datasets/{id}` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/datasets/{id}/values` | `schema:anon/766eaf4007e238e701301c1cc85e64116d4b270e` | `` | `missing` |
| `GET` | `/datasets/{id}/values` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/datasets/{id}/values/{value_id}` | `schema:definitions/DatasetValueFull` | `DatasetValueFullDataObject` | `root` |
| `GET` | `/datasets/{id}/values/{value_id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `HEAD` | `/datasets/{id}/values/{value_id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/datasets/{id}/values/{value_id}` | `schema:definitions/DatasetValueFull` | `DatasetValueFullDataObject` | `root` |
| `PUT` | `/datasets/{id}/values/{value_id}` | `schema:definitions/DatasetValueFull` | `DatasetValueFullDataObject` | `root` |
| `PUT` | `/datasets/{id}/values/{value_id}` | `schema:definitions/Error` | `` | `missing` |
| `DELETE` | `/datasets/{id}/values/{value_id}` | `schema:definitions/Error` | `` | `missing` |
| `POST` | `/document_type_prediction_run` | `schema:definitions/DocumentTypePredictionRun` | `DocumentTypePredictionRunDataObject` | `root` |
| `POST` | `/document_type_prediction_run` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `POST` | `/document_type_prediction_run` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/document_type_prediction_run/{id}` | `schema:definitions/DocumentTypePredictionRun` | `DocumentTypePredictionRunDataObject` | `root` |
| `GET` | `/document_type_prediction_run/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `GET` | `/macros` | `schema:anon/38b2796c882026cacb10dc2047ba6da0283fcb15` | `` | `missing` |
| `GET` | `/macros/{id}` | `schema:definitions/MacroDetail` | `` | `missing` |
| `GET` | `/macros/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/macros/{id}` | `schema:definitions/MacroDetail` | `` | `missing` |
| `PUT` | `/macros/{id}` | `schema:definitions/MacroDetail` | `` | `missing` |
| `PUT` | `/macros/{id}` | `schema:definitions/Error` | `` | `missing` |
| `GET` | `/custom_status` | `schema:anon/2ea0111c6225430d57de709997a73a74c59d4337` | `` | `missing` |
| `GET` | `/custom_status/{id}` | `schema:definitions/CustomStatusDetail` | `` | `missing` |
| `GET` | `/custom_status/{id}` | `schema:definitions/BadRequest` | `BadRequestDataObject` | `root` |
| `PUT` | `/custom_status/{id}` | `schema:definitions/CustomStatusDetail` | `` | `missing` |
| `PUT` | `/custom_status/{id}` | `schema:definitions/CustomStatusDetail` | `` | `missing` |
| `PUT` | `/custom_status/{id}` | `schema:definitions/Error` | `` | `missing` |

## Unmapped Schemas

- `schema:anon/04f3aee7230e3fba1c509255862123dfc9f22cd2`
- `schema:anon/05f5b629ed8097ca7cddfd668e515f1e85181448`
- `schema:anon/089ee1bd66e109c974975933f2010b60b1ccab71`
- `schema:anon/08ade60f52657cdad656585770b0ed0603dfa5a4`
- `schema:anon/0943141efa0200182a6c0bb0d6b9444b716abe26`
- `schema:anon/0b6db8ffe97262bfb8d32aa75ed908d16f3913e6`
- `schema:anon/12e4c29a4d55d063dc86bebeaf38bf8fdab962e5`
- `schema:anon/1f57037e5c42b4db439332c55f0a1c6802ae7a84`
- `schema:anon/25ce8149912273a869f2c4e931666e01bdb86bbf`
- `schema:anon/2ea0111c6225430d57de709997a73a74c59d4337`
- `schema:anon/2edaec8241dcf7c871fc19b8b6f92bae66cfaf10`
- `schema:anon/3043869d9d959dbd70c0572f1c48f37687317660`
- `schema:anon/373db6efdc978baa34136c20670e74cb22fc3cbc`
- `schema:anon/38b2796c882026cacb10dc2047ba6da0283fcb15`
- `schema:anon/3bfb95c39dd9c9740e366c2a0f63f7597632a6cc`
- `schema:anon/49e966dbb2286958e7bd268f2b7f00e279570463`
- `schema:anon/4ef0966440754d94ecce66468691d81fe9b2a120`
- `schema:anon/4fda8799c92e57c81aff0b5fec0301de1a3a79c5`
- `schema:anon/510932133ea32afb1165548fc5d46b15720f18ef`
- `schema:anon/574132e6e898a6dde6c146408dacf2510e9fe68f`
- `schema:anon/64b27ab8c3c56801e744779c2582279b8bd7eb40`
- `schema:anon/6585ded45263b3acb3c85a031b33d07ddb5838ce`
- `schema:anon/6e85c5ca7ec2767e831b3fa8eaec108d8fee8a8c`
- `schema:anon/713127302efd3e065589fb6ffc2c924ea6dfa3d8`
- `schema:anon/766eaf4007e238e701301c1cc85e64116d4b270e`
- `schema:anon/775063622faa0c3238bbe8e30f977893a59e85f0`
- `schema:anon/775ab4200a85248650330620627c3191895b6b8f`
- `schema:anon/7848fbf9d588bc0223492736dd5178fcfacc18aa`
- `schema:anon/784c9c2066d6295cc3b049eacb69d4815eea3400`
- `schema:anon/80021de2832ff47b51d3143a1ab9f9d6d0782bb9`
- `schema:anon/810ccd9b714002635c36ac4a9a1b0991dc0fd449`
- `schema:anon/888d6facb4aefdffb6ce9cb24b8f6dbf3ebf2b94`
- `schema:anon/906cd7d087081a0d824839e56dd6cb2fef2bfdb9`
- `schema:anon/a6dc079ddf9eff65144267392e407e1f5ead40cc`
- `schema:anon/a7d973accdf4c2c2660945da290d177c9b727cd0`
- `schema:anon/aa0cfc068e025c28d6d580b4397375e997e965bd`
- `schema:anon/aa296d5d3ced8247f5b49d4c0ca0bc5840c26f62`
- `schema:anon/ac6d1dc118b25a7ed1b92b83b08dd27fe2febb2f`
- `schema:anon/b06a702c0cc5b75c38a2f13547adf26fae995cd8`
- `schema:anon/b0c37f04150f97e8cac6df1a54929b8a5cfb8bd0`
- `schema:anon/b20d699cf7b14746324dbd42bf959b87d0a930ec`
- `schema:anon/bb4cf25bfe441228ba77915ab5cb2edad954dbd4`
- `schema:anon/c071e6cecd79b1e634f7dc4aafb3e664234a67e8`
- `schema:anon/c194bdf2ca6aa88d63a9f86b63ae43f3e0ad2674`
- `schema:anon/c33cf55f8516018dfec2345eadb6c3b8a504c947`
- `schema:anon/c4ab9b52f95636e64eb20c166044935588f1c435`
- `schema:anon/c6e719439cb16efc1d588734262fa68b3656ea68`
- `schema:anon/c8499daacd0b84ab9982b5a6f1c38a7171d8f366`
- `schema:anon/d14f6e39b9c2423c40bdac150f0e9a1cbaa65bc2`
- `schema:anon/d66080a6d8906ee35e18b5732d6197fe03d5a6ef`
- `schema:anon/dadb9bfad9410c9ba708c98acf88909c6e0730ab`
- `schema:anon/ecc811652a928c2fe8ecf0bfeab4342ce84786be`
- `schema:anon/ef8a93997d834fc0787d5023a82362d99e83839f`
- `schema:anon/f19a35a40a7859425a63281011673eb6c82b360f`
- `schema:anon/f467c82983edfab75b39cfdd081102de6b3498b9`
- `schema:definitions/AckTaskPayload`
- `schema:definitions/AcknowledgmentTaskTemplates`
- `schema:definitions/BaseError`
- `schema:definitions/BasicTaskPayload`
- `schema:definitions/BasicTaskTemplates`
- `schema:definitions/CompanyDocumentTypeFull`
- `schema:definitions/CoreClientFull`
- `schema:definitions/CoreSettingsFull`
- `schema:definitions/CsvCampaign`
- `schema:definitions/CustomStatusDetail`
- `schema:definitions/DistributionFull`
- `schema:definitions/DistributionProjectFull`
- `schema:definitions/DocGenFullWithErrors`
- `schema:definitions/EmployeeDocumentTypeFull`
- `schema:definitions/EmployeeSubscriptionFull`
- `schema:definitions/Error`
- `schema:definitions/FieldSet`
- `schema:definitions/FillFormTaskPayload`
- `schema:definitions/FillFormTaskTemplates`
- `schema:definitions/FillPdfTaskPayload`
- `schema:definitions/FillPdfTaskTemplates`
- `schema:definitions/KbArticleFull`
- `schema:definitions/KbArticleImage`
- `schema:definitions/KbCategoryDeletionError`
- `schema:definitions/MacroDetail`
- `schema:definitions/OAuthError`
- `schema:definitions/OrganizationFull`
- `schema:definitions/OrganizationGroupFull`
- `schema:definitions/PdfTemplateDetail`
- `schema:definitions/ProcessFull`
- `schema:definitions/ProcessPostActionSharedPayload`
- `schema:definitions/ProcessPostActionUserPayload`
- `schema:definitions/RateLimitErrors`
- `schema:definitions/RequestFormFull`
- `schema:definitions/RequestFormPatch`
- `schema:definitions/RequestFormPut`
- `schema:definitions/SignatureTaskPayload`
- `schema:definitions/SignatureTaskTemplates`
- `schema:definitions/TaskFull`
- `schema:definitions/TokenFull`
- `schema:definitions/UploadDocument`
- `schema:definitions/ValidationTaskPayload`
- `schema:definitions/ValidationTaskTemplates`
- `schema:definitions/WebhookFull`
