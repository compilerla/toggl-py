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


class ModelsStatistics:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"admins": "list[ModelsUserData]", "groups_count": "int", "members_count": "int"}

    attribute_map = {"admins": "admins", "groups_count": "groups_count", "members_count": "members_count"}

    def __init__(self, admins=None, groups_count=None, members_count=None, _configuration=None):  # noqa: E501
        """ModelsStatistics - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._admins = None
        self._groups_count = None
        self._members_count = None
        self.discriminator = None

        if admins is not None:
            self.admins = admins
        if groups_count is not None:
            self.groups_count = groups_count
        if members_count is not None:
            self.members_count = members_count

    @property
    def admins(self):
        """Gets the admins of this ModelsStatistics.  # noqa: E501


        :return: The admins of this ModelsStatistics.  # noqa: E501
        :rtype: list[ModelsUserData]
        """
        return self._admins

    @admins.setter
    def admins(self, admins):
        """Sets the admins of this ModelsStatistics.


        :param admins: The admins of this ModelsStatistics.  # noqa: E501
        :type: list[ModelsUserData]
        """

        self._admins = admins

    @property
    def groups_count(self):
        """Gets the groups_count of this ModelsStatistics.  # noqa: E501


        :return: The groups_count of this ModelsStatistics.  # noqa: E501
        :rtype: int
        """
        return self._groups_count

    @groups_count.setter
    def groups_count(self, groups_count):
        """Sets the groups_count of this ModelsStatistics.


        :param groups_count: The groups_count of this ModelsStatistics.  # noqa: E501
        :type: int
        """

        self._groups_count = groups_count

    @property
    def members_count(self):
        """Gets the members_count of this ModelsStatistics.  # noqa: E501


        :return: The members_count of this ModelsStatistics.  # noqa: E501
        :rtype: int
        """
        return self._members_count

    @members_count.setter
    def members_count(self, members_count):
        """Sets the members_count of this ModelsStatistics.


        :param members_count: The members_count of this ModelsStatistics.  # noqa: E501
        :type: int
        """

        self._members_count = members_count

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
        if issubclass(ModelsStatistics, dict):
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
        if not isinstance(other, ModelsStatistics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsStatistics):
            return True

        return self.to_dict() != other.to_dict()
