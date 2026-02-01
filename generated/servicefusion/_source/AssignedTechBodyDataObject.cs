/// <summary>
/// An assigned tech's body schema.
/// </summary>
[PrimaryKey("id", nameof(Id))]
[Description("An assigned tech's body schema.")]
public class AssignedTechBodyDataObject
{
    [JsonPropertyName("id")]
    [Description("Used to send the assigned tech's identifier that will be searched. If this field is set then the entry will be searched by it, otherwise the search will be performed by its full name.")]
    [Required]
    public required int Id { get; init; }

    [JsonPropertyName("first_name")]
    [Description("Used to send the assigned tech's first name that will be searched. Required field for full name search.")]
    [Nullable(true)]
    public string? FirstName { get; init; }

    [JsonPropertyName("last_name")]
    [Description("Used to send the assigned tech's last name that will be searched. Required field for full name search.")]
    [Nullable(true)]
    public string? LastName { get; init; }
}
