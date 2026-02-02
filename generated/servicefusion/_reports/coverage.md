# Schema Coverage Report: servicefusion

**Generated:** 2026-02-01 21:10:31
**IR Source:** `/Users/taylorhale/Documents/dev_hub/Brynhild/repos/Schmith/ir/servicefusion`

## Summary

| Metric | Count |
|--------|-------|
| Total schemas in spec | 94 |
| Generated DataObjects | 89 |
| Generated Roots | 23 |
| Nested-only Schemas | 26 |
| Filtered out | 5 |
| **Coverage** | **94.7%** |

## Filtered Schemas by Category

| Category | Count | Description |
|----------|-------|-------------|
| Primitive types | 4 | Intentionally excluded |
| Non-object kinds | 1 | Intentionally excluded |

## Generated DataObjects (Eligible Schemas)

The following 89 schemas are eligible for generation (before root/nested split):

| # | DataObject Name | Schema ID |
|---|-----------------|-----------|
| 1 | `Anonymous_56cecfadDataObject` | `schema:anon/56cecfad266bf953db2b3c6fa598418203a6592a` |
| 2 | `Anonymous_1dfe40b1DataObject` | `schema:anon/1dfe40b15f8339052c1208956acd01e486182051` |
| 3 | `Anonymous_5ccd2dd5DataObject` | `schema:anon/5ccd2dd5603bcd7e53d41c9bd5d4fcdc77c76118` |
| 4 | `Anonymous_50fd9975DataObject` | `schema:anon/50fd9975c7782c0811c1aca63f2e95e42f362200` |
| 5 | `Anonymous_ee256c5fDataObject` | `schema:anon/ee256c5fb2e71146c623815d25ec3bac3be32af3` |
| 6 | `Anonymous_8ed6ccdeDataObject` | `schema:anon/8ed6ccde9e78b86a5e48f91db61009acd0f077bc` |
| 7 | `Anonymous_a9aa79b8DataObject` | `schema:anon/a9aa79b8a530ebccf52a3891930e373e790da323` |
| 8 | `Anonymous_0a001c6bDataObject` | `schema:anon/0a001c6b5b204d66e1d536a7e82a8aac7e133b8d` |
| 9 | `Anonymous_124d7e49DataObject` | `schema:anon/124d7e495fe798ba9c648496f2b833e2ed2f1ea1` |
| 10 | `Anonymous_bd6f96bdDataObject` | `schema:anon/bd6f96bd182650c63771bc69acd0b3ba2262187a` |
| 11 | `Anonymous_5099ea82DataObject` | `schema:anon/5099ea82d845cee3899e956816856e24d1424f3b` |
| 12 | `_metaDataObject` | `schema:anon/4aef56ef1b5df2d8eedd0c54df071b3b2d3e9a0c` |
| 13 | `AssignedTechDataObject` | `schema:anon/8bb81687b6fec9f1342c2bba21e484956904c2af` |
| 14 | `itemsDataObject` | `schema:anon/c43bbb9a0c1d95e3fa51ca9c12c9b74d7d887542` |
| 15 | `JobDataObject` | `schema:anon/b2441a9ee496ebd118af85da9e0caf01df0f4e71` |
| 16 | `OAuthTokenDataObject` | `schema:types/OAuthToken` |
| 17 | `OAuthTokenErrorDataObject` | `schema:types/OAuthTokenError` |
| 18 | `400ErrorDataObject` | `schema:types/typ.400Error` |
| 19 | `404ErrorDataObject` | `schema:types/typ.404Error` |
| 20 | `405ErrorDataObject` | `schema:types/typ.405Error` |
| 21 | `415ErrorDataObject` | `schema:types/typ.415Error` |
| 22 | `429ErrorDataObject` | `schema:types/typ.429Error` |
| 23 | `500ErrorDataObject` | `schema:types/typ.500Error` |
| 24 | `AgentDataObject` | `schema:types/typ.Agent` |
| 25 | `AgentBodyDataObject` | `schema:types/typ.AgentBody` |
| 26 | `AssignedTechDataObject` | `schema:types/typ.AssignedTech` |
| 27 | `AssignedTechBodyDataObject` | `schema:types/typ.AssignedTechBody` |
| 28 | `CalendarTaskDataObject` | `schema:types/typ.CalendarTask` |
| 29 | `CalendarTaskRepeatDataObject` | `schema:types/typ.CalendarTaskRepeat` |
| 30 | `CalendarTaskViewDataObject` | `schema:types/typ.CalendarTaskView` |
| 31 | `CustomerDataObject` | `schema:types/typ.Customer` |
| 32 | `CustomerBodyDataObject` | `schema:types/typ.CustomerBody` |
| 33 | `CustomerContactDataObject` | `schema:types/typ.CustomerContact` |
| 34 | `CustomerContactBodyDataObject` | `schema:types/typ.CustomerContactBody` |
| 35 | `CustomerEmailDataObject` | `schema:types/typ.CustomerEmail` |
| 36 | `CustomerEmailBodyDataObject` | `schema:types/typ.CustomerEmailBody` |
| 37 | `CustomerLocationDataObject` | `schema:types/typ.CustomerLocation` |
| 38 | `CustomerLocationBodyDataObject` | `schema:types/typ.CustomerLocationBody` |
| 39 | `CustomerPhoneDataObject` | `schema:types/typ.CustomerPhone` |
| 40 | `CustomerPhoneBodyDataObject` | `schema:types/typ.CustomerPhoneBody` |
| 41 | `CustomerViewDataObject` | `schema:types/typ.CustomerView` |
| 42 | `CustomFieldDataObject` | `schema:types/typ.CustomField` |
| 43 | `CustomFieldBodyDataObject` | `schema:types/typ.CustomFieldBody` |
| 44 | `DocumentDataObject` | `schema:types/typ.Document` |
| 45 | `EquipmentDataObject` | `schema:types/typ.Equipment` |
| 46 | `EquipmentBodyDataObject` | `schema:types/typ.EquipmentBody` |
| 47 | `EquipmentViewDataObject` | `schema:types/typ.EquipmentView` |
| 48 | `ErrorDataObject` | `schema:types/typ.Error` |
| 49 | `EstimateDataObject` | `schema:types/typ.Estimate` |
| 50 | `EstimateBodyDataObject` | `schema:types/typ.EstimateBody` |
| 51 | `EstimateViewDataObject` | `schema:types/typ.EstimateView` |
| 52 | `InvoiceDataObject` | `schema:types/typ.Invoice` |
| 53 | `InvoiceViewDataObject` | `schema:types/typ.InvoiceView` |
| 54 | `JobDataObject` | `schema:types/typ.Job` |
| 55 | `JobBodyDataObject` | `schema:types/typ.JobBody` |
| 56 | `JobCategoryDataObject` | `schema:types/typ.JobCategory` |
| 57 | `JobCategoryViewDataObject` | `schema:types/typ.JobCategoryView` |
| 58 | `JobDocumentDataObject` | `schema:types/typ.JobDocument` |
| 59 | `JobExpenseDataObject` | `schema:types/typ.JobExpense` |
| 60 | `JobExpenseBodyDataObject` | `schema:types/typ.JobExpenseBody` |
| 61 | `JobLaborChargeDataObject` | `schema:types/typ.JobLaborCharge` |
| 62 | `JobLaborChargeBodyDataObject` | `schema:types/typ.JobLaborChargeBody` |
| 63 | `JobNoteDataObject` | `schema:types/typ.JobNote` |
| 64 | `JobNoteBodyDataObject` | `schema:types/typ.JobNoteBody` |
| 65 | `JobOtherChargeDataObject` | `schema:types/typ.JobOtherCharge` |
| 66 | `JobOtherChargeBodyDataObject` | `schema:types/typ.JobOtherChargeBody` |
| 67 | `JobProductDataObject` | `schema:types/typ.JobProduct` |
| 68 | `JobProductBodyDataObject` | `schema:types/typ.JobProductBody` |
| 69 | `JobServiceDataObject` | `schema:types/typ.JobService` |
| 70 | `JobServiceBodyDataObject` | `schema:types/typ.JobServiceBody` |
| 71 | `JobSignatureDataObject` | `schema:types/typ.JobSignature` |
| 72 | `JobStatusDataObject` | `schema:types/typ.JobStatus` |
| 73 | `JobStatusViewDataObject` | `schema:types/typ.JobStatusView` |
| 74 | `JobTagDataObject` | `schema:types/typ.JobTag` |
| 75 | `JobTagBodyDataObject` | `schema:types/typ.JobTagBody` |
| 76 | `JobTaskDataObject` | `schema:types/typ.JobTask` |
| 77 | `JobTaskBodyDataObject` | `schema:types/typ.JobTaskBody` |
| 78 | `JobViewDataObject` | `schema:types/typ.JobView` |
| 79 | `JobVisitDataObject` | `schema:types/typ.JobVisit` |
| 80 | `MeViewDataObject` | `schema:types/typ.MeView` |
| 81 | `PaymentDataObject` | `schema:types/typ.Payment` |
| 82 | `PaymentTypeDataObject` | `schema:types/typ.PaymentType` |
| 83 | `PaymentTypeViewDataObject` | `schema:types/typ.PaymentTypeView` |
| 84 | `PictureDataObject` | `schema:types/typ.Picture` |
| 85 | `PrintableWorkOrderDataObject` | `schema:types/typ.PrintableWorkOrder` |
| 86 | `SourceDataObject` | `schema:types/typ.Source` |
| 87 | `SourceViewDataObject` | `schema:types/typ.SourceView` |
| 88 | `TechDataObject` | `schema:types/typ.Tech` |
| 89 | `TechViewDataObject` | `schema:types/typ.TechView` |

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

### Primitive types (4)

| Name | Schema ID |
|------|-----------|
| `array` | `schema:types/array` |
| `items` | `schema:types/integer` |
| `object` | `schema:types/object` |
| `items` | `schema:types/string` |

### Non-object kinds (1)

| Name | Schema ID |
|------|-----------|
| `typ.422Error` | `schema:types/typ.422Error` |

## Status

✅ **All schemas accounted for** - Every schema in the spec is either generated or intentionally filtered.