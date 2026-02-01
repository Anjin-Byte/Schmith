/// <summary>
/// A customer contact's body schema.
/// </summary>
[PrimaryKey("fname", nameof(Fname))] // [REVIEW: PrimaryKey auto-selected]
[Description("A customer contact's body schema.")]
public class CustomerContactBodyDataObject
{
    [JsonPropertyName("prefix")]
    [Description("Used to send the contact's prefix that will be set.")]
    [Nullable(true)]
    public string? Prefix { get; init; }

    [JsonPropertyName("fname")]
    [Description("Used to send the contact's first name that will be set.")]
    [Required]
    public required string Fname { get; init; }

    [JsonPropertyName("lname")]
    [Description("Used to send the contact's last name that will be set.")]
    [Required]
    public required string Lname { get; init; }

    [JsonPropertyName("suffix")]
    [Description("Used to send the contact's suffix that will be set.")]
    [Nullable(true)]
    public string? Suffix { get; init; }

    [JsonPropertyName("contact_type")]
    [Description("Used to send the contact's type that will be set.")]
    [Nullable(true)]
    public string? ContactType { get; init; }

    [JsonPropertyName("dob")]
    [Description("Used to send the contact's dob that will be set.")]
    [Nullable(true)]
    public string? Dob { get; init; }

    [JsonPropertyName("anniversary")]
    [Description("Used to send the contact's anniversary that will be set.")]
    [Nullable(true)]
    public string? Anniversary { get; init; }

    [JsonPropertyName("job_title")]
    [Description("Used to send the contact's job title that will be set.")]
    [Nullable(true)]
    public string? JobTitle { get; init; }

    [JsonPropertyName("department")]
    [Description("Used to send the contact's department that will be set.")]
    [Nullable(true)]
    public string? Department { get; init; }

    [JsonPropertyName("is_primary")]
    [Description("Used to send the contact's is primary flag that will be set. When it is passed as `true`, then the customer's existing primary contact (if any) will become secondary, and this one will become the primary one.")]
    [Nullable(true)]
    public bool? IsPrimary { get; init; }

    [JsonPropertyName("phones")]
    [Description("Used to send the contact's phones list that will be set.")]
    [Nullable(true)]
    public CustomerPhoneBody[]? Phones { get; init; }

    [JsonPropertyName("emails")]
    [Description("Used to send the contact's emails list that will be set.")]
    [Nullable(true)]
    public CustomerEmailBody[]? Emails { get; init; }
}

/// <summary>
/// A customer email's body schema.
/// </summary>
public class CustomerEmailBody
{
    [JsonPropertyName("email")]
    [Description("Used to send the email's address that will be set.")]
    [Required]
    public required string Email { get; init; }

    [JsonPropertyName("class")]
    [Description("Used to send the email's class that will be set.")]
    [Nullable(true)]
    public string? Class { get; init; }

    [JsonPropertyName("types_accepted")]
    [Description("Used to send the email's types accepted that will be set. Accepted value is comma-separated string.")]
    [Nullable(true)]
    public string? TypesAccepted { get; init; }
}

/// <summary>
/// A customer phone's body schema.
/// </summary>
public class CustomerPhoneBody
{
    [JsonPropertyName("phone")]
    [Description("Used to send the phone's number that will be set.")]
    [Required]
    public required string Phone { get; init; }

    [JsonPropertyName("ext")]
    [Description("Used to send the phone's extension that will be set.")]
    [Nullable(true)]
    public int? Ext { get; init; }

    [JsonPropertyName("type")]
    [Description("Used to send the phone's type that will be set.")]
    [Nullable(true)]
    public string? Type { get; init; }
}
