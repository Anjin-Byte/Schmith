# Schema Coverage Report: procore

**Generated:** 2026-02-01 14:11:51
**IR Source:** `/Users/taylorhale/Documents/dev_hub/Brynhild/repos/Schmith/ir/procore`

## Summary

| Metric | Count |
|--------|-------|
| Total schemas in spec | 141 |
| Generated DataObjects | 66 |
| Generated Roots | 22 |
| Nested-only Schemas | 26 |
| Filtered out | 75 |
| **Coverage** | **46.8%** |

## Filtered Schemas by Category

| Category | Count | Description |
|----------|-------|-------------|
| Anonymous/inline schemas | 75 | Intentionally excluded |

## Generated DataObjects (Eligible Schemas)

The following 66 schemas are eligible for generation (before root/nested split):

| # | DataObject Name | Schema ID |
|---|-----------------|-----------|
| 1 | `ApprovalWorkflowItemResponseDataObject` | `schema:components/ApprovalWorkflowItemResponse` |
| 2 | `ApprovalWorkflowResponseDataObject` | `schema:components/ApprovalWorkflowResponse` |
| 3 | `CompanyVendorContactPhoneRequestDataObject` | `schema:components/CompanyVendorContactPhoneRequest` |
| 4 | `OauthClientCredentialsResponseDataObject` | `schema:components/OauthClientCredentialsResponse` |
| 5 | `OauthFlowPostRequestDataObject` | `schema:components/OauthFlowPostRequest` |
| 6 | `OauthUserDataObject` | `schema:components/OauthUser` |
| 7 | `PagingOrderDataResponseDataObject` | `schema:components/PagingOrderDataResponse` |
| 8 | `PagingRequestDataObject` | `schema:components/PagingRequest` |
| 9 | `PagingResponsePubAccountingCodeDataObject` | `schema:components/PagingResponsePubAccountingCode` |
| 10 | `PagingResponsePubAccountingInvoiceDataObject` | `schema:components/PagingResponsePubAccountingInvoice` |
| 11 | `PagingResponsePubChangeOrderBaseResponseDataObject` | `schema:components/PagingResponsePubChangeOrderBaseResponse` |
| 12 | `PagingResponsePubCompanyBuildingResponseDataObject` | `schema:components/PagingResponsePubCompanyBuildingResponse` |
| 13 | `PagingResponsePubCompanyVendorContactResponseDataObject` | `schema:components/PagingResponsePubCompanyVendorContactResponse` |
| 14 | `PagingResponsePubCompanyVendorResponseDataObject` | `schema:components/PagingResponsePubCompanyVendorResponse` |
| 15 | `PagingResponsePubContractBaseResponseDataObject` | `schema:components/PagingResponsePubContractBaseResponse` |
| 16 | `PagingResponsePubInvoiceAccountingRawBaseResponseDataObject` | `schema:components/PagingResponsePubInvoiceAccountingRawBaseResponse` |
| 17 | `PagingResponsePubInvoiceBaseResponseDataObject` | `schema:components/PagingResponsePubInvoiceBaseResponse` |
| 18 | `PagingResponsePubJobBaseResponseDataObject` | `schema:components/PagingResponsePubJobBaseResponse` |
| 19 | `PagingResponsePubUserGetResponseDataObject` | `schema:components/PagingResponsePubUserGetResponse` |
| 20 | `PagingResponsePubUserJobGetResponseDataObject` | `schema:components/PagingResponsePubUserJobGetResponse` |
| 21 | `PubAccountingCodeDataObject` | `schema:components/PubAccountingCode` |
| 22 | `PubAccountingCodeResponseDataObject` | `schema:components/PubAccountingCodeResponse` |
| 23 | `PubAccountingInvoiceDataObject` | `schema:components/PubAccountingInvoice` |
| 24 | `PubAccountingInvoiceDetailDataObject` | `schema:components/PubAccountingInvoiceDetail` |
| 25 | `PubBidderResponseDataObject` | `schema:components/PubBidderResponse` |
| 26 | `PubBidroomPostRequestDataObject` | `schema:components/PubBidroomPostRequest` |
| 27 | `PubBidroomResponseDataObject` | `schema:components/PubBidroomResponse` |
| 28 | `PubChangeOrderBaseResponseDataObject` | `schema:components/PubChangeOrderBaseResponse` |
| 29 | `PubChangeOrderHistoryResponseDataObject` | `schema:components/PubChangeOrderHistoryResponse` |
| 30 | `PubChangeOrderPutStatusRequestDataObject` | `schema:components/PubChangeOrderPutStatusRequest` |
| 31 | `PubChangeOrderResponseDataObject` | `schema:components/PubChangeOrderResponse` |
| 32 | `PubCompanyBuildingRequestDataObject` | `schema:components/PubCompanyBuildingRequest` |
| 33 | `PubCompanyBuildingResponseDataObject` | `schema:components/PubCompanyBuildingResponse` |
| 34 | `PubCompanyVendorContactPhoneNumberResponseDataObject` | `schema:components/PubCompanyVendorContactPhoneNumberResponse` |
| 35 | `PubCompanyVendorContactRequestDataObject` | `schema:components/PubCompanyVendorContactRequest` |
| 36 | `PubCompanyVendorContactResponseDataObject` | `schema:components/PubCompanyVendorContactResponse` |
| 37 | `PubCompanyVendorRequestDataObject` | `schema:components/PubCompanyVendorRequest` |
| 38 | `PubCompanyVendorResponseDataObject` | `schema:components/PubCompanyVendorResponse` |
| 39 | `PubCompanyVendorTypeRequestDataObject` | `schema:components/PubCompanyVendorTypeRequest` |
| 40 | `PubContractBaseResponseDataObject` | `schema:components/PubContractBaseResponse` |
| 41 | `PubContractRequestDataObject` | `schema:components/PubContractRequest` |
| 42 | `PubContractResponseDataObject` | `schema:components/PubContractResponse` |
| 43 | `PubCostDetailResponseDataObject` | `schema:components/PubCostDetailResponse` |
| 44 | `PubInvoiceAccountingDetailRawPostRequestDataObject` | `schema:components/PubInvoiceAccountingDetailRawPostRequest` |
| 45 | `PubInvoiceAccountingDetailRawPutRequestDataObject` | `schema:components/PubInvoiceAccountingDetailRawPutRequest` |
| 46 | `PubInvoiceAccountingDetailRawResponseDataObject` | `schema:components/PubInvoiceAccountingDetailRawResponse` |
| 47 | `PubInvoiceAccountingRawBaseResponseDataObject` | `schema:components/PubInvoiceAccountingRawBaseResponse` |
| 48 | `PubInvoiceAccountingRawPostRequestDataObject` | `schema:components/PubInvoiceAccountingRawPostRequest` |
| 49 | `PubInvoiceAccountingRawPutRequestDataObject` | `schema:components/PubInvoiceAccountingRawPutRequest` |
| 50 | `PubInvoiceAccountingRawResponseDataObject` | `schema:components/PubInvoiceAccountingRawResponse` |
| 51 | `PubInvoiceBaseResponseDataObject` | `schema:components/PubInvoiceBaseResponse` |
| 52 | `PubInvoiceDetailResponseDataObject` | `schema:components/PubInvoiceDetailResponse` |
| 53 | `PubInvoicePutRequestDataObject` | `schema:components/PubInvoicePutRequest` |
| 54 | `PubInvoiceResponseDataObject` | `schema:components/PubInvoiceResponse` |
| 55 | `PubJobBaseResponseDataObject` | `schema:components/PubJobBaseResponse` |
| 56 | `PubJobItemResponseDataObject` | `schema:components/PubJobItemResponse` |
| 57 | `PubJobItemSectionResponseDataObject` | `schema:components/PubJobItemSectionResponse` |
| 58 | `PubJobRequestDataObject` | `schema:components/PubJobRequest` |
| 59 | `PubJobResponseDataObject` | `schema:components/PubJobResponse` |
| 60 | `PubMessageResponseDataObject` | `schema:components/PubMessageResponse` |
| 61 | `PubUserGetResponseDataObject` | `schema:components/PubUserGetResponse` |
| 62 | `PubUserJobDeleteRequestDataObject` | `schema:components/PubUserJobDeleteRequest` |
| 63 | `PubUserJobGetResponseDataObject` | `schema:components/PubUserJobGetResponse` |
| 64 | `PubUserJobPostRequestDataObject` | `schema:components/PubUserJobPostRequest` |
| 65 | `PubUserPostRequestDataObject` | `schema:components/PubUserPostRequest` |
| 66 | `UserResponseDataObject` | `schema:components/UserResponse` |

