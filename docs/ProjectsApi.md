# swagger_client.ProjectsApi

All URIs are relative to *https://languagecloud.sdl.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_approve**](ProjectsApi.md#projects_approve) | **POST** /tm4lc/api/v1/projects/{projectId} | Approve
[**projects_assign_vendor**](ProjectsApi.md#projects_assign_vendor) | **POST** /tm4lc/api/v1/projects/{projectId}/vendor | Assign Vendor
[**projects_cancel_or_complete**](ProjectsApi.md#projects_cancel_or_complete) | **DELETE** /tm4lc/api/v1/projects/{projectId} | Cancel Or Complete
[**projects_cancel_or_complete_file**](ProjectsApi.md#projects_cancel_or_complete_file) | **DELETE** /tm4lc/api/v1/projects/{projectId}/{fileId} | Cancel Or Complete File
[**projects_clear_project_templates**](ProjectsApi.md#projects_clear_project_templates) | **DELETE** /tm4lc/api/v1/projects/templates/clear | Clear Project Templates
[**projects_create**](ProjectsApi.md#projects_create) | **POST** /tm4lc/api/v1/projects | Create
[**projects_delete_project_template**](ProjectsApi.md#projects_delete_project_template) | **DELETE** /tm4lc/api/v1/projects/templates/{id} | Delete Project Template
[**projects_fetch_projects**](ProjectsApi.md#projects_fetch_projects) | **POST** /tm4lc/api/v1/projects/fetch | Fetch Projects
[**projects_get_project**](ProjectsApi.md#projects_get_project) | **GET** /tm4lc/api/v1/projects/{projectId} | Get Project
[**projects_get_project_creation_options**](ProjectsApi.md#projects_get_project_creation_options) | **GET** /tm4lc/api/v1/projects/options | Get Project Creation Options
[**projects_get_project_creation_options_by_scope_option**](ProjectsApi.md#projects_get_project_creation_options_by_scope_option) | **GET** /tm4lc/api/v1/projects/options/{scopeOptionId} | Get Project Creation Options By Scope Option
[**projects_get_project_group_quote**](ProjectsApi.md#projects_get_project_group_quote) | **GET** /tm4lc/api/v1/projects/projectgroup/{projectGroupId}/quote/{format} | Get Project Group Quote
[**projects_get_project_quote**](ProjectsApi.md#projects_get_project_quote) | **GET** /tm4lc/api/v1/projects/{projectId}/quote/{format} | Get Project Quote
[**projects_get_project_scope_options**](ProjectsApi.md#projects_get_project_scope_options) | **GET** /tm4lc/api/v1/projects/scopeoptions | Get Project Scope Options
[**projects_get_project_templates**](ProjectsApi.md#projects_get_project_templates) | **GET** /tm4lc/api/v1/projects/templates | Get Project Templates
[**projects_get_project_zip**](ProjectsApi.md#projects_get_project_zip) | **GET** /tm4lc/api/v1/projects/{projectId}/zip | Get Project Zip
[**projects_get_project_zip_with_specific_files**](ProjectsApi.md#projects_get_project_zip_with_specific_files) | **POST** /tm4lc/api/v1/projects/{projectId}/zip | Get Project Zip With Specific Files
[**projects_get_projects**](ProjectsApi.md#projects_get_projects) | **GET** /tm4lc/api/v1/projects | Get Projects
[**projects_get_projects_at_status**](ProjectsApi.md#projects_get_projects_at_status) | **GET** /tm4lc/api/v1/projects/status/{status} | Get Projects At Status
[**projects_get_projects_list**](ProjectsApi.md#projects_get_projects_list) | **GET** /tm4lc/api/v1/projects/list | Get Projects List
[**projects_get_projects_list_at_status**](ProjectsApi.md#projects_get_projects_list_at_status) | **GET** /tm4lc/api/v1/projects/list/{status} | Get Projects List At Status
[**projects_get_projects_with_search_term**](ProjectsApi.md#projects_get_projects_with_search_term) | **GET** /tm4lc/api/v1/projects/search/{term} | Get Projects With Search Term
[**projects_get_search_meta_data_options**](ProjectsApi.md#projects_get_search_meta_data_options) | **GET** /tm4lc/api/v1/projects/options/metadata/{id} | Get Search Meta Data Options
[**projects_reject_file**](ProjectsApi.md#projects_reject_file) | **POST** /tm4lc/api/v1/projects/{projectId}/reject/{fileId} | Reject File
[**projects_report_file_problem**](ProjectsApi.md#projects_report_file_problem) | **POST** /tm4lc/api/v1/projects/{projectId}/{fileId}/error | Report File Problem
[**projects_set_project_templates**](ProjectsApi.md#projects_set_project_templates) | **POST** /tm4lc/api/v1/projects/templates | Set Project Templates
[**projects_start_project**](ProjectsApi.md#projects_start_project) | **POST** /tm4lc/api/v1/projects/{projectId}/start | Start Project

# **projects_approve**
> projects_approve(project_id)

Approve

Approves the specified project.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | The project identifier.

try:
    # Approve
    api_instance.projects_approve(project_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_approve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The project identifier. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_assign_vendor**
> projects_assign_vendor(body, project_id)

Assign Vendor

Assigns the specified vendor to the project and moves the project to the next status.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
body = 'body_example' # str | The vendor identifier. This value can be obtained from PortalVendor.Id.
project_id = 'project_id_example' # str | The project identifier of the project to which the specified vendor should be assigned. This value can be obtained from PortalProjectStatus.Id.

try:
    # Assign Vendor
    api_instance.projects_assign_vendor(body, project_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_assign_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| The vendor identifier. This value can be obtained from PortalVendor.Id. | 
 **project_id** | **str**| The project identifier of the project to which the specified vendor should be assigned. This value can be obtained from PortalProjectStatus.Id. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_cancel_or_complete**
> projects_cancel_or_complete(project_id)

Cancel Or Complete

Cancels or completes the specified project.  <br/>If the project is awaiting download, the project will transition through any final steps in the workflow, and will eventually be moved to complete.<br/>If the project is awaiting approval or vendor selection it will be cancelled.<br/>If the project is at any other status, the request will fail.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | The project identifier.

try:
    # Cancel Or Complete
    api_instance.projects_cancel_or_complete(project_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_cancel_or_complete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The project identifier. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_cancel_or_complete_file**
> projects_cancel_or_complete_file(project_id, file_id)

Cancel Or Complete File

Cancels or completes the specified file within the specified project.  <br/>If the file is awaiting download, the file will transition through any final steps in the workflow, and will eventually be moved to complete.<br/>If the file is awaiting approval or vendor selection it will be cancelled.<br/>If the file is at any other status, the request will fail.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | The project identifier.
file_id = 'file_id_example' # str | The file identifier.

try:
    # Cancel Or Complete File
    api_instance.projects_cancel_or_complete_file(project_id, file_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_cancel_or_complete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The project identifier. | 
 **file_id** | **str**| The file identifier. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_clear_project_templates**
> projects_clear_project_templates()

Clear Project Templates

Deletes all portal user project templates.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))

try:
    # Clear Project Templates
    api_instance.projects_clear_project_templates()
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_clear_project_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_create**
> PortalCreateProjectResponse projects_create(body)

Create

Creates the specified project.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PortalProjectParams() # PortalProjectParams | The project creation parameters.

try:
    # Create
    api_response = api_instance.projects_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PortalProjectParams**](PortalProjectParams.md)| The project creation parameters. | 

### Return type

[**PortalCreateProjectResponse**](PortalCreateProjectResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_delete_project_template**
> projects_delete_project_template(id)

Delete Project Template

Delete portal user project templates.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The guid of the setting that will be deleted

try:
    # Delete Project Template
    api_instance.projects_delete_project_template(id)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_delete_project_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The guid of the setting that will be deleted | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_fetch_projects**
> list[PortalProjectStatus] projects_fetch_projects(body)

Fetch Projects

Gets a specified collection of projects.  <br/>Allows the retrieval of multiple, specific projects in one request.<br/>Any project that cannot be found will simply be ignored. No error will arise.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
body = ['body_example'] # list[str] | The projectIds of the projects to retrieve.

try:
    # Fetch Projects
    api_response = api_instance.projects_fetch_projects(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_fetch_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| The projectIds of the projects to retrieve. | 

### Return type

[**list[PortalProjectStatus]**](PortalProjectStatus.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_project**
> PortalProjectStatus projects_get_project(project_id, include_canceled=include_canceled)

Get Project

Gets the specified project.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | The project identifier.
include_canceled = true # bool | Should a canceled project be included in the result. (optional)

try:
    # Get Project
    api_response = api_instance.projects_get_project(project_id, include_canceled=include_canceled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The project identifier. | 
 **include_canceled** | **bool**| Should a canceled project be included in the result. | [optional] 

### Return type

[**PortalProjectStatus**](PortalProjectStatus.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_project_creation_options**
> list[PortalProjectOptions] projects_get_project_creation_options(max_options=max_options, order_by=order_by, top=top, skip=skip)

Get Project Creation Options

Gets the available project creation options  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
max_options = 56 # int | The maximum number of metadata options returned (optional)
order_by = 'order_by_example' # str |  (optional)
top = 56 # int |  (optional)
skip = 56 # int |  (optional)

try:
    # Get Project Creation Options
    api_response = api_instance.projects_get_project_creation_options(max_options=max_options, order_by=order_by, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get_project_creation_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_options** | **int**| The maximum number of metadata options returned | [optional] 
 **order_by** | **str**|  | [optional] 
 **top** | **int**|  | [optional] 
 **skip** | **int**|  | [optional] 

### Return type

[**list[PortalProjectOptions]**](PortalProjectOptions.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_project_creation_options_by_scope_option**
> list[PortalProjectOptions] projects_get_project_creation_options_by_scope_option(scope_option_id, max_options=max_options, order_by=order_by, top=top, skip=skip)

Get Project Creation Options By Scope Option

Gets the available project creation options.  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
scope_option_id = 'scope_option_id_example' # str | Scope option Id.
max_options = 56 # int | The maximum number of metadata options returned (optional)
order_by = 'order_by_example' # str |  (optional)
top = 56 # int |  (optional)
skip = 56 # int |  (optional)

try:
    # Get Project Creation Options By Scope Option
    api_response = api_instance.projects_get_project_creation_options_by_scope_option(scope_option_id, max_options=max_options, order_by=order_by, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get_project_creation_options_by_scope_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_option_id** | **str**| Scope option Id. | 
 **max_options** | **int**| The maximum number of metadata options returned | [optional] 
 **order_by** | **str**|  | [optional] 
 **top** | **int**|  | [optional] 
 **skip** | **int**|  | [optional] 

### Return type

[**list[PortalProjectOptions]**](PortalProjectOptions.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_project_group_quote**
> str projects_get_project_group_quote(project_group_id, format)

Get Project Group Quote

Generates a quote for the specified project group.  <br/> Quotes will be provided as either Excel or PDF. If the format parameter is omitted or provides a value other than <code>pdf</code>, and the Accept HTTP header does not contain \"application/pdf\" the quote will be provided in Excel 2003 (XLS) format. The HTTP Accept header takes precedence over the pdf parameter value. 

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project_group_id = 'project_group_id_example' # str | The project group identifier.
format = 'format_example' # str | The format - either xls or pdf.

try:
    # Get Project Group Quote
    api_response = api_instance.projects_get_project_group_quote(project_group_id, format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get_project_group_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_group_id** | **str**| The project group identifier. | 
 **format** | **str**| The format - either xls or pdf. | 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_project_quote**
> str projects_get_project_quote(project_id, format)

Get Project Quote

Generates a quote for the specified project.  <br/> Quotes will be provided as either Excel or PDF. If the format parameter is omitted or provides a value other than <code>pdf</code>, and the Accept HTTP header does not contain \"application/pdf\" the quote will be provided in Excel 2003 (XLS) format. The HTTP Accept header takes precedence over the pdf parameter value. 

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | The project identifier.
format = 'format_example' # str | The format - either xls or pdf.

try:
    # Get Project Quote
    api_response = api_instance.projects_get_project_quote(project_id, format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get_project_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The project identifier. | 
 **format** | **str**| The format - either xls or pdf. | 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_project_scope_options**
> list[PortalScopeOption] projects_get_project_scope_options(hierarchical=hierarchical, order_by=order_by, top=top, skip=skip)

Get Project Scope Options

Gets the available scope options  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
hierarchical = true # bool | If true it will return a hierarhical list (optional)
order_by = 'order_by_example' # str |  (optional)
top = 56 # int |  (optional)
skip = 56 # int |  (optional)

try:
    # Get Project Scope Options
    api_response = api_instance.projects_get_project_scope_options(hierarchical=hierarchical, order_by=order_by, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get_project_scope_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hierarchical** | **bool**| If true it will return a hierarhical list | [optional] 
 **order_by** | **str**|  | [optional] 
 **top** | **int**|  | [optional] 
 **skip** | **int**|  | [optional] 

### Return type

[**list[PortalScopeOption]**](PortalScopeOption.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_project_templates**
> projects_get_project_templates(id=id)

Get Project Templates

Get portal user project templates.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Optional specifying the guid of the setting to be returned (optional)

try:
    # Get Project Templates
    api_instance.projects_get_project_templates(id=id)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get_project_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Optional specifying the guid of the setting to be returned | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_project_zip**
> str projects_get_project_zip(project_id, types=types)

Get Project Zip

Gets the zip of translated files for the specified project.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | The project identifier.
types = 'types_example' # str | The types to download. 1 = TargetFiles, 2 = SourceFiles, 4 = ReferenceFiles (optional)

try:
    # Get Project Zip
    api_response = api_instance.projects_get_project_zip(project_id, types=types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get_project_zip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The project identifier. | 
 **types** | **str**| The types to download. 1 &#x3D; TargetFiles, 2 &#x3D; SourceFiles, 4 &#x3D; ReferenceFiles | [optional] 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_project_zip_with_specific_files**
> str projects_get_project_zip_with_specific_files(body, project_id, types=types)

Get Project Zip With Specific Files

Gets the zip of translated files for the specified project.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DownloadFiles() # DownloadFiles | An object with string[] TargetFiles property
project_id = 'project_id_example' # str | The project identifier.
types = 'types_example' # str | The types to download. 1 = TargetFiles, 2 = SourceFiles, 4 = ReferenceFiles (optional)

try:
    # Get Project Zip With Specific Files
    api_response = api_instance.projects_get_project_zip_with_specific_files(body, project_id, types=types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get_project_zip_with_specific_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DownloadFiles**](DownloadFiles.md)| An object with string[] TargetFiles property | 
 **project_id** | **str**| The project identifier. | 
 **types** | **str**| The types to download. 1 &#x3D; TargetFiles, 2 &#x3D; SourceFiles, 4 &#x3D; ReferenceFiles | [optional] 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_projects**
> list[PortalProjectStatus] projects_get_projects(order_by=order_by, top=top, skip=skip)

Get Projects

Gets information about every project available to the user.  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
order_by = 'order_by_example' # str |  (optional)
top = 56 # int |  (optional)
skip = 56 # int |  (optional)

try:
    # Get Projects
    api_response = api_instance.projects_get_projects(order_by=order_by, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_by** | **str**|  | [optional] 
 **top** | **int**|  | [optional] 
 **skip** | **int**|  | [optional] 

### Return type

[**list[PortalProjectStatus]**](PortalProjectStatus.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_projects_at_status**
> list[PortalProjectStatus] projects_get_projects_at_status(status, order_by=order_by, top=top, skip=skip)

Get Projects At Status

Gets all available projects at the specified status.  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
status = 'status_example' # str | The status. 0 = Preparing, 1 = ForApproval, 2 = InProgress, 3 = ForDownload, 4 = Completed, 5 = PartialDownload, 6 = InReview, 7 = Reviewed, 8 = InSignOff, 9 = SignedOff, 10 = ForVendorSelection, 11 = Cancelled, 12 = New
order_by = 'order_by_example' # str |  (optional)
top = 56 # int |  (optional)
skip = 56 # int |  (optional)

try:
    # Get Projects At Status
    api_response = api_instance.projects_get_projects_at_status(status, order_by=order_by, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get_projects_at_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| The status. 0 &#x3D; Preparing, 1 &#x3D; ForApproval, 2 &#x3D; InProgress, 3 &#x3D; ForDownload, 4 &#x3D; Completed, 5 &#x3D; PartialDownload, 6 &#x3D; InReview, 7 &#x3D; Reviewed, 8 &#x3D; InSignOff, 9 &#x3D; SignedOff, 10 &#x3D; ForVendorSelection, 11 &#x3D; Cancelled, 12 &#x3D; New | 
 **order_by** | **str**|  | [optional] 
 **top** | **int**|  | [optional] 
 **skip** | **int**|  | [optional] 

### Return type

[**list[PortalProjectStatus]**](PortalProjectStatus.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_projects_list**
> list[PortalProjectListEntry] projects_get_projects_list(order_by=order_by, top=top, skip=skip)

Get Projects List

Gets a simple list of all projects, providing general information about each project.  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
order_by = 'order_by_example' # str |  (optional)
top = 56 # int |  (optional)
skip = 56 # int |  (optional)

try:
    # Get Projects List
    api_response = api_instance.projects_get_projects_list(order_by=order_by, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get_projects_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_by** | **str**|  | [optional] 
 **top** | **int**|  | [optional] 
 **skip** | **int**|  | [optional] 

### Return type

[**list[PortalProjectListEntry]**](PortalProjectListEntry.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_projects_list_at_status**
> list[PortalProjectListEntry] projects_get_projects_list_at_status(status, order_by=order_by, top=top, skip=skip)

Get Projects List At Status

Gets a simple list of all projects at the specified status, providing only the most basic information about each project.  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
status = 'status_example' # str | The status. 0 = Preparing, 1 = ForApproval, 2 = InProgress, 3 = ForDownload, 4 = Completed, 5 = PartialDownload, 6 = InReview, 7 = Reviewed, 8 = InSignOff, 9 = SignedOff, 10 = ForVendorSelection, 11 = Cancelled, 12 = New
order_by = 'order_by_example' # str |  (optional)
top = 56 # int |  (optional)
skip = 56 # int |  (optional)

try:
    # Get Projects List At Status
    api_response = api_instance.projects_get_projects_list_at_status(status, order_by=order_by, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get_projects_list_at_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| The status. 0 &#x3D; Preparing, 1 &#x3D; ForApproval, 2 &#x3D; InProgress, 3 &#x3D; ForDownload, 4 &#x3D; Completed, 5 &#x3D; PartialDownload, 6 &#x3D; InReview, 7 &#x3D; Reviewed, 8 &#x3D; InSignOff, 9 &#x3D; SignedOff, 10 &#x3D; ForVendorSelection, 11 &#x3D; Cancelled, 12 &#x3D; New | 
 **order_by** | **str**|  | [optional] 
 **top** | **int**|  | [optional] 
 **skip** | **int**|  | [optional] 

### Return type

[**list[PortalProjectListEntry]**](PortalProjectListEntry.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_projects_with_search_term**
> list[PortalProjectStatus] projects_get_projects_with_search_term(term, order_by=order_by, top=top, skip=skip)

Get Projects With Search Term

Provides projects that contain the specified search term.  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
term = 'term_example' # str | The term.
order_by = 'order_by_example' # str |  (optional)
top = 56 # int |  (optional)
skip = 56 # int |  (optional)

try:
    # Get Projects With Search Term
    api_response = api_instance.projects_get_projects_with_search_term(term, order_by=order_by, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get_projects_with_search_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| The term. | 
 **order_by** | **str**|  | [optional] 
 **top** | **int**|  | [optional] 
 **skip** | **int**|  | [optional] 

### Return type

[**list[PortalProjectStatus]**](PortalProjectStatus.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_search_meta_data_options**
> list[PortalProjectOptions] projects_get_search_meta_data_options(id, search_expression, max_options=max_options)

Get Search Meta Data Options

returns a list of matching metadata options

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The metadata id
search_expression = 'search_expression_example' # str | A string representing the searched expressions
max_options = 56 # int | The maximum number of metadata options returned (optional)

try:
    # Get Search Meta Data Options
    api_response = api_instance.projects_get_search_meta_data_options(id, search_expression, max_options=max_options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get_search_meta_data_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The metadata id | 
 **search_expression** | **str**| A string representing the searched expressions | 
 **max_options** | **int**| The maximum number of metadata options returned | [optional] 

### Return type

[**list[PortalProjectOptions]**](PortalProjectOptions.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_reject_file**
> projects_reject_file(body, project_id, file_id)

Reject File

Allows rejecting a task with a rejection message .

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
body = 'body_example' # str | The rejection message.
project_id = 'project_id_example' # str | The project identifier.
file_id = 'file_id_example' # str | The file identifier.

try:
    # Reject File
    api_instance.projects_reject_file(body, project_id, file_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_reject_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| The rejection message. | 
 **project_id** | **str**| The project identifier. | 
 **file_id** | **str**| The file identifier. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_report_file_problem**
> projects_report_file_problem(body, project_id, file_id)

Report File Problem

Allows reporting a problem with a file that has been downloaded.  <br/>For example, during import into your repository an Xml file fails DTD/schema validation because of a tag ordering problem introduced during translation. Use this method to tell us about the problem - the file will be routed to an engineer for investigation and will be moved to the \"InProgress\" status.<br/>Once the problem is resolved, the file will return to \"ForDownload\" and you can retrieve the file again.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
body = 'body_example' # str | The error message.
project_id = 'project_id_example' # str | The project identifier.
file_id = 'file_id_example' # str | The file identifier.

try:
    # Report File Problem
    api_instance.projects_report_file_problem(body, project_id, file_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_report_file_problem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| The error message. | 
 **project_id** | **str**| The project identifier. | 
 **file_id** | **str**| The file identifier. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_set_project_templates**
> projects_set_project_templates(body)

Set Project Templates

Save portal user project templates.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PortalUserProjectTemplate() # PortalUserProjectTemplate | The project template settings

try:
    # Set Project Templates
    api_instance.projects_set_project_templates(body)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_set_project_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PortalUserProjectTemplate**](PortalUserProjectTemplate.md)| The project template settings | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_start_project**
> PortalStartProjectResponse projects_start_project(project_id)

Start Project

Starts the specified project.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | The project identifier.

try:
    # Start Project
    api_response = api_instance.projects_start_project(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_start_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The project identifier. | 

### Return type

[**PortalStartProjectResponse**](PortalStartProjectResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

