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


class AuthenticationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def authentication_login(self, grant_type, client_id, client_secret, username, password, implementation, **kwargs):  # noqa: E501
        """Login  # noqa: E501

        Generates an access token for use with subsequent API calls using the OAuth2 Resource Owner Password Credentials Grant flow.  <br/> In order to generate an access token which can be supplied with each subsequent API call, a user must provide five values to this method, in the form of an <code>application/x-www-form-urlencoded</code> submission. The value supplied for <code>grant_type</code> must be <code>password</code>. <br/> Subsequent API requests must supply an HTTP <code>Authorization</code> header, with a value of <code>token_type access_token</code> where the values are taken from the token supplied in response to this API call. <br/>For more details see <code>https://tools.ietf.org/html/rfc6749#section-4.3</code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_login(grant_type, client_id, client_secret, username, password, implementation, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str grant_type: The grant_type - must be \"password\". (required)
        :param str client_id: The client_id assigned to your application. (required)
        :param str client_secret: The client_secret assigned to your application. (required)
        :param str username: The username. (required)
        :param str password: The password. (required)
        :param str implementation: [Optional] The name of the backend implementation against which authentication should occur, if the supplied credentials are appropriate for use with more than one implementation. Unless told otherwise, you should probably omit this. (required)
        :return: TokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authentication_login_with_http_info(grant_type, client_id, client_secret, username, password, implementation, **kwargs)  # noqa: E501
        else:
            (data) = self.authentication_login_with_http_info(grant_type, client_id, client_secret, username, password, implementation, **kwargs)  # noqa: E501
            return data

    def authentication_login_with_http_info(self, grant_type, client_id, client_secret, username, password, implementation, **kwargs):  # noqa: E501
        """Login  # noqa: E501

        Generates an access token for use with subsequent API calls using the OAuth2 Resource Owner Password Credentials Grant flow.  <br/> In order to generate an access token which can be supplied with each subsequent API call, a user must provide five values to this method, in the form of an <code>application/x-www-form-urlencoded</code> submission. The value supplied for <code>grant_type</code> must be <code>password</code>. <br/> Subsequent API requests must supply an HTTP <code>Authorization</code> header, with a value of <code>token_type access_token</code> where the values are taken from the token supplied in response to this API call. <br/>For more details see <code>https://tools.ietf.org/html/rfc6749#section-4.3</code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_login_with_http_info(grant_type, client_id, client_secret, username, password, implementation, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str grant_type: The grant_type - must be \"password\". (required)
        :param str client_id: The client_id assigned to your application. (required)
        :param str client_secret: The client_secret assigned to your application. (required)
        :param str username: The username. (required)
        :param str password: The password. (required)
        :param str implementation: [Optional] The name of the backend implementation against which authentication should occur, if the supplied credentials are appropriate for use with more than one implementation. Unless told otherwise, you should probably omit this. (required)
        :return: TokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['grant_type', 'client_id', 'client_secret', 'username', 'password', 'implementation']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authentication_login" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'grant_type' is set
        if self.api_client.client_side_validation and ('grant_type' not in params or
                                                       params['grant_type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `grant_type` when calling `authentication_login`")  # noqa: E501
        # verify the required parameter 'client_id' is set
        if self.api_client.client_side_validation and ('client_id' not in params or
                                                       params['client_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `client_id` when calling `authentication_login`")  # noqa: E501
        # verify the required parameter 'client_secret' is set
        if self.api_client.client_side_validation and ('client_secret' not in params or
                                                       params['client_secret'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `client_secret` when calling `authentication_login`")  # noqa: E501
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `authentication_login`")  # noqa: E501
        # verify the required parameter 'password' is set
        if self.api_client.client_side_validation and ('password' not in params or
                                                       params['password'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `password` when calling `authentication_login`")  # noqa: E501
        # verify the required parameter 'implementation' is set
        if self.api_client.client_side_validation and ('implementation' not in params or
                                                       params['implementation'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `implementation` when calling `authentication_login`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'grant_type' in params:
            form_params.append(('grant_type', params['grant_type']))  # noqa: E501
        if 'client_id' in params:
            form_params.append(('client_id', params['client_id']))  # noqa: E501
        if 'client_secret' in params:
            form_params.append(('client_secret', params['client_secret']))  # noqa: E501
        if 'username' in params:
            form_params.append(('username', params['username']))  # noqa: E501
        if 'password' in params:
            form_params.append(('password', params['password']))  # noqa: E501
        if 'implementation' in params:
            form_params.append(('implementation', params['implementation']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/auth/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def authentication_refresh_token(self, grant_type, client_id, client_secret, refresh_token, **kwargs):  # noqa: E501
        """Refresh Token  # noqa: E501

        Regenerates an access token from the supplied refresh token.  <br/> In order to regenerate an access token which can be supplied with each subsequent API call, a user must provide four values to this method, in the form of an <code>application/x-www-form-urlencoded</code> submission. The value supplied for <code>grant_type</code> must be <code>refresh_token</code>. <br/> Subsequent API requests must supply an HTTP <code>Authorization</code> header, with a value of <code>token_type access_token</code> where the values are taken from the token supplied in response to this API call. <br/>For more details see <code>https://tools.ietf.org/html/rfc6749#section-6</code><br/>The same result can be obtained by submitting the request to the <code>/token</code> endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_refresh_token(grant_type, client_id, client_secret, refresh_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str grant_type: The grant_type - must be \"refresh_token\". (required)
        :param str client_id: The client_id assigned to your application. (required)
        :param str client_secret: The client_secret assigned to your application. (required)
        :param str refresh_token: The refresh token supplied from a previous call to /token or /token/refresh. (required)
        :return: TokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authentication_refresh_token_with_http_info(grant_type, client_id, client_secret, refresh_token, **kwargs)  # noqa: E501
        else:
            (data) = self.authentication_refresh_token_with_http_info(grant_type, client_id, client_secret, refresh_token, **kwargs)  # noqa: E501
            return data

    def authentication_refresh_token_with_http_info(self, grant_type, client_id, client_secret, refresh_token, **kwargs):  # noqa: E501
        """Refresh Token  # noqa: E501

        Regenerates an access token from the supplied refresh token.  <br/> In order to regenerate an access token which can be supplied with each subsequent API call, a user must provide four values to this method, in the form of an <code>application/x-www-form-urlencoded</code> submission. The value supplied for <code>grant_type</code> must be <code>refresh_token</code>. <br/> Subsequent API requests must supply an HTTP <code>Authorization</code> header, with a value of <code>token_type access_token</code> where the values are taken from the token supplied in response to this API call. <br/>For more details see <code>https://tools.ietf.org/html/rfc6749#section-6</code><br/>The same result can be obtained by submitting the request to the <code>/token</code> endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_refresh_token_with_http_info(grant_type, client_id, client_secret, refresh_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str grant_type: The grant_type - must be \"refresh_token\". (required)
        :param str client_id: The client_id assigned to your application. (required)
        :param str client_secret: The client_secret assigned to your application. (required)
        :param str refresh_token: The refresh token supplied from a previous call to /token or /token/refresh. (required)
        :return: TokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['grant_type', 'client_id', 'client_secret', 'refresh_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authentication_refresh_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'grant_type' is set
        if self.api_client.client_side_validation and ('grant_type' not in params or
                                                       params['grant_type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `grant_type` when calling `authentication_refresh_token`")  # noqa: E501
        # verify the required parameter 'client_id' is set
        if self.api_client.client_side_validation and ('client_id' not in params or
                                                       params['client_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `client_id` when calling `authentication_refresh_token`")  # noqa: E501
        # verify the required parameter 'client_secret' is set
        if self.api_client.client_side_validation and ('client_secret' not in params or
                                                       params['client_secret'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `client_secret` when calling `authentication_refresh_token`")  # noqa: E501
        # verify the required parameter 'refresh_token' is set
        if self.api_client.client_side_validation and ('refresh_token' not in params or
                                                       params['refresh_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `refresh_token` when calling `authentication_refresh_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'grant_type' in params:
            form_params.append(('grant_type', params['grant_type']))  # noqa: E501
        if 'client_id' in params:
            form_params.append(('client_id', params['client_id']))  # noqa: E501
        if 'client_secret' in params:
            form_params.append(('client_secret', params['client_secret']))  # noqa: E501
        if 'refresh_token' in params:
            form_params.append(('refresh_token', params['refresh_token']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tm4lc/api/v1/auth/token/refresh', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
