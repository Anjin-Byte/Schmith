# Schema Coverage Report: servicefusion

**Generated:** 2026-01-31 15:20:05
**IR Source:** `/Users/taylorhale/Documents/dev_hub/Brynhild/repos/Schmith/ir/servicefusion`

## Summary

| Metric | Count |
|--------|-------|
| Total schemas in spec | 98 |
| Generated DataObjects | 66 |
| Generated Roots | 23 |
| Nested-only Schemas | 26 |
| Filtered out | 32 |
| **Coverage** | **67.3%** |

## Filtered Schemas by Category

| Category | Count | Description |
|----------|-------|-------------|
| Anonymous/inline schemas | 21 | Intentionally excluded |
| Primitive types | 2 | Intentionally excluded |
| Non-object kinds | 1 | Intentionally excluded |
| Error schemas | 8 | Intentionally excluded |

## Generated DataObjects (Eligible Schemas)

The following 66 schemas are eligible for generation (before root/nested split):

| # | DataObject Name | Schema ID |
|---|-----------------|-----------|
| 1 | `OAuthTokenDataObject` | `schema:types/OAuthToken` |
| 2 | `AgentDataObject` | `schema:types/typ.Agent` |
| 3 | `AgentBodyDataObject` | `schema:types/typ.AgentBody` |
| 4 | `AssignedTechDataObject` | `schema:types/typ.AssignedTech` |
| 5 | `AssignedTechBodyDataObject` | `schema:types/typ.AssignedTechBody` |
| 6 | `CalendarTaskDataObject` | `schema:types/typ.CalendarTask` |
| 7 | `CalendarTaskRepeatDataObject` | `schema:types/typ.CalendarTaskRepeat` |
| 8 | `CalendarTaskViewDataObject` | `schema:types/typ.CalendarTaskView` |
| 9 | `CustomerDataObject` | `schema:types/typ.Customer` |
| 10 | `CustomerBodyDataObject` | `schema:types/typ.CustomerBody` |
| 11 | `CustomerContactDataObject` | `schema:types/typ.CustomerContact` |
| 12 | `CustomerContactBodyDataObject` | `schema:types/typ.CustomerContactBody` |
| 13 | `CustomerEmailDataObject` | `schema:types/typ.CustomerEmail` |
| 14 | `CustomerEmailBodyDataObject` | `schema:types/typ.CustomerEmailBody` |
| 15 | `CustomerLocationDataObject` | `schema:types/typ.CustomerLocation` |
| 16 | `CustomerLocationBodyDataObject` | `schema:types/typ.CustomerLocationBody` |
| 17 | `CustomerPhoneDataObject` | `schema:types/typ.CustomerPhone` |
| 18 | `CustomerPhoneBodyDataObject` | `schema:types/typ.CustomerPhoneBody` |
| 19 | `CustomerViewDataObject` | `schema:types/typ.CustomerView` |
| 20 | `CustomFieldDataObject` | `schema:types/typ.CustomField` |
| 21 | `CustomFieldBodyDataObject` | `schema:types/typ.CustomFieldBody` |
| 22 | `DocumentDataObject` | `schema:types/typ.Document` |
| 23 | `EquipmentDataObject` | `schema:types/typ.Equipment` |
| 24 | `EquipmentBodyDataObject` | `schema:types/typ.EquipmentBody` |
| 25 | `EquipmentViewDataObject` | `schema:types/typ.EquipmentView` |
| 26 | `EstimateDataObject` | `schema:types/typ.Estimate` |
| 27 | `EstimateBodyDataObject` | `schema:types/typ.EstimateBody` |
| 28 | `EstimateViewDataObject` | `schema:types/typ.EstimateView` |
| 29 | `InvoiceDataObject` | `schema:types/typ.Invoice` |
| 30 | `InvoiceViewDataObject` | `schema:types/typ.InvoiceView` |
| 31 | `JobDataObject` | `schema:types/typ.Job` |
| 32 | `JobBodyDataObject` | `schema:types/typ.JobBody` |
| 33 | `JobCategoryDataObject` | `schema:types/typ.JobCategory` |
| 34 | `JobCategoryViewDataObject` | `schema:types/typ.JobCategoryView` |
| 35 | `JobDocumentDataObject` | `schema:types/typ.JobDocument` |
| 36 | `JobExpenseDataObject` | `schema:types/typ.JobExpense` |
| 37 | `JobExpenseBodyDataObject` | `schema:types/typ.JobExpenseBody` |
| 38 | `JobLaborChargeDataObject` | `schema:types/typ.JobLaborCharge` |
| 39 | `JobLaborChargeBodyDataObject` | `schema:types/typ.JobLaborChargeBody` |
| 40 | `JobNoteDataObject` | `schema:types/typ.JobNote` |
| 41 | `JobNoteBodyDataObject` | `schema:types/typ.JobNoteBody` |
| 42 | `JobOtherChargeDataObject` | `schema:types/typ.JobOtherCharge` |
| 43 | `JobOtherChargeBodyDataObject` | `schema:types/typ.JobOtherChargeBody` |
| 44 | `JobProductDataObject` | `schema:types/typ.JobProduct` |
| 45 | `JobProductBodyDataObject` | `schema:types/typ.JobProductBody` |
| 46 | `JobServiceDataObject` | `schema:types/typ.JobService` |
| 47 | `JobServiceBodyDataObject` | `schema:types/typ.JobServiceBody` |
| 48 | `JobSignatureDataObject` | `schema:types/typ.JobSignature` |
| 49 | `JobStatusDataObject` | `schema:types/typ.JobStatus` |
| 50 | `JobStatusViewDataObject` | `schema:types/typ.JobStatusView` |
| 51 | `JobTagDataObject` | `schema:types/typ.JobTag` |
| 52 | `JobTagBodyDataObject` | `schema:types/typ.JobTagBody` |
| 53 | `JobTaskDataObject` | `schema:types/typ.JobTask` |
| 54 | `JobTaskBodyDataObject` | `schema:types/typ.JobTaskBody` |
| 55 | `JobViewDataObject` | `schema:types/typ.JobView` |
| 56 | `JobVisitDataObject` | `schema:types/typ.JobVisit` |
| 57 | `MeViewDataObject` | `schema:types/typ.MeView` |
| 58 | `PaymentDataObject` | `schema:types/typ.Payment` |
| 59 | `PaymentTypeDataObject` | `schema:types/typ.PaymentType` |
| 60 | `PaymentTypeViewDataObject` | `schema:types/typ.PaymentTypeView` |
| 61 | `PictureDataObject` | `schema:types/typ.Picture` |
| 62 | `PrintableWorkOrderDataObject` | `schema:types/typ.PrintableWorkOrder` |
| 63 | `SourceDataObject` | `schema:types/typ.Source` |
| 64 | `SourceViewDataObject` | `schema:types/typ.SourceView` |
| 65 | `TechDataObject` | `schema:types/typ.Tech` |
| 66 | `TechViewDataObject` | `schema:types/typ.TechView` |

