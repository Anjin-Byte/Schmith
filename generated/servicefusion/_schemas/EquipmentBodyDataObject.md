# EquipmentBodyDataObject

## EquipmentBodyDataObject
- Role: parent
- Schema Name: EquipmentBody
- Schema ID: schema:types/typ.EquipmentBody
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `string` |
| `type` | `string` |
| `make` | `string` |
| `model` | `string` |
| `sku` | `string` |
| `serial_number` | `string` |
| `location` | `string` |
| `notes` | `string` |
| `extended_warranty_provider` | `string` |
| `is_extended_warranty` | `bool` |
| `extended_warranty_date` | `DateTime` |
| `warranty_date` | `DateTime` |
| `install_date` | `DateTime` |
| `customer_location` | `string` |
| `custom_fields` | `CustomFieldBody[]` |

### Nested Types
- `CustomFieldBody`

## CustomFieldBody
- Role: nested
- Parent: EquipmentBodyDataObject
- Schema Name: CustomFieldBody
- Schema ID: schema:types/typ.CustomFieldBody

### Fields

| Field | Type |
|------|------|
| `name` | `string` |
| `value` | `JsonElement` |
