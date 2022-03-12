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

class PortalProjectOptions(object):
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
        'allow_only_online_access_to_project': 'bool',
        'allow_wildcard_extensions': 'bool',
        'description': 'str',
        'disabled_dates': 'list[datetime]',
        'due_date_minimum': 'int',
        'due_date_offset': 'int',
        'file_types': 'list[PortalFileType]',
        'hide_in_create_job_page': 'bool',
        'id': 'str',
        'language_pairs': 'list[PortalLanguagePair]',
        'metadata': 'list[PortalMetadata]',
        'name': 'str',
        'supports_due_date': 'bool',
        'supports_job_description': 'bool',
        'supports_job_name': 'bool',
        'supports_project_template': 'bool',
        'supports_reference_files': 'bool',
        'tm_sequences': 'list[PortalTmSequence]',
        'vendors': 'list[str]'
    }

    attribute_map = {
        'allow_only_online_access_to_project': 'AllowOnlyOnlineAccessToProject',
        'allow_wildcard_extensions': 'AllowWildcardExtensions',
        'description': 'Description',
        'disabled_dates': 'DisabledDates',
        'due_date_minimum': 'DueDateMinimum',
        'due_date_offset': 'DueDateOffset',
        'file_types': 'FileTypes',
        'hide_in_create_job_page': 'HideInCreateJobPage',
        'id': 'Id',
        'language_pairs': 'LanguagePairs',
        'metadata': 'Metadata',
        'name': 'Name',
        'supports_due_date': 'SupportsDueDate',
        'supports_job_description': 'SupportsJobDescription',
        'supports_job_name': 'SupportsJobName',
        'supports_project_template': 'SupportsProjectTemplate',
        'supports_reference_files': 'SupportsReferenceFiles',
        'tm_sequences': 'TmSequences',
        'vendors': 'Vendors'
    }

    def __init__(self, allow_only_online_access_to_project=None, allow_wildcard_extensions=None, description=None, disabled_dates=None, due_date_minimum=None, due_date_offset=None, file_types=None, hide_in_create_job_page=None, id=None, language_pairs=None, metadata=None, name=None, supports_due_date=None, supports_job_description=None, supports_job_name=None, supports_project_template=None, supports_reference_files=None, tm_sequences=None, vendors=None):  # noqa: E501
        """PortalProjectOptions - a model defined in Swagger"""  # noqa: E501
        self._allow_only_online_access_to_project = None
        self._allow_wildcard_extensions = None
        self._description = None
        self._disabled_dates = None
        self._due_date_minimum = None
        self._due_date_offset = None
        self._file_types = None
        self._hide_in_create_job_page = None
        self._id = None
        self._language_pairs = None
        self._metadata = None
        self._name = None
        self._supports_due_date = None
        self._supports_job_description = None
        self._supports_job_name = None
        self._supports_project_template = None
        self._supports_reference_files = None
        self._tm_sequences = None
        self._vendors = None
        self.discriminator = None
        if allow_only_online_access_to_project is not None:
            self.allow_only_online_access_to_project = allow_only_online_access_to_project
        if allow_wildcard_extensions is not None:
            self.allow_wildcard_extensions = allow_wildcard_extensions
        if description is not None:
            self.description = description
        if disabled_dates is not None:
            self.disabled_dates = disabled_dates
        if due_date_minimum is not None:
            self.due_date_minimum = due_date_minimum
        if due_date_offset is not None:
            self.due_date_offset = due_date_offset
        if file_types is not None:
            self.file_types = file_types
        if hide_in_create_job_page is not None:
            self.hide_in_create_job_page = hide_in_create_job_page
        if id is not None:
            self.id = id
        if language_pairs is not None:
            self.language_pairs = language_pairs
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if supports_due_date is not None:
            self.supports_due_date = supports_due_date
        if supports_job_description is not None:
            self.supports_job_description = supports_job_description
        if supports_job_name is not None:
            self.supports_job_name = supports_job_name
        if supports_project_template is not None:
            self.supports_project_template = supports_project_template
        if supports_reference_files is not None:
            self.supports_reference_files = supports_reference_files
        if tm_sequences is not None:
            self.tm_sequences = tm_sequences
        if vendors is not None:
            self.vendors = vendors

    @property
    def allow_only_online_access_to_project(self):
        """Gets the allow_only_online_access_to_project of this PortalProjectOptions.  # noqa: E501

        Gets or sets a value indicating whether this project option is used for secre projects.  # noqa: E501

        :return: The allow_only_online_access_to_project of this PortalProjectOptions.  # noqa: E501
        :rtype: bool
        """
        return self._allow_only_online_access_to_project

    @allow_only_online_access_to_project.setter
    def allow_only_online_access_to_project(self, allow_only_online_access_to_project):
        """Sets the allow_only_online_access_to_project of this PortalProjectOptions.

        Gets or sets a value indicating whether this project option is used for secre projects.  # noqa: E501

        :param allow_only_online_access_to_project: The allow_only_online_access_to_project of this PortalProjectOptions.  # noqa: E501
        :type: bool
        """

        self._allow_only_online_access_to_project = allow_only_online_access_to_project

    @property
    def allow_wildcard_extensions(self):
        """Gets the allow_wildcard_extensions of this PortalProjectOptions.  # noqa: E501

        Gets or sets a value indicating whether [allow wildcard extensions].  # noqa: E501

        :return: The allow_wildcard_extensions of this PortalProjectOptions.  # noqa: E501
        :rtype: bool
        """
        return self._allow_wildcard_extensions

    @allow_wildcard_extensions.setter
    def allow_wildcard_extensions(self, allow_wildcard_extensions):
        """Sets the allow_wildcard_extensions of this PortalProjectOptions.

        Gets or sets a value indicating whether [allow wildcard extensions].  # noqa: E501

        :param allow_wildcard_extensions: The allow_wildcard_extensions of this PortalProjectOptions.  # noqa: E501
        :type: bool
        """

        self._allow_wildcard_extensions = allow_wildcard_extensions

    @property
    def description(self):
        """Gets the description of this PortalProjectOptions.  # noqa: E501

        Gets or sets the description.  # noqa: E501

        :return: The description of this PortalProjectOptions.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PortalProjectOptions.

        Gets or sets the description.  # noqa: E501

        :param description: The description of this PortalProjectOptions.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def disabled_dates(self):
        """Gets the disabled_dates of this PortalProjectOptions.  # noqa: E501

        Gets the disabled dates.  # noqa: E501

        :return: The disabled_dates of this PortalProjectOptions.  # noqa: E501
        :rtype: list[datetime]
        """
        return self._disabled_dates

    @disabled_dates.setter
    def disabled_dates(self, disabled_dates):
        """Sets the disabled_dates of this PortalProjectOptions.

        Gets the disabled dates.  # noqa: E501

        :param disabled_dates: The disabled_dates of this PortalProjectOptions.  # noqa: E501
        :type: list[datetime]
        """

        self._disabled_dates = disabled_dates

    @property
    def due_date_minimum(self):
        """Gets the due_date_minimum of this PortalProjectOptions.  # noqa: E501

        Gets or sets the due date minimum number of days.  # noqa: E501

        :return: The due_date_minimum of this PortalProjectOptions.  # noqa: E501
        :rtype: int
        """
        return self._due_date_minimum

    @due_date_minimum.setter
    def due_date_minimum(self, due_date_minimum):
        """Sets the due_date_minimum of this PortalProjectOptions.

        Gets or sets the due date minimum number of days.  # noqa: E501

        :param due_date_minimum: The due_date_minimum of this PortalProjectOptions.  # noqa: E501
        :type: int
        """

        self._due_date_minimum = due_date_minimum

    @property
    def due_date_offset(self):
        """Gets the due_date_offset of this PortalProjectOptions.  # noqa: E501

        Gets or sets the due date offset.  # noqa: E501

        :return: The due_date_offset of this PortalProjectOptions.  # noqa: E501
        :rtype: int
        """
        return self._due_date_offset

    @due_date_offset.setter
    def due_date_offset(self, due_date_offset):
        """Sets the due_date_offset of this PortalProjectOptions.

        Gets or sets the due date offset.  # noqa: E501

        :param due_date_offset: The due_date_offset of this PortalProjectOptions.  # noqa: E501
        :type: int
        """

        self._due_date_offset = due_date_offset

    @property
    def file_types(self):
        """Gets the file_types of this PortalProjectOptions.  # noqa: E501

        Gets or sets the file types.  # noqa: E501

        :return: The file_types of this PortalProjectOptions.  # noqa: E501
        :rtype: list[PortalFileType]
        """
        return self._file_types

    @file_types.setter
    def file_types(self, file_types):
        """Sets the file_types of this PortalProjectOptions.

        Gets or sets the file types.  # noqa: E501

        :param file_types: The file_types of this PortalProjectOptions.  # noqa: E501
        :type: list[PortalFileType]
        """

        self._file_types = file_types

    @property
    def hide_in_create_job_page(self):
        """Gets the hide_in_create_job_page of this PortalProjectOptions.  # noqa: E501

        Gets or sets a value indicating whether a project template is hidden in create new job page.  # noqa: E501

        :return: The hide_in_create_job_page of this PortalProjectOptions.  # noqa: E501
        :rtype: bool
        """
        return self._hide_in_create_job_page

    @hide_in_create_job_page.setter
    def hide_in_create_job_page(self, hide_in_create_job_page):
        """Sets the hide_in_create_job_page of this PortalProjectOptions.

        Gets or sets a value indicating whether a project template is hidden in create new job page.  # noqa: E501

        :param hide_in_create_job_page: The hide_in_create_job_page of this PortalProjectOptions.  # noqa: E501
        :type: bool
        """

        self._hide_in_create_job_page = hide_in_create_job_page

    @property
    def id(self):
        """Gets the id of this PortalProjectOptions.  # noqa: E501

        Gets or sets the identifier.  # noqa: E501

        :return: The id of this PortalProjectOptions.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PortalProjectOptions.

        Gets or sets the identifier.  # noqa: E501

        :param id: The id of this PortalProjectOptions.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def language_pairs(self):
        """Gets the language_pairs of this PortalProjectOptions.  # noqa: E501

        Gets or sets the language pairs.  # noqa: E501

        :return: The language_pairs of this PortalProjectOptions.  # noqa: E501
        :rtype: list[PortalLanguagePair]
        """
        return self._language_pairs

    @language_pairs.setter
    def language_pairs(self, language_pairs):
        """Sets the language_pairs of this PortalProjectOptions.

        Gets or sets the language pairs.  # noqa: E501

        :param language_pairs: The language_pairs of this PortalProjectOptions.  # noqa: E501
        :type: list[PortalLanguagePair]
        """

        self._language_pairs = language_pairs

    @property
    def metadata(self):
        """Gets the metadata of this PortalProjectOptions.  # noqa: E501

        Gets or sets the metadata.  # noqa: E501

        :return: The metadata of this PortalProjectOptions.  # noqa: E501
        :rtype: list[PortalMetadata]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PortalProjectOptions.

        Gets or sets the metadata.  # noqa: E501

        :param metadata: The metadata of this PortalProjectOptions.  # noqa: E501
        :type: list[PortalMetadata]
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this PortalProjectOptions.  # noqa: E501

        Gets or sets the name.  # noqa: E501

        :return: The name of this PortalProjectOptions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PortalProjectOptions.

        Gets or sets the name.  # noqa: E501

        :param name: The name of this PortalProjectOptions.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def supports_due_date(self):
        """Gets the supports_due_date of this PortalProjectOptions.  # noqa: E501

        Gets or sets a value indicating whether this PortalProjectOptions supports a due date.  # noqa: E501

        :return: The supports_due_date of this PortalProjectOptions.  # noqa: E501
        :rtype: bool
        """
        return self._supports_due_date

    @supports_due_date.setter
    def supports_due_date(self, supports_due_date):
        """Sets the supports_due_date of this PortalProjectOptions.

        Gets or sets a value indicating whether this PortalProjectOptions supports a due date.  # noqa: E501

        :param supports_due_date: The supports_due_date of this PortalProjectOptions.  # noqa: E501
        :type: bool
        """

        self._supports_due_date = supports_due_date

    @property
    def supports_job_description(self):
        """Gets the supports_job_description of this PortalProjectOptions.  # noqa: E501

        Gets or sets a value indicating whether this PortalProjectOptions supports job description.  # noqa: E501

        :return: The supports_job_description of this PortalProjectOptions.  # noqa: E501
        :rtype: bool
        """
        return self._supports_job_description

    @supports_job_description.setter
    def supports_job_description(self, supports_job_description):
        """Sets the supports_job_description of this PortalProjectOptions.

        Gets or sets a value indicating whether this PortalProjectOptions supports job description.  # noqa: E501

        :param supports_job_description: The supports_job_description of this PortalProjectOptions.  # noqa: E501
        :type: bool
        """

        self._supports_job_description = supports_job_description

    @property
    def supports_job_name(self):
        """Gets the supports_job_name of this PortalProjectOptions.  # noqa: E501

        Gets or sets a value indicating whether this PortalProjectOptions supports job name.  # noqa: E501

        :return: The supports_job_name of this PortalProjectOptions.  # noqa: E501
        :rtype: bool
        """
        return self._supports_job_name

    @supports_job_name.setter
    def supports_job_name(self, supports_job_name):
        """Sets the supports_job_name of this PortalProjectOptions.

        Gets or sets a value indicating whether this PortalProjectOptions supports job name.  # noqa: E501

        :param supports_job_name: The supports_job_name of this PortalProjectOptions.  # noqa: E501
        :type: bool
        """

        self._supports_job_name = supports_job_name

    @property
    def supports_project_template(self):
        """Gets the supports_project_template of this PortalProjectOptions.  # noqa: E501

        Gets or sets a value indicating whether this PortalProjectOptions supports a project template.  # noqa: E501

        :return: The supports_project_template of this PortalProjectOptions.  # noqa: E501
        :rtype: bool
        """
        return self._supports_project_template

    @supports_project_template.setter
    def supports_project_template(self, supports_project_template):
        """Sets the supports_project_template of this PortalProjectOptions.

        Gets or sets a value indicating whether this PortalProjectOptions supports a project template.  # noqa: E501

        :param supports_project_template: The supports_project_template of this PortalProjectOptions.  # noqa: E501
        :type: bool
        """

        self._supports_project_template = supports_project_template

    @property
    def supports_reference_files(self):
        """Gets the supports_reference_files of this PortalProjectOptions.  # noqa: E501

        Gets or sets a value indicating whether this PortalProjectOptions supports reference files.  # noqa: E501

        :return: The supports_reference_files of this PortalProjectOptions.  # noqa: E501
        :rtype: bool
        """
        return self._supports_reference_files

    @supports_reference_files.setter
    def supports_reference_files(self, supports_reference_files):
        """Sets the supports_reference_files of this PortalProjectOptions.

        Gets or sets a value indicating whether this PortalProjectOptions supports reference files.  # noqa: E501

        :param supports_reference_files: The supports_reference_files of this PortalProjectOptions.  # noqa: E501
        :type: bool
        """

        self._supports_reference_files = supports_reference_files

    @property
    def tm_sequences(self):
        """Gets the tm_sequences of this PortalProjectOptions.  # noqa: E501

        Gets the tm sequences.  # noqa: E501

        :return: The tm_sequences of this PortalProjectOptions.  # noqa: E501
        :rtype: list[PortalTmSequence]
        """
        return self._tm_sequences

    @tm_sequences.setter
    def tm_sequences(self, tm_sequences):
        """Sets the tm_sequences of this PortalProjectOptions.

        Gets the tm sequences.  # noqa: E501

        :param tm_sequences: The tm_sequences of this PortalProjectOptions.  # noqa: E501
        :type: list[PortalTmSequence]
        """

        self._tm_sequences = tm_sequences

    @property
    def vendors(self):
        """Gets the vendors of this PortalProjectOptions.  # noqa: E501

        Gets or sets the vendors available for selection with this project option.  # noqa: E501

        :return: The vendors of this PortalProjectOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._vendors

    @vendors.setter
    def vendors(self, vendors):
        """Sets the vendors of this PortalProjectOptions.

        Gets or sets the vendors available for selection with this project option.  # noqa: E501

        :param vendors: The vendors of this PortalProjectOptions.  # noqa: E501
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
        if issubclass(PortalProjectOptions, dict):
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
        if not isinstance(other, PortalProjectOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
