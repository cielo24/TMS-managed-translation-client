# swagger_client.ApiVersionApi

All URIs are relative to *https://languagecloud.sdl.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_version_get_api_build**](ApiVersionApi.md#api_version_get_api_build) | **GET** /tm4lc/api/apibuild | Get Api Build
[**api_version_get_api_version**](ApiVersionApi.md#api_version_get_api_version) | **GET** /tm4lc/api/apiversion | Get Api Version


# **api_version_get_api_build**
> dict(str, VersionReport) api_version_get_api_build()

Get Api Build

Gets the current build number for the application.  <br/>_This method does not require you to supply an authentication token._

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiVersionApi()

try:
    # Get Api Build
    api_response = api_instance.api_version_get_api_build()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiVersionApi->api_version_get_api_build: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, VersionReport)**](VersionReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_version_get_api_version**
> int api_version_get_api_version()

Get Api Version

Gets the highest supported API version for the application.  <br/>This api method allows you to interrogate the application to identify the highest supported API version. <br/>_This method does not require you to supply an authentication token._

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiVersionApi()

try:
    # Get Api Version
    api_response = api_instance.api_version_get_api_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiVersionApi->api_version_get_api_version: %s\n" % e)
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

