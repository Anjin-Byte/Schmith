/// <summary>
/// A customer's schema.
/// </summary>
[PrimaryKey("id", nameof(Id))]
[Description("A customer's schema.")]
public class CustomerDataObject
{
    [JsonPropertyName("id")]
    [Description("The customer's identifier.")]
    [Required]
    public required int Id { get; init; }

    [JsonPropertyName("customer_name")]
    [Description("The customer's name.")]
    [Nullable(true)]
    public string? CustomerName { get; init; }

    [JsonPropertyName("fully_qualified_name")]
    [Description("The customer's fully qualified name.")]
    [Nullable(true)]
    public string? FullyQualifiedName { get; init; }

    [JsonPropertyName("parent_customer")]
    [Description("The `header` of attached parent customer to the customer (Note: `header` - [string] the parent customer's fields concatenated by pattern `{first_name} {last_name}` with space as separator).")]
    [Nullable(true)]
    public string? ParentCustomer { get; init; }

    [JsonPropertyName("account_number")]
    [Description("The customer's account number.")]
    [Nullable(true)]
    public string? AccountNumber { get; init; }

    [JsonPropertyName("account_balance")]
    [Description("The customer's account balance.")]
    [Nullable(true)]
    public double? AccountBalance { get; init; }

    [JsonPropertyName("private_notes")]
    [Description("The customer's private notes.")]
    [Nullable(true)]
    public string? PrivateNotes { get; init; }

    [JsonPropertyName("public_notes")]
    [Description("The customer's public notes.")]
    [Nullable(true)]
    public string? PublicNotes { get; init; }

    [JsonPropertyName("credit_rating")]
    [Description("The customer's credit rating.")]
    [Nullable(true)]
    public string? CreditRating { get; init; }

    [JsonPropertyName("labor_charge_type")]
    [Description("The customer's labor charge type.")]
    [Nullable(true)]
    public string? LaborChargeType { get; init; }

    [JsonPropertyName("labor_charge_default_rate")]
    [Description("The customer's labor charge default rate.")]
    [Nullable(true)]
    public double? LaborChargeDefaultRate { get; init; }

    [JsonPropertyName("last_serviced_date")]
    [Description("The customer's last serviced date.")]
    [Nullable(true)]
    public DateTime? LastServicedDate { get; init; }

    [JsonPropertyName("is_bill_for_drive_time")]
    [Description("The customer's is bill for drive time flag.")]
    [Nullable(true)]
    public bool? IsBillForDriveTime { get; init; }

    [JsonPropertyName("is_vip")]
    [Description("The customer's is vip flag.")]
    [Nullable(true)]
    public bool? IsVip { get; init; }

    [JsonPropertyName("referral_source")]
    [Description("The `header` of attached referral source to the customer (Note: `header` - [string] the referral source's fields concatenated by pattern `{short_name}`).")]
    [Nullable(true)]
    public string? ReferralSource { get; init; }

    [JsonPropertyName("agent")]
    [Description("The `header` of attached agent to the customer (Note: `header` - [string] the agent's fields concatenated by pattern `{first_name} {last_name}` with space as separator).")]
    [Nullable(true)]
    public string? Agent { get; init; }

    [JsonPropertyName("discount")]
    [Description("The customer's discount.")]
    [Nullable(true)]
    public double? Discount { get; init; }

    [JsonPropertyName("discount_type")]
    [Description("The customer's discount type.")]
    [Nullable(true)]
    public string? DiscountType { get; init; }

    [JsonPropertyName("payment_type")]
    [Description("The `header` of attached payment type to the customer (Note: `header` - [string] the payment type's fields concatenated by pattern `{name}`).")]
    [Nullable(true)]
    public string? PaymentType { get; init; }

    [JsonPropertyName("payment_terms")]
    [Description("The customer's payment terms.")]
    [Nullable(true)]
    public string? PaymentTerms { get; init; }

    [JsonPropertyName("assigned_contract")]
    [Description("The `header` of attached contract to the customer (Note: `header` - [string] the contract's fields concatenated by pattern `{contract_title}`).")]
    [Nullable(true)]
    public string? AssignedContract { get; init; }

    [JsonPropertyName("industry")]
    [Description("The `header` of attached industry to the customer (Note: `header` - [string] the industry's fields concatenated by pattern `{industry}`).")]
    [Nullable(true)]
    public string? Industry { get; init; }

    [JsonPropertyName("is_taxable")]
    [Description("The customer's is taxable flag.")]
    [Nullable(true)]
    public bool? IsTaxable { get; init; }

    [JsonPropertyName("tax_item_name")]
    [Description("The `header` of attached tax item to the customer (Note: `header` - [string] the tax item's fields concatenated by pattern `{short_name}` with space as separator).")]
    [Nullable(true)]
    public string? TaxItemName { get; init; }

    [JsonPropertyName("qbo_sync_token")]
    [Description("The customer's qbo sync token.")]
    [Nullable(true)]
    public int? QboSyncToken { get; init; }

    [JsonPropertyName("qbo_currency")]
    [Description("The customer's qbo currency.")]
    [Nullable(true)]
    public string? QboCurrency { get; init; }

    [JsonPropertyName("qbo_id")]
    [Description("The customer's qbo id.")]
    [Nullable(true)]
    public int? QboId { get; init; }

    [JsonPropertyName("qbd_id")]
    [Description("The customer's qbd id.")]
    [Nullable(true)]
    public string? QbdId { get; init; }

    [JsonPropertyName("created_at")]
    [Description("The customer's created date.")]
    [Nullable(true)]
    public DateTime? CreatedAt { get; init; }

    [JsonPropertyName("updated_at")]
    [Description("The customer's updated date.")]
    [Nullable(true)]
    public DateTime? UpdatedAt { get; init; }

    [JsonPropertyName("contacts")]
    [Description("The customer's contacts list.")]
    [Nullable(true)]
    public CustomerContact[]? Contacts { get; init; }

    [JsonPropertyName("locations")]
    [Description("The customer's locations list.")]
    [Nullable(true)]
    public CustomerLocation[]? Locations { get; init; }

    [JsonPropertyName("custom_fields")]
    [Description("The customer's custom fields list.")]
    [Nullable(true)]
    public CustomField[]? CustomFields { get; init; }
}

/// <summary>
/// A custom field's schema.
/// </summary>
public class CustomField
{
    [JsonPropertyName("name")]
    [Description("The custom field's name.")]
    [Nullable(true)]
    public string? Name { get; init; }

    [JsonPropertyName("value")]
    [Description("The custom field's value.")]
    [Nullable(true)]
    public object? Value { get; init; }

    [JsonPropertyName("type")]
    [Description("The custom field's type.")]
    [Nullable(true)]
    public string? Type { get; init; }

    [JsonPropertyName("group")]
    [Description("The custom field's group.")]
    [Nullable(true)]
    public string? Group { get; init; }

    [JsonPropertyName("created_at")]
    [Description("The custom field's created date.")]
    [Nullable(true)]
    public DateTime? CreatedAt { get; init; }

    [JsonPropertyName("updated_at")]
    [Description("The custom field's updated date.")]
    [Nullable(true)]
    public DateTime? UpdatedAt { get; init; }

    [JsonPropertyName("is_required")]
    [Description("The custom field's is required flag.")]
    [Nullable(true)]
    public bool? IsRequired { get; init; }
}

/// <summary>
/// A customer contact's schema.
/// </summary>
public class CustomerContact
{
    [JsonPropertyName("prefix")]
    [Description("The contact's prefix.")]
    [Nullable(true)]
    public string? Prefix { get; init; }

    [JsonPropertyName("fname")]
    [Description("The contact's first name.")]
    [Nullable(true)]
    public string? Fname { get; init; }

    [JsonPropertyName("lname")]
    [Description("The contact's last name.")]
    [Nullable(true)]
    public string? Lname { get; init; }

    [JsonPropertyName("suffix")]
    [Description("The contact's suffix.")]
    [Nullable(true)]
    public string? Suffix { get; init; }

    [JsonPropertyName("contact_type")]
    [Description("The contact's type.")]
    [Nullable(true)]
    public string? ContactType { get; init; }

    [JsonPropertyName("dob")]
    [Description("The contact's dob.")]
    [Nullable(true)]
    public string? Dob { get; init; }

    [JsonPropertyName("anniversary")]
    [Description("The contact's anniversary.")]
    [Nullable(true)]
    public string? Anniversary { get; init; }

    [JsonPropertyName("job_title")]
    [Description("The contact's job title.")]
    [Nullable(true)]
    public string? JobTitle { get; init; }

    [JsonPropertyName("department")]
    [Description("The contact's department.")]
    [Nullable(true)]
    public string? Department { get; init; }

    [JsonPropertyName("created_at")]
    [Description("The contact's created date.")]
    [Nullable(true)]
    public DateTime? CreatedAt { get; init; }

    [JsonPropertyName("updated_at")]
    [Description("The contact's updated date.")]
    [Nullable(true)]
    public DateTime? UpdatedAt { get; init; }

    [JsonPropertyName("is_primary")]
    [Description("The contact's is primary flag.")]
    [Nullable(true)]
    public bool? IsPrimary { get; init; }

    [JsonPropertyName("phones")]
    [Description("The contact's phones list.")]
    [Nullable(true)]
    public CustomerPhone[]? Phones { get; init; }

