# Timesheet

## Timesheet

- Schema ID: `schema:anon/e4cf001eb598ba8eb4236b8c662fbaa081f02752`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `CreatedAt` | `schema:types/datetime` |
| `UpdatedAt` | `schema:types/datetime` |
| `Date` | `schema:types/date` |
| `Number` | `schema:types/integer` |
| `CreatedBy` | `TimesheetCreatedBy` |
| `Name` | `schema:types/string` |
| `Status` | `schema:types/string` |
| `TimecardEntries` | `TimesheetEntries[]` |

---

## Nested Types

### EntriesCustomFieldsCustomFieldBoolean

- Schema ID: `schema:anon/d7aaf7e4245f8b5e58720e73973a9fdbdbc7839e`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `DataType` | `schema:types/string` |
| `Value` | `schema:types/boolean` |

### EntriesCustomFieldsCustomFieldDecimal

- Schema ID: `schema:anon/8178757753fe7302f7d5443936cb13b481bd73ff`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `DataType` | `schema:types/string` |
| `Value` | `schema:types/number` |

### EntriesCustomFieldsCustomFieldLovEntries

- Schema ID: `schema:anon/d50bbe7063fb38ebfcc50625f772776d0020e2f7`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `DataType` | `schema:types/string` |
| `Value` | `LovEntriesValueNestedItem[]` |

### EntriesCustomFieldsCustomFieldLovEntry

- Schema ID: `schema:anon/33d4a72922e5630c3242f8b04f6ee313e990b793`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `DataType` | `schema:types/string` |
| `Value` | `FieldLovEntryValue` |

### EntriesCustomFieldsCustomFieldString

- Schema ID: `schema:anon/8c3d88cb61be32fb0e8459abd64e13d194ffdb10`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `DataType` | `schema:types/string` |
| `Value` | `schema:types/string` |

### FieldLovEntryValue

- Schema ID: `schema:anon/87cff48788164388a7c8910cf94ab26c21bee6e1`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Label` | `schema:types/string` |

### Location

- Schema ID: `schema:anon/7d4098f2df6d84102332d015429ec5ed48bef6c6`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |
| `NodeName` | `schema:types/string` |
| `ParentId` | `schema:types/integer` |
| `CreatedAt` | `schema:types/datetime` |
| `UpdatedAt` | `schema:types/datetime` |

### LovEntriesValueNestedItem

- Schema ID: `schema:anon/98dfbe72f61b8f25de0fb5b18d6fa8d9a4ec580a`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Label` | `schema:types/string` |

### TimecardTimeType

- Schema ID: `schema:anon/624e5b84c1ef324765d2f2603c1fb9e89c850e60`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `TimeType` | `schema:types/string` |
| `AbbreviatedTimeType` | `schema:types/string` |
| `Global` | `schema:types/boolean` |

### TimesheetCreatedBy

- Schema ID: `schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Login` | `schema:types/string` |
| `Name` | `schema:types/string` |

### TimesheetEntries

- Schema ID: `schema:anon/bec319389a4ae7e1faf450cc470f20ac379221c7`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `CreatedAt` | `schema:types/datetime` |
| `Date` | `schema:types/date` |
| `DeletedAt` | `schema:types/datetime` |
| `Description` | `schema:types/string` |
| `Hours` | `schema:types/string` |
| `UpdatedAt` | `schema:types/datetime` |
| `TimeIn` | `schema:types/datetime` |
| `TimeOut` | `schema:types/datetime` |
| `Injured` | `schema:types/boolean` |
| `LunchTime` | `schema:types/integer` |
| `Billable` | `schema:types/boolean` |
| `OriginId` | `schema:types/integer` |
| `OriginData` | `schema:types/string` |
| `Crew` | `TimesheetEntriesCrew` |
| `CostCode` | `TimesheetEntriesCostCode` |
| `CreatedBy` | `TimesheetCreatedBy` |
| `LoginInformation` | `TimesheetCreatedBy` |
| `Location` | `Location` |
| `TimecardTimeType` | `TimecardTimeType` |
| `WbsCodeId` | `schema:types/integer` |
| `CustomFields` | `TimesheetEntriesCustomFields` |

### TimesheetEntriesCostCode

- Schema ID: `schema:anon/7a7d890c7fa0b0fc15a34087ae7717936b876e3d`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |

### TimesheetEntriesCrew

- Schema ID: `schema:anon/1b84fbeda50b5c7abe4576ef5c771c87841511b4`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |

### TimesheetEntriesCustomFields

- Schema ID: `schema:anon/18c858aabec7b2c6828e2c316ea32d80e8f6c1be`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `CustomFieldString` | `EntriesCustomFieldsCustomFieldString` |
| `CustomFieldDecimal` | `EntriesCustomFieldsCustomFieldDecimal` |
| `CustomFieldBoolean` | `EntriesCustomFieldsCustomFieldBoolean` |
| `CustomFieldLovEntry` | `EntriesCustomFieldsCustomFieldLovEntry` |
| `CustomFieldLovEntries` | `EntriesCustomFieldsCustomFieldLovEntries` |
