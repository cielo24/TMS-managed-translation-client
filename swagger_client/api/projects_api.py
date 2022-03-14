# coding: utf-8

"""
    Managed Translation API

    # Getting Started with the Managed Translation API  A good way of getting started with the Managed Translation API is to follow a project throughout its entire life cycle, from its creation to its completion.    ## Step 1: Authenticate with the API  Obtaining an access token is the main prerequisite for all the requests that you can make to the Managed Translation API. The most common way of obtaining such a token is through the Login endpoint. The Managed Translation API handles authentication requests using the OAuth 2.0 Authorization Framework.  1. Log in to Managed Translation and create an application for your integration. This will give you a client ID and a secret.  2. Use the client ID, the secret, and your Managed Translation credentials to make a `POST` request to the Login endpoint [`/auth/token`](#operation/Authentication_Login).    Select the `application/x-www-form-urlencoded` content type when you make this request. The value of the `access_token` parameter in the response is your access token. Use this token in the header of all the requests you will make afterwards.    ## Step 2: Create a project  Before you can create a project, you need to find out what options are available to you and to upload the files that need to be translated. Project creation options are particularly useful for selecting the language pair of your project and for knowing what types of files you can upload.  1. Make a `GET` request to the [`/projects/options`](#operation/Projects_GetProjectCreationOptions) endpoint.       Decide on the most appropriate option for the project you want to create and make sure you remember its `Id`, which is included in the response. You will need to specify this `Id` both when uploading files and when creating the project.  2. Upload the files that need to be translated by making a `POST` request to the [`/files/{projectOptionsId}`](#operation/Files_Upload) endpoint.       When you upload the files, Managed Translation analyzes them and provides detailed information about them in the response. For example, whether or not they are translatable.  3. Create the project by making a `POST` request to the [`/projects`](#operation/Projects_Create) endpoint.       Make sure that you remember the value of the `ProjectId` parameter in the response. You will need it for tracking, approving, and completing your project.    ## Step 3: Track your project  After you create a project, you can track it by making requests to endpoints such as the following:    | Request type | Endpoint | Description |  |-------------|:-------------|-------------|  | `GET`| [`/projects/{projectId}`](#operation/Projects_GetProject) | Get information about a specific project based on the `ProjectId`. |  | `GET`| [`/projects`](#operation/Projects_GetProjects) | Get information all the projects in the system. |  | `GET`| [`/projects/status/{status}`](#operation/Projects_GetProjectsAtStatus) | Get information about all the projects having a certain status. |  | `POST`| [`/projects/fetch`](#operation/Projects_FetchProjects) | Get information about multiple projects of your choice in one request. |    ## Step 4: Approve the project and download the translated files  When the response to a tracking request shows that your project has the `ForApproval` status, approve the project by making a `POST` request to the [`/projects/{projectId}`](#operation/Projects_Approve) endpoint, and then keep tracking your project until one or all of its files has the `ForDownload` status. At that point, download the translated files by making a `GET` request to the [`/files/{projectId}/{fileId}`](#operation/Files_GetTranslatedFile) endpoint (to download one translated file at a time) or to the [`/projects/{projectId}/zip`](#operation/Projects_GetProjectZip) endpoint (to download all the translated files in the project as a .zip archive).    ## Step 5: Mark the files as completed  After your files have been translated and you downloaded them, make a `DELETE` request to the [`/projects/{projectId}/{fileId}`](#operation/Projects_CancelOrComplete) endpoint. This request performs two different actions depending on the status of the files that you specify as parameters:  * If the status is `ForApproval`, Managed Translation cancels the files.  * If the status is `ForDownload`, Managed Translation completes the files.    If the files have any other status, the request is invalid.    # Rate limits  Applications can make a limited number of API requests per minute and per hour. These limits protect against abuse and against runaway applications. They are applied per application, per user, and per API endpoint or path. This means, for example, that you can make 200 project-specific status requests within a minute, but requesting a full list of projects is limited to 100 requests per minute.    | Time frame | Maximum requests |  |:-------------|:-------------|  | Per minute| 100 |  | Per hour| 1500 |    If your application regularly and legitimately exceeds this limits and receives 409 responses, please contact us.  # noqa: E501

    OpenAPI spec version: v1
    Contact: connectors@sdl.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ProjectsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def projects_approve(self, project_id, **kwargs):  # noqa: E501
        """Approve  # noqa: E501

        Approves the specified project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_approve(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_approve_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_approve_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def projects_approve_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """Approve  # noqa: E501

        Approves the specified project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_approve_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_approve" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in params or
                                                       params['project_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `project_id` when calling `projects_approve`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/{projectId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_assign_vendor(self, project_id, vendor_id, **kwargs):  # noqa: E501
        """Assign Vendor  # noqa: E501

        Assigns the specified vendor to the project and moves the project to the next status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_assign_vendor(project_id, vendor_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier of the project to which the specified vendor should be assigned. This value can be obtained from PortalProjectStatus.Id. (required)
        :param str vendor_id: The vendor identifier. This value can be obtained from PortalVendor.Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_assign_vendor_with_http_info(project_id, vendor_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_assign_vendor_with_http_info(project_id, vendor_id, **kwargs)  # noqa: E501
            return data

    def projects_assign_vendor_with_http_info(self, project_id, vendor_id, **kwargs):  # noqa: E501
        """Assign Vendor  # noqa: E501

        Assigns the specified vendor to the project and moves the project to the next status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_assign_vendor_with_http_info(project_id, vendor_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier of the project to which the specified vendor should be assigned. This value can be obtained from PortalProjectStatus.Id. (required)
        :param str vendor_id: The vendor identifier. This value can be obtained from PortalVendor.Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'vendor_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_assign_vendor" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in params or
                                                       params['project_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `project_id` when calling `projects_assign_vendor`")  # noqa: E501
        # verify the required parameter 'vendor_id' is set
        if self.api_client.client_side_validation and ('vendor_id' not in params or
                                                       params['vendor_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `vendor_id` when calling `projects_assign_vendor`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'vendor_id' in params:
            body_params = params['vendor_id']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/{projectId}/vendor', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_cancel_or_complete(self, project_id, **kwargs):  # noqa: E501
        """Cancel Or Complete  # noqa: E501

        Cancels or completes the specified project.  <br/>If the project is awaiting download, the project will transition through any final steps in the workflow, and will eventually be moved to complete.<br/>If the project is awaiting approval or vendor selection it will be cancelled.<br/>If the project is at any other status, the request will fail.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_cancel_or_complete(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_cancel_or_complete_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_cancel_or_complete_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def projects_cancel_or_complete_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """Cancel Or Complete  # noqa: E501

        Cancels or completes the specified project.  <br/>If the project is awaiting download, the project will transition through any final steps in the workflow, and will eventually be moved to complete.<br/>If the project is awaiting approval or vendor selection it will be cancelled.<br/>If the project is at any other status, the request will fail.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_cancel_or_complete_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_cancel_or_complete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in params or
                                                       params['project_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `project_id` when calling `projects_cancel_or_complete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/{projectId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_cancel_or_complete_file(self, project_id, file_id, **kwargs):  # noqa: E501
        """Cancel Or Complete File  # noqa: E501

        Cancels or completes the specified file within the specified project.  <br/>If the file is awaiting download, the file will transition through any final steps in the workflow, and will eventually be moved to complete.<br/>If the file is awaiting approval or vendor selection it will be cancelled.<br/>If the file is at any other status, the request will fail.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_cancel_or_complete_file(project_id, file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier. (required)
        :param str file_id: The file identifier. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_cancel_or_complete_file_with_http_info(project_id, file_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_cancel_or_complete_file_with_http_info(project_id, file_id, **kwargs)  # noqa: E501
            return data

    def projects_cancel_or_complete_file_with_http_info(self, project_id, file_id, **kwargs):  # noqa: E501
        """Cancel Or Complete File  # noqa: E501

        Cancels or completes the specified file within the specified project.  <br/>If the file is awaiting download, the file will transition through any final steps in the workflow, and will eventually be moved to complete.<br/>If the file is awaiting approval or vendor selection it will be cancelled.<br/>If the file is at any other status, the request will fail.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_cancel_or_complete_file_with_http_info(project_id, file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier. (required)
        :param str file_id: The file identifier. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'file_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_cancel_or_complete_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in params or
                                                       params['project_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `project_id` when calling `projects_cancel_or_complete_file`")  # noqa: E501
        # verify the required parameter 'file_id' is set
        if self.api_client.client_side_validation and ('file_id' not in params or
                                                       params['file_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `file_id` when calling `projects_cancel_or_complete_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501
        if 'file_id' in params:
            path_params['fileId'] = params['file_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/{projectId}/{fileId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_clear_project_templates(self, **kwargs):  # noqa: E501
        """Clear Project Templates  # noqa: E501

        Deletes all portal user project templates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_clear_project_templates(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_clear_project_templates_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.projects_clear_project_templates_with_http_info(**kwargs)  # noqa: E501
            return data

    def projects_clear_project_templates_with_http_info(self, **kwargs):  # noqa: E501
        """Clear Project Templates  # noqa: E501

        Deletes all portal user project templates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_clear_project_templates_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_clear_project_templates" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/templates/clear', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_create(self, project_parameters, **kwargs):  # noqa: E501
        """Create  # noqa: E501

        Creates the specified project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_create(project_parameters, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PortalProjectParams project_parameters: The project creation parameters. (required)
        :return: PortalCreateProjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_create_with_http_info(project_parameters, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_create_with_http_info(project_parameters, **kwargs)  # noqa: E501
            return data

    def projects_create_with_http_info(self, project_parameters, **kwargs):  # noqa: E501
        """Create  # noqa: E501

        Creates the specified project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_create_with_http_info(project_parameters, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PortalProjectParams project_parameters: The project creation parameters. (required)
        :return: PortalCreateProjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_parameters']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_parameters' is set
        if self.api_client.client_side_validation and ('project_parameters' not in params or
                                                       params['project_parameters'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `project_parameters` when calling `projects_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'project_parameters' in params:
            body_params = params['project_parameters']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PortalCreateProjectResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_delete_project_template(self, id, **kwargs):  # noqa: E501
        """Delete Project Template  # noqa: E501

        Delete portal user project templates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_delete_project_template(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The guid of the setting that will be deleted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_delete_project_template_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_delete_project_template_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def projects_delete_project_template_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete Project Template  # noqa: E501

        Delete portal user project templates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_delete_project_template_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The guid of the setting that will be deleted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_delete_project_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `projects_delete_project_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/templates/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_fetch_projects(self, projects, **kwargs):  # noqa: E501
        """Fetch Projects  # noqa: E501

        Gets a specified collection of projects.  <br/>Allows the retrieval of multiple, specific projects in one request.<br/>Any project that cannot be found will simply be ignored. No error will arise.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_fetch_projects(projects, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] projects: The projectIds of the projects to retrieve. (required)
        :return: list[PortalProjectStatus]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_fetch_projects_with_http_info(projects, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_fetch_projects_with_http_info(projects, **kwargs)  # noqa: E501
            return data

    def projects_fetch_projects_with_http_info(self, projects, **kwargs):  # noqa: E501
        """Fetch Projects  # noqa: E501

        Gets a specified collection of projects.  <br/>Allows the retrieval of multiple, specific projects in one request.<br/>Any project that cannot be found will simply be ignored. No error will arise.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_fetch_projects_with_http_info(projects, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] projects: The projectIds of the projects to retrieve. (required)
        :return: list[PortalProjectStatus]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['projects']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_fetch_projects" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'projects' is set
        if self.api_client.client_side_validation and ('projects' not in params or
                                                       params['projects'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `projects` when calling `projects_fetch_projects`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'projects' in params:
            body_params = params['projects']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/fetch', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PortalProjectStatus]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_get_project(self, project_id, **kwargs):  # noqa: E501
        """Get Project  # noqa: E501

        Gets the specified project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_project(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier. (required)
        :param bool include_canceled: Should a canceled project be included in the result.
        :return: PortalProjectStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_get_project_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_get_project_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def projects_get_project_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """Get Project  # noqa: E501

        Gets the specified project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_project_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier. (required)
        :param bool include_canceled: Should a canceled project be included in the result.
        :return: PortalProjectStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'include_canceled']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_get_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in params or
                                                       params['project_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `project_id` when calling `projects_get_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []
        if 'include_canceled' in params:
            query_params.append(('includeCanceled', params['include_canceled']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/{projectId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PortalProjectStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_get_project_creation_options(self, **kwargs):  # noqa: E501
        """Get Project Creation Options  # noqa: E501

        Gets the available project creation options  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_project_creation_options(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int max_options: The maximum number of metadata options returned
        :param str order_by:
        :param int top:
        :param int skip:
        :return: list[PortalProjectOptions]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_get_project_creation_options_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.projects_get_project_creation_options_with_http_info(**kwargs)  # noqa: E501
            return data

    def projects_get_project_creation_options_with_http_info(self, **kwargs):  # noqa: E501
        """Get Project Creation Options  # noqa: E501

        Gets the available project creation options  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_project_creation_options_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int max_options: The maximum number of metadata options returned
        :param str order_by:
        :param int top:
        :param int skip:
        :return: list[PortalProjectOptions]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['max_options', 'order_by', 'top', 'skip']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_get_project_creation_options" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'max_options' in params:
            query_params.append(('maxOptions', params['max_options']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('$orderBy', params['order_by']))  # noqa: E501
        if 'top' in params:
            query_params.append(('$top', params['top']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('$skip', params['skip']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/options', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PortalProjectOptions]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_get_project_creation_options_by_scope_option(self, scope_option_id, **kwargs):  # noqa: E501
        """Get Project Creation Options By Scope Option  # noqa: E501

        Gets the available project creation options.  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_project_creation_options_by_scope_option(scope_option_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_option_id: Scope option Id. (required)
        :param int max_options: The maximum number of metadata options returned
        :param str order_by:
        :param int top:
        :param int skip:
        :return: list[PortalProjectOptions]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_get_project_creation_options_by_scope_option_with_http_info(scope_option_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_get_project_creation_options_by_scope_option_with_http_info(scope_option_id, **kwargs)  # noqa: E501
            return data

    def projects_get_project_creation_options_by_scope_option_with_http_info(self, scope_option_id, **kwargs):  # noqa: E501
        """Get Project Creation Options By Scope Option  # noqa: E501

        Gets the available project creation options.  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_project_creation_options_by_scope_option_with_http_info(scope_option_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_option_id: Scope option Id. (required)
        :param int max_options: The maximum number of metadata options returned
        :param str order_by:
        :param int top:
        :param int skip:
        :return: list[PortalProjectOptions]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scope_option_id', 'max_options', 'order_by', 'top', 'skip']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_get_project_creation_options_by_scope_option" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scope_option_id' is set
        if self.api_client.client_side_validation and ('scope_option_id' not in params or
                                                       params['scope_option_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `scope_option_id` when calling `projects_get_project_creation_options_by_scope_option`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope_option_id' in params:
            path_params['scopeOptionId'] = params['scope_option_id']  # noqa: E501

        query_params = []
        if 'max_options' in params:
            query_params.append(('maxOptions', params['max_options']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('$orderBy', params['order_by']))  # noqa: E501
        if 'top' in params:
            query_params.append(('$top', params['top']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('$skip', params['skip']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/options/{scopeOptionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PortalProjectOptions]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_get_project_group_quote(self, project_group_id, format, **kwargs):  # noqa: E501
        """Get Project Group Quote  # noqa: E501

        Generates a quote for the specified project group.  <br/> Quotes will be provided as either Excel or PDF. If the format parameter is omitted or provides a value other than <code>pdf</code>, and the Accept HTTP header does not contain \"application/pdf\" the quote will be provided in Excel 2003 (XLS) format. The HTTP Accept header takes precedence over the pdf parameter value.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_project_group_quote(project_group_id, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_group_id: The project group identifier. (required)
        :param str format: The format - either xls or pdf. (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_get_project_group_quote_with_http_info(project_group_id, format, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_get_project_group_quote_with_http_info(project_group_id, format, **kwargs)  # noqa: E501
            return data

    def projects_get_project_group_quote_with_http_info(self, project_group_id, format, **kwargs):  # noqa: E501
        """Get Project Group Quote  # noqa: E501

        Generates a quote for the specified project group.  <br/> Quotes will be provided as either Excel or PDF. If the format parameter is omitted or provides a value other than <code>pdf</code>, and the Accept HTTP header does not contain \"application/pdf\" the quote will be provided in Excel 2003 (XLS) format. The HTTP Accept header takes precedence over the pdf parameter value.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_project_group_quote_with_http_info(project_group_id, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_group_id: The project group identifier. (required)
        :param str format: The format - either xls or pdf. (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_group_id', 'format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_get_project_group_quote" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_group_id' is set
        if self.api_client.client_side_validation and ('project_group_id' not in params or
                                                       params['project_group_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `project_group_id` when calling `projects_get_project_group_quote`")  # noqa: E501
        # verify the required parameter 'format' is set
        if self.api_client.client_side_validation and ('format' not in params or
                                                       params['format'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `format` when calling `projects_get_project_group_quote`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_group_id' in params:
            path_params['projectGroupId'] = params['project_group_id']  # noqa: E501
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/projectgroup/{projectGroupId}/quote/{format}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_get_project_quote(self, project_id, format, **kwargs):  # noqa: E501
        """Get Project Quote  # noqa: E501

        Generates a quote for the specified project.  <br/> Quotes will be provided as either Excel or PDF. If the format parameter is omitted or provides a value other than <code>pdf</code>, and the Accept HTTP header does not contain \"application/pdf\" the quote will be provided in Excel 2003 (XLS) format. The HTTP Accept header takes precedence over the pdf parameter value.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_project_quote(project_id, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier. (required)
        :param str format: The format - either xls or pdf. (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_get_project_quote_with_http_info(project_id, format, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_get_project_quote_with_http_info(project_id, format, **kwargs)  # noqa: E501
            return data

    def projects_get_project_quote_with_http_info(self, project_id, format, **kwargs):  # noqa: E501
        """Get Project Quote  # noqa: E501

        Generates a quote for the specified project.  <br/> Quotes will be provided as either Excel or PDF. If the format parameter is omitted or provides a value other than <code>pdf</code>, and the Accept HTTP header does not contain \"application/pdf\" the quote will be provided in Excel 2003 (XLS) format. The HTTP Accept header takes precedence over the pdf parameter value.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_project_quote_with_http_info(project_id, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier. (required)
        :param str format: The format - either xls or pdf. (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_get_project_quote" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in params or
                                                       params['project_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `project_id` when calling `projects_get_project_quote`")  # noqa: E501
        # verify the required parameter 'format' is set
        if self.api_client.client_side_validation and ('format' not in params or
                                                       params['format'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `format` when calling `projects_get_project_quote`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/{projectId}/quote/{format}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_get_project_scope_options(self, **kwargs):  # noqa: E501
        """Get Project Scope Options  # noqa: E501

        Gets the available scope options  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_project_scope_options(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool hierarchical: If true it will return a hierarhical list
        :param str order_by:
        :param int top:
        :param int skip:
        :return: list[PortalScopeOption]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_get_project_scope_options_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.projects_get_project_scope_options_with_http_info(**kwargs)  # noqa: E501
            return data

    def projects_get_project_scope_options_with_http_info(self, **kwargs):  # noqa: E501
        """Get Project Scope Options  # noqa: E501

        Gets the available scope options  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_project_scope_options_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool hierarchical: If true it will return a hierarhical list
        :param str order_by:
        :param int top:
        :param int skip:
        :return: list[PortalScopeOption]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hierarchical', 'order_by', 'top', 'skip']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_get_project_scope_options" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'hierarchical' in params:
            query_params.append(('hierarchical', params['hierarchical']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('$orderBy', params['order_by']))  # noqa: E501
        if 'top' in params:
            query_params.append(('$top', params['top']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('$skip', params['skip']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/scopeoptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PortalScopeOption]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_get_project_templates(self, **kwargs):  # noqa: E501
        """Get Project Templates  # noqa: E501

        Get portal user project templates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_project_templates(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Optional specifying the guid of the setting to be returned
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_get_project_templates_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.projects_get_project_templates_with_http_info(**kwargs)  # noqa: E501
            return data

    def projects_get_project_templates_with_http_info(self, **kwargs):  # noqa: E501
        """Get Project Templates  # noqa: E501

        Get portal user project templates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_project_templates_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Optional specifying the guid of the setting to be returned
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_get_project_templates" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/templates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_get_project_zip(self, project_id, **kwargs):  # noqa: E501
        """Get Project Zip  # noqa: E501

        Gets the zip of translated files for the specified project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_project_zip(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier. (required)
        :param str types: The types to download. 1 = TargetFiles, 2 = SourceFiles, 4 = ReferenceFiles
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_get_project_zip_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_get_project_zip_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def projects_get_project_zip_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """Get Project Zip  # noqa: E501

        Gets the zip of translated files for the specified project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_project_zip_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier. (required)
        :param str types: The types to download. 1 = TargetFiles, 2 = SourceFiles, 4 = ReferenceFiles
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'types']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_get_project_zip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in params or
                                                       params['project_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `project_id` when calling `projects_get_project_zip`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []
        if 'types' in params:
            query_params.append(('types', params['types']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/{projectId}/zip', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_get_project_zip_with_specific_files(self, project_id, download_files, **kwargs):  # noqa: E501
        """Get Project Zip With Specific Files  # noqa: E501

        Gets the zip of translated files for the specified project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_project_zip_with_specific_files(project_id, download_files, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier. (required)
        :param DownloadFiles download_files: An object with string[] TargetFiles property (required)
        :param str types: The types to download. 1 = TargetFiles, 2 = SourceFiles, 4 = ReferenceFiles
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_get_project_zip_with_specific_files_with_http_info(project_id, download_files, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_get_project_zip_with_specific_files_with_http_info(project_id, download_files, **kwargs)  # noqa: E501
            return data

    def projects_get_project_zip_with_specific_files_with_http_info(self, project_id, download_files, **kwargs):  # noqa: E501
        """Get Project Zip With Specific Files  # noqa: E501

        Gets the zip of translated files for the specified project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_project_zip_with_specific_files_with_http_info(project_id, download_files, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier. (required)
        :param DownloadFiles download_files: An object with string[] TargetFiles property (required)
        :param str types: The types to download. 1 = TargetFiles, 2 = SourceFiles, 4 = ReferenceFiles
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'download_files', 'types']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_get_project_zip_with_specific_files" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in params or
                                                       params['project_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `project_id` when calling `projects_get_project_zip_with_specific_files`")  # noqa: E501
        # verify the required parameter 'download_files' is set
        if self.api_client.client_side_validation and ('download_files' not in params or
                                                       params['download_files'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `download_files` when calling `projects_get_project_zip_with_specific_files`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []
        if 'types' in params:
            query_params.append(('types', params['types']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'download_files' in params:
            body_params = params['download_files']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/{projectId}/zip', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_get_projects(self, **kwargs):  # noqa: E501
        """Get Projects  # noqa: E501

        Gets information about every project available to the user.  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_projects(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_by:
        :param int top:
        :param int skip:
        :return: list[PortalProjectStatus]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_get_projects_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.projects_get_projects_with_http_info(**kwargs)  # noqa: E501
            return data

    def projects_get_projects_with_http_info(self, **kwargs):  # noqa: E501
        """Get Projects  # noqa: E501

        Gets information about every project available to the user.  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_projects_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_by:
        :param int top:
        :param int skip:
        :return: list[PortalProjectStatus]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_by', 'top', 'skip']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_get_projects" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_by' in params:
            query_params.append(('$orderBy', params['order_by']))  # noqa: E501
        if 'top' in params:
            query_params.append(('$top', params['top']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('$skip', params['skip']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PortalProjectStatus]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_get_projects_at_status(self, status, **kwargs):  # noqa: E501
        """Get Projects At Status  # noqa: E501

        Gets all available projects at the specified status.  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_projects_at_status(status, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status: The status. 0 = Preparing, 1 = ForApproval, 2 = InProgress, 3 = ForDownload, 4 = Completed, 5 = PartialDownload, 6 = InReview, 7 = Reviewed, 8 = InSignOff, 9 = SignedOff, 10 = ForVendorSelection, 11 = Cancelled, 12 = New (required)
        :param str order_by:
        :param int top:
        :param int skip:
        :return: list[PortalProjectStatus]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_get_projects_at_status_with_http_info(status, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_get_projects_at_status_with_http_info(status, **kwargs)  # noqa: E501
            return data

    def projects_get_projects_at_status_with_http_info(self, status, **kwargs):  # noqa: E501
        """Get Projects At Status  # noqa: E501

        Gets all available projects at the specified status.  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_projects_at_status_with_http_info(status, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status: The status. 0 = Preparing, 1 = ForApproval, 2 = InProgress, 3 = ForDownload, 4 = Completed, 5 = PartialDownload, 6 = InReview, 7 = Reviewed, 8 = InSignOff, 9 = SignedOff, 10 = ForVendorSelection, 11 = Cancelled, 12 = New (required)
        :param str order_by:
        :param int top:
        :param int skip:
        :return: list[PortalProjectStatus]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['status', 'order_by', 'top', 'skip']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_get_projects_at_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'status' is set
        if self.api_client.client_side_validation and ('status' not in params or
                                                       params['status'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `status` when calling `projects_get_projects_at_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'status' in params:
            path_params['status'] = params['status']  # noqa: E501

        query_params = []
        if 'order_by' in params:
            query_params.append(('$orderBy', params['order_by']))  # noqa: E501
        if 'top' in params:
            query_params.append(('$top', params['top']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('$skip', params['skip']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/status/{status}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PortalProjectStatus]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_get_projects_list(self, **kwargs):  # noqa: E501
        """Get Projects List  # noqa: E501

        Gets a simple list of all projects, providing general information about each project.  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_projects_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_by:
        :param int top:
        :param int skip:
        :return: list[PortalProjectListEntry]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_get_projects_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.projects_get_projects_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def projects_get_projects_list_with_http_info(self, **kwargs):  # noqa: E501
        """Get Projects List  # noqa: E501

        Gets a simple list of all projects, providing general information about each project.  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_projects_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_by:
        :param int top:
        :param int skip:
        :return: list[PortalProjectListEntry]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_by', 'top', 'skip']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_get_projects_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_by' in params:
            query_params.append(('$orderBy', params['order_by']))  # noqa: E501
        if 'top' in params:
            query_params.append(('$top', params['top']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('$skip', params['skip']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PortalProjectListEntry]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_get_projects_list_at_status(self, status, **kwargs):  # noqa: E501
        """Get Projects List At Status  # noqa: E501

        Gets a simple list of all projects at the specified status, providing only the most basic information about each project.  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_projects_list_at_status(status, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status: The status. 0 = Preparing, 1 = ForApproval, 2 = InProgress, 3 = ForDownload, 4 = Completed, 5 = PartialDownload, 6 = InReview, 7 = Reviewed, 8 = InSignOff, 9 = SignedOff, 10 = ForVendorSelection, 11 = Cancelled, 12 = New (required)
        :param str order_by:
        :param int top:
        :param int skip:
        :return: list[PortalProjectListEntry]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_get_projects_list_at_status_with_http_info(status, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_get_projects_list_at_status_with_http_info(status, **kwargs)  # noqa: E501
            return data

    def projects_get_projects_list_at_status_with_http_info(self, status, **kwargs):  # noqa: E501
        """Get Projects List At Status  # noqa: E501

        Gets a simple list of all projects at the specified status, providing only the most basic information about each project.  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_projects_list_at_status_with_http_info(status, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status: The status. 0 = Preparing, 1 = ForApproval, 2 = InProgress, 3 = ForDownload, 4 = Completed, 5 = PartialDownload, 6 = InReview, 7 = Reviewed, 8 = InSignOff, 9 = SignedOff, 10 = ForVendorSelection, 11 = Cancelled, 12 = New (required)
        :param str order_by:
        :param int top:
        :param int skip:
        :return: list[PortalProjectListEntry]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['status', 'order_by', 'top', 'skip']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_get_projects_list_at_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'status' is set
        if self.api_client.client_side_validation and ('status' not in params or
                                                       params['status'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `status` when calling `projects_get_projects_list_at_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'status' in params:
            path_params['status'] = params['status']  # noqa: E501

        query_params = []
        if 'order_by' in params:
            query_params.append(('$orderBy', params['order_by']))  # noqa: E501
        if 'top' in params:
            query_params.append(('$top', params['top']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('$skip', params['skip']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/list/{status}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PortalProjectListEntry]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_get_projects_with_search_term(self, term, **kwargs):  # noqa: E501
        """Get Projects With Search Term  # noqa: E501

        Provides projects that contain the specified search term.  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_projects_with_search_term(term, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str term: The term. (required)
        :param str order_by:
        :param int top:
        :param int skip:
        :return: list[PortalProjectStatus]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_get_projects_with_search_term_with_http_info(term, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_get_projects_with_search_term_with_http_info(term, **kwargs)  # noqa: E501
            return data

    def projects_get_projects_with_search_term_with_http_info(self, term, **kwargs):  # noqa: E501
        """Get Projects With Search Term  # noqa: E501

        Provides projects that contain the specified search term.  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_projects_with_search_term_with_http_info(term, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str term: The term. (required)
        :param str order_by:
        :param int top:
        :param int skip:
        :return: list[PortalProjectStatus]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['term', 'order_by', 'top', 'skip']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_get_projects_with_search_term" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'term' is set
        if self.api_client.client_side_validation and ('term' not in params or
                                                       params['term'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `term` when calling `projects_get_projects_with_search_term`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'term' in params:
            path_params['term'] = params['term']  # noqa: E501

        query_params = []
        if 'order_by' in params:
            query_params.append(('$orderBy', params['order_by']))  # noqa: E501
        if 'top' in params:
            query_params.append(('$top', params['top']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('$skip', params['skip']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/search/{term}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PortalProjectStatus]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_get_search_meta_data_options(self, id, search_expression, **kwargs):  # noqa: E501
        """Get Search Meta Data Options  # noqa: E501

        returns a list of matching metadata options  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_search_meta_data_options(id, search_expression, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The metadata id (required)
        :param str search_expression: A string representing the searched expressions (required)
        :param int max_options: The maximum number of metadata options returned
        :return: list[PortalProjectOptions]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_get_search_meta_data_options_with_http_info(id, search_expression, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_get_search_meta_data_options_with_http_info(id, search_expression, **kwargs)  # noqa: E501
            return data

    def projects_get_search_meta_data_options_with_http_info(self, id, search_expression, **kwargs):  # noqa: E501
        """Get Search Meta Data Options  # noqa: E501

        returns a list of matching metadata options  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_get_search_meta_data_options_with_http_info(id, search_expression, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The metadata id (required)
        :param str search_expression: A string representing the searched expressions (required)
        :param int max_options: The maximum number of metadata options returned
        :return: list[PortalProjectOptions]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'search_expression', 'max_options']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_get_search_meta_data_options" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `projects_get_search_meta_data_options`")  # noqa: E501
        # verify the required parameter 'search_expression' is set
        if self.api_client.client_side_validation and ('search_expression' not in params or
                                                       params['search_expression'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `search_expression` when calling `projects_get_search_meta_data_options`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'search_expression' in params:
            query_params.append(('searchExpression', params['search_expression']))  # noqa: E501
        if 'max_options' in params:
            query_params.append(('maxOptions', params['max_options']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/options/metadata/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PortalProjectOptions]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_reject_file(self, project_id, file_id, reject_message, **kwargs):  # noqa: E501
        """Reject File  # noqa: E501

        Allows rejecting a task with a rejection message .  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_reject_file(project_id, file_id, reject_message, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier. (required)
        :param str file_id: The file identifier. (required)
        :param str reject_message: The rejection message. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_reject_file_with_http_info(project_id, file_id, reject_message, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_reject_file_with_http_info(project_id, file_id, reject_message, **kwargs)  # noqa: E501
            return data

    def projects_reject_file_with_http_info(self, project_id, file_id, reject_message, **kwargs):  # noqa: E501
        """Reject File  # noqa: E501

        Allows rejecting a task with a rejection message .  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_reject_file_with_http_info(project_id, file_id, reject_message, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier. (required)
        :param str file_id: The file identifier. (required)
        :param str reject_message: The rejection message. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'file_id', 'reject_message']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_reject_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in params or
                                                       params['project_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `project_id` when calling `projects_reject_file`")  # noqa: E501
        # verify the required parameter 'file_id' is set
        if self.api_client.client_side_validation and ('file_id' not in params or
                                                       params['file_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `file_id` when calling `projects_reject_file`")  # noqa: E501
        # verify the required parameter 'reject_message' is set
        if self.api_client.client_side_validation and ('reject_message' not in params or
                                                       params['reject_message'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `reject_message` when calling `projects_reject_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501
        if 'file_id' in params:
            path_params['fileId'] = params['file_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'reject_message' in params:
            body_params = params['reject_message']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/{projectId}/reject/{fileId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_report_file_problem(self, project_id, file_id, error_message, **kwargs):  # noqa: E501
        """Report File Problem  # noqa: E501

        Allows reporting a problem with a file that has been downloaded.  <br/>For example, during import into your repository an Xml file fails DTD/schema validation because of a tag ordering problem introduced during translation. Use this method to tell us about the problem - the file will be routed to an engineer for investigation and will be moved to the \"InProgress\" status.<br/>Once the problem is resolved, the file will return to \"ForDownload\" and you can retrieve the file again.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_report_file_problem(project_id, file_id, error_message, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier. (required)
        :param str file_id: The file identifier. (required)
        :param str error_message: The error message. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_report_file_problem_with_http_info(project_id, file_id, error_message, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_report_file_problem_with_http_info(project_id, file_id, error_message, **kwargs)  # noqa: E501
            return data

    def projects_report_file_problem_with_http_info(self, project_id, file_id, error_message, **kwargs):  # noqa: E501
        """Report File Problem  # noqa: E501

        Allows reporting a problem with a file that has been downloaded.  <br/>For example, during import into your repository an Xml file fails DTD/schema validation because of a tag ordering problem introduced during translation. Use this method to tell us about the problem - the file will be routed to an engineer for investigation and will be moved to the \"InProgress\" status.<br/>Once the problem is resolved, the file will return to \"ForDownload\" and you can retrieve the file again.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_report_file_problem_with_http_info(project_id, file_id, error_message, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier. (required)
        :param str file_id: The file identifier. (required)
        :param str error_message: The error message. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'file_id', 'error_message']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_report_file_problem" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in params or
                                                       params['project_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `project_id` when calling `projects_report_file_problem`")  # noqa: E501
        # verify the required parameter 'file_id' is set
        if self.api_client.client_side_validation and ('file_id' not in params or
                                                       params['file_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `file_id` when calling `projects_report_file_problem`")  # noqa: E501
        # verify the required parameter 'error_message' is set
        if self.api_client.client_side_validation and ('error_message' not in params or
                                                       params['error_message'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `error_message` when calling `projects_report_file_problem`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501
        if 'file_id' in params:
            path_params['fileId'] = params['file_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'error_message' in params:
            body_params = params['error_message']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/{projectId}/{fileId}/error', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_set_project_templates(self, portal_user_project_template, **kwargs):  # noqa: E501
        """Set Project Templates  # noqa: E501

        Save portal user project templates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_set_project_templates(portal_user_project_template, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PortalUserProjectTemplate portal_user_project_template: The project template settings (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_set_project_templates_with_http_info(portal_user_project_template, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_set_project_templates_with_http_info(portal_user_project_template, **kwargs)  # noqa: E501
            return data

    def projects_set_project_templates_with_http_info(self, portal_user_project_template, **kwargs):  # noqa: E501
        """Set Project Templates  # noqa: E501

        Save portal user project templates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_set_project_templates_with_http_info(portal_user_project_template, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PortalUserProjectTemplate portal_user_project_template: The project template settings (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['portal_user_project_template']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_set_project_templates" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'portal_user_project_template' is set
        if self.api_client.client_side_validation and ('portal_user_project_template' not in params or
                                                       params['portal_user_project_template'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `portal_user_project_template` when calling `projects_set_project_templates`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'portal_user_project_template' in params:
            body_params = params['portal_user_project_template']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/templates', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_start_project(self, project_id, **kwargs):  # noqa: E501
        """Start Project  # noqa: E501

        Starts the specified project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_start_project(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier. (required)
        :return: PortalStartProjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_start_project_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_start_project_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def projects_start_project_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """Start Project  # noqa: E501

        Starts the specified project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_start_project_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier. (required)
        :return: PortalStartProjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_start_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in params or
                                                       params['project_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `project_id` when calling `projects_start_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/projects/{projectId}/start', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PortalStartProjectResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
