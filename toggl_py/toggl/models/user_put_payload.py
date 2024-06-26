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


class UserPutPayload:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"labour_cost": "int", "manager": "bool", "rate": "float", "rate_change_mode": "str"}

    attribute_map = {
        "labour_cost": "labour_cost",
        "manager": "manager",
        "rate": "rate",
        "rate_change_mode": "rate_change_mode",
    }

    def __init__(self, labour_cost=None, manager=None, rate=None, rate_change_mode=None, _configuration=None):  # noqa: E501
        """UserPutPayload - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._labour_cost = None
        self._manager = None
        self._rate = None
        self._rate_change_mode = None
        self.discriminator = None

        if labour_cost is not None:
            self.labour_cost = labour_cost
        if manager is not None:
            self.manager = manager
        if rate is not None:
            self.rate = rate
        if rate_change_mode is not None:
            self.rate_change_mode = rate_change_mode

    @property
    def labour_cost(self):
        """Gets the labour_cost of this UserPutPayload.  # noqa: E501

        Labour cost for this project user  # noqa: E501

        :return: The labour_cost of this UserPutPayload.  # noqa: E501
        :rtype: int
        """
        return self._labour_cost

    @labour_cost.setter
    def labour_cost(self, labour_cost):
        """Sets the labour_cost of this UserPutPayload.

        Labour cost for this project user  # noqa: E501

        :param labour_cost: The labour_cost of this UserPutPayload.  # noqa: E501
        :type: int
        """

        self._labour_cost = labour_cost

    @property
    def manager(self):
        """Gets the manager of this UserPutPayload.  # noqa: E501

        Whether the user will be manager of the project  # noqa: E501

        :return: The manager of this UserPutPayload.  # noqa: E501
        :rtype: bool
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """Sets the manager of this UserPutPayload.

        Whether the user will be manager of the project  # noqa: E501

        :param manager: The manager of this UserPutPayload.  # noqa: E501
        :type: bool
        """

        self._manager = manager

    @property
    def rate(self):
        """Gets the rate of this UserPutPayload.  # noqa: E501

        Rate for this project user  # noqa: E501

        :return: The rate of this UserPutPayload.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this UserPutPayload.

        Rate for this project user  # noqa: E501

        :param rate: The rate of this UserPutPayload.  # noqa: E501
        :type: float
        """

        self._rate = rate

    @property
    def rate_change_mode(self):
        """Gets the rate_change_mode of this UserPutPayload.  # noqa: E501

        Rate change mode for this project user. Can be \"start-today\", \"override-current\", \"override-all\"  # noqa: E501

        :return: The rate_change_mode of this UserPutPayload.  # noqa: E501
        :rtype: str
        """
        return self._rate_change_mode

    @rate_change_mode.setter
    def rate_change_mode(self, rate_change_mode):
        """Sets the rate_change_mode of this UserPutPayload.

        Rate change mode for this project user. Can be \"start-today\", \"override-current\", \"override-all\"  # noqa: E501

        :param rate_change_mode: The rate_change_mode of this UserPutPayload.  # noqa: E501
        :type: str
        """

        self._rate_change_mode = rate_change_mode

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
        if issubclass(UserPutPayload, dict):
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
        if not isinstance(other, UserPutPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserPutPayload):
            return True

        return self.to_dict() != other.to_dict()
