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


class ClientsDataTrendsGraph:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"data": "list[ClientsDataTrendsGraphData]", "resolution": "str"}

    attribute_map = {"data": "data", "resolution": "resolution"}

    def __init__(self, data=None, resolution=None, _configuration=None):  # noqa: E501
        """ClientsDataTrendsGraph - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._data = None
        self._resolution = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if resolution is not None:
            self.resolution = resolution

    @property
    def data(self):
        """Gets the data of this ClientsDataTrendsGraph.  # noqa: E501


        :return: The data of this ClientsDataTrendsGraph.  # noqa: E501
        :rtype: list[ClientsDataTrendsGraphData]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ClientsDataTrendsGraph.


        :param data: The data of this ClientsDataTrendsGraph.  # noqa: E501
        :type: list[ClientsDataTrendsGraphData]
        """

        self._data = data

    @property
    def resolution(self):
        """Gets the resolution of this ClientsDataTrendsGraph.  # noqa: E501


        :return: The resolution of this ClientsDataTrendsGraph.  # noqa: E501
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this ClientsDataTrendsGraph.


        :param resolution: The resolution of this ClientsDataTrendsGraph.  # noqa: E501
        :type: str
        """

        self._resolution = resolution

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
        if issubclass(ClientsDataTrendsGraph, dict):
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
        if not isinstance(other, ClientsDataTrendsGraph):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClientsDataTrendsGraph):
            return True

        return self.to_dict() != other.to_dict()