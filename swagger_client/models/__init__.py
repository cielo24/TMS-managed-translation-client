# coding: utf-8

# flake8: noqa
"""
    Managed Translation API

    # Getting Started with the Managed Translation API  A good way of getting started with the Managed Translation API is to follow a project throughout its entire life cycle, from its creation to its completion.    ## Step 1: Authenticate with the API  Obtaining an access token is the main prerequisite for all the requests that you can make to the Managed Translation API. The most common way of obtaining such a token is through the Login endpoint. The Managed Translation API handles authentication requests using the OAuth 2.0 Authorization Framework.  1. Log in to Managed Translation and create an application for your integration. This will give you a client ID and a secret.  2. Use the client ID, the secret, and your Managed Translation credentials to make a `POST` request to the Login endpoint [`/auth/token`](#operation/Authentication_Login).    Select the `application/x-www-form-urlencoded` content type when you make this request. The value of the `access_token` parameter in the response is your access token. Use this token in the header of all the requests you will make afterwards.    ## Step 2: Create a project  Before you can create a project, you need to find out what options are available to you and to upload the files that need to be translated. Project creation options are particularly useful for selecting the language pair of your project and for knowing what types of files you can upload.  1. Make a `GET` request to the [`/projects/options`](#operation/Projects_GetProjectCreationOptions) endpoint.       Decide on the most appropriate option for the project you want to create and make sure you remember its `Id`, which is included in the response. You will need to specify this `Id` both when uploading files and when creating the project.  2. Upload the files that need to be translated by making a `POST` request to the [`/files/{projectOptionsId}`](#operation/Files_Upload) endpoint.       When you upload the files, Managed Translation analyzes them and provides detailed information about them in the response. For example, whether or not they are translatable.  3. Create the project by making a `POST` request to the [`/projects`](#operation/Projects_Create) endpoint.       Make sure that you remember the value of the `ProjectId` parameter in the response. You will need it for tracking, approving, and completing your project.    ## Step 3: Track your project  After you create a project, you can track it by making requests to endpoints such as the following:    | Request type | Endpoint | Description |  |-------------|:-------------|-------------|  | `GET`| [`/projects/{projectId}`](#operation/Projects_GetProject) | Get information about a specific project based on the `ProjectId`. |  | `GET`| [`/projects`](#operation/Projects_GetProjects) | Get information all the projects in the system. |  | `GET`| [`/projects/status/{status}`](#operation/Projects_GetProjectsAtStatus) | Get information about all the projects having a certain status. |  | `POST`| [`/projects/fetch`](#operation/Projects_FetchProjects) | Get information about multiple projects of your choice in one request. |    ## Step 4: Approve the project and download the translated files  When the response to a tracking request shows that your project has the `ForApproval` status, approve the project by making a `POST` request to the [`/projects/{projectId}`](#operation/Projects_Approve) endpoint, and then keep tracking your project until one or all of its files has the `ForDownload` status. At that point, download the translated files by making a `GET` request to the [`/files/{projectId}/{fileId}`](#operation/Files_GetTranslatedFile) endpoint (to download one translated file at a time) or to the [`/projects/{projectId}/zip`](#operation/Projects_GetProjectZip) endpoint (to download all the translated files in the project as a .zip archive).    ## Step 5: Mark the files as completed  After your files have been translated and you downloaded them, make a `DELETE` request to the [`/projects/{projectId}/{fileId}`](#operation/Projects_CancelOrComplete) endpoint. This request performs two different actions depending on the status of the files that you specify as parameters:  * If the status is `ForApproval`, Managed Translation cancels the files.  * If the status is `ForDownload`, Managed Translation completes the files.    If the files have any other status, the request is invalid.    # Rate limits  Applications can make a limited number of API requests per minute and per hour. These limits protect against abuse and against runaway applications. They are applied per application, per user, and per API endpoint or path. This means, for example, that you can make 200 project-specific status requests within a minute, but requesting a full list of projects is limited to 100 requests per minute.    | Time frame | Maximum requests |  |:-------------|:-------------|  | Per minute| 100 |  | Per hour| 1500 |    If your application regularly and legitimately exceeds this limits and receives 409 responses, please contact us.  # noqa: E501

    OpenAPI spec version: v1
    Contact: connectors@sdl.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from swagger_client.models.api_error import ApiError
from swagger_client.models.auth_token_body import AuthTokenBody
from swagger_client.models.cost import Cost
from swagger_client.models.download_files import DownloadFiles
from swagger_client.models.files_project_options_id_body import FilesProjectOptionsIdBody
from swagger_client.models.key_value_pair_string_string import KeyValuePairStringString
from swagger_client.models.language import Language
from swagger_client.models.lc_file import LcFile
from swagger_client.models.portal_assignee import PortalAssignee
from swagger_client.models.portal_cost_attribute import PortalCostAttribute
from swagger_client.models.portal_cost_band import PortalCostBand
from swagger_client.models.portal_create_project_response import PortalCreateProjectResponse
from swagger_client.models.portal_currency import PortalCurrency
from swagger_client.models.portal_daily_statistic import PortalDailyStatistic
from swagger_client.models.portal_file_type import PortalFileType
from swagger_client.models.portal_group import PortalGroup
from swagger_client.models.portal_language import PortalLanguage
from swagger_client.models.portal_language_pair import PortalLanguagePair
from swagger_client.models.portal_language_pair_word_count import PortalLanguagePairWordCount
from swagger_client.models.portal_metadata import PortalMetadata
from swagger_client.models.portal_owner import PortalOwner
from swagger_client.models.portal_project_cost_band_details import PortalProjectCostBandDetails
from swagger_client.models.portal_project_cost_detail import PortalProjectCostDetail
from swagger_client.models.portal_project_file_details import PortalProjectFileDetails
from swagger_client.models.portal_project_language_status import PortalProjectLanguageStatus
from swagger_client.models.portal_project_list_entry import PortalProjectListEntry
from swagger_client.models.portal_project_options import PortalProjectOptions
from swagger_client.models.portal_project_params import PortalProjectParams
from swagger_client.models.portal_project_status import PortalProjectStatus
from swagger_client.models.portal_project_vendor_cost import PortalProjectVendorCost
from swagger_client.models.portal_reviewer import PortalReviewer
from swagger_client.models.portal_scope_option import PortalScopeOption
from swagger_client.models.portal_signoffer import PortalSignoffer
from swagger_client.models.portal_start_project_response import PortalStartProjectResponse
from swagger_client.models.portal_tm_options import PortalTmOptions
from swagger_client.models.portal_tm_sequence import PortalTmSequence
from swagger_client.models.portal_user_project_template import PortalUserProjectTemplate
from swagger_client.models.portal_vendor import PortalVendor
from swagger_client.models.portal_vendor_assignee import PortalVendorAssignee
from swagger_client.models.portal_vendor_assignee_language_pair import PortalVendorAssigneeLanguagePair
from swagger_client.models.portal_workflow_attribute import PortalWorkflowAttribute
from swagger_client.models.project_file import ProjectFile
from swagger_client.models.project_id_reference_body import ProjectIdReferenceBody
from swagger_client.models.project_metadata import ProjectMetadata
from swagger_client.models.search_metadata_options import SearchMetadataOptions
from swagger_client.models.studiopackage_upload_body import StudiopackageUploadBody
from swagger_client.models.tm_attribute import TmAttribute
from swagger_client.models.tm_penalty import TmPenalty
from swagger_client.models.tm_search_params import TmSearchParams
from swagger_client.models.tm_search_result import TmSearchResult
from swagger_client.models.tm_search_segment import TmSearchSegment
from swagger_client.models.tm_update_params import TmUpdateParams
from swagger_client.models.tm_update_segment import TmUpdateSegment
from swagger_client.models.token_error_response import TokenErrorResponse
from swagger_client.models.token_refresh_body import TokenRefreshBody
from swagger_client.models.token_response import TokenResponse
from swagger_client.models.ui_language import UiLanguage
from swagger_client.models.version_report import VersionReport
