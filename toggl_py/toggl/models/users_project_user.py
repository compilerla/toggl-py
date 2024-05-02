"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import pprint
import re  # noqa: F401
from datetime import datetime  # noqa: F401
from typing import Any

from toggl.configuration import Configuration


class UsersProjectUser:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "group_id": "int",
        "hourly_rate": "float",
        "id": "int",
        "labour_cost": "int",
        "manager": "bool",
        "project_id": "int",
        "user_id": "int",
    }

    attribute_map = {
        "group_id": "group_id",
        "hourly_rate": "hourly_rate",
        "id": "id",
        "labour_cost": "labour_cost",
        "manager": "manager",
        "project_id": "project_id",
        "user_id": "user_id",
    }

    def __init__(
        self,
        group_id: int = None,
        hourly_rate: float = None,
        id: int = None,
        labour_cost: int = None,
        manager: bool = None,
        project_id: int = None,
        user_id: int = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        UsersProjectUser - a model defined in Swagger

        Parameters:
          group_id (int): Optional
          hourly_rate (float): Optional
          id (int): Optional
          labour_cost (int): Optional
          manager (bool): Optional
          project_id (int): Optional
          user_id (int): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._group_id = None
        self._hourly_rate = None
        self._id = None
        self._labour_cost = None
        self._manager = None
        self._project_id = None
        self._user_id = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if hourly_rate is not None:
            self.hourly_rate = hourly_rate
        if id is not None:
            self.id = id
        if labour_cost is not None:
            self.labour_cost = labour_cost
        if manager is not None:
            self.manager = manager
        if project_id is not None:
            self.project_id = project_id
        if user_id is not None:
            self.user_id = user_id

    @property
    def group_id(self) -> int:
        """Gets the group_id of this UsersProjectUser.  # noqa: E501


        :return: The group_id of this UsersProjectUser.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id: int):
        """Sets the group_id of this UsersProjectUser.


        :param group_id: The group_id of this UsersProjectUser.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def hourly_rate(self) -> float:
        """Gets the hourly_rate of this UsersProjectUser.  # noqa: E501


        :return: The hourly_rate of this UsersProjectUser.  # noqa: E501
        :rtype: float
        """
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, hourly_rate: float):
        """Sets the hourly_rate of this UsersProjectUser.


        :param hourly_rate: The hourly_rate of this UsersProjectUser.  # noqa: E501
        :type: float
        """

        self._hourly_rate = hourly_rate

    @property
    def id(self) -> int:
        """Gets the id of this UsersProjectUser.  # noqa: E501


        :return: The id of this UsersProjectUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this UsersProjectUser.


        :param id: The id of this UsersProjectUser.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def labour_cost(self) -> int:
        """Gets the labour_cost of this UsersProjectUser.  # noqa: E501


        :return: The labour_cost of this UsersProjectUser.  # noqa: E501
        :rtype: int
        """
        return self._labour_cost

    @labour_cost.setter
    def labour_cost(self, labour_cost: int):
        """Sets the labour_cost of this UsersProjectUser.


        :param labour_cost: The labour_cost of this UsersProjectUser.  # noqa: E501
        :type: int
        """

        self._labour_cost = labour_cost

    @property
    def manager(self) -> bool:
        """Gets the manager of this UsersProjectUser.  # noqa: E501


        :return: The manager of this UsersProjectUser.  # noqa: E501
        :rtype: bool
        """
        return self._manager

    @manager.setter
    def manager(self, manager: bool):
        """Sets the manager of this UsersProjectUser.


        :param manager: The manager of this UsersProjectUser.  # noqa: E501
        :type: bool
        """

        self._manager = manager

    @property
    def project_id(self) -> int:
        """Gets the project_id of this UsersProjectUser.  # noqa: E501


        :return: The project_id of this UsersProjectUser.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id: int):
        """Sets the project_id of this UsersProjectUser.


        :param project_id: The project_id of this UsersProjectUser.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def user_id(self) -> int:
        """Gets the user_id of this UsersProjectUser.  # noqa: E501


        :return: The user_id of this UsersProjectUser.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this UsersProjectUser.


        :param user_id: The user_id of this UsersProjectUser.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    def to_dict(self) -> dict[str, Any]:
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
        if issubclass(UsersProjectUser, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UsersProjectUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UsersProjectUser):
            return True

        return self.to_dict() != other.to_dict()
