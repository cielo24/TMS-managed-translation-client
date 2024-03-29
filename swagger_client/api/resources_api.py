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


class ResourcesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def resources_java_script_strings(self, lang, version, userid, **kwargs):  # noqa: E501
        """Java Script Strings  # noqa: E501

        Generates client side localized text as a JSON object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resources_java_script_strings(lang, version, userid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str lang: The language. (required)
        :param int version: The version - an unused parameter that enables cache busting. (required)
        :param str userid: The current user identifier - an optional, unused parameter that enables cache busting after authentication, when text substitution may be required. (required)
        :return: dict(str, str)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.resources_java_script_strings_with_http_info(lang, version, userid, **kwargs)  # noqa: E501
        else:
            (data) = self.resources_java_script_strings_with_http_info(lang, version, userid, **kwargs)  # noqa: E501
            return data

    def resources_java_script_strings_with_http_info(self, lang, version, userid, **kwargs):  # noqa: E501
        """Java Script Strings  # noqa: E501

        Generates client side localized text as a JSON object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resources_java_script_strings_with_http_info(lang, version, userid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str lang: The language. (required)
        :param int version: The version - an unused parameter that enables cache busting. (required)
        :param str userid: The current user identifier - an optional, unused parameter that enables cache busting after authentication, when text substitution may be required. (required)
        :return: dict(str, str)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lang', 'version', 'userid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resources_java_script_strings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'lang' is set
        if self.api_client.client_side_validation and ('lang' not in params or
                                                       params['lang'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `lang` when calling `resources_java_script_strings`")  # noqa: E501
        # verify the required parameter 'version' is set
        if self.api_client.client_side_validation and ('version' not in params or
                                                       params['version'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `version` when calling `resources_java_script_strings`")  # noqa: E501
        # verify the required parameter 'userid' is set
        if self.api_client.client_side_validation and ('userid' not in params or
                                                       params['userid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `userid` when calling `resources_java_script_strings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'lang' in params:
            path_params['lang'] = params['lang']  # noqa: E501
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501
        if 'userid' in params:
            path_params['userid'] = params['userid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/resources/strings/{lang}/{version}/{userid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, str)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resources_ui_languages(self, **kwargs):  # noqa: E501
        """Ui Languages  # noqa: E501

        Gets the languages supported by the UI and API.  <br/>_This method does not require you to supply an authentication token._  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resources_ui_languages(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[UiLanguage]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.resources_ui_languages_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resources_ui_languages_with_http_info(**kwargs)  # noqa: E501
            return data

    def resources_ui_languages_with_http_info(self, **kwargs):  # noqa: E501
        """Ui Languages  # noqa: E501

        Gets the languages supported by the UI and API.  <br/>_This method does not require you to supply an authentication token._  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resources_ui_languages_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[UiLanguage]
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
                    " to method resources_ui_languages" % key
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/resources/uilanguages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[UiLanguage]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resources_version(self, **kwargs):  # noqa: E501
        """Version  # noqa: E501

        Gets the current version of the application. This value can be used in query-strings to enable version specific cache busting.  <br/>_This method does not require you to supply an authentication token._  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resources_version(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.resources_version_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resources_version_with_http_info(**kwargs)  # noqa: E501
            return data

    def resources_version_with_http_info(self, **kwargs):  # noqa: E501
        """Version  # noqa: E501

        Gets the current version of the application. This value can be used in query-strings to enable version specific cache busting.  <br/>_This method does not require you to supply an authentication token._  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resources_version_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: int
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
                    " to method resources_version" % key
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/resources/version', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
