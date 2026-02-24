/// <summary>
/// Company User
/// </summary>
[PrimaryKey("id", nameof(Id))] // [REVIEW: PrimaryKey auto-selected]
[Description("Company User")]
public class CompanyUserDataObject
{
    [JsonPropertyName("address")]
    [Description("User address")]
    [Nullable(true)]
    public string? Address { get; init; }

    [JsonPropertyName("avatar")]
    [Description("User avatar url")]
    [Nullable(true)]
    public string? Avatar { get; init; }

    [JsonPropertyName("business_id")]
    [Description("Business id")]
    [Nullable(true)]
    public string? BusinessId { get; init; }

    [JsonPropertyName("business_phone")]
    [Description("User business phone")]
    [Nullable(true)]
    public string? BusinessPhone { get; init; }

    [JsonPropertyName("business_phone_extension")]
    [Description("User business phone extension")]
    [Nullable(true)]
    public int? BusinessPhoneExtension { get; init; }

    [JsonPropertyName("city")]
    [Description("User city")]
    [Nullable(true)]
    public string? City { get; init; }

    [JsonPropertyName("contact_id")]
    [Description("User Contact ID")]
    [Nullable(true)]
    public int? ContactId { get; init; }

    [JsonPropertyName("country_code")]
    [Description("User country code (ISO-3166 Alpha-2 format)")]
    [Nullable(true)]
    public string? CountryCode { get; init; }

    [JsonPropertyName("created_at")]
    [Description("User created at")]
    [Nullable(true)]
    public DateTime? CreatedAt { get; init; }

    [JsonPropertyName("email_address")]
    [Description("User email")]
    [Nullable(true)]
    public string? EmailAddress { get; init; }

    [JsonPropertyName("email_signature")]
    [Description("User email signature")]
    [Nullable(true)]
    public string? EmailSignature { get; init; }

    [JsonPropertyName("employee_id")]
    [Description("User employee id")]
    [Nullable(true)]
    public string? EmployeeId { get; init; }

    [JsonPropertyName("erp_integrated_accountant")]
    [Description("User ERP integrated accountant status")]
    [Nullable(true)]
    public bool? ErpIntegratedAccountant { get; init; }

    [JsonPropertyName("fax_number")]
    [Description("User fax number")]
    [Nullable(true)]
    public string? FaxNumber { get; init; }

    [JsonPropertyName("first_name")]
    [Description("User first name")]
    [Nullable(true)]
    public string? FirstName { get; init; }

    [JsonPropertyName("id")]
    [Description("User id")]
    [Required]
    public required int Id { get; init; }

    [JsonPropertyName("initials")]
    [Description("User initials")]
    [Nullable(true)]
    public string? Initials { get; init; }

    [JsonPropertyName("is_active")]
    [Description("User active status")]
    [Nullable(true)]
    public bool? IsActive { get; init; }

    [JsonPropertyName("is_employee")]
    [Description("User employee status")]
    [Nullable(true)]
    public bool? IsEmployee { get; init; }

    [JsonPropertyName("job_title")]
    [Description("User job title")]
    [Nullable(true)]
    public string? JobTitle { get; init; }

    [JsonPropertyName("last_activated_at")]
    [Description("User last activated at")]
    [Nullable(true)]
    public DateTime? LastActivatedAt { get; init; }

    [JsonPropertyName("last_login_at")]
    [Description("User last login at")]
    [Nullable(true)]
    public DateTime? LastLoginAt { get; init; }

    [JsonPropertyName("last_name")]
    [Description("User last name")]
    [Nullable(true)]
    public string? LastName { get; init; }

    [JsonPropertyName("mobile_phone")]
    [Description("User mobile phone")]
    [Nullable(true)]
    public string? MobilePhone { get; init; }

    [JsonPropertyName("name")]
    [Description("User full name")]
    [Nullable(true)]
    public string? Name { get; init; }

    [JsonPropertyName("notes")]
    [Description("User notes")]
    [Nullable(true)]
    public string? Notes { get; init; }

    [JsonPropertyName("origin_id")]
    [Description("User origin id")]
    [Nullable(true)]
    public string? OriginId { get; init; }

    [JsonPropertyName("origin_data")]
    [Description("User origin data")]
    [Nullable(true)]
    public string? OriginData { get; init; }

    [JsonPropertyName("state_code")]
    [Description("User state code (ISO-3166 Alpha-2 format)")]
    [Nullable(true)]
    public string? StateCode { get; init; }

    [JsonPropertyName("updated_at")]
    [Description("User updated at")]
    [Nullable(true)]
    public DateTime? UpdatedAt { get; init; }

    [JsonPropertyName("welcome_email_sent_at")]
    [Description("User welcome email sent at")]
    [Nullable(true)]
    public DateTime? WelcomeEmailSentAt { get; init; }

    [JsonPropertyName("zip")]
    [Description("User zip code")]
    [Nullable(true)]
    public string? Zip { get; init; }

    [JsonPropertyName("work_classification_id")]
    [Description("Work classification id")]
    [Nullable(true)]
    public int? WorkClassificationId { get; init; }

    [JsonPropertyName("permission_template")]
    [Description("permission_template")]
    [Nullable(true)]
    public object? PermissionTemplate { get; init; } // [REVIEW: Type unresolved from IR]

    [JsonPropertyName("company_permission_template")]
    [Description("company_permission_template")]
    [Nullable(true)]
    public object? CompanyPermissionTemplate { get; init; } // [REVIEW: Type unresolved from IR]

    [JsonPropertyName("vendor")]
    [Description("vendor")]
    [Nullable(true)]
    public object? Vendor { get; init; } // [REVIEW: Type unresolved from IR]
}