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


class ModelsTimelineSettings:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {"record_timeline": "bool"}

    attribute_map = {"record_timeline": "record_timeline"}

    def __init__(self, record_timeline: bool = None, _configuration: Configuration = None):  # noqa: E501
        """
        ModelsTimelineSettings - a model defined in Swagger

        Parameters:
          record_timeline (bool): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._record_timeline = None
        self.discriminator = None

        if record_timeline is not None:
            self.record_timeline = record_timeline

    @property
    def record_timeline(self) -> bool:
        """Gets the record_timeline of this ModelsTimelineSettings.  # noqa: E501


        :return: The record_timeline of this ModelsTimelineSettings.  # noqa: E501
        :rtype: bool
        """
        return self._record_timeline

    @record_timeline.setter
    def record_timeline(self, record_timeline: bool):
        """Sets the record_timeline of this ModelsTimelineSettings.


        :param record_timeline: The record_timeline of this ModelsTimelineSettings.  # noqa: E501
        :type: bool
        """

        self._record_timeline = record_timeline

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
        if issubclass(ModelsTimelineSettings, dict):
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
        if not isinstance(other, ModelsTimelineSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsTimelineSettings):
            return True

        return self.to_dict() != other.to_dict()
