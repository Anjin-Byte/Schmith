# CompanyUser

## CompanyUser

Company User

- Schema ID: `schema:anon/2bea3e351c3415087b489a156353354ea381eeb9`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Address` | `schema:types/string` |
| `Avatar` | `schema:types/string` |
| `BusinessId` | `schema:types/string` |
| `BusinessPhone` | `schema:types/string` |
| `BusinessPhoneExtension` | `schema:types/integer` |
| `City` | `schema:types/string` |
| `ContactId` | `schema:types/integer` |
| `CountryCode` | `schema:types/string` |
| `CreatedAt` | `schema:types/datetime` |
| `EmailAddress` | `schema:types/string` |
| `EmailSignature` | `schema:types/string` |
| `EmployeeId` | `schema:types/string` |
| `ErpIntegratedAccountant` | `schema:types/boolean` |
| `FaxNumber` | `schema:types/string` |
| `FirstName` | `schema:types/string` |
| `Id` | `schema:types/integer` |
| `Initials` | `schema:types/string` |
| `IsActive` | `schema:types/boolean` |
| `IsEmployee` | `schema:types/boolean` |
| `JobTitle` | `schema:types/string` |
| `LastActivatedAt` | `schema:types/datetime` |
| `LastLoginAt` | `schema:types/datetime` |
| `LastName` | `schema:types/string` |
| `MobilePhone` | `schema:types/string` |
| `Name` | `schema:types/string` |
| `Notes` | `schema:types/string` |
| `OriginId` | `schema:types/string` |
| `OriginData` | `schema:types/string` |
| `StateCode` | `schema:types/string` |
| `UpdatedAt` | `schema:types/datetime` |
| `WelcomeEmailSentAt` | `schema:types/datetime` |
| `Zip` | `schema:types/string` |
| `WorkClassificationId` | `schema:types/integer` |
| `PermissionTemplate` | `CompanyUserPermissionTemplate` |
| `CompanyPermissionTemplate` | `CompanyUserPermissionTemplate` |
| `Vendor` | `CompanyUserVendor` |

---

## Nested Types

### CompanyUserPermissionTemplate

- Schema ID: `schema:anon/cb2b399883077d55c5ecd2277c77fe2a599c10e8`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |
| `ProjectSpecific` | `schema:types/boolean` |
| `Type` | `UserPermissionTemplateType` |

### CompanyUserVendor

- Schema ID: `schema:anon/bdbc967ef89c11cac60241a5dcf6df780325d1d8`
- Kind: object

### Fields

| C# Property | Resolved Type |
|-------------|--------------|
| `Id` | `schema:types/integer` |
| `Name` | `schema:types/string` |

### UserPermissionTemplateType

The type of the Permission Template

- Schema ID: `schema:anon/601a069b104f181a867c3475152231333b188f20`
- Kind: string

### Enum Values

- `company_tools`
- `global`
- `project_specific`