## Generated Roots (Standalone DataObjects)

The following 23 schemas produce standalone scaffolding:

| # | DataObject Name |
|---|-----------------|
| 1 | `AgentBodyDataObject` |
| 2 | `AssignedTechBodyDataObject` |
| 3 | `CalendarTaskDataObject` |
| 4 | `CustomerDataObject` |
| 5 | `CustomerContactBodyDataObject` |
| 6 | `CustomerLocationBodyDataObject` |
| 7 | `EquipmentBodyDataObject` |
| 8 | `EstimateDataObject` |
| 9 | `JobDataObject` |
| 10 | `JobCategoryDataObject` |
| 11 | `JobExpenseBodyDataObject` |
| 12 | `JobLaborChargeBodyDataObject` |
| 13 | `JobNoteBodyDataObject` |
| 14 | `JobOtherChargeBodyDataObject` |
| 15 | `JobProductBodyDataObject` |
| 16 | `JobServiceBodyDataObject` |
| 17 | `JobStatusDataObject` |
| 18 | `JobTagBodyDataObject` |
| 19 | `JobTaskBodyDataObject` |
| 20 | `PaymentTypeDataObject` |
| 21 | `PictureDataObject` |
| 22 | `SourceDataObject` |
| 23 | `TechDataObject` |

## Nested-only Schemas

The following 26 schemas are included as nested types under roots:

