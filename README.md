# Managed Translation API

## Getting Started with the Managed Translation API  

A good way of getting started with the Managed Translation API is to follow a project throughout its entire life cycle, 
from its creation to its completion.    

### Step 1: Authenticate with the API  

Obtaining an access token is the main prerequisite for all the requests that you can make to the Managed Translation API. 
The most common way of obtaining such a token is through the Login endpoint. 
The Managed Translation API handles authentication requests using the OAuth 2.0 Authorization Framework.  

1. Log in to Managed Translation and create an application for your integration. This will give you a client ID and a secret.  
2. Use the client ID, the secret, and your Managed Translation credentials to make a `POST` request to the Login endpoint [`/auth/token`](#operation/Authentication_Login).

Select the `application/x-www-form-urlencoded` content type when you make this request. The value of the `access_token` parameter in the response is your access token. Use this token in the header of all the requests you will make afterwards.    

### Step 2: Create a project  

Before you can create a project, you need to find out what options are available to you and to upload the files that need to be translated. Project creation options are particularly useful for selecting the language pair of your project and for knowing what types of files you can upload.

1. Make a `GET` request to the [`/projects/options`](#operation/Projects_GetProjectCreationOptions) endpoint.       
Decide on the most appropriate option for the project you want to create and make sure you remember its `Id`, which is included in the response. You will need to specify this `Id` both when uploading files and when creating the project.  
2. Upload the files that need to be translated by making a `POST` request to the [`/files/{projectOptionsId}`](#operation/Files_Upload) endpoint.      
When you upload the files, Managed Translation analyzes them and provides detailed information about them in the response. For example, whether or not they are translatable.  
3. Create the project by making a `POST` request to the [`/projects`](#operation/Projects_Create) endpoint.       
Make sure that you remember the value of the `ProjectId` parameter in the response. You will need it for tracking, approving, and completing your project.

### Step 3: Track your project

After you create a project, you can track it by making requests to endpoints such as the following:   

| Request type | Endpoint                                                               | Description                                                            |
|--------------|:-----------------------------------------------------------------------|------------------------------------------------------------------------|
| `GET`        | [`/projects/{projectId}`](#operation/Projects_GetProject)              | Get information about a specific project based on the `ProjectId`.     |
| `GET`        | [`/projects`](#operation/Projects_GetProjects)                         | Get information all the projects in the system.                        |
| `GET`        | [`/projects/status/{status}`](#operation/Projects_GetProjectsAtStatus) | Get information about all the projects having a certain status.        |
| `POST`       | [`/projects/fetch`](#operation/Projects_FetchProjects)                 | Get information about multiple projects of your choice in one request. |

### Step 4: Approve the project and download the translated files  

When the response to a tracking request shows that your project has the `ForApproval` status, approve the project by making a `POST` request to the [`/projects/{projectId}`](#operation/Projects_Approve) endpoint, and then keep tracking your project until one or all of its files has the `ForDownload` status. At that point, download the translated files by making a `GET` request to the [`/files/{projectId}/{fileId}`](#operation/Files_GetTranslatedFile) endpoint (to download one translated file at a time) or to the [`/projects/{projectId}/zip`](#operation/Projects_GetProjectZip) endpoint (to download all the translated files in the project as a .zip archive).    

### Step 5: Mark the files as completed  

After your files have been translated and you downloaded them, make a `DELETE` request to the [`/projects/{projectId}/{fileId}`](#operation/Projects_CancelOrComplete) endpoint. This request performs two different actions depending on the status of the files that you specify as parameters:  
* If the status is `ForApproval`, Managed Translation cancels the files. 
* If the status is `ForDownload`, Managed Translation completes the files.    If the files have any other status, the request is invalid.    

## Rate limits  

Applications can make a limited number of API requests per minute and per hour. These limits protect against abuse and against runaway applications. They are applied per application, per user, and per API endpoint or path. This means, for example, that you can make 200 project-specific status requests within a minute, but requesting a full list of projects is limited to 100 requests per minute.

| Time frame | Maximum requests |
|:-----------|:-----------------|
| Per minute | 100              |
| Per hour   | 1500             |

If your application regularly and legitimately exceeds this limits and receives 409 responses, please contact us.

---

# Swagger-Client

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on GitHub, you can install directly from GitHub

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiVersionApi(swagger_client.ApiClient(configuration))

try:
    # Get Api Build
    api_response = api_instance.api_version_get_api_build()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiVersionApi->api_version_get_api_build: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://languagecloud.sdl.com*

|         Class          |                                                                 Method                                                                 |                                 HTTP request                                |                 Description                  |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|----------------------------------------------|
| *ApiVersionApi*        | [**api_version_get_api_build**](docs/ApiVersionApi.md#api_version_get_api_build)                                                       | **GET** /tm4lc/api/apibuild                                                 | Get Api Build                                |
| *ApiVersionApi*        | [**api_version_get_api_version**](docs/ApiVersionApi.md#api_version_get_api_version)                                                   | **GET** /tm4lc/api/apiversion                                               | Get Api Version                              |
| *AuthenticationApi*    | [**authentication_login**](docs/AuthenticationApi.md#authentication_login)                                                             | **POST** /tm4lc/api/v1/auth/token                                           | Login                                        |
| *AuthenticationApi*    | [**authentication_refresh_token**](docs/AuthenticationApi.md#authentication_refresh_token)                                             | **POST** /tm4lc/api/v1/auth/token/refresh                                   | Refresh Token                                |
| *FilesApi*             | [**files_add_reference_file**](docs/FilesApi.md#files_add_reference_file)                                                              | **POST** /tm4lc/api/v1/files/{projectId}/reference                          | Add Reference File                           |
| *FilesApi*             | [**files_delete**](docs/FilesApi.md#files_delete)                                                                                      | **DELETE** /tm4lc/api/v1/files/{fileId}                                     | Delete                                       |
| *FilesApi*             | [**files_get_files**](docs/FilesApi.md#files_get_files)                                                                                | **GET** /tm4lc/api/v1/files/{fileId}                                        | Get Files                                    |
| *FilesApi*             | [**files_get_studio_packages**](docs/FilesApi.md#files_get_studio_packages)                                                            | **POST** /tm4lc/api/v1/files/studiopackage/download                         | Get Studio Packages                          |
| *FilesApi*             | [**files_get_studio_packages_by_files**](docs/FilesApi.md#files_get_studio_packages_by_files)                                          | **POST** /tm4lc/api/v1/files/studiopackage/downloadbyfile                   | Get Studio Packages By Files                 |
| *FilesApi*             | [**files_get_translated_file**](docs/FilesApi.md#files_get_translated_file)                                                            | **GET** /tm4lc/api/v1/files/{projectId}/{fileId}                            | Get Translated File                          |
| *FilesApi*             | [**files_set_studio_package**](docs/FilesApi.md#files_set_studio_package)                                                              | **POST** /tm4lc/api/v1/files/studiopackage/upload                           | Set Studio Package                           |
| *FilesApi*             | [**files_upload**](docs/FilesApi.md#files_upload)                                                                                      | **POST** /tm4lc/api/v1/files/{fileId}                                       | Upload                                       |
| *LanguagesApi*         | [**languages_get_all_languages**](docs/LanguagesApi.md#languages_get_all_languages)                                                    | **GET** /tm4lc/api/v1/languages/list                                        | Get All Languages                            |
| *ProjectsApi*          | [**projects_approve**](docs/ProjectsApi.md#projects_approve)                                                                           | **POST** /tm4lc/api/v1/projects/{projectId}                                 | Approve                                      |
| *ProjectsApi*          | [**projects_assign_vendor**](docs/ProjectsApi.md#projects_assign_vendor)                                                               | **POST** /tm4lc/api/v1/projects/{projectId}/vendor                          | Assign Vendor                                |
| *ProjectsApi*          | [**projects_cancel_or_complete**](docs/ProjectsApi.md#projects_cancel_or_complete)                                                     | **DELETE** /tm4lc/api/v1/projects/{projectId}                               | Cancel Or Complete                           |
| *ProjectsApi*          | [**projects_cancel_or_complete_file**](docs/ProjectsApi.md#projects_cancel_or_complete_file)                                           | **DELETE** /tm4lc/api/v1/projects/{projectId}/{fileId}                      | Cancel Or Complete File                      |
| *ProjectsApi*          | [**projects_clear_project_templates**](docs/ProjectsApi.md#projects_clear_project_templates)                                           | **DELETE** /tm4lc/api/v1/projects/templates/clear                           | Clear Project Templates                      |
| *ProjectsApi*          | [**projects_create**](docs/ProjectsApi.md#projects_create)                                                                             | **POST** /tm4lc/api/v1/projects                                             | Create                                       |
| *ProjectsApi*          | [**projects_delete_project_template**](docs/ProjectsApi.md#projects_delete_project_template)                                           | **DELETE** /tm4lc/api/v1/projects/templates/{id}                            | Delete Project Template                      |
| *ProjectsApi*          | [**projects_fetch_projects**](docs/ProjectsApi.md#projects_fetch_projects)                                                             | **POST** /tm4lc/api/v1/projects/fetch                                       | Fetch Projects                               |
| *ProjectsApi*          | [**projects_get_project**](docs/ProjectsApi.md#projects_get_project)                                                                   | **GET** /tm4lc/api/v1/projects/{projectId}                                  | Get Project                                  |
| *ProjectsApi*          | [**projects_get_project_creation_options**](docs/ProjectsApi.md#projects_get_project_creation_options)                                 | **GET** /tm4lc/api/v1/projects/options                                      | Get Project Creation Options                 |
| *ProjectsApi*          | [**projects_get_project_creation_options_by_scope_option**](docs/ProjectsApi.md#projects_get_project_creation_options_by_scope_option) | **GET** /tm4lc/api/v1/projects/options/{scopeOptionId}                      | Get Project Creation Options By Scope Option |
| *ProjectsApi*          | [**projects_get_project_group_quote**](docs/ProjectsApi.md#projects_get_project_group_quote)                                           | **GET** /tm4lc/api/v1/projects/projectgroup/{projectGroupId}/quote/{format} | Get Project Group Quote                      |
| *ProjectsApi*          | [**projects_get_project_quote**](docs/ProjectsApi.md#projects_get_project_quote)                                                       | **GET** /tm4lc/api/v1/projects/{projectId}/quote/{format}                   | Get Project Quote                            |
| *ProjectsApi*          | [**projects_get_project_scope_options**](docs/ProjectsApi.md#projects_get_project_scope_options)                                       | **GET** /tm4lc/api/v1/projects/scopeoptions                                 | Get Project Scope Options                    |
| *ProjectsApi*          | [**projects_get_project_templates**](docs/ProjectsApi.md#projects_get_project_templates)                                               | **GET** /tm4lc/api/v1/projects/templates                                    | Get Project Templates                        |
| *ProjectsApi*          | [**projects_get_project_zip**](docs/ProjectsApi.md#projects_get_project_zip)                                                           | **GET** /tm4lc/api/v1/projects/{projectId}/zip                              | Get Project Zip                              |
| *ProjectsApi*          | [**projects_get_project_zip_with_specific_files**](docs/ProjectsApi.md#projects_get_project_zip_with_specific_files)                   | **POST** /tm4lc/api/v1/projects/{projectId}/zip                             | Get Project Zip With Specific Files          |
| *ProjectsApi*          | [**projects_get_projects**](docs/ProjectsApi.md#projects_get_projects)                                                                 | **GET** /tm4lc/api/v1/projects                                              | Get Projects                                 |
| *ProjectsApi*          | [**projects_get_projects_at_status**](docs/ProjectsApi.md#projects_get_projects_at_status)                                             | **GET** /tm4lc/api/v1/projects/status/{status}                              | Get Projects At Status                       |
| *ProjectsApi*          | [**projects_get_projects_list**](docs/ProjectsApi.md#projects_get_projects_list)                                                       | **GET** /tm4lc/api/v1/projects/list                                         | Get Projects List                            |
| *ProjectsApi*          | [**projects_get_projects_list_at_status**](docs/ProjectsApi.md#projects_get_projects_list_at_status)                                   | **GET** /tm4lc/api/v1/projects/list/{status}                                | Get Projects List At Status                  |
| *ProjectsApi*          | [**projects_get_projects_with_search_term**](docs/ProjectsApi.md#projects_get_projects_with_search_term)                               | **GET** /tm4lc/api/v1/projects/search/{term}                                | Get Projects With Search Term                |
| *ProjectsApi*          | [**projects_get_search_meta_data_options**](docs/ProjectsApi.md#projects_get_search_meta_data_options)                                 | **GET** /tm4lc/api/v1/projects/options/metadata/{id}                        | Get Search Meta Data Options                 |
| *ProjectsApi*          | [**projects_reject_file**](docs/ProjectsApi.md#projects_reject_file)                                                                   | **POST** /tm4lc/api/v1/projects/{projectId}/reject/{fileId}                 | Reject File                                  |
| *ProjectsApi*          | [**projects_report_file_problem**](docs/ProjectsApi.md#projects_report_file_problem)                                                   | **POST** /tm4lc/api/v1/projects/{projectId}/{fileId}/error                  | Report File Problem                          |
| *ProjectsApi*          | [**projects_set_project_templates**](docs/ProjectsApi.md#projects_set_project_templates)                                               | **POST** /tm4lc/api/v1/projects/templates                                   | Set Project Templates                        |
| *ProjectsApi*          | [**projects_start_project**](docs/ProjectsApi.md#projects_start_project)                                                               | **POST** /tm4lc/api/v1/projects/{projectId}/start                           | Start Project                                |
| *ResourcesApi*         | [**resources_java_script_strings**](docs/ResourcesApi.md#resources_java_script_strings)                                                | **GET** /tm4lc/api/v1/resources/strings/{lang}/{version}/{userid}           | Java Script Strings                          |
| *ResourcesApi*         | [**resources_ui_languages**](docs/ResourcesApi.md#resources_ui_languages)                                                              | **GET** /tm4lc/api/v1/resources/uilanguages                                 | Ui Languages                                 |
| *ResourcesApi*         | [**resources_version**](docs/ResourcesApi.md#resources_version)                                                                        | **GET** /tm4lc/api/v1/resources/version                                     | Version                                      |
| *StatisticsApi*        | [**statistics_get_statistics**](docs/StatisticsApi.md#statistics_get_statistics)                                                       | **GET** /tm4lc/api/v1/statistics/{duration}                                 | Get Statistics                               |
| *TranslationMemoryApi* | [**translation_memory_get_tm_search_options**](docs/TranslationMemoryApi.md#translation_memory_get_tm_search_options)                  | **GET** /tm4lc/api/v1/tm/options/{requestInheritedConfigs}                  | Get Tm Search Options                        |
| *TranslationMemoryApi* | [**translation_memory_search_by_file**](docs/TranslationMemoryApi.md#translation_memory_search_by_file)                                | **POST** /tm4lc/api/v1/tm/search/file/{fileId}                              | Search By File                               |
| *TranslationMemoryApi* | [**translation_memory_search_by_project_option**](docs/TranslationMemoryApi.md#translation_memory_search_by_project_option)            | **POST** /tm4lc/api/v1/tm/search/{projectOptionsId}                         | Search By Project Option                     |
| *TranslationMemoryApi* | [**translation_memory_update_by_file**](docs/TranslationMemoryApi.md#translation_memory_update_by_file)                                | **POST** /tm4lc/api/v1/tm/update/file/{fileId}                              | Update By File                               |
| *TranslationMemoryApi* | [**translation_memory_update_by_project_option**](docs/TranslationMemoryApi.md#translation_memory_update_by_project_option)            | **POST** /tm4lc/api/v1/tm/update/{projectOptionsId}                         | Update By Project Option                     |
| *VendorsApi*           | [**vendors_get_vendor**](docs/VendorsApi.md#vendors_get_vendor)                                                                        | **GET** /tm4lc/api/v1/vendors/{vendorId}                                    | Get Vendor                                   |
| *VendorsApi*           | [**vendors_get_vendors**](docs/VendorsApi.md#vendors_get_vendors)                                                                      | **GET** /tm4lc/api/v1/vendors                                               | Get Vendors                                  |


## Documentation For Models

 - [ApiError](docs/ApiError.md)
 - [Cost](docs/Cost.md)
 - [DownloadFiles](docs/DownloadFiles.md)
 - [KeyValuePair](docs/KeyValuePair.md)
 - [Language](docs/Language.md)
 - [LcFile](docs/LcFile.md)
 - [PortalAssignee](docs/PortalAssignee.md)
 - [PortalCostAttribute](docs/PortalCostAttribute.md)
 - [PortalCostBand](docs/PortalCostBand.md)
 - [PortalCreateProjectResponse](docs/PortalCreateProjectResponse.md)
 - [PortalCurrency](docs/PortalCurrency.md)
 - [PortalDailyStatistic](docs/PortalDailyStatistic.md)
 - [PortalFileType](docs/PortalFileType.md)
 - [PortalGroup](docs/PortalGroup.md)
 - [PortalLanguage](docs/PortalLanguage.md)
 - [PortalLanguagePair](docs/PortalLanguagePair.md)
 - [PortalLanguagePairWordCount](docs/PortalLanguagePairWordCount.md)
 - [PortalMetadata](docs/PortalMetadata.md)
 - [PortalOwner](docs/PortalOwner.md)
 - [PortalProjectCostBandDetails](docs/PortalProjectCostBandDetails.md)
 - [PortalProjectCostDetail](docs/PortalProjectCostDetail.md)
 - [PortalProjectFileDetails](docs/PortalProjectFileDetails.md)
 - [PortalProjectLanguageStatus](docs/PortalProjectLanguageStatus.md)
 - [PortalProjectListEntry](docs/PortalProjectListEntry.md)
 - [PortalProjectOptions](docs/PortalProjectOptions.md)
 - [PortalProjectParams](docs/PortalProjectParams.md)
 - [PortalProjectStatus](docs/PortalProjectStatus.md)
 - [PortalProjectVendorCost](docs/PortalProjectVendorCost.md)
 - [PortalReviewer](docs/PortalReviewer.md)
 - [PortalScopeOption](docs/PortalScopeOption.md)
 - [PortalSignoffer](docs/PortalSignoffer.md)
 - [PortalStartProjectResponse](docs/PortalStartProjectResponse.md)
 - [PortalTmOptions](docs/PortalTmOptions.md)
 - [PortalTmSequence](docs/PortalTmSequence.md)
 - [PortalUserProjectTemplate](docs/PortalUserProjectTemplate.md)
 - [PortalVendor](docs/PortalVendor.md)
 - [PortalVendorAssignee](docs/PortalVendorAssignee.md)
 - [PortalVendorAssigneeLanguagePair](docs/PortalVendorAssigneeLanguagePair.md)
 - [PortalWorkflowAttribute](docs/PortalWorkflowAttribute.md)
 - [ProjectFile](docs/ProjectFile.md)
 - [ProjectMetadata](docs/ProjectMetadata.md)
 - [SearchMetadataOptions](docs/SearchMetadataOptions.md)
 - [TmAttribute](docs/TmAttribute.md)
 - [TmPenalty](docs/TmPenalty.md)
 - [TmSearchParams](docs/TmSearchParams.md)
 - [TmSearchResult](docs/TmSearchResult.md)
 - [TmSearchSegment](docs/TmSearchSegment.md)
 - [TmUpdateParams](docs/TmUpdateParams.md)
 - [TmUpdateSegment](docs/TmUpdateSegment.md)
 - [TokenErrorResponse](docs/TokenErrorResponse.md)
 - [TokenResponse](docs/TokenResponse.md)
 - [UiLanguage](docs/UiLanguage.md)
 - [VersionReport](docs/VersionReport.md)


## Documentation For Authorization


## oauth2

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: 
 - **public**: Access to public API methods


## Author

connectors@sdl.com
