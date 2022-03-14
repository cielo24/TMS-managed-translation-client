# swagger_client.AuthenticationApi

All URIs are relative to *https://languagecloud.sdl.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication_login**](AuthenticationApi.md#authentication_login) | **POST** /tm4lc/api/v1/auth/token | Login
[**authentication_refresh_token**](AuthenticationApi.md#authentication_refresh_token) | **POST** /tm4lc/api/v1/auth/token/refresh | Refresh Token


# **authentication_login**
> TokenResponse authentication_login(grant_type, client_id, client_secret, username, password, implementation)

Login

Generates an access token for use with subsequent API calls using the OAuth2 Resource Owner Password Credentials Grant flow.  <br/> In order to generate an access token which can be supplied with each subsequent API call, a user must provide five values to this method, in the form of an <code>application/x-www-form-urlencoded</code> submission. The value supplied for <code>grant_type</code> must be <code>password</code>. <br/> Subsequent API requests must supply an HTTP <code>Authorization</code> header, with a value of <code>token_type access_token</code> where the values are taken from the token supplied in response to this API call. <br/>For more details see <code>https://tools.ietf.org/html/rfc6749#section-4.3</code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
grant_type = 'grant_type_example' # str | The grant_type - must be \"password\".
client_id = 'client_id_example' # str | The client_id assigned to your application.
client_secret = 'client_secret_example' # str | The client_secret assigned to your application.
username = 'username_example' # str | The username.
password = 'password_example' # str | The password.
implementation = 'implementation_example' # str | [Optional] The name of the backend implementation against which authentication should occur, if the supplied credentials are appropriate for use with more than one implementation. Unless told otherwise, you should probably omit this.

try:
    # Login
    api_response = api_instance.authentication_login(grant_type, client_id, client_secret, username, password, implementation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| The grant_type - must be \&quot;password\&quot;. | 
 **client_id** | **str**| The client_id assigned to your application. | 
 **client_secret** | **str**| The client_secret assigned to your application. | 
 **username** | **str**| The username. | 
 **password** | **str**| The password. | 
 **implementation** | **str**| [Optional] The name of the backend implementation against which authentication should occur, if the supplied credentials are appropriate for use with more than one implementation. Unless told otherwise, you should probably omit this. | 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_refresh_token**
> TokenResponse authentication_refresh_token(grant_type, client_id, client_secret, refresh_token)

Refresh Token

Regenerates an access token from the supplied refresh token.  <br/> In order to regenerate an access token which can be supplied with each subsequent API call, a user must provide four values to this method, in the form of an <code>application/x-www-form-urlencoded</code> submission. The value supplied for <code>grant_type</code> must be <code>refresh_token</code>. <br/> Subsequent API requests must supply an HTTP <code>Authorization</code> header, with a value of <code>token_type access_token</code> where the values are taken from the token supplied in response to this API call. <br/>For more details see <code>https://tools.ietf.org/html/rfc6749#section-6</code><br/>The same result can be obtained by submitting the request to the <code>/token</code> endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
grant_type = 'grant_type_example' # str | The grant_type - must be \"refresh_token\".
client_id = 'client_id_example' # str | The client_id assigned to your application.
client_secret = 'client_secret_example' # str | The client_secret assigned to your application.
refresh_token = 'refresh_token_example' # str | The refresh token supplied from a previous call to /token or /token/refresh.

try:
    # Refresh Token
    api_response = api_instance.authentication_refresh_token(grant_type, client_id, client_secret, refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| The grant_type - must be \&quot;refresh_token\&quot;. | 
 **client_id** | **str**| The client_id assigned to your application. | 
 **client_secret** | **str**| The client_secret assigned to your application. | 
 **refresh_token** | **str**| The refresh token supplied from a previous call to /token or /token/refresh. | 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

