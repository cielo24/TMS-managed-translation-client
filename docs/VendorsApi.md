# swagger_client.VendorsApi

All URIs are relative to *https://languagecloud.sdl.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vendors_get_vendor**](VendorsApi.md#vendors_get_vendor) | **GET** /tm4lc/api/v1/vendors/{vendorId} | Get Vendor
[**vendors_get_vendors**](VendorsApi.md#vendors_get_vendors) | **GET** /tm4lc/api/v1/vendors | Get Vendors


# **vendors_get_vendor**
> PortalVendor vendors_get_vendor(vendor_id)

Get Vendor

Gets the vendor.

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
api_instance = swagger_client.VendorsApi(swagger_client.ApiClient(configuration))
vendor_id = 'vendor_id_example' # str | The vendor identifier.

try:
    # Get Vendor
    api_response = api_instance.vendors_get_vendor(vendor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->vendors_get_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **str**| The vendor identifier. | 

### Return type

[**PortalVendor**](PortalVendor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendors_get_vendors**
> list[PortalVendor] vendors_get_vendors()

Get Vendors

Gets the vendors for the current user.

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
api_instance = swagger_client.VendorsApi(swagger_client.ApiClient(configuration))

try:
    # Get Vendors
    api_response = api_instance.vendors_get_vendors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->vendors_get_vendors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PortalVendor]**](PortalVendor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

