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


class GroupOrganizationGroupResponse:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "at": "str",
        "group_id": "int",
        "name": "str",
        "permissions": "str",
        "users": "list[ModelsOrganizationUserSimple]",
        "workspaces": "list[int]",
    }

    attribute_map = {
        "at": "at",
        "group_id": "group_id",
        "name": "name",
        "permissions": "permissions",
        "users": "users",
        "workspaces": "workspaces",
    }

    def __init__(
        self, at=None, group_id=None, name=None, permissions=None, users=None, workspaces=None, _configuration=None
    ):  # noqa: E501
        """GroupOrganizationGroupResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._at = None
        self._group_id = None
        self._name = None
        self._permissions = None
        self._users = None
        self._workspaces = None
        self.discriminator = None

        if at is not None:
            self.at = at
        if group_id is not None:
            self.group_id = group_id
        if name is not None:
            self.name = name
        if permissions is not None:
            self.permissions = permissions
        if users is not None:
            self.users = users
        if workspaces is not None:
            self.workspaces = workspaces

    @property
    def at(self):
        """Gets the at of this GroupOrganizationGroupResponse.  # noqa: E501


        :return: The at of this GroupOrganizationGroupResponse.  # noqa: E501
        :rtype: str
        """
        return self._at

    @at.setter
    def at(self, at):
        """Sets the at of this GroupOrganizationGroupResponse.


        :param at: The at of this GroupOrganizationGroupResponse.  # noqa: E501
        :type: str
        """

        self._at = at

    @property
    def group_id(self):
        """Gets the group_id of this GroupOrganizationGroupResponse.  # noqa: E501


        :return: The group_id of this GroupOrganizationGroupResponse.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GroupOrganizationGroupResponse.


        :param group_id: The group_id of this GroupOrganizationGroupResponse.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def name(self):
        """Gets the name of this GroupOrganizationGroupResponse.  # noqa: E501


        :return: The name of this GroupOrganizationGroupResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupOrganizationGroupResponse.


        :param name: The name of this GroupOrganizationGroupResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def permissions(self):
        """Gets the permissions of this GroupOrganizationGroupResponse.  # noqa: E501


        :return: The permissions of this GroupOrganizationGroupResponse.  # noqa: E501
        :rtype: str
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this GroupOrganizationGroupResponse.


        :param permissions: The permissions of this GroupOrganizationGroupResponse.  # noqa: E501
        :type: str
        """

        self._permissions = permissions

    @property
    def users(self):
        """Gets the users of this GroupOrganizationGroupResponse.  # noqa: E501


        :return: The users of this GroupOrganizationGroupResponse.  # noqa: E501
        :rtype: list[ModelsOrganizationUserSimple]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this GroupOrganizationGroupResponse.


        :param users: The users of this GroupOrganizationGroupResponse.  # noqa: E501
        :type: list[ModelsOrganizationUserSimple]
        """

        self._users = users

    @property
    def workspaces(self):
        """Gets the workspaces of this GroupOrganizationGroupResponse.  # noqa: E501


        :return: The workspaces of this GroupOrganizationGroupResponse.  # noqa: E501
        :rtype: list[int]
        """
        return self._workspaces

    @workspaces.setter
    def workspaces(self, workspaces):
        """Sets the workspaces of this GroupOrganizationGroupResponse.


        :param workspaces: The workspaces of this GroupOrganizationGroupResponse.  # noqa: E501
        :type: list[int]
        """

        self._workspaces = workspaces

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
        if issubclass(GroupOrganizationGroupResponse, dict):
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
        if not isinstance(other, GroupOrganizationGroupResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupOrganizationGroupResponse):
            return True

        return self.to_dict() != other.to_dict()
