# Objects and Serialization For Your Connector

Objects that are sent to the Xchange Platform are first serialized into JSON. Typically most cases there are no changes needed besides the use of [JsonPropertyName](#json-property-name).

For documentation on generation schema from objects refer to [Object Schema](../object-schema/).

## Available Attributes

Here are some attributes included by default that you may want to leverage. This list does not exhaust all of the built in attributes.

### JsonPropertyName Attribute

Like referenced in the [Object Schema](../object-schema/#jsonpropertyname-attribute) document.

Use this attribute to specify how the property should be named when serializing into JSON. This also gets used when deserializing from JSON into an instance of the class.

This attribute is useful in that it allows class properties to still follow C#'s property naming guideline of pascal casing even when the JSON representation is a different casing (or a mixture).

#### Usage of PropertyNameCaseInsensitive

In the context of using `JsonSerializerOptions` in integrations, it is not desired to ignore casing for property names. Properties should explicitly define their casing using `[JsonPropertyName]`. This approach ensures that the schema generated for the Connector metadata matches the target system, preventing integration issues.

Incorrect Usage:

```csharp
new JsonSerializerOptions
{
    PropertyNameCaseInsensitive = true
}
```

Correct Usage: Define the casing in the object properties:

```csharp
public class Example
{
    [JsonPropertyName("propertyName")]
    public string PropertyName { get; set; }
}
```

A Connector is represented on Xchange by its metadata, which includes the schema for data objects and action inputs/outputs. If the schema does not match the target system's output, it will result in integration issues due to an inaccurate contract. Explicitly defining property names ensures consistency and accuracy.

### JsonIgnore Attribute

This attribute can be used to avoid sending a null value to an optional property on the target system API. For example, if you had an optional property CategoryId that only accepted the type `string` and not `null` you could implement that as below:

```csharp
[JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
[JsonPropertyName("CategoryId")]
[Nullable(true)]
public string? categoryId { get; set; }
```

Note that the `JsonIgnore` attribute would still keep the property in schema, it is only used when serializing instances of the object.

### JsonStringEnumMemberName Attribute

Starting in version .NET 9 support for changing the string representation of a string was added. This attribute allows you to specify what the string values would be for the index of an enumeration.

Take the following for example:

```csharp
public enum ProjectStatus
{
    [JsonStringEnumMemberName("active")]
    Active,
    [JsonStringEnumMemberName("inactive")]
    Inactive
}
```

Given the above code snippet results when serializing property of type `ProjectStatus` it will produce strings

### JsonConverter

There are cases where you want to manipulate how the JSON is read or written. In order to do that a converter can be used and then reference using that converter on the desired property. You can find common examples below.

#### JsonStringEnumConverter Converter

It is very common to have objects with enums in it and wanting those enums when serialized/deserialized to use the string representation of them. Below is an example on how to do that via the use of `[JsonConverter(typeof(JsonStringEnumConverter))]`.

<details>
<summary>JsonStringEnumConverter Example</summary>

```csharp
[PrimaryKey("id", nameof(Id))]
[Description("Representation of a project in TargetSystemName")]
[AdditionalProperties(false)]
public class ProjectDataObject
{
    [JsonPropertyName("id")]
    [Description("Unique identifier property for a project")]
    public Guid Id { get; init; }

    [JsonPropertyName("status")]
    [Description("The current state of a project")]
    public ProjectStatus Status { get; init; } = ProjectStatus.Active;
}

[JsonConverter(typeof(JsonStringEnumConverter))]
public enum ProjectStatus
{
    [JsonStringEnumMemberName("active")]
    Active,
    [JsonStringEnumMemberName("inactive")]
    Inactive
}
```

</details>

#### Custom JsonConverters

For cases where you need more control on how to read and write values from properties you can create your own converter.

##### Different Types Between Systems

There are cases where the target system may have one type and when processing it on a Connector it should be another. For example maybe in the target system there is a property that is a high precision decimal. Thus while it is on the Xchange Platform you want it to be represented as a string. The converter would look as follows:

<details>
<summary>Number to String Converter Example</summary>

```csharp
public class NumberToStringConverter : JsonConverter<object>
{
    public override bool CanConvert(Type typeToConvert)
    {
        return typeof(string) == typeToConvert;
    }

    public override object Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        switch (reader.TokenType)
        {
            case JsonTokenType.Number:
                return reader.TryGetInt64(out var l)
                    ? l.ToString()
                    : reader.GetDouble().ToString(CultureInfo.InvariantCulture);
            case JsonTokenType.String:
                return reader.GetString() ?? string.Empty;
            default:
            {
                using var document = JsonDocument.ParseValue(ref reader);
                return document.RootElement.Clone().ToString();
            }
        }
    }

    public override void Write(Utf8JsonWriter writer, object value, JsonSerializerOptions options)
    {
        writer.WriteStringValue(value.ToString());
    }
}
```

</details>

Using it would then be as follows:

```csharp
[PrimaryKey("id", nameof(Id))]
[Description("Representation of a project in TargetSystemName")]
[AdditionalProperties(false)]
public class ProjectDataObject
{
    [JsonPropertyName("id")]
    [Description("Unique identifier property for a project")]
    public Guid Id { get; init; }

    [JsonPropertyName("cost")]
    [Description("How much the project costs")]
    [JsonConverter(typeof(NumberToStringConverter))]
    public string Cost { get; init; }
}
```

<details open>
<summary>Info</summary>

There is also a [JsonNumberHandling](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonnumberhandlingattribute) attribute which could be used in this scenario as well.

</details>

##### Skip Escaping and Encoding

Take for example having a string value with a non safe HTML character in it. By default the JsonSerializer will encode this character to its unicode representation. Below is an example converter to avoid doing such.

<details>
<summary>Write raw strings example</summary>

```csharp
public class WriteRawStringConverter : JsonConverter<string>
{
    public override string? Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options) => reader.GetString();

    public override void Write(Utf8JsonWriter writer, string value, JsonSerializerOptions options)
    {
        writer.WriteRawValue($"\"{value}\"");
    }
}
```

</details>

<details open>
<summary>Warning</summary>

In most cases this is not needed as escaped character or unicode equivalent will be handled by parsers automatically and rendered to end users as its expected representation. In other words, sending `\u0027` over the wire is equivalent as sending `'` for most cases.

</details>
