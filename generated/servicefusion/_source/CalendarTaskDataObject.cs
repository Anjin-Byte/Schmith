/// <summary>
/// A calendar task's schema.
/// </summary>
[PrimaryKey("id", nameof(Id))]
[Description("A calendar task's schema.")]
public class CalendarTaskDataObject
{
    [JsonPropertyName("id")]
    [Description("The calendar task's identifier.")]
    [Required]
    public required int Id { get; init; }

    [JsonPropertyName("type")]
    [Description("The calendar task's type.")]
    [Nullable(true)]
    public string? Type { get; init; }

    [JsonPropertyName("description")]
    [Description("The calendar task's description.")]
    [Nullable(true)]
    public string? Description { get; init; }

    [JsonPropertyName("start_time")]
    [Description("The calendar task's start time.")]
    [Nullable(true)]
    public string? StartTime { get; init; }

    [JsonPropertyName("end_time")]
    [Description("The calendar task's end time.")]
    [Nullable(true)]
    public string? EndTime { get; init; }

    [JsonPropertyName("start_date")]
    [Description("The calendar task's start date.")]
    [Nullable(true)]
    public DateTime? StartDate { get; init; }

    [JsonPropertyName("end_date")]
    [Description("The calendar task's end date.")]
    [Nullable(true)]
    public DateTime? EndDate { get; init; }

    [JsonPropertyName("created_at")]
    [Description("The calendar task's created date.")]
    [Nullable(true)]
    public DateTime? CreatedAt { get; init; }

    [JsonPropertyName("updated_at")]
    [Description("The calendar task's updated date.")]
    [Nullable(true)]
    public DateTime? UpdatedAt { get; init; }

    [JsonPropertyName("is_public")]
    [Description("The calendar task's is public flag.")]
    [Nullable(true)]
    public bool? IsPublic { get; init; }

    [JsonPropertyName("is_completed")]
    [Description("The calendar task's is completed flag.")]
    [Nullable(true)]
    public bool? IsCompleted { get; init; }

    [JsonPropertyName("repeat_id")]
    [Description("The calendar task's repeat id.")]
    [Nullable(true)]
    public int? RepeatId { get; init; }

    [JsonPropertyName("users_id")]
    [Description("The calendar task's users list of identifiers.")]
    [Required]
    public required int[] UsersId { get; init; }

    [JsonPropertyName("customers_id")]
    [Description("The calendar task's customers list of identifiers.")]
    [Required]
    public required int[] CustomersId { get; init; }

    [JsonPropertyName("jobs_id")]
    [Description("The calendar task's jobs list of identifiers.")]
    [Required]
    public required int[] JobsId { get; init; }

    [JsonPropertyName("estimates_id")]
    [Description("The calendar task's estimates list of identifiers.")]
    [Required]
    public required int[] EstimatesId { get; init; }

    [JsonPropertyName("repeat")]
    [Description("The calendar task's repeat.")]
    [Nullable(true)]
    public CalendarTaskRepeat? Repeat { get; init; }
}

/// <summary>
/// A calendar task repeat's schema.
/// </summary>
public class CalendarTaskRepeat
{
    [JsonPropertyName("id")]
    [Description("The repeat's identifier.")]
    [Nullable(true)]
    public int? Id { get; init; }

    [JsonPropertyName("repeat_type")]
    [Description("The repeat's type.")]
    [Nullable(true)]
    public string? RepeatType { get; init; }

    [JsonPropertyName("repeat_frequency")]
    [Description("The repeat's frequency.")]
    [Nullable(true)]
    public int? RepeatFrequency { get; init; }

    [JsonPropertyName("repeat_weekly_days")]
    [Description("The repeat's weekly days list.")]
    [Required]
    public required string[] RepeatWeeklyDays { get; init; }

    [JsonPropertyName("repeat_monthly_type")]
    [Description("The repeat's monthly type.")]
    [Nullable(true)]
    public string? RepeatMonthlyType { get; init; }

    [JsonPropertyName("stop_repeat_type")]
    [Description("The repeat's stop type.")]
    [Nullable(true)]
    public string? StopRepeatType { get; init; }

    [JsonPropertyName("stop_repeat_on_occurrence")]
    [Description("The repeat's stop on occurrence.")]
    [Nullable(true)]
    public int? StopRepeatOnOccurrence { get; init; }

    [JsonPropertyName("stop_repeat_on_date")]
    [Description("The repeat's stop on date.")]
    [Nullable(true)]
    public DateTime? StopRepeatOnDate { get; init; }

    [JsonPropertyName("start_date")]
    [Description("The repeat's start date.")]
    [Nullable(true)]
    public DateTime? StartDate { get; init; }

    [JsonPropertyName("end_date")]
    [Description("The repeat's end date.")]
    [Nullable(true)]
    public DateTime? EndDate { get; init; }
}
