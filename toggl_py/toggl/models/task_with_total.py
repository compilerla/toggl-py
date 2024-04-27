"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import pprint
import re  # noqa: F401

from toggl.configuration import Configuration


class TaskWithTotal:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "active": "bool",
        "at": "str",
        "estimated_seconds": "int",
        "id": "int",
        "name": "str",
        "permissions": "str",
        "project_id": "int",
        "recurring": "bool",
        "server_deleted_at": "str",
        "toggl_accounts_id": "str",
        "tracked_seconds": "int",
        "user_id": "int",
        "workspace_id": "int",
    }

    attribute_map = {
        "active": "active",
        "at": "at",
        "estimated_seconds": "estimated_seconds",
        "id": "id",
        "name": "name",
        "permissions": "permissions",
        "project_id": "project_id",
        "recurring": "recurring",
        "server_deleted_at": "server_deleted_at",
        "toggl_accounts_id": "toggl_accounts_id",
        "tracked_seconds": "tracked_seconds",
        "user_id": "user_id",
        "workspace_id": "workspace_id",
    }

    def __init__(
        self,
        active=None,
        at=None,
        estimated_seconds=None,
        id=None,
        name=None,
        permissions=None,
        project_id=None,
        recurring=None,
        server_deleted_at=None,
        toggl_accounts_id=None,
        tracked_seconds=None,
        user_id=None,
        workspace_id=None,
        _configuration=None,
    ):  # noqa: E501
        """TaskWithTotal - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active = None
        self._at = None
        self._estimated_seconds = None
        self._id = None
        self._name = None
        self._permissions = None
        self._project_id = None
        self._recurring = None
        self._server_deleted_at = None
        self._toggl_accounts_id = None
        self._tracked_seconds = None
        self._user_id = None
        self._workspace_id = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if at is not None:
            self.at = at
        if estimated_seconds is not None:
            self.estimated_seconds = estimated_seconds
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if permissions is not None:
            self.permissions = permissions
        if project_id is not None:
            self.project_id = project_id
        if recurring is not None:
            self.recurring = recurring
        if server_deleted_at is not None:
            self.server_deleted_at = server_deleted_at
        if toggl_accounts_id is not None:
            self.toggl_accounts_id = toggl_accounts_id
        if tracked_seconds is not None:
            self.tracked_seconds = tracked_seconds
        if user_id is not None:
            self.user_id = user_id
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def active(self):
        """Gets the active of this TaskWithTotal.  # noqa: E501

        False when the task has been done  # noqa: E501

        :return: The active of this TaskWithTotal.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this TaskWithTotal.

        False when the task has been done  # noqa: E501

        :param active: The active of this TaskWithTotal.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def at(self):
        """Gets the at of this TaskWithTotal.  # noqa: E501

        When the task was created/last modified  # noqa: E501

        :return: The at of this TaskWithTotal.  # noqa: E501
        :rtype: str
        """
        return self._at

    @at.setter
    def at(self, at):
        """Sets the at of this TaskWithTotal.

        When the task was created/last modified  # noqa: E501

        :param at: The at of this TaskWithTotal.  # noqa: E501
        :type: str
        """

        self._at = at

    @property
    def estimated_seconds(self):
        """Gets the estimated_seconds of this TaskWithTotal.  # noqa: E501

        Estimation time for this task in seconds  # noqa: E501

        :return: The estimated_seconds of this TaskWithTotal.  # noqa: E501
        :rtype: int
        """
        return self._estimated_seconds

    @estimated_seconds.setter
    def estimated_seconds(self, estimated_seconds):
        """Sets the estimated_seconds of this TaskWithTotal.

        Estimation time for this task in seconds  # noqa: E501

        :param estimated_seconds: The estimated_seconds of this TaskWithTotal.  # noqa: E501
        :type: int
        """

        self._estimated_seconds = estimated_seconds

    @property
    def id(self):
        """Gets the id of this TaskWithTotal.  # noqa: E501

        Task ID  # noqa: E501

        :return: The id of this TaskWithTotal.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskWithTotal.

        Task ID  # noqa: E501

        :param id: The id of this TaskWithTotal.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this TaskWithTotal.  # noqa: E501

        Task Name  # noqa: E501

        :return: The name of this TaskWithTotal.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskWithTotal.

        Task Name  # noqa: E501

        :param name: The name of this TaskWithTotal.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def permissions(self):
        """Gets the permissions of this TaskWithTotal.  # noqa: E501


        :return: The permissions of this TaskWithTotal.  # noqa: E501
        :rtype: str
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this TaskWithTotal.


        :param permissions: The permissions of this TaskWithTotal.  # noqa: E501
        :type: str
        """

        self._permissions = permissions

    @property
    def project_id(self):
        """Gets the project_id of this TaskWithTotal.  # noqa: E501

        Project ID  # noqa: E501

        :return: The project_id of this TaskWithTotal.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TaskWithTotal.

        Project ID  # noqa: E501

        :param project_id: The project_id of this TaskWithTotal.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def recurring(self):
        """Gets the recurring of this TaskWithTotal.  # noqa: E501

        Whether this is a recurring task  # noqa: E501

        :return: The recurring of this TaskWithTotal.  # noqa: E501
        :rtype: bool
        """
        return self._recurring

    @recurring.setter
    def recurring(self, recurring):
        """Sets the recurring of this TaskWithTotal.

        Whether this is a recurring task  # noqa: E501

        :param recurring: The recurring of this TaskWithTotal.  # noqa: E501
        :type: bool
        """

        self._recurring = recurring

    @property
    def server_deleted_at(self):
        """Gets the server_deleted_at of this TaskWithTotal.  # noqa: E501

        When the task was deleted  # noqa: E501

        :return: The server_deleted_at of this TaskWithTotal.  # noqa: E501
        :rtype: str
        """
        return self._server_deleted_at

    @server_deleted_at.setter
    def server_deleted_at(self, server_deleted_at):
        """Sets the server_deleted_at of this TaskWithTotal.

        When the task was deleted  # noqa: E501

        :param server_deleted_at: The server_deleted_at of this TaskWithTotal.  # noqa: E501
        :type: str
        """

        self._server_deleted_at = server_deleted_at

    @property
    def toggl_accounts_id(self):
        """Gets the toggl_accounts_id of this TaskWithTotal.  # noqa: E501

        Task assignee, if set above this will be the toggl_account_id for that user  # noqa: E501

        :return: The toggl_accounts_id of this TaskWithTotal.  # noqa: E501
        :rtype: str
        """
        return self._toggl_accounts_id

    @toggl_accounts_id.setter
    def toggl_accounts_id(self, toggl_accounts_id):
        """Sets the toggl_accounts_id of this TaskWithTotal.

        Task assignee, if set above this will be the toggl_account_id for that user  # noqa: E501

        :param toggl_accounts_id: The toggl_accounts_id of this TaskWithTotal.  # noqa: E501
        :type: str
        """

        self._toggl_accounts_id = toggl_accounts_id

    @property
    def tracked_seconds(self):
        """Gets the tracked_seconds of this TaskWithTotal.  # noqa: E501

        The value tracked_seconds is in milliseconds, not in seconds.  # noqa: E501

        :return: The tracked_seconds of this TaskWithTotal.  # noqa: E501
        :rtype: int
        """
        return self._tracked_seconds

    @tracked_seconds.setter
    def tracked_seconds(self, tracked_seconds):
        """Sets the tracked_seconds of this TaskWithTotal.

        The value tracked_seconds is in milliseconds, not in seconds.  # noqa: E501

        :param tracked_seconds: The tracked_seconds of this TaskWithTotal.  # noqa: E501
        :type: int
        """

        self._tracked_seconds = tracked_seconds

    @property
    def user_id(self):
        """Gets the user_id of this TaskWithTotal.  # noqa: E501

        Task assignee, if available  # noqa: E501

        :return: The user_id of this TaskWithTotal.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TaskWithTotal.

        Task assignee, if available  # noqa: E501

        :param user_id: The user_id of this TaskWithTotal.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this TaskWithTotal.  # noqa: E501

        Workspace ID  # noqa: E501

        :return: The workspace_id of this TaskWithTotal.  # noqa: E501
        :rtype: int
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this TaskWithTotal.

        Workspace ID  # noqa: E501

        :param workspace_id: The workspace_id of this TaskWithTotal.  # noqa: E501
        :type: int
        """

        self._workspace_id = workspace_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.swagger_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item, value.items())
                )
            else:
                result[attr] = value
        if issubclass(TaskWithTotal, dict):
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
        if not isinstance(other, TaskWithTotal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskWithTotal):
            return True

        return self.to_dict() != other.to_dict()
