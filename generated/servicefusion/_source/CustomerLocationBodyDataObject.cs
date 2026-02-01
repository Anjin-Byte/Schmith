/// <summary>
/// A customer location's body schema.
/// </summary>
[PrimaryKey("street_1", nameof(Street1))] // [REVIEW: PrimaryKey auto-selected]
[Description("A customer location's body schema.")]
public class CustomerLocationBodyDataObject
{
    [JsonPropertyName("street_1")]
    [Description("Used to send the location's street 1 that will be set.")]
    [Required]
    public required string Street1 { get; init; }

    [JsonPropertyName("street_2")]
    [Description("Used to send the location's street 2 that will be set.")]
    [Nullable(true)]
    public string? Street2 { get; init; }

    [JsonPropertyName("city")]
    [Description("Used to send the location's city that will be set.")]
    [Nullable(true)]
    public string? City { get; init; }

    [JsonPropertyName("state_prov")]
    [Description("Used to send the location's state that will be set.")]
    [Nullable(true)]
    public string? StateProv { get; init; }

    [JsonPropertyName("postal_code")]
    [Description("Used to send the location's postal code that will be set.")]
    [Nullable(true)]
    public string? PostalCode { get; init; }

    [JsonPropertyName("country")]
    [Description("Used to send the location's country that will be set.")]
    [Nullable(true)]
    public string? Country { get; init; }

    [JsonPropertyName("nickname")]
    [Description("Used to send the location's nickname that will be set.")]
    [Nullable(true)]
    public string? Nickname { get; init; }

    [JsonPropertyName("gate_instructions")]
    [Description("Used to send the location's gate instructions that will be set.")]
    [Nullable(true)]
    public string? GateInstructions { get; init; }

    [JsonPropertyName("latitude")]
    [Description("Used to send the location's latitude that will be set.")]
    [Nullable(true)]
    public double? Latitude { get; init; }

    [JsonPropertyName("longitude")]
    [Description("Used to send the location's longitude that will be set.")]
    [Nullable(true)]
    public double? Longitude { get; init; }

    [JsonPropertyName("location_type")]
    [Description("Used to send the location's type that will be set.")]
    [Nullable(true)]
    public string? LocationType { get; init; }

    [JsonPropertyName("is_primary")]
    [Description("Used to send the location's is primary flag that will be set. When it is passed as `true`, then the customer's existing primary location (if any) will become secondary, and this one will become the primary one.")]
    [Nullable(true)]
    public bool? IsPrimary { get; init; }

    [JsonPropertyName("is_gated")]
    [Description("Used to send the location's `is gated` flag that will be set.")]
    [Nullable(true)]
    public bool? IsGated { get; init; }

    [JsonPropertyName("is_bill_to")]
    [Description("Used to send the location's is bill to flag that will be set.")]
    [Nullable(true)]
    public bool? IsBillTo { get; init; }

    [JsonPropertyName("customer_contact")]
    [Description("Used to send a customer contact's `id` or `header` that will be attached to the location (Note: `id` - [integer] the customer contact's identifier, `header` - [string] the customer contact's fields concatenated by pattern `{fname} {lname}` with space as separator).")]
    [Nullable(true)]
    public string? CustomerContact { get; init; }
}
