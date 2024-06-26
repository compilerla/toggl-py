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


class TimesheetsGetPaginatedResponse:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"data": "list[TimesheetsAPITimesheet]", "page": "int", "per_page": "int", "total_count": "int"}

    attribute_map = {"data": "data", "page": "page", "per_page": "per_page", "total_count": "total_count"}

    def __init__(self, data=None, page=None, per_page=None, total_count=None, _configuration=None):  # noqa: E501
        """TimesheetsGetPaginatedResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._data = None
        self._page = None
        self._per_page = None
        self._total_count = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page
        if total_count is not None:
            self.total_count = total_count

    @property
    def data(self):
        """Gets the data of this TimesheetsGetPaginatedResponse.  # noqa: E501


        :return: The data of this TimesheetsGetPaginatedResponse.  # noqa: E501
        :rtype: list[TimesheetsAPITimesheet]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TimesheetsGetPaginatedResponse.


        :param data: The data of this TimesheetsGetPaginatedResponse.  # noqa: E501
        :type: list[TimesheetsAPITimesheet]
        """

        self._data = data

    @property
    def page(self):
        """Gets the page of this TimesheetsGetPaginatedResponse.  # noqa: E501


        :return: The page of this TimesheetsGetPaginatedResponse.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this TimesheetsGetPaginatedResponse.


        :param page: The page of this TimesheetsGetPaginatedResponse.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def per_page(self):
        """Gets the per_page of this TimesheetsGetPaginatedResponse.  # noqa: E501


        :return: The per_page of this TimesheetsGetPaginatedResponse.  # noqa: E501
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this TimesheetsGetPaginatedResponse.


        :param per_page: The per_page of this TimesheetsGetPaginatedResponse.  # noqa: E501
        :type: int
        """

        self._per_page = per_page

    @property
    def total_count(self):
        """Gets the total_count of this TimesheetsGetPaginatedResponse.  # noqa: E501


        :return: The total_count of this TimesheetsGetPaginatedResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this TimesheetsGetPaginatedResponse.


        :param total_count: The total_count of this TimesheetsGetPaginatedResponse.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if issubclass(TimesheetsGetPaginatedResponse, dict):
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
        if not isinstance(other, TimesheetsGetPaginatedResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimesheetsGetPaginatedResponse):
            return True

        return self.to_dict() != other.to_dict()
