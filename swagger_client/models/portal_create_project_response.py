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

from swagger_client.configuration import Configuration


class PortalCreateProjectResponse(object):
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
        'expect_extended_preparation_time': 'bool',
        'is_users_first_project': 'bool',
        'project_id': 'str',
        'result': 'str'
    }

    attribute_map = {
        'expect_extended_preparation_time': 'ExpectExtendedPreparationTime',
        'is_users_first_project': 'IsUsersFirstProject',
        'project_id': 'ProjectId',
        'result': 'Result'
    }

    def __init__(self, expect_extended_preparation_time=None, is_users_first_project=None, project_id=None, result=None, _configuration=None):  # noqa: E501
        """PortalCreateProjectResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._expect_extended_preparation_time = None
        self._is_users_first_project = None
        self._project_id = None
        self._result = None
        self.discriminator = None

        if expect_extended_preparation_time is not None:
            self.expect_extended_preparation_time = expect_extended_preparation_time
        if is_users_first_project is not None:
            self.is_users_first_project = is_users_first_project
        if project_id is not None:
            self.project_id = project_id
        if result is not None:
            self.result = result

    @property
    def expect_extended_preparation_time(self):
        """Gets the expect_extended_preparation_time of this PortalCreateProjectResponse.  # noqa: E501

        Gets or sets a value indicating whether to expect extended preparation time.  # noqa: E501

        :return: The expect_extended_preparation_time of this PortalCreateProjectResponse.  # noqa: E501
        :rtype: bool
        """
        return self._expect_extended_preparation_time

    @expect_extended_preparation_time.setter
    def expect_extended_preparation_time(self, expect_extended_preparation_time):
        """Sets the expect_extended_preparation_time of this PortalCreateProjectResponse.

        Gets or sets a value indicating whether to expect extended preparation time.  # noqa: E501

        :param expect_extended_preparation_time: The expect_extended_preparation_time of this PortalCreateProjectResponse.  # noqa: E501
        :type: bool
        """

        self._expect_extended_preparation_time = expect_extended_preparation_time

    @property
    def is_users_first_project(self):
        """Gets the is_users_first_project of this PortalCreateProjectResponse.  # noqa: E501

        Gets or sets a value indicating whether this is the user's first project.  # noqa: E501

        :return: The is_users_first_project of this PortalCreateProjectResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_users_first_project

    @is_users_first_project.setter
    def is_users_first_project(self, is_users_first_project):
        """Sets the is_users_first_project of this PortalCreateProjectResponse.

        Gets or sets a value indicating whether this is the user's first project.  # noqa: E501

        :param is_users_first_project: The is_users_first_project of this PortalCreateProjectResponse.  # noqa: E501
        :type: bool
        """

        self._is_users_first_project = is_users_first_project

    @property
    def project_id(self):
        """Gets the project_id of this PortalCreateProjectResponse.  # noqa: E501

        Gets or sets the project identifier.  # noqa: E501

        :return: The project_id of this PortalCreateProjectResponse.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PortalCreateProjectResponse.

        Gets or sets the project identifier.  # noqa: E501

        :param project_id: The project_id of this PortalCreateProjectResponse.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def result(self):
        """Gets the result of this PortalCreateProjectResponse.  # noqa: E501

        Gets or sets the result.0 = Success, 1 = SuccessFilesToBeDownloadedSeparately, 2 = Failure, 3 = ValidationFailed, 4 = ActiveProjectsQuotaReached, 5 = ProjectTargetLanguagesQuotaReached, 6 = ProjectCreationQuotaReached, 7 = ProjectCreationAccepted  # noqa: E501

        :return: The result of this PortalCreateProjectResponse.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this PortalCreateProjectResponse.

        Gets or sets the result.0 = Success, 1 = SuccessFilesToBeDownloadedSeparately, 2 = Failure, 3 = ValidationFailed, 4 = ActiveProjectsQuotaReached, 5 = ProjectTargetLanguagesQuotaReached, 6 = ProjectCreationQuotaReached, 7 = ProjectCreationAccepted  # noqa: E501

        :param result: The result of this PortalCreateProjectResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Success", "SuccessFilesToBeDownloadedSeparately", "Failure", "ValidationFailed", "ActiveProjectsQuotaReached", "ProjectTargetLanguagesQuotaReached", "ProjectCreationQuotaReached", "ProjectCreationAccepted"]  # noqa: E501
        if (self._configuration.client_side_validation and
                result not in allowed_values):
            raise ValueError(
                "Invalid value for `result` ({0}), must be one of {1}"  # noqa: E501
                .format(result, allowed_values)
            )

        self._result = result

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
        if issubclass(PortalCreateProjectResponse, dict):
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
        if not isinstance(other, PortalCreateProjectResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortalCreateProjectResponse):
            return True

        return self.to_dict() != other.to_dict()
