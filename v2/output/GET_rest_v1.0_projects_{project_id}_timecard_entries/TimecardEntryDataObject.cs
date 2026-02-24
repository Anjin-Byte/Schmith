/// <summary>
/// No description
/// </summary>
[Description("No description")]
public class TimecardEntryDataObject
{
    [JsonPropertyName("id")]
    [Description("ID")]
    [Nullable(true)]
    public int? Id { get; init; }

    [JsonPropertyName("billable")]
    [Description("The billable status of the timecard entry. Must be either true or false.")]
    [Nullable(true)]
    public bool? Billable { get; init; }

    [JsonPropertyName("created_at")]
    [Description("The date and time when the timecard entry was created.")]
    [Nullable(true)]
    public DateTime? CreatedAt { get; init; }

    [JsonPropertyName("date")]
    [Description("The date when the timecard was created.")]
    [Nullable(true)]
    public DateOnly? Date { get; init; }

    [JsonPropertyName("datetime")]
    [Description("The estimated UTC date time of record.")]
    [Nullable(true)]
    public DateTime? Datetime { get; init; }

    [JsonPropertyName("deleted_at")]
    [Description("The date and time when the timecard entry was deleted.")]
    [Nullable(true)]
    public DateTime? DeletedAt { get; init; }

    [JsonPropertyName("description")]
    [Description("The description for the timecard entry.")]
    [Nullable(true)]
    public string? Description { get; init; }

    [JsonPropertyName("hours")]
    [Description("Total number of hours the resource was on sight.")]
    [Nullable(true)]
    public string? Hours { get; init; }

    [JsonPropertyName("timesheet_status")]
    [Description("Deprecated. Reference status property.")]
    [Nullable(true)]
    public string? TimesheetStatus { get; init; }

    [JsonPropertyName("approval_status")]
    [Description("Supervisor approval status")]
    [Nullable(true)]
    public string? ApprovalStatus { get; init; }

    [JsonPropertyName("lunch_time")]
    [Description("Number of hours taken for lunch")]
    [Nullable(true)]
    public int? LunchTime { get; init; }

    [JsonPropertyName("time_in")]
    [Description("The date and time the timecard was last updated")]
    [Nullable(true)]
    public DateOnly? TimeIn { get; init; }

    [JsonPropertyName("time_out")]
    [Description("The date and time the timecard was last updated")]
    [Nullable(true)]
    public DateOnly? TimeOut { get; init; }

    [JsonPropertyName("injured")]
    [Description("Whether or not an injury occured during work hours. Must be either true or false.")]
    [Nullable(true)]
    public bool? Injured { get; init; }

    [JsonPropertyName("signed")]
    [Description("Whether or not the timecard has been signed. Must be either true or false.")]
    [Nullable(true)]
    public bool? Signed { get; init; }

    [JsonPropertyName("origin_id")]
    [Description("The ID of related external data")]
    [Nullable(true)]
    public int? OriginId { get; init; }

    [JsonPropertyName("origin_data")]
    [Description("The value of related external data")]
    [Nullable(true)]
    public string? OriginData { get; init; }

    [JsonPropertyName("timesheet")]
    [Description("")]
    [Nullable(true)]
    public Timesheet? Timesheet { get; init; }

    [JsonPropertyName("updated_at")]
    [Description("The date and time when the timesheet was updated.")]
    [Nullable(true)]
    public DateTime? UpdatedAt { get; init; }

    [JsonPropertyName("cost_code")]
    [Description("")]
    [Nullable(true)]
    public object? CostCode { get; init; } // [REVIEW: Type unresolved from IR]

    [JsonPropertyName("crew")]
    [Description("")]
    [Nullable(true)]
    public object? Crew { get; init; } // [REVIEW: Type unresolved from IR]

    [JsonPropertyName("location")]
    [Description("")]
    [Nullable(true)]
    public Location? Location { get; init; }

    [JsonPropertyName("party")]
    [Description("")]
    [Nullable(true)]
    public Party? Party { get; init; }

    [JsonPropertyName("procore_signature")]
    [Description("")]
    [Nullable(true)]
    public TimesheetsSignature? ProcoreSignature { get; init; }

    [JsonPropertyName("sub_job")]
    [Description("")]
    [Nullable(true)]
    public object? SubJob { get; init; } // [REVIEW: Type unresolved from IR]

    [JsonPropertyName("created_by")]
    [Description("")]
    [Nullable(true)]
    public object? CreatedBy { get; init; } // [REVIEW: Type unresolved from IR]

    [JsonPropertyName("login_information")]
    [Description("")]
    [Nullable(true)]
    public object? LoginInformation { get; init; } // [REVIEW: Type unresolved from IR]

    [JsonPropertyName("timecard_time_type")]
    [Description("")]
    [Nullable(true)]
    public TimecardTimeType? TimecardTimeType { get; init; }

    [JsonPropertyName("line_item_type_id")]
    [Description("The ID of the line item type of the timecard entry")]
    [Nullable(true)]
    public int? LineItemTypeId { get; init; }

    [JsonPropertyName("daily_log_segment_id")]
    [Description("Daily Log Segment ID")]
    [Nullable(true)]
    public int? DailyLogSegmentId { get; init; }

    [JsonPropertyName("custom_fields")]
    [Description("")]
    [Nullable(true)]
    public object? CustomFields { get; init; } // [REVIEW: Type unresolved from IR]

    [JsonPropertyName("automatically_split_timecard_entries")]
    [Description("Timecard entries returned with associated object as part of overtime_management")]
    [Nullable(true)]
    public TimecardEntry[]? AutomaticallySplitTimecardEntries { get; init; }
}