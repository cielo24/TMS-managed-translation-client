# swagger_client.FilesApi

All URIs are relative to *https://languagecloud.sdl.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**files_add_reference_file**](FilesApi.md#files_add_reference_file) | **POST** /tm4lc/api/v1/files/{projectId}/reference | Add Reference File
[**files_delete**](FilesApi.md#files_delete) | **DELETE** /tm4lc/api/v1/files/{fileId} | Delete
[**files_get_files**](FilesApi.md#files_get_files) | **GET** /tm4lc/api/v1/files/{fileId} | Get Files
[**files_get_studio_packages**](FilesApi.md#files_get_studio_packages) | **POST** /tm4lc/api/v1/files/studiopackage/download | Get Studio Packages
[**files_get_studio_packages_by_files**](FilesApi.md#files_get_studio_packages_by_files) | **POST** /tm4lc/api/v1/files/studiopackage/downloadbyfile | Get Studio Packages By Files
[**files_get_translated_file**](FilesApi.md#files_get_translated_file) | **GET** /tm4lc/api/v1/files/{projectId}/{fileId} | Get Translated File
[**files_set_studio_package**](FilesApi.md#files_set_studio_package) | **POST** /tm4lc/api/v1/files/studiopackage/upload | Set Studio Package
[**files_upload**](FilesApi.md#files_upload) | **POST** /tm4lc/api/v1/files/{fileId} | Upload


# **files_add_reference_file**
> list[LcFile] files_add_reference_file(project_id, file)

Add Reference File

Add a reference file to an existing project.  <br/> If the content you provide is encoded using Base64 encoding, please supply an HTTP header named \" X-Base64-Content\" to indicate the provided content should be Base64 Decoded prior to processing. The value of the HTTP header should any of \"true\", \"yes\" or \"1\" to indicate that the content is Base64 encoded. Any other value, or the absence of the header, will result in the content being handled without first being Base64 decoded. 

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | The project identifier.
file = '/path/to/file.txt' # file | 

try:
    # Add Reference File
    api_response = api_instance.files_add_reference_file(project_id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->files_add_reference_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The project identifier. | 
 **file** | **file**|  | 

### Return type

[**list[LcFile]**](LcFile.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_delete**
> files_delete(file_id)

Delete

Deletes a previously uploaded file from the repository. If a file is included in a translation project, it will be automatically deleted from the             repository once the project has been created, and will no longer appear in the list of files returned by [Get Files](#operation/Files_GetFiles).

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
file_id = 'file_id_example' # str | The file identifier supplied in the FileId property of the response to an upload.

try:
    # Delete
    api_instance.files_delete(file_id)
except ApiException as e:
    print("Exception when calling FilesApi->files_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The file identifier supplied in the FileId property of the response to an upload. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_get_files**
> list[LcFile] files_get_files(file_id)

Get Files

Gets information about previously uploaded files that have not yet been included in a translation project.

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
file_id = 'file_id_example' # str | The project options identifier - if specified, the returned list of files will be             evaluated for suitability against the specified project creation options.

try:
    # Get Files
    api_response = api_instance.files_get_files(file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->files_get_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The project options identifier - if specified, the returned list of files will be             evaluated for suitability against the specified project creation options. | 

### Return type

[**list[LcFile]**](LcFile.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_get_studio_packages**
> file files_get_studio_packages(project_ids)

Get Studio Packages

Retrieves the studio packages for specified projects  <br/> This API method allows you to retrieve studio package file 

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
project_ids = [swagger_client.list[str]()] # list[str] | The project identifier as supplied by PortalProjectStatus.Id.

try:
    # Get Studio Packages
    api_response = api_instance.files_get_studio_packages(project_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->files_get_studio_packages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_ids** | **list[str]**| The project identifier as supplied by PortalProjectStatus.Id. | 

### Return type

[**file**](file.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_get_studio_packages_by_files**
> file files_get_studio_packages_by_files(file_ids)

Get Studio Packages By Files

Retrieves the studio packages for specified files  <br/> This API method allows you to retrieve studio package file 

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
file_ids = [swagger_client.list[str]()] # list[str] | A list of file identifiers

try:
    # Get Studio Packages By Files
    api_response = api_instance.files_get_studio_packages_by_files(file_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->files_get_studio_packages_by_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_ids** | **list[str]**| A list of file identifiers | 

### Return type

[**file**](file.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_get_translated_file**
> file files_get_translated_file(project_id, file_id)

Get Translated File

Retrieves the contents of a single translated file, contained within the specified project. If the requested file is not yet             at the Download status, the content of the file may not yet be fully translated. If the file is at the Download status,             and you have successfully retrieved it, you will want to mark the file as Complete using the             [Cancel Or Complete File](#operation/Projects_CancelOrCompleteFile) method.  <br/> This API method allows you to retrieve a single translated file, by specifying the projectId and fileId. The fileId parameter can be obtained from the <code>PortalProjectFileDetails.Id</code> member. 

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | The project identifier as supplied by PortalProjectStatus.Id.
file_id = 'file_id_example' # str | The target-language file identifier, for example project.LanguagePairDetails[0].Files[0].Id.

try:
    # Get Translated File
    api_response = api_instance.files_get_translated_file(project_id, file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->files_get_translated_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The project identifier as supplied by PortalProjectStatus.Id. | 
 **file_id** | **str**| The target-language file identifier, for example project.LanguagePairDetails[0].Files[0].Id. | 

### Return type

[**file**](file.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_set_studio_package**
> files_set_studio_package(file)

Set Studio Package

Allows studio package file uploads. Uploads must be submitted using              [multipart/form-data](https://www.w3.org/TR/html401/interact/forms.html#h-17.13.4.2) and can contain more             than one file, although this is rarely useful and increases the impact of any failure.              In the case of archives (zip, rar, 7z, tar files) we will examine the contents of the archive and will upload             each file separately.  <br/> If the content you provide is encoded using Base64 encoding, please supply an HTTP header named \" X-Base64-Content\" to indicate the provided content should be Base64 Decoded prior to processing. The value of the HTTP header should any of \"true\", \"yes\" or \"1\" to indicate that the content is Base64 encoded. Any other value, or the absence of the header, will result in the content being handled without first being Base64 decoded. 

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
file = '/path/to/file.txt' # file | 

try:
    # Set Studio Package
    api_instance.files_set_studio_package(file)
except ApiException as e:
    print("Exception when calling FilesApi->files_set_studio_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_upload**
> list[LcFile] files_upload(file_id, file)

Upload

Allows uploads of files for translation or for inclusion in a translation project as reference material. Uploads must be             submitted using [multipart/form-data](https://www.w3.org/TR/html401/interact/forms.html#h-17.13.4.2) and can contain more             than one file, although this is rarely useful and increases the impact of any failure. The Uri requires you to specify             the ProjectOptionId that should be used to evaluate the uploaded file(s).             This is used to enable us to consider whether each file you upload is a possible candidate for translation or must be handled as             reference material. In the case of archives (zip, rar, 7z, tar files) we will examine the contents of the archive and indicate             whether the archive as a whole can be translated or not, or whether it contains a mixture of translatable and non-translatable files.  <br/> If the content you provide is encoded using Base64 encoding, please supply an HTTP header named \" X-Base64-Content\" to indicate that the provided content should be Base64 Decoded prior to processing. The value of the HTTP header should any of \"true\", \"yes\" or \"1\" to indicate that the content is Base64 encoded. Any other value, or the absence of the header, will result in the content being handled without first being Base64 decoded. 

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
file_id = 'file_id_example' # str | The project options identifier against which the uploaded file will be evaluated.
file = '/path/to/file.txt' # file | 

try:
    # Upload
    api_response = api_instance.files_upload(file_id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->files_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The project options identifier against which the uploaded file will be evaluated. | 
 **file** | **file**|  | 

### Return type

[**list[LcFile]**](LcFile.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

