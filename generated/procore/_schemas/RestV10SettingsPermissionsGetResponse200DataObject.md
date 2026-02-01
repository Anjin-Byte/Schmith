# RestV10SettingsPermissionsGetResponse200DataObject

## RestV10SettingsPermissionsGetResponse200DataObject
- Role: parent
- Schema Name: RestV10SettingsPermissionsGetResponse200
- Schema ID: schema:anon/044f37c4a68c1ef7d260306f6150803c014d7c40

### Fields

| Field | Type |
|------|------|
| `tools` | `RestV10SettingsPermissionsGetResponse200ToolsItem[]` |

### Nested Types
- `RestV10SettingsPermissionsGetResponse200ToolsItem`
- `RestV10SettingsPermissionsGetResponse200ToolsItemPermittedActionsItem`
- `RestV10SettingsPermissionsGetResponse200ToolsItemUserAccessLevel`

## RestV10SettingsPermissionsGetResponse200ToolsItem
- Role: nested
- Parent: RestV10SettingsPermissionsGetResponse200DataObject
- Schema Name: RestV10SettingsPermissionsGetResponse200ToolsItem
- Schema ID: schema:anon/a3ddf9189e40618231fb6b9d02b70ef02f2cbc19
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
| `friendly_name` | `string` |
| `domain_id` | `int` |
| `tab_group` | `string` |
| `available_for_user` | `bool` |
| `url` | `string` |
| `user_access_level` | `RestV10SettingsPermissionsGetResponse200ToolsItemUserAccessLevel` |
| `permitted_actions` | `RestV10SettingsPermissionsGetResponse200ToolsItemPermittedActionsItem[]` |
| `create_url` | `string` |
| `can_create` | `bool` |
| `trial` | `bool` |

## RestV10SettingsPermissionsGetResponse200ToolsItemPermittedActionsItem
- Role: nested
- Parent: RestV10SettingsPermissionsGetResponse200DataObject
- Schema Name: RestV10SettingsPermissionsGetResponse200ToolsItemPermittedActionsItem
- Schema ID: schema:anon/091ed909b094145ac397969273024dd434da2242
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `action_name` | `string` |
| `label` | `string` |
| `tool_name` | `string` |

## RestV10SettingsPermissionsGetResponse200ToolsItemUserAccessLevel
- Role: nested
- Parent: RestV10SettingsPermissionsGetResponse200DataObject
- Schema Name: RestV10SettingsPermissionsGetResponse200ToolsItemUserAccessLevel
- Schema ID: schema:anon/4f7a8fe84575a86f48db6966429d931fb71cd108
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `name` | `string` |
