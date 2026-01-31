# CreateSchedulingShiftsResponseDataObject

## CreateSchedulingShiftsResponseDataObject
- Role: parent
- Schema Name: CreateSchedulingShiftsResponse
- Schema ID: schema:components/CreateSchedulingShiftsResponse

### Fields
- `shifts`: `SchedulingShiftResponseItem[]`

### Nested Types
- `SchedulingShiftResponseItem`

## SchedulingShiftResponseItem
- Role: nested
- Parent: CreateSchedulingShiftsResponseDataObject
- Schema Name: SchedulingShiftResponseItem
- Schema ID: schema:components/SchedulingShiftResponseItem

### Fields
- `shiftId`: `string`
- `shiftModelId`: `string`
- `warningsOrErrors`: `string[]`
