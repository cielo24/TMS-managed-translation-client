# swagger_client.ResourcesApi

All URIs are relative to *https://languagecloud.sdl.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resources_java_script_strings**](ResourcesApi.md#resources_java_script_strings) | **GET** /tm4lc/api/v1/resources/strings/{lang}/{version}/{userid} | Java Script Strings
[**resources_ui_languages**](ResourcesApi.md#resources_ui_languages) | **GET** /tm4lc/api/v1/resources/uilanguages | Ui Languages
[**resources_version**](ResourcesApi.md#resources_version) | **GET** /tm4lc/api/v1/resources/version | Version

# **resources_java_script_strings**
> dict(str, str) resources_java_script_strings(lang, version, userid)

Java Script Strings

Generates client side localized text as a JSON object.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesApi()
lang = 'lang_example' # str | The language.
version = 56 # int | The version - an unused parameter that enables cache busting.
userid = 'userid_example' # str | The current user identifier - an optional, unused parameter that enables cache busting after authentication, when text substitution may be required.

try:
    # Java Script Strings
    api_response = api_instance.resources_java_script_strings(lang, version, userid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_java_script_strings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language. | 
 **version** | **int**| The version - an unused parameter that enables cache busting. | 
 **userid** | **str**| The current user identifier - an optional, unused parameter that enables cache busting after authentication, when text substitution may be required. | 

### Return type

**dict(str, str)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_ui_languages**
> list[UiLanguage] resources_ui_languages()

Ui Languages

Gets the languages supported by the UI and API.  <br/>_This method does not require you to supply an authentication token._

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesApi()

try:
    # Ui Languages
    api_response = api_instance.resources_ui_languages()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_ui_languages: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UiLanguage]**](UiLanguage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_version**
> int resources_version()

Version

Gets the current version of the application. This value can be used in query-strings to enable version specific cache busting.  <br/>_This method does not require you to supply an authentication token._

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesApi()

try:
    # Version
    api_response = api_instance.resources_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

