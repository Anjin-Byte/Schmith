# PubChangeOrderResponseDataObject

## PubChangeOrderResponseDataObject
- Role: parent
- Schema Name: PubChangeOrderResponse
- Schema ID: schema:components/PubChangeOrderResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `title` | `string` |
| `changeOrderNumber` | `int` |
| `changeOrderValue` | `double` |
| `reason` | `string` |
| `contractId` | `int` |
| `dateApproved` | `string` |
| `dateCreated` | `string` |
| `dateUpdated` | `string` |
| `status` | `PubChangeOrderResponseStatus` |
| `description` | `string` |
| `changeOrderCode` | `string` |
| `contractCode` | `string` |
| `contractNumber` | `int` |
| `approvalDate` | `string` |
| `history` | `PubChangeOrderHistoryResponse[]` |
| `isCreatedByVendor` | `bool` |
| `sentToAccountingFlag` | `bool` |
| `sentToAccountingTimeStamp` | `string` |
| `sentToAccountingUserId` | `int` |
| `costScheduleId` | `int` |
| `approvalWorkflow` | `ApprovalWorkflowResponse` |
| `costDetails` | `PubCostDetailResponse[]` |

### Nested Types
- `ApprovalWorkflowItemResponse`
- `ApprovalWorkflowItemResponseStatus`
- `ApprovalWorkflowResponse`
- `ApprovalWorkflowResponseStatus`
- `PubAccountingCodeResponse`
- `PubChangeOrderHistoryResponse`
- `PubChangeOrderHistoryResponseAction`
- `PubChangeOrderResponseStatus`
- `PubCostDetailResponse`

## ApprovalWorkflowItemResponse
- Role: nested
- Parent: PubChangeOrderResponseDataObject
- Schema Name: ApprovalWorkflowItemResponse
- Schema ID: schema:components/ApprovalWorkflowItemResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `approvalWorkflowId` | `int` |
| `status` | `ApprovalWorkflowItemResponseStatus` |
| `approvalUserId` | `int` |
| `ordinal` | `int` |
| `comment` | `string` |
| `statusDate` | `string` |
| `userId` | `int` |
| `firstName` | `string` |
| `lastName` | `string` |

## ApprovalWorkflowItemResponseStatus
- Role: nested
- Parent: PubChangeOrderResponseDataObject
- Schema Name: ApprovalWorkflowItemResponseStatus
- Schema ID: schema:anon/12281169ae29eabab242b3fd278c8272916b5d00

### Enum

Values: pending, approved, rejected

## ApprovalWorkflowResponse
- Role: nested
- Parent: PubChangeOrderResponseDataObject
- Schema Name: ApprovalWorkflowResponse
- Schema ID: schema:components/ApprovalWorkflowResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `status` | `ApprovalWorkflowResponseStatus` |
| `publishedUserId` | `int` |
| `firstName` | `string` |
| `lastName` | `string` |
| `dateCreated` | `string` |
| `approvalWorkflowItems` | `ApprovalWorkflowItemResponse[]` |

## ApprovalWorkflowResponseStatus
- Role: nested
- Parent: PubChangeOrderResponseDataObject
- Schema Name: ApprovalWorkflowResponseStatus
- Schema ID: schema:anon/13ab6cdf8ff5de14ef09152b0a5acd89901563f7

### Enum

Values: pending, approved, canceled, rejected

## PubAccountingCodeResponse
- Role: nested
- Parent: PubChangeOrderResponseDataObject
- Schema Name: PubAccountingCodeResponse
- Schema ID: schema:components/PubAccountingCodeResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `label` | `string` |
| `accountCode` | `string` |
| `jobType` | `string` |
| `phaseCode` | `string` |
| `entityCode` | `string` |
| `costCategory` | `string` |
| `costList` | `string` |
| `costCode` | `string` |

## PubChangeOrderHistoryResponse
- Role: nested
- Parent: PubChangeOrderResponseDataObject
- Schema Name: PubChangeOrderHistoryResponse
- Schema ID: schema:components/PubChangeOrderHistoryResponse

### Fields

| Field | Type |
|------|------|
| `userId` | `int` |
| `userName` | `string` |
| `companyName` | `string` |
| `actionDate` | `string` |
| `createdDate` | `string` |
| `action` | `PubChangeOrderHistoryResponseAction` |
| `newStatus` | `PubChangeOrderResponseStatus` |
| `reason` | `string` |
| `companyVendorContactId` | `int` |

## PubChangeOrderHistoryResponseAction
- Role: nested
- Parent: PubChangeOrderResponseDataObject
- Schema Name: PubChangeOrderHistoryResponseAction
- Schema ID: schema:anon/a711254531da35dbb8bc069916fb8371f5b06e06

### Enum

Values: created, updated

## PubChangeOrderResponseStatus
- Role: nested
- Parent: PubChangeOrderResponseDataObject
- Schema Name: PubChangeOrderResponseStatus
- Schema ID: schema:anon/1353e159f3139f31dfbb5a96623dcf1f1d192b82

### Enum

Values: pending, approved, rejected, closed, potential, reviewed

## PubCostDetailResponse
- Role: nested
- Parent: PubChangeOrderResponseDataObject
- Schema Name: PubCostDetailResponse
- Schema ID: schema:components/PubCostDetailResponse
- Primary Key: Id

### Fields

| Field | Type |
|------|------|
| `id` | `int` |
| `costScheduleId` | `int` |
| `cost` | `double` |
| `label` | `string` |
| `accountingCode` | `PubAccountingCodeResponse` |
| `dateCreated` | `string` |
| `dateUpdated` | `string` |
