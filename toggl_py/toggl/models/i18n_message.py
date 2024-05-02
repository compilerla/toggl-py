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


class I18nMessage:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {"default_message": "str", "id": "str", "values": "dict(str, str)"}

    attribute_map = {"default_message": "default_message", "id": "id", "values": "values"}

    def __init__(
        self,
        default_message: str = None,
        id: str = None,
        values: dict[str, str] = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        I18nMessage - a model defined in Swagger

        Parameters:
          default_message (str): Optional
          id (str): Optional
          values (dict[str, str]): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._default_message = None
        self._id = None
        self._values = None
        self.discriminator = None

        if default_message is not None:
            self.default_message = default_message
        if id is not None:
            self.id = id
        if values is not None:
            self.values = values

    @property
    def default_message(self) -> str:
        """Gets the default_message of this I18nMessage.  # noqa: E501


        :return: The default_message of this I18nMessage.  # noqa: E501
        :rtype: str
        """
        return self._default_message

    @default_message.setter
    def default_message(self, default_message: str):
        """Sets the default_message of this I18nMessage.


        :param default_message: The default_message of this I18nMessage.  # noqa: E501
        :type: str
        """

        self._default_message = default_message

    @property
    def id(self) -> str:
        """Gets the id of this I18nMessage.  # noqa: E501


        :return: The id of this I18nMessage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this I18nMessage.


        :param id: The id of this I18nMessage.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def values(self) -> dict[str, str]:
        """Gets the values of this I18nMessage.  # noqa: E501


        :return: The values of this I18nMessage.  # noqa: E501
        :rtype: dict[str, str]
        """
        return self._values

    @values.setter
    def values(self, values: dict[str, str]):
        """Sets the values of this I18nMessage.


        :param values: The values of this I18nMessage.  # noqa: E501
        :type: dict[str, str]
        """

        self._values = values

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
        if issubclass(I18nMessage, dict):
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
        if not isinstance(other, I18nMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, I18nMessage):
            return True

        return self.to_dict() != other.to_dict()
