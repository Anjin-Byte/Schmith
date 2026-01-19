namespace Connector.ADPWorkforceNowAPI.v1.Common;

using Json.Schema.Generation;
using System.Collections.Generic;
using System.Text.Json.Serialization;

/// <summary>
/// Common classes shared across US Tax Profile endpoints (Federal, State, Local)
/// These classes represent standard ADP data structures used in multiple tax-related APIs
/// </summary>

/// <summary>
/// Standard ADP code/value pattern with optional short and long names
/// Used for status codes, filing status codes, state codes, local codes, etc.
/// </summary>
public class CodeItem
{
    [JsonPropertyName("codeValue")]
    [Nullable(true)]
    public string? CodeValue { get; init; }

    [JsonPropertyName("shortName")]
    [Nullable(true)]
    public string? ShortName { get; init; }

    [JsonPropertyName("longName")]
    [Nullable(true)]
    public string? LongName { get; init; }

    [JsonPropertyName("prenoteDate")]
    [Nullable(true)]
    public string? PrenoteDate { get; init; }
}

/// <summary>
/// Tax withholding status structure common across Federal, State, and Local tax instructions
/// </summary>
public class TaxWithholdingStatus
{
    [JsonPropertyName("statusCode")]
    [Nullable(true)]
    public CodeItem? StatusCode { get; init; }

    [JsonPropertyName("reasonCode")]
    [Nullable(true)]
    public string? ReasonCode { get; init; }

    [JsonPropertyName("effectiveDate")]
    [Nullable(true)]
    public string? EffectiveDate { get; init; }
}

/// <summary>
/// Monetary amount with currency code - used for tax amounts throughout tax profiles
/// Amount values are marked WriteOnly as they contain financial information
/// </summary>
public class TaxAmount
{
    [JsonPropertyName("amountValue")]
    [Nullable(true)]
    [WriteOnly]
    public decimal? AmountValue { get; init; }

    [JsonPropertyName("currencyCode")]
    [Nullable(true)]
    public string? CurrencyCode { get; init; }
}

/// <summary>
/// Payroll group code structure used in all tax profile responses
/// </summary>
public class PayrollGroupCode
{
    [JsonPropertyName("codeValue")]
    [Nullable(true)]
    public string? CodeValue { get; init; }

    [JsonPropertyName("longName")]
    [Nullable(true)]
    public string? LongName { get; init; }
}

/// <summary>
/// Payroll region code structure used in state tax profiles
/// </summary>
public class PayrollRegionCode
{
    [JsonPropertyName("codeValue")]
    [Nullable(true)]
    public string? CodeValue { get; init; }
}

/// <summary>
/// Tax allowance structure for Federal tax - uses TaxAmount for allowance amounts
/// </summary>
public class FederalTaxAllowance
{
    [JsonPropertyName("allowanceTypeCode")]
    [Nullable(true)]
    public CodeItem? AllowanceTypeCode { get; init; }

    [JsonPropertyName("taxAllowanceAmount")]
    [Nullable(true)]
    public TaxAmount? TaxAllowanceAmount { get; init; }
}

/// <summary>
/// Tax allowance structure for State tax - uses quantity instead of amount
/// </summary>
public class StateTaxAllowance
{
    [JsonPropertyName("allowanceTypeCode")]
    [Nullable(true)]
    public CodeItem? AllowanceTypeCode { get; init; }

    [JsonPropertyName("taxAllowanceQuantity")]
    [Nullable(true)]
    public int? TaxAllowanceQuantity { get; init; }
}
