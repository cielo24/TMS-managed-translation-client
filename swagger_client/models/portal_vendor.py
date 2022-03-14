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


class PortalVendor(object):
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
        'address': 'str',
        'assignees': 'list[PortalVendorAssignee]',
        'assignees_language_pair': 'list[PortalVendorAssigneeLanguagePair]',
        'description': 'str',
        'id': 'str',
        'key_contact_email': 'str',
        'key_contact_name': 'str',
        'language_pairs': 'list[PortalLanguagePair]',
        'metadata': 'list[PortalMetadata]',
        'name': 'str',
        'on_time_deliveries': 'float',
        'quality_rating': 'float',
        'telephone': 'str'
    }

    attribute_map = {
        'address': 'Address',
        'assignees': 'Assignees',
        'assignees_language_pair': 'AssigneesLanguagePair',
        'description': 'Description',
        'id': 'Id',
        'key_contact_email': 'KeyContactEmail',
        'key_contact_name': 'KeyContactName',
        'language_pairs': 'LanguagePairs',
        'metadata': 'Metadata',
        'name': 'Name',
        'on_time_deliveries': 'OnTimeDeliveries',
        'quality_rating': 'QualityRating',
        'telephone': 'Telephone'
    }

    def __init__(self, address=None, assignees=None, assignees_language_pair=None, description=None, id=None, key_contact_email=None, key_contact_name=None, language_pairs=None, metadata=None, name=None, on_time_deliveries=None, quality_rating=None, telephone=None, _configuration=None):  # noqa: E501
        """PortalVendor - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address = None
        self._assignees = None
        self._assignees_language_pair = None
        self._description = None
        self._id = None
        self._key_contact_email = None
        self._key_contact_name = None
        self._language_pairs = None
        self._metadata = None
        self._name = None
        self._on_time_deliveries = None
        self._quality_rating = None
        self._telephone = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if assignees is not None:
            self.assignees = assignees
        if assignees_language_pair is not None:
            self.assignees_language_pair = assignees_language_pair
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if key_contact_email is not None:
            self.key_contact_email = key_contact_email
        if key_contact_name is not None:
            self.key_contact_name = key_contact_name
        if language_pairs is not None:
            self.language_pairs = language_pairs
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if on_time_deliveries is not None:
            self.on_time_deliveries = on_time_deliveries
        if quality_rating is not None:
            self.quality_rating = quality_rating
        if telephone is not None:
            self.telephone = telephone

    @property
    def address(self):
        """Gets the address of this PortalVendor.  # noqa: E501

        Gets or sets the address.  # noqa: E501

        :return: The address of this PortalVendor.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PortalVendor.

        Gets or sets the address.  # noqa: E501

        :param address: The address of this PortalVendor.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def assignees(self):
        """Gets the assignees of this PortalVendor.  # noqa: E501

        Gets or sets the ProjectManager/DTP/Engineer.  # noqa: E501

        :return: The assignees of this PortalVendor.  # noqa: E501
        :rtype: list[PortalVendorAssignee]
        """
        return self._assignees

    @assignees.setter
    def assignees(self, assignees):
        """Sets the assignees of this PortalVendor.

        Gets or sets the ProjectManager/DTP/Engineer.  # noqa: E501

        :param assignees: The assignees of this PortalVendor.  # noqa: E501
        :type: list[PortalVendorAssignee]
        """

        self._assignees = assignees

    @property
    def assignees_language_pair(self):
        """Gets the assignees_language_pair of this PortalVendor.  # noqa: E501

        Gets or sets the language Translators/Reviewers.  # noqa: E501

        :return: The assignees_language_pair of this PortalVendor.  # noqa: E501
        :rtype: list[PortalVendorAssigneeLanguagePair]
        """
        return self._assignees_language_pair

    @assignees_language_pair.setter
    def assignees_language_pair(self, assignees_language_pair):
        """Sets the assignees_language_pair of this PortalVendor.

        Gets or sets the language Translators/Reviewers.  # noqa: E501

        :param assignees_language_pair: The assignees_language_pair of this PortalVendor.  # noqa: E501
        :type: list[PortalVendorAssigneeLanguagePair]
        """

        self._assignees_language_pair = assignees_language_pair

    @property
    def description(self):
        """Gets the description of this PortalVendor.  # noqa: E501

        Gets or sets the description.  # noqa: E501

        :return: The description of this PortalVendor.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PortalVendor.

        Gets or sets the description.  # noqa: E501

        :param description: The description of this PortalVendor.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this PortalVendor.  # noqa: E501

        Gets or sets the identifier.  # noqa: E501

        :return: The id of this PortalVendor.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PortalVendor.

        Gets or sets the identifier.  # noqa: E501

        :param id: The id of this PortalVendor.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def key_contact_email(self):
        """Gets the key_contact_email of this PortalVendor.  # noqa: E501

        Gets or sets the key contact email.  # noqa: E501

        :return: The key_contact_email of this PortalVendor.  # noqa: E501
        :rtype: str
        """
        return self._key_contact_email

    @key_contact_email.setter
    def key_contact_email(self, key_contact_email):
        """Sets the key_contact_email of this PortalVendor.

        Gets or sets the key contact email.  # noqa: E501

        :param key_contact_email: The key_contact_email of this PortalVendor.  # noqa: E501
        :type: str
        """

        self._key_contact_email = key_contact_email

    @property
    def key_contact_name(self):
        """Gets the key_contact_name of this PortalVendor.  # noqa: E501

        Gets or sets the key contact.  # noqa: E501

        :return: The key_contact_name of this PortalVendor.  # noqa: E501
        :rtype: str
        """
        return self._key_contact_name

    @key_contact_name.setter
    def key_contact_name(self, key_contact_name):
        """Sets the key_contact_name of this PortalVendor.

        Gets or sets the key contact.  # noqa: E501

        :param key_contact_name: The key_contact_name of this PortalVendor.  # noqa: E501
        :type: str
        """

        self._key_contact_name = key_contact_name

    @property
    def language_pairs(self):
        """Gets the language_pairs of this PortalVendor.  # noqa: E501

        Gets or sets the language pairs.  # noqa: E501

        :return: The language_pairs of this PortalVendor.  # noqa: E501
        :rtype: list[PortalLanguagePair]
        """
        return self._language_pairs

    @language_pairs.setter
    def language_pairs(self, language_pairs):
        """Sets the language_pairs of this PortalVendor.

        Gets or sets the language pairs.  # noqa: E501

        :param language_pairs: The language_pairs of this PortalVendor.  # noqa: E501
        :type: list[PortalLanguagePair]
        """

        self._language_pairs = language_pairs

    @property
    def metadata(self):
        """Gets the metadata of this PortalVendor.  # noqa: E501

        Gets or sets the metadata.  # noqa: E501

        :return: The metadata of this PortalVendor.  # noqa: E501
        :rtype: list[PortalMetadata]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PortalVendor.

        Gets or sets the metadata.  # noqa: E501

        :param metadata: The metadata of this PortalVendor.  # noqa: E501
        :type: list[PortalMetadata]
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this PortalVendor.  # noqa: E501

        Gets or sets the name.  # noqa: E501

        :return: The name of this PortalVendor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PortalVendor.

        Gets or sets the name.  # noqa: E501

        :param name: The name of this PortalVendor.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def on_time_deliveries(self):
        """Gets the on_time_deliveries of this PortalVendor.  # noqa: E501

        Gets or sets the percentage of on time deliveries.  # noqa: E501

        :return: The on_time_deliveries of this PortalVendor.  # noqa: E501
        :rtype: float
        """
        return self._on_time_deliveries

    @on_time_deliveries.setter
    def on_time_deliveries(self, on_time_deliveries):
        """Sets the on_time_deliveries of this PortalVendor.

        Gets or sets the percentage of on time deliveries.  # noqa: E501

        :param on_time_deliveries: The on_time_deliveries of this PortalVendor.  # noqa: E501
        :type: float
        """

        self._on_time_deliveries = on_time_deliveries

    @property
    def quality_rating(self):
        """Gets the quality_rating of this PortalVendor.  # noqa: E501

        Gets or sets the quality rating percentage.  # noqa: E501

        :return: The quality_rating of this PortalVendor.  # noqa: E501
        :rtype: float
        """
        return self._quality_rating

    @quality_rating.setter
    def quality_rating(self, quality_rating):
        """Sets the quality_rating of this PortalVendor.

        Gets or sets the quality rating percentage.  # noqa: E501

        :param quality_rating: The quality_rating of this PortalVendor.  # noqa: E501
        :type: float
        """

        self._quality_rating = quality_rating

    @property
    def telephone(self):
        """Gets the telephone of this PortalVendor.  # noqa: E501

        Gets or sets the telephone.  # noqa: E501

        :return: The telephone of this PortalVendor.  # noqa: E501
        :rtype: str
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """Sets the telephone of this PortalVendor.

        Gets or sets the telephone.  # noqa: E501

        :param telephone: The telephone of this PortalVendor.  # noqa: E501
        :type: str
        """

        self._telephone = telephone

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
        if issubclass(PortalVendor, dict):
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
        if not isinstance(other, PortalVendor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortalVendor):
            return True

        return self.to_dict() != other.to_dict()