## Generated Roots (Standalone DataObjects)

The following 22 schemas produce standalone scaffolding:

| # | DataObject Name |
|---|-----------------|
| 1 | `OauthClientCredentialsResponseDataObject` |
| 2 | `OauthUserDataObject` |
| 3 | `PagingResponsePubAccountingCodeDataObject` |
| 4 | `PagingResponsePubAccountingInvoiceDataObject` |
| 5 | `PagingResponsePubChangeOrderBaseResponseDataObject` |
| 6 | `PagingResponsePubCompanyBuildingResponseDataObject` |
| 7 | `PagingResponsePubCompanyVendorContactResponseDataObject` |
| 8 | `PagingResponsePubCompanyVendorResponseDataObject` |
| 9 | `PagingResponsePubContractBaseResponseDataObject` |
| 10 | `PagingResponsePubInvoiceAccountingRawBaseResponseDataObject` |
| 11 | `PagingResponsePubInvoiceBaseResponseDataObject` |
| 12 | `PagingResponsePubJobBaseResponseDataObject` |
| 13 | `PagingResponsePubUserGetResponseDataObject` |
| 14 | `PagingResponsePubUserJobGetResponseDataObject` |
| 15 | `PubBidroomResponseDataObject` |
| 16 | `PubChangeOrderResponseDataObject` |
| 17 | `PubContractResponseDataObject` |
| 18 | `PubInvoiceAccountingRawResponseDataObject` |
| 19 | `PubInvoiceResponseDataObject` |
| 20 | `PubJobResponseDataObject` |
| 21 | `PubMessageResponseDataObject` |
| 22 | `PubUserPostRequestDataObject` |

