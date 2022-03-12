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

class PortalProjectListEntry(object):
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
        'authorized_date': 'datetime',
        'can_be_cancelled': 'bool',
        'cost': 'float',
        'cost_details': 'list[PortalProjectCostDetail]',
        'created_by_user_id': 'str',
        'created_by_user_name': 'str',
        'created_date': 'datetime',
        'currency_info': 'PortalCurrency',
        'delivered_date': 'datetime',
        'delivery_estimate': 'datetime',
        'description': 'str',
        'due_date': 'datetime',
        'duration_hours': 'int',
        'fuzzy_words': 'int',
        'has_approval_step': 'bool',
        'has_multiple_batches': 'bool',
        'has_reference_files': 'bool',
        'hundred_words': 'int',
        'id': 'str',
        'languages': 'int',
        'locked_words': 'int',
        'metadata': 'list[PortalMetadata]',
        'name': 'str',
        'new_words': 'int',
        'percent_complete': 'int',
        'perfect_match_words': 'int',
        'project_group_guid': 'str',
        'project_group_id': 'str',
        'project_group_name': 'str',
        'project_options_id': 'str',
        'project_options_localized_name': 'str',
        'project_options_name': 'str',
        'project_type': 'str',
        'provider_project_id': 'str',
        'repeated_words': 'int',
        'scope_option_id': 'str',
        'scope_option_name': 'str',
        'source_files': 'int',
        'source_langauge': 'PortalLanguage',
        'source_words': 'int',
        'started_batches': 'int',
        'status': 'str',
        'target_languages': 'list[PortalLanguage]',
        'tm_savings': 'float',
        'vendor_costs': 'list[PortalProjectVendorCost]',
        'vendor_id': 'str',
        'vendor_name': 'str',
        'word_count': 'int'
    }

    attribute_map = {
        'authorized_date': 'AuthorizedDate',
        'can_be_cancelled': 'CanBeCancelled',
        'cost': 'Cost',
        'cost_details': 'CostDetails',
        'created_by_user_id': 'CreatedByUserId',
        'created_by_user_name': 'CreatedByUserName',
        'created_date': 'CreatedDate',
        'currency_info': 'CurrencyInfo',
        'delivered_date': 'DeliveredDate',
        'delivery_estimate': 'DeliveryEstimate',
        'description': 'Description',
        'due_date': 'DueDate',
        'duration_hours': 'DurationHours',
        'fuzzy_words': 'FuzzyWords',
        'has_approval_step': 'HasApprovalStep',
        'has_multiple_batches': 'HasMultipleBatches',
        'has_reference_files': 'HasReferenceFiles',
        'hundred_words': 'HundredWords',
        'id': 'Id',
        'languages': 'Languages',
        'locked_words': 'LockedWords',
        'metadata': 'Metadata',
        'name': 'Name',
        'new_words': 'NewWords',
        'percent_complete': 'PercentComplete',
        'perfect_match_words': 'PerfectMatchWords',
        'project_group_guid': 'ProjectGroupGuid',
        'project_group_id': 'ProjectGroupId',
        'project_group_name': 'ProjectGroupName',
        'project_options_id': 'ProjectOptionsId',
        'project_options_localized_name': 'ProjectOptionsLocalizedName',
        'project_options_name': 'ProjectOptionsName',
        'project_type': 'ProjectType',
        'provider_project_id': 'ProviderProjectId',
        'repeated_words': 'RepeatedWords',
        'scope_option_id': 'ScopeOptionId',
        'scope_option_name': 'ScopeOptionName',
        'source_files': 'SourceFiles',
        'source_langauge': 'SourceLangauge',
        'source_words': 'SourceWords',
        'started_batches': 'StartedBatches',
        'status': 'Status',
        'target_languages': 'TargetLanguages',
        'tm_savings': 'TMSavings',
        'vendor_costs': 'VendorCosts',
        'vendor_id': 'VendorId',
        'vendor_name': 'VendorName',
        'word_count': 'WordCount'
    }

    def __init__(self, authorized_date=None, can_be_cancelled=None, cost=None, cost_details=None, created_by_user_id=None, created_by_user_name=None, created_date=None, currency_info=None, delivered_date=None, delivery_estimate=None, description=None, due_date=None, duration_hours=None, fuzzy_words=None, has_approval_step=None, has_multiple_batches=None, has_reference_files=None, hundred_words=None, id=None, languages=None, locked_words=None, metadata=None, name=None, new_words=None, percent_complete=None, perfect_match_words=None, project_group_guid=None, project_group_id=None, project_group_name=None, project_options_id=None, project_options_localized_name=None, project_options_name=None, project_type=None, provider_project_id=None, repeated_words=None, scope_option_id=None, scope_option_name=None, source_files=None, source_langauge=None, source_words=None, started_batches=None, status=None, target_languages=None, tm_savings=None, vendor_costs=None, vendor_id=None, vendor_name=None, word_count=None):  # noqa: E501
        """PortalProjectListEntry - a model defined in Swagger"""  # noqa: E501
        self._authorized_date = None
        self._can_be_cancelled = None
        self._cost = None
        self._cost_details = None
        self._created_by_user_id = None
        self._created_by_user_name = None
        self._created_date = None
        self._currency_info = None
        self._delivered_date = None
        self._delivery_estimate = None
        self._description = None
        self._due_date = None
        self._duration_hours = None
        self._fuzzy_words = None
        self._has_approval_step = None
        self._has_multiple_batches = None
        self._has_reference_files = None
        self._hundred_words = None
        self._id = None
        self._languages = None
        self._locked_words = None
        self._metadata = None
        self._name = None
        self._new_words = None
        self._percent_complete = None
        self._perfect_match_words = None
        self._project_group_guid = None
        self._project_group_id = None
        self._project_group_name = None
        self._project_options_id = None
        self._project_options_localized_name = None
        self._project_options_name = None
        self._project_type = None
        self._provider_project_id = None
        self._repeated_words = None
        self._scope_option_id = None
        self._scope_option_name = None
        self._source_files = None
        self._source_langauge = None
        self._source_words = None
        self._started_batches = None
        self._status = None
        self._target_languages = None
        self._tm_savings = None
        self._vendor_costs = None
        self._vendor_id = None
        self._vendor_name = None
        self._word_count = None
        self.discriminator = None
        if authorized_date is not None:
            self.authorized_date = authorized_date
        if can_be_cancelled is not None:
            self.can_be_cancelled = can_be_cancelled
        if cost is not None:
            self.cost = cost
        if cost_details is not None:
            self.cost_details = cost_details
        if created_by_user_id is not None:
            self.created_by_user_id = created_by_user_id
        if created_by_user_name is not None:
            self.created_by_user_name = created_by_user_name
        if created_date is not None:
            self.created_date = created_date
        if currency_info is not None:
            self.currency_info = currency_info
        if delivered_date is not None:
            self.delivered_date = delivered_date
        if delivery_estimate is not None:
            self.delivery_estimate = delivery_estimate
        if description is not None:
            self.description = description
        if due_date is not None:
            self.due_date = due_date
        if duration_hours is not None:
            self.duration_hours = duration_hours
        if fuzzy_words is not None:
            self.fuzzy_words = fuzzy_words
        if has_approval_step is not None:
            self.has_approval_step = has_approval_step
        if has_multiple_batches is not None:
            self.has_multiple_batches = has_multiple_batches
        if has_reference_files is not None:
            self.has_reference_files = has_reference_files
        if hundred_words is not None:
            self.hundred_words = hundred_words
        if id is not None:
            self.id = id
        if languages is not None:
            self.languages = languages
        if locked_words is not None:
            self.locked_words = locked_words
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if new_words is not None:
            self.new_words = new_words
        if percent_complete is not None:
            self.percent_complete = percent_complete
        if perfect_match_words is not None:
            self.perfect_match_words = perfect_match_words
        if project_group_guid is not None:
            self.project_group_guid = project_group_guid
        if project_group_id is not None:
            self.project_group_id = project_group_id
        if project_group_name is not None:
            self.project_group_name = project_group_name
        if project_options_id is not None:
            self.project_options_id = project_options_id
        if project_options_localized_name is not None:
            self.project_options_localized_name = project_options_localized_name
        if project_options_name is not None:
            self.project_options_name = project_options_name
        if project_type is not None:
            self.project_type = project_type
        if provider_project_id is not None:
            self.provider_project_id = provider_project_id
        if repeated_words is not None:
            self.repeated_words = repeated_words
        if scope_option_id is not None:
            self.scope_option_id = scope_option_id
        if scope_option_name is not None:
            self.scope_option_name = scope_option_name
        if source_files is not None:
            self.source_files = source_files
        if source_langauge is not None:
            self.source_langauge = source_langauge
        if source_words is not None:
            self.source_words = source_words
        if started_batches is not None:
            self.started_batches = started_batches
        if status is not None:
            self.status = status
        if target_languages is not None:
            self.target_languages = target_languages
        if tm_savings is not None:
            self.tm_savings = tm_savings
        if vendor_costs is not None:
            self.vendor_costs = vendor_costs
        if vendor_id is not None:
            self.vendor_id = vendor_id
        if vendor_name is not None:
            self.vendor_name = vendor_name
        if word_count is not None:
            self.word_count = word_count

    @property
    def authorized_date(self):
        """Gets the authorized_date of this PortalProjectListEntry.  # noqa: E501

        Gets the date and time, in UTC, that the project was approved.  # noqa: E501

        :return: The authorized_date of this PortalProjectListEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._authorized_date

    @authorized_date.setter
    def authorized_date(self, authorized_date):
        """Sets the authorized_date of this PortalProjectListEntry.

        Gets the date and time, in UTC, that the project was approved.  # noqa: E501

        :param authorized_date: The authorized_date of this PortalProjectListEntry.  # noqa: E501
        :type: datetime
        """

        self._authorized_date = authorized_date

    @property
    def can_be_cancelled(self):
        """Gets the can_be_cancelled of this PortalProjectListEntry.  # noqa: E501

        Indicates whether the project can be cancelled, based upon its current status and the current user's permissions.  # noqa: E501

        :return: The can_be_cancelled of this PortalProjectListEntry.  # noqa: E501
        :rtype: bool
        """
        return self._can_be_cancelled

    @can_be_cancelled.setter
    def can_be_cancelled(self, can_be_cancelled):
        """Sets the can_be_cancelled of this PortalProjectListEntry.

        Indicates whether the project can be cancelled, based upon its current status and the current user's permissions.  # noqa: E501

        :param can_be_cancelled: The can_be_cancelled of this PortalProjectListEntry.  # noqa: E501
        :type: bool
        """

        self._can_be_cancelled = can_be_cancelled

    @property
    def cost(self):
        """Gets the cost of this PortalProjectListEntry.  # noqa: E501

        The total cost of the project.  # noqa: E501

        :return: The cost of this PortalProjectListEntry.  # noqa: E501
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this PortalProjectListEntry.

        The total cost of the project.  # noqa: E501

        :param cost: The cost of this PortalProjectListEntry.  # noqa: E501
        :type: float
        """

        self._cost = cost

    @property
    def cost_details(self):
        """Gets the cost_details of this PortalProjectListEntry.  # noqa: E501

        The project level costs  # noqa: E501

        :return: The cost_details of this PortalProjectListEntry.  # noqa: E501
        :rtype: list[PortalProjectCostDetail]
        """
        return self._cost_details

    @cost_details.setter
    def cost_details(self, cost_details):
        """Sets the cost_details of this PortalProjectListEntry.

        The project level costs  # noqa: E501

        :param cost_details: The cost_details of this PortalProjectListEntry.  # noqa: E501
        :type: list[PortalProjectCostDetail]
        """

        self._cost_details = cost_details

    @property
    def created_by_user_id(self):
        """Gets the created_by_user_id of this PortalProjectListEntry.  # noqa: E501

        The Managed Translation Id of the user who created the project.  # noqa: E501

        :return: The created_by_user_id of this PortalProjectListEntry.  # noqa: E501
        :rtype: str
        """
        return self._created_by_user_id

    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id):
        """Sets the created_by_user_id of this PortalProjectListEntry.

        The Managed Translation Id of the user who created the project.  # noqa: E501

        :param created_by_user_id: The created_by_user_id of this PortalProjectListEntry.  # noqa: E501
        :type: str
        """

        self._created_by_user_id = created_by_user_id

    @property
    def created_by_user_name(self):
        """Gets the created_by_user_name of this PortalProjectListEntry.  # noqa: E501

        The display name or username of the user who created the project.  # noqa: E501

        :return: The created_by_user_name of this PortalProjectListEntry.  # noqa: E501
        :rtype: str
        """
        return self._created_by_user_name

    @created_by_user_name.setter
    def created_by_user_name(self, created_by_user_name):
        """Sets the created_by_user_name of this PortalProjectListEntry.

        The display name or username of the user who created the project.  # noqa: E501

        :param created_by_user_name: The created_by_user_name of this PortalProjectListEntry.  # noqa: E501
        :type: str
        """

        self._created_by_user_name = created_by_user_name

    @property
    def created_date(self):
        """Gets the created_date of this PortalProjectListEntry.  # noqa: E501

        The date and time, in UTC, the project was created.  # noqa: E501

        :return: The created_date of this PortalProjectListEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this PortalProjectListEntry.

        The date and time, in UTC, the project was created.  # noqa: E501

        :param created_date: The created_date of this PortalProjectListEntry.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def currency_info(self):
        """Gets the currency_info of this PortalProjectListEntry.  # noqa: E501


        :return: The currency_info of this PortalProjectListEntry.  # noqa: E501
        :rtype: PortalCurrency
        """
        return self._currency_info

    @currency_info.setter
    def currency_info(self, currency_info):
        """Sets the currency_info of this PortalProjectListEntry.


        :param currency_info: The currency_info of this PortalProjectListEntry.  # noqa: E501
        :type: PortalCurrency
        """

        self._currency_info = currency_info

    @property
    def delivered_date(self):
        """Gets the delivered_date of this PortalProjectListEntry.  # noqa: E501

        The date and time, in UTC, the project was delivered and ready to download.  # noqa: E501

        :return: The delivered_date of this PortalProjectListEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._delivered_date

    @delivered_date.setter
    def delivered_date(self, delivered_date):
        """Sets the delivered_date of this PortalProjectListEntry.

        The date and time, in UTC, the project was delivered and ready to download.  # noqa: E501

        :param delivered_date: The delivered_date of this PortalProjectListEntry.  # noqa: E501
        :type: datetime
        """

        self._delivered_date = delivered_date

    @property
    def delivery_estimate(self):
        """Gets the delivery_estimate of this PortalProjectListEntry.  # noqa: E501

        Gets the estimated delivery date, calculated from the estimated Duration at the time the project was approved.  # noqa: E501

        :return: The delivery_estimate of this PortalProjectListEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._delivery_estimate

    @delivery_estimate.setter
    def delivery_estimate(self, delivery_estimate):
        """Sets the delivery_estimate of this PortalProjectListEntry.

        Gets the estimated delivery date, calculated from the estimated Duration at the time the project was approved.  # noqa: E501

        :param delivery_estimate: The delivery_estimate of this PortalProjectListEntry.  # noqa: E501
        :type: datetime
        """

        self._delivery_estimate = delivery_estimate

    @property
    def description(self):
        """Gets the description of this PortalProjectListEntry.  # noqa: E501

        The project description, provided during project creation.  # noqa: E501

        :return: The description of this PortalProjectListEntry.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PortalProjectListEntry.

        The project description, provided during project creation.  # noqa: E501

        :param description: The description of this PortalProjectListEntry.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def due_date(self):
        """Gets the due_date of this PortalProjectListEntry.  # noqa: E501

        The date and time, in UTC, that the project should be completed, specified during project creation.  # noqa: E501

        :return: The due_date of this PortalProjectListEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this PortalProjectListEntry.

        The date and time, in UTC, that the project should be completed, specified during project creation.  # noqa: E501

        :param due_date: The due_date of this PortalProjectListEntry.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def duration_hours(self):
        """Gets the duration_hours of this PortalProjectListEntry.  # noqa: E501

        Gets the Estimated Duration in hours required to complete the project.  # noqa: E501

        :return: The duration_hours of this PortalProjectListEntry.  # noqa: E501
        :rtype: int
        """
        return self._duration_hours

    @duration_hours.setter
    def duration_hours(self, duration_hours):
        """Sets the duration_hours of this PortalProjectListEntry.

        Gets the Estimated Duration in hours required to complete the project.  # noqa: E501

        :param duration_hours: The duration_hours of this PortalProjectListEntry.  # noqa: E501
        :type: int
        """

        self._duration_hours = duration_hours

    @property
    def fuzzy_words(self):
        """Gets the fuzzy_words of this PortalProjectListEntry.  # noqa: E501

        The total number of words receiving a fuzzy match from the translation memory during preparation.  # noqa: E501

        :return: The fuzzy_words of this PortalProjectListEntry.  # noqa: E501
        :rtype: int
        """
        return self._fuzzy_words

    @fuzzy_words.setter
    def fuzzy_words(self, fuzzy_words):
        """Sets the fuzzy_words of this PortalProjectListEntry.

        The total number of words receiving a fuzzy match from the translation memory during preparation.  # noqa: E501

        :param fuzzy_words: The fuzzy_words of this PortalProjectListEntry.  # noqa: E501
        :type: int
        """

        self._fuzzy_words = fuzzy_words

    @property
    def has_approval_step(self):
        """Gets the has_approval_step of this PortalProjectListEntry.  # noqa: E501

        Does the workflow used to create this project contains a customer qoute reviea step  # noqa: E501

        :return: The has_approval_step of this PortalProjectListEntry.  # noqa: E501
        :rtype: bool
        """
        return self._has_approval_step

    @has_approval_step.setter
    def has_approval_step(self, has_approval_step):
        """Sets the has_approval_step of this PortalProjectListEntry.

        Does the workflow used to create this project contains a customer qoute reviea step  # noqa: E501

        :param has_approval_step: The has_approval_step of this PortalProjectListEntry.  # noqa: E501
        :type: bool
        """

        self._has_approval_step = has_approval_step

    @property
    def has_multiple_batches(self):
        """Gets the has_multiple_batches of this PortalProjectListEntry.  # noqa: E501

        Indicates whether the project has multiple started batches.  # noqa: E501

        :return: The has_multiple_batches of this PortalProjectListEntry.  # noqa: E501
        :rtype: bool
        """
        return self._has_multiple_batches

    @has_multiple_batches.setter
    def has_multiple_batches(self, has_multiple_batches):
        """Sets the has_multiple_batches of this PortalProjectListEntry.

        Indicates whether the project has multiple started batches.  # noqa: E501

        :param has_multiple_batches: The has_multiple_batches of this PortalProjectListEntry.  # noqa: E501
        :type: bool
        """

        self._has_multiple_batches = has_multiple_batches

    @property
    def has_reference_files(self):
        """Gets the has_reference_files of this PortalProjectListEntry.  # noqa: E501

        Indicates whether the project has any associated reference files.  # noqa: E501

        :return: The has_reference_files of this PortalProjectListEntry.  # noqa: E501
        :rtype: bool
        """
        return self._has_reference_files

    @has_reference_files.setter
    def has_reference_files(self, has_reference_files):
        """Sets the has_reference_files of this PortalProjectListEntry.

        Indicates whether the project has any associated reference files.  # noqa: E501

        :param has_reference_files: The has_reference_files of this PortalProjectListEntry.  # noqa: E501
        :type: bool
        """

        self._has_reference_files = has_reference_files

    @property
    def hundred_words(self):
        """Gets the hundred_words of this PortalProjectListEntry.  # noqa: E501

        The total number of words receiving a one hundred percent match from the translation memory during preparation.  # noqa: E501

        :return: The hundred_words of this PortalProjectListEntry.  # noqa: E501
        :rtype: int
        """
        return self._hundred_words

    @hundred_words.setter
    def hundred_words(self, hundred_words):
        """Sets the hundred_words of this PortalProjectListEntry.

        The total number of words receiving a one hundred percent match from the translation memory during preparation.  # noqa: E501

        :param hundred_words: The hundred_words of this PortalProjectListEntry.  # noqa: E501
        :type: int
        """

        self._hundred_words = hundred_words

    @property
    def id(self):
        """Gets the id of this PortalProjectListEntry.  # noqa: E501

        The unique identifier of the project, allocated when the project was created.  # noqa: E501

        :return: The id of this PortalProjectListEntry.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PortalProjectListEntry.

        The unique identifier of the project, allocated when the project was created.  # noqa: E501

        :param id: The id of this PortalProjectListEntry.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def languages(self):
        """Gets the languages of this PortalProjectListEntry.  # noqa: E501

        Calculates the number of languages (pairs) associated with the project.  # noqa: E501

        :return: The languages of this PortalProjectListEntry.  # noqa: E501
        :rtype: int
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """Sets the languages of this PortalProjectListEntry.

        Calculates the number of languages (pairs) associated with the project.  # noqa: E501

        :param languages: The languages of this PortalProjectListEntry.  # noqa: E501
        :type: int
        """

        self._languages = languages

    @property
    def locked_words(self):
        """Gets the locked_words of this PortalProjectListEntry.  # noqa: E501

        The total number of words considered to be repeated during preparation.  # noqa: E501

        :return: The locked_words of this PortalProjectListEntry.  # noqa: E501
        :rtype: int
        """
        return self._locked_words

    @locked_words.setter
    def locked_words(self, locked_words):
        """Sets the locked_words of this PortalProjectListEntry.

        The total number of words considered to be repeated during preparation.  # noqa: E501

        :param locked_words: The locked_words of this PortalProjectListEntry.  # noqa: E501
        :type: int
        """

        self._locked_words = locked_words

    @property
    def metadata(self):
        """Gets the metadata of this PortalProjectListEntry.  # noqa: E501

        The collection of project specific custom attributes (metadata) associated with the project.  # noqa: E501

        :return: The metadata of this PortalProjectListEntry.  # noqa: E501
        :rtype: list[PortalMetadata]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PortalProjectListEntry.

        The collection of project specific custom attributes (metadata) associated with the project.  # noqa: E501

        :param metadata: The metadata of this PortalProjectListEntry.  # noqa: E501
        :type: list[PortalMetadata]
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this PortalProjectListEntry.  # noqa: E501

        The name of the project, provided during project creation.  # noqa: E501

        :return: The name of this PortalProjectListEntry.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PortalProjectListEntry.

        The name of the project, provided during project creation.  # noqa: E501

        :param name: The name of this PortalProjectListEntry.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def new_words(self):
        """Gets the new_words of this PortalProjectListEntry.  # noqa: E501

        The total number of words receiving no match from the translation memory during preparation.  # noqa: E501

        :return: The new_words of this PortalProjectListEntry.  # noqa: E501
        :rtype: int
        """
        return self._new_words

    @new_words.setter
    def new_words(self, new_words):
        """Sets the new_words of this PortalProjectListEntry.

        The total number of words receiving no match from the translation memory during preparation.  # noqa: E501

        :param new_words: The new_words of this PortalProjectListEntry.  # noqa: E501
        :type: int
        """

        self._new_words = new_words

    @property
    def percent_complete(self):
        """Gets the percent_complete of this PortalProjectListEntry.  # noqa: E501

        A summary value indicating the approximate completion percentage of the project. Often this value is calculated from the number of files which have reached the ForDownload status.  # noqa: E501

        :return: The percent_complete of this PortalProjectListEntry.  # noqa: E501
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """Sets the percent_complete of this PortalProjectListEntry.

        A summary value indicating the approximate completion percentage of the project. Often this value is calculated from the number of files which have reached the ForDownload status.  # noqa: E501

        :param percent_complete: The percent_complete of this PortalProjectListEntry.  # noqa: E501
        :type: int
        """

        self._percent_complete = percent_complete

    @property
    def perfect_match_words(self):
        """Gets the perfect_match_words of this PortalProjectListEntry.  # noqa: E501

        The total number of words receiving a perfect or contextual match from the translation memory during preparation.  # noqa: E501

        :return: The perfect_match_words of this PortalProjectListEntry.  # noqa: E501
        :rtype: int
        """
        return self._perfect_match_words

    @perfect_match_words.setter
    def perfect_match_words(self, perfect_match_words):
        """Sets the perfect_match_words of this PortalProjectListEntry.

        The total number of words receiving a perfect or contextual match from the translation memory during preparation.  # noqa: E501

        :param perfect_match_words: The perfect_match_words of this PortalProjectListEntry.  # noqa: E501
        :type: int
        """

        self._perfect_match_words = perfect_match_words

    @property
    def project_group_guid(self):
        """Gets the project_group_guid of this PortalProjectListEntry.  # noqa: E501

        The unique identifier of the project group to which the project belongs.  # noqa: E501

        :return: The project_group_guid of this PortalProjectListEntry.  # noqa: E501
        :rtype: str
        """
        return self._project_group_guid

    @project_group_guid.setter
    def project_group_guid(self, project_group_guid):
        """Sets the project_group_guid of this PortalProjectListEntry.

        The unique identifier of the project group to which the project belongs.  # noqa: E501

        :param project_group_guid: The project_group_guid of this PortalProjectListEntry.  # noqa: E501
        :type: str
        """

        self._project_group_guid = project_group_guid

    @property
    def project_group_id(self):
        """Gets the project_group_id of this PortalProjectListEntry.  # noqa: E501

        The unique int identifier of the project group to which the project belongs.  # noqa: E501

        :return: The project_group_id of this PortalProjectListEntry.  # noqa: E501
        :rtype: str
        """
        return self._project_group_id

    @project_group_id.setter
    def project_group_id(self, project_group_id):
        """Sets the project_group_id of this PortalProjectListEntry.

        The unique int identifier of the project group to which the project belongs.  # noqa: E501

        :param project_group_id: The project_group_id of this PortalProjectListEntry.  # noqa: E501
        :type: str
        """

        self._project_group_id = project_group_id

    @property
    def project_group_name(self):
        """Gets the project_group_name of this PortalProjectListEntry.  # noqa: E501

        The name of the project group to which the project belongs.  # noqa: E501

        :return: The project_group_name of this PortalProjectListEntry.  # noqa: E501
        :rtype: str
        """
        return self._project_group_name

    @project_group_name.setter
    def project_group_name(self, project_group_name):
        """Sets the project_group_name of this PortalProjectListEntry.

        The name of the project group to which the project belongs.  # noqa: E501

        :param project_group_name: The project_group_name of this PortalProjectListEntry.  # noqa: E501
        :type: str
        """

        self._project_group_name = project_group_name

    @property
    def project_options_id(self):
        """Gets the project_options_id of this PortalProjectListEntry.  # noqa: E501

        The unique identifier of the Project Option chosen during project creation.  # noqa: E501

        :return: The project_options_id of this PortalProjectListEntry.  # noqa: E501
        :rtype: str
        """
        return self._project_options_id

    @project_options_id.setter
    def project_options_id(self, project_options_id):
        """Sets the project_options_id of this PortalProjectListEntry.

        The unique identifier of the Project Option chosen during project creation.  # noqa: E501

        :param project_options_id: The project_options_id of this PortalProjectListEntry.  # noqa: E501
        :type: str
        """

        self._project_options_id = project_options_id

    @property
    def project_options_localized_name(self):
        """Gets the project_options_localized_name of this PortalProjectListEntry.  # noqa: E501

        The localized name of the Project Option chosen during project creation, assuming Managed Translation has a localized version of the text, otherwise the original native language text.  # noqa: E501

        :return: The project_options_localized_name of this PortalProjectListEntry.  # noqa: E501
        :rtype: str
        """
        return self._project_options_localized_name

    @project_options_localized_name.setter
    def project_options_localized_name(self, project_options_localized_name):
        """Sets the project_options_localized_name of this PortalProjectListEntry.

        The localized name of the Project Option chosen during project creation, assuming Managed Translation has a localized version of the text, otherwise the original native language text.  # noqa: E501

        :param project_options_localized_name: The project_options_localized_name of this PortalProjectListEntry.  # noqa: E501
        :type: str
        """

        self._project_options_localized_name = project_options_localized_name

    @property
    def project_options_name(self):
        """Gets the project_options_name of this PortalProjectListEntry.  # noqa: E501

        The name of the project option selected when creating the project.  # noqa: E501

        :return: The project_options_name of this PortalProjectListEntry.  # noqa: E501
        :rtype: str
        """
        return self._project_options_name

    @project_options_name.setter
    def project_options_name(self, project_options_name):
        """Sets the project_options_name of this PortalProjectListEntry.

        The name of the project option selected when creating the project.  # noqa: E501

        :param project_options_name: The project_options_name of this PortalProjectListEntry.  # noqa: E501
        :type: str
        """

        self._project_options_name = project_options_name

    @property
    def project_type(self):
        """Gets the project_type of this PortalProjectListEntry.  # noqa: E501

        Indicates whether the project was created using Managed Translation (manual) or a legacy integration (automatic) with the backend platform.0 = Manual, 1 = Automatic  # noqa: E501

        :return: The project_type of this PortalProjectListEntry.  # noqa: E501
        :rtype: str
        """
        return self._project_type

    @project_type.setter
    def project_type(self, project_type):
        """Sets the project_type of this PortalProjectListEntry.

        Indicates whether the project was created using Managed Translation (manual) or a legacy integration (automatic) with the backend platform.0 = Manual, 1 = Automatic  # noqa: E501

        :param project_type: The project_type of this PortalProjectListEntry.  # noqa: E501
        :type: str
        """
        allowed_values = ["Manual", "Automatic"]  # noqa: E501
        if project_type not in allowed_values:
            raise ValueError(
                "Invalid value for `project_type` ({0}), must be one of {1}"  # noqa: E501
                .format(project_type, allowed_values)
            )

        self._project_type = project_type

    @property
    def provider_project_id(self):
        """Gets the provider_project_id of this PortalProjectListEntry.  # noqa: E501

        The identifier for the project used by the underlying platform.  # noqa: E501

        :return: The provider_project_id of this PortalProjectListEntry.  # noqa: E501
        :rtype: str
        """
        return self._provider_project_id

    @provider_project_id.setter
    def provider_project_id(self, provider_project_id):
        """Sets the provider_project_id of this PortalProjectListEntry.

        The identifier for the project used by the underlying platform.  # noqa: E501

        :param provider_project_id: The provider_project_id of this PortalProjectListEntry.  # noqa: E501
        :type: str
        """

        self._provider_project_id = provider_project_id

    @property
    def repeated_words(self):
        """Gets the repeated_words of this PortalProjectListEntry.  # noqa: E501

        The total number of words considered to be repeated during preparation.  # noqa: E501

        :return: The repeated_words of this PortalProjectListEntry.  # noqa: E501
        :rtype: int
        """
        return self._repeated_words

    @repeated_words.setter
    def repeated_words(self, repeated_words):
        """Sets the repeated_words of this PortalProjectListEntry.

        The total number of words considered to be repeated during preparation.  # noqa: E501

        :param repeated_words: The repeated_words of this PortalProjectListEntry.  # noqa: E501
        :type: int
        """

        self._repeated_words = repeated_words

    @property
    def scope_option_id(self):
        """Gets the scope_option_id of this PortalProjectListEntry.  # noqa: E501

        The unique identifier of the scope at which the project was created. A scope may have a different meaning             on different underlying platforms. In Translation Management System, a Scope corresponds to an Organization.  # noqa: E501

        :return: The scope_option_id of this PortalProjectListEntry.  # noqa: E501
        :rtype: str
        """
        return self._scope_option_id

    @scope_option_id.setter
    def scope_option_id(self, scope_option_id):
        """Sets the scope_option_id of this PortalProjectListEntry.

        The unique identifier of the scope at which the project was created. A scope may have a different meaning             on different underlying platforms. In Translation Management System, a Scope corresponds to an Organization.  # noqa: E501

        :param scope_option_id: The scope_option_id of this PortalProjectListEntry.  # noqa: E501
        :type: str
        """

        self._scope_option_id = scope_option_id

    @property
    def scope_option_name(self):
        """Gets the scope_option_name of this PortalProjectListEntry.  # noqa: E501

        The name of the scope at which the project was created. A scope may have a different meaning             on different underlying platforms. In Translation Management System, a Scope corresponds to an Organization.  # noqa: E501

        :return: The scope_option_name of this PortalProjectListEntry.  # noqa: E501
        :rtype: str
        """
        return self._scope_option_name

    @scope_option_name.setter
    def scope_option_name(self, scope_option_name):
        """Sets the scope_option_name of this PortalProjectListEntry.

        The name of the scope at which the project was created. A scope may have a different meaning             on different underlying platforms. In Translation Management System, a Scope corresponds to an Organization.  # noqa: E501

        :param scope_option_name: The scope_option_name of this PortalProjectListEntry.  # noqa: E501
        :type: str
        """

        self._scope_option_name = scope_option_name

    @property
    def source_files(self):
        """Gets the source_files of this PortalProjectListEntry.  # noqa: E501

        The number of unique source files associated with the project.  # noqa: E501

        :return: The source_files of this PortalProjectListEntry.  # noqa: E501
        :rtype: int
        """
        return self._source_files

    @source_files.setter
    def source_files(self, source_files):
        """Sets the source_files of this PortalProjectListEntry.

        The number of unique source files associated with the project.  # noqa: E501

        :param source_files: The source_files of this PortalProjectListEntry.  # noqa: E501
        :type: int
        """

        self._source_files = source_files

    @property
    def source_langauge(self):
        """Gets the source_langauge of this PortalProjectListEntry.  # noqa: E501


        :return: The source_langauge of this PortalProjectListEntry.  # noqa: E501
        :rtype: PortalLanguage
        """
        return self._source_langauge

    @source_langauge.setter
    def source_langauge(self, source_langauge):
        """Sets the source_langauge of this PortalProjectListEntry.


        :param source_langauge: The source_langauge of this PortalProjectListEntry.  # noqa: E501
        :type: PortalLanguage
        """

        self._source_langauge = source_langauge

    @property
    def source_words(self):
        """Gets the source_words of this PortalProjectListEntry.  # noqa: E501

        The total number of words in all the source files associated with the project.  # noqa: E501

        :return: The source_words of this PortalProjectListEntry.  # noqa: E501
        :rtype: int
        """
        return self._source_words

    @source_words.setter
    def source_words(self, source_words):
        """Sets the source_words of this PortalProjectListEntry.

        The total number of words in all the source files associated with the project.  # noqa: E501

        :param source_words: The source_words of this PortalProjectListEntry.  # noqa: E501
        :type: int
        """

        self._source_words = source_words

    @property
    def started_batches(self):
        """Gets the started_batches of this PortalProjectListEntry.  # noqa: E501

        The number of started batches whitin the project.  # noqa: E501

        :return: The started_batches of this PortalProjectListEntry.  # noqa: E501
        :rtype: int
        """
        return self._started_batches

    @started_batches.setter
    def started_batches(self, started_batches):
        """Sets the started_batches of this PortalProjectListEntry.

        The number of started batches whitin the project.  # noqa: E501

        :param started_batches: The started_batches of this PortalProjectListEntry.  # noqa: E501
        :type: int
        """

        self._started_batches = started_batches

    @property
    def status(self):
        """Gets the status of this PortalProjectListEntry.  # noqa: E501

        The status of the project. This value is a simplified, project level status, and does not mean that every             file within the project is at this status.0 = Preparing, 1 = ForApproval, 2 = InProgress, 3 = ForDownload, 4 = Completed, 5 = PartialDownload, 6 = InReview, 7 = Reviewed, 8 = InSignOff, 9 = SignedOff, 10 = ForVendorSelection, 11 = Cancelled, 12 = New  # noqa: E501

        :return: The status of this PortalProjectListEntry.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PortalProjectListEntry.

        The status of the project. This value is a simplified, project level status, and does not mean that every             file within the project is at this status.0 = Preparing, 1 = ForApproval, 2 = InProgress, 3 = ForDownload, 4 = Completed, 5 = PartialDownload, 6 = InReview, 7 = Reviewed, 8 = InSignOff, 9 = SignedOff, 10 = ForVendorSelection, 11 = Cancelled, 12 = New  # noqa: E501

        :param status: The status of this PortalProjectListEntry.  # noqa: E501
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
    def target_languages(self):
        """Gets the target_languages of this PortalProjectListEntry.  # noqa: E501

        The target languages of the project.  # noqa: E501

        :return: The target_languages of this PortalProjectListEntry.  # noqa: E501
        :rtype: list[PortalLanguage]
        """
        return self._target_languages

    @target_languages.setter
    def target_languages(self, target_languages):
        """Sets the target_languages of this PortalProjectListEntry.

        The target languages of the project.  # noqa: E501

        :param target_languages: The target_languages of this PortalProjectListEntry.  # noqa: E501
        :type: list[PortalLanguage]
        """

        self._target_languages = target_languages

    @property
    def tm_savings(self):
        """Gets the tm_savings of this PortalProjectListEntry.  # noqa: E501

        The financial value of any saving derived from the use of Translation Memory.  # noqa: E501

        :return: The tm_savings of this PortalProjectListEntry.  # noqa: E501
        :rtype: float
        """
        return self._tm_savings

    @tm_savings.setter
    def tm_savings(self, tm_savings):
        """Sets the tm_savings of this PortalProjectListEntry.

        The financial value of any saving derived from the use of Translation Memory.  # noqa: E501

        :param tm_savings: The tm_savings of this PortalProjectListEntry.  # noqa: E501
        :type: float
        """

        self._tm_savings = tm_savings

    @property
    def vendor_costs(self):
        """Gets the vendor_costs of this PortalProjectListEntry.  # noqa: E501

        The calculated cost for the project as calculated by each of the Vendors selected at project creation.  # noqa: E501

        :return: The vendor_costs of this PortalProjectListEntry.  # noqa: E501
        :rtype: list[PortalProjectVendorCost]
        """
        return self._vendor_costs

    @vendor_costs.setter
    def vendor_costs(self, vendor_costs):
        """Sets the vendor_costs of this PortalProjectListEntry.

        The calculated cost for the project as calculated by each of the Vendors selected at project creation.  # noqa: E501

        :param vendor_costs: The vendor_costs of this PortalProjectListEntry.  # noqa: E501
        :type: list[PortalProjectVendorCost]
        """

        self._vendor_costs = vendor_costs

    @property
    def vendor_id(self):
        """Gets the vendor_id of this PortalProjectListEntry.  # noqa: E501

        The unique identifier of the translation vendor assigned to the project, when the underlying             platform allows selection of vendors.  # noqa: E501

        :return: The vendor_id of this PortalProjectListEntry.  # noqa: E501
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """Sets the vendor_id of this PortalProjectListEntry.

        The unique identifier of the translation vendor assigned to the project, when the underlying             platform allows selection of vendors.  # noqa: E501

        :param vendor_id: The vendor_id of this PortalProjectListEntry.  # noqa: E501
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def vendor_name(self):
        """Gets the vendor_name of this PortalProjectListEntry.  # noqa: E501

        The name of the translation vendor assigned to the project, when the underlying             platform allows selection of vendors.  # noqa: E501

        :return: The vendor_name of this PortalProjectListEntry.  # noqa: E501
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """Sets the vendor_name of this PortalProjectListEntry.

        The name of the translation vendor assigned to the project, when the underlying             platform allows selection of vendors.  # noqa: E501

        :param vendor_name: The vendor_name of this PortalProjectListEntry.  # noqa: E501
        :type: str
        """

        self._vendor_name = vendor_name

    @property
    def word_count(self):
        """Gets the word_count of this PortalProjectListEntry.  # noqa: E501

        The total word count of the project, considering all target language files.  # noqa: E501

        :return: The word_count of this PortalProjectListEntry.  # noqa: E501
        :rtype: int
        """
        return self._word_count

    @word_count.setter
    def word_count(self, word_count):
        """Sets the word_count of this PortalProjectListEntry.

        The total word count of the project, considering all target language files.  # noqa: E501

        :param word_count: The word_count of this PortalProjectListEntry.  # noqa: E501
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
        if issubclass(PortalProjectListEntry, dict):
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
        if not isinstance(other, PortalProjectListEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
