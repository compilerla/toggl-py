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


class ClientsDataTrendsGraphData:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"clients": "list[ClientsReportClient]", "_date": "str"}

    attribute_map = {"clients": "clients", "_date": "date"}

    def __init__(self, clients=None, _date=None, _configuration=None):  # noqa: E501
        """ClientsDataTrendsGraphData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._clients = None
        self.__date = None
        self.discriminator = None

        if clients is not None:
            self.clients = clients
        if _date is not None:
            self._date = _date

    @property
    def clients(self):
        """Gets the clients of this ClientsDataTrendsGraphData.  # noqa: E501


        :return: The clients of this ClientsDataTrendsGraphData.  # noqa: E501
        :rtype: list[ClientsReportClient]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this ClientsDataTrendsGraphData.


        :param clients: The clients of this ClientsDataTrendsGraphData.  # noqa: E501
        :type: list[ClientsReportClient]
        """

        self._clients = clients

    @property
    def _date(self):
        """Gets the _date of this ClientsDataTrendsGraphData.  # noqa: E501


        :return: The _date of this ClientsDataTrendsGraphData.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ClientsDataTrendsGraphData.


        :param _date: The _date of this ClientsDataTrendsGraphData.  # noqa: E501
        :type: str
        """

        self.__date = _date

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
        if issubclass(ClientsDataTrendsGraphData, dict):
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
        if not isinstance(other, ClientsDataTrendsGraphData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClientsDataTrendsGraphData):
            return True

        return self.to_dict() != other.to_dict()