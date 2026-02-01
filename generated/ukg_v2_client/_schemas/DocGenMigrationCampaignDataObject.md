# DocGenMigrationCampaignDataObject

## DocGenMigrationCampaignDataObject
- Role: parent
- Schema Name: DocGenMigrationCampaign
- Schema ID: schema:definitions/DocGenMigrationCampaign

### Fields

| Field | Type |
|------|------|
| `status` | `DocGenMigrationCampaignStatus` |
| `new_migration_available` | `bool` |

### Nested Types
- `DocGenMigrationCampaignStatus`

## DocGenMigrationCampaignStatus
- Role: nested
- Parent: DocGenMigrationCampaignDataObject
- Schema Name: DocGenMigrationCampaignStatus
- Schema ID: schema:anon/90d3539a873fedbd9b0a95acf3ed43b1770dd996

### Enum

Values: created, started, completed, failed, canceled
