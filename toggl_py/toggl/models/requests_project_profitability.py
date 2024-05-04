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


class RequestsProjectProfitability:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "billable": "bool",
        "client_ids": "list[int]",
        "currency": "str",
        "end_date": "str",
        "project_ids": "list[int]",
        "resolution": "str",
        "rounding": "int",
        "rounding_minutes": "int",
        "start_date": "str",
    }

    attribute_map = {
        "billable": "billable",
        "client_ids": "client_ids",
        "currency": "currency",
        "end_date": "end_date",
        "project_ids": "project_ids",
        "resolution": "resolution",
        "rounding": "rounding",
        "rounding_minutes": "rounding_minutes",
        "start_date": "start_date",
    }

    def __init__(
        self,
        currency: str,
        billable: bool = None,
        client_ids: list[int] = None,
        end_date: str = None,
        project_ids: list[int] = None,
        resolution: str = None,
        rounding: int = None,
        rounding_minutes: int = None,
        start_date: str = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        RequestsProjectProfitability - a model defined in Swagger

        Parameters:
          currency (str): Required
          billable (bool): Optional
          client_ids (list[int]): Optional
          end_date (str): Optional
          project_ids (list[int]): Optional
          resolution (str): Optional
          rounding (int): Optional
          rounding_minutes (int): Optional
          start_date (str): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._billable = None
        self._client_ids = None
        self._currency = None
        self._end_date = None
        self._project_ids = None
        self._resolution = None
        self._rounding = None
        self._rounding_minutes = None
        self._start_date = None
        self.discriminator = None

        if billable is not None:
            self.billable = billable
        if client_ids is not None:
            self.client_ids = client_ids
        self.currency = currency
        if end_date is not None:
            self.end_date = end_date
        if project_ids is not None:
            self.project_ids = project_ids
        if resolution is not None:
            self.resolution = resolution
        if rounding is not None:
            self.rounding = rounding
        if rounding_minutes is not None:
            self.rounding_minutes = rounding_minutes
        if start_date is not None:
            self.start_date = start_date

    @property
    def billable(self) -> bool:
        """Gets the billable of this RequestsProjectProfitability.  # noqa: E501

        Whether the project is set as billable, optional, premium feature.  # noqa: E501

        :return: The billable of this RequestsProjectProfitability.  # noqa: E501
        :rtype: bool
        """
        return self._billable

    @billable.setter
    def billable(self, billable: bool):
        """Sets the billable of this RequestsProjectProfitability.

        Whether the project is set as billable, optional, premium feature.  # noqa: E501

        :param billable: The billable of this RequestsProjectProfitability.  # noqa: E501
        :type: bool
        """

        self._billable = billable

    @property
    def client_ids(self) -> list[int]:
        """Gets the client_ids of this RequestsProjectProfitability.  # noqa: E501

        Client IDs, optional. A nil entry on this list means that only projects without client will be selected.  # noqa: E501

        :return: The client_ids of this RequestsProjectProfitability.  # noqa: E501
        :rtype: list[int]
        """
        return self._client_ids

    @client_ids.setter
    def client_ids(self, client_ids: list[int]):
        """Sets the client_ids of this RequestsProjectProfitability.

        Client IDs, optional. A nil entry on this list means that only projects without client will be selected.  # noqa: E501

        :param client_ids: The client_ids of this RequestsProjectProfitability.  # noqa: E501
        :type: list[int]
        """

        self._client_ids = client_ids

    @property
    def currency(self) -> str:
        """Gets the currency of this RequestsProjectProfitability.  # noqa: E501

        Currency, example: \"usd\".  # noqa: E501

        :return: The currency of this RequestsProjectProfitability.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency: str):
        """Sets the currency of this RequestsProjectProfitability.

        Currency, example: \"usd\".  # noqa: E501

        :param currency: The currency of this RequestsProjectProfitability.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def end_date(self) -> str:
        """Gets the end_date of this RequestsProjectProfitability.  # noqa: E501

        End date, optional, example: time.DateOnly. Should be greater than Start date.  # noqa: E501

        :return: The end_date of this RequestsProjectProfitability.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: str):
        """Sets the end_date of this RequestsProjectProfitability.

        End date, optional, example: time.DateOnly. Should be greater than Start date.  # noqa: E501

        :param end_date: The end_date of this RequestsProjectProfitability.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def project_ids(self) -> list[int]:
        """Gets the project_ids of this RequestsProjectProfitability.  # noqa: E501

        Project IDS, optional.  # noqa: E501

        :return: The project_ids of this RequestsProjectProfitability.  # noqa: E501
        :rtype: list[int]
        """
        return self._project_ids

    @project_ids.setter
    def project_ids(self, project_ids: list[int]):
        """Sets the project_ids of this RequestsProjectProfitability.

        Project IDS, optional.  # noqa: E501

        :param project_ids: The project_ids of this RequestsProjectProfitability.  # noqa: E501
        :type: list[int]
        """

        self._project_ids = project_ids

    @property
    def resolution(self) -> str:
        """Gets the resolution of this RequestsProjectProfitability.  # noqa: E501

        Resolution, optional. Can be \"day\", \"week\" or \"month\".  # noqa: E501

        :return: The resolution of this RequestsProjectProfitability.  # noqa: E501
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution: str):
        """Sets the resolution of this RequestsProjectProfitability.

        Resolution, optional. Can be \"day\", \"week\" or \"month\".  # noqa: E501

        :param resolution: The resolution of this RequestsProjectProfitability.  # noqa: E501
        :type: str
        """

        self._resolution = resolution

    @property
    def rounding(self) -> int:
        """Gets the rounding of this RequestsProjectProfitability.  # noqa: E501

        Rounding, optional, duration rounding settings, premium feature.  # noqa: E501

        :return: The rounding of this RequestsProjectProfitability.  # noqa: E501
        :rtype: int
        """
        return self._rounding

    @rounding.setter
    def rounding(self, rounding: int):
        """Sets the rounding of this RequestsProjectProfitability.

        Rounding, optional, duration rounding settings, premium feature.  # noqa: E501

        :param rounding: The rounding of this RequestsProjectProfitability.  # noqa: E501
        :type: int
        """

        self._rounding = rounding

    @property
    def rounding_minutes(self) -> int:
        """Gets the rounding_minutes of this RequestsProjectProfitability.  # noqa: E501

        RoundingMinutes, optional, duration rounding minutes settings, premium feature.  # noqa: E501

        :return: The rounding_minutes of this RequestsProjectProfitability.  # noqa: E501
        :rtype: int
        """
        return self._rounding_minutes

    @rounding_minutes.setter
    def rounding_minutes(self, rounding_minutes: int):
        """Sets the rounding_minutes of this RequestsProjectProfitability.

        RoundingMinutes, optional, duration rounding minutes settings, premium feature.  # noqa: E501

        :param rounding_minutes: The rounding_minutes of this RequestsProjectProfitability.  # noqa: E501
        :type: int
        """

        self._rounding_minutes = rounding_minutes

    @property
    def start_date(self) -> str:
        """Gets the start_date of this RequestsProjectProfitability.  # noqa: E501

        Start date, optional, example: time.DateOnly. Should be less than End date.  # noqa: E501

        :return: The start_date of this RequestsProjectProfitability.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: str):
        """Sets the start_date of this RequestsProjectProfitability.

        Start date, optional, example: time.DateOnly. Should be less than End date.  # noqa: E501

        :param start_date: The start_date of this RequestsProjectProfitability.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

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
        if issubclass(RequestsProjectProfitability, dict):
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
        if not isinstance(other, RequestsProjectProfitability):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequestsProjectProfitability):
            return True

        return self.to_dict() != other.to_dict()
