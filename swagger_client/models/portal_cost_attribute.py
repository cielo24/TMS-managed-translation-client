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

class PortalCostAttribute(object):
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
        'attribute_name': 'str',
        'attribute_type': 'str',
        'attribute_value': 'str',
        'cost_matrix_name': 'str',
        'data_length': 'str',
        'data_type': 'str',
        'guid': 'str',
        'id': 'int'
    }

    attribute_map = {
        'attribute_name': 'AttributeName',
        'attribute_type': 'AttributeType',
        'attribute_value': 'AttributeValue',
        'cost_matrix_name': 'CostMatrixName',
        'data_length': 'DataLength',
        'data_type': 'DataType',
        'guid': 'Guid',
        'id': 'Id'
    }

    def __init__(self, attribute_name=None, attribute_type=None, attribute_value=None, cost_matrix_name=None, data_length=None, data_type=None, guid=None, id=None):  # noqa: E501
        """PortalCostAttribute - a model defined in Swagger"""  # noqa: E501
        self._attribute_name = None
        self._attribute_type = None
        self._attribute_value = None
        self._cost_matrix_name = None
        self._data_length = None
        self._data_type = None
        self._guid = None
        self._id = None
        self.discriminator = None
        if attribute_name is not None:
            self.attribute_name = attribute_name
        if attribute_type is not None:
            self.attribute_type = attribute_type
        if attribute_value is not None:
            self.attribute_value = attribute_value
        if cost_matrix_name is not None:
            self.cost_matrix_name = cost_matrix_name
        if data_length is not None:
            self.data_length = data_length
        if data_type is not None:
            self.data_type = data_type
        if guid is not None:
            self.guid = guid
        if id is not None:
            self.id = id

    @property
    def attribute_name(self):
        """Gets the attribute_name of this PortalCostAttribute.  # noqa: E501

        Gets or sets the cost attribute name.  # noqa: E501

        :return: The attribute_name of this PortalCostAttribute.  # noqa: E501
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name):
        """Sets the attribute_name of this PortalCostAttribute.

        Gets or sets the cost attribute name.  # noqa: E501

        :param attribute_name: The attribute_name of this PortalCostAttribute.  # noqa: E501
        :type: str
        """

        self._attribute_name = attribute_name

    @property
    def attribute_type(self):
        """Gets the attribute_type of this PortalCostAttribute.  # noqa: E501

        Gets or sets the cost attribute type.  # noqa: E501

        :return: The attribute_type of this PortalCostAttribute.  # noqa: E501
        :rtype: str
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type):
        """Sets the attribute_type of this PortalCostAttribute.

        Gets or sets the cost attribute type.  # noqa: E501

        :param attribute_type: The attribute_type of this PortalCostAttribute.  # noqa: E501
        :type: str
        """

        self._attribute_type = attribute_type

    @property
    def attribute_value(self):
        """Gets the attribute_value of this PortalCostAttribute.  # noqa: E501

        Gets or sets the cost attribute value.  # noqa: E501

        :return: The attribute_value of this PortalCostAttribute.  # noqa: E501
        :rtype: str
        """
        return self._attribute_value

    @attribute_value.setter
    def attribute_value(self, attribute_value):
        """Sets the attribute_value of this PortalCostAttribute.

        Gets or sets the cost attribute value.  # noqa: E501

        :param attribute_value: The attribute_value of this PortalCostAttribute.  # noqa: E501
        :type: str
        """

        self._attribute_value = attribute_value

    @property
    def cost_matrix_name(self):
        """Gets the cost_matrix_name of this PortalCostAttribute.  # noqa: E501

        Gets or sets the cost matrix name.  # noqa: E501

        :return: The cost_matrix_name of this PortalCostAttribute.  # noqa: E501
        :rtype: str
        """
        return self._cost_matrix_name

    @cost_matrix_name.setter
    def cost_matrix_name(self, cost_matrix_name):
        """Sets the cost_matrix_name of this PortalCostAttribute.

        Gets or sets the cost matrix name.  # noqa: E501

        :param cost_matrix_name: The cost_matrix_name of this PortalCostAttribute.  # noqa: E501
        :type: str
        """

        self._cost_matrix_name = cost_matrix_name

    @property
    def data_length(self):
        """Gets the data_length of this PortalCostAttribute.  # noqa: E501

        Gets or sets the cost attribute data length.  # noqa: E501

        :return: The data_length of this PortalCostAttribute.  # noqa: E501
        :rtype: str
        """
        return self._data_length

    @data_length.setter
    def data_length(self, data_length):
        """Sets the data_length of this PortalCostAttribute.

        Gets or sets the cost attribute data length.  # noqa: E501

        :param data_length: The data_length of this PortalCostAttribute.  # noqa: E501
        :type: str
        """

        self._data_length = data_length

    @property
    def data_type(self):
        """Gets the data_type of this PortalCostAttribute.  # noqa: E501

        Gets or sets the cost attribute data type.  # noqa: E501

        :return: The data_type of this PortalCostAttribute.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this PortalCostAttribute.

        Gets or sets the cost attribute data type.  # noqa: E501

        :param data_type: The data_type of this PortalCostAttribute.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def guid(self):
        """Gets the guid of this PortalCostAttribute.  # noqa: E501

        Gets or sets the attribute GUID.  # noqa: E501

        :return: The guid of this PortalCostAttribute.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this PortalCostAttribute.

        Gets or sets the attribute GUID.  # noqa: E501

        :param guid: The guid of this PortalCostAttribute.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def id(self):
        """Gets the id of this PortalCostAttribute.  # noqa: E501

        Gets or sets the attribute Id.  # noqa: E501

        :return: The id of this PortalCostAttribute.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PortalCostAttribute.

        Gets or sets the attribute Id.  # noqa: E501

        :param id: The id of this PortalCostAttribute.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(PortalCostAttribute, dict):
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
        if not isinstance(other, PortalCostAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
