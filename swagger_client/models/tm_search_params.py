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


class TmSearchParams(object):
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
        'format': 'str',
        'maximum_matches': 'int',
        'minimum_match_percentage': 'float',
        'partial_search': 'bool',
        'segments': 'list[TmSearchSegment]',
        'source_language': 'str',
        'target_language': 'str'
    }

    attribute_map = {
        'format': 'Format',
        'maximum_matches': 'MaximumMatches',
        'minimum_match_percentage': 'MinimumMatchPercentage',
        'partial_search': 'PartialSearch',
        'segments': 'Segments',
        'source_language': 'SourceLanguage',
        'target_language': 'TargetLanguage'
    }

    def __init__(self, format=None, maximum_matches=None, minimum_match_percentage=None, partial_search=None, segments=None, source_language=None, target_language=None, _configuration=None):  # noqa: E501
        """TmSearchParams - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._format = None
        self._maximum_matches = None
        self._minimum_match_percentage = None
        self._partial_search = None
        self._segments = None
        self._source_language = None
        self._target_language = None
        self.discriminator = None

        if format is not None:
            self.format = format
        if maximum_matches is not None:
            self.maximum_matches = maximum_matches
        if minimum_match_percentage is not None:
            self.minimum_match_percentage = minimum_match_percentage
        if partial_search is not None:
            self.partial_search = partial_search
        if segments is not None:
            self.segments = segments
        if source_language is not None:
            self.source_language = source_language
        if target_language is not None:
            self.target_language = target_language

    @property
    def format(self):
        """Gets the format of this TmSearchParams.  # noqa: E501

        Gets or sets the format of the segment supplied in the  member.             Search results will also be supplied in this format.0 = Tmx, 1 = PlainText, 2 = JsonBcm  # noqa: E501

        :return: The format of this TmSearchParams.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this TmSearchParams.

        Gets or sets the format of the segment supplied in the  member.             Search results will also be supplied in this format.0 = Tmx, 1 = PlainText, 2 = JsonBcm  # noqa: E501

        :param format: The format of this TmSearchParams.  # noqa: E501
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
    def maximum_matches(self):
        """Gets the maximum_matches of this TmSearchParams.  # noqa: E501

        Gets or sets the maximum results.  # noqa: E501

        :return: The maximum_matches of this TmSearchParams.  # noqa: E501
        :rtype: int
        """
        return self._maximum_matches

    @maximum_matches.setter
    def maximum_matches(self, maximum_matches):
        """Sets the maximum_matches of this TmSearchParams.

        Gets or sets the maximum results.  # noqa: E501

        :param maximum_matches: The maximum_matches of this TmSearchParams.  # noqa: E501
        :type: int
        """

        self._maximum_matches = maximum_matches

    @property
    def minimum_match_percentage(self):
        """Gets the minimum_match_percentage of this TmSearchParams.  # noqa: E501

        Gets or sets the minimum match percentage.  # noqa: E501

        :return: The minimum_match_percentage of this TmSearchParams.  # noqa: E501
        :rtype: float
        """
        return self._minimum_match_percentage

    @minimum_match_percentage.setter
    def minimum_match_percentage(self, minimum_match_percentage):
        """Sets the minimum_match_percentage of this TmSearchParams.

        Gets or sets the minimum match percentage.  # noqa: E501

        :param minimum_match_percentage: The minimum_match_percentage of this TmSearchParams.  # noqa: E501
        :type: float
        """

        self._minimum_match_percentage = minimum_match_percentage

    @property
    def partial_search(self):
        """Gets the partial_search of this TmSearchParams.  # noqa: E501

        Gets or sets a value indicating whether [partial search].  # noqa: E501

        :return: The partial_search of this TmSearchParams.  # noqa: E501
        :rtype: bool
        """
        return self._partial_search

    @partial_search.setter
    def partial_search(self, partial_search):
        """Sets the partial_search of this TmSearchParams.

        Gets or sets a value indicating whether [partial search].  # noqa: E501

        :param partial_search: The partial_search of this TmSearchParams.  # noqa: E501
        :type: bool
        """

        self._partial_search = partial_search

    @property
    def segments(self):
        """Gets the segments of this TmSearchParams.  # noqa: E501

        Gets or sets the segments.  # noqa: E501

        :return: The segments of this TmSearchParams.  # noqa: E501
        :rtype: list[TmSearchSegment]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """Sets the segments of this TmSearchParams.

        Gets or sets the segments.  # noqa: E501

        :param segments: The segments of this TmSearchParams.  # noqa: E501
        :type: list[TmSearchSegment]
        """

        self._segments = segments

    @property
    def source_language(self):
        """Gets the source_language of this TmSearchParams.  # noqa: E501

        Gets or sets the source language.  # noqa: E501

        :return: The source_language of this TmSearchParams.  # noqa: E501
        :rtype: str
        """
        return self._source_language

    @source_language.setter
    def source_language(self, source_language):
        """Sets the source_language of this TmSearchParams.

        Gets or sets the source language.  # noqa: E501

        :param source_language: The source_language of this TmSearchParams.  # noqa: E501
        :type: str
        """

        self._source_language = source_language

    @property
    def target_language(self):
        """Gets the target_language of this TmSearchParams.  # noqa: E501

        Gets or sets the target language.  # noqa: E501

        :return: The target_language of this TmSearchParams.  # noqa: E501
        :rtype: str
        """
        return self._target_language

    @target_language.setter
    def target_language(self, target_language):
        """Sets the target_language of this TmSearchParams.

        Gets or sets the target language.  # noqa: E501

        :param target_language: The target_language of this TmSearchParams.  # noqa: E501
        :type: str
        """

        self._target_language = target_language

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
        if issubclass(TmSearchParams, dict):
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
        if not isinstance(other, TmSearchParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TmSearchParams):
            return True

        return self.to_dict() != other.to_dict()
