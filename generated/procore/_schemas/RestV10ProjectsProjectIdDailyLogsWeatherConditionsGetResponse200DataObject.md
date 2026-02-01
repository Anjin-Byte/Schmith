# RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200DataObject

## RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200DataObject
- Role: parent
- Schema Name: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200
- Schema ID: schema:anon/b83c994e575f78e157d395fdd85f23cc0e17f5a5

### Fields

| Field | Type |
|------|------|
| `sky` | `RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200SkyItem[]` |
| `ground` | `RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200GroundItem[]` |
| `calamity` | `RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200CalamityItem[]` |
| `wind` | `RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200WindItem[]` |
| `temperature` | `RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200TemperatureItem[]` |

### Nested Types
- `RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200CalamityItem`
- `RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200CalamityItemKey`
- `RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200GroundItem`
- `RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200GroundItemKey`
- `RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200SkyItem`
- `RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200SkyItemKey`
- `RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200TemperatureItem`
- `RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200TemperatureItemKey`
- `RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200WindItem`
- `RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200WindItemKey`

## RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200CalamityItem
- Role: nested
- Parent: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200CalamityItem
- Schema ID: schema:anon/59502421160376f5680b4351bcc9ed1b31b0e7cf

### Fields

| Field | Type |
|------|------|
| `key` | `RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200CalamityItemKey` |
| `value` | `string` |

## RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200CalamityItemKey
- Role: nested
- Parent: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200CalamityItemKey
- Schema ID: schema:anon/6a7f0a4e7c4f785f8bff0e3ad237db6e6106d7e3

### Enum

Values: Earthquake, Fire, Flash Flood, Landslide, Tornado, Hurricane, Snow, Other

## RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200GroundItem
- Role: nested
- Parent: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200GroundItem
- Schema ID: schema:anon/a13545280ed16bf687d06dc2e28f8fa295eba9f4

### Fields

| Field | Type |
|------|------|
| `key` | `RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200GroundItemKey` |
| `value` | `string` |

## RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200GroundItemKey
- Role: nested
- Parent: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200GroundItemKey
- Schema ID: schema:anon/b0b21fdcca8777675fb27f8fce68fdc16f589cbc

### Enum

Values: Dry, Wet/Muddy, Flooded, Snow, Frozen, -----, High Tide, Low Tide, Heavy Surf/Swell

## RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200SkyItem
- Role: nested
- Parent: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200SkyItem
- Schema ID: schema:anon/e64182b5eef39d07d4743334ba0a6103b5b64e2d

### Fields

| Field | Type |
|------|------|
| `key` | `RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200SkyItemKey` |
| `value` | `string` |

## RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200SkyItemKey
- Role: nested
- Parent: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200SkyItemKey
- Schema ID: schema:anon/acf1ccb1070a6640444d8ffca4cf52336b91dcef

### Enum

Values: Clear, Cloudy, Overcast, Fog, Mist, Rain, Snow, Ice/Sleet/Hail, Smoke

## RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200TemperatureItem
- Role: nested
- Parent: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200TemperatureItem
- Schema ID: schema:anon/44c3114d8f76e5b254f96a1bc390631a5021d396

### Fields

| Field | Type |
|------|------|
| `key` | `RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200TemperatureItemKey` |
| `value` | `string` |

## RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200TemperatureItemKey
- Role: nested
- Parent: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200TemperatureItemKey
- Schema ID: schema:anon/01648afd2a92c97936c1632b5ca79e66605b763b

### Enum

Values: Very Hot, Hot, Mild, Cold, Very Cold

## RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200WindItem
- Role: nested
- Parent: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200WindItem
- Schema ID: schema:anon/68fa1d6cc614b1f9104c960c138fa585e78b6eba

### Fields

| Field | Type |
|------|------|
| `key` | `RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200WindItemKey` |
| `value` | `string` |

## RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200WindItemKey
- Role: nested
- Parent: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200DataObject
- Schema Name: RestV10ProjectsProjectIdDailyLogsWeatherConditionsGetResponse200WindItemKey
- Schema ID: schema:anon/5335a929a33b006aa07105a45da0278326d5be94

### Enum

Values: Calm, Light Wind, High Wind
