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


class PortalProjectParams(object):
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
        'description': 'str',
        'due_date': 'datetime',
        'files': 'list[ProjectFile]',
        'metadata': 'list[ProjectMetadata]',
        'name': 'str',
        'project_group_id': 'str',
        'project_options_id': 'str',
        'scope_option_id': 'str',
        'src_lang': 'str',
        'tgt_langs': 'list[str]',
        'tm_sequence_id': 'str',
        'vendors': 'list[str]'
    }

    attribute_map = {
        'description': 'Description',
        'due_date': 'DueDate',
        'files': 'Files',
        'metadata': 'Metadata',
        'name': 'Name',
        'project_group_id': 'ProjectGroupId',
        'project_options_id': 'ProjectOptionsId',
        'scope_option_id': 'ScopeOptionId',
        'src_lang': 'SrcLang',
        'tgt_langs': 'TgtLangs',
        'tm_sequence_id': 'TmSequenceId',
        'vendors': 'Vendors'
    }

    def __init__(self, description=None, due_date=None, files=None, metadata=None, name=None, project_group_id=None, project_options_id=None, scope_option_id=None, src_lang=None, tgt_langs=None, tm_sequence_id=None, vendors=None, _configuration=None):  # noqa: E501
        """PortalProjectParams - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._due_date = None
        self._files = None
        self._metadata = None
        self._name = None
        self._project_group_id = None
        self._project_options_id = None
        self._scope_option_id = None
        self._src_lang = None
        self._tgt_langs = None
        self._tm_sequence_id = None
        self._vendors = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if due_date is not None:
            self.due_date = due_date
        if files is not None:
            self.files = files
        if metadata is not None:
            self.metadata = metadata
        self.name = name
        if project_group_id is not None:
            self.project_group_id = project_group_id
        self.project_options_id = project_options_id
        if scope_option_id is not None:
            self.scope_option_id = scope_option_id
        self.src_lang = src_lang
        if tgt_langs is not None:
            self.tgt_langs = tgt_langs
        if tm_sequence_id is not None:
            self.tm_sequence_id = tm_sequence_id
        if vendors is not None:
            self.vendors = vendors

    @property
    def description(self):
        """Gets the description of this PortalProjectParams.  # noqa: E501

        Gets or sets the description for the project.  # noqa: E501

        :return: The description of this PortalProjectParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PortalProjectParams.

        Gets or sets the description for the project.  # noqa: E501

        :param description: The description of this PortalProjectParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def due_date(self):
        """Gets the due_date of this PortalProjectParams.  # noqa: E501

        Gets or sets the due date.  # noqa: E501

        :return: The due_date of this PortalProjectParams.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this PortalProjectParams.

        Gets or sets the due date.  # noqa: E501

        :param due_date: The due_date of this PortalProjectParams.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def files(self):
        """Gets the files of this PortalProjectParams.  # noqa: E501

        Gets the files to be included in the project.  # noqa: E501

        :return: The files of this PortalProjectParams.  # noqa: E501
        :rtype: list[ProjectFile]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this PortalProjectParams.

        Gets the files to be included in the project.  # noqa: E501

        :param files: The files of this PortalProjectParams.  # noqa: E501
        :type: list[ProjectFile]
        """

        self._files = files

    @property
    def metadata(self):
        """Gets the metadata of this PortalProjectParams.  # noqa: E501

        Gets or sets the metadata.  # noqa: E501

        :return: The metadata of this PortalProjectParams.  # noqa: E501
        :rtype: list[ProjectMetadata]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PortalProjectParams.

        Gets or sets the metadata.  # noqa: E501

        :param metadata: The metadata of this PortalProjectParams.  # noqa: E501
        :type: list[ProjectMetadata]
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this PortalProjectParams.  # noqa: E501

        Gets or sets the name of the project.  # noqa: E501

        :return: The name of this PortalProjectParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PortalProjectParams.

        Gets or sets the name of the project.  # noqa: E501

        :param name: The name of this PortalProjectParams.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def project_group_id(self):
        """Gets the project_group_id of this PortalProjectParams.  # noqa: E501

        Gets or sets the project group uniqueidentifier  # noqa: E501

        :return: The project_group_id of this PortalProjectParams.  # noqa: E501
        :rtype: str
        """
        return self._project_group_id

    @project_group_id.setter
    def project_group_id(self, project_group_id):
        """Sets the project_group_id of this PortalProjectParams.

        Gets or sets the project group uniqueidentifier  # noqa: E501

        :param project_group_id: The project_group_id of this PortalProjectParams.  # noqa: E501
        :type: str
        """

        self._project_group_id = project_group_id

    @property
    def project_options_id(self):
        """Gets the project_options_id of this PortalProjectParams.  # noqa: E501

        Gets or sets the project options identifier.  # noqa: E501

        :return: The project_options_id of this PortalProjectParams.  # noqa: E501
        :rtype: str
        """
        return self._project_options_id

    @project_options_id.setter
    def project_options_id(self, project_options_id):
        """Sets the project_options_id of this PortalProjectParams.

        Gets or sets the project options identifier.  # noqa: E501

        :param project_options_id: The project_options_id of this PortalProjectParams.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and project_options_id is None:
            raise ValueError("Invalid value for `project_options_id`, must not be `None`")  # noqa: E501

        self._project_options_id = project_options_id

    @property
    def scope_option_id(self):
        """Gets the scope_option_id of this PortalProjectParams.  # noqa: E501

        Gets or sets the scope option identifier.  # noqa: E501

        :return: The scope_option_id of this PortalProjectParams.  # noqa: E501
        :rtype: str
        """
        return self._scope_option_id

    @scope_option_id.setter
    def scope_option_id(self, scope_option_id):
        """Sets the scope_option_id of this PortalProjectParams.

        Gets or sets the scope option identifier.  # noqa: E501

        :param scope_option_id: The scope_option_id of this PortalProjectParams.  # noqa: E501
        :type: str
        """

        self._scope_option_id = scope_option_id

    @property
    def src_lang(self):
        """Gets the src_lang of this PortalProjectParams.  # noqa: E501

        Gets or sets the source language for the project.                          A project can support only one source language, therefore we assume that all files within the project contain content             in the specified source language.             The value supplied here should be taken from the             PortalLanguage.CultureCode property.  # noqa: E501

        :return: The src_lang of this PortalProjectParams.  # noqa: E501
        :rtype: str
        """
        return self._src_lang

    @src_lang.setter
    def src_lang(self, src_lang):
        """Sets the src_lang of this PortalProjectParams.

        Gets or sets the source language for the project.                          A project can support only one source language, therefore we assume that all files within the project contain content             in the specified source language.             The value supplied here should be taken from the             PortalLanguage.CultureCode property.  # noqa: E501

        :param src_lang: The src_lang of this PortalProjectParams.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and src_lang is None:
            raise ValueError("Invalid value for `src_lang`, must not be `None`")  # noqa: E501

        self._src_lang = src_lang

    @property
    def tgt_langs(self):
        """Gets the tgt_langs of this PortalProjectParams.  # noqa: E501

        Gets or sets the target languages that apply to the files supplied in .                          The values supplied here should be taken from the             PortalLanguage.CultureCode property.  # noqa: E501

        :return: The tgt_langs of this PortalProjectParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._tgt_langs

    @tgt_langs.setter
    def tgt_langs(self, tgt_langs):
        """Sets the tgt_langs of this PortalProjectParams.

        Gets or sets the target languages that apply to the files supplied in .                          The values supplied here should be taken from the             PortalLanguage.CultureCode property.  # noqa: E501

        :param tgt_langs: The tgt_langs of this PortalProjectParams.  # noqa: E501
        :type: list[str]
        """

        self._tgt_langs = tgt_langs

    @property
    def tm_sequence_id(self):
        """Gets the tm_sequence_id of this PortalProjectParams.  # noqa: E501

        Gets or sets the tm sequence identifier.  # noqa: E501

        :return: The tm_sequence_id of this PortalProjectParams.  # noqa: E501
        :rtype: str
        """
        return self._tm_sequence_id

    @tm_sequence_id.setter
    def tm_sequence_id(self, tm_sequence_id):
        """Sets the tm_sequence_id of this PortalProjectParams.

        Gets or sets the tm sequence identifier.  # noqa: E501

        :param tm_sequence_id: The tm_sequence_id of this PortalProjectParams.  # noqa: E501
        :type: str
        """

        self._tm_sequence_id = tm_sequence_id

    @property
    def vendors(self):
        """Gets the vendors of this PortalProjectParams.  # noqa: E501

        Gets the vendor ids to be associated with this project.  # noqa: E501

        :return: The vendors of this PortalProjectParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._vendors

    @vendors.setter
    def vendors(self, vendors):
        """Sets the vendors of this PortalProjectParams.

        Gets the vendor ids to be associated with this project.  # noqa: E501

        :param vendors: The vendors of this PortalProjectParams.  # noqa: E501
        :type: list[str]
        """

        self._vendors = vendors

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
        if issubclass(PortalProjectParams, dict):
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
        if not isinstance(other, PortalProjectParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortalProjectParams):
            return True

        return self.to_dict() != other.to_dict()
