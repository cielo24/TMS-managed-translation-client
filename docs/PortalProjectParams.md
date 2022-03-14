# PortalProjectParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Gets or sets the description for the project. | [optional] 
**due_date** | **datetime** | Gets or sets the due date. | [optional] 
**files** | [**list[ProjectFile]**](ProjectFile.md) | Gets the files to be included in the project. | [optional] 
**metadata** | [**list[ProjectMetadata]**](ProjectMetadata.md) | Gets or sets the metadata. | [optional] 
**name** | **str** | Gets or sets the name of the project. | 
**project_group_id** | **str** | Gets or sets the project group uniqueidentifier | [optional] 
**project_options_id** | **str** | Gets or sets the project options identifier. | 
**scope_option_id** | **str** | Gets or sets the scope option identifier. | [optional] 
**src_lang** | **str** | Gets or sets the source language for the project.                          A project can support only one source language, therefore we assume that all files within the project contain content             in the specified source language.             The value supplied here should be taken from the             PortalLanguage.CultureCode property. | 
**tgt_langs** | **list[str]** | Gets or sets the target languages that apply to the files supplied in .                          The values supplied here should be taken from the             PortalLanguage.CultureCode property. | [optional] 
**tm_sequence_id** | **str** | Gets or sets the tm sequence identifier. | [optional] 
**vendors** | **list[str]** | Gets the vendor ids to be associated with this project. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


