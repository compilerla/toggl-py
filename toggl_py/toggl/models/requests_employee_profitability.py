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


class RequestsEmployeeProfitability:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "currency": "str",
        "end_date": "str",
        "group_ids": "UtilsInt64Slice",
        "resolution": "str",
        "rounding": "int",
        "rounding_minutes": "int",
        "start_date": "str",
        "user_ids": "UtilsInt64Slice",
    }

    attribute_map = {
        "currency": "currency",
        "end_date": "end_date",
        "group_ids": "group_ids",
        "resolution": "resolution",
        "rounding": "rounding",
        "rounding_minutes": "rounding_minutes",
        "start_date": "start_date",
        "user_ids": "user_ids",
    }

    def __init__(
        self,
        currency=None,
        end_date=None,
        group_ids=None,
        resolution=None,
        rounding=None,
        rounding_minutes=None,
        start_date=None,
        user_ids=None,
        _configuration=None,
    ):  # noqa: E501
        """RequestsEmployeeProfitability - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._currency = None
        self._end_date = None
        self._group_ids = None
        self._resolution = None
        self._rounding = None
        self._rounding_minutes = None
        self._start_date = None
        self._user_ids = None
        self.discriminator = None

        self.currency = currency
        if end_date is not None:
            self.end_date = end_date
        if group_ids is not None:
            self.group_ids = group_ids
        if resolution is not None:
            self.resolution = resolution
        if rounding is not None:
            self.rounding = rounding
        if rounding_minutes is not None:
            self.rounding_minutes = rounding_minutes
        if start_date is not None:
            self.start_date = start_date
        if user_ids is not None:
            self.user_ids = user_ids

    @property
    def currency(self):
        """Gets the currency of this RequestsEmployeeProfitability.  # noqa: E501


        :return: The currency of this RequestsEmployeeProfitability.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this RequestsEmployeeProfitability.


        :param currency: The currency of this RequestsEmployeeProfitability.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def end_date(self):
        """Gets the end_date of this RequestsEmployeeProfitability.  # noqa: E501


        :return: The end_date of this RequestsEmployeeProfitability.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this RequestsEmployeeProfitability.


        :param end_date: The end_date of this RequestsEmployeeProfitability.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def group_ids(self):
        """Gets the group_ids of this RequestsEmployeeProfitability.  # noqa: E501


        :return: The group_ids of this RequestsEmployeeProfitability.  # noqa: E501
        :rtype: UtilsInt64Slice
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this RequestsEmployeeProfitability.


        :param group_ids: The group_ids of this RequestsEmployeeProfitability.  # noqa: E501
        :type: UtilsInt64Slice
        """

        self._group_ids = group_ids

    @property
    def resolution(self):
        """Gets the resolution of this RequestsEmployeeProfitability.  # noqa: E501


        :return: The resolution of this RequestsEmployeeProfitability.  # noqa: E501
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this RequestsEmployeeProfitability.


        :param resolution: The resolution of this RequestsEmployeeProfitability.  # noqa: E501
        :type: str
        """

        self._resolution = resolution

    @property
    def rounding(self):
        """Gets the rounding of this RequestsEmployeeProfitability.  # noqa: E501


        :return: The rounding of this RequestsEmployeeProfitability.  # noqa: E501
        :rtype: int
        """
        return self._rounding

    @rounding.setter
    def rounding(self, rounding):
        """Sets the rounding of this RequestsEmployeeProfitability.


        :param rounding: The rounding of this RequestsEmployeeProfitability.  # noqa: E501
        :type: int
        """

        self._rounding = rounding

    @property
    def rounding_minutes(self):
        """Gets the rounding_minutes of this RequestsEmployeeProfitability.  # noqa: E501


        :return: The rounding_minutes of this RequestsEmployeeProfitability.  # noqa: E501
        :rtype: int
        """
        return self._rounding_minutes

    @rounding_minutes.setter
    def rounding_minutes(self, rounding_minutes):
        """Sets the rounding_minutes of this RequestsEmployeeProfitability.


        :param rounding_minutes: The rounding_minutes of this RequestsEmployeeProfitability.  # noqa: E501
        :type: int
        """

        self._rounding_minutes = rounding_minutes

    @property
    def start_date(self):
        """Gets the start_date of this RequestsEmployeeProfitability.  # noqa: E501


        :return: The start_date of this RequestsEmployeeProfitability.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this RequestsEmployeeProfitability.


        :param start_date: The start_date of this RequestsEmployeeProfitability.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def user_ids(self):
        """Gets the user_ids of this RequestsEmployeeProfitability.  # noqa: E501


        :return: The user_ids of this RequestsEmployeeProfitability.  # noqa: E501
        :rtype: UtilsInt64Slice
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this RequestsEmployeeProfitability.


        :param user_ids: The user_ids of this RequestsEmployeeProfitability.  # noqa: E501
        :type: UtilsInt64Slice
        """

        self._user_ids = user_ids

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
        if issubclass(RequestsEmployeeProfitability, dict):
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
        if not isinstance(other, RequestsEmployeeProfitability):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequestsEmployeeProfitability):
            return True

        return self.to_dict() != other.to_dict()
