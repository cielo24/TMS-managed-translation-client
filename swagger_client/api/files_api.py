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


class FilesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def files_add_reference_file(self, file, project_id, **kwargs):  # noqa: E501
        """Add Reference File  # noqa: E501

        Add a reference file to an existing project.  <br/> If the content you provide is encoded using Base64 encoding, please supply an HTTP header named \" X-Base64-Content\" to indicate the provided content should be Base64 Decoded prior to processing. The value of the HTTP header should any of \"true\", \"yes\" or \"1\" to indicate that the content is Base64 encoded. Any other value, or the absence of the header, will result in the content being handled without first being Base64 decoded.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_add_reference_file(file, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file: (required)
        :param str project_id: The project identifier. (required)
        :return: list[LcFile]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.files_add_reference_file_with_http_info(file, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.files_add_reference_file_with_http_info(file, project_id, **kwargs)  # noqa: E501
            return data

    def files_add_reference_file_with_http_info(self, file, project_id, **kwargs):  # noqa: E501
        """Add Reference File  # noqa: E501

        Add a reference file to an existing project.  <br/> If the content you provide is encoded using Base64 encoding, please supply an HTTP header named \" X-Base64-Content\" to indicate the provided content should be Base64 Decoded prior to processing. The value of the HTTP header should any of \"true\", \"yes\" or \"1\" to indicate that the content is Base64 encoded. Any other value, or the absence of the header, will result in the content being handled without first being Base64 decoded.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_add_reference_file_with_http_info(file, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file: (required)
        :param str project_id: The project identifier. (required)
        :return: list[LcFile]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'project_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method files_add_reference_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `files_add_reference_file`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `files_add_reference_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/files/{projectId}/reference', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[LcFile]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def files_delete(self, file_id, **kwargs):  # noqa: E501
        """Delete  # noqa: E501

        Deletes a previously uploaded file from the repository. If a file is included in a translation project, it will be automatically deleted from the             repository once the project has been created, and will no longer appear in the list of files returned by [Get Files](#operation/Files_GetFiles).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_delete(file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file_id: The file identifier supplied in the FileId property of the response to an upload. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.files_delete_with_http_info(file_id, **kwargs)  # noqa: E501
        else:
            (data) = self.files_delete_with_http_info(file_id, **kwargs)  # noqa: E501
            return data

    def files_delete_with_http_info(self, file_id, **kwargs):  # noqa: E501
        """Delete  # noqa: E501

        Deletes a previously uploaded file from the repository. If a file is included in a translation project, it will be automatically deleted from the             repository once the project has been created, and will no longer appear in the list of files returned by [Get Files](#operation/Files_GetFiles).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_delete_with_http_info(file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file_id: The file identifier supplied in the FileId property of the response to an upload. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method files_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_id' is set
        if ('file_id' not in params or
                params['file_id'] is None):
            raise ValueError("Missing the required parameter `file_id` when calling `files_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'file_id' in params:
            path_params['fileId'] = params['file_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/files/{fileId}', 'DELETE',
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

    def files_get_files(self, project_options_id, **kwargs):  # noqa: E501
        """Get Files  # noqa: E501

        Gets information about previously uploaded files that have not yet been included in a translation project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_get_files(project_options_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_options_id: The project options identifier - if specified, the returned list of files will be             evaluated for suitability against the specified project creation options. (required)
        :return: list[LcFile]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.files_get_files_with_http_info(project_options_id, **kwargs)  # noqa: E501
        else:
            (data) = self.files_get_files_with_http_info(project_options_id, **kwargs)  # noqa: E501
            return data

    def files_get_files_with_http_info(self, project_options_id, **kwargs):  # noqa: E501
        """Get Files  # noqa: E501

        Gets information about previously uploaded files that have not yet been included in a translation project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_get_files_with_http_info(project_options_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_options_id: The project options identifier - if specified, the returned list of files will be             evaluated for suitability against the specified project creation options. (required)
        :return: list[LcFile]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_options_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method files_get_files" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_options_id' is set
        if ('project_options_id' not in params or
                params['project_options_id'] is None):
            raise ValueError("Missing the required parameter `project_options_id` when calling `files_get_files`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_options_id' in params:
            path_params['projectOptionsId'] = params['project_options_id']  # noqa: E501

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
            '/tm4lc/api/v1/files/{projectOptionsId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[LcFile]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def files_get_studio_packages(self, body, **kwargs):  # noqa: E501
        """Get Studio Packages  # noqa: E501

        Retrieves the studio packages for specified projects  <br/> This API method allows you to retrieve studio package file   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_get_studio_packages(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: The project identifier as supplied by PortalProjectStatus.Id. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.files_get_studio_packages_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.files_get_studio_packages_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def files_get_studio_packages_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get Studio Packages  # noqa: E501

        Retrieves the studio packages for specified projects  <br/> This API method allows you to retrieve studio package file   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_get_studio_packages_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: The project identifier as supplied by PortalProjectStatus.Id. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method files_get_studio_packages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `files_get_studio_packages`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/files/studiopackage/download', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def files_get_studio_packages_by_files(self, body, **kwargs):  # noqa: E501
        """Get Studio Packages By Files  # noqa: E501

        Retrieves the studio packages for specified files  <br/> This API method allows you to retrieve studio package file   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_get_studio_packages_by_files(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: A list of file identifiers (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.files_get_studio_packages_by_files_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.files_get_studio_packages_by_files_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def files_get_studio_packages_by_files_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get Studio Packages By Files  # noqa: E501

        Retrieves the studio packages for specified files  <br/> This API method allows you to retrieve studio package file   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_get_studio_packages_by_files_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: A list of file identifiers (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method files_get_studio_packages_by_files" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `files_get_studio_packages_by_files`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/files/studiopackage/downloadbyfile', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def files_get_translated_file(self, project_id, file_id, **kwargs):  # noqa: E501
        """Get Translated File  # noqa: E501

        Retrieves the contents of a single translated file, contained within the specified project. If the requested file is not yet             at the Download status, the content of the file may not yet be fully translated. If the file is at the Download status,             and you have successfully retrieved it, you will want to mark the file as Complete using the             [Cancel Or Complete File](#operation/Projects_CancelOrCompleteFile) method.  <br/> This API method allows you to retrieve a single translated file, by specifying the projectId and fileId. The fileId parameter can be obtained from the <code>PortalProjectFileDetails.Id</code> member.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_get_translated_file(project_id, file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier as supplied by PortalProjectStatus.Id. (required)
        :param str file_id: The target-language file identifier, for example project.LanguagePairDetails[0].Files[0].Id. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.files_get_translated_file_with_http_info(project_id, file_id, **kwargs)  # noqa: E501
        else:
            (data) = self.files_get_translated_file_with_http_info(project_id, file_id, **kwargs)  # noqa: E501
            return data

    def files_get_translated_file_with_http_info(self, project_id, file_id, **kwargs):  # noqa: E501
        """Get Translated File  # noqa: E501

        Retrieves the contents of a single translated file, contained within the specified project. If the requested file is not yet             at the Download status, the content of the file may not yet be fully translated. If the file is at the Download status,             and you have successfully retrieved it, you will want to mark the file as Complete using the             [Cancel Or Complete File](#operation/Projects_CancelOrCompleteFile) method.  <br/> This API method allows you to retrieve a single translated file, by specifying the projectId and fileId. The fileId parameter can be obtained from the <code>PortalProjectFileDetails.Id</code> member.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_get_translated_file_with_http_info(project_id, file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: The project identifier as supplied by PortalProjectStatus.Id. (required)
        :param str file_id: The target-language file identifier, for example project.LanguagePairDetails[0].Files[0].Id. (required)
        :return: str
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
                    " to method files_get_translated_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `files_get_translated_file`")  # noqa: E501
        # verify the required parameter 'file_id' is set
        if ('file_id' not in params or
                params['file_id'] is None):
            raise ValueError("Missing the required parameter `file_id` when calling `files_get_translated_file`")  # noqa: E501

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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/files/{projectId}/{fileId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def files_set_studio_package(self, file, **kwargs):  # noqa: E501
        """Set Studio Package  # noqa: E501

        Allows studio package file uploads. Uploads must be submitted using              [multipart/form-data](https://www.w3.org/TR/html401/interact/forms.html#h-17.13.4.2) and can contain more             than one file, although this is rarely useful and increases the impact of any failure.              In the case of archives (zip, rar, 7z, tar files) we will examine the contents of the archive and will upload             each file separately.  <br/> If the content you provide is encoded using Base64 encoding, please supply an HTTP header named \" X-Base64-Content\" to indicate the provided content should be Base64 Decoded prior to processing. The value of the HTTP header should any of \"true\", \"yes\" or \"1\" to indicate that the content is Base64 encoded. Any other value, or the absence of the header, will result in the content being handled without first being Base64 decoded.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_set_studio_package(file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.files_set_studio_package_with_http_info(file, **kwargs)  # noqa: E501
        else:
            (data) = self.files_set_studio_package_with_http_info(file, **kwargs)  # noqa: E501
            return data

    def files_set_studio_package_with_http_info(self, file, **kwargs):  # noqa: E501
        """Set Studio Package  # noqa: E501

        Allows studio package file uploads. Uploads must be submitted using              [multipart/form-data](https://www.w3.org/TR/html401/interact/forms.html#h-17.13.4.2) and can contain more             than one file, although this is rarely useful and increases the impact of any failure.              In the case of archives (zip, rar, 7z, tar files) we will examine the contents of the archive and will upload             each file separately.  <br/> If the content you provide is encoded using Base64 encoding, please supply an HTTP header named \" X-Base64-Content\" to indicate the provided content should be Base64 Decoded prior to processing. The value of the HTTP header should any of \"true\", \"yes\" or \"1\" to indicate that the content is Base64 encoded. Any other value, or the absence of the header, will result in the content being handled without first being Base64 decoded.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_set_studio_package_with_http_info(file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method files_set_studio_package" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `files_set_studio_package`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/files/studiopackage/upload', 'POST',
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

    def files_upload(self, file, project_options_id, **kwargs):  # noqa: E501
        """Upload  # noqa: E501

        Allows uploads of files for translation or for inclusion in a translation project as reference material. Uploads must be             submitted using [multipart/form-data](https://www.w3.org/TR/html401/interact/forms.html#h-17.13.4.2) and can contain more             than one file, although this is rarely useful and increases the impact of any failure. The Uri requires you to specify             the ProjectOptionId that should be used to evaluate the uploaded file(s).             This is used to enable us to consider whether each file you upload is a possible candidate for translation or must be handled as             reference material. In the case of archives (zip, rar, 7z, tar files) we will examine the contents of the archive and indicate             whether the archive as a whole can be translated or not, or whether it contains a mixture of translatable and non-translatable files.  <br/> If the content you provide is encoded using Base64 encoding, please supply an HTTP header named \" X-Base64-Content\" to indicate that the provided content should be Base64 Decoded prior to processing. The value of the HTTP header should any of \"true\", \"yes\" or \"1\" to indicate that the content is Base64 encoded. Any other value, or the absence of the header, will result in the content being handled without first being Base64 decoded.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_upload(file, project_options_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file: (required)
        :param str project_options_id: The project options identifier against which the uploaded file will be evaluated. (required)
        :return: list[LcFile]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.files_upload_with_http_info(file, project_options_id, **kwargs)  # noqa: E501
        else:
            (data) = self.files_upload_with_http_info(file, project_options_id, **kwargs)  # noqa: E501
            return data

    def files_upload_with_http_info(self, file, project_options_id, **kwargs):  # noqa: E501
        """Upload  # noqa: E501

        Allows uploads of files for translation or for inclusion in a translation project as reference material. Uploads must be             submitted using [multipart/form-data](https://www.w3.org/TR/html401/interact/forms.html#h-17.13.4.2) and can contain more             than one file, although this is rarely useful and increases the impact of any failure. The Uri requires you to specify             the ProjectOptionId that should be used to evaluate the uploaded file(s).             This is used to enable us to consider whether each file you upload is a possible candidate for translation or must be handled as             reference material. In the case of archives (zip, rar, 7z, tar files) we will examine the contents of the archive and indicate             whether the archive as a whole can be translated or not, or whether it contains a mixture of translatable and non-translatable files.  <br/> If the content you provide is encoded using Base64 encoding, please supply an HTTP header named \" X-Base64-Content\" to indicate that the provided content should be Base64 Decoded prior to processing. The value of the HTTP header should any of \"true\", \"yes\" or \"1\" to indicate that the content is Base64 encoded. Any other value, or the absence of the header, will result in the content being handled without first being Base64 decoded.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_upload_with_http_info(file, project_options_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file: (required)
        :param str project_options_id: The project options identifier against which the uploaded file will be evaluated. (required)
        :return: list[LcFile]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'project_options_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method files_upload" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `files_upload`")  # noqa: E501
        # verify the required parameter 'project_options_id' is set
        if ('project_options_id' not in params or
                params['project_options_id'] is None):
            raise ValueError("Missing the required parameter `project_options_id` when calling `files_upload`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_options_id' in params:
            path_params['projectOptionsId'] = params['project_options_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/files/{projectOptionsId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[LcFile]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
