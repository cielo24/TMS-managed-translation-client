# swagger_client.TranslationMemoryApi

All URIs are relative to *https://languagecloud.sdl.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translation_memory_get_tm_search_options**](TranslationMemoryApi.md#translation_memory_get_tm_search_options) | **GET** /tm4lc/api/v1/tm/options/{requestInheritedConfigs} | Get Tm Search Options
[**translation_memory_search_by_file**](TranslationMemoryApi.md#translation_memory_search_by_file) | **POST** /tm4lc/api/v1/tm/search/file/{fileId} | Search By File
[**translation_memory_search_by_project_option**](TranslationMemoryApi.md#translation_memory_search_by_project_option) | **POST** /tm4lc/api/v1/tm/search/{projectOptionsId} | Search By Project Option
[**translation_memory_update_by_file**](TranslationMemoryApi.md#translation_memory_update_by_file) | **POST** /tm4lc/api/v1/tm/update/file/{fileId} | Update By File
[**translation_memory_update_by_project_option**](TranslationMemoryApi.md#translation_memory_update_by_project_option) | **POST** /tm4lc/api/v1/tm/update/{projectOptionsId} | Update By Project Option

# **translation_memory_get_tm_search_options**
> list[PortalTmOptions] translation_memory_get_tm_search_options(request_inherited_configs)

Get Tm Search Options

Gets the available translation memory search options  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TranslationMemoryApi(swagger_client.ApiClient(configuration))
request_inherited_configs = true # bool | Use inherited configs.

try:
    # Get Tm Search Options
    api_response = api_instance.translation_memory_get_tm_search_options(request_inherited_configs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->translation_memory_get_tm_search_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_inherited_configs** | **bool**| Use inherited configs. | 

### Return type

[**list[PortalTmOptions]**](PortalTmOptions.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translation_memory_search_by_file**
> list[TmSearchResult] translation_memory_search_by_file(body, file_id)

Search By File

Performs a Tm search against the translation memories associated with the specified file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TranslationMemoryApi(swagger_client.ApiClient(configuration))
body = swagger_client.TmSearchParams() # TmSearchParams | The search parameters.
file_id = 'file_id_example' # str | The file identifier.

try:
    # Search By File
    api_response = api_instance.translation_memory_search_by_file(body, file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->translation_memory_search_by_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TmSearchParams**](TmSearchParams.md)| The search parameters. | 
 **file_id** | **str**| The file identifier. | 

### Return type

[**list[TmSearchResult]**](TmSearchResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translation_memory_search_by_project_option**
> list[TmSearchResult] translation_memory_search_by_project_option(body, project_options_id)

Search By Project Option

Performs a Tm search against the translation memories associated with the specified project option.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TranslationMemoryApi(swagger_client.ApiClient(configuration))
body = swagger_client.TmSearchParams() # TmSearchParams | The search parameters.
project_options_id = 'project_options_id_example' # str | The project options identifier.

try:
    # Search By Project Option
    api_response = api_instance.translation_memory_search_by_project_option(body, project_options_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->translation_memory_search_by_project_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TmSearchParams**](TmSearchParams.md)| The search parameters. | 
 **project_options_id** | **str**| The project options identifier. | 

### Return type

[**list[TmSearchResult]**](TmSearchResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translation_memory_update_by_file**
> bool translation_memory_update_by_file(body, file_id)

Update By File

Performs a Tm update against the translation memories associated with the specified file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TranslationMemoryApi(swagger_client.ApiClient(configuration))
body = swagger_client.TmUpdateParams() # TmUpdateParams | The update parameters.
file_id = 'file_id_example' # str | The file identifier.

try:
    # Update By File
    api_response = api_instance.translation_memory_update_by_file(body, file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->translation_memory_update_by_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TmUpdateParams**](TmUpdateParams.md)| The update parameters. | 
 **file_id** | **str**| The file identifier. | 

### Return type

**bool**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translation_memory_update_by_project_option**
> bool translation_memory_update_by_project_option(body, project_options_id)

Update By Project Option

Performs a Tm update against the translation memories associated with the specified project option.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TranslationMemoryApi(swagger_client.ApiClient(configuration))
body = swagger_client.TmUpdateParams() # TmUpdateParams | The update parameters.
project_options_id = 'project_options_id_example' # str | The project options identifier.

try:
    # Update By Project Option
    api_response = api_instance.translation_memory_update_by_project_option(body, project_options_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->translation_memory_update_by_project_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TmUpdateParams**](TmUpdateParams.md)| The update parameters. | 
 **project_options_id** | **str**| The project options identifier. | 

### Return type

**bool**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

