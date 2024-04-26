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


class DtoProjectUserResponse:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
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
        group_id=None,
        hourly_rate=None,
        id=None,
        labour_cost=None,
        manager=None,
        project_id=None,
        user_id=None,
        _configuration=None,
    ):  # noqa: E501
        """DtoProjectUserResponse - a model defined in Swagger"""  # noqa: E501
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
    def group_id(self):
        """Gets the group_id of this DtoProjectUserResponse.  # noqa: E501


        :return: The group_id of this DtoProjectUserResponse.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this DtoProjectUserResponse.


        :param group_id: The group_id of this DtoProjectUserResponse.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def hourly_rate(self):
        """Gets the hourly_rate of this DtoProjectUserResponse.  # noqa: E501


        :return: The hourly_rate of this DtoProjectUserResponse.  # noqa: E501
        :rtype: float
        """
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, hourly_rate):
        """Sets the hourly_rate of this DtoProjectUserResponse.


        :param hourly_rate: The hourly_rate of this DtoProjectUserResponse.  # noqa: E501
        :type: float
        """

        self._hourly_rate = hourly_rate

    @property
    def id(self):
        """Gets the id of this DtoProjectUserResponse.  # noqa: E501


        :return: The id of this DtoProjectUserResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DtoProjectUserResponse.


        :param id: The id of this DtoProjectUserResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def labour_cost(self):
        """Gets the labour_cost of this DtoProjectUserResponse.  # noqa: E501


        :return: The labour_cost of this DtoProjectUserResponse.  # noqa: E501
        :rtype: int
        """
        return self._labour_cost

    @labour_cost.setter
    def labour_cost(self, labour_cost):
        """Sets the labour_cost of this DtoProjectUserResponse.


        :param labour_cost: The labour_cost of this DtoProjectUserResponse.  # noqa: E501
        :type: int
        """

        self._labour_cost = labour_cost

    @property
    def manager(self):
        """Gets the manager of this DtoProjectUserResponse.  # noqa: E501


        :return: The manager of this DtoProjectUserResponse.  # noqa: E501
        :rtype: bool
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """Sets the manager of this DtoProjectUserResponse.


        :param manager: The manager of this DtoProjectUserResponse.  # noqa: E501
        :type: bool
        """

        self._manager = manager

    @property
    def project_id(self):
        """Gets the project_id of this DtoProjectUserResponse.  # noqa: E501


        :return: The project_id of this DtoProjectUserResponse.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DtoProjectUserResponse.


        :param project_id: The project_id of this DtoProjectUserResponse.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def user_id(self):
        """Gets the user_id of this DtoProjectUserResponse.  # noqa: E501


        :return: The user_id of this DtoProjectUserResponse.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this DtoProjectUserResponse.


        :param user_id: The user_id of this DtoProjectUserResponse.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

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
        if issubclass(DtoProjectUserResponse, dict):
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
        if not isinstance(other, DtoProjectUserResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DtoProjectUserResponse):
            return True

        return self.to_dict() != other.to_dict()