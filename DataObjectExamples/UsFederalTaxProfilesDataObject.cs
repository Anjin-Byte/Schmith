namespace Connector.ADPWorkforceNowAPI.v1.UsFederalTaxProfiles;

using Connector.ADPWorkforceNowAPI.v1.Common;
using Json.Schema.Generation;
using System.Text.Json.Serialization;
using Xchange.Connector.SDK.CacheWriter;

/// <summary>
/// Represents a worker's US Federal Tax Profile from ADP Workforce Now
/// Contains federal tax withholding instructions, allowances, and Form 1099 information
/// </summary>
[PrimaryKey("compositePrimaryKey", nameof(AssociateOID), nameof(ItemID))]
[Description("US Federal Tax Profile for a worker including federal income tax, Social Security, Medicare, and unemployment tax instructions")]
public class UsFederalTaxProfilesDataObject
{
    [JsonPropertyName("associateOID")]
    [Description("Associate OID from the worker record - links to Workers data object")]
    [Required]
    public required string AssociateOID { get; init; }

    [JsonPropertyName("itemID")]
    [Description("Unique identifier for this specific tax profile record")]
    [Required]
    public required string ItemID { get; init; }

    [JsonPropertyName("payrollFileNumber")]
    [Description("Payroll file number for this worker")]
    [Nullable(true)]
    public string? PayrollFileNumber { get; init; }

    [JsonPropertyName("payrollGroupCode")]
    [Description("Payroll group code and name")]
    [Nullable(true)]
    public PayrollGroupCode? PayrollGroupCode { get; init; }

    [JsonPropertyName("usFederalTaxInstruction")]
    [Description("Container for all US federal tax instructions")]
    [Nullable(true)]
    public UsFederalTaxInstruction? UsFederalTaxInstruction { get; init; }
}

/// <summary>
/// Container for US federal tax instructions including income tax, Social Security, Medicare, and unemployment
/// </summary>
public class UsFederalTaxInstruction
{
    [JsonPropertyName("multipleJobIndicator")]
    [Description("Indicates if the worker has multiple jobs")]
    [Nullable(true)]
    public bool? MultipleJobIndicator { get; init; }

    [JsonPropertyName("federalIncomeTaxInstruction")]
    [Description("Federal income tax withholding instructions including filing status and allowances")]
    [Nullable(true)]
    public FederalIncomeTaxInstruction? FederalIncomeTaxInstruction { get; init; }

    [JsonPropertyName("socialSecurityTaxInstruction")]
    [Description("Social Security tax withholding instructions")]
    [Nullable(true)]
    public TaxWithholdingStatus? SocialSecurityTaxInstruction { get; init; }

    [JsonPropertyName("medicareTaxInstruction")]
    [Description("Medicare tax withholding instructions")]
    [Nullable(true)]
    public TaxWithholdingStatus? MedicareTaxInstruction { get; init; }

    [JsonPropertyName("federalUnemploymentTaxInstruction")]
    [Description("Federal unemployment tax (FUTA) withholding instructions")]
    [Nullable(true)]
    public TaxWithholdingStatus? FederalUnemploymentTaxInstruction { get; init; }

    [JsonPropertyName("form1099Instruction")]
    [Description("Form 1099 tax reporting instructions")]
    [Nullable(true)]
    public Form1099Instruction? Form1099Instruction { get; init; }

    [JsonPropertyName("interimW2IssuedIndicator")]
    [Description("Indicates if an interim W-2 has been issued")]
    [Nullable(true)]
    public bool? InterimW2IssuedIndicator { get; init; }

    [JsonPropertyName("statutoryWorkerIndicator")]
    [Description("Indicates if the worker is a statutory employee")]
    [Nullable(true)]
    public bool? StatutoryWorkerIndicator { get; init; }

    [JsonPropertyName("qualifiedPensionPlanCoverageIndicator")]
    [Description("Indicates if the worker is covered by a qualified pension plan")]
    [Nullable(true)]
    public bool? QualifiedPensionPlanCoverageIndicator { get; init; }
}

