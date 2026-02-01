/// <summary>
/// An equipment's body schema.
/// </summary>
[PrimaryKey("id", nameof(Id))]
[Description("An equipment's body schema.")]
public class EquipmentBodyDataObject
{
    [JsonPropertyName("id")]
    [Description("Used to send the equipment's identifier that will be searched. You may pass this parameter if you do not want to create new entry but assign existing one. You may assign by `identifier` or `header` (Note: `identifier` - [integer] the equipment's identifier, `header` - [string] the equipment's fields concatenated by pattern `{type}:{make}:{model}:{serial_number}` with colon as separator).")]
    [Required]
    public required string Id { get; init; }

    [JsonPropertyName("type")]
    [Description("Used to send the equipment's type that will be set.")]
    [Nullable(true)]
    public string? Type { get; init; }

    [JsonPropertyName("make")]
    [Description("Used to send the equipment's make that will be set.")]
    [Nullable(true)]
    public string? Make { get; init; }

    [JsonPropertyName("model")]
    [Description("Used to send the equipment's model that will be set.")]
    [Nullable(true)]
    public string? Model { get; init; }

    [JsonPropertyName("sku")]
    [Description("Used to send the equipment's sku that will be set.")]
    [Nullable(true)]
    public string? Sku { get; init; }

    [JsonPropertyName("serial_number")]
    [Description("Used to send the equipment's serial number that will be set.")]
    [Nullable(true)]
    public string? SerialNumber { get; init; }

    [JsonPropertyName("location")]
    [Description("Used to send the equipment's location that will be set.")]
    [Nullable(true)]
    public string? Location { get; init; }

    [JsonPropertyName("notes")]
    [Description("Used to send the equipment's notes that will be set.")]
    [Nullable(true)]
    public string? Notes { get; init; }

    [JsonPropertyName("extended_warranty_provider")]
    [Description("Used to send the equipment's extended warranty provider that will be set.")]
    [Nullable(true)]
    public string? ExtendedWarrantyProvider { get; init; }

    [JsonPropertyName("is_extended_warranty")]
    [Description("Used to send the equipment's is extended warranty flag that will be set.")]
    [Nullable(true)]
    public bool? IsExtendedWarranty { get; init; }

    [JsonPropertyName("extended_warranty_date")]
    [Description("Used to send the equipment's extended warranty date that will be set.")]
    [Nullable(true)]
    public DateTime? ExtendedWarrantyDate { get; init; }

    [JsonPropertyName("warranty_date")]
    [Description("Used to send the equipment's warranty date that will be set.")]
    [Nullable(true)]
    public DateTime? WarrantyDate { get; init; }

    [JsonPropertyName("install_date")]
    [Description("Used to send the equipment's install date that will be set.")]
    [Nullable(true)]
    public DateTime? InstallDate { get; init; }

    [JsonPropertyName("customer_location")]
    [Description("Used to send a customer location's `id` or `header` that will be attached to the equipment (Note: `id` - [integer] the customer location's identifier, `header` - [string] the customer location's fields concatenated by pattern `{nickname} {street_1} {city}` with space as separator).")]
    [Nullable(true)]
    public string? CustomerLocation { get; init; }

    [JsonPropertyName("custom_fields")]
    [Description("Used to send the equipment's custom fields list that will be set.")]
    [Nullable(true)]
    public CustomFieldBody[]? CustomFields { get; init; }
}

/// <summary>
/// A custom field's body schema.
/// </summary>
public class CustomFieldBody
{
    [JsonPropertyName("name")]
    [Description("Used to send the custom field's name that will be set.")]
    [Required]
    public required string Name { get; init; }

    [JsonPropertyName("value")]
    [Description("Used to send the custom field's value that will be set.")]
    [Required]
    public required object Value { get; init; }
}