    [JsonPropertyName("emails")]
    [Description("The contact's emails list.")]
    [Nullable(true)]
    public CustomerEmail[]? Emails { get; init; }
}

/// <summary>
/// A customer email's schema.
/// </summary>
public class CustomerEmail
{
    [JsonPropertyName("email")]
    [Description("The email's address.")]
    [Nullable(true)]
    public string? Email { get; init; }

    [JsonPropertyName("class")]
    [Description("The email's class.")]
    [Nullable(true)]
    public string? Class { get; init; }

    [JsonPropertyName("types_accepted")]
    [Description("The email's types accepted.")]
    [Nullable(true)]
    public string? TypesAccepted { get; init; }

    [JsonPropertyName("created_at")]
    [Description("The email's created date.")]
    [Nullable(true)]
    public DateTime? CreatedAt { get; init; }

    [JsonPropertyName("updated_at")]
    [Description("The email's updated date.")]
    [Nullable(true)]
    public DateTime? UpdatedAt { get; init; }
}

/// <summary>
/// A customer location's schema.
/// </summary>
public class CustomerLocation
{
    [JsonPropertyName("street_1")]
    [Description("The location's street 1.")]
    [Nullable(true)]
    public string? Street1 { get; init; }

    [JsonPropertyName("street_2")]
    [Description("The location's street 2.")]
    [Nullable(true)]
    public string? Street2 { get; init; }

    [JsonPropertyName("city")]
    [Description("The location's city.")]
    [Nullable(true)]
    public string? City { get; init; }

    [JsonPropertyName("state_prov")]
    [Description("The location's state.")]
    [Nullable(true)]
    public string? StateProv { get; init; }

    [JsonPropertyName("postal_code")]
    [Description("The location's postal code.")]
    [Nullable(true)]
    public string? PostalCode { get; init; }

    [JsonPropertyName("country")]
    [Description("The location's country.")]
    [Nullable(true)]
    public string? Country { get; init; }

    [JsonPropertyName("nickname")]
    [Description("The location's nickname.")]
    [Nullable(true)]
    public string? Nickname { get; init; }

    [JsonPropertyName("gate_instructions")]
    [Description("The location's gate instructions.")]
    [Nullable(true)]
    public string? GateInstructions { get; init; }

    [JsonPropertyName("latitude")]
    [Description("The location's latitude.")]
    [Nullable(true)]
    public double? Latitude { get; init; }

    [JsonPropertyName("longitude")]
    [Description("The location's longitude.")]
    [Nullable(true)]
    public double? Longitude { get; init; }

    [JsonPropertyName("location_type")]
    [Description("The location's type.")]
    [Nullable(true)]
    public string? LocationType { get; init; }

    [JsonPropertyName("created_at")]
    [Description("The location's created date.")]
    [Nullable(true)]
    public DateTime? CreatedAt { get; init; }

    [JsonPropertyName("updated_at")]
    [Description("The location's updated date.")]
    [Nullable(true)]
    public DateTime? UpdatedAt { get; init; }

    [JsonPropertyName("is_primary")]
    [Description("The location's is primary flag.")]
    [Nullable(true)]
    public bool? IsPrimary { get; init; }

    [JsonPropertyName("is_gated")]
    [Description("The location's is gated flag.")]
    [Nullable(true)]
    public bool? IsGated { get; init; }

    [JsonPropertyName("is_bill_to")]
    [Description("The location's is bill to flag.")]
    [Nullable(true)]
    public bool? IsBillTo { get; init; }

    [JsonPropertyName("customer_contact")]
    [Description("The `header` of attached customer contact to the location (Note: `header` - [string] the customer contact's fields concatenated by pattern `{fname} {lname}` with space as separator).")]
    [Nullable(true)]
    public string? CustomerContact { get; init; }
}

/// <summary>
/// A customer phone's schema.
/// </summary>
public class CustomerPhone
{
    [JsonPropertyName("phone")]
    [Description("The phone's number.")]
    [Nullable(true)]
    public string? Phone { get; init; }

    [JsonPropertyName("ext")]
    [Description("The phone's extension.")]
    [Nullable(true)]
    public int? Ext { get; init; }

    [JsonPropertyName("type")]
    [Description("The phone's type.")]
    [Nullable(true)]
    public string? Type { get; init; }

    [JsonPropertyName("created_at")]
    [Description("The phone's created date.")]
    [Nullable(true)]
    public DateTime? CreatedAt { get; init; }

    [JsonPropertyName("updated_at")]
    [Description("The phone's updated date.")]
    [Nullable(true)]
    public DateTime? UpdatedAt { get; init; }

    [JsonPropertyName("is_mobile")]
    [Description("The phone's is mobile flag.")]
    [Nullable(true)]
    public bool? IsMobile { get; init; }
}
