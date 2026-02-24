# TimecardEntry

## TimecardEntry

- Schema ID: `schema:anon/21bb94936089b44e94b80a3c9c051ab5bcc3a439`
- Kind: unknown

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Billable` | `schema:types/boolean` |
| `CreatedAt` | `schema:types/datetime` |
| `Date` | `schema:types/date` |
| `Datetime` | `schema:types/datetime` |
| `DeletedAt` | `schema:types/datetime` |
| `Description` | `schema:types/string` |
| `Hours` | `schema:types/string` |
| `TimesheetStatus` | `schema:types/string` |
| `ApprovalStatus` | `schema:types/string` |
| `LunchTime` | `schema:types/integer` |
| `TimeIn` | `schema:types/date` |
| `TimeOut` | `schema:types/date` |
| `Injured` | `schema:types/boolean` |
| `Signed` | `schema:types/boolean` |
| `OriginId` | `schema:types/integer` |
| `OriginData` | `schema:types/string` |
| `Timesheet` | `Timesheet` |
| `UpdatedAt` | `schema:types/datetime` |
| `CostCode` | `TimecardEntryCostCode` |
| `Crew` | `TimecardEntryCrew` |
| `Location` | `Location` |
| `Party` | `Party` |
| `ProcoreSignature` | `TimesheetsSignature` |
| `SubJob` | `TimecardEntrySubJob` |
| `CreatedBy` | `TimesheetCreatedBy` |
| `LoginInformation` | `TimesheetCreatedBy` |
| `TimecardTimeType` | `TimecardTimeType` |
| `LineItemTypeId` | `schema:types/integer` |
| `DailyLogSegmentId` | `schema:types/integer` |
| `CustomFields` | `TimecardEntryCustomFields` |
| `AutomaticallySplitTimecardEntries` | `TimecardEntry[]` |

---

## Nested Types

### Anonymous_21bb9493Nested

- Schema ID: `schema:anon/fb7b44b095bd003aaca97261ac199ca9f9b633eb`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `AutomaticallySplitTimecardEntries` | `TimecardEntry[]` |

### EntryCustomFieldsCustomFieldBoolean

- Schema ID: `schema:anon/d7aaf7e4245f8b5e58720e73973a9fdbdbc7839e`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `DataType` | `schema:types/string` |
| `Value` | `schema:types/boolean` |

### EntryCustomFieldsCustomFieldDecimal

- Schema ID: `schema:anon/8178757753fe7302f7d5443936cb13b481bd73ff`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `DataType` | `schema:types/string` |
| `Value` | `schema:types/number` |

### EntryCustomFieldsCustomFieldLovEntries

- Schema ID: `schema:anon/d50bbe7063fb38ebfcc50625f772776d0020e2f7`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `DataType` | `schema:types/string` |
| `Value` | `LovEntriesValueNestedItem[]` |

### EntryCustomFieldsCustomFieldLovEntry

- Schema ID: `schema:anon/33d4a72922e5630c3242f8b04f6ee313e990b793`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `DataType` | `schema:types/string` |
| `Value` | `FieldLovEntryValue` |

### EntryCustomFieldsCustomFieldString

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

### Party

- Schema ID: `schema:anon/c2b1d340229e56b6ddbcd4f0909fcc8ef8e85a38`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |

### TimecardEntry

- Schema ID: `schema:anon/9dde5ef01ab66ff6a520ecea98059ef04ddef0f5`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Billable` | `schema:types/boolean` |
| `CreatedAt` | `schema:types/datetime` |
| `Date` | `schema:types/date` |
| `Datetime` | `schema:types/datetime` |
| `DeletedAt` | `schema:types/datetime` |
| `Description` | `schema:types/string` |
| `Hours` | `schema:types/string` |
| `TimesheetStatus` | `schema:types/string` |
| `ApprovalStatus` | `schema:types/string` |
| `LunchTime` | `schema:types/integer` |
| `TimeIn` | `schema:types/date` |
| `TimeOut` | `schema:types/date` |
| `Injured` | `schema:types/boolean` |
| `Signed` | `schema:types/boolean` |
| `OriginId` | `schema:types/integer` |
| `OriginData` | `schema:types/string` |
| `Timesheet` | `Timesheet` |
| `UpdatedAt` | `schema:types/datetime` |
| `CostCode` | `TimecardEntryCostCode` |
| `Crew` | `TimecardEntryCrew` |
| `Location` | `Location` |
| `Party` | `Party` |
| `ProcoreSignature` | `TimesheetsSignature` |
| `SubJob` | `TimecardEntrySubJob` |
| `CreatedBy` | `TimesheetCreatedBy` |
| `LoginInformation` | `TimesheetCreatedBy` |
| `TimecardTimeType` | `TimecardTimeType` |
| `LineItemTypeId` | `schema:types/integer` |
| `DailyLogSegmentId` | `schema:types/integer` |
| `CustomFields` | `TimecardEntryCustomFields` |

### TimecardEntryCostCode

- Schema ID: `schema:anon/7a7d890c7fa0b0fc15a34087ae7717936b876e3d`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |

### TimecardEntryCrew

- Schema ID: `schema:anon/0d3bbebb4e82dca70ea54506bfba795c4b1563af`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |
| `ProjectId` | `schema:types/integer` |
| `CompanyId` | `schema:types/integer` |
| `Employees` | `TimesheetCreatedBy[]` |
| `CreatedBy` | `TimesheetCreatedBy` |
| `Lead` | `TimesheetCreatedBy` |
| `CreatedAt` | `schema:types/datetime` |
| `UpdatedAt` | `schema:types/datetime` |

### TimecardEntryCustomFields

- Schema ID: `schema:anon/18c858aabec7b2c6828e2c316ea32d80e8f6c1be`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `CustomFieldString` | `EntryCustomFieldsCustomFieldString` |
| `CustomFieldDecimal` | `EntryCustomFieldsCustomFieldDecimal` |
| `CustomFieldBoolean` | `EntryCustomFieldsCustomFieldBoolean` |
| `CustomFieldLovEntry` | `EntryCustomFieldsCustomFieldLovEntry` |
| `CustomFieldLovEntries` | `EntryCustomFieldsCustomFieldLovEntries` |

### TimecardEntrySubJob

- Schema ID: `schema:anon/da0bb5f02a915c724ba132fd733aecd61215bb07`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |
| `Code` | `schema:types/string` |

### TimecardTimeType

- Schema ID: `schema:anon/5ff150fcfcc34bfb25ca814f2bab9dd2ad48f058`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `AbbreviatedTimeType` | `schema:types/string` |
| `CompanyId` | `schema:types/integer` |
| `Global` | `schema:types/boolean` |
| `TimeType` | `schema:types/string` |

### Timesheet

- Schema ID: `schema:anon/f40043c0c093953dfe6202058c748868281658d4`
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

### TimesheetCreatedBy

- Schema ID: `schema:anon/c01b825dffaac16200107c1b2b5fc05002120b9d`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Login` | `schema:types/string` |
| `Name` | `schema:types/string` |

### TimesheetsSignature

- Schema ID: `schema:anon/b47158c114ea748df4b65ed45d1666176d65265d`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `SignatureText` | `schema:types/string` |
| `FileName` | `schema:types/string` |
| `Url` | `schema:types/string` |
| `MediumThumbnailUrl` | `schema:types/string` |
| `LargeThumbnailUrl` | `schema:types/string` |
| `CreatedBy` | `TimesheetCreatedBy` |