| # | Schema Name |
|---|-------------|
| 1 | `Agent` |
| 2 | `AssignedTech` |
| 3 | `CalendarTaskRepeat` |
| 4 | `CustomField` |
| 5 | `CustomFieldBody` |
| 6 | `CustomerContact` |
| 7 | `CustomerEmail` |
| 8 | `CustomerEmailBody` |
| 9 | `CustomerLocation` |
| 10 | `CustomerPhone` |
| 11 | `CustomerPhoneBody` |
| 12 | `Document` |
| 13 | `Equipment` |
| 14 | `Invoice` |
| 15 | `JobExpense` |
| 16 | `JobLaborCharge` |
| 17 | `JobNote` |
| 18 | `JobOtherCharge` |
| 19 | `JobProduct` |
| 20 | `JobService` |
| 21 | `JobSignature` |
| 22 | `JobTag` |
| 23 | `JobTask` |
| 24 | `JobVisit` |
| 25 | `Payment` |
| 26 | `PrintableWorkOrder` |

## Filtered Schema Details

### Anonymous/inline schemas (21)

| Name | Schema ID |
|------|-----------|
| `None` | `schema:anon/0a001c6b5b204d66e1d536a7e82a8aac7e133b8d` |
| `None` | `schema:anon/124d7e495fe798ba9c648496f2b833e2ed2f1ea1` |
| `None` | `schema:anon/1dfe40b15f8339052c1208956acd01e486182051` |
| `items` | `schema:anon/49e60392e4b641f4c7cd787e2d2f056ed7315a31` |
| `_meta` | `schema:anon/4aef56ef1b5df2d8eedd0c54df071b3b2d3e9a0c` |
| `items` | `schema:anon/4b0ddaabb4fa2a259c7effc43eb30e05adfce2de` |
| `None` | `schema:anon/5099ea82d845cee3899e956816856e24d1424f3b` |
| `None` | `schema:anon/50fd9975c7782c0811c1aca63f2e95e42f362200` |
| `None` | `schema:anon/56cecfad266bf953db2b3c6fa598418203a6592a` |
| `None` | `schema:anon/5ccd2dd5603bcd7e53d41c9bd5d4fcdc77c76118` |
| `items` | `schema:anon/7cb68b1b7ee21eea168641a1efa7871424b3bf4b` |
| `AssignedTech` | `schema:anon/8bb81687b6fec9f1342c2bba21e484956904c2af` |
| `None` | `schema:anon/8ed6ccde9e78b86a5e48f91db61009acd0f077bc` |
| `None` | `schema:anon/a9aa79b8a530ebccf52a3891930e373e790da323` |
| `items` | `schema:anon/ab3f875c8616f895b8d8898634bbc9497d42411c` |
| `Job` | `schema:anon/b2441a9ee496ebd118af85da9e0caf01df0f4e71` |
| `None` | `schema:anon/bd6f96bd182650c63771bc69acd0b3ba2262187a` |
| `items` | `schema:anon/c43bbb9a0c1d95e3fa51ca9c12c9b74d7d887542` |
| `items` | `schema:anon/c83c88cdba15cb620be5734bbe2168d4b373f343` |
| `items` | `schema:anon/e6d7c085f06d737cd8db642516e1a28fc507570b` |
| `None` | `schema:anon/ee256c5fb2e71146c623815d25ec3bac3be32af3` |

### Primitive types (2)

| Name | Schema ID |
|------|-----------|
| `array` | `schema:types/array` |
| `object` | `schema:types/object` |

### Non-object kinds (1)

| Name | Schema ID |
|------|-----------|
| `typ.422Error` | `schema:types/typ.422Error` |

### Error schemas (8)

| Name | Schema ID |
|------|-----------|
| `OAuthTokenError` | `schema:types/OAuthTokenError` |
| `typ.400Error` | `schema:types/typ.400Error` |
| `typ.404Error` | `schema:types/typ.404Error` |
| `typ.405Error` | `schema:types/typ.405Error` |
| `typ.415Error` | `schema:types/typ.415Error` |
| `typ.429Error` | `schema:types/typ.429Error` |
| `typ.500Error` | `schema:types/typ.500Error` |
| `typ.Error` | `schema:types/typ.Error` |

## Status

✅ **All schemas accounted for** - Every schema in the spec is either generated or intentionally filtered.