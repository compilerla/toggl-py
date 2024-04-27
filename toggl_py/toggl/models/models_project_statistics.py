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


class ModelsProjectStatistics:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"earliest_time_entry": "str", "latest_time_entry": "str"}

    attribute_map = {"earliest_time_entry": "earliest_time_entry", "latest_time_entry": "latest_time_entry"}

    def __init__(self, earliest_time_entry=None, latest_time_entry=None, _configuration=None):  # noqa: E501
        """ModelsProjectStatistics - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._earliest_time_entry = None
        self._latest_time_entry = None
        self.discriminator = None

        if earliest_time_entry is not None:
            self.earliest_time_entry = earliest_time_entry
        if latest_time_entry is not None:
            self.latest_time_entry = latest_time_entry

    @property
    def earliest_time_entry(self):
        """Gets the earliest_time_entry of this ModelsProjectStatistics.  # noqa: E501


        :return: The earliest_time_entry of this ModelsProjectStatistics.  # noqa: E501
        :rtype: str
        """
        return self._earliest_time_entry

    @earliest_time_entry.setter
    def earliest_time_entry(self, earliest_time_entry):
        """Sets the earliest_time_entry of this ModelsProjectStatistics.


        :param earliest_time_entry: The earliest_time_entry of this ModelsProjectStatistics.  # noqa: E501
        :type: str
        """

        self._earliest_time_entry = earliest_time_entry

    @property
    def latest_time_entry(self):
        """Gets the latest_time_entry of this ModelsProjectStatistics.  # noqa: E501


        :return: The latest_time_entry of this ModelsProjectStatistics.  # noqa: E501
        :rtype: str
        """
        return self._latest_time_entry

    @latest_time_entry.setter
    def latest_time_entry(self, latest_time_entry):
        """Sets the latest_time_entry of this ModelsProjectStatistics.


        :param latest_time_entry: The latest_time_entry of this ModelsProjectStatistics.  # noqa: E501
        :type: str
        """

        self._latest_time_entry = latest_time_entry

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
        if issubclass(ModelsProjectStatistics, dict):
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
        if not isinstance(other, ModelsProjectStatistics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsProjectStatistics):
            return True

        return self.to_dict() != other.to_dict()
