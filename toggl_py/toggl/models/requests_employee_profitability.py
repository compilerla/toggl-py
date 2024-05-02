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
from toggl.models.utils_int64_slice import UtilsInt64Slice  # noqa: F401


class RequestsEmployeeProfitability:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
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
        currency: str = None,
        end_date: str = None,
        group_ids: UtilsInt64Slice = None,
        resolution: str = None,
        rounding: int = None,
        rounding_minutes: int = None,
        start_date: str = None,
        user_ids: UtilsInt64Slice = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        RequestsEmployeeProfitability - a model defined in Swagger

        Parameters:
          currency (str): Required
          end_date (str): Optional
          group_ids (UtilsInt64Slice): Optional
          resolution (str): Optional
          rounding (int): Optional
          rounding_minutes (int): Optional
          start_date (str): Optional
          user_ids (UtilsInt64Slice): Optional
        """
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
    def currency(self) -> str:
        """Gets the currency of this RequestsEmployeeProfitability.  # noqa: E501


        :return: The currency of this RequestsEmployeeProfitability.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency: str):
        """Sets the currency of this RequestsEmployeeProfitability.


        :param currency: The currency of this RequestsEmployeeProfitability.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def end_date(self) -> str:
        """Gets the end_date of this RequestsEmployeeProfitability.  # noqa: E501


        :return: The end_date of this RequestsEmployeeProfitability.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: str):
        """Sets the end_date of this RequestsEmployeeProfitability.


        :param end_date: The end_date of this RequestsEmployeeProfitability.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def group_ids(self) -> UtilsInt64Slice:
        """Gets the group_ids of this RequestsEmployeeProfitability.  # noqa: E501


        :return: The group_ids of this RequestsEmployeeProfitability.  # noqa: E501
        :rtype: UtilsInt64Slice
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids: UtilsInt64Slice):
        """Sets the group_ids of this RequestsEmployeeProfitability.


        :param group_ids: The group_ids of this RequestsEmployeeProfitability.  # noqa: E501
        :type: UtilsInt64Slice
        """

        self._group_ids = group_ids

    @property
    def resolution(self) -> str:
        """Gets the resolution of this RequestsEmployeeProfitability.  # noqa: E501


        :return: The resolution of this RequestsEmployeeProfitability.  # noqa: E501
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution: str):
        """Sets the resolution of this RequestsEmployeeProfitability.


        :param resolution: The resolution of this RequestsEmployeeProfitability.  # noqa: E501
        :type: str
        """

        self._resolution = resolution

    @property
    def rounding(self) -> int:
        """Gets the rounding of this RequestsEmployeeProfitability.  # noqa: E501


        :return: The rounding of this RequestsEmployeeProfitability.  # noqa: E501
        :rtype: int
        """
        return self._rounding

    @rounding.setter
    def rounding(self, rounding: int):
        """Sets the rounding of this RequestsEmployeeProfitability.


        :param rounding: The rounding of this RequestsEmployeeProfitability.  # noqa: E501
        :type: int
        """

        self._rounding = rounding

    @property
    def rounding_minutes(self) -> int:
        """Gets the rounding_minutes of this RequestsEmployeeProfitability.  # noqa: E501


        :return: The rounding_minutes of this RequestsEmployeeProfitability.  # noqa: E501
        :rtype: int
        """
        return self._rounding_minutes

    @rounding_minutes.setter
    def rounding_minutes(self, rounding_minutes: int):
        """Sets the rounding_minutes of this RequestsEmployeeProfitability.


        :param rounding_minutes: The rounding_minutes of this RequestsEmployeeProfitability.  # noqa: E501
        :type: int
        """

        self._rounding_minutes = rounding_minutes

    @property
    def start_date(self) -> str:
        """Gets the start_date of this RequestsEmployeeProfitability.  # noqa: E501


        :return: The start_date of this RequestsEmployeeProfitability.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: str):
        """Sets the start_date of this RequestsEmployeeProfitability.


        :param start_date: The start_date of this RequestsEmployeeProfitability.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def user_ids(self) -> UtilsInt64Slice:
        """Gets the user_ids of this RequestsEmployeeProfitability.  # noqa: E501


        :return: The user_ids of this RequestsEmployeeProfitability.  # noqa: E501
        :rtype: UtilsInt64Slice
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids: UtilsInt64Slice):
        """Sets the user_ids of this RequestsEmployeeProfitability.


        :param user_ids: The user_ids of this RequestsEmployeeProfitability.  # noqa: E501
        :type: UtilsInt64Slice
        """

        self._user_ids = user_ids

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
        if issubclass(RequestsEmployeeProfitability, dict):
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
        if not isinstance(other, RequestsEmployeeProfitability):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequestsEmployeeProfitability):
            return True

        return self.to_dict() != other.to_dict()
