namespace ServiceFusion.Common;

using Json.Schema.Generation;
using System.Text.Json.Serialization;

/// <summary>
/// Common classes for Service Fusion data objects.
/// </summary>

public class ServiceFusionEmail
{
    [JsonPropertyName("email")]
    [Description("Email address")]
    [Nullable(true)]
    [WriteOnly]
    public string? Email { get; init; }

    [JsonPropertyName("class")]
    [Description("Email class (e.g., Personal, Work)")]
    [Nullable(true)]
    public string? Class { get; init; }

    [JsonPropertyName("types_accepted")]
    [Description("Accepted email types (e.g., CONF, PMT)")]
    [Nullable(true)]
    public string? TypesAccepted { get; init; }

    [JsonPropertyName("created_at")]
    [Description("Created timestamp")]
    [Nullable(true)]
    public string? CreatedAt { get; init; }

    [JsonPropertyName("updated_at")]
    [Description("Updated timestamp")]
    [Nullable(true)]
    public string? UpdatedAt { get; init; }
}

public class ServiceFusionPhone
{
    [JsonPropertyName("phone")]
    [Description("Phone number")]
    [Nullable(true)]
    [WriteOnly]
    public string? Phone { get; init; }

    [JsonPropertyName("ext")]
    [Description("Phone extension")]
    [Nullable(true)]
    public int? Extension { get; init; }

    [JsonPropertyName("type")]
    [Description("Phone type (e.g., Mobile, Home)")]
    [Nullable(true)]
    public string? Type { get; init; }

    [JsonPropertyName("created_at")]
    [Description("Created timestamp")]
    [Nullable(true)]
    public string? CreatedAt { get; init; }

    [JsonPropertyName("updated_at")]
    [Description("Updated timestamp")]
    [Nullable(true)]
    public string? UpdatedAt { get; init; }

    [JsonPropertyName("is_mobile")]
    [Description("True if phone is mobile")]
    [Nullable(true)]
    public bool? IsMobile { get; init; }
}

public class ServiceFusionContact
{
    [JsonPropertyName("prefix")]
    [Description("Contact prefix")]
    [Nullable(true)]
    public string? Prefix { get; init; }

    [JsonPropertyName("fname")]
    [Description("Contact first name")]
    [Nullable(true)]
    [WriteOnly]
    public string? FirstName { get; init; }

    [JsonPropertyName("lname")]
    [Description("Contact last name")]
    [Nullable(true)]
    [WriteOnly]
    public string? LastName { get; init; }

    [JsonPropertyName("suffix")]
    [Description("Contact suffix")]
    [Nullable(true)]
    public string? Suffix { get; init; }

    [JsonPropertyName("contact_type")]
    [Description("Contact type (e.g., Billing)")]
    [Nullable(true)]
    public string? ContactType { get; init; }

    [JsonPropertyName("dob")]
    [Description("Contact date of birth")]
    [Nullable(true)]
    [WriteOnly]
    public string? DateOfBirth { get; init; }

    [JsonPropertyName("anniversary")]
    [Description("Contact anniversary")]
    [Nullable(true)]
    public string? Anniversary { get; init; }

    [JsonPropertyName("job_title")]
    [Description("Contact job title")]
    [Nullable(true)]
    public string? JobTitle { get; init; }

    [JsonPropertyName("department")]
    [Description("Contact department")]
    [Nullable(true)]
    public string? Department { get; init; }

    [JsonPropertyName("created_at")]
    [Description("Created timestamp")]
    [Nullable(true)]
    public string? CreatedAt { get; init; }

    [JsonPropertyName("updated_at")]
    [Description("Updated timestamp")]
    [Nullable(true)]
    public string? UpdatedAt { get; init; }

    [JsonPropertyName("is_primary")]
    [Description("True if this is the primary contact")]
    [Nullable(true)]
    public bool? IsPrimary { get; init; }

    [JsonPropertyName("phones")]
    [Description("Contact phone list")]
    [Nullable(true)]
    public ServiceFusionPhone[]? Phones { get; init; }

    [JsonPropertyName("emails")]
    [Description("Contact email list")]
    [Nullable(true)]
    public ServiceFusionEmail[]? Emails { get; init; }
}

public class ServiceFusionAddress
{
    [JsonPropertyName("street_1")]
    [Description("Street line 1")]
    [Nullable(true)]
    [WriteOnly]
    public string? Street1 { get; init; }

    [JsonPropertyName("street_2")]
    [Description("Street line 2")]
    [Nullable(true)]
    [WriteOnly]
    public string? Street2 { get; init; }

    [JsonPropertyName("city")]
    [Description("City")]
    [Nullable(true)]
    [WriteOnly]
    public string? City { get; init; }

    [JsonPropertyName("state_prov")]
    [Description("State or province")]
    [Nullable(true)]
    public string? StateProvince { get; init; }

    [JsonPropertyName("postal_code")]
    [Description("Postal code")]
    [Nullable(true)]
    [WriteOnly]
    public string? PostalCode { get; init; }

    [JsonPropertyName("country")]
    [Description("Country")]
    [Nullable(true)]
    public string? Country { get; init; }

    [JsonPropertyName("nickname")]
    [Description("Location nickname")]
    [Nullable(true)]
    public string? Nickname { get; init; }

    [JsonPropertyName("gate_instructions")]
    [Description("Gate instructions")]
    [Nullable(true)]
    public string? GateInstructions { get; init; }

    [JsonPropertyName("latitude")]
    [Description("Latitude")]
    [Nullable(true)]
    public float? Latitude { get; init; }

    [JsonPropertyName("longitude")]
    [Description("Longitude")]
    [Nullable(true)]
    public float? Longitude { get; init; }

    [JsonPropertyName("location_type")]
    [Description("Location type (e.g., home, work)")]
    [Nullable(true)]
    public string? LocationType { get; init; }

    [JsonPropertyName("created_at")]
    [Description("Created timestamp")]
    [Nullable(true)]
    public string? CreatedAt { get; init; }

    [JsonPropertyName("updated_at")]
    [Description("Updated timestamp")]
    [Nullable(true)]
    public string? UpdatedAt { get; init; }

    [JsonPropertyName("is_primary")]
    [Description("True if this is the primary location")]
    [Nullable(true)]
    public bool? IsPrimary { get; init; }

    [JsonPropertyName("is_gated")]
    [Description("True if location is gated")]
    [Nullable(true)]
    public bool? IsGated { get; init; }

    [JsonPropertyName("is_bill_to")]
    [Description("True if location is bill-to")]
    [Nullable(true)]
    public bool? IsBillTo { get; init; }

    [JsonPropertyName("customer_contact")]
    [Description("Primary contact name for location")]
    [Nullable(true)]
    public string? CustomerContact { get; init; }
}
