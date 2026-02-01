/// <summary>
/// An agent's body schema.
/// </summary>
[PrimaryKey("id", nameof(Id))]
[Description("An agent's body schema.")]
public class AgentBodyDataObject
{
    [JsonPropertyName("id")]
    [Description("Used to send the agent's identifier that will be searched. If this field is set then the entry will be searched by it, otherwise the search will be performed by its full name.")]
    [Required]
    public required int Id { get; init; }

    [JsonPropertyName("first_name")]
    [Description("Used to send the agent's first name that will be searched. Required field for full name search.")]
    [Nullable(true)]
    public string? FirstName { get; init; }

    [JsonPropertyName("last_name")]
    [Description("Used to send the agent's last name that will be searched. Required field for full name search.")]
    [Nullable(true)]
    public string? LastName { get; init; }
}
