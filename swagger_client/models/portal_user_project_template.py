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

class PortalUserProjectTemplate(object):
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
        'id': 'str',
        'metadata': 'list[dict(str, str)]',
        'name': 'str',
        'organization': 'str',
        'project_group': 'str',
        'project_option': 'str',
        'source_language': 'str',
        'target_languages': 'list[str]',
        'tm_sequence': 'str',
        'vendors': 'list[str]'
    }

    attribute_map = {
        'id': 'Id',
        'metadata': 'Metadata',
        'name': 'Name',
        'organization': 'Organization',
        'project_group': 'ProjectGroup',
        'project_option': 'ProjectOption',
        'source_language': 'SourceLanguage',
        'target_languages': 'TargetLanguages',
        'tm_sequence': 'TmSequence',
        'vendors': 'Vendors'
    }

    def __init__(self, id=None, metadata=None, name=None, organization=None, project_group=None, project_option=None, source_language=None, target_languages=None, tm_sequence=None, vendors=None):  # noqa: E501
        """PortalUserProjectTemplate - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._metadata = None
        self._name = None
        self._organization = None
        self._project_group = None
        self._project_option = None
        self._source_language = None
        self._target_languages = None
        self._tm_sequence = None
        self._vendors = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if organization is not None:
            self.organization = organization
        if project_group is not None:
            self.project_group = project_group
        if project_option is not None:
            self.project_option = project_option
        if source_language is not None:
            self.source_language = source_language
        if target_languages is not None:
            self.target_languages = target_languages
        if tm_sequence is not None:
            self.tm_sequence = tm_sequence
        if vendors is not None:
            self.vendors = vendors

    @property
    def id(self):
        """Gets the id of this PortalUserProjectTemplate.  # noqa: E501

        The identifier of the project template  # noqa: E501

        :return: The id of this PortalUserProjectTemplate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PortalUserProjectTemplate.

        The identifier of the project template  # noqa: E501

        :param id: The id of this PortalUserProjectTemplate.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def metadata(self):
        """Gets the metadata of this PortalUserProjectTemplate.  # noqa: E501

        Metadata values  # noqa: E501

        :return: The metadata of this PortalUserProjectTemplate.  # noqa: E501
        :rtype: list[dict(str, str)]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PortalUserProjectTemplate.

        Metadata values  # noqa: E501

        :param metadata: The metadata of this PortalUserProjectTemplate.  # noqa: E501
        :type: list[dict(str, str)]
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this PortalUserProjectTemplate.  # noqa: E501

        The name of the project template  # noqa: E501

        :return: The name of this PortalUserProjectTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PortalUserProjectTemplate.

        The name of the project template  # noqa: E501

        :param name: The name of this PortalUserProjectTemplate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def organization(self):
        """Gets the organization of this PortalUserProjectTemplate.  # noqa: E501

        Organization identifier  # noqa: E501

        :return: The organization of this PortalUserProjectTemplate.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this PortalUserProjectTemplate.

        Organization identifier  # noqa: E501

        :param organization: The organization of this PortalUserProjectTemplate.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def project_group(self):
        """Gets the project_group of this PortalUserProjectTemplate.  # noqa: E501

        Project group identifier  # noqa: E501

        :return: The project_group of this PortalUserProjectTemplate.  # noqa: E501
        :rtype: str
        """
        return self._project_group

    @project_group.setter
    def project_group(self, project_group):
        """Sets the project_group of this PortalUserProjectTemplate.

        Project group identifier  # noqa: E501

        :param project_group: The project_group of this PortalUserProjectTemplate.  # noqa: E501
        :type: str
        """

        self._project_group = project_group

    @property
    def project_option(self):
        """Gets the project_option of this PortalUserProjectTemplate.  # noqa: E501

        Project option identifier  # noqa: E501

        :return: The project_option of this PortalUserProjectTemplate.  # noqa: E501
        :rtype: str
        """
        return self._project_option

    @project_option.setter
    def project_option(self, project_option):
        """Sets the project_option of this PortalUserProjectTemplate.

        Project option identifier  # noqa: E501

        :param project_option: The project_option of this PortalUserProjectTemplate.  # noqa: E501
        :type: str
        """

        self._project_option = project_option

    @property
    def source_language(self):
        """Gets the source_language of this PortalUserProjectTemplate.  # noqa: E501

        Source language  # noqa: E501

        :return: The source_language of this PortalUserProjectTemplate.  # noqa: E501
        :rtype: str
        """
        return self._source_language

    @source_language.setter
    def source_language(self, source_language):
        """Sets the source_language of this PortalUserProjectTemplate.

        Source language  # noqa: E501

        :param source_language: The source_language of this PortalUserProjectTemplate.  # noqa: E501
        :type: str
        """

        self._source_language = source_language

    @property
    def target_languages(self):
        """Gets the target_languages of this PortalUserProjectTemplate.  # noqa: E501

        List of selected target languages  # noqa: E501

        :return: The target_languages of this PortalUserProjectTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_languages

    @target_languages.setter
    def target_languages(self, target_languages):
        """Sets the target_languages of this PortalUserProjectTemplate.

        List of selected target languages  # noqa: E501

        :param target_languages: The target_languages of this PortalUserProjectTemplate.  # noqa: E501
        :type: list[str]
        """

        self._target_languages = target_languages

    @property
    def tm_sequence(self):
        """Gets the tm_sequence of this PortalUserProjectTemplate.  # noqa: E501

        Selected TmSequence identifier  # noqa: E501

        :return: The tm_sequence of this PortalUserProjectTemplate.  # noqa: E501
        :rtype: str
        """
        return self._tm_sequence

    @tm_sequence.setter
    def tm_sequence(self, tm_sequence):
        """Sets the tm_sequence of this PortalUserProjectTemplate.

        Selected TmSequence identifier  # noqa: E501

        :param tm_sequence: The tm_sequence of this PortalUserProjectTemplate.  # noqa: E501
        :type: str
        """

        self._tm_sequence = tm_sequence

    @property
    def vendors(self):
        """Gets the vendors of this PortalUserProjectTemplate.  # noqa: E501

        List of vendor identifiers  # noqa: E501

        :return: The vendors of this PortalUserProjectTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._vendors

    @vendors.setter
    def vendors(self, vendors):
        """Sets the vendors of this PortalUserProjectTemplate.

        List of vendor identifiers  # noqa: E501

        :param vendors: The vendors of this PortalUserProjectTemplate.  # noqa: E501
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
        if issubclass(PortalUserProjectTemplate, dict):
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
        if not isinstance(other, PortalUserProjectTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
