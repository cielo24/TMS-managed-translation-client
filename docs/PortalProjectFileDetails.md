# PortalProjectFileDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotated_file_id** | **str** | The unique identifier of the annotated source file if one exists. Used by the In-Context Review functionality if available. | [optional] 
**annotated_file_stored_date** | **datetime** | The date the annotated source file was stored. | [optional] 
**assignees** | [**PortalGroup**](PortalGroup.md) |  | [optional] 
**authorized_date** | **datetime** | The date the file was authorized. | [optional] 
**can_be_cancelled** | **bool** | Indicates whether the file can be cancelled. | [optional] 
**cost** | **float** | The total cost for translating the file. | [optional] 
**cost_attributes** | [**list[PortalCostAttribute]**](PortalCostAttribute.md) | Gets or sets the cost attributes. | [optional] 
**cost_bands** | [**list[PortalCostBand]**](PortalCostBand.md) | Gets or sets the cost bands associated with the file. | [optional] 
**cost_matrix_name** | **str** | The name of the cost model used to calculate the translation costs for the file. | [optional] 
**folder** | **str** | The relative path of the file established when the project is created from a zip file, a connector or an integration. | [optional] 
**fuzzy_words** | **int** | The total number of words for the file receiving a fuzzy match from the translation memory during preparation. | [optional] 
**hundred_words** | **int** | The total number of words for the file receiving a one hundred percent match from the translation memory during preparation. | [optional] 
**id** | **str** | The unique identifider of the file in the associated target language. | [optional] 
**in_context_preview_status** | **str** | The status of the In-Context Review feature for the file. Values can be NotRequired, InProgress, AnnotatedFileDownloadFailed, AnnotatedFileDownloaded, PreviewCompleted | [optional] 
**locked_words** | **int** | The total number of words marked as locked during preparation. | [optional] 
**name** | **str** | The name of the file, without any preceeding path information. | [optional] 
**new_words** | **int** | The total number of words for the file receiving no match from the translation memory during preparation. | [optional] 
**owner** | [**PortalOwner**](PortalOwner.md) |  | [optional] 
**perfect_match_words** | **int** | The total number of words for the file receiving a pefect match from the translation memory during preparation. | [optional] 
**portal_reviewers** | [**list[PortalReviewer]**](PortalReviewer.md) | Gets or sets the review information. | [optional] 
**portal_signoffers** | [**list[PortalSignoffer]**](PortalSignoffer.md) | Gets or sets the signoff information. | [optional] 
**rejected** | **bool** | Gets or sets the task reject status. | [optional] 
**repeated_words** | **int** | The total number of words for the file considered to be repeated during preparation. | [optional] 
**source_id** | **str** | The unique identifier of the source file associated with the file. | [optional] 
**status** | **str** | The status of the file within the workflow.0 &#x3D; Preparing, 1 &#x3D; ForApproval, 2 &#x3D; InProgress, 3 &#x3D; ForDownload, 4 &#x3D; Completed, 5 &#x3D; PartialDownload, 6 &#x3D; InReview, 7 &#x3D; Reviewed, 8 &#x3D; InSignOff, 9 &#x3D; SignedOff, 10 &#x3D; ForVendorSelection, 11 &#x3D; Cancelled, 12 &#x3D; New | [optional] 
**status_detail** | **str** | Gets or sets the workflow status detail. | [optional] 
**status_id** | **str** | Gets or sets the workflow stage status id. | [optional] 
**status_type** | **str** | Gets or sets the workflow status type. | [optional] 
**target_language** | [**PortalLanguage**](PortalLanguage.md) |  | [optional] 
**task_id** | **str** | Gets or sets the identifier. | [optional] 
**tm_leverage** | **float** | Gets or sets the tm leverage. | [optional] 
**tm_savings** | **float** | Gets or sets the tm savings. | [optional] 
**total_words** | **int** | Gets the total words. | [optional] 
**workflow_attributes** | [**list[PortalWorkflowAttribute]**](PortalWorkflowAttribute.md) | Gets or sets the workflow attributes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

