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

class PortalDailyStatistic(object):
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
        'costs': 'list[Cost]',
        '_date': 'datetime',
        'language_pairs': 'list[PortalLanguagePairWordCount]',
        'leverage': 'dict(str, int)',
        'overall_leverage': 'float',
        'savings': 'list[Cost]',
        'total_files': 'int',
        'total_projects': 'int',
        'total_words': 'int'
    }

    attribute_map = {
        'costs': 'Costs',
        '_date': 'Date',
        'language_pairs': 'LanguagePairs',
        'leverage': 'Leverage',
        'overall_leverage': 'OverallLeverage',
        'savings': 'Savings',
        'total_files': 'TotalFiles',
        'total_projects': 'TotalProjects',
        'total_words': 'TotalWords'
    }

    def __init__(self, costs=None, _date=None, language_pairs=None, leverage=None, overall_leverage=None, savings=None, total_files=None, total_projects=None, total_words=None):  # noqa: E501
        """PortalDailyStatistic - a model defined in Swagger"""  # noqa: E501
        self._costs = None
        self.__date = None
        self._language_pairs = None
        self._leverage = None
        self._overall_leverage = None
        self._savings = None
        self._total_files = None
        self._total_projects = None
        self._total_words = None
        self.discriminator = None
        if costs is not None:
            self.costs = costs
        if _date is not None:
            self._date = _date
        if language_pairs is not None:
            self.language_pairs = language_pairs
        if leverage is not None:
            self.leverage = leverage
        if overall_leverage is not None:
            self.overall_leverage = overall_leverage
        if savings is not None:
            self.savings = savings
        if total_files is not None:
            self.total_files = total_files
        if total_projects is not None:
            self.total_projects = total_projects
        if total_words is not None:
            self.total_words = total_words

    @property
    def costs(self):
        """Gets the costs of this PortalDailyStatistic.  # noqa: E501

        Gets the total cost of approved projects, by currency, created on this day.  # noqa: E501

        :return: The costs of this PortalDailyStatistic.  # noqa: E501
        :rtype: list[Cost]
        """
        return self._costs

    @costs.setter
    def costs(self, costs):
        """Sets the costs of this PortalDailyStatistic.

        Gets the total cost of approved projects, by currency, created on this day.  # noqa: E501

        :param costs: The costs of this PortalDailyStatistic.  # noqa: E501
        :type: list[Cost]
        """

        self._costs = costs

    @property
    def _date(self):
        """Gets the _date of this PortalDailyStatistic.  # noqa: E501

        Gets the date for which these statistics apply.  # noqa: E501

        :return: The _date of this PortalDailyStatistic.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this PortalDailyStatistic.

        Gets the date for which these statistics apply.  # noqa: E501

        :param _date: The _date of this PortalDailyStatistic.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def language_pairs(self):
        """Gets the language_pairs of this PortalDailyStatistic.  # noqa: E501

        Gets the language pairs and the number of words for that language in approved projects created on this day.  # noqa: E501

        :return: The language_pairs of this PortalDailyStatistic.  # noqa: E501
        :rtype: list[PortalLanguagePairWordCount]
        """
        return self._language_pairs

    @language_pairs.setter
    def language_pairs(self, language_pairs):
        """Sets the language_pairs of this PortalDailyStatistic.

        Gets the language pairs and the number of words for that language in approved projects created on this day.  # noqa: E501

        :param language_pairs: The language_pairs of this PortalDailyStatistic.  # noqa: E501
        :type: list[PortalLanguagePairWordCount]
        """

        self._language_pairs = language_pairs

    @property
    def leverage(self):
        """Gets the leverage of this PortalDailyStatistic.  # noqa: E501

        Gets the Translation Memory leverage category and the number of words in that category in approved projects created on this day.  # noqa: E501

        :return: The leverage of this PortalDailyStatistic.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._leverage

    @leverage.setter
    def leverage(self, leverage):
        """Sets the leverage of this PortalDailyStatistic.

        Gets the Translation Memory leverage category and the number of words in that category in approved projects created on this day.  # noqa: E501

        :param leverage: The leverage of this PortalDailyStatistic.  # noqa: E501
        :type: dict(str, int)
        """

        self._leverage = leverage

    @property
    def overall_leverage(self):
        """Gets the overall_leverage of this PortalDailyStatistic.  # noqa: E501

        Gets the overall Translation Memory leverage in approved projects created on this day.  # noqa: E501

        :return: The overall_leverage of this PortalDailyStatistic.  # noqa: E501
        :rtype: float
        """
        return self._overall_leverage

    @overall_leverage.setter
    def overall_leverage(self, overall_leverage):
        """Sets the overall_leverage of this PortalDailyStatistic.

        Gets the overall Translation Memory leverage in approved projects created on this day.  # noqa: E501

        :param overall_leverage: The overall_leverage of this PortalDailyStatistic.  # noqa: E501
        :type: float
        """

        self._overall_leverage = overall_leverage

    @property
    def savings(self):
        """Gets the savings of this PortalDailyStatistic.  # noqa: E501

        Gets the total value of any Translation Memory related cost savings, by currency, in approved projects created on this day.  # noqa: E501

        :return: The savings of this PortalDailyStatistic.  # noqa: E501
        :rtype: list[Cost]
        """
        return self._savings

    @savings.setter
    def savings(self, savings):
        """Sets the savings of this PortalDailyStatistic.

        Gets the total value of any Translation Memory related cost savings, by currency, in approved projects created on this day.  # noqa: E501

        :param savings: The savings of this PortalDailyStatistic.  # noqa: E501
        :type: list[Cost]
        """

        self._savings = savings

    @property
    def total_files(self):
        """Gets the total_files of this PortalDailyStatistic.  # noqa: E501

        Gets the total number of target-language files in approved projects created on this day.  # noqa: E501

        :return: The total_files of this PortalDailyStatistic.  # noqa: E501
        :rtype: int
        """
        return self._total_files

    @total_files.setter
    def total_files(self, total_files):
        """Sets the total_files of this PortalDailyStatistic.

        Gets the total number of target-language files in approved projects created on this day.  # noqa: E501

        :param total_files: The total_files of this PortalDailyStatistic.  # noqa: E501
        :type: int
        """

        self._total_files = total_files

    @property
    def total_projects(self):
        """Gets the total_projects of this PortalDailyStatistic.  # noqa: E501

        Gets total number of approved projects created on this day.  # noqa: E501

        :return: The total_projects of this PortalDailyStatistic.  # noqa: E501
        :rtype: int
        """
        return self._total_projects

    @total_projects.setter
    def total_projects(self, total_projects):
        """Sets the total_projects of this PortalDailyStatistic.

        Gets total number of approved projects created on this day.  # noqa: E501

        :param total_projects: The total_projects of this PortalDailyStatistic.  # noqa: E501
        :type: int
        """

        self._total_projects = total_projects

    @property
    def total_words(self):
        """Gets the total_words of this PortalDailyStatistic.  # noqa: E501

        Gets the total words in approved projects created on this day.  # noqa: E501

        :return: The total_words of this PortalDailyStatistic.  # noqa: E501
        :rtype: int
        """
        return self._total_words

    @total_words.setter
    def total_words(self, total_words):
        """Sets the total_words of this PortalDailyStatistic.

        Gets the total words in approved projects created on this day.  # noqa: E501

        :param total_words: The total_words of this PortalDailyStatistic.  # noqa: E501
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
        if issubclass(PortalDailyStatistic, dict):
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
        if not isinstance(other, PortalDailyStatistic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
