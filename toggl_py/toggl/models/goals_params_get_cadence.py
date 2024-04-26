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


class GoalsParamsGetCadence:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"amount": "int", "archived": "str", "goal": "list[int]", "offset": "int"}

    attribute_map = {"amount": "amount", "archived": "archived", "goal": "goal", "offset": "offset"}

    def __init__(self, amount=None, archived=None, goal=None, offset=None, _configuration=None):  # noqa: E501
        """GoalsParamsGetCadence - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._amount = None
        self._archived = None
        self._goal = None
        self._offset = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if archived is not None:
            self.archived = archived
        if goal is not None:
            self.goal = goal
        if offset is not None:
            self.offset = offset

    @property
    def amount(self):
        """Gets the amount of this GoalsParamsGetCadence.  # noqa: E501


        :return: The amount of this GoalsParamsGetCadence.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GoalsParamsGetCadence.


        :param amount: The amount of this GoalsParamsGetCadence.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def archived(self):
        """Gets the archived of this GoalsParamsGetCadence.  # noqa: E501


        :return: The archived of this GoalsParamsGetCadence.  # noqa: E501
        :rtype: str
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this GoalsParamsGetCadence.


        :param archived: The archived of this GoalsParamsGetCadence.  # noqa: E501
        :type: str
        """

        self._archived = archived

    @property
    def goal(self):
        """Gets the goal of this GoalsParamsGetCadence.  # noqa: E501


        :return: The goal of this GoalsParamsGetCadence.  # noqa: E501
        :rtype: list[int]
        """
        return self._goal

    @goal.setter
    def goal(self, goal):
        """Sets the goal of this GoalsParamsGetCadence.


        :param goal: The goal of this GoalsParamsGetCadence.  # noqa: E501
        :type: list[int]
        """

        self._goal = goal

    @property
    def offset(self):
        """Gets the offset of this GoalsParamsGetCadence.  # noqa: E501


        :return: The offset of this GoalsParamsGetCadence.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this GoalsParamsGetCadence.


        :param offset: The offset of this GoalsParamsGetCadence.  # noqa: E501
        :type: int
        """

        self._offset = offset

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
        if issubclass(GoalsParamsGetCadence, dict):
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
        if not isinstance(other, GoalsParamsGetCadence):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GoalsParamsGetCadence):
            return True

        return self.to_dict() != other.to_dict()
