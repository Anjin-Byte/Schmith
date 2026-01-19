namespace Connector.PaycorAPIV2.v2.Employees;

using Json.Schema.Generation;
using System.Text.Json.Serialization;
using Xchange.Connector.SDK.CacheWriter;

/// <summary>
/// Employee work data (non-PII) including position, status, and work location.
/// </summary>
[PrimaryKey("id", nameof(EmployeeId))]
[Description("Employee work data (non-PII) including position, status, and work location")]
public class EmployeesDataObject
{
    [JsonPropertyName("id")]
    [Description("Unique employee identifier")]
    [Required]
    public required string EmployeeId { get; init; }

    [JsonPropertyName("employeeNumber")]
    [Description("Human-readable employee number")]
    [Required]
    public required string EmployeeNumber { get; init; }

    [JsonPropertyName("firstName")]
    [Description("Employee first name")]
    [Required]
    [WriteOnly]
    public required string FirstName { get; init; }

    [JsonPropertyName("middleName")]
    [Description("Employee middle name")]
    [Nullable(true)]
    [WriteOnly]
    public string? MiddleName { get; init; }

    [JsonPropertyName("lastName")]
    [Description("Employee last name")]
    [Required]
    [WriteOnly]
    public required string LastName { get; init; }

    [JsonPropertyName("lastName2")]
    [Description("Secondary last name (for compound surnames)")]
    [Nullable(true)]
    [WriteOnly]
    public string? LastName2 { get; init; }

    [JsonPropertyName("workerCategory")]
    [Description("Worker category (e.g., Paid, Unpaid)")]
    [Nullable(true)]
    public string? WorkerCategory { get; init; }

    [JsonPropertyName("workCountryCode")]
    [Description("Country code for work location")]
    [Nullable(true)]
    public string? WorkCountryCode { get; init; }

    [JsonPropertyName("email")]
    [Description("Work email address")]
    [Nullable(true)]
    [WriteOnly]
    public EmployeeEmail? WorkEmail { get; init; }

    [JsonPropertyName("positionData")]
    [Description("Employee position and job information")]
    [Nullable(true)]
    public EmployeePosition? Position { get; init; }

    [JsonPropertyName("employmentDateData")]
    [Description("Employment dates and milestones")]
    [Nullable(true)]
    public EmploymentDates? EmploymentDates { get; init; }

    [JsonPropertyName("statusData")]
    [Description("Employment status information")]
    [Nullable(true)]
    public EmployeeStatus? Status { get; init; }

    [JsonPropertyName("workLocation")]
    [Description("Primary work location")]
    [Nullable(true)]
    public EmployeeWorkLocation? WorkLocation { get; init; }

    [JsonPropertyName("legalEntity")]
    [Description("Legal entity reference")]
    [Nullable(true)]
    public EmployeeLegalEntity? LegalEntity { get; init; }

    [JsonPropertyName("person")]
    [Description("Person record reference")]
    [Nullable(true)]
    public EmployeePerson? Person { get; init; }

    [JsonPropertyName("department")]
    [Description("Department reference")]
    [Nullable(true)]
    public EmployeeDepartment? Department { get; init; }
}

public class EmployeeEmail
{
    [JsonPropertyName("type")]
    [Description("Email type (Work)")]
    [WriteOnly]
    public string? Type { get; init; }

    [JsonPropertyName("emailAddress")]
    [Description("Work email address")]
    [WriteOnly]
    public string? EmailAddress { get; init; }
}

public class EmployeePosition
{
    [JsonPropertyName("jobTitle")]
    [Description("Job title")]
    [Nullable(true)]
    public string? JobTitle { get; init; }

    [JsonPropertyName("jobCode")]
    [Description("Job code")]
    [Nullable(true)]
    public string? JobCode { get; init; }

    [JsonPropertyName("effectiveEndDate")]
    [Description("Position end date")]
    [Nullable(true)]
    public string? EffectiveEndDate { get; init; }

    [JsonPropertyName("payGroupId")]
    [Description("Pay group identifier")]
    [Nullable(true)]
    public string? PayGroupId { get; init; }

    [JsonPropertyName("manager")]
    [Description("Employee's manager information")]
    [Nullable(true)]
    public EmployeeManager? Manager { get; init; }
}

