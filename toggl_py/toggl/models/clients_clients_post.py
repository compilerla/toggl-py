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


class ClientsClientsPost:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {"ids": "list[int]", "name": "str", "start": "int"}

    attribute_map = {"ids": "ids", "name": "name", "start": "start"}

    def __init__(
        self, ids: list[int] = None, name: str = None, start: int = None, _configuration: Configuration = None  # noqa: E501
    ):
        """
        ClientsClientsPost - a model defined in Swagger

        Parameters:
          ids (list[int]): Optional
          name (str): Optional
          start (int): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ids = None
        self._name = None
        self._start = None
        self.discriminator = None

        if ids is not None:
            self.ids = ids
        if name is not None:
            self.name = name
        if start is not None:
            self.start = start

    @property
    def ids(self) -> list[int]:
        """Gets the ids of this ClientsClientsPost.  # noqa: E501


        :return: The ids of this ClientsClientsPost.  # noqa: E501
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids: list[int]):
        """Sets the ids of this ClientsClientsPost.


        :param ids: The ids of this ClientsClientsPost.  # noqa: E501
        :type: list[int]
        """

        self._ids = ids

    @property
    def name(self) -> str:
        """Gets the name of this ClientsClientsPost.  # noqa: E501


        :return: The name of this ClientsClientsPost.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ClientsClientsPost.


        :param name: The name of this ClientsClientsPost.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def start(self) -> int:
        """Gets the start of this ClientsClientsPost.  # noqa: E501


        :return: The start of this ClientsClientsPost.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start: int):
        """Sets the start of this ClientsClientsPost.


        :param start: The start of this ClientsClientsPost.  # noqa: E501
        :type: int
        """

        self._start = start

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
        if issubclass(ClientsClientsPost, dict):
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
        if not isinstance(other, ClientsClientsPost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClientsClientsPost):
            return True

        return self.to_dict() != other.to_dict()
