# coding: utf-8

"""
    Managed Translation API

    # Getting Started with the Managed Translation API  A good way of getting started with the Managed Translation API is to follow a project throughout its entire life cycle, from its creation to its completion.    ## Step 1: Authenticate with the API  Obtaining an access token is the main prerequisite for all the requests that you can make to the Managed Translation API. The most common way of obtaining such a token is through the Login endpoint. The Managed Translation API handles authentication requests using the OAuth 2.0 Authorization Framework.  1. Log in to Managed Translation and create an application for your integration. This will give you a client ID and a secret.  2. Use the client ID, the secret, and your Managed Translation credentials to make a `POST` request to the Login endpoint [`/auth/token`](#operation/Authentication_Login).    Select the `application/x-www-form-urlencoded` content type when you make this request. The value of the `access_token` parameter in the response is your access token. Use this token in the header of all the requests you will make afterwards.    ## Step 2: Create a project  Before you can create a project, you need to find out what options are available to you and to upload the files that need to be translated. Project creation options are particularly useful for selecting the language pair of your project and for knowing what types of files you can upload.  1. Make a `GET` request to the [`/projects/options`](#operation/Projects_GetProjectCreationOptions) endpoint.       Decide on the most appropriate option for the project you want to create and make sure you remember its `Id`, which is included in the response. You will need to specify this `Id` both when uploading files and when creating the project.  2. Upload the files that need to be translated by making a `POST` request to the [`/files/{projectOptionsId}`](#operation/Files_Upload) endpoint.       When you upload the files, Managed Translation analyzes them and provides detailed information about them in the response. For example, whether or not they are translatable.  3. Create the project by making a `POST` request to the [`/projects`](#operation/Projects_Create) endpoint.       Make sure that you remember the value of the `ProjectId` parameter in the response. You will need it for tracking, approving, and completing your project.    ## Step 3: Track your project  After you create a project, you can track it by making requests to endpoints such as the following:    | Request type | Endpoint | Description |  |-------------|:-------------|-------------|  | `GET`| [`/projects/{projectId}`](#operation/Projects_GetProject) | Get information about a specific project based on the `ProjectId`. |  | `GET`| [`/projects`](#operation/Projects_GetProjects) | Get information all the projects in the system. |  | `GET`| [`/projects/status/{status}`](#operation/Projects_GetProjectsAtStatus) | Get information about all the projects having a certain status. |  | `POST`| [`/projects/fetch`](#operation/Projects_FetchProjects) | Get information about multiple projects of your choice in one request. |    ## Step 4: Approve the project and download the translated files  When the response to a tracking request shows that your project has the `ForApproval` status, approve the project by making a `POST` request to the [`/projects/{projectId}`](#operation/Projects_Approve) endpoint, and then keep tracking your project until one or all of its files has the `ForDownload` status. At that point, download the translated files by making a `GET` request to the [`/files/{projectId}/{fileId}`](#operation/Files_GetTranslatedFile) endpoint (to download one translated file at a time) or to the [`/projects/{projectId}/zip`](#operation/Projects_GetProjectZip) endpoint (to download all the translated files in the project as a .zip archive).    ## Step 5: Mark the files as completed  After your files have been translated and you downloaded them, make a `DELETE` request to the [`/projects/{projectId}/{fileId}`](#operation/Projects_CancelOrComplete) endpoint. This request performs two different actions depending on the status of the files that you specify as parameters:  * If the status is `ForApproval`, Managed Translation cancels the files.  * If the status is `ForDownload`, Managed Translation completes the files.    If the files have any other status, the request is invalid.    # Rate limits  Applications can make a limited number of API requests per minute and per hour. These limits protect against abuse and against runaway applications. They are applied per application, per user, and per API endpoint or path. This means, for example, that you can make 200 project-specific status requests within a minute, but requesting a full list of projects is limited to 100 requests per minute.    | Time frame | Maximum requests |  |:-------------|:-------------|  | Per minute| 100 |  | Per hour| 1500 |    If your application regularly and legitimately exceeds this limits and receives 409 responses, please contact us.  # noqa: E501

    OpenAPI spec version: v1
    Contact: connectors@sdl.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PortalScopeOption(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'can_create_projects': 'bool',
        'default_scope_option': 'bool',
        'deleted': 'bool',
        'disabled': 'bool',
        'lc_meta_data': 'list[KeyValuePairStringString]',
        'location': 'str',
        'scope_id': 'str',
        'scope_name': 'str',
        'scope_options': 'list[PortalScopeOption]'
    }

    attribute_map = {
        'can_create_projects': 'CanCreateProjects',
        'default_scope_option': 'DefaultScopeOption',
        'deleted': 'Deleted',
        'disabled': 'Disabled',
        'lc_meta_data': 'LcMetaData',
        'location': 'Location',
        'scope_id': 'ScopeId',
        'scope_name': 'ScopeName',
        'scope_options': 'ScopeOptions'
    }

    def __init__(self, can_create_projects=None, default_scope_option=None, deleted=None, disabled=None, lc_meta_data=None, location=None, scope_id=None, scope_name=None, scope_options=None):  # noqa: E501
        """PortalScopeOption - a model defined in Swagger"""  # noqa: E501
        self._can_create_projects = None
        self._default_scope_option = None
        self._deleted = None
        self._disabled = None
        self._lc_meta_data = None
        self._location = None
        self._scope_id = None
        self._scope_name = None
        self._scope_options = None
        self.discriminator = None
        if can_create_projects is not None:
            self.can_create_projects = can_create_projects
        if default_scope_option is not None:
            self.default_scope_option = default_scope_option
        if deleted is not None:
            self.deleted = deleted
        if disabled is not None:
            self.disabled = disabled
        if lc_meta_data is not None:
            self.lc_meta_data = lc_meta_data
        if location is not None:
            self.location = location
        if scope_id is not None:
            self.scope_id = scope_id
        if scope_name is not None:
            self.scope_name = scope_name
        if scope_options is not None:
            self.scope_options = scope_options

    @property
    def can_create_projects(self):
        """Gets the can_create_projects of this PortalScopeOption.  # noqa: E501

        If its true then the current user can create projects in the folder  # noqa: E501

        :return: The can_create_projects of this PortalScopeOption.  # noqa: E501
        :rtype: bool
        """
        return self._can_create_projects

    @can_create_projects.setter
    def can_create_projects(self, can_create_projects):
        """Sets the can_create_projects of this PortalScopeOption.

        If its true then the current user can create projects in the folder  # noqa: E501

        :param can_create_projects: The can_create_projects of this PortalScopeOption.  # noqa: E501
        :type: bool
        """

        self._can_create_projects = can_create_projects

    @property
    def default_scope_option(self):
        """Gets the default_scope_option of this PortalScopeOption.  # noqa: E501

        If its true then the current scope is the default scope/folder.  # noqa: E501

        :return: The default_scope_option of this PortalScopeOption.  # noqa: E501
        :rtype: bool
        """
        return self._default_scope_option

    @default_scope_option.setter
    def default_scope_option(self, default_scope_option):
        """Sets the default_scope_option of this PortalScopeOption.

        If its true then the current scope is the default scope/folder.  # noqa: E501

        :param default_scope_option: The default_scope_option of this PortalScopeOption.  # noqa: E501
        :type: bool
        """

        self._default_scope_option = default_scope_option

    @property
    def deleted(self):
        """Gets the deleted of this PortalScopeOption.  # noqa: E501

        If its true then the current user should not see this organisation in the tree  # noqa: E501

        :return: The deleted of this PortalScopeOption.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this PortalScopeOption.

        If its true then the current user should not see this organisation in the tree  # noqa: E501

        :param deleted: The deleted of this PortalScopeOption.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def disabled(self):
        """Gets the disabled of this PortalScopeOption.  # noqa: E501

        If its true then the current user doesn't have rights to create jobs on this organization  # noqa: E501

        :return: The disabled of this PortalScopeOption.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this PortalScopeOption.

        If its true then the current user doesn't have rights to create jobs on this organization  # noqa: E501

        :param disabled: The disabled of this PortalScopeOption.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def lc_meta_data(self):
        """Gets the lc_meta_data of this PortalScopeOption.  # noqa: E501

        Gets or sets the organization Language Cloud related meta data.  # noqa: E501

        :return: The lc_meta_data of this PortalScopeOption.  # noqa: E501
        :rtype: list[KeyValuePairStringString]
        """
        return self._lc_meta_data

    @lc_meta_data.setter
    def lc_meta_data(self, lc_meta_data):
        """Sets the lc_meta_data of this PortalScopeOption.

        Gets or sets the organization Language Cloud related meta data.  # noqa: E501

        :param lc_meta_data: The lc_meta_data of this PortalScopeOption.  # noqa: E501
        :type: list[KeyValuePairStringString]
        """

        self._lc_meta_data = lc_meta_data

    @property
    def location(self):
        """Gets the location of this PortalScopeOption.  # noqa: E501

        Gets the location.  # noqa: E501

        :return: The location of this PortalScopeOption.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this PortalScopeOption.

        Gets the location.  # noqa: E501

        :param location: The location of this PortalScopeOption.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def scope_id(self):
        """Gets the scope_id of this PortalScopeOption.  # noqa: E501

        Gets or sets the scope identifier.  # noqa: E501

        :return: The scope_id of this PortalScopeOption.  # noqa: E501
        :rtype: str
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        """Sets the scope_id of this PortalScopeOption.

        Gets or sets the scope identifier.  # noqa: E501

        :param scope_id: The scope_id of this PortalScopeOption.  # noqa: E501
        :type: str
        """

        self._scope_id = scope_id

    @property
    def scope_name(self):
        """Gets the scope_name of this PortalScopeOption.  # noqa: E501

        Gets or sets the name of the scope.  # noqa: E501

        :return: The scope_name of this PortalScopeOption.  # noqa: E501
        :rtype: str
        """
        return self._scope_name

    @scope_name.setter
    def scope_name(self, scope_name):
        """Sets the scope_name of this PortalScopeOption.

        Gets or sets the name of the scope.  # noqa: E501

        :param scope_name: The scope_name of this PortalScopeOption.  # noqa: E501
        :type: str
        """

        self._scope_name = scope_name

    @property
    def scope_options(self):
        """Gets the scope_options of this PortalScopeOption.  # noqa: E501

        Gets or sets the scope options.  # noqa: E501

        :return: The scope_options of this PortalScopeOption.  # noqa: E501
        :rtype: list[PortalScopeOption]
        """
        return self._scope_options

    @scope_options.setter
    def scope_options(self, scope_options):
        """Sets the scope_options of this PortalScopeOption.

        Gets or sets the scope options.  # noqa: E501

        :param scope_options: The scope_options of this PortalScopeOption.  # noqa: E501
        :type: list[PortalScopeOption]
        """

        self._scope_options = scope_options

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PortalScopeOption, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PortalScopeOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
