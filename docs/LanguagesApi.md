# swagger_client.LanguagesApi

All URIs are relative to *https://languagecloud.sdl.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**languages_get_all_languages**](LanguagesApi.md#languages_get_all_languages) | **GET** /tm4lc/api/v1/languages/list | Get All Languages


# **languages_get_all_languages**
> list[Language] languages_get_all_languages()

Get All Languages

Gets all languages.  <br/>This list of languages is provided as a reference. It is common for developers to need to map language codes, and for that to happen one must know all the avaiable language codes from RWS.<br/>The presence of a language in this list does not mean that the language is available for use in translation projects. You must refer to the supported language pairs in the  for a list of available language pairs.

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
api_instance = swagger_client.LanguagesApi(swagger_client.ApiClient(configuration))

try:
    # Get All Languages
    api_response = api_instance.languages_get_all_languages()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->languages_get_all_languages: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Language]**](Language.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

