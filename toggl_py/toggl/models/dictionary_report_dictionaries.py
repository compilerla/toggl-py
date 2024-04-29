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


class DictionaryReportDictionaries:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "clients": "DictionaryGeneralDictionary",
        "filters": "DictionaryReportDictionariesData",
        "projects": "DictionaryProjectDictionary",
        "tags": "DictionaryGeneralDictionary",
        "tasks": "DictionaryTaskDictionary",
        "user_groups": "DictionaryGeneralDictionary",
        "users": "DictionaryUserDictionary",
    }

    attribute_map = {
        "clients": "clients",
        "filters": "filters",
        "projects": "projects",
        "tags": "tags",
        "tasks": "tasks",
        "user_groups": "user_groups",
        "users": "users",
    }

    def __init__(
        self,
        clients=None,
        filters=None,
        projects=None,
        tags=None,
        tasks=None,
        user_groups=None,
        users=None,
        _configuration=None,
    ):  # noqa: E501
        """DictionaryReportDictionaries - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._clients = None
        self._filters = None
        self._projects = None
        self._tags = None
        self._tasks = None
        self._user_groups = None
        self._users = None
        self.discriminator = None

        if clients is not None:
            self.clients = clients
        if filters is not None:
            self.filters = filters
        if projects is not None:
            self.projects = projects
        if tags is not None:
            self.tags = tags
        if tasks is not None:
            self.tasks = tasks
        if user_groups is not None:
            self.user_groups = user_groups
        if users is not None:
            self.users = users

    @property
    def clients(self):
        """Gets the clients of this DictionaryReportDictionaries.  # noqa: E501


        :return: The clients of this DictionaryReportDictionaries.  # noqa: E501
        :rtype: DictionaryGeneralDictionary
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this DictionaryReportDictionaries.


        :param clients: The clients of this DictionaryReportDictionaries.  # noqa: E501
        :type: DictionaryGeneralDictionary
        """

        self._clients = clients

    @property
    def filters(self):
        """Gets the filters of this DictionaryReportDictionaries.  # noqa: E501

        Remove it after FlexQ release.  # noqa: E501

        :return: The filters of this DictionaryReportDictionaries.  # noqa: E501
        :rtype: DictionaryReportDictionariesData
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this DictionaryReportDictionaries.

        Remove it after FlexQ release.  # noqa: E501

        :param filters: The filters of this DictionaryReportDictionaries.  # noqa: E501
        :type: DictionaryReportDictionariesData
        """

        self._filters = filters

    @property
    def projects(self):
        """Gets the projects of this DictionaryReportDictionaries.  # noqa: E501


        :return: The projects of this DictionaryReportDictionaries.  # noqa: E501
        :rtype: DictionaryProjectDictionary
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this DictionaryReportDictionaries.


        :param projects: The projects of this DictionaryReportDictionaries.  # noqa: E501
        :type: DictionaryProjectDictionary
        """

        self._projects = projects

    @property
    def tags(self):
        """Gets the tags of this DictionaryReportDictionaries.  # noqa: E501


        :return: The tags of this DictionaryReportDictionaries.  # noqa: E501
        :rtype: DictionaryGeneralDictionary
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DictionaryReportDictionaries.


        :param tags: The tags of this DictionaryReportDictionaries.  # noqa: E501
        :type: DictionaryGeneralDictionary
        """

        self._tags = tags

    @property
    def tasks(self):
        """Gets the tasks of this DictionaryReportDictionaries.  # noqa: E501


        :return: The tasks of this DictionaryReportDictionaries.  # noqa: E501
        :rtype: DictionaryTaskDictionary
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this DictionaryReportDictionaries.


        :param tasks: The tasks of this DictionaryReportDictionaries.  # noqa: E501
        :type: DictionaryTaskDictionary
        """

        self._tasks = tasks

    @property
    def user_groups(self):
        """Gets the user_groups of this DictionaryReportDictionaries.  # noqa: E501


        :return: The user_groups of this DictionaryReportDictionaries.  # noqa: E501
        :rtype: DictionaryGeneralDictionary
        """
        return self._user_groups

    @user_groups.setter
    def user_groups(self, user_groups):
        """Sets the user_groups of this DictionaryReportDictionaries.


        :param user_groups: The user_groups of this DictionaryReportDictionaries.  # noqa: E501
        :type: DictionaryGeneralDictionary
        """

        self._user_groups = user_groups

    @property
    def users(self):
        """Gets the users of this DictionaryReportDictionaries.  # noqa: E501


        :return: The users of this DictionaryReportDictionaries.  # noqa: E501
        :rtype: DictionaryUserDictionary
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this DictionaryReportDictionaries.


        :param users: The users of this DictionaryReportDictionaries.  # noqa: E501
        :type: DictionaryUserDictionary
        """

        self._users = users

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
        if issubclass(DictionaryReportDictionaries, dict):
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
        if not isinstance(other, DictionaryReportDictionaries):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DictionaryReportDictionaries):
            return True

        return self.to_dict() != other.to_dict()
