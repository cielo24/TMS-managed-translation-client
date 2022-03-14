# PortalProjectLanguageStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**list[PortalProjectFileDetails]**](PortalProjectFileDetails.md) | The files assocaited with the language. | [optional] 
**fuzzy_words** | **int** | The total number of words for the language receiving a fuzzy match from the translation memory during preparation. | [optional] 
**hundred_words** | **int** | The total number of words for the language receiving a one hundred percent match from the translation memory during preparation. | [optional] 
**language** | [**PortalLanguage**](PortalLanguage.md) | The associated target language within the project. | [optional] 
**locked_words** | **int** | The total number of words for the language considered to be locked during preparation. | [optional] 
**new_words** | **int** | The total number of words for the language receiving no match from the translation memory during preparation. | [optional] 
**percent_complete** | **int** | A summary value indicating the approximate completion percentage of the language. Often this value is calculated from the number of files which have reached the ForDownload status. | [optional] 
**perfect_match_words** | **int** | The total number of words for the language receiving no match from the translation memory during preparation. | [optional] 
**repeated_words** | **int** | The total number of words for the language considered to be repeated during preparation. | [optional] 
**tm_leverage** | **float** | The overall percentage of words leverage from Translation Memory during preparation. | [optional] 
**tm_savings** | **float** | The financial value of any saving derived from the use of Translation Memory for the language. | [optional] 
**total_cost** | **float** | The total cost for the language. | [optional] 
**total_words** | **int** | The total number of words to be translated for the language. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


