# RestV10BudgetViewSnapshotsPostResponse202DataObject

## RestV10BudgetViewSnapshotsPostResponse202DataObject
- Role: parent
- Schema Name: RestV10BudgetViewSnapshotsPostResponse202
- Schema ID: schema:anon/017b4de88880ef394e14174b988c3dda06a635a9

### Fields

| Field | Type |
|------|------|
| `data` | `RestV10BudgetViewSnapshotsPostResponse202Data` |

### Nested Types
- `RestV10BudgetViewSnapshotsPostResponse202Data`
- `RestV10BudgetViewSnapshotsPostResponse202DataStatus`

## RestV10BudgetViewSnapshotsPostResponse202Data
- Role: nested
- Parent: RestV10BudgetViewSnapshotsPostResponse202DataObject
- Schema Name: RestV10BudgetViewSnapshotsPostResponse202Data
- Schema ID: schema:anon/6c8799f20dbb1a10edf27cce69dd64c7826d84a1
- Primary Key: SnapshotRequestId

### Fields

| Field | Type |
|------|------|
| `snapshot_request_id` | `int` |
| `status` | `RestV10BudgetViewSnapshotsPostResponse202DataStatus` |
| `budget_template_id` | `int` |
| `project_id` | `int` |
| `company_id` | `int` |

## RestV10BudgetViewSnapshotsPostResponse202DataStatus
- Role: nested
- Parent: RestV10BudgetViewSnapshotsPostResponse202DataObject
- Schema Name: RestV10BudgetViewSnapshotsPostResponse202DataStatus
- Schema ID: schema:anon/a9ea48d1e5c99441ff585b6cf4b857fc04d54933

### Enum

Values: queued, processing, completed, failed
