/// <summary>
/// No description
/// </summary>
[PrimaryKey("id", nameof(Id))] // [REVIEW: PrimaryKey auto-selected]
[Description("No description")]
public class TimesheetDataObject
{
    [JsonPropertyName("id")]
    [Description("ID")]
    [Required]
    public required int Id { get; init; }

    [JsonPropertyName("created_at")]
    [Description("Created at")]
    [Nullable(true)]
    public DateTime? CreatedAt { get; init; }

    [JsonPropertyName("updated_at")]
    [Description("Updated at")]
    [Nullable(true)]
    public DateTime? UpdatedAt { get; init; }

    [JsonPropertyName("date")]
    [Description("Timesheet date")]
    [Nullable(true)]
    public DateOnly? Date { get; init; }

    [JsonPropertyName("number")]
    [Description("Timesheet number")]
    [Nullable(true)]
    public int? Number { get; init; }

    [JsonPropertyName("created_by")]
    [Description("")]
    [Nullable(true)]
    public object? CreatedBy { get; init; } // [REVIEW: Type unresolved from IR]

    [JsonPropertyName("name")]
    [Description("Timesheet name")]
    [Nullable(true)]
    public string? Name { get; init; }

    [JsonPropertyName("status")]
    [Description("The approval status of the Timesheet")]
    [Nullable(true)]
    public string? Status { get; init; }

    [JsonPropertyName("timecard_entries")]
    [Description("")]
    [Nullable(true)]
    public TimesheetEntries[]? TimecardEntries { get; init; }
}