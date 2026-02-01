# RestV10BudgetViewSnapshotsPostResponse201DataObject

## RestV10BudgetViewSnapshotsPostResponse201DataObject
- Role: parent
- Schema Name: RestV10BudgetViewSnapshotsPostResponse201
- Schema ID: schema:anon/e8f51482c34821ed214bd9df22b63bac19cc49e9

### Fields

| Field | Type |
|------|------|
| `data` | `RestV10BudgetViewSnapshotsPostResponse201Data` |

### Nested Types
- `RestV10BudgetViewSnapshotsPostResponse201Data`
- `RestV10BudgetViewSnapshotsPostResponse201DataApprovalStatus`
- `RestV10BudgetViewSnapshotsPostResponse201DataBudgetView`
- `RestV10BudgetViewSnapshotsPostResponse201DataCreatedBy`
- `RestV10BudgetViewSnapshotsPostResponse201DataLinks`
- `RestV10BudgetViewSnapshotsPostResponse201DataSnapshotType`
- `RestV10BudgetViewSnapshotsPostResponse201DataStatus`
- `RestV10BudgetViewSnapshotsPostResponse201DataStatusMappedToStatus`
- `RestV10BudgetViewSnapshotsPostResponse201DataStatusStandardType`

## RestV10BudgetViewSnapshotsPostResponse201Data
- Role: nested
- Parent: RestV10BudgetViewSnapshotsPostResponse201DataObject
- Schema Name: RestV10BudgetViewSnapshotsPostResponse201Data
- Schema ID: schema:anon/c51c66665ed4dcac8d86ea1d6c3d14c48610a9b8
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `description` | `string` |
| `created_at` | `string` |
| `created_by` | `RestV10BudgetViewSnapshotsPostResponse201DataCreatedBy` |
| `budget_view` | `RestV10BudgetViewSnapshotsPostResponse201DataBudgetView` |
| `snapshot_type` | `RestV10BudgetViewSnapshotsPostResponse201DataSnapshotType` |
| `approval_status` | `RestV10BudgetViewSnapshotsPostResponse201DataApprovalStatus` |
| `status` | `RestV10BudgetViewSnapshotsPostResponse201DataStatus` |
| `links` | `RestV10BudgetViewSnapshotsPostResponse201DataLinks` |

## RestV10BudgetViewSnapshotsPostResponse201DataApprovalStatus
- Role: nested
- Parent: RestV10BudgetViewSnapshotsPostResponse201DataObject
- Schema Name: RestV10BudgetViewSnapshotsPostResponse201DataApprovalStatus
- Schema ID: schema:anon/186a4b5347cc3d2622aa8e9842e6d592a937394a

### Enum

Values: approved, under_review, custom

## RestV10BudgetViewSnapshotsPostResponse201DataBudgetView
- Role: nested
- Parent: RestV10BudgetViewSnapshotsPostResponse201DataObject
- Schema Name: RestV10BudgetViewSnapshotsPostResponse201DataBudgetView
- Schema ID: schema:anon/6189116eded751c26849e9f8eafcc994f8bce518
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |

## RestV10BudgetViewSnapshotsPostResponse201DataCreatedBy
- Role: nested
- Parent: RestV10BudgetViewSnapshotsPostResponse201DataObject
- Schema Name: RestV10BudgetViewSnapshotsPostResponse201DataCreatedBy
- Schema ID: schema:anon/b234ed52e7436ec99d0f862d766f735ad671221c
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `login` | `string` |

## RestV10BudgetViewSnapshotsPostResponse201DataLinks
- Role: nested
- Parent: RestV10BudgetViewSnapshotsPostResponse201DataObject
- Schema Name: RestV10BudgetViewSnapshotsPostResponse201DataLinks
- Schema ID: schema:anon/326099237c901b03bac97882e80a2667363096e9

### Fields

| Field | Type |
|------|------|
| `detail_rows` | `string` |
| `summary_rows` | `string` |

## RestV10BudgetViewSnapshotsPostResponse201DataSnapshotType
- Role: nested
- Parent: RestV10BudgetViewSnapshotsPostResponse201DataObject
- Schema Name: RestV10BudgetViewSnapshotsPostResponse201DataSnapshotType
- Schema ID: schema:anon/77e7d5b7ac03f36fb517de84ab21279642f5b6ea

### Enum

Values: ad_hoc, project_status_snapshot

## RestV10BudgetViewSnapshotsPostResponse201DataStatus
- Role: nested
- Parent: RestV10BudgetViewSnapshotsPostResponse201DataObject
- Schema Name: RestV10BudgetViewSnapshotsPostResponse201DataStatus
- Schema ID: schema:anon/efca8ebccbe2e3850acdecc314c23607af441917
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `name` | `string` |
| `mapped_to_status` | `RestV10BudgetViewSnapshotsPostResponse201DataStatusMappedToStatus` |
| `available` | `bool` |
| `initial` | `bool` |
| `standard_type` | `RestV10BudgetViewSnapshotsPostResponse201DataStatusStandardType` |
| `created_at` | `string` |
| `updated_at` | `string` |

## RestV10BudgetViewSnapshotsPostResponse201DataStatusMappedToStatus
- Role: nested
- Parent: RestV10BudgetViewSnapshotsPostResponse201DataObject
- Schema Name: RestV10BudgetViewSnapshotsPostResponse201DataStatusMappedToStatus
- Schema ID: schema:anon/5706a21ae8966d3e8a4e59dd65b0ec324054b14d

### Enum

Values: open, closed, void, pending

## RestV10BudgetViewSnapshotsPostResponse201DataStatusStandardType
- Role: nested
- Parent: RestV10BudgetViewSnapshotsPostResponse201DataObject
- Schema Name: RestV10BudgetViewSnapshotsPostResponse201DataStatusStandardType
- Schema ID: schema:anon/6429efd4b3f48aea799d14fb1618a146303b71f7

### Enum

Values: approved, under_review, custom