## Nested-only Schemas

The following 26 schemas are included as nested types under roots:

| # | Schema Name |
|---|-------------|
| 1 | `ApprovalWorkflowItemResponse` |
| 2 | `ApprovalWorkflowResponse` |
| 3 | `PagingOrderDataResponse` |
| 4 | `PubAccountingCode` |
| 5 | `PubAccountingCodeResponse` |
| 6 | `PubAccountingInvoice` |
| 7 | `PubAccountingInvoiceDetail` |
| 8 | `PubBidderResponse` |
| 9 | `PubChangeOrderBaseResponse` |
| 10 | `PubChangeOrderHistoryResponse` |
| 11 | `PubCompanyBuildingResponse` |
| 12 | `PubCompanyVendorContactPhoneNumberResponse` |
| 13 | `PubCompanyVendorContactResponse` |
| 14 | `PubCompanyVendorResponse` |
| 15 | `PubContractBaseResponse` |
| 16 | `PubCostDetailResponse` |
| 17 | `PubInvoiceAccountingDetailRawResponse` |
| 18 | `PubInvoiceAccountingRawBaseResponse` |
| 19 | `PubInvoiceBaseResponse` |
| 20 | `PubInvoiceDetailResponse` |
| 21 | `PubJobBaseResponse` |
| 22 | `PubJobItemResponse` |
| 23 | `PubJobItemSectionResponse` |
| 24 | `PubUserGetResponse` |
| 25 | `PubUserJobGetResponse` |
| 26 | `UserResponse` |

## Filtered Schema Details

