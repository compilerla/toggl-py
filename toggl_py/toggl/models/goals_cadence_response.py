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


class GoalsCadenceResponse:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"goal_id": "int", "parameters": "list[GoalsCadenceParameter]"}

    attribute_map = {"goal_id": "goal_id", "parameters": "parameters"}

    def __init__(self, goal_id=None, parameters=None, _configuration=None):  # noqa: E501
        """GoalsCadenceResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._goal_id = None
        self._parameters = None
        self.discriminator = None

        if goal_id is not None:
            self.goal_id = goal_id
        if parameters is not None:
            self.parameters = parameters

    @property
    def goal_id(self):
        """Gets the goal_id of this GoalsCadenceResponse.  # noqa: E501


        :return: The goal_id of this GoalsCadenceResponse.  # noqa: E501
        :rtype: int
        """
        return self._goal_id

    @goal_id.setter
    def goal_id(self, goal_id):
        """Sets the goal_id of this GoalsCadenceResponse.


        :param goal_id: The goal_id of this GoalsCadenceResponse.  # noqa: E501
        :type: int
        """

        self._goal_id = goal_id

    @property
    def parameters(self):
        """Gets the parameters of this GoalsCadenceResponse.  # noqa: E501


        :return: The parameters of this GoalsCadenceResponse.  # noqa: E501
        :rtype: list[GoalsCadenceParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this GoalsCadenceResponse.


        :param parameters: The parameters of this GoalsCadenceResponse.  # noqa: E501
        :type: list[GoalsCadenceParameter]
        """

        self._parameters = parameters

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
        if issubclass(GoalsCadenceResponse, dict):
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
        if not isinstance(other, GoalsCadenceResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GoalsCadenceResponse):
            return True

        return self.to_dict() != other.to_dict()
