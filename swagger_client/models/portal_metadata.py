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

class PortalMetadata(object):
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
        'control': 'str',
        'default_value': 'str',
        'description': 'str',
        'id': 'str',
        'is_read_only': 'bool',
        'is_required': 'bool',
        'language': 'PortalLanguage',
        'maximum_length': 'int',
        'max_option_length': 'int',
        'min_option_length': 'int',
        'name': 'str',
        'options': 'list[str]',
        'total_options_count': 'int',
        'type': 'str',
        'value': 'str',
        'watermark': 'str'
    }

    attribute_map = {
        'control': 'Control',
        'default_value': 'DefaultValue',
        'description': 'Description',
        'id': 'Id',
        'is_read_only': 'IsReadOnly',
        'is_required': 'IsRequired',
        'language': 'Language',
        'maximum_length': 'MaximumLength',
        'max_option_length': 'MaxOptionLength',
        'min_option_length': 'MinOptionLength',
        'name': 'Name',
        'options': 'Options',
        'total_options_count': 'TotalOptionsCount',
        'type': 'Type',
        'value': 'Value',
        'watermark': 'Watermark'
    }

    def __init__(self, control=None, default_value=None, description=None, id=None, is_read_only=None, is_required=None, language=None, maximum_length=None, max_option_length=None, min_option_length=None, name=None, options=None, total_options_count=None, type=None, value=None, watermark=None):  # noqa: E501
        """PortalMetadata - a model defined in Swagger"""  # noqa: E501
        self._control = None
        self._default_value = None
        self._description = None
        self._id = None
        self._is_read_only = None
        self._is_required = None
        self._language = None
        self._maximum_length = None
        self._max_option_length = None
        self._min_option_length = None
        self._name = None
        self._options = None
        self._total_options_count = None
        self._type = None
        self._value = None
        self._watermark = None
        self.discriminator = None
        if control is not None:
            self.control = control
        if default_value is not None:
            self.default_value = default_value
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if is_read_only is not None:
            self.is_read_only = is_read_only
        if is_required is not None:
            self.is_required = is_required
        if language is not None:
            self.language = language
        if maximum_length is not None:
            self.maximum_length = maximum_length
        if max_option_length is not None:
            self.max_option_length = max_option_length
        if min_option_length is not None:
            self.min_option_length = min_option_length
        if name is not None:
            self.name = name
        if options is not None:
            self.options = options
        if total_options_count is not None:
            self.total_options_count = total_options_count
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if watermark is not None:
            self.watermark = watermark

    @property
    def control(self):
        """Gets the control of this PortalMetadata.  # noqa: E501

        Gets or sets the control.0 = Input, 1 = TextArea, 2 = Calendar, 3 = CheckBox, 4 = PickList, 5 = LanguagePickList, 6 = Numeric, 7 = Decimal, 8 = ReadonlyNumeric, 9 = ReadonlyText, 10 = MultiPickList  # noqa: E501

        :return: The control of this PortalMetadata.  # noqa: E501
        :rtype: str
        """
        return self._control

    @control.setter
    def control(self, control):
        """Sets the control of this PortalMetadata.

        Gets or sets the control.0 = Input, 1 = TextArea, 2 = Calendar, 3 = CheckBox, 4 = PickList, 5 = LanguagePickList, 6 = Numeric, 7 = Decimal, 8 = ReadonlyNumeric, 9 = ReadonlyText, 10 = MultiPickList  # noqa: E501

        :param control: The control of this PortalMetadata.  # noqa: E501
        :type: str
        """
        allowed_values = ["Input", "TextArea", "Calendar", "CheckBox", "PickList", "LanguagePickList", "Numeric", "Decimal", "ReadonlyNumeric", "ReadonlyText", "MultiPickList"]  # noqa: E501
        if control not in allowed_values:
            raise ValueError(
                "Invalid value for `control` ({0}), must be one of {1}"  # noqa: E501
                .format(control, allowed_values)
            )

        self._control = control

    @property
    def default_value(self):
        """Gets the default_value of this PortalMetadata.  # noqa: E501

        Gets or sets the default value.  # noqa: E501

        :return: The default_value of this PortalMetadata.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this PortalMetadata.

        Gets or sets the default value.  # noqa: E501

        :param default_value: The default_value of this PortalMetadata.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def description(self):
        """Gets the description of this PortalMetadata.  # noqa: E501

        Gets or sets the description.  # noqa: E501

        :return: The description of this PortalMetadata.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PortalMetadata.

        Gets or sets the description.  # noqa: E501

        :param description: The description of this PortalMetadata.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this PortalMetadata.  # noqa: E501

        Gets or sets the identifier.  # noqa: E501

        :return: The id of this PortalMetadata.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PortalMetadata.

        Gets or sets the identifier.  # noqa: E501

        :param id: The id of this PortalMetadata.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_read_only(self):
        """Gets the is_read_only of this PortalMetadata.  # noqa: E501

        Gets or sets a value indicating whether this  is read only.  # noqa: E501

        :return: The is_read_only of this PortalMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only):
        """Sets the is_read_only of this PortalMetadata.

        Gets or sets a value indicating whether this  is read only.  # noqa: E501

        :param is_read_only: The is_read_only of this PortalMetadata.  # noqa: E501
        :type: bool
        """

        self._is_read_only = is_read_only

    @property
    def is_required(self):
        """Gets the is_required of this PortalMetadata.  # noqa: E501

        Gets or sets a value indicating whether this  is required.  # noqa: E501

        :return: The is_required of this PortalMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """Sets the is_required of this PortalMetadata.

        Gets or sets a value indicating whether this  is required.  # noqa: E501

        :param is_required: The is_required of this PortalMetadata.  # noqa: E501
        :type: bool
        """

        self._is_required = is_required

    @property
    def language(self):
        """Gets the language of this PortalMetadata.  # noqa: E501


        :return: The language of this PortalMetadata.  # noqa: E501
        :rtype: PortalLanguage
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this PortalMetadata.


        :param language: The language of this PortalMetadata.  # noqa: E501
        :type: PortalLanguage
        """

        self._language = language

    @property
    def maximum_length(self):
        """Gets the maximum_length of this PortalMetadata.  # noqa: E501

        Gets or sets the maximum length.  # noqa: E501

        :return: The maximum_length of this PortalMetadata.  # noqa: E501
        :rtype: int
        """
        return self._maximum_length

    @maximum_length.setter
    def maximum_length(self, maximum_length):
        """Sets the maximum_length of this PortalMetadata.

        Gets or sets the maximum length.  # noqa: E501

        :param maximum_length: The maximum_length of this PortalMetadata.  # noqa: E501
        :type: int
        """

        self._maximum_length = maximum_length

    @property
    def max_option_length(self):
        """Gets the max_option_length of this PortalMetadata.  # noqa: E501

        Gets or sets the maximum option length.  # noqa: E501

        :return: The max_option_length of this PortalMetadata.  # noqa: E501
        :rtype: int
        """
        return self._max_option_length

    @max_option_length.setter
    def max_option_length(self, max_option_length):
        """Sets the max_option_length of this PortalMetadata.

        Gets or sets the maximum option length.  # noqa: E501

        :param max_option_length: The max_option_length of this PortalMetadata.  # noqa: E501
        :type: int
        """

        self._max_option_length = max_option_length

    @property
    def min_option_length(self):
        """Gets the min_option_length of this PortalMetadata.  # noqa: E501

        Gets or sets the minimum option length.  # noqa: E501

        :return: The min_option_length of this PortalMetadata.  # noqa: E501
        :rtype: int
        """
        return self._min_option_length

    @min_option_length.setter
    def min_option_length(self, min_option_length):
        """Sets the min_option_length of this PortalMetadata.

        Gets or sets the minimum option length.  # noqa: E501

        :param min_option_length: The min_option_length of this PortalMetadata.  # noqa: E501
        :type: int
        """

        self._min_option_length = min_option_length

    @property
    def name(self):
        """Gets the name of this PortalMetadata.  # noqa: E501

        Gets or sets the name.  # noqa: E501

        :return: The name of this PortalMetadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PortalMetadata.

        Gets or sets the name.  # noqa: E501

        :param name: The name of this PortalMetadata.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def options(self):
        """Gets the options of this PortalMetadata.  # noqa: E501

        Gets or sets the options.  # noqa: E501

        :return: The options of this PortalMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this PortalMetadata.

        Gets or sets the options.  # noqa: E501

        :param options: The options of this PortalMetadata.  # noqa: E501
        :type: list[str]
        """

        self._options = options

    @property
    def total_options_count(self):
        """Gets the total_options_count of this PortalMetadata.  # noqa: E501

        Gets or sets the number of meta data options.  # noqa: E501

        :return: The total_options_count of this PortalMetadata.  # noqa: E501
        :rtype: int
        """
        return self._total_options_count

    @total_options_count.setter
    def total_options_count(self, total_options_count):
        """Sets the total_options_count of this PortalMetadata.

        Gets or sets the number of meta data options.  # noqa: E501

        :param total_options_count: The total_options_count of this PortalMetadata.  # noqa: E501
        :type: int
        """

        self._total_options_count = total_options_count

    @property
    def type(self):
        """Gets the type of this PortalMetadata.  # noqa: E501

        Gets or sets the type.0 = Project, 1 = Language, 2 = Vendor  # noqa: E501

        :return: The type of this PortalMetadata.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PortalMetadata.

        Gets or sets the type.0 = Project, 1 = Language, 2 = Vendor  # noqa: E501

        :param type: The type of this PortalMetadata.  # noqa: E501
        :type: str
        """
        allowed_values = ["Project", "Language", "Vendor"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def value(self):
        """Gets the value of this PortalMetadata.  # noqa: E501

        Gets or sets the vaue.  # noqa: E501

        :return: The value of this PortalMetadata.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PortalMetadata.

        Gets or sets the vaue.  # noqa: E501

        :param value: The value of this PortalMetadata.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def watermark(self):
        """Gets the watermark of this PortalMetadata.  # noqa: E501

        Gets or sets the water mark.  # noqa: E501

        :return: The watermark of this PortalMetadata.  # noqa: E501
        :rtype: str
        """
        return self._watermark

    @watermark.setter
    def watermark(self, watermark):
        """Sets the watermark of this PortalMetadata.

        Gets or sets the water mark.  # noqa: E501

        :param watermark: The watermark of this PortalMetadata.  # noqa: E501
        :type: str
        """

        self._watermark = watermark

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
        if issubclass(PortalMetadata, dict):
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
        if not isinstance(other, PortalMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
