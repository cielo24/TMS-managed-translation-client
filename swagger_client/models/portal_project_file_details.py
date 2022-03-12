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

class PortalProjectFileDetails(object):
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
        'annotated_file_id': 'str',
        'annotated_file_stored_date': 'datetime',
        'assignees': 'PortalGroup',
        'authorized_date': 'datetime',
        'can_be_cancelled': 'bool',
        'cost': 'float',
        'cost_attributes': 'list[PortalCostAttribute]',
        'cost_bands': 'list[PortalCostBand]',
        'cost_matrix_name': 'str',
        'folder': 'str',
        'fuzzy_words': 'int',
        'hundred_words': 'int',
        'id': 'str',
        'in_context_preview_status': 'str',
        'locked_words': 'int',
        'name': 'str',
        'new_words': 'int',
        'owner': 'PortalOwner',
        'perfect_match_words': 'int',
        'portal_reviewers': 'list[PortalReviewer]',
        'portal_signoffers': 'list[PortalSignoffer]',
        'rejected': 'bool',
        'repeated_words': 'int',
        'source_id': 'str',
        'status': 'str',
        'status_detail': 'str',
        'status_id': 'str',
        'status_type': 'str',
        'target_language': 'PortalLanguage',
        'task_id': 'str',
        'tm_leverage': 'float',
        'tm_savings': 'float',
        'total_words': 'int',
        'workflow_attributes': 'list[PortalWorkflowAttribute]'
    }

    attribute_map = {
        'annotated_file_id': 'AnnotatedFileId',
        'annotated_file_stored_date': 'AnnotatedFileStoredDate',
        'assignees': 'Assignees',
        'authorized_date': 'AuthorizedDate',
        'can_be_cancelled': 'CanBeCancelled',
        'cost': 'Cost',
        'cost_attributes': 'CostAttributes',
        'cost_bands': 'CostBands',
        'cost_matrix_name': 'CostMatrixName',
        'folder': 'Folder',
        'fuzzy_words': 'FuzzyWords',
        'hundred_words': 'HundredWords',
        'id': 'Id',
        'in_context_preview_status': 'InContextPreviewStatus',
        'locked_words': 'LockedWords',
        'name': 'Name',
        'new_words': 'NewWords',
        'owner': 'Owner',
        'perfect_match_words': 'PerfectMatchWords',
        'portal_reviewers': 'PortalReviewers',
        'portal_signoffers': 'PortalSignoffers',
        'rejected': 'Rejected',
        'repeated_words': 'RepeatedWords',
        'source_id': 'SourceId',
        'status': 'Status',
        'status_detail': 'StatusDetail',
        'status_id': 'StatusId',
        'status_type': 'StatusType',
        'target_language': 'TargetLanguage',
        'task_id': 'TaskId',
        'tm_leverage': 'TMLeverage',
        'tm_savings': 'TMSavings',
        'total_words': 'TotalWords',
        'workflow_attributes': 'WorkflowAttributes'
    }

    def __init__(self, annotated_file_id=None, annotated_file_stored_date=None, assignees=None, authorized_date=None, can_be_cancelled=None, cost=None, cost_attributes=None, cost_bands=None, cost_matrix_name=None, folder=None, fuzzy_words=None, hundred_words=None, id=None, in_context_preview_status=None, locked_words=None, name=None, new_words=None, owner=None, perfect_match_words=None, portal_reviewers=None, portal_signoffers=None, rejected=None, repeated_words=None, source_id=None, status=None, status_detail=None, status_id=None, status_type=None, target_language=None, task_id=None, tm_leverage=None, tm_savings=None, total_words=None, workflow_attributes=None):  # noqa: E501
        """PortalProjectFileDetails - a model defined in Swagger"""  # noqa: E501
        self._annotated_file_id = None
        self._annotated_file_stored_date = None
        self._assignees = None
        self._authorized_date = None
        self._can_be_cancelled = None
        self._cost = None
        self._cost_attributes = None
        self._cost_bands = None
        self._cost_matrix_name = None
        self._folder = None
        self._fuzzy_words = None
        self._hundred_words = None
        self._id = None
        self._in_context_preview_status = None
        self._locked_words = None
        self._name = None
        self._new_words = None
        self._owner = None
        self._perfect_match_words = None
        self._portal_reviewers = None
        self._portal_signoffers = None
        self._rejected = None
        self._repeated_words = None
        self._source_id = None
        self._status = None
        self._status_detail = None
        self._status_id = None
        self._status_type = None
        self._target_language = None
        self._task_id = None
        self._tm_leverage = None
        self._tm_savings = None
        self._total_words = None
        self._workflow_attributes = None
        self.discriminator = None
        if annotated_file_id is not None:
            self.annotated_file_id = annotated_file_id
        if annotated_file_stored_date is not None:
            self.annotated_file_stored_date = annotated_file_stored_date
        if assignees is not None:
            self.assignees = assignees
        if authorized_date is not None:
            self.authorized_date = authorized_date
        if can_be_cancelled is not None:
            self.can_be_cancelled = can_be_cancelled
        if cost is not None:
            self.cost = cost
        if cost_attributes is not None:
            self.cost_attributes = cost_attributes
        if cost_bands is not None:
            self.cost_bands = cost_bands
        if cost_matrix_name is not None:
            self.cost_matrix_name = cost_matrix_name
        if folder is not None:
            self.folder = folder
        if fuzzy_words is not None:
            self.fuzzy_words = fuzzy_words
        if hundred_words is not None:
            self.hundred_words = hundred_words
        if id is not None:
            self.id = id
        if in_context_preview_status is not None:
            self.in_context_preview_status = in_context_preview_status
        if locked_words is not None:
            self.locked_words = locked_words
        if name is not None:
            self.name = name
        if new_words is not None:
            self.new_words = new_words
        if owner is not None:
            self.owner = owner
        if perfect_match_words is not None:
            self.perfect_match_words = perfect_match_words
        if portal_reviewers is not None:
            self.portal_reviewers = portal_reviewers
        if portal_signoffers is not None:
            self.portal_signoffers = portal_signoffers
        if rejected is not None:
            self.rejected = rejected
        if repeated_words is not None:
            self.repeated_words = repeated_words
        if source_id is not None:
            self.source_id = source_id
        if status is not None:
            self.status = status
        if status_detail is not None:
            self.status_detail = status_detail
        if status_id is not None:
            self.status_id = status_id
        if status_type is not None:
            self.status_type = status_type
        if target_language is not None:
            self.target_language = target_language
        if task_id is not None:
            self.task_id = task_id
        if tm_leverage is not None:
            self.tm_leverage = tm_leverage
        if tm_savings is not None:
            self.tm_savings = tm_savings
        if total_words is not None:
            self.total_words = total_words
        if workflow_attributes is not None:
            self.workflow_attributes = workflow_attributes

    @property
    def annotated_file_id(self):
        """Gets the annotated_file_id of this PortalProjectFileDetails.  # noqa: E501

        The unique identifier of the annotated source file if one exists. Used by the In-Context Review functionality if available.  # noqa: E501

        :return: The annotated_file_id of this PortalProjectFileDetails.  # noqa: E501
        :rtype: str
        """
        return self._annotated_file_id

    @annotated_file_id.setter
    def annotated_file_id(self, annotated_file_id):
        """Sets the annotated_file_id of this PortalProjectFileDetails.

        The unique identifier of the annotated source file if one exists. Used by the In-Context Review functionality if available.  # noqa: E501

        :param annotated_file_id: The annotated_file_id of this PortalProjectFileDetails.  # noqa: E501
        :type: str
        """

        self._annotated_file_id = annotated_file_id

    @property
    def annotated_file_stored_date(self):
        """Gets the annotated_file_stored_date of this PortalProjectFileDetails.  # noqa: E501

        The date the annotated source file was stored.  # noqa: E501

        :return: The annotated_file_stored_date of this PortalProjectFileDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._annotated_file_stored_date

    @annotated_file_stored_date.setter
    def annotated_file_stored_date(self, annotated_file_stored_date):
        """Sets the annotated_file_stored_date of this PortalProjectFileDetails.

        The date the annotated source file was stored.  # noqa: E501

        :param annotated_file_stored_date: The annotated_file_stored_date of this PortalProjectFileDetails.  # noqa: E501
        :type: datetime
        """

        self._annotated_file_stored_date = annotated_file_stored_date

    @property
    def assignees(self):
        """Gets the assignees of this PortalProjectFileDetails.  # noqa: E501


        :return: The assignees of this PortalProjectFileDetails.  # noqa: E501
        :rtype: PortalGroup
        """
        return self._assignees

    @assignees.setter
    def assignees(self, assignees):
        """Sets the assignees of this PortalProjectFileDetails.


        :param assignees: The assignees of this PortalProjectFileDetails.  # noqa: E501
        :type: PortalGroup
        """

        self._assignees = assignees

    @property
    def authorized_date(self):
        """Gets the authorized_date of this PortalProjectFileDetails.  # noqa: E501

        The date the file was authorized.  # noqa: E501

        :return: The authorized_date of this PortalProjectFileDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._authorized_date

    @authorized_date.setter
    def authorized_date(self, authorized_date):
        """Sets the authorized_date of this PortalProjectFileDetails.

        The date the file was authorized.  # noqa: E501

        :param authorized_date: The authorized_date of this PortalProjectFileDetails.  # noqa: E501
        :type: datetime
        """

        self._authorized_date = authorized_date

    @property
    def can_be_cancelled(self):
        """Gets the can_be_cancelled of this PortalProjectFileDetails.  # noqa: E501

        Indicates whether the file can be cancelled.  # noqa: E501

        :return: The can_be_cancelled of this PortalProjectFileDetails.  # noqa: E501
        :rtype: bool
        """
        return self._can_be_cancelled

    @can_be_cancelled.setter
    def can_be_cancelled(self, can_be_cancelled):
        """Sets the can_be_cancelled of this PortalProjectFileDetails.

        Indicates whether the file can be cancelled.  # noqa: E501

        :param can_be_cancelled: The can_be_cancelled of this PortalProjectFileDetails.  # noqa: E501
        :type: bool
        """

        self._can_be_cancelled = can_be_cancelled

    @property
    def cost(self):
        """Gets the cost of this PortalProjectFileDetails.  # noqa: E501

        The total cost for translating the file.  # noqa: E501

        :return: The cost of this PortalProjectFileDetails.  # noqa: E501
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this PortalProjectFileDetails.

        The total cost for translating the file.  # noqa: E501

        :param cost: The cost of this PortalProjectFileDetails.  # noqa: E501
        :type: float
        """

        self._cost = cost

    @property
    def cost_attributes(self):
        """Gets the cost_attributes of this PortalProjectFileDetails.  # noqa: E501

        Gets or sets the cost attributes.  # noqa: E501

        :return: The cost_attributes of this PortalProjectFileDetails.  # noqa: E501
        :rtype: list[PortalCostAttribute]
        """
        return self._cost_attributes

    @cost_attributes.setter
    def cost_attributes(self, cost_attributes):
        """Sets the cost_attributes of this PortalProjectFileDetails.

        Gets or sets the cost attributes.  # noqa: E501

        :param cost_attributes: The cost_attributes of this PortalProjectFileDetails.  # noqa: E501
        :type: list[PortalCostAttribute]
        """

        self._cost_attributes = cost_attributes

    @property
    def cost_bands(self):
        """Gets the cost_bands of this PortalProjectFileDetails.  # noqa: E501

        Gets or sets the cost bands associated with the file.  # noqa: E501

        :return: The cost_bands of this PortalProjectFileDetails.  # noqa: E501
        :rtype: list[PortalCostBand]
        """
        return self._cost_bands

    @cost_bands.setter
    def cost_bands(self, cost_bands):
        """Sets the cost_bands of this PortalProjectFileDetails.

        Gets or sets the cost bands associated with the file.  # noqa: E501

        :param cost_bands: The cost_bands of this PortalProjectFileDetails.  # noqa: E501
        :type: list[PortalCostBand]
        """

        self._cost_bands = cost_bands

    @property
    def cost_matrix_name(self):
        """Gets the cost_matrix_name of this PortalProjectFileDetails.  # noqa: E501

        The name of the cost model used to calculate the translation costs for the file.  # noqa: E501

        :return: The cost_matrix_name of this PortalProjectFileDetails.  # noqa: E501
        :rtype: str
        """
        return self._cost_matrix_name

    @cost_matrix_name.setter
    def cost_matrix_name(self, cost_matrix_name):
        """Sets the cost_matrix_name of this PortalProjectFileDetails.

        The name of the cost model used to calculate the translation costs for the file.  # noqa: E501

        :param cost_matrix_name: The cost_matrix_name of this PortalProjectFileDetails.  # noqa: E501
        :type: str
        """

        self._cost_matrix_name = cost_matrix_name

    @property
    def folder(self):
        """Gets the folder of this PortalProjectFileDetails.  # noqa: E501

        The relative path of the file established when the project is created from a zip file, a connector or an integration.  # noqa: E501

        :return: The folder of this PortalProjectFileDetails.  # noqa: E501
        :rtype: str
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this PortalProjectFileDetails.

        The relative path of the file established when the project is created from a zip file, a connector or an integration.  # noqa: E501

        :param folder: The folder of this PortalProjectFileDetails.  # noqa: E501
        :type: str
        """

        self._folder = folder

    @property
    def fuzzy_words(self):
        """Gets the fuzzy_words of this PortalProjectFileDetails.  # noqa: E501

        The total number of words for the file receiving a fuzzy match from the translation memory during preparation.  # noqa: E501

        :return: The fuzzy_words of this PortalProjectFileDetails.  # noqa: E501
        :rtype: int
        """
        return self._fuzzy_words

    @fuzzy_words.setter
    def fuzzy_words(self, fuzzy_words):
        """Sets the fuzzy_words of this PortalProjectFileDetails.

        The total number of words for the file receiving a fuzzy match from the translation memory during preparation.  # noqa: E501

        :param fuzzy_words: The fuzzy_words of this PortalProjectFileDetails.  # noqa: E501
        :type: int
        """

        self._fuzzy_words = fuzzy_words

    @property
    def hundred_words(self):
        """Gets the hundred_words of this PortalProjectFileDetails.  # noqa: E501

        The total number of words for the file receiving a one hundred percent match from the translation memory during preparation.  # noqa: E501

        :return: The hundred_words of this PortalProjectFileDetails.  # noqa: E501
        :rtype: int
        """
        return self._hundred_words

    @hundred_words.setter
    def hundred_words(self, hundred_words):
        """Sets the hundred_words of this PortalProjectFileDetails.

        The total number of words for the file receiving a one hundred percent match from the translation memory during preparation.  # noqa: E501

        :param hundred_words: The hundred_words of this PortalProjectFileDetails.  # noqa: E501
        :type: int
        """

        self._hundred_words = hundred_words

    @property
    def id(self):
        """Gets the id of this PortalProjectFileDetails.  # noqa: E501

        The unique identifider of the file in the associated target language.  # noqa: E501

        :return: The id of this PortalProjectFileDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PortalProjectFileDetails.

        The unique identifider of the file in the associated target language.  # noqa: E501

        :param id: The id of this PortalProjectFileDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def in_context_preview_status(self):
        """Gets the in_context_preview_status of this PortalProjectFileDetails.  # noqa: E501

        The status of the In-Context Review feature for the file. Values can be NotRequired, InProgress, AnnotatedFileDownloadFailed, AnnotatedFileDownloaded, PreviewCompleted  # noqa: E501

        :return: The in_context_preview_status of this PortalProjectFileDetails.  # noqa: E501
        :rtype: str
        """
        return self._in_context_preview_status

    @in_context_preview_status.setter
    def in_context_preview_status(self, in_context_preview_status):
        """Sets the in_context_preview_status of this PortalProjectFileDetails.

        The status of the In-Context Review feature for the file. Values can be NotRequired, InProgress, AnnotatedFileDownloadFailed, AnnotatedFileDownloaded, PreviewCompleted  # noqa: E501

        :param in_context_preview_status: The in_context_preview_status of this PortalProjectFileDetails.  # noqa: E501
        :type: str
        """

        self._in_context_preview_status = in_context_preview_status

    @property
    def locked_words(self):
        """Gets the locked_words of this PortalProjectFileDetails.  # noqa: E501

        The total number of words marked as locked during preparation.  # noqa: E501

        :return: The locked_words of this PortalProjectFileDetails.  # noqa: E501
        :rtype: int
        """
        return self._locked_words

    @locked_words.setter
    def locked_words(self, locked_words):
        """Sets the locked_words of this PortalProjectFileDetails.

        The total number of words marked as locked during preparation.  # noqa: E501

        :param locked_words: The locked_words of this PortalProjectFileDetails.  # noqa: E501
        :type: int
        """

        self._locked_words = locked_words

    @property
    def name(self):
        """Gets the name of this PortalProjectFileDetails.  # noqa: E501

        The name of the file, without any preceeding path information.  # noqa: E501

        :return: The name of this PortalProjectFileDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PortalProjectFileDetails.

        The name of the file, without any preceeding path information.  # noqa: E501

        :param name: The name of this PortalProjectFileDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def new_words(self):
        """Gets the new_words of this PortalProjectFileDetails.  # noqa: E501

        The total number of words for the file receiving no match from the translation memory during preparation.  # noqa: E501

        :return: The new_words of this PortalProjectFileDetails.  # noqa: E501
        :rtype: int
        """
        return self._new_words

    @new_words.setter
    def new_words(self, new_words):
        """Sets the new_words of this PortalProjectFileDetails.

        The total number of words for the file receiving no match from the translation memory during preparation.  # noqa: E501

        :param new_words: The new_words of this PortalProjectFileDetails.  # noqa: E501
        :type: int
        """

        self._new_words = new_words

    @property
    def owner(self):
        """Gets the owner of this PortalProjectFileDetails.  # noqa: E501


        :return: The owner of this PortalProjectFileDetails.  # noqa: E501
        :rtype: PortalOwner
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this PortalProjectFileDetails.


        :param owner: The owner of this PortalProjectFileDetails.  # noqa: E501
        :type: PortalOwner
        """

        self._owner = owner

    @property
    def perfect_match_words(self):
        """Gets the perfect_match_words of this PortalProjectFileDetails.  # noqa: E501

        The total number of words for the file receiving a pefect match from the translation memory during preparation.  # noqa: E501

        :return: The perfect_match_words of this PortalProjectFileDetails.  # noqa: E501
        :rtype: int
        """
        return self._perfect_match_words

    @perfect_match_words.setter
    def perfect_match_words(self, perfect_match_words):
        """Sets the perfect_match_words of this PortalProjectFileDetails.

        The total number of words for the file receiving a pefect match from the translation memory during preparation.  # noqa: E501

        :param perfect_match_words: The perfect_match_words of this PortalProjectFileDetails.  # noqa: E501
        :type: int
        """

        self._perfect_match_words = perfect_match_words

    @property
    def portal_reviewers(self):
        """Gets the portal_reviewers of this PortalProjectFileDetails.  # noqa: E501

        Gets or sets the review information.  # noqa: E501

        :return: The portal_reviewers of this PortalProjectFileDetails.  # noqa: E501
        :rtype: list[PortalReviewer]
        """
        return self._portal_reviewers

    @portal_reviewers.setter
    def portal_reviewers(self, portal_reviewers):
        """Sets the portal_reviewers of this PortalProjectFileDetails.

        Gets or sets the review information.  # noqa: E501

        :param portal_reviewers: The portal_reviewers of this PortalProjectFileDetails.  # noqa: E501
        :type: list[PortalReviewer]
        """

        self._portal_reviewers = portal_reviewers

    @property
    def portal_signoffers(self):
        """Gets the portal_signoffers of this PortalProjectFileDetails.  # noqa: E501

        Gets or sets the signoff information.  # noqa: E501

        :return: The portal_signoffers of this PortalProjectFileDetails.  # noqa: E501
        :rtype: list[PortalSignoffer]
        """
        return self._portal_signoffers

    @portal_signoffers.setter
    def portal_signoffers(self, portal_signoffers):
        """Sets the portal_signoffers of this PortalProjectFileDetails.

        Gets or sets the signoff information.  # noqa: E501

        :param portal_signoffers: The portal_signoffers of this PortalProjectFileDetails.  # noqa: E501
        :type: list[PortalSignoffer]
        """

        self._portal_signoffers = portal_signoffers

    @property
    def rejected(self):
        """Gets the rejected of this PortalProjectFileDetails.  # noqa: E501

        Gets or sets the task reject status.  # noqa: E501

        :return: The rejected of this PortalProjectFileDetails.  # noqa: E501
        :rtype: bool
        """
        return self._rejected

    @rejected.setter
    def rejected(self, rejected):
        """Sets the rejected of this PortalProjectFileDetails.

        Gets or sets the task reject status.  # noqa: E501

        :param rejected: The rejected of this PortalProjectFileDetails.  # noqa: E501
        :type: bool
        """

        self._rejected = rejected

    @property
    def repeated_words(self):
        """Gets the repeated_words of this PortalProjectFileDetails.  # noqa: E501

        The total number of words for the file considered to be repeated during preparation.  # noqa: E501

        :return: The repeated_words of this PortalProjectFileDetails.  # noqa: E501
        :rtype: int
        """
        return self._repeated_words

    @repeated_words.setter
    def repeated_words(self, repeated_words):
        """Sets the repeated_words of this PortalProjectFileDetails.

        The total number of words for the file considered to be repeated during preparation.  # noqa: E501

        :param repeated_words: The repeated_words of this PortalProjectFileDetails.  # noqa: E501
        :type: int
        """

        self._repeated_words = repeated_words

    @property
    def source_id(self):
        """Gets the source_id of this PortalProjectFileDetails.  # noqa: E501

        The unique identifier of the source file associated with the file.  # noqa: E501

        :return: The source_id of this PortalProjectFileDetails.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this PortalProjectFileDetails.

        The unique identifier of the source file associated with the file.  # noqa: E501

        :param source_id: The source_id of this PortalProjectFileDetails.  # noqa: E501
        :type: str
        """

        self._source_id = source_id

    @property
    def status(self):
        """Gets the status of this PortalProjectFileDetails.  # noqa: E501

        The status of the file within the workflow.0 = Preparing, 1 = ForApproval, 2 = InProgress, 3 = ForDownload, 4 = Completed, 5 = PartialDownload, 6 = InReview, 7 = Reviewed, 8 = InSignOff, 9 = SignedOff, 10 = ForVendorSelection, 11 = Cancelled, 12 = New  # noqa: E501

        :return: The status of this PortalProjectFileDetails.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PortalProjectFileDetails.

        The status of the file within the workflow.0 = Preparing, 1 = ForApproval, 2 = InProgress, 3 = ForDownload, 4 = Completed, 5 = PartialDownload, 6 = InReview, 7 = Reviewed, 8 = InSignOff, 9 = SignedOff, 10 = ForVendorSelection, 11 = Cancelled, 12 = New  # noqa: E501

        :param status: The status of this PortalProjectFileDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["Preparing", "ForApproval", "InProgress", "ForDownload", "Completed", "PartialDownload", "InReview", "Reviewed", "InSignOff", "SignedOff", "ForVendorSelection", "Cancelled", "New"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def status_detail(self):
        """Gets the status_detail of this PortalProjectFileDetails.  # noqa: E501

        Gets or sets the workflow status detail.  # noqa: E501

        :return: The status_detail of this PortalProjectFileDetails.  # noqa: E501
        :rtype: str
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        """Sets the status_detail of this PortalProjectFileDetails.

        Gets or sets the workflow status detail.  # noqa: E501

        :param status_detail: The status_detail of this PortalProjectFileDetails.  # noqa: E501
        :type: str
        """

        self._status_detail = status_detail

    @property
    def status_id(self):
        """Gets the status_id of this PortalProjectFileDetails.  # noqa: E501

        Gets or sets the workflow stage status id.  # noqa: E501

        :return: The status_id of this PortalProjectFileDetails.  # noqa: E501
        :rtype: str
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        """Sets the status_id of this PortalProjectFileDetails.

        Gets or sets the workflow stage status id.  # noqa: E501

        :param status_id: The status_id of this PortalProjectFileDetails.  # noqa: E501
        :type: str
        """

        self._status_id = status_id

    @property
    def status_type(self):
        """Gets the status_type of this PortalProjectFileDetails.  # noqa: E501

        Gets or sets the workflow status type.  # noqa: E501

        :return: The status_type of this PortalProjectFileDetails.  # noqa: E501
        :rtype: str
        """
        return self._status_type

    @status_type.setter
    def status_type(self, status_type):
        """Sets the status_type of this PortalProjectFileDetails.

        Gets or sets the workflow status type.  # noqa: E501

        :param status_type: The status_type of this PortalProjectFileDetails.  # noqa: E501
        :type: str
        """

        self._status_type = status_type

    @property
    def target_language(self):
        """Gets the target_language of this PortalProjectFileDetails.  # noqa: E501


        :return: The target_language of this PortalProjectFileDetails.  # noqa: E501
        :rtype: PortalLanguage
        """
        return self._target_language

    @target_language.setter
    def target_language(self, target_language):
        """Sets the target_language of this PortalProjectFileDetails.


        :param target_language: The target_language of this PortalProjectFileDetails.  # noqa: E501
        :type: PortalLanguage
        """

        self._target_language = target_language

    @property
    def task_id(self):
        """Gets the task_id of this PortalProjectFileDetails.  # noqa: E501

        Gets or sets the identifier.  # noqa: E501

        :return: The task_id of this PortalProjectFileDetails.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this PortalProjectFileDetails.

        Gets or sets the identifier.  # noqa: E501

        :param task_id: The task_id of this PortalProjectFileDetails.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def tm_leverage(self):
        """Gets the tm_leverage of this PortalProjectFileDetails.  # noqa: E501

        Gets or sets the tm leverage.  # noqa: E501

        :return: The tm_leverage of this PortalProjectFileDetails.  # noqa: E501
        :rtype: float
        """
        return self._tm_leverage

    @tm_leverage.setter
    def tm_leverage(self, tm_leverage):
        """Sets the tm_leverage of this PortalProjectFileDetails.

        Gets or sets the tm leverage.  # noqa: E501

        :param tm_leverage: The tm_leverage of this PortalProjectFileDetails.  # noqa: E501
        :type: float
        """

        self._tm_leverage = tm_leverage

    @property
    def tm_savings(self):
        """Gets the tm_savings of this PortalProjectFileDetails.  # noqa: E501

        Gets or sets the tm savings.  # noqa: E501

        :return: The tm_savings of this PortalProjectFileDetails.  # noqa: E501
        :rtype: float
        """
        return self._tm_savings

    @tm_savings.setter
    def tm_savings(self, tm_savings):
        """Sets the tm_savings of this PortalProjectFileDetails.

        Gets or sets the tm savings.  # noqa: E501

        :param tm_savings: The tm_savings of this PortalProjectFileDetails.  # noqa: E501
        :type: float
        """

        self._tm_savings = tm_savings

    @property
    def total_words(self):
        """Gets the total_words of this PortalProjectFileDetails.  # noqa: E501

        Gets the total words.  # noqa: E501

        :return: The total_words of this PortalProjectFileDetails.  # noqa: E501
        :rtype: int
        """
        return self._total_words

    @total_words.setter
    def total_words(self, total_words):
        """Sets the total_words of this PortalProjectFileDetails.

        Gets the total words.  # noqa: E501

        :param total_words: The total_words of this PortalProjectFileDetails.  # noqa: E501
        :type: int
        """

        self._total_words = total_words

    @property
    def workflow_attributes(self):
        """Gets the workflow_attributes of this PortalProjectFileDetails.  # noqa: E501

        Gets or sets the workflow attributes.  # noqa: E501

        :return: The workflow_attributes of this PortalProjectFileDetails.  # noqa: E501
        :rtype: list[PortalWorkflowAttribute]
        """
        return self._workflow_attributes

    @workflow_attributes.setter
    def workflow_attributes(self, workflow_attributes):
        """Sets the workflow_attributes of this PortalProjectFileDetails.

        Gets or sets the workflow attributes.  # noqa: E501

        :param workflow_attributes: The workflow_attributes of this PortalProjectFileDetails.  # noqa: E501
        :type: list[PortalWorkflowAttribute]
        """

        self._workflow_attributes = workflow_attributes

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
        if issubclass(PortalProjectFileDetails, dict):
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
        if not isinstance(other, PortalProjectFileDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
