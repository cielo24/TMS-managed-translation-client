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


class LcFile(object):
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
        'allow_all_file_extensions': 'bool',
        'archive_file_name_hashes': 'list[str]',
        'archive_is_password_protected': 'bool',
        'archive_is_unsupported': 'bool',
        'file_id': 'str',
        'file_name': 'str',
        'file_name_hash': 'str',
        'has_unsupported_path_length': 'bool',
        'is_reference': 'bool',
        'is_translatable': 'bool',
        'provider_name': 'str',
        'unsupported_are_reference': 'bool',
        'unsupported_files_in_archive': 'bool',
        'upload_complete': 'bool',
        'word_count': 'int'
    }

    attribute_map = {
        'allow_all_file_extensions': 'AllowAllFileExtensions',
        'archive_file_name_hashes': 'ArchiveFileNameHashes',
        'archive_is_password_protected': 'ArchiveIsPasswordProtected',
        'archive_is_unsupported': 'ArchiveIsUnsupported',
        'file_id': 'FileId',
        'file_name': 'FileName',
        'file_name_hash': 'FileNameHash',
        'has_unsupported_path_length': 'HasUnsupportedPathLength',
        'is_reference': 'IsReference',
        'is_translatable': 'IsTranslatable',
        'provider_name': 'ProviderName',
        'unsupported_are_reference': 'UnsupportedAreReference',
        'unsupported_files_in_archive': 'UnsupportedFilesInArchive',
        'upload_complete': 'UploadComplete',
        'word_count': 'WordCount'
    }

    def __init__(self, allow_all_file_extensions=None, archive_file_name_hashes=None, archive_is_password_protected=None, archive_is_unsupported=None, file_id=None, file_name=None, file_name_hash=None, has_unsupported_path_length=None, is_reference=None, is_translatable=None, provider_name=None, unsupported_are_reference=None, unsupported_files_in_archive=None, upload_complete=None, word_count=None, _configuration=None):  # noqa: E501
        """LcFile - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_all_file_extensions = None
        self._archive_file_name_hashes = None
        self._archive_is_password_protected = None
        self._archive_is_unsupported = None
        self._file_id = None
        self._file_name = None
        self._file_name_hash = None
        self._has_unsupported_path_length = None
        self._is_reference = None
        self._is_translatable = None
        self._provider_name = None
        self._unsupported_are_reference = None
        self._unsupported_files_in_archive = None
        self._upload_complete = None
        self._word_count = None
        self.discriminator = None

        if allow_all_file_extensions is not None:
            self.allow_all_file_extensions = allow_all_file_extensions
        if archive_file_name_hashes is not None:
            self.archive_file_name_hashes = archive_file_name_hashes
        if archive_is_password_protected is not None:
            self.archive_is_password_protected = archive_is_password_protected
        if archive_is_unsupported is not None:
            self.archive_is_unsupported = archive_is_unsupported
        if file_id is not None:
            self.file_id = file_id
        if file_name is not None:
            self.file_name = file_name
        if file_name_hash is not None:
            self.file_name_hash = file_name_hash
        if has_unsupported_path_length is not None:
            self.has_unsupported_path_length = has_unsupported_path_length
        if is_reference is not None:
            self.is_reference = is_reference
        if is_translatable is not None:
            self.is_translatable = is_translatable
        if provider_name is not None:
            self.provider_name = provider_name
        if unsupported_are_reference is not None:
            self.unsupported_are_reference = unsupported_are_reference
        if unsupported_files_in_archive is not None:
            self.unsupported_files_in_archive = unsupported_files_in_archive
        if upload_complete is not None:
            self.upload_complete = upload_complete
        if word_count is not None:
            self.word_count = word_count

    @property
    def allow_all_file_extensions(self):
        """Gets the allow_all_file_extensions of this LcFile.  # noqa: E501

        Gets or sets a value indicating whether an unsupported file, or an unsupported file contained in the archive is allowed as translatable  # noqa: E501

        :return: The allow_all_file_extensions of this LcFile.  # noqa: E501
        :rtype: bool
        """
        return self._allow_all_file_extensions

    @allow_all_file_extensions.setter
    def allow_all_file_extensions(self, allow_all_file_extensions):
        """Sets the allow_all_file_extensions of this LcFile.

        Gets or sets a value indicating whether an unsupported file, or an unsupported file contained in the archive is allowed as translatable  # noqa: E501

        :param allow_all_file_extensions: The allow_all_file_extensions of this LcFile.  # noqa: E501
        :type: bool
        """

        self._allow_all_file_extensions = allow_all_file_extensions

    @property
    def archive_file_name_hashes(self):
        """Gets the archive_file_name_hashes of this LcFile.  # noqa: E501

        Gets or sets the file name MD5 hashes for files contained in an archive.  # noqa: E501

        :return: The archive_file_name_hashes of this LcFile.  # noqa: E501
        :rtype: list[str]
        """
        return self._archive_file_name_hashes

    @archive_file_name_hashes.setter
    def archive_file_name_hashes(self, archive_file_name_hashes):
        """Sets the archive_file_name_hashes of this LcFile.

        Gets or sets the file name MD5 hashes for files contained in an archive.  # noqa: E501

        :param archive_file_name_hashes: The archive_file_name_hashes of this LcFile.  # noqa: E501
        :type: list[str]
        """

        self._archive_file_name_hashes = archive_file_name_hashes

    @property
    def archive_is_password_protected(self):
        """Gets the archive_is_password_protected of this LcFile.  # noqa: E501

        Gets or sets a value indicating whether the archive is encrypted  # noqa: E501

        :return: The archive_is_password_protected of this LcFile.  # noqa: E501
        :rtype: bool
        """
        return self._archive_is_password_protected

    @archive_is_password_protected.setter
    def archive_is_password_protected(self, archive_is_password_protected):
        """Sets the archive_is_password_protected of this LcFile.

        Gets or sets a value indicating whether the archive is encrypted  # noqa: E501

        :param archive_is_password_protected: The archive_is_password_protected of this LcFile.  # noqa: E501
        :type: bool
        """

        self._archive_is_password_protected = archive_is_password_protected

    @property
    def archive_is_unsupported(self):
        """Gets the archive_is_unsupported of this LcFile.  # noqa: E501

        Gets or sets a value indicating whether the archive type is supported  # noqa: E501

        :return: The archive_is_unsupported of this LcFile.  # noqa: E501
        :rtype: bool
        """
        return self._archive_is_unsupported

    @archive_is_unsupported.setter
    def archive_is_unsupported(self, archive_is_unsupported):
        """Sets the archive_is_unsupported of this LcFile.

        Gets or sets a value indicating whether the archive type is supported  # noqa: E501

        :param archive_is_unsupported: The archive_is_unsupported of this LcFile.  # noqa: E501
        :type: bool
        """

        self._archive_is_unsupported = archive_is_unsupported

    @property
    def file_id(self):
        """Gets the file_id of this LcFile.  # noqa: E501

        Gets or sets the file identifier.  # noqa: E501

        :return: The file_id of this LcFile.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this LcFile.

        Gets or sets the file identifier.  # noqa: E501

        :param file_id: The file_id of this LcFile.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def file_name(self):
        """Gets the file_name of this LcFile.  # noqa: E501

        Gets or sets the name of the file.  # noqa: E501

        :return: The file_name of this LcFile.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this LcFile.

        Gets or sets the name of the file.  # noqa: E501

        :param file_name: The file_name of this LcFile.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def file_name_hash(self):
        """Gets the file_name_hash of this LcFile.  # noqa: E501

        Gets or sets the file name MD5 hash.  # noqa: E501

        :return: The file_name_hash of this LcFile.  # noqa: E501
        :rtype: str
        """
        return self._file_name_hash

    @file_name_hash.setter
    def file_name_hash(self, file_name_hash):
        """Sets the file_name_hash of this LcFile.

        Gets or sets the file name MD5 hash.  # noqa: E501

        :param file_name_hash: The file_name_hash of this LcFile.  # noqa: E501
        :type: str
        """

        self._file_name_hash = file_name_hash

    @property
    def has_unsupported_path_length(self):
        """Gets the has_unsupported_path_length of this LcFile.  # noqa: E501

        Gets or sets a value indicating whether this file, or a file contained in this archive, has a path length greater than the supported path length.  # noqa: E501

        :return: The has_unsupported_path_length of this LcFile.  # noqa: E501
        :rtype: bool
        """
        return self._has_unsupported_path_length

    @has_unsupported_path_length.setter
    def has_unsupported_path_length(self, has_unsupported_path_length):
        """Sets the has_unsupported_path_length of this LcFile.

        Gets or sets a value indicating whether this file, or a file contained in this archive, has a path length greater than the supported path length.  # noqa: E501

        :param has_unsupported_path_length: The has_unsupported_path_length of this LcFile.  # noqa: E501
        :type: bool
        """

        self._has_unsupported_path_length = has_unsupported_path_length

    @property
    def is_reference(self):
        """Gets the is_reference of this LcFile.  # noqa: E501

        Gets or sets a value indicating whether this instance is reference.  # noqa: E501

        :return: The is_reference of this LcFile.  # noqa: E501
        :rtype: bool
        """
        return self._is_reference

    @is_reference.setter
    def is_reference(self, is_reference):
        """Sets the is_reference of this LcFile.

        Gets or sets a value indicating whether this instance is reference.  # noqa: E501

        :param is_reference: The is_reference of this LcFile.  # noqa: E501
        :type: bool
        """

        self._is_reference = is_reference

    @property
    def is_translatable(self):
        """Gets the is_translatable of this LcFile.  # noqa: E501

        Gets or sets a value indicating whether this instance is translatable.  # noqa: E501

        :return: The is_translatable of this LcFile.  # noqa: E501
        :rtype: bool
        """
        return self._is_translatable

    @is_translatable.setter
    def is_translatable(self, is_translatable):
        """Sets the is_translatable of this LcFile.

        Gets or sets a value indicating whether this instance is translatable.  # noqa: E501

        :param is_translatable: The is_translatable of this LcFile.  # noqa: E501
        :type: bool
        """

        self._is_translatable = is_translatable

    @property
    def provider_name(self):
        """Gets the provider_name of this LcFile.  # noqa: E501

        Gets or sets a value indicating whether [provider name].  # noqa: E501

        :return: The provider_name of this LcFile.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this LcFile.

        Gets or sets a value indicating whether [provider name].  # noqa: E501

        :param provider_name: The provider_name of this LcFile.  # noqa: E501
        :type: str
        """

        self._provider_name = provider_name

    @property
    def unsupported_are_reference(self):
        """Gets the unsupported_are_reference of this LcFile.  # noqa: E501

        Gets or sets a value indicating whether unsupported files in the archive will be handled as reference files.  # noqa: E501

        :return: The unsupported_are_reference of this LcFile.  # noqa: E501
        :rtype: bool
        """
        return self._unsupported_are_reference

    @unsupported_are_reference.setter
    def unsupported_are_reference(self, unsupported_are_reference):
        """Sets the unsupported_are_reference of this LcFile.

        Gets or sets a value indicating whether unsupported files in the archive will be handled as reference files.  # noqa: E501

        :param unsupported_are_reference: The unsupported_are_reference of this LcFile.  # noqa: E501
        :type: bool
        """

        self._unsupported_are_reference = unsupported_are_reference

    @property
    def unsupported_files_in_archive(self):
        """Gets the unsupported_files_in_archive of this LcFile.  # noqa: E501

        Gets or sets a value indicating whether there are unsupported files in the archive.  # noqa: E501

        :return: The unsupported_files_in_archive of this LcFile.  # noqa: E501
        :rtype: bool
        """
        return self._unsupported_files_in_archive

    @unsupported_files_in_archive.setter
    def unsupported_files_in_archive(self, unsupported_files_in_archive):
        """Sets the unsupported_files_in_archive of this LcFile.

        Gets or sets a value indicating whether there are unsupported files in the archive.  # noqa: E501

        :param unsupported_files_in_archive: The unsupported_files_in_archive of this LcFile.  # noqa: E501
        :type: bool
        """

        self._unsupported_files_in_archive = unsupported_files_in_archive

    @property
    def upload_complete(self):
        """Gets the upload_complete of this LcFile.  # noqa: E501

        Gets or sets a value indicating whether the file upload has been successfully completed.  # noqa: E501

        :return: The upload_complete of this LcFile.  # noqa: E501
        :rtype: bool
        """
        return self._upload_complete

    @upload_complete.setter
    def upload_complete(self, upload_complete):
        """Sets the upload_complete of this LcFile.

        Gets or sets a value indicating whether the file upload has been successfully completed.  # noqa: E501

        :param upload_complete: The upload_complete of this LcFile.  # noqa: E501
        :type: bool
        """

        self._upload_complete = upload_complete

    @property
    def word_count(self):
        """Gets the word_count of this LcFile.  # noqa: E501

        Gets or sets a value indicating the word count.  # noqa: E501

        :return: The word_count of this LcFile.  # noqa: E501
        :rtype: int
        """
        return self._word_count

    @word_count.setter
    def word_count(self, word_count):
        """Sets the word_count of this LcFile.

        Gets or sets a value indicating the word count.  # noqa: E501

        :param word_count: The word_count of this LcFile.  # noqa: E501
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
        if issubclass(LcFile, dict):
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
        if not isinstance(other, LcFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LcFile):
            return True

        return self.to_dict() != other.to_dict()
