"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Last changed: 2024-04-26T22:13:16.785Z
Generated by: https://github.com/compilerla/toggl-py/tree/main/codegen
"""

import pprint
import re  # noqa: F401

from toggl.configuration import Configuration


class TasksTasksPost:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "active": "bool",
        "ids": "list[int]",
        "name": "str",
        "page_size": "int",
        "project_active": "bool",
        "project_ids": "list[int]",
        "start": "int",
        "user_ids": "list[int]",
    }

    attribute_map = {
        "active": "active",
        "ids": "ids",
        "name": "name",
        "page_size": "page_size",
        "project_active": "project_active",
        "project_ids": "project_ids",
        "start": "start",
        "user_ids": "user_ids",
    }

    def __init__(
        self,
        active=None,
        ids=None,
        name=None,
        page_size=None,
        project_active=None,
        project_ids=None,
        start=None,
        user_ids=None,
        _configuration=None,
    ):  # noqa: E501
        """TasksTasksPost - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active = None
        self._ids = None
        self._name = None
        self._page_size = None
        self._project_active = None
        self._project_ids = None
        self._start = None
        self._user_ids = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if ids is not None:
            self.ids = ids
        if name is not None:
            self.name = name
        if page_size is not None:
            self.page_size = page_size
        if project_active is not None:
            self.project_active = project_active
        if project_ids is not None:
            self.project_ids = project_ids
        if start is not None:
            self.start = start
        if user_ids is not None:
            self.user_ids = user_ids

    @property
    def active(self):
        """Gets the active of this TasksTasksPost.  # noqa: E501


        :return: The active of this TasksTasksPost.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this TasksTasksPost.


        :param active: The active of this TasksTasksPost.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def ids(self):
        """Gets the ids of this TasksTasksPost.  # noqa: E501


        :return: The ids of this TasksTasksPost.  # noqa: E501
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this TasksTasksPost.


        :param ids: The ids of this TasksTasksPost.  # noqa: E501
        :type: list[int]
        """

        self._ids = ids

    @property
    def name(self):
        """Gets the name of this TasksTasksPost.  # noqa: E501


        :return: The name of this TasksTasksPost.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TasksTasksPost.


        :param name: The name of this TasksTasksPost.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def page_size(self):
        """Gets the page_size of this TasksTasksPost.  # noqa: E501


        :return: The page_size of this TasksTasksPost.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this TasksTasksPost.


        :param page_size: The page_size of this TasksTasksPost.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def project_active(self):
        """Gets the project_active of this TasksTasksPost.  # noqa: E501


        :return: The project_active of this TasksTasksPost.  # noqa: E501
        :rtype: bool
        """
        return self._project_active

    @project_active.setter
    def project_active(self, project_active):
        """Sets the project_active of this TasksTasksPost.


        :param project_active: The project_active of this TasksTasksPost.  # noqa: E501
        :type: bool
        """

        self._project_active = project_active

    @property
    def project_ids(self):
        """Gets the project_ids of this TasksTasksPost.  # noqa: E501


        :return: The project_ids of this TasksTasksPost.  # noqa: E501
        :rtype: list[int]
        """
        return self._project_ids

    @project_ids.setter
    def project_ids(self, project_ids):
        """Sets the project_ids of this TasksTasksPost.


        :param project_ids: The project_ids of this TasksTasksPost.  # noqa: E501
        :type: list[int]
        """

        self._project_ids = project_ids

    @property
    def start(self):
        """Gets the start of this TasksTasksPost.  # noqa: E501


        :return: The start of this TasksTasksPost.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this TasksTasksPost.


        :param start: The start of this TasksTasksPost.  # noqa: E501
        :type: int
        """

        self._start = start

    @property
    def user_ids(self):
        """Gets the user_ids of this TasksTasksPost.  # noqa: E501


        :return: The user_ids of this TasksTasksPost.  # noqa: E501
        :rtype: list[int]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this TasksTasksPost.


        :param user_ids: The user_ids of this TasksTasksPost.  # noqa: E501
        :type: list[int]
        """

        self._user_ids = user_ids

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
        if issubclass(TasksTasksPost, dict):
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
        if not isinstance(other, TasksTasksPost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TasksTasksPost):
            return True

        return self.to_dict() != other.to_dict()
