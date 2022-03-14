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


class PortalProjectLanguageStatus(object):
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
        'files': 'list[PortalProjectFileDetails]',
        'fuzzy_words': 'int',
        'hundred_words': 'int',
        'language': 'PortalLanguage',
        'locked_words': 'int',
        'new_words': 'int',
        'percent_complete': 'int',
        'perfect_match_words': 'int',
        'repeated_words': 'int',
        'tm_leverage': 'float',
        'tm_savings': 'float',
        'total_cost': 'float',
        'total_words': 'int'
    }

    attribute_map = {
        'files': 'Files',
        'fuzzy_words': 'FuzzyWords',
        'hundred_words': 'HundredWords',
        'language': 'Language',
        'locked_words': 'LockedWords',
        'new_words': 'NewWords',
        'percent_complete': 'PercentComplete',
        'perfect_match_words': 'PerfectMatchWords',
        'repeated_words': 'RepeatedWords',
        'tm_leverage': 'TMLeverage',
        'tm_savings': 'TMSavings',
        'total_cost': 'TotalCost',
        'total_words': 'TotalWords'
    }

    def __init__(self, files=None, fuzzy_words=None, hundred_words=None, language=None, locked_words=None, new_words=None, percent_complete=None, perfect_match_words=None, repeated_words=None, tm_leverage=None, tm_savings=None, total_cost=None, total_words=None, _configuration=None):  # noqa: E501
        """PortalProjectLanguageStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._files = None
        self._fuzzy_words = None
        self._hundred_words = None
        self._language = None
        self._locked_words = None
        self._new_words = None
        self._percent_complete = None
        self._perfect_match_words = None
        self._repeated_words = None
        self._tm_leverage = None
        self._tm_savings = None
        self._total_cost = None
        self._total_words = None
        self.discriminator = None

        if files is not None:
            self.files = files
        if fuzzy_words is not None:
            self.fuzzy_words = fuzzy_words
        if hundred_words is not None:
            self.hundred_words = hundred_words
        if language is not None:
            self.language = language
        if locked_words is not None:
            self.locked_words = locked_words
        if new_words is not None:
            self.new_words = new_words
        if percent_complete is not None:
            self.percent_complete = percent_complete
        if perfect_match_words is not None:
            self.perfect_match_words = perfect_match_words
        if repeated_words is not None:
            self.repeated_words = repeated_words
        if tm_leverage is not None:
            self.tm_leverage = tm_leverage
        if tm_savings is not None:
            self.tm_savings = tm_savings
        if total_cost is not None:
            self.total_cost = total_cost
        if total_words is not None:
            self.total_words = total_words

    @property
    def files(self):
        """Gets the files of this PortalProjectLanguageStatus.  # noqa: E501

        The files assocaited with the language.  # noqa: E501

        :return: The files of this PortalProjectLanguageStatus.  # noqa: E501
        :rtype: list[PortalProjectFileDetails]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this PortalProjectLanguageStatus.

        The files assocaited with the language.  # noqa: E501

        :param files: The files of this PortalProjectLanguageStatus.  # noqa: E501
        :type: list[PortalProjectFileDetails]
        """

        self._files = files

    @property
    def fuzzy_words(self):
        """Gets the fuzzy_words of this PortalProjectLanguageStatus.  # noqa: E501

        The total number of words for the language receiving a fuzzy match from the translation memory during preparation.  # noqa: E501

        :return: The fuzzy_words of this PortalProjectLanguageStatus.  # noqa: E501
        :rtype: int
        """
        return self._fuzzy_words

    @fuzzy_words.setter
    def fuzzy_words(self, fuzzy_words):
        """Sets the fuzzy_words of this PortalProjectLanguageStatus.

        The total number of words for the language receiving a fuzzy match from the translation memory during preparation.  # noqa: E501

        :param fuzzy_words: The fuzzy_words of this PortalProjectLanguageStatus.  # noqa: E501
        :type: int
        """

        self._fuzzy_words = fuzzy_words

    @property
    def hundred_words(self):
        """Gets the hundred_words of this PortalProjectLanguageStatus.  # noqa: E501

        The total number of words for the language receiving a one hundred percent match from the translation memory during preparation.  # noqa: E501

        :return: The hundred_words of this PortalProjectLanguageStatus.  # noqa: E501
        :rtype: int
        """
        return self._hundred_words

    @hundred_words.setter
    def hundred_words(self, hundred_words):
        """Sets the hundred_words of this PortalProjectLanguageStatus.

        The total number of words for the language receiving a one hundred percent match from the translation memory during preparation.  # noqa: E501

        :param hundred_words: The hundred_words of this PortalProjectLanguageStatus.  # noqa: E501
        :type: int
        """

        self._hundred_words = hundred_words

    @property
    def language(self):
        """Gets the language of this PortalProjectLanguageStatus.  # noqa: E501

        The associated target language within the project.  # noqa: E501

        :return: The language of this PortalProjectLanguageStatus.  # noqa: E501
        :rtype: PortalLanguage
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this PortalProjectLanguageStatus.

        The associated target language within the project.  # noqa: E501

        :param language: The language of this PortalProjectLanguageStatus.  # noqa: E501
        :type: PortalLanguage
        """

        self._language = language

    @property
    def locked_words(self):
        """Gets the locked_words of this PortalProjectLanguageStatus.  # noqa: E501

        The total number of words for the language considered to be locked during preparation.  # noqa: E501

        :return: The locked_words of this PortalProjectLanguageStatus.  # noqa: E501
        :rtype: int
        """
        return self._locked_words

    @locked_words.setter
    def locked_words(self, locked_words):
        """Sets the locked_words of this PortalProjectLanguageStatus.

        The total number of words for the language considered to be locked during preparation.  # noqa: E501

        :param locked_words: The locked_words of this PortalProjectLanguageStatus.  # noqa: E501
        :type: int
        """

        self._locked_words = locked_words

    @property
    def new_words(self):
        """Gets the new_words of this PortalProjectLanguageStatus.  # noqa: E501

        The total number of words for the language receiving no match from the translation memory during preparation.  # noqa: E501

        :return: The new_words of this PortalProjectLanguageStatus.  # noqa: E501
        :rtype: int
        """
        return self._new_words

    @new_words.setter
    def new_words(self, new_words):
        """Sets the new_words of this PortalProjectLanguageStatus.

        The total number of words for the language receiving no match from the translation memory during preparation.  # noqa: E501

        :param new_words: The new_words of this PortalProjectLanguageStatus.  # noqa: E501
        :type: int
        """

        self._new_words = new_words

    @property
    def percent_complete(self):
        """Gets the percent_complete of this PortalProjectLanguageStatus.  # noqa: E501

        A summary value indicating the approximate completion percentage of the language. Often this value is calculated from the number of files which have reached the ForDownload status.  # noqa: E501

        :return: The percent_complete of this PortalProjectLanguageStatus.  # noqa: E501
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """Sets the percent_complete of this PortalProjectLanguageStatus.

        A summary value indicating the approximate completion percentage of the language. Often this value is calculated from the number of files which have reached the ForDownload status.  # noqa: E501

        :param percent_complete: The percent_complete of this PortalProjectLanguageStatus.  # noqa: E501
        :type: int
        """

        self._percent_complete = percent_complete

    @property
    def perfect_match_words(self):
        """Gets the perfect_match_words of this PortalProjectLanguageStatus.  # noqa: E501

        The total number of words for the language receiving no match from the translation memory during preparation.  # noqa: E501

        :return: The perfect_match_words of this PortalProjectLanguageStatus.  # noqa: E501
        :rtype: int
        """
        return self._perfect_match_words

    @perfect_match_words.setter
    def perfect_match_words(self, perfect_match_words):
        """Sets the perfect_match_words of this PortalProjectLanguageStatus.

        The total number of words for the language receiving no match from the translation memory during preparation.  # noqa: E501

        :param perfect_match_words: The perfect_match_words of this PortalProjectLanguageStatus.  # noqa: E501
        :type: int
        """

        self._perfect_match_words = perfect_match_words

    @property
    def repeated_words(self):
        """Gets the repeated_words of this PortalProjectLanguageStatus.  # noqa: E501

        The total number of words for the language considered to be repeated during preparation.  # noqa: E501

        :return: The repeated_words of this PortalProjectLanguageStatus.  # noqa: E501
        :rtype: int
        """
        return self._repeated_words

    @repeated_words.setter
    def repeated_words(self, repeated_words):
        """Sets the repeated_words of this PortalProjectLanguageStatus.

        The total number of words for the language considered to be repeated during preparation.  # noqa: E501

        :param repeated_words: The repeated_words of this PortalProjectLanguageStatus.  # noqa: E501
        :type: int
        """

        self._repeated_words = repeated_words

    @property
    def tm_leverage(self):
        """Gets the tm_leverage of this PortalProjectLanguageStatus.  # noqa: E501

        The overall percentage of words leverage from Translation Memory during preparation.  # noqa: E501

        :return: The tm_leverage of this PortalProjectLanguageStatus.  # noqa: E501
        :rtype: float
        """
        return self._tm_leverage

    @tm_leverage.setter
    def tm_leverage(self, tm_leverage):
        """Sets the tm_leverage of this PortalProjectLanguageStatus.

        The overall percentage of words leverage from Translation Memory during preparation.  # noqa: E501

        :param tm_leverage: The tm_leverage of this PortalProjectLanguageStatus.  # noqa: E501
        :type: float
        """

        self._tm_leverage = tm_leverage

    @property
    def tm_savings(self):
        """Gets the tm_savings of this PortalProjectLanguageStatus.  # noqa: E501

        The financial value of any saving derived from the use of Translation Memory for the language.  # noqa: E501

        :return: The tm_savings of this PortalProjectLanguageStatus.  # noqa: E501
        :rtype: float
        """
        return self._tm_savings

    @tm_savings.setter
    def tm_savings(self, tm_savings):
        """Sets the tm_savings of this PortalProjectLanguageStatus.

        The financial value of any saving derived from the use of Translation Memory for the language.  # noqa: E501

        :param tm_savings: The tm_savings of this PortalProjectLanguageStatus.  # noqa: E501
        :type: float
        """

        self._tm_savings = tm_savings

    @property
    def total_cost(self):
        """Gets the total_cost of this PortalProjectLanguageStatus.  # noqa: E501

        The total cost for the language.  # noqa: E501

        :return: The total_cost of this PortalProjectLanguageStatus.  # noqa: E501
        :rtype: float
        """
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        """Sets the total_cost of this PortalProjectLanguageStatus.

        The total cost for the language.  # noqa: E501

        :param total_cost: The total_cost of this PortalProjectLanguageStatus.  # noqa: E501
        :type: float
        """

        self._total_cost = total_cost

    @property
    def total_words(self):
        """Gets the total_words of this PortalProjectLanguageStatus.  # noqa: E501

        The total number of words to be translated for the language.  # noqa: E501

        :return: The total_words of this PortalProjectLanguageStatus.  # noqa: E501
        :rtype: int
        """
        return self._total_words

    @total_words.setter
    def total_words(self, total_words):
        """Sets the total_words of this PortalProjectLanguageStatus.

        The total number of words to be translated for the language.  # noqa: E501

        :param total_words: The total_words of this PortalProjectLanguageStatus.  # noqa: E501
        :type: int
        """

        self._total_words = total_words

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
        if issubclass(PortalProjectLanguageStatus, dict):
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
        if not isinstance(other, PortalProjectLanguageStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortalProjectLanguageStatus):
            return True

        return self.to_dict() != other.to_dict()
