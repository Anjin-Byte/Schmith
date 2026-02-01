# Endpoint Response Coverage: paycore

## Summary

| Metric | Count |
|--------|-------|
| Total endpoints | 52 |
| Total response schemas | 31 |
| Mapped response schemas | 20 |
| Unmapped response schemas | 11 |

## Endpoint Responses

| Method | Path | Response Schema | DataObject | Mapping |
|--------|------|-----------------|-----------|---------|
| `GET` | `/v1/employees/{employeeId}/payschedule` | `schema:components/PagedResultOfPayPeriod` | `PagedResultOfPayPeriodDataObject` | `root` |
| `GET` | `/v1/employees/{employeeId}/payschedule` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/payschedule` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/payschedule` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/payschedule` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/schedules` | `schema:anon/3d34c272b33f6c79a137e25e4b69f54396f8b60e` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/schedules` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/schedules` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/schedules` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/schedules` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/employees/{employeeId}/schedules` | `schema:components/CreateOrUpdateResponse` | `CreateOrUpdateResponseDataObject` | `root` |
| `POST` | `/v1/employees/{employeeId}/schedules` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/employees/{employeeId}/schedules` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/employees/{employeeId}/schedules` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `POST` | `/v1/employees/{employeeId}/schedules` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalEntities/{legalEntityId}/schedules` | `schema:components/PagedResultOfEmployeeSchedule` | `PagedResultOfEmployeeScheduleDataObject` | `root` |
| `GET` | `/v1/legalEntities/{legalEntityId}/schedules` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalEntities/{legalEntityId}/schedules` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalEntities/{legalEntityId}/schedules` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/legalEntities/{legalEntityId}/schedules` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/schedules/{scheduleId}` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/schedules/{scheduleId}` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/schedules/{scheduleId}` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/schedules/{scheduleId}` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/SchedulingJobs` | `schema:components/PagedResultOfSchedulingJob` | `PagedResultOfSchedulingJobDataObject` | `root` |
| `GET` | `/v1/legalentities/{legalEntityId}/SchedulingJobs` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/SchedulingJobs` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/SchedulingJobs` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/SchedulingJobs` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/schedulingShifts` | `schema:components/PagedResultOfSchedulingShift` | `PagedResultOfSchedulingShiftDataObject` | `root` |
| `GET` | `/v1/legalentities/{legalEntityId}/schedulingShifts` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/schedulingShifts` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/schedulingShifts` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/schedulingShifts` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/schedulingShifts` | `schema:components/CreateSchedulingShiftsResponse` | `CreateSchedulingShiftsResponseDataObject` | `root` |
| `POST` | `/v1/legalentities/{legalEntityId}/schedulingShifts` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/schedulingShifts` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/schedulingShifts` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/schedulingShifts` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/schedulingShifts/{shiftId}` | `schema:components/SchedulingShift` | `SchedulingShift` | `nested_only` |
| `GET` | `/v1/legalentities/{legalEntityId}/schedulingShifts/{shiftId}` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/schedulingShifts/{shiftId}` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/schedulingShifts/{shiftId}` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/schedulingShifts/{shiftId}` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/legalentities/{legalEntityId}/schedulingShifts/{shiftId}` | `schema:components/CreateOrUpdateResponse` | `CreateOrUpdateResponseDataObject` | `root` |
| `PUT` | `/v1/legalentities/{legalEntityId}/schedulingShifts/{shiftId}` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/legalentities/{legalEntityId}/schedulingShifts/{shiftId}` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/legalentities/{legalEntityId}/schedulingShifts/{shiftId}` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `PUT` | `/v1/legalentities/{legalEntityId}/schedulingShifts/{shiftId}` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/legalentities/{legalEntityId}/schedulingShifts/{shiftId}` | `schema:anon/bf21a9e8fbc5a3846fb05b4fa0859e0917b2202f` | `` | `missing` |
| `DELETE` | `/v1/legalentities/{legalEntityId}/schedulingShifts/{shiftId}` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/legalentities/{legalEntityId}/schedulingShifts/{shiftId}` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/legalentities/{legalEntityId}/schedulingShifts/{shiftId}` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/legalentities/{legalEntityId}/schedulingShifts/{shiftId}` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `DELETE` | `/v1/legalentities/{legalEntityId}/schedulingShifts/{shiftId}` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalEntities/{legalEntityId}/punches` | `schema:components/PagedResultOfTimeCardV3` | `PagedResultOfTimeCardV3DataObject` | `root` |
| `GET` | `/v1/legalEntities/{legalEntityId}/punches` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalEntities/{legalEntityId}/punches` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalEntities/{legalEntityId}/punches` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/legalEntities/{legalEntityId}/punches` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/punches` | `schema:components/PagedResultOfTimeCardV3` | `PagedResultOfTimeCardV3DataObject` | `root` |
| `GET` | `/v1/employees/{employeeId}/punches` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/punches` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/punches` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/punches` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/timeoffaccruals` | `schema:components/PagedResultOfEmployeeBalance` | `PagedResultOfEmployeeBalanceDataObject` | `root` |
| `GET` | `/v1/employees/{employeeId}/timeoffaccruals` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/timeoffaccruals` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/timeoffaccruals` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/timeoffaccruals` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeoffaccruals` | `schema:components/PagedResultOfEmployeeBalance` | `PagedResultOfEmployeeBalanceDataObject` | `root` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeoffaccruals` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeoffaccruals` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeoffaccruals` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeoffaccruals` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/employees/{employeeId}/timeoffplanassignment` | `schema:components/CreateOrUpdateResponse` | `CreateOrUpdateResponseDataObject` | `root` |
| `POST` | `/v1/employees/{employeeId}/timeoffplanassignment` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/employees/{employeeId}/timeoffplanassignment` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/employees/{employeeId}/timeoffplanassignment` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `POST` | `/v1/employees/{employeeId}/timeoffplanassignment` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/timeoffplanassignment` | `schema:components/CreateOrUpdateResponse` | `CreateOrUpdateResponseDataObject` | `root` |
| `PUT` | `/v1/employees/{employeeId}/timeoffplanassignment` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/timeoffplanassignment` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/timeoffplanassignment` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/timeoffplanassignment` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/timeoffplanassignment` | `schema:components/CreateOrUpdateResponse` | `CreateOrUpdateResponseDataObject` | `root` |
| `DELETE` | `/v1/employees/{employeeId}/timeoffplanassignment` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/timeoffplanassignment` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/timeoffplanassignment` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/timeoffplanassignment` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/timeoffplanassignment` | `schema:anon/74cf2338a43d073736096fc40344446b0b1ef340` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/timeoffplanassignment` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/timeoffplanassignment` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/timeoffplanassignment` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/timeoffplanassignment` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/timeoffplanassignment/startingbalance` | `schema:components/CreateOrUpdateResponse` | `CreateOrUpdateResponseDataObject` | `root` |
| `PUT` | `/v1/employees/{employeeId}/timeoffplanassignment/startingbalance` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/timeoffplanassignment/startingbalance` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/timeoffplanassignment/startingbalance` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/timeoffplanassignment/startingbalance` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/timeoffrequests` | `schema:components/PagedResultOfEmployeeTimeOffRequest` | `PagedResultOfEmployeeTimeOffRequestDataObject` | `root` |
| `GET` | `/v1/employees/{employeeId}/timeoffrequests` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/timeoffrequests` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/timeoffrequests` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/timeoffrequests` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/schedulegroups` | `schema:components/PagedResultOfScheduleGroup` | `PagedResultOfScheduleGroupDataObject` | `root` |
| `GET` | `/v1/legalentities/{legalEntityId}/schedulegroups` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/schedulegroups` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/schedulegroups` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/schedulegroups` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/CreatePunches` | `schema:components/CreateOrUpdateResponse` | `CreateOrUpdateResponseDataObject` | `root` |
| `POST` | `/v1/legalentities/{legalEntityId}/CreatePunches` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/CreatePunches` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/CreatePunches` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/CreatePunches` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/CreateHours` | `schema:components/CreateOrUpdateResponse` | `CreateOrUpdateResponseDataObject` | `root` |
| `POST` | `/v1/legalentities/{legalEntityId}/CreateHours` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/CreateHours` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/CreateHours` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/CreateHours` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/punchErrorLog/{trackingId}` | `schema:components/PagedResultOfPunchErrorLog` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/punchErrorLog/{trackingId}` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/punchErrorLog/{trackingId}` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/punchErrorLog/{trackingId}` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/punchErrorLog/{trackingId}` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/HourErrorLog/{trackingId}` | `schema:components/PagedResultOfHourErrorLog` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/HourErrorLog/{trackingId}` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/HourErrorLog/{trackingId}` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/HourErrorLog/{trackingId}` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/HourErrorLog/{trackingId}` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/payItemErrorLog/{trackingId}` | `schema:components/PagedResultOfPayItemErrorLog` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/payItemErrorLog/{trackingId}` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/payItemErrorLog/{trackingId}` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/payItemErrorLog/{trackingId}` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/payItemErrorLog/{trackingId}` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/payItems` | `schema:components/PagedResultOfPayItem` | `PagedResultOfPayItemDataObject` | `root` |
| `GET` | `/v1/legalentities/{legalEntityId}/payItems` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/payItems` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/payItems` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/payItems` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/CreatePayItems` | `schema:components/CreateOrUpdateResponse` | `CreateOrUpdateResponseDataObject` | `root` |
| `POST` | `/v1/legalentities/{legalEntityId}/CreatePayItems` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/CreatePayItems` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/CreatePayItems` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/CreatePayItems` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/employeePunches` | `schema:anon/9af3b2f89c0503483bc23b2f3021cb06f10b1898` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/employeePunches` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/employeePunches` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/employeePunches` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/employeePunches` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/DeletePunches` | `schema:components/CreateOrUpdateResponse` | `CreateOrUpdateResponseDataObject` | `root` |
| `DELETE` | `/v1/employees/{employeeId}/DeletePunches` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/DeletePunches` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/DeletePunches` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/DeletePunches` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/unassignedpunches` | `schema:components/PagedResultOfUnassignedTimeCardPunch` | `PagedResultOfUnassignedTimeCardPunchDataObject` | `root` |
| `GET` | `/v1/legalentities/{legalEntityId}/unassignedpunches` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/unassignedpunches` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/unassignedpunches` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/unassignedpunches` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/employeeHours` | `schema:anon/55dc7353fd994a8d6a4ccfa820a7fb76616b6cd2` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/employeeHours` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/employeeHours` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/employeeHours` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/employeeHours` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/updatePunches` | `schema:components/CreateOrUpdateResponse` | `CreateOrUpdateResponseDataObject` | `root` |
| `PUT` | `/v1/employees/{employeeId}/updatePunches` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/updatePunches` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/updatePunches` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/updatePunches` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/UpdateHours` | `schema:components/CreateOrUpdateResponse` | `CreateOrUpdateResponseDataObject` | `root` |
| `PUT` | `/v1/employees/{employeeId}/UpdateHours` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/UpdateHours` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/UpdateHours` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/UpdateHours` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/DeletePayItems` | `schema:components/CreateOrUpdateResponse` | `CreateOrUpdateResponseDataObject` | `root` |
| `DELETE` | `/v1/employees/{employeeId}/DeletePayItems` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/DeletePayItems` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/DeletePayItems` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/DeletePayItems` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/DeleteHours` | `schema:components/CreateOrUpdateResponse` | `CreateOrUpdateResponseDataObject` | `root` |
| `DELETE` | `/v1/employees/{employeeId}/DeleteHours` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/DeleteHours` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/DeleteHours` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/DeleteHours` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/updatePayItems` | `schema:components/CreateOrUpdateResponse` | `CreateOrUpdateResponseDataObject` | `root` |
| `PUT` | `/v1/employees/{employeeId}/updatePayItems` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/updatePayItems` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/updatePayItems` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/updatePayItems` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/missedPunchRequests` | `schema:components/PagedResultOfMissedPunchRequest` | `PagedResultOfMissedPunchRequestDataObject` | `root` |
| `GET` | `/v1/legalentities/{legalEntityId}/missedPunchRequests` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/missedPunchRequests` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/missedPunchRequests` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/missedPunchRequests` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/reasonCodes` | `schema:components/PagedResultOfReasonCode` | `PagedResultOfReasonCodeDataObject` | `root` |
| `GET` | `/v1/legalentities/{legalEntityId}/reasonCodes` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/reasonCodes` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/reasonCodes` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/reasonCodes` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/legalentities/{legalEntityId}/approveOrDenyMissedPunchRequests` | `schema:components/CreateOrUpdateResponse` | `CreateOrUpdateResponseDataObject` | `root` |
| `PUT` | `/v1/legalentities/{legalEntityId}/approveOrDenyMissedPunchRequests` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/legalentities/{legalEntityId}/approveOrDenyMissedPunchRequests` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/legalentities/{legalEntityId}/approveOrDenyMissedPunchRequests` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `PUT` | `/v1/legalentities/{legalEntityId}/approveOrDenyMissedPunchRequests` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/createMissedPunchRequests` | `schema:components/CreateOrUpdateResponse` | `CreateOrUpdateResponseDataObject` | `root` |
| `POST` | `/v1/legalentities/{legalEntityId}/createMissedPunchRequests` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/createMissedPunchRequests` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/createMissedPunchRequests` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/createMissedPunchRequests` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/employeePunchProfileData` | `schema:components/EmployeePunchProfileData` | `EmployeePunchProfileDataDataObject` | `root` |
| `GET` | `/v1/employees/{employeeId}/employeePunchProfileData` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/employeePunchProfileData` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/employeePunchProfileData` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/employeePunchProfileData` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/employeePolicyGroupData` | `schema:components/PolicyGroup` | `PolicyGroupDataObject` | `root` |
| `GET` | `/v1/employees/{employeeId}/employeePolicyGroupData` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/employeePolicyGroupData` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/employeePolicyGroupData` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/employees/{employeeId}/employeePolicyGroupData` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeoffplans` | `schema:components/PagedResultOfTimeOffPlan` | `PagedResultOfTimeOffPlanDataObject` | `root` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeoffplans` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeoffplans` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeoffplans` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeoffplans` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeoffrequests` | `schema:components/PagedResultOfEmployeeTimeOffRequest` | `PagedResultOfEmployeeTimeOffRequestDataObject` | `root` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeoffrequests` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeoffrequests` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeoffrequests` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeoffrequests` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeoffRequests/{timeoffRequestId}` | `schema:components/EmployeeTimeOffRequest` | `EmployeeTimeOffRequest` | `nested_only` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeoffRequests/{timeoffRequestId}` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeoffRequests/{timeoffRequestId}` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeoffRequests/{timeoffRequestId}` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeoffRequests/{timeoffRequestId}` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/timeOffRequests` | `schema:components/CreateOrUpdateResponse` | `CreateOrUpdateResponseDataObject` | `root` |
| `POST` | `/v1/legalentities/{legalEntityId}/timeOffRequests` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/timeOffRequests` | `schema:components/PaycorError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/timeOffRequests` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `POST` | `/v1/legalentities/{legalEntityId}/timeOffRequests` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/DeleteTimeOffRequests` | `schema:components/CreateOrUpdateResponse` | `CreateOrUpdateResponseDataObject` | `root` |
| `DELETE` | `/v1/employees/{employeeId}/DeleteTimeOffRequests` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/DeleteTimeOffRequests` | `schema:components/PaycorError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/DeleteTimeOffRequests` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `DELETE` | `/v1/employees/{employeeId}/DeleteTimeOffRequests` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/UpdateTimeOffRequests` | `schema:components/CreateOrUpdateResponse` | `CreateOrUpdateResponseDataObject` | `root` |
| `PUT` | `/v1/employees/{employeeId}/UpdateTimeOffRequests` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/UpdateTimeOffRequests` | `schema:components/PaycorError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/UpdateTimeOffRequests` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `PUT` | `/v1/employees/{employeeId}/UpdateTimeOffRequests` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeOffRequestsErrorLog/{trackingId}` | `schema:anon/9e1d18186f6aefd998ef56d059d69300e305a697` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeOffRequestsErrorLog/{trackingId}` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeOffRequestsErrorLog/{trackingId}` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeOffRequestsErrorLog/{trackingId}` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeOffRequestsErrorLog/{trackingId}` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeofftypes` | `schema:components/PagedResultOfTimeOffType` | `PagedResultOfTimeOffTypeDataObject` | `root` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeofftypes` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeofftypes` | `schema:components/PaycorError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeofftypes` | `schema:components/PaycorRateLimitError` | `` | `missing` |
| `GET` | `/v1/legalentities/{legalEntityId}/timeofftypes` | `schema:components/PaycorError` | `` | `missing` |

## Unmapped Schemas

- `schema:anon/3d34c272b33f6c79a137e25e4b69f54396f8b60e`
- `schema:anon/55dc7353fd994a8d6a4ccfa820a7fb76616b6cd2`
- `schema:anon/74cf2338a43d073736096fc40344446b0b1ef340`
- `schema:anon/9af3b2f89c0503483bc23b2f3021cb06f10b1898`
- `schema:anon/9e1d18186f6aefd998ef56d059d69300e305a697`
- `schema:anon/bf21a9e8fbc5a3846fb05b4fa0859e0917b2202f`
- `schema:components/PagedResultOfHourErrorLog`
- `schema:components/PagedResultOfPayItemErrorLog`
- `schema:components/PagedResultOfPunchErrorLog`
- `schema:components/PaycorError`
- `schema:components/PaycorRateLimitError`
