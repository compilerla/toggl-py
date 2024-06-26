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


class MePostSessionHandlerRequestBody:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"remember_me": "bool"}

    attribute_map = {"remember_me": "remember_me"}

    def __init__(self, remember_me=None, _configuration=None):  # noqa: E501
        """MePostSessionHandlerRequestBody - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._remember_me = None
        self.discriminator = None

        if remember_me is not None:
            self.remember_me = remember_me

    @property
    def remember_me(self):
        """Gets the remember_me of this MePostSessionHandlerRequestBody.  # noqa: E501

        If true, the session cookie will be valid for 24 hours, otherwise until the browser is closed  # noqa: E501

        :return: The remember_me of this MePostSessionHandlerRequestBody.  # noqa: E501
        :rtype: bool
        """
        return self._remember_me

    @remember_me.setter
    def remember_me(self, remember_me):
        """Sets the remember_me of this MePostSessionHandlerRequestBody.

        If true, the session cookie will be valid for 24 hours, otherwise until the browser is closed  # noqa: E501

        :param remember_me: The remember_me of this MePostSessionHandlerRequestBody.  # noqa: E501
        :type: bool
        """

        self._remember_me = remember_me

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
        if issubclass(MePostSessionHandlerRequestBody, dict):
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
        if not isinstance(other, MePostSessionHandlerRequestBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MePostSessionHandlerRequestBody):
            return True

        return self.to_dict() != other.to_dict()