### Anonymous/inline schemas (75)

| Name | Schema ID |
|------|-----------|
| `None` | `schema:anon/0312c055a885bc39a5edfcbba7bc7b725891af9f` |
| `None` | `schema:anon/085d3aff93343af95c8250fc4901cfb159dc9ac5` |
| `None` | `schema:anon/0e7332eca9a208062e463d1840a71006b9c3b995` |
| `None` | `schema:anon/12281169ae29eabab242b3fd278c8272916b5d00` |
| `None` | `schema:anon/1353e159f3139f31dfbb5a96623dcf1f1d192b82` |
| `None` | `schema:anon/13ab6cdf8ff5de14ef09152b0a5acd89901563f7` |
| `None` | `schema:anon/13c38b99624adde11456c3cc928d62a2c62e9967` |
| `None` | `schema:anon/13db86838411001e586fd69f50b5b3376256c822` |
| `None` | `schema:anon/1581f3caa587364cf025503320cfb0b51756ccd6` |
| `None` | `schema:anon/1b20ec29acf0375af105bbc0234187715f4fb3f5` |
| `None` | `schema:anon/1b7c1dbdf101d0304a799df7b6b0eb166000fdb6` |
| `None` | `schema:anon/1d75d23dce4cf517a0e64ef4822b59408a327762` |
| `None` | `schema:anon/1e2da1e832eca3a6ed1e5c7aec1ebeca917ceed5` |
| `None` | `schema:anon/23b205236cfe7ea7fb79c4a1754e14109e0578ed` |
| `None` | `schema:anon/252bb802e141f32dab191a964c9cc53b679c742d` |
| `None` | `schema:anon/28a6976b44bb7a4a5478db8acdad01db3347dba5` |
| `None` | `schema:anon/327133f335a0382f20288ea00a033eb0d0d9c6cc` |
| `None` | `schema:anon/362b1f711c7ef6bd41727197e5a57fff47f84b94` |
| `None` | `schema:anon/3999e05b8b3d416c001ac8b25a8546a446de2cf4` |
| `None` | `schema:anon/402808f6f78708308f51a081444280c3cffc20dc` |
| `None` | `schema:anon/404a996d693b567ae6c2ed2e41a0af0185295b8d` |
| `None` | `schema:anon/4101dc02ed66cfa13b09ad8bc47d01636d5f658f` |
| `None` | `schema:anon/420dffc45c5ae6ec50224fd5f1a65ce78209dc23` |
| `None` | `schema:anon/4219ce0bc3728ec62275b0bd2a8ee31f53d14a77` |
| `None` | `schema:anon/43bdbac97542bb064b5429aedfed4e22e5acfdc6` |
| `None` | `schema:anon/46b0bec2264fb6eca3082b9ff341158a8c4a7c82` |
| `None` | `schema:anon/4a21f058d6199d19a3f42e1bf798a7f991070383` |
| `None` | `schema:anon/4b0d5310d0c74e79dbf00b4fb5b8893e343c9b08` |
| `None` | `schema:anon/4b1e54e81dd37daa7100b53d82cda1401924243f` |
| `None` | `schema:anon/4df23f6fcb2f843ba1603f8fd67bfbb0659b678d` |
| `None` | `schema:anon/4f7acea0a43a99f3bc82c544663899166a72a92c` |
| `None` | `schema:anon/4f94515bc2a16cdb600ea81b4fe9735492d8e3ed` |
| `None` | `schema:anon/500613f04f15954056fcc8e00fdabd25b285811b` |
| `None` | `schema:anon/535f2190951618a752bca794677b5e77933a3921` |
| `None` | `schema:anon/55df94d215c00f01c9d89f9e33494439ab87b7a3` |
| `None` | `schema:anon/5630e1e6a53cde273f361b152fd8262c996025fe` |
| `None` | `schema:anon/5b1cd5713a375e18bb93e9635b8a2dc5fc2672cf` |
| `None` | `schema:anon/5df94513aa6e646d7a36f8f1e1874d3ef889ce60` |
| `None` | `schema:anon/5ee1c00d8df2e117c693e9e4ac95d030084e2f70` |
| `None` | `schema:anon/63cc6ad725500751e8646cdb39a8573584f9de90` |
| `None` | `schema:anon/69e9bab1b4702f0716211a0fe0439293f2bf97e0` |
| `None` | `schema:anon/6ef8abd8ac2163e7db8cc3c6cfcf7d1590b11ed6` |
| `None` | `schema:anon/6f8befd3a7ac0a3b9c36ac95270ad5e64f0a615a` |
| `None` | `schema:anon/7219bb3b49bca44bf52fdfc440c4ccde12b5efe0` |
| `None` | `schema:anon/7eb9f57e49b44f841ea06ce89219107d5fca6775` |
| `None` | `schema:anon/89d9a33b86380ab29ca174859ec89150489b751c` |
| `None` | `schema:anon/8d99152896cb876d43f7b92ed3bb375178d17e81` |
| `None` | `schema:anon/8e3f77de77c0572d4e555e877de5ead9625ced02` |
| `None` | `schema:anon/934d03aa68aa78cdc4b2cc9faf2d3573af6908fe` |
| `None` | `schema:anon/94438e86ec1bbd3b43b8d2b67a39357814d6d0ad` |
| `None` | `schema:anon/974587ef512cdfdf02642d44fa98c5a73387e4ff` |
| `None` | `schema:anon/979a8281ac8b56925d931ee32ae3fcfa97d7daca` |
| `None` | `schema:anon/a36e6596d7e427a64e521580e850fba84c368c64` |
| `None` | `schema:anon/a711254531da35dbb8bc069916fb8371f5b06e06` |
| `None` | `schema:anon/ad5a99b66c3b5114bc90d6c456cea5d4d508bc6b` |
| `None` | `schema:anon/b97a0e88caefc6f0ddfd8bee3ad6f74808f0dd5b` |
| `None` | `schema:anon/ba27824ebdb9cfe0f2a4d626c06e741c56aeb6d9` |
| `None` | `schema:anon/bb2da9bf7898fc182de25d0b1a4b466023b7c9af` |
| `None` | `schema:anon/bf7996daa96dda162542c1e0b005355ec53e4232` |
| `None` | `schema:anon/c0504b8fa25f592cae324df5b2f1567e6c266b24` |
| `None` | `schema:anon/c3c0d74abf7b8f7fbc27cfb363ae01febd7e001c` |
| `None` | `schema:anon/c648ddf22add955dabeccc1b719ad7890156c725` |
| `None` | `schema:anon/c8d7af009a811a6d1611090cdaeffb58543cf96e` |
| `None` | `schema:anon/caa7697b51d28d2a13648b49784faa6e3975ad70` |
| `None` | `schema:anon/cd1b64103e65237e09146325d215aea5a0540e4e` |
| `None` | `schema:anon/cd432c5c6bd43aaa070aa268d1f585a78a335e25` |
| `None` | `schema:anon/d005f4d343e3145c9082cdbedab65effe3da2980` |
| `None` | `schema:anon/d456fd00e2852a078e269756bafa55c936c1863b` |
| `None` | `schema:anon/d9ae4f0129a526da08c620170aa24b4ab16f2e40` |
| `None` | `schema:anon/da8c7da2018b9436d358323ec9a3f24a2c05afae` |
| `None` | `schema:anon/db983a5a2db2b88ddfadd36b1608983e55a86f47` |
| `None` | `schema:anon/e7184cdd93d160eb8d1d97de1f01fff8c4c5bc57` |
| `None` | `schema:anon/f224db90930b1da5cfc1bd2c18ac347f598bd122` |
| `None` | `schema:anon/fd59d309968793604d7575cab61f7b300fc8fbe7` |
| `None` | `schema:anon/ff84999bb2109df07a74317287bf70c948176070` |

## Status

✅ **All schemas accounted for** - Every schema in the spec is either generated or intentionally filtered.