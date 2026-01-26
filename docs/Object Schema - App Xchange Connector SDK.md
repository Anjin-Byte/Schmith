# Objects and Schemas For Your Connector

This guide will help you understand the various objects that a connector will provide and how to properly attribute them in your connector. You can always run `xchange extract` command to view the schemas being generated locally before being submitted to Xchange (via the `connector.json` file). 

**Please read this guide in its entirety as missing or improper attributes represent a common reason a submission is rejected.**

For documentation on serializing objects into JSON refer to [Object Serialization](../object-serialization/).

## Data Uniqueness and the Primary Key Attribute

Data objects in a Connector acts as a representation of resources on the target system. Xchange needs to be able to uniquely identify records coming from the target system in order to be able to support change detection and give users of the Connector a reliable way to look up records when supporting integration logic.

The way records are uniquely identified is through the use of its respective data object's key definition via the `PrimaryKey` attribute.

### Defining a Key

When defining a key for a data object it should be composed of properties that are not optional or nullable. Ideally you use the same property(s) that is used by your system for tenanting uniqueness. Take the following record for example of an `Employee` resource.

```
{
    "id": 123,
    "firstName": "John",
    "middleName": null,
    "lastName": "Smith"
}

```

When it comes to defining your data object it could look as follows

```
// The first argument specifies the name of the key. Subsequent arguments define the properties that make up the key.  
// Alternatively, you can use the nameof operator to reference the property, e.g., nameof(Id).
[PrimaryKey("id", "id")]
[Description("The representation of an employee")]
public class EmployeeDataObject
{
    [Required]
    public required long Id { get; init; }
    [Required]
    public required string FirstName { get; init; }
    [Nullable(true)]
    public string? MiddleName { get; init; }
    [Required]
    public required string LastName { get; init; }
}

```

**A Note About Property Names**

The values used for property names should be in the casing that they are when serialized into JSON

In this case here the name of the data object key is called `id` and it is composed of the `Id` property. The name of the key provides a way to identify the key as it is possible to define multiple keys on a single data object definition. 

Simply using `id` as the name on all `PrimaryKey` attributes on each defined data object is fine.

#### Composite Keys

It is possible to not be able to define uniqueness from only one property and instead need to compose multiple properties together to do so. Take for example a employee record again but this time the records are tenanted by a division and each division has their own identifier. A record could look like as follows:

```
{
    "id": 123,
    "division": "accounting",
    "firstName": "John",
    "middleName": null,
    "lastName": "Smith"
}

```

We would then want its key to resolve as `id/accounting/123`. To do that we would define our data object as follows:

```
[PrimaryKey("id", "division", "id")]
[Description("The representation of an employee")]
public class EmployeeDataObject
{
    [Required]
    public required long Id { get; init; }
    [Required]
    public required string Division { get; init; }
    [Required]
    public required string FirstName { get; init; }
    [Nullable(true)]
    public string? MiddleName { get; init; }
    [Required]
    public required string LastName { get; init; }
}

```

#### Alternate Keys

An Alternate Key is any key that is not the primary key. A composite key is a common use case for an alternate key. Consider the following options for an Employees data object: 

```
[PrimaryKey("id", nameof(Id))]
//[AlternateKey("naturalKey", nameof(FirstName), nameof(LastName))] // composite alternate key example
[AlternateKey("ssn", nameof(Ssn))] // unique property alternate key example 
[Description("Represents an Employee")]
public class EmployeesDataObject
{
    [JsonPropertyName("id")]
    [Description("Example primary key of the object")]
    [Required]
    public required string Id { get; init; }

    [JsonPropertyName("firstName")]
    [Description("First name of the employee")]
    [Required]
    public string FirstName { get; set; }

    [JsonPropertyName("lastName")]
    [Description("Surname of the employee")]
    [Required]
    public string LastName { get; set; }

    [JsonPropertyName("ssn")]
    [Description("ssn of the employee")]
    [Required]
    public string Ssn { get; set; }

```

## Available Attributes

The main JSON attributes we provide fall into two categories: metadata and validation. The metadata attributes are more for clarity in terms of how the properties are represented and what they are for. The validation attributes are used for validating that the data that is provided for the objects meets the requirements of what should be provided. These attributes should be on BOTH data object and action schemas. 

This is not exhaustive, but it provides the most common use cases. For more see [json-everything's Schema Generation](https://docs.json-everything.net/schema/schemagen/schema-generation/)

### Metadata Attributes

- Title: The title attribute gives us a value that can be used in place of the property name. Used to improve readability if the property name is abbreviated or lacking context to the property or class.
- Description: The description attribute gets used to give the user more information on what the property is, hopefully making it more clear how to populate it.
- JsonPropertyName: Allows you to override the property name that will be chosen when the object gets serialized to JSON. (Only for properties)

An Example of the usage of the attributes on an object and a property:

```
[Title("Equipment V1 Action Processor Configuration")]
[Description("Configuration of the data object actions for the module.")]
public class EquipmentV1ActionProcessorConfig
{
    [Title("Add Equipment Action handler Configuration")]
    [Description("Configuration object for the add equipment action.")]
    [JsonPropertyName("addEquipmentConfig")]
    public AddEquipmentHandlerConfig AddEquipmentConfig { get; init; }
}

```

#### JsonPropertyName Attribute

You should also keep in mind that due to the nature of JSON Serialization, if you don't set a desired `JsonPropertyName` to your properties with a specific casing, they will be cast into camelCase by default when the metadata is extracted.

According to the [json-everything's Schema Generation documentation](https://docs.json-everything.net/schema/schemagen/schema-generation/), the commonly-used casing conventions are:

- camelCase
- PascalCase
- kebab-case
- UPPER-KEBAB-CASE
- snake_case
- UPPER_SNAKE_CASE

If you want your properties to keep a specific casing, the `JsonPropertyName` can help you with that.

```
[JsonPropertyName("AddEquipmentConfig")] // PascalCase example
public AddEquipmentHandlerConfig AddEquipmentConfig { get; init; }

[JsonPropertyName("add-equipment-config")] // kebab-case example
public AddEquipmentHandlerConfig AddEquipmentConfig { get; init; }

[JsonPropertyName("ADD-EQUIPMENT-CONFIG")] // UPPER-KEBAB-CASE example
public AddEquipmentHandlerConfig AddEquipmentConfig { get; init; }

[JsonPropertyName("add_equipment_config")] // snake_case example
public AddEquipmentHandlerConfig AddEquipmentConfig { get; init; }

[JsonPropertyName("ADD_EQUIPMENT_CONFIG")] // UPPER_SNAKE_CASE example
public AddEquipmentHandlerConfig AddEquipmentConfig { get; init; }

```

##### Usage of PropertyNameCaseInsensitive

Refer to [Object Serialization](../object-serialization/#usage-of-propertynamecaseinsensitive) for more information on usage of `PropertyNameCaseInsensitive`.

#### Nullable Attribute

Can be set to tell whether or not the property can be nullable. By default the JSON schema generation sets the properties to not be nullable. Even if you mark the property type with a `?` to indicate it is nullable at compile time, you will still need to set this attribute to true on the property for the schema generation to recognize it as nullable.

```
[Nullable(true)]
public Guid? CategoryId { get; set; }

```

#### JsonIgnore Attribute

Moved to [Object Serialization](../object-serialization/#jsonignore-attribute).

#### Required Attribute

There may be properties on your object that have to be provided, such as a property used as record's identifier or when creating/updating (action input) a record on your system.

```
[Required]
public Guid Id { get; set; }

[Required]
public required string FirstName { get; set; }
[Nullable(true)]
public string? MiddleName { get; set; }
[Required]
public required string LastName { get; set; }

```

#### C# types vs Json annotations

It can be easy to confuse or overmatch the C# type and the Json annotations. A property may have the "[Required]" attribute for platform validation but not the [Required type](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/required) for example, which will make using it for data object inheritance and initialization easier. In the example above, the Guid `Id` will be required on the platform, but the object can be initialized without setting the `Id` property. 

### WriteOnly Attribute

Your data objects may contain sensitive financial or personally identifiable information. This attribute **must** be added to such properties to obscure the data on the App Xchange platform and enhance security. Such data will be replaced with "--hidden value--" when viewed on App Xchange, though it can be revealed with appropriate permissions, and will **not** prevent use in flow. See our [Best Practices Guide](../best-practices/#mark-all-personally-identifiable-information-pii-and-financially-sensitive-information-with-the-writeonly-attribute) for which properties require this attribute. See the following example: 

```
[WriteOnly]
public int PassportNumber { get; set; }

```

### Validation Attributes

Below is an outline of additional attributes that can be used to further enforce business logic you may have on your objects. This is not an exhaustive list of everything possible. You can view the library's documentation for [more usages](https://docs.json-everything.net/schema/schemagen/schema-generation/#schema-schemagen-best-practices)

#### String Validation Attributes

- MaxLength(int): Allows a maximum length to be set for the property
- MinLength(int): Allows a minimum length to be set for the property
- Pattern(string): Allows a regex to be applied to a property to make sure that the value matches the pattern.

```
[MaxLength(5), MinLength(3)]
public string CostCenter { get; set; }

[Pattern(@"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$")]
public string PhoneNumber { get; set; }

```

#### Number Validation Attributes

- Maximum: Sets the maximum value a property can be set to.
- Minimum: Sets the minimum value a property can be set to.

```
[Maximum(500), Minimum(1)]
public int Length { get; set; }

```

## Objects to Attribute

Connectors work on different kinds of resources:

- Data Objects
- Action Objects
- Service Configuration
- Connection Registration Configuration

Below is a brief overview of these resources

### Data Objects

For the data objects that are uploaded into the cache, the schema is used for validation that it is properly formed before it's entered into the cache. In addition it should mean that all data in the cache matches the schema.

> 

Schema validation happens on the Xchange platform when ingesting new records.

### Action Objects

For your action objects, the ones that implement the `IAction<>` interface, the reference types that are used for the input, output, and failure cases. All of these will be validated when passed to the Xchange platform. It will allow you and your integrators to know when any of the objects are not properly formed.

In addition to the validation, the metadata attributes will help those building integrations or testing flows better understand what the properties are for.

> 

Schema validation happens on the Xchange platform when queuing or closing out an action instance.

### Service Configuration

The service configurations are created when an new module is created for your connector, and there will be one for each type of service: Cache writer configuration and Action Processor configuration

Similar to the [Connector Registration Configuration](#connector-registration-configuration) in that the title and description are used for clarity, and validation is used to make sure that the service is properly configured prior to execution. Some additional notes on both kinds of configuration are below:

#### Cache Writer

This configuration by default will contain a `Configuration` property for each data object of type CacheWriterObjectConfig. If you want to allow more configuration for your data objects, you can extend this configuration type and add additional properties. 

The `CacheWriterObjectConfig` property is necessary because it provides a property `UploadObject` that gives the user with a way to enable/disable that particular data object's cache writer from uploading data to the cache. A connector may contain a large number of data objects, and it's quite possible an integration is only going to need a subset of those objects. This allows the data types to be turned off to limit the amount of data uploaded into the Xchange platform.

```
public class EquipmentV1CacheWriterConfig
{
    // Data Reader configuration
    [Title("Equipment")]
    public CacheWriterObjectConfig EquipmentConfig { get; set; } = new();
}

```

#### Action Processor

This configuration by default will contain a `Configuration` property for each action of each data object of type `DefaultActionHandlerConfig`. If you want to allow more configuration for your data objects, you can extend this configuration type and add additional properties. 

The DefaultActionHandlerConfig property is necessary because it provides a property `ProcessQueuedEvent` that gives the user with a way to enable/disable that particular action from being performed by the system. A connector may contain a large number of actions for the data objects, and it's quite possible an integration is only going to need a subset of those actions. This allows the actions to be turned off to limit the amount of data processed in the Xchange platform.

```
public class EquipmentV1ActionProcessorConfig
{
    // Action Handler configuration
    [Title("Add Equipment Action handler Configuration")]
    public DefaultActionHandlerConfig AddEquipmentConfig { get; set; } = new();
}

```

#### Connector Registration Configuration

This object is generated on new Connectors. It can be used to define configurations that are scoped by workspaces.

The [Validation attributes](#validation-attributes) will be used to validate the supplied configuration against the schema prior to it being used. An invalid configuration will stop the Connector from fully starting with error messages indicating what was invalid in the configuration.

### Dynamic Types

There are changes where your resource may contain a property in which the type is dynamic. 

#### Hash Maps

For example you may have a data object with an optional property `CustomFields` and Custom fields on your system is just a hash map of string keys with values also being strings. In which case your data object for this property would look as follows:

```
[Nullable(true)]
public Dictionary<string, string>? CustomFields { get;init; }

```

This would produce the following schema on our platform:

```
"CustomFields": {
    "type": [
        "object",
        "null"
        ],
    "additionalProperties": {
        "type": "string"
    }
}

```

**Non String Hash Map Values**

If your hash map values aren't just `string`s then you can change the property to `Dictionary<string, object>` as this will allow for any kind of value for each key.

This would produce a schema that looks as follows:

```
"CustomFields": {
    "type": [
        "object",
        "null"
        ],
    "additionalProperties": true
}

```

#### Fully Dynamic

If you set a property with a type of `object` then this produces a schema that can be anything. Doing so is not desired as it is unlikely that your target system has a record that has no structure as part of its business logic.

For example if your property on the CSharp model is as follows:

```
public object? CustomFields { get; init; }

```

This would produce the JSON schema:

```
"CustomFields": true

```

This means that the CustomFields property can be anything (null, object, array, bool, number, etc)

It is important that your schemas present what your target system produces so that integrations built with it can can more true to your available APIs.
January 14, 2026January 14, 2026
