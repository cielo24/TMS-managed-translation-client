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


class TranslationMemoryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def translation_memory_get_tm_search_options(self, request_inherited_configs, **kwargs):  # noqa: E501
        """Get Tm Search Options  # noqa: E501

        Gets the available translation memory search options  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.translation_memory_get_tm_search_options(request_inherited_configs, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool request_inherited_configs: Use inherited configs. (required)
        :return: list[PortalTmOptions]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.translation_memory_get_tm_search_options_with_http_info(request_inherited_configs, **kwargs)  # noqa: E501
        else:
            (data) = self.translation_memory_get_tm_search_options_with_http_info(request_inherited_configs, **kwargs)  # noqa: E501
            return data

    def translation_memory_get_tm_search_options_with_http_info(self, request_inherited_configs, **kwargs):  # noqa: E501
        """Get Tm Search Options  # noqa: E501

        Gets the available translation memory search options  <br/>This method allows the results to be paged, by specifying <code>$top</code>, <code>$skip</code> and <code>$orderby</code> query parameters.<br/><code>http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752361</code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.translation_memory_get_tm_search_options_with_http_info(request_inherited_configs, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool request_inherited_configs: Use inherited configs. (required)
        :return: list[PortalTmOptions]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request_inherited_configs']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method translation_memory_get_tm_search_options" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request_inherited_configs' is set
        if ('request_inherited_configs' not in params or
                params['request_inherited_configs'] is None):
            raise ValueError("Missing the required parameter `request_inherited_configs` when calling `translation_memory_get_tm_search_options`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'request_inherited_configs' in params:
            path_params['requestInheritedConfigs'] = params['request_inherited_configs']  # noqa: E501

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
            '/tm4lc/api/v1/tm/options/{requestInheritedConfigs}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PortalTmOptions]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def translation_memory_search_by_file(self, body, file_id, **kwargs):  # noqa: E501
        """Search By File  # noqa: E501

        Performs a Tm search against the translation memories associated with the specified file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.translation_memory_search_by_file(body, file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TmSearchParams body: The search parameters. (required)
        :param str file_id: The file identifier. (required)
        :return: list[TmSearchResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.translation_memory_search_by_file_with_http_info(body, file_id, **kwargs)  # noqa: E501
        else:
            (data) = self.translation_memory_search_by_file_with_http_info(body, file_id, **kwargs)  # noqa: E501
            return data

    def translation_memory_search_by_file_with_http_info(self, body, file_id, **kwargs):  # noqa: E501
        """Search By File  # noqa: E501

        Performs a Tm search against the translation memories associated with the specified file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.translation_memory_search_by_file_with_http_info(body, file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TmSearchParams body: The search parameters. (required)
        :param str file_id: The file identifier. (required)
        :return: list[TmSearchResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'file_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method translation_memory_search_by_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `translation_memory_search_by_file`")  # noqa: E501
        # verify the required parameter 'file_id' is set
        if ('file_id' not in params or
                params['file_id'] is None):
            raise ValueError("Missing the required parameter `file_id` when calling `translation_memory_search_by_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'file_id' in params:
            path_params['fileId'] = params['file_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/tm/search/file/{fileId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TmSearchResult]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def translation_memory_search_by_project_option(self, body, project_options_id, **kwargs):  # noqa: E501
        """Search By Project Option  # noqa: E501

        Performs a Tm search against the translation memories associated with the specified project option.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.translation_memory_search_by_project_option(body, project_options_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TmSearchParams body: The search parameters. (required)
        :param str project_options_id: The project options identifier. (required)
        :return: list[TmSearchResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.translation_memory_search_by_project_option_with_http_info(body, project_options_id, **kwargs)  # noqa: E501
        else:
            (data) = self.translation_memory_search_by_project_option_with_http_info(body, project_options_id, **kwargs)  # noqa: E501
            return data

    def translation_memory_search_by_project_option_with_http_info(self, body, project_options_id, **kwargs):  # noqa: E501
        """Search By Project Option  # noqa: E501

        Performs a Tm search against the translation memories associated with the specified project option.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.translation_memory_search_by_project_option_with_http_info(body, project_options_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TmSearchParams body: The search parameters. (required)
        :param str project_options_id: The project options identifier. (required)
        :return: list[TmSearchResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'project_options_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method translation_memory_search_by_project_option" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `translation_memory_search_by_project_option`")  # noqa: E501
        # verify the required parameter 'project_options_id' is set
        if ('project_options_id' not in params or
                params['project_options_id'] is None):
            raise ValueError("Missing the required parameter `project_options_id` when calling `translation_memory_search_by_project_option`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_options_id' in params:
            path_params['projectOptionsId'] = params['project_options_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/tm/search/{projectOptionsId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TmSearchResult]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def translation_memory_update_by_file(self, body, file_id, **kwargs):  # noqa: E501
        """Update By File  # noqa: E501

        Performs a Tm update against the translation memories associated with the specified file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.translation_memory_update_by_file(body, file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TmUpdateParams body: The update parameters. (required)
        :param str file_id: The file identifier. (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.translation_memory_update_by_file_with_http_info(body, file_id, **kwargs)  # noqa: E501
        else:
            (data) = self.translation_memory_update_by_file_with_http_info(body, file_id, **kwargs)  # noqa: E501
            return data

    def translation_memory_update_by_file_with_http_info(self, body, file_id, **kwargs):  # noqa: E501
        """Update By File  # noqa: E501

        Performs a Tm update against the translation memories associated with the specified file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.translation_memory_update_by_file_with_http_info(body, file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TmUpdateParams body: The update parameters. (required)
        :param str file_id: The file identifier. (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'file_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method translation_memory_update_by_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `translation_memory_update_by_file`")  # noqa: E501
        # verify the required parameter 'file_id' is set
        if ('file_id' not in params or
                params['file_id'] is None):
            raise ValueError("Missing the required parameter `file_id` when calling `translation_memory_update_by_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'file_id' in params:
            path_params['fileId'] = params['file_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/tm/update/file/{fileId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def translation_memory_update_by_project_option(self, body, project_options_id, **kwargs):  # noqa: E501
        """Update By Project Option  # noqa: E501

        Performs a Tm update against the translation memories associated with the specified project option.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.translation_memory_update_by_project_option(body, project_options_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TmUpdateParams body: The update parameters. (required)
        :param str project_options_id: The project options identifier. (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.translation_memory_update_by_project_option_with_http_info(body, project_options_id, **kwargs)  # noqa: E501
        else:
            (data) = self.translation_memory_update_by_project_option_with_http_info(body, project_options_id, **kwargs)  # noqa: E501
            return data

    def translation_memory_update_by_project_option_with_http_info(self, body, project_options_id, **kwargs):  # noqa: E501
        """Update By Project Option  # noqa: E501

        Performs a Tm update against the translation memories associated with the specified project option.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.translation_memory_update_by_project_option_with_http_info(body, project_options_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TmUpdateParams body: The update parameters. (required)
        :param str project_options_id: The project options identifier. (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'project_options_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method translation_memory_update_by_project_option" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `translation_memory_update_by_project_option`")  # noqa: E501
        # verify the required parameter 'project_options_id' is set
        if ('project_options_id' not in params or
                params['project_options_id'] is None):
            raise ValueError("Missing the required parameter `project_options_id` when calling `translation_memory_update_by_project_option`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_options_id' in params:
            path_params['projectOptionsId'] = params['project_options_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/tm/update/{projectOptionsId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
