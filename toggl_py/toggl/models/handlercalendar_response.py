"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

from __future__ import annotations  # noqa: F401
import pprint
import re  # noqa: F401
from datetime import datetime  # noqa: F401
from typing import Any

from toggl.configuration import Configuration


class HandlercalendarResponse:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {"fetched_events": "int"}

    attribute_map = {"fetched_events": "fetched_events"}

    def __init__(self, fetched_events: int = None, _configuration: Configuration = None):  # noqa: E501
        """
        HandlercalendarResponse - a model defined in Swagger

        Parameters:
          fetched_events (int): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._fetched_events = None
        self.discriminator = None

        if fetched_events is not None:
            self.fetched_events = fetched_events

    @property
    def fetched_events(self) -> int:
        """Gets the fetched_events of this HandlercalendarResponse.  # noqa: E501


        :return: The fetched_events of this HandlercalendarResponse.  # noqa: E501
        :rtype: int
        """
        return self._fetched_events

    @fetched_events.setter
    def fetched_events(self, fetched_events: int):
        """Sets the fetched_events of this HandlercalendarResponse.


        :param fetched_events: The fetched_events of this HandlercalendarResponse.  # noqa: E501
        :type: int
        """

        self._fetched_events = fetched_events

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
        if issubclass(HandlercalendarResponse, dict):
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
        if not isinstance(other, HandlercalendarResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HandlercalendarResponse):
            return True

        return self.to_dict() != other.to_dict()
