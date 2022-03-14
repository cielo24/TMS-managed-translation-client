# swagger_client.StatisticsApi

All URIs are relative to *https://languagecloud.sdl.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statistics_get_statistics**](StatisticsApi.md#statistics_get_statistics) | **GET** /tm4lc/api/v1/statistics/{duration} | Get Statistics


# **statistics_get_statistics**
> list[PortalDailyStatistic] statistics_get_statistics(duration)

Get Statistics

Provides translation statistics for approved project created within the specified period.

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
api_instance = swagger_client.StatisticsApi(swagger_client.ApiClient(configuration))
duration = 'duration_example' # str | The duration. 0 = LastThreeMonths, 1 = ThisMonth, 2 = ThisYear, 3 = LastTwelveMonths

try:
    # Get Statistics
    api_response = api_instance.statistics_get_statistics(duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->statistics_get_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **duration** | **str**| The duration. 0 &#x3D; LastThreeMonths, 1 &#x3D; ThisMonth, 2 &#x3D; ThisYear, 3 &#x3D; LastTwelveMonths | 

### Return type

[**list[PortalDailyStatistic]**](PortalDailyStatistic.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

