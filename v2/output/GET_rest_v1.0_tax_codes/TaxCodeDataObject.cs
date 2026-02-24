/// <summary>
/// No description
/// </summary>
[PrimaryKey("id", nameof(Id))] // [REVIEW: PrimaryKey auto-selected]
[Description("No description")]
public class TaxCodeDataObject
{
    [JsonPropertyName("id")]
    [Description("The ID of the Tax Code")]
    [Required]
    public required int Id { get; init; }

    [JsonPropertyName("code")]
    [Description("The Tax Code")]
    [Nullable(true)]
    public string? Code { get; init; }

    [JsonPropertyName("description")]
    [Description("Description of the Tax Code")]
    [Nullable(true)]
    public string? Description { get; init; }

    [JsonPropertyName("origin_data")]
    [Description("Additional Third-party Metadata for the Tax Code. Note: This is a free-form text field.")]
    [Nullable(true)]
    public string? OriginData { get; init; }

    [JsonPropertyName("origin_id")]
    [Description("The Third-party ID of the Tax Code")]
    [Nullable(true)]
    public string? OriginId { get; init; }

    [JsonPropertyName("rate1")]
    [Description("Rate to apply for first Tax Type")]
    [Nullable(true)]
    public double? Rate1 { get; init; }

    [JsonPropertyName("archived")]
    [Description("Set to true if this tax code has been archived")]
    [Nullable(true)]
    public bool? Archived { get; init; }

    [JsonPropertyName("default_tax_code")]
    [Description("Set to true if this tax code is default tax code")]
    [Nullable(true)]
    public bool? DefaultTaxCode { get; init; }
}