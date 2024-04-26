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


class DtoAggregationRequest:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"alias": "str", "function": "str", "_property": "str"}

    attribute_map = {"alias": "alias", "function": "function", "_property": "property"}

    def __init__(self, alias=None, function=None, _property=None, _configuration=None):  # noqa: E501
        """DtoAggregationRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alias = None
        self._function = None
        self.__property = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        self.function = function
        self._property = _property

    @property
    def alias(self):
        """Gets the alias of this DtoAggregationRequest.  # noqa: E501


        :return: The alias of this DtoAggregationRequest.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this DtoAggregationRequest.


        :param alias: The alias of this DtoAggregationRequest.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def function(self):
        """Gets the function of this DtoAggregationRequest.  # noqa: E501


        :return: The function of this DtoAggregationRequest.  # noqa: E501
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this DtoAggregationRequest.


        :param function: The function of this DtoAggregationRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and function is None:
            raise ValueError("Invalid value for `function`, must not be `None`")  # noqa: E501

        self._function = function

    @property
    def _property(self):
        """Gets the _property of this DtoAggregationRequest.  # noqa: E501


        :return: The _property of this DtoAggregationRequest.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this DtoAggregationRequest.


        :param _property: The _property of this DtoAggregationRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and _property is None:
            raise ValueError("Invalid value for `_property`, must not be `None`")  # noqa: E501

        self.__property = _property

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
        if issubclass(DtoAggregationRequest, dict):
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
        if not isinstance(other, DtoAggregationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DtoAggregationRequest):
            return True

        return self.to_dict() != other.to_dict()
