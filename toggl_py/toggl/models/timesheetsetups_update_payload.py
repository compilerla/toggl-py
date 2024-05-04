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


class TimesheetsetupsUpdatePayload:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {"approver_id": "int", "end_date": "str", "reminder_day": "str", "reminder_time": "str"}

    attribute_map = {
        "approver_id": "approver_id",
        "end_date": "end_date",
        "reminder_day": "reminder_day",
        "reminder_time": "reminder_time",
    }

    def __init__(
        self,
        approver_id: int = None,
        end_date: str = None,
        reminder_day: str = None,
        reminder_time: str = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        TimesheetsetupsUpdatePayload - a model defined in Swagger

        Parameters:
          approver_id (int): Optional
          end_date (str): Optional
          reminder_day (str): Optional
          reminder_time (str): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._approver_id = None
        self._end_date = None
        self._reminder_day = None
        self._reminder_time = None
        self.discriminator = None

        if approver_id is not None:
            self.approver_id = approver_id
        if end_date is not None:
            self.end_date = end_date
        if reminder_day is not None:
            self.reminder_day = reminder_day
        if reminder_time is not None:
            self.reminder_time = reminder_time

    @property
    def approver_id(self) -> int:
        """Gets the approver_id of this TimesheetsetupsUpdatePayload.  # noqa: E501


        :return: The approver_id of this TimesheetsetupsUpdatePayload.  # noqa: E501
        :rtype: int
        """
        return self._approver_id

    @approver_id.setter
    def approver_id(self, approver_id: int):
        """Sets the approver_id of this TimesheetsetupsUpdatePayload.


        :param approver_id: The approver_id of this TimesheetsetupsUpdatePayload.  # noqa: E501
        :type: int
        """

        self._approver_id = approver_id

    @property
    def end_date(self) -> str:
        """Gets the end_date of this TimesheetsetupsUpdatePayload.  # noqa: E501


        :return: The end_date of this TimesheetsetupsUpdatePayload.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: str):
        """Sets the end_date of this TimesheetsetupsUpdatePayload.


        :param end_date: The end_date of this TimesheetsetupsUpdatePayload.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def reminder_day(self) -> str:
        """Gets the reminder_day of this TimesheetsetupsUpdatePayload.  # noqa: E501


        :return: The reminder_day of this TimesheetsetupsUpdatePayload.  # noqa: E501
        :rtype: str
        """
        return self._reminder_day

    @reminder_day.setter
    def reminder_day(self, reminder_day: str):
        """Sets the reminder_day of this TimesheetsetupsUpdatePayload.


        :param reminder_day: The reminder_day of this TimesheetsetupsUpdatePayload.  # noqa: E501
        :type: str
        """

        self._reminder_day = reminder_day

    @property
    def reminder_time(self) -> str:
        """Gets the reminder_time of this TimesheetsetupsUpdatePayload.  # noqa: E501


        :return: The reminder_time of this TimesheetsetupsUpdatePayload.  # noqa: E501
        :rtype: str
        """
        return self._reminder_time

    @reminder_time.setter
    def reminder_time(self, reminder_time: str):
        """Sets the reminder_time of this TimesheetsetupsUpdatePayload.


        :param reminder_time: The reminder_time of this TimesheetsetupsUpdatePayload.  # noqa: E501
        :type: str
        """

        self._reminder_time = reminder_time

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
        if issubclass(TimesheetsetupsUpdatePayload, dict):
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
        if not isinstance(other, TimesheetsetupsUpdatePayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimesheetsetupsUpdatePayload):
            return True

        return self.to_dict() != other.to_dict()
