# PortalDailyStatistic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**costs** | [**list[Cost]**](Cost.md) | Gets the total cost of approved projects, by currency, created on this day. | [optional] 
**_date** | **datetime** | Gets the date for which these statistics apply. | [optional] 
**language_pairs** | [**list[PortalLanguagePairWordCount]**](PortalLanguagePairWordCount.md) | Gets the language pairs and the number of words for that language in approved projects created on this day. | [optional] 
**leverage** | **dict(str, int)** | Gets the Translation Memory leverage category and the number of words in that category in approved projects created on this day. | [optional] 
**overall_leverage** | **float** | Gets the overall Translation Memory leverage in approved projects created on this day. | [optional] 
**savings** | [**list[Cost]**](Cost.md) | Gets the total value of any Translation Memory related cost savings, by currency, in approved projects created on this day. | [optional] 
**total_files** | **int** | Gets the total number of target-language files in approved projects created on this day. | [optional] 
**total_projects** | **int** | Gets total number of approved projects created on this day. | [optional] 
**total_words** | **int** | Gets the total words in approved projects created on this day. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

