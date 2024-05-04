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
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from toggl.models.utils_int64_slice import UtilsInt64Slice  # noqa: F401


class WeeklyDataRow:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "billable_amounts_in_cents": "UtilsInt64Slice",
        "billable_seconds": "UtilsInt64Slice",
        "client_name": "str",
        "currency": "str",
        "hourly_rate_in_cents": "int",
        "planned_task_id": "int",
        "project_color": "str",
        "project_hex_color": "str",
        "project_id": "int",
        "project_name": "str",
        "seconds": "UtilsInt64Slice",
        "user_id": "int",
        "user_name": "str",
    }

    attribute_map = {
        "billable_amounts_in_cents": "billable_amounts_in_cents",
        "billable_seconds": "billable_seconds",
        "client_name": "client_name",
        "currency": "currency",
        "hourly_rate_in_cents": "hourly_rate_in_cents",
        "planned_task_id": "planned_task_id",
        "project_color": "project_color",
        "project_hex_color": "project_hex_color",
        "project_id": "project_id",
        "project_name": "project_name",
        "seconds": "seconds",
        "user_id": "user_id",
        "user_name": "user_name",
    }

    def __init__(
        self,
        billable_amounts_in_cents: UtilsInt64Slice = None,
        billable_seconds: UtilsInt64Slice = None,
        client_name: str = None,
        currency: str = None,
        hourly_rate_in_cents: int = None,
        planned_task_id: int = None,
        project_color: str = None,
        project_hex_color: str = None,
        project_id: int = None,
        project_name: str = None,
        seconds: UtilsInt64Slice = None,
        user_id: int = None,
        user_name: str = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        WeeklyDataRow - a model defined in Swagger

        Parameters:
          billable_amounts_in_cents (UtilsInt64Slice): Optional
          billable_seconds (UtilsInt64Slice): Optional
          client_name (str): Optional
          currency (str): Optional
          hourly_rate_in_cents (int): Optional
          planned_task_id (int): Optional
          project_color (str): Optional
          project_hex_color (str): Optional
          project_id (int): Optional
          project_name (str): Optional
          seconds (UtilsInt64Slice): Optional
          user_id (int): Optional
          user_name (str): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._billable_amounts_in_cents = None
        self._billable_seconds = None
        self._client_name = None
        self._currency = None
        self._hourly_rate_in_cents = None
        self._planned_task_id = None
        self._project_color = None
        self._project_hex_color = None
        self._project_id = None
        self._project_name = None
        self._seconds = None
        self._user_id = None
        self._user_name = None
        self.discriminator = None

        if billable_amounts_in_cents is not None:
            self.billable_amounts_in_cents = billable_amounts_in_cents
        if billable_seconds is not None:
            self.billable_seconds = billable_seconds
        if client_name is not None:
            self.client_name = client_name
        if currency is not None:
            self.currency = currency
        if hourly_rate_in_cents is not None:
            self.hourly_rate_in_cents = hourly_rate_in_cents
        if planned_task_id is not None:
            self.planned_task_id = planned_task_id
        if project_color is not None:
            self.project_color = project_color
        if project_hex_color is not None:
            self.project_hex_color = project_hex_color
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if seconds is not None:
            self.seconds = seconds
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name

    @property
    def billable_amounts_in_cents(self) -> UtilsInt64Slice:
        """Gets the billable_amounts_in_cents of this WeeklyDataRow.  # noqa: E501


        :return: The billable_amounts_in_cents of this WeeklyDataRow.  # noqa: E501
        :rtype: UtilsInt64Slice
        """
        return self._billable_amounts_in_cents

    @billable_amounts_in_cents.setter
    def billable_amounts_in_cents(self, billable_amounts_in_cents: UtilsInt64Slice):
        """Sets the billable_amounts_in_cents of this WeeklyDataRow.


        :param billable_amounts_in_cents: The billable_amounts_in_cents of this WeeklyDataRow.  # noqa: E501
        :type: UtilsInt64Slice
        """

        self._billable_amounts_in_cents = billable_amounts_in_cents

    @property
    def billable_seconds(self) -> UtilsInt64Slice:
        """Gets the billable_seconds of this WeeklyDataRow.  # noqa: E501


        :return: The billable_seconds of this WeeklyDataRow.  # noqa: E501
        :rtype: UtilsInt64Slice
        """
        return self._billable_seconds

    @billable_seconds.setter
    def billable_seconds(self, billable_seconds: UtilsInt64Slice):
        """Sets the billable_seconds of this WeeklyDataRow.


        :param billable_seconds: The billable_seconds of this WeeklyDataRow.  # noqa: E501
        :type: UtilsInt64Slice
        """

        self._billable_seconds = billable_seconds

    @property
    def client_name(self) -> str:
        """Gets the client_name of this WeeklyDataRow.  # noqa: E501


        :return: The client_name of this WeeklyDataRow.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name: str):
        """Sets the client_name of this WeeklyDataRow.


        :param client_name: The client_name of this WeeklyDataRow.  # noqa: E501
        :type: str
        """

        self._client_name = client_name

    @property
    def currency(self) -> str:
        """Gets the currency of this WeeklyDataRow.  # noqa: E501


        :return: The currency of this WeeklyDataRow.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency: str):
        """Sets the currency of this WeeklyDataRow.


        :param currency: The currency of this WeeklyDataRow.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def hourly_rate_in_cents(self) -> int:
        """Gets the hourly_rate_in_cents of this WeeklyDataRow.  # noqa: E501

        In cents  # noqa: E501

        :return: The hourly_rate_in_cents of this WeeklyDataRow.  # noqa: E501
        :rtype: int
        """
        return self._hourly_rate_in_cents

    @hourly_rate_in_cents.setter
    def hourly_rate_in_cents(self, hourly_rate_in_cents: int):
        """Sets the hourly_rate_in_cents of this WeeklyDataRow.

        In cents  # noqa: E501

        :param hourly_rate_in_cents: The hourly_rate_in_cents of this WeeklyDataRow.  # noqa: E501
        :type: int
        """

        self._hourly_rate_in_cents = hourly_rate_in_cents

    @property
    def planned_task_id(self) -> int:
        """Gets the planned_task_id of this WeeklyDataRow.  # noqa: E501


        :return: The planned_task_id of this WeeklyDataRow.  # noqa: E501
        :rtype: int
        """
        return self._planned_task_id

    @planned_task_id.setter
    def planned_task_id(self, planned_task_id: int):
        """Sets the planned_task_id of this WeeklyDataRow.


        :param planned_task_id: The planned_task_id of this WeeklyDataRow.  # noqa: E501
        :type: int
        """

        self._planned_task_id = planned_task_id

    @property
    def project_color(self) -> str:
        """Gets the project_color of this WeeklyDataRow.  # noqa: E501


        :return: The project_color of this WeeklyDataRow.  # noqa: E501
        :rtype: str
        """
        return self._project_color

    @project_color.setter
    def project_color(self, project_color: str):
        """Sets the project_color of this WeeklyDataRow.


        :param project_color: The project_color of this WeeklyDataRow.  # noqa: E501
        :type: str
        """

        self._project_color = project_color

    @property
    def project_hex_color(self) -> str:
        """Gets the project_hex_color of this WeeklyDataRow.  # noqa: E501


        :return: The project_hex_color of this WeeklyDataRow.  # noqa: E501
        :rtype: str
        """
        return self._project_hex_color

    @project_hex_color.setter
    def project_hex_color(self, project_hex_color: str):
        """Sets the project_hex_color of this WeeklyDataRow.


        :param project_hex_color: The project_hex_color of this WeeklyDataRow.  # noqa: E501
        :type: str
        """

        self._project_hex_color = project_hex_color

    @property
    def project_id(self) -> int:
        """Gets the project_id of this WeeklyDataRow.  # noqa: E501


        :return: The project_id of this WeeklyDataRow.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id: int):
        """Sets the project_id of this WeeklyDataRow.


        :param project_id: The project_id of this WeeklyDataRow.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def project_name(self) -> str:
        """Gets the project_name of this WeeklyDataRow.  # noqa: E501


        :return: The project_name of this WeeklyDataRow.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name: str):
        """Sets the project_name of this WeeklyDataRow.


        :param project_name: The project_name of this WeeklyDataRow.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def seconds(self) -> UtilsInt64Slice:
        """Gets the seconds of this WeeklyDataRow.  # noqa: E501


        :return: The seconds of this WeeklyDataRow.  # noqa: E501
        :rtype: UtilsInt64Slice
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds: UtilsInt64Slice):
        """Sets the seconds of this WeeklyDataRow.


        :param seconds: The seconds of this WeeklyDataRow.  # noqa: E501
        :type: UtilsInt64Slice
        """

        self._seconds = seconds

    @property
    def user_id(self) -> int:
        """Gets the user_id of this WeeklyDataRow.  # noqa: E501


        :return: The user_id of this WeeklyDataRow.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this WeeklyDataRow.


        :param user_id: The user_id of this WeeklyDataRow.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def user_name(self) -> str:
        """Gets the user_name of this WeeklyDataRow.  # noqa: E501


        :return: The user_name of this WeeklyDataRow.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name: str):
        """Sets the user_name of this WeeklyDataRow.


        :param user_name: The user_name of this WeeklyDataRow.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if issubclass(WeeklyDataRow, dict):
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
        if not isinstance(other, WeeklyDataRow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WeeklyDataRow):
            return True

        return self.to_dict() != other.to_dict()