public class EmployeeManager
{
    [JsonPropertyName("id")]
    [Description("Manager's employee ID")]
    [Nullable(true)]
    public string? ManagerEmployeeId { get; init; }

    [JsonPropertyName("employeeNumber")]
    [Description("Manager's employee number")]
    [Nullable(true)]
    public string? ManagerEmployeeNumber { get; init; }
}

public class EmploymentDates
{
    [JsonPropertyName("hireDate")]
    [Description("Original hire date")]
    [Nullable(true)]
    public string? HireDate { get; init; }

    [JsonPropertyName("adjustedHireDate")]
    [Description("Adjusted hire date for benefits calculation")]
    [Nullable(true)]
    public string? AdjustedHireDate { get; init; }

    [JsonPropertyName("terminationDate")]
    [Description("Employment termination date")]
    [Nullable(true)]
    public string? TerminationDate { get; init; }

    [JsonPropertyName("terminationReason")]
    [Description("Reason for termination")]
    [Nullable(true)]
    public string? TerminationReason { get; init; }

    [JsonPropertyName("reHireDate")]
    [Description("Most recent rehire date")]
    [Nullable(true)]
    public string? ReHireDate { get; init; }

    [JsonPropertyName("seniorityDate")]
    [Description("Seniority calculation date")]
    [Nullable(true)]
    public string? SeniorityDate { get; init; }
}

public class EmployeeStatus
{
    [JsonPropertyName("isFullTime")]
    [Description("Whether employee is full-time")]
    [Nullable(true)]
    public bool? IsFullTime { get; init; }

    [JsonPropertyName("status")]
    [Description("Employment status (Active, Terminated, OnLeave)")]
    [Nullable(true)]
    public string? EmploymentStatus { get; init; }

    [JsonPropertyName("flsa")]
    [Description("FLSA status (HourlyNonExempt, SalaryNonExempt, SalaryExempt, Unknown)")]
    [Nullable(true)]
    public string? FlsaStatus { get; init; }

    [JsonPropertyName("type")]
    [Description("Employee type (Regular, Temporary, etc.)")]
    [Nullable(true)]
    public string? EmployeeType { get; init; }

    [JsonPropertyName("eligibleForRehire")]
    [Description("Whether employee is eligible for rehire (Yes, No, Unknown)")]
    [Nullable(true)]
    public string? EligibleForRehire { get; init; }
}

public class EmployeeWorkLocation
{
    [JsonPropertyName("id")]
    [Description("Work location identifier")]
    [Nullable(true)]
    public string? LocationId { get; init; }

    [JsonPropertyName("name")]
    [Description("Work location name")]
    [Nullable(true)]
    public string? LocationName { get; init; }

    [JsonPropertyName("streetLine1")]
    [Description("Street address line 1")]
    [Nullable(true)]
    [WriteOnly]
    public string? StreetLine1 { get; init; }

    [JsonPropertyName("type")]
    [Description("Location type (Physical, Remote)")]
    [Nullable(true)]
    public string? LocationType { get; init; }

    [JsonPropertyName("city")]
    [Description("City")]
    [Nullable(true)]
    [WriteOnly]
    public string? City { get; init; }

    [JsonPropertyName("county")]
    [Description("County")]
    [Nullable(true)]
    public string? County { get; init; }

    [JsonPropertyName("state")]
    [Description("State/Province code")]
    [Nullable(true)]
    public string? State { get; init; }

    [JsonPropertyName("zipCode")]
    [Description("ZIP/Postal code")]
    [Nullable(true)]
    public string? ZipCode { get; init; }

    [JsonPropertyName("country")]
    [Description("Country code")]
    [Nullable(true)]
    public string? Country { get; init; }
}

public class EmployeeLegalEntity
{
    [JsonPropertyName("id")]
    [Description("Legal entity ID")]
    [Nullable(true)]
    public string? LegalEntityId { get; init; }
}

public class EmployeePerson
{
    [JsonPropertyName("id")]
    [Description("Person ID (links to Persons cache writer)")]
    [Nullable(true)]
    public string? PersonId { get; init; }
}

public class EmployeeDepartment
{
    [JsonPropertyName("id")]
    [Description("Department ID")]
    [Nullable(true)]
    public string? DepartmentId { get; init; }
}