/// <summary>
/// Federal income tax withholding instructions
/// </summary>
public class FederalIncomeTaxInstruction
{
    [JsonPropertyName("taxWithholdingStatus")]
    [Description("Tax withholding status (exempt or non-exempt)")]
    [Nullable(true)]
    public TaxWithholdingStatus? TaxWithholdingStatus { get; init; }

    [JsonPropertyName("taxFilingStatusCode")]
    [Description("Tax filing status code (Single, Married, etc.)")]
    [Nullable(true)]
    public CodeItem? TaxFilingStatusCode { get; init; }

    [JsonPropertyName("taxWithholdingAllowanceQuantity")]
    [Description("Number of tax withholding allowances claimed")]
    [Nullable(true)]
    public int? TaxWithholdingAllowanceQuantity { get; init; }

    [JsonPropertyName("taxAllowances")]
    [Description("Array of tax allowances with types and amounts")]
    [Nullable(true)]
    public System.Collections.Generic.List<FederalTaxAllowance>? TaxAllowances { get; init; }

    [JsonPropertyName("additionalIncomeAmount")]
    [Description("Additional income amount to factor into withholding - marked WriteOnly as financial data")]
    [Nullable(true)]
    public TaxAmount? AdditionalIncomeAmount { get; init; }

    [JsonPropertyName("additionalTaxPercentage")]
    [Description("Additional tax percentage to withhold")]
    [Nullable(true)]
    public decimal? AdditionalTaxPercentage { get; init; }

    [JsonPropertyName("additionalTaxAmount")]
    [Description("Additional tax amount to withhold - marked WriteOnly as financial data")]
    [Nullable(true)]
    public TaxAmount? AdditionalTaxAmount { get; init; }

    [JsonPropertyName("overrideTaxPercentage")]
    [Description("Override tax percentage")]
    [Nullable(true)]
    public decimal? OverrideTaxPercentage { get; init; }

    [JsonPropertyName("overrideTaxAmount")]
    [Description("Override tax amount - marked WriteOnly as financial data")]
    [Nullable(true)]
    public TaxAmount? OverrideTaxAmount { get; init; }
}

/// <summary>
/// Form 1099 tax reporting instructions for contractors and non-employees
/// </summary>
public class Form1099Instruction
{
    [JsonPropertyName("distributionCodes")]
    [Description("Array of distribution codes for Form 1099 reporting")]
    [Nullable(true)]
    public System.Collections.Generic.List<CodeItem>? DistributionCodes { get; init; }

    [JsonPropertyName("totalDistributionIndicator")]
    [Description("Indicates if this is a total distribution")]
    [Nullable(true)]
    public bool? TotalDistributionIndicator { get; init; }

    [JsonPropertyName("individualRetirementAccountIndicator")]
    [Description("Indicates if this is an Individual Retirement Account (IRA)")]
    [Nullable(true)]
    public bool? IndividualRetirementAccountIndicator { get; init; }

    [JsonPropertyName("simplifiedEmployeePensionAccountIndicator")]
    [Description("Indicates if this is a Simplified Employee Pension (SEP) account")]
    [Nullable(true)]
    public bool? SimplifiedEmployeePensionAccountIndicator { get; init; }
}

/// <summary>
/// DTO for deserializing ADP API response - matches API structure without AssociateOID
/// This is used only for deserialization; the data reader creates the final UsFederalTaxProfilesDataObject
/// </summary>
public class UsFederalTaxProfilesDto
{
    [JsonPropertyName("itemID")]
    [Nullable(true)]
    public string? ItemID { get; init; }

    [JsonPropertyName("payrollFileNumber")]
    [Nullable(true)]
    public string? PayrollFileNumber { get; init; }

    [JsonPropertyName("payrollGroupCode")]
    [Nullable(true)]
    public PayrollGroupCode? PayrollGroupCode { get; init; }

    [JsonPropertyName("usFederalTaxInstruction")]
    [Nullable(true)]
    public UsFederalTaxInstruction? UsFederalTaxInstruction { get; init; }
}
