namespace Connector.ADPWorkforceNowAPI.v1.LaborCodeMeta;

using Json.Schema.Generation;
using System.Collections.Generic;
using System.Text.Json.Serialization;
using Xchange.Connector.SDK.CacheWriter;

/// <summary>
/// Dynamic data object for labor code metadata.
/// Schema varies between customers.
/// Single record with static Id = 0 to trigger flows on change;
/// No PII Present, API Doc here: https://developers.adp.com/apis/api-explorer/hcm-offrg-wfn/hcm-offrg-wfn-time-labor-allocation-code-uploads-v2-labor-allocation-code-uploads?operation=GET%2Ftime%2Fv1%2Flabor-allocation-code%2Fupload-requests%2Fmeta#swagger
/// </summary>
[PrimaryKey("id", nameof(Id))]
[Description("Labor code metadata from ADP - schema varies per customer")]
public class LaborCodeMetaDataObject
{
    [JsonPropertyName("id")]
    [Description("Static identifier (always 0)")]
    [Required]
    public required int Id { get; init; }

    [JsonPropertyName("meta")]
    [Description("Dynamic metadata content - nested structure varies per customer")]
    [Nullable(true)]
    public Dictionary<string, object>? Meta { get; init; }
}
