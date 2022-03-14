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


class TmSearchResult(object):
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
        'annotated_source_text': 'str',
        'attributes': 'list[TmAttribute]',
        'format': 'str',
        'penalties': 'list[TmPenalty]',
        'score': 'float',
        'segment_id': 'int',
        'source_text': 'str',
        'target_text': 'str',
        'tm_name': 'str',
        'total_penalty': 'int',
        'translation_id': 'str'
    }

    attribute_map = {
        'annotated_source_text': 'AnnotatedSourceText',
        'attributes': 'Attributes',
        'format': 'Format',
        'penalties': 'Penalties',
        'score': 'Score',
        'segment_id': 'SegmentId',
        'source_text': 'SourceText',
        'target_text': 'TargetText',
        'tm_name': 'TmName',
        'total_penalty': 'TotalPenalty',
        'translation_id': 'TranslationId'
    }

    def __init__(self, annotated_source_text=None, attributes=None, format=None, penalties=None, score=None, segment_id=None, source_text=None, target_text=None, tm_name=None, total_penalty=None, translation_id=None, _configuration=None):  # noqa: E501
        """TmSearchResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._annotated_source_text = None
        self._attributes = None
        self._format = None
        self._penalties = None
        self._score = None
        self._segment_id = None
        self._source_text = None
        self._target_text = None
        self._tm_name = None
        self._total_penalty = None
        self._translation_id = None
        self.discriminator = None

        if annotated_source_text is not None:
            self.annotated_source_text = annotated_source_text
        if attributes is not None:
            self.attributes = attributes
        if format is not None:
            self.format = format
        if penalties is not None:
            self.penalties = penalties
        if score is not None:
            self.score = score
        if segment_id is not None:
            self.segment_id = segment_id
        if source_text is not None:
            self.source_text = source_text
        if target_text is not None:
            self.target_text = target_text
        if tm_name is not None:
            self.tm_name = tm_name
        if total_penalty is not None:
            self.total_penalty = total_penalty
        if translation_id is not None:
            self.translation_id = translation_id

    @property
    def annotated_source_text(self):
        """Gets the annotated_source_text of this TmSearchResult.  # noqa: E501

        Gets or sets the annotated source text.  # noqa: E501

        :return: The annotated_source_text of this TmSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._annotated_source_text

    @annotated_source_text.setter
    def annotated_source_text(self, annotated_source_text):
        """Sets the annotated_source_text of this TmSearchResult.

        Gets or sets the annotated source text.  # noqa: E501

        :param annotated_source_text: The annotated_source_text of this TmSearchResult.  # noqa: E501
        :type: str
        """

        self._annotated_source_text = annotated_source_text

    @property
    def attributes(self):
        """Gets the attributes of this TmSearchResult.  # noqa: E501

        Gets or sets the attributes.  # noqa: E501

        :return: The attributes of this TmSearchResult.  # noqa: E501
        :rtype: list[TmAttribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this TmSearchResult.

        Gets or sets the attributes.  # noqa: E501

        :param attributes: The attributes of this TmSearchResult.  # noqa: E501
        :type: list[TmAttribute]
        """

        self._attributes = attributes

    @property
    def format(self):
        """Gets the format of this TmSearchResult.  # noqa: E501

        Gets or sets the format.0 = Tmx, 1 = PlainText, 2 = JsonBcm  # noqa: E501

        :return: The format of this TmSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this TmSearchResult.

        Gets or sets the format.0 = Tmx, 1 = PlainText, 2 = JsonBcm  # noqa: E501

        :param format: The format of this TmSearchResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["Tmx", "PlainText", "JsonBcm"]  # noqa: E501
        if (self._configuration.client_side_validation and
                format not in allowed_values):
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def penalties(self):
        """Gets the penalties of this TmSearchResult.  # noqa: E501

        Gets or sets the penalties.  # noqa: E501

        :return: The penalties of this TmSearchResult.  # noqa: E501
        :rtype: list[TmPenalty]
        """
        return self._penalties

    @penalties.setter
    def penalties(self, penalties):
        """Sets the penalties of this TmSearchResult.

        Gets or sets the penalties.  # noqa: E501

        :param penalties: The penalties of this TmSearchResult.  # noqa: E501
        :type: list[TmPenalty]
        """

        self._penalties = penalties

    @property
    def score(self):
        """Gets the score of this TmSearchResult.  # noqa: E501

        Gets or sets the score.  # noqa: E501

        :return: The score of this TmSearchResult.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this TmSearchResult.

        Gets or sets the score.  # noqa: E501

        :param score: The score of this TmSearchResult.  # noqa: E501
        :type: float
        """

        self._score = score

    @property
    def segment_id(self):
        """Gets the segment_id of this TmSearchResult.  # noqa: E501

        Gets or sets the identifier.  # noqa: E501

        :return: The segment_id of this TmSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._segment_id

    @segment_id.setter
    def segment_id(self, segment_id):
        """Sets the segment_id of this TmSearchResult.

        Gets or sets the identifier.  # noqa: E501

        :param segment_id: The segment_id of this TmSearchResult.  # noqa: E501
        :type: int
        """

        self._segment_id = segment_id

    @property
    def source_text(self):
        """Gets the source_text of this TmSearchResult.  # noqa: E501

        Gets or sets the source text.  # noqa: E501

        :return: The source_text of this TmSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._source_text

    @source_text.setter
    def source_text(self, source_text):
        """Sets the source_text of this TmSearchResult.

        Gets or sets the source text.  # noqa: E501

        :param source_text: The source_text of this TmSearchResult.  # noqa: E501
        :type: str
        """

        self._source_text = source_text

    @property
    def target_text(self):
        """Gets the target_text of this TmSearchResult.  # noqa: E501

        Gets or sets the target text.  # noqa: E501

        :return: The target_text of this TmSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._target_text

    @target_text.setter
    def target_text(self, target_text):
        """Sets the target_text of this TmSearchResult.

        Gets or sets the target text.  # noqa: E501

        :param target_text: The target_text of this TmSearchResult.  # noqa: E501
        :type: str
        """

        self._target_text = target_text

    @property
    def tm_name(self):
        """Gets the tm_name of this TmSearchResult.  # noqa: E501

        Gets or sets the name of the tm.  # noqa: E501

        :return: The tm_name of this TmSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._tm_name

    @tm_name.setter
    def tm_name(self, tm_name):
        """Sets the tm_name of this TmSearchResult.

        Gets or sets the name of the tm.  # noqa: E501

        :param tm_name: The tm_name of this TmSearchResult.  # noqa: E501
        :type: str
        """

        self._tm_name = tm_name

    @property
    def total_penalty(self):
        """Gets the total_penalty of this TmSearchResult.  # noqa: E501

        Gets or sets the total penalties.  # noqa: E501

        :return: The total_penalty of this TmSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._total_penalty

    @total_penalty.setter
    def total_penalty(self, total_penalty):
        """Sets the total_penalty of this TmSearchResult.

        Gets or sets the total penalties.  # noqa: E501

        :param total_penalty: The total_penalty of this TmSearchResult.  # noqa: E501
        :type: int
        """

        self._total_penalty = total_penalty

    @property
    def translation_id(self):
        """Gets the translation_id of this TmSearchResult.  # noqa: E501

        Gets or sets the translation identifier.  # noqa: E501

        :return: The translation_id of this TmSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._translation_id

    @translation_id.setter
    def translation_id(self, translation_id):
        """Sets the translation_id of this TmSearchResult.

        Gets or sets the translation identifier.  # noqa: E501

        :param translation_id: The translation_id of this TmSearchResult.  # noqa: E501
        :type: str
        """

        self._translation_id = translation_id

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
        if issubclass(TmSearchResult, dict):
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
        if not isinstance(other, TmSearchResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TmSearchResult):
            return True

        return self.to_dict() != other.to_dict()
