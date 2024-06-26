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


class DtoOrdinationRequest:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"direction": "str", "nulls": "str", "_property": "str"}

    attribute_map = {"direction": "direction", "nulls": "nulls", "_property": "property"}

    def __init__(self, direction=None, nulls=None, _property=None, _configuration=None):  # noqa: E501
        """DtoOrdinationRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._direction = None
        self._nulls = None
        self.__property = None
        self.discriminator = None

        if direction is not None:
            self.direction = direction
        if nulls is not None:
            self.nulls = nulls
        self._property = _property

    @property
    def direction(self):
        """Gets the direction of this DtoOrdinationRequest.  # noqa: E501


        :return: The direction of this DtoOrdinationRequest.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this DtoOrdinationRequest.


        :param direction: The direction of this DtoOrdinationRequest.  # noqa: E501
        :type: str
        """

        self._direction = direction

    @property
    def nulls(self):
        """Gets the nulls of this DtoOrdinationRequest.  # noqa: E501


        :return: The nulls of this DtoOrdinationRequest.  # noqa: E501
        :rtype: str
        """
        return self._nulls

    @nulls.setter
    def nulls(self, nulls):
        """Sets the nulls of this DtoOrdinationRequest.


        :param nulls: The nulls of this DtoOrdinationRequest.  # noqa: E501
        :type: str
        """

        self._nulls = nulls

    @property
    def _property(self):
        """Gets the _property of this DtoOrdinationRequest.  # noqa: E501


        :return: The _property of this DtoOrdinationRequest.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this DtoOrdinationRequest.


        :param _property: The _property of this DtoOrdinationRequest.  # noqa: E501
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
        if issubclass(DtoOrdinationRequest, dict):
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
        if not isinstance(other, DtoOrdinationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DtoOrdinationRequest):
            return True

        return self.to_dict() != other.to_dict()
