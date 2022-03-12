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

class PortalCostBand(object):
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
        'band_id': 'int',
        'min_value': 'int',
        'repeated_cost_per_word': 'float',
        'word_cost': 'float',
        'word_count': 'int'
    }

    attribute_map = {
        'band_id': 'BandId',
        'min_value': 'MinValue',
        'repeated_cost_per_word': 'RepeatedCostPerWord',
        'word_cost': 'WordCost',
        'word_count': 'WordCount'
    }

    def __init__(self, band_id=None, min_value=None, repeated_cost_per_word=None, word_cost=None, word_count=None):  # noqa: E501
        """PortalCostBand - a model defined in Swagger"""  # noqa: E501
        self._band_id = None
        self._min_value = None
        self._repeated_cost_per_word = None
        self._word_cost = None
        self._word_count = None
        self.discriminator = None
        if band_id is not None:
            self.band_id = band_id
        if min_value is not None:
            self.min_value = min_value
        if repeated_cost_per_word is not None:
            self.repeated_cost_per_word = repeated_cost_per_word
        if word_cost is not None:
            self.word_cost = word_cost
        if word_count is not None:
            self.word_count = word_count

    @property
    def band_id(self):
        """Gets the band_id of this PortalCostBand.  # noqa: E501

        The id of the cost band.  # noqa: E501

        :return: The band_id of this PortalCostBand.  # noqa: E501
        :rtype: int
        """
        return self._band_id

    @band_id.setter
    def band_id(self, band_id):
        """Sets the band_id of this PortalCostBand.

        The id of the cost band.  # noqa: E501

        :param band_id: The band_id of this PortalCostBand.  # noqa: E501
        :type: int
        """

        self._band_id = band_id

    @property
    def min_value(self):
        """Gets the min_value of this PortalCostBand.  # noqa: E501

        The minimum match percentage of the band.  # noqa: E501

        :return: The min_value of this PortalCostBand.  # noqa: E501
        :rtype: int
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this PortalCostBand.

        The minimum match percentage of the band.  # noqa: E501

        :param min_value: The min_value of this PortalCostBand.  # noqa: E501
        :type: int
        """

        self._min_value = min_value

    @property
    def repeated_cost_per_word(self):
        """Gets the repeated_cost_per_word of this PortalCostBand.  # noqa: E501

        The cost for a repeated word - not cost-band specific.  # noqa: E501

        :return: The repeated_cost_per_word of this PortalCostBand.  # noqa: E501
        :rtype: float
        """
        return self._repeated_cost_per_word

    @repeated_cost_per_word.setter
    def repeated_cost_per_word(self, repeated_cost_per_word):
        """Sets the repeated_cost_per_word of this PortalCostBand.

        The cost for a repeated word - not cost-band specific.  # noqa: E501

        :param repeated_cost_per_word: The repeated_cost_per_word of this PortalCostBand.  # noqa: E501
        :type: float
        """

        self._repeated_cost_per_word = repeated_cost_per_word

    @property
    def word_cost(self):
        """Gets the word_cost of this PortalCostBand.  # noqa: E501

        The cost for the translation of a word in the cost band.  # noqa: E501

        :return: The word_cost of this PortalCostBand.  # noqa: E501
        :rtype: float
        """
        return self._word_cost

    @word_cost.setter
    def word_cost(self, word_cost):
        """Sets the word_cost of this PortalCostBand.

        The cost for the translation of a word in the cost band.  # noqa: E501

        :param word_cost: The word_cost of this PortalCostBand.  # noqa: E501
        :type: float
        """

        self._word_cost = word_cost

    @property
    def word_count(self):
        """Gets the word_count of this PortalCostBand.  # noqa: E501

        The number of words allocated to the cost band.  # noqa: E501

        :return: The word_count of this PortalCostBand.  # noqa: E501
        :rtype: int
        """
        return self._word_count

    @word_count.setter
    def word_count(self, word_count):
        """Sets the word_count of this PortalCostBand.

        The number of words allocated to the cost band.  # noqa: E501

        :param word_count: The word_count of this PortalCostBand.  # noqa: E501
        :type: int
        """

        self._word_count = word_count

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
        if issubclass(PortalCostBand, dict):
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
        if not isinstance(other, PortalCostBand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
