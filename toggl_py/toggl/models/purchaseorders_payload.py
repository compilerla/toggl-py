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


class PurchaseordersPayload:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"user_count": "int"}

    attribute_map = {"user_count": "user_count"}

    def __init__(self, user_count=None, _configuration=None):  # noqa: E501
        """PurchaseordersPayload - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_count = None
        self.discriminator = None

        self.user_count = user_count

    @property
    def user_count(self):
        """Gets the user_count of this PurchaseordersPayload.  # noqa: E501


        :return: The user_count of this PurchaseordersPayload.  # noqa: E501
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this PurchaseordersPayload.


        :param user_count: The user_count of this PurchaseordersPayload.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and user_count is None:
            raise ValueError("Invalid value for `user_count`, must not be `None`")  # noqa: E501
        if self._configuration.client_side_validation and user_count is not None and user_count < 1:  # noqa: E501
            raise ValueError("Invalid value for `user_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self._user_count = user_count

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
        if issubclass(PurchaseordersPayload, dict):
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
        if not isinstance(other, PurchaseordersPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PurchaseordersPayload):
            return True

        return self.to_dict() != other.to_dict()