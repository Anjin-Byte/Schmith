# RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200DataObject

## RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200DataObject
- Role: parent
- Schema Name: RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200
- Schema ID: schema:anon/77a1354ebba5833d84da709e17602e910bbaccab
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `title` | `string` |
| `files` | `RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItem[]` |
| `pdm_pagination` | `RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200PdmPagination` |

### Nested Types
- `RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItem`
- `RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItemDrawing`
- `RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItemPdm`
- `RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItemPdmAttachment`
- `RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItemPdmDocumentRevision`
- `RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItemPdmDocumentRevisionPermissions`
- `RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200PdmPagination`

## RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItem
- Role: nested
- Parent: RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItem
- Schema ID: schema:anon/ef27dc4748a842a0eac36415ac80fd3b3f62ea00

### Fields

| Field | Type |
|------|------|
| `size` | `int` |
| `file_path` | `string` |
| `s3_source` | `string` |
| `type` | `string` |
| `drawing` | `RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItemDrawing` |
| `pdm` | `RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItemPdm` |

## RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItemDrawing
- Role: nested
- Parent: RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItemDrawing
- Schema ID: schema:anon/6285670d1d5ffe4cdd686e932cd2dd4b0f761067
- Primary Key: DrawingSetId

### Fields

| Field | Type |
|------|------|
| `dpi` | `double` |
| `revision` | `string` |
| `drawing_set_id` | `double` |
| `drawing_id` | `double` |
| `width` | `double` |
| `height` | `double` |
| `png_s3_source` | `string` |
| `thumbnail_url` | `string` |

## RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItemPdm
- Role: nested
- Parent: RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItemPdm
- Schema ID: schema:anon/f0cb2bf47b519e8fabd59ddf9499a29b1c9fb0dc
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `document_revision_id` | `string` |
| `document_container_id` | `string` |
| `document_collection_id` | `string` |
| `document_revision` | `RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItemPdmDocumentRevision` |
| `attachment` | `RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItemPdmAttachment` |

## RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItemPdmAttachment
- Role: nested
- Parent: RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItemPdmAttachment
- Schema ID: schema:anon/74373ab705818d85f8b5f1d6fc5255cdd7d79c95
- Primary Key: AttachedToItemId

### Fields

| Field | Type |
|------|------|
| `attached_to_item_id` | `string` |
| `attached_to_item_type` | `string` |
| `viewer_url` | `string` |

## RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItemPdmDocumentRevision
- Role: nested
- Parent: RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItemPdmDocumentRevision
- Schema ID: schema:anon/b0df03fc1bea873ea1b6ab1d467389a19dd16e5f

### Fields

| Field | Type |
|------|------|
| `name` | `string` |
| `download_url` | `string` |
| `file_locked` | `bool` |
| `status` | `string` |
| `description` | `string` |
| `type` | `string` |
| `revision` | `string` |
| `format` | `string` |
| `original_filename` | `string` |
| `file_size` | `string` |
| `originator` | `string` |
| `number` | `string` |
| `location` | `string` |
| `discipline` | `string` |
| `date_authored` | `string` |
| `version` | `string` |
| `uploaded_at` | `string` |
| `permissions` | `RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItemPdmDocumentRevisionPermissions` |

## RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItemPdmDocumentRevisionPermissions
- Role: nested
- Parent: RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200FilesItemPdmDocumentRevisionPermissions
- Schema ID: schema:anon/21d2cd9b6a34bfd1590a35821947e159f8314dbf

### Fields

| Field | Type |
|------|------|
| `allowed_actions` | `string[]` |

## RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200PdmPagination
- Role: nested
- Parent: RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200DataObject
- Schema Name: RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGetResponse200PdmPagination
- Schema ID: schema:anon/b1c7bf4b3deaf5bbc6ea21cd5ecf70d7aaaa4a06

### Fields

| Field | Type |
|------|------|
| `current_page` | `int` |
| `per_page` | `int` |
| `total_count` | `int` |
| `total_pages` | `int` |
| `has_next_page` | `bool` |
| `has_previous_page` | `bool` |
