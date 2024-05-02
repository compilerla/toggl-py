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


class SmailContactPayload:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {"email": "str", "message": "str", "name": "str"}

    attribute_map = {"email": "Email", "message": "Message", "name": "Name"}

    def __init__(
        self, email: str = None, message: str = None, name: str = None, _configuration: Configuration = None  # noqa: E501
    ):
        """
        SmailContactPayload - a model defined in Swagger

        Parameters:
          email (str): Optional
          message (str): Optional
          name (str): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._email = None
        self._message = None
        self._name = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if message is not None:
            self.message = message
        if name is not None:
            self.name = name

    @property
    def email(self) -> str:
        """Gets the email of this SmailContactPayload.  # noqa: E501


        :return: The email of this SmailContactPayload.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this SmailContactPayload.


        :param email: The email of this SmailContactPayload.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def message(self) -> str:
        """Gets the message of this SmailContactPayload.  # noqa: E501


        :return: The message of this SmailContactPayload.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this SmailContactPayload.


        :param message: The message of this SmailContactPayload.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def name(self) -> str:
        """Gets the name of this SmailContactPayload.  # noqa: E501


        :return: The name of this SmailContactPayload.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this SmailContactPayload.


        :param name: The name of this SmailContactPayload.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(SmailContactPayload, dict):
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
        if not isinstance(other, SmailContactPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmailContactPayload):
            return True

        return self.to_dict() != other.to_dict()
