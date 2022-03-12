# coding: utf-8

"""
    Managed Translation API

    # Getting Started with the Managed Translation API  A good way of getting started with the Managed Translation API is to follow a project throughout its entire life cycle, from its creation to its completion.    ## Step 1: Authenticate with the API  Obtaining an access token is the main prerequisite for all the requests that you can make to the Managed Translation API. The most common way of obtaining such a token is through the Login endpoint. The Managed Translation API handles authentication requests using the OAuth 2.0 Authorization Framework.  1. Log in to Managed Translation and create an application for your integration. This will give you a client ID and a secret.  2. Use the client ID, the secret, and your Managed Translation credentials to make a `POST` request to the Login endpoint [`/auth/token`](#operation/Authentication_Login).    Select the `application/x-www-form-urlencoded` content type when you make this request. The value of the `access_token` parameter in the response is your access token. Use this token in the header of all the requests you will make afterwards.    ## Step 2: Create a project  Before you can create a project, you need to find out what options are available to you and to upload the files that need to be translated. Project creation options are particularly useful for selecting the language pair of your project and for knowing what types of files you can upload.  1. Make a `GET` request to the [`/projects/options`](#operation/Projects_GetProjectCreationOptions) endpoint.       Decide on the most appropriate option for the project you want to create and make sure you remember its `Id`, which is included in the response. You will need to specify this `Id` both when uploading files and when creating the project.  2. Upload the files that need to be translated by making a `POST` request to the [`/files/{projectOptionsId}`](#operation/Files_Upload) endpoint.       When you upload the files, Managed Translation analyzes them and provides detailed information about them in the response. For example, whether or not they are translatable.  3. Create the project by making a `POST` request to the [`/projects`](#operation/Projects_Create) endpoint.       Make sure that you remember the value of the `ProjectId` parameter in the response. You will need it for tracking, approving, and completing your project.    ## Step 3: Track your project  After you create a project, you can track it by making requests to endpoints such as the following:    | Request type | Endpoint | Description |  |-------------|:-------------|-------------|  | `GET`| [`/projects/{projectId}`](#operation/Projects_GetProject) | Get information about a specific project based on the `ProjectId`. |  | `GET`| [`/projects`](#operation/Projects_GetProjects) | Get information all the projects in the system. |  | `GET`| [`/projects/status/{status}`](#operation/Projects_GetProjectsAtStatus) | Get information about all the projects having a certain status. |  | `POST`| [`/projects/fetch`](#operation/Projects_FetchProjects) | Get information about multiple projects of your choice in one request. |    ## Step 4: Approve the project and download the translated files  When the response to a tracking request shows that your project has the `ForApproval` status, approve the project by making a `POST` request to the [`/projects/{projectId}`](#operation/Projects_Approve) endpoint, and then keep tracking your project until one or all of its files has the `ForDownload` status. At that point, download the translated files by making a `GET` request to the [`/files/{projectId}/{fileId}`](#operation/Files_GetTranslatedFile) endpoint (to download one translated file at a time) or to the [`/projects/{projectId}/zip`](#operation/Projects_GetProjectZip) endpoint (to download all the translated files in the project as a .zip archive).    ## Step 5: Mark the files as completed  After your files have been translated and you downloaded them, make a `DELETE` request to the [`/projects/{projectId}/{fileId}`](#operation/Projects_CancelOrComplete) endpoint. This request performs two different actions depending on the status of the files that you specify as parameters:  * If the status is `ForApproval`, Managed Translation cancels the files.  * If the status is `ForDownload`, Managed Translation completes the files.    If the files have any other status, the request is invalid.    # Rate limits  Applications can make a limited number of API requests per minute and per hour. These limits protect against abuse and against runaway applications. They are applied per application, per user, and per API endpoint or path. This means, for example, that you can make 200 project-specific status requests within a minute, but requesting a full list of projects is limited to 100 requests per minute.    | Time frame | Maximum requests |  |:-------------|:-------------|  | Per minute| 100 |  | Per hour| 1500 |    If your application regularly and legitimately exceeds this limits and receives 409 responses, please contact us.  # noqa: E501

    OpenAPI spec version: v1
    Contact: connectors@sdl.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.projects_api import ProjectsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self):
        self.api = ProjectsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_projects_approve(self):
        """Test case for projects_approve

        Approve  # noqa: E501
        """
        pass

    def test_projects_assign_vendor(self):
        """Test case for projects_assign_vendor

        Assign Vendor  # noqa: E501
        """
        pass

    def test_projects_cancel_or_complete(self):
        """Test case for projects_cancel_or_complete

        Cancel Or Complete  # noqa: E501
        """
        pass

    def test_projects_cancel_or_complete_file(self):
        """Test case for projects_cancel_or_complete_file

        Cancel Or Complete File  # noqa: E501
        """
        pass

    def test_projects_clear_project_templates(self):
        """Test case for projects_clear_project_templates

        Clear Project Templates  # noqa: E501
        """
        pass

    def test_projects_create(self):
        """Test case for projects_create

        Create  # noqa: E501
        """
        pass

    def test_projects_delete_project_template(self):
        """Test case for projects_delete_project_template

        Delete Project Template  # noqa: E501
        """
        pass

    def test_projects_fetch_projects(self):
        """Test case for projects_fetch_projects

        Fetch Projects  # noqa: E501
        """
        pass

    def test_projects_get_project(self):
        """Test case for projects_get_project

        Get Project  # noqa: E501
        """
        pass

    def test_projects_get_project_creation_options(self):
        """Test case for projects_get_project_creation_options

        Get Project Creation Options  # noqa: E501
        """
        pass

    def test_projects_get_project_creation_options_by_scope_option(self):
        """Test case for projects_get_project_creation_options_by_scope_option

        Get Project Creation Options By Scope Option  # noqa: E501
        """
        pass

    def test_projects_get_project_group_quote(self):
        """Test case for projects_get_project_group_quote

        Get Project Group Quote  # noqa: E501
        """
        pass

    def test_projects_get_project_quote(self):
        """Test case for projects_get_project_quote

        Get Project Quote  # noqa: E501
        """
        pass

    def test_projects_get_project_scope_options(self):
        """Test case for projects_get_project_scope_options

        Get Project Scope Options  # noqa: E501
        """
        pass

    def test_projects_get_project_templates(self):
        """Test case for projects_get_project_templates

        Get Project Templates  # noqa: E501
        """
        pass

    def test_projects_get_project_zip(self):
        """Test case for projects_get_project_zip

        Get Project Zip  # noqa: E501
        """
        pass

    def test_projects_get_project_zip_with_specific_files(self):
        """Test case for projects_get_project_zip_with_specific_files

        Get Project Zip With Specific Files  # noqa: E501
        """
        pass

    def test_projects_get_projects(self):
        """Test case for projects_get_projects

        Get Projects  # noqa: E501
        """
        pass

    def test_projects_get_projects_at_status(self):
        """Test case for projects_get_projects_at_status

        Get Projects At Status  # noqa: E501
        """
        pass

    def test_projects_get_projects_list(self):
        """Test case for projects_get_projects_list

        Get Projects List  # noqa: E501
        """
        pass

    def test_projects_get_projects_list_at_status(self):
        """Test case for projects_get_projects_list_at_status

        Get Projects List At Status  # noqa: E501
        """
        pass

    def test_projects_get_projects_with_search_term(self):
        """Test case for projects_get_projects_with_search_term

        Get Projects With Search Term  # noqa: E501
        """
        pass

    def test_projects_get_search_meta_data_options(self):
        """Test case for projects_get_search_meta_data_options

        Get Search Meta Data Options  # noqa: E501
        """
        pass

    def test_projects_reject_file(self):
        """Test case for projects_reject_file

        Reject File  # noqa: E501
        """
        pass

    def test_projects_report_file_problem(self):
        """Test case for projects_report_file_problem

        Report File Problem  # noqa: E501
        """
        pass

    def test_projects_set_project_templates(self):
        """Test case for projects_set_project_templates

        Set Project Templates  # noqa: E501
        """
        pass

    def test_projects_start_project(self):
        """Test case for projects_start_project

        Start Project  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
