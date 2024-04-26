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


class TimesheetsTimesheetHoursResponse:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "start_date": "str",
        "timesheet_setup_id": "int",
        "total_seconds": "int",
        "working_hours_in_minutes": "int",
    }

    attribute_map = {
        "start_date": "start_date",
        "timesheet_setup_id": "timesheet_setup_id",
        "total_seconds": "total_seconds",
        "working_hours_in_minutes": "working_hours_in_minutes",
    }

    def __init__(
        self, start_date=None, timesheet_setup_id=None, total_seconds=None, working_hours_in_minutes=None, _configuration=None
    ):  # noqa: E501
        """TimesheetsTimesheetHoursResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._start_date = None
        self._timesheet_setup_id = None
        self._total_seconds = None
        self._working_hours_in_minutes = None
        self.discriminator = None

        if start_date is not None:
            self.start_date = start_date
        if timesheet_setup_id is not None:
            self.timesheet_setup_id = timesheet_setup_id
        if total_seconds is not None:
            self.total_seconds = total_seconds
        if working_hours_in_minutes is not None:
            self.working_hours_in_minutes = working_hours_in_minutes

    @property
    def start_date(self):
        """Gets the start_date of this TimesheetsTimesheetHoursResponse.  # noqa: E501


        :return: The start_date of this TimesheetsTimesheetHoursResponse.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this TimesheetsTimesheetHoursResponse.


        :param start_date: The start_date of this TimesheetsTimesheetHoursResponse.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def timesheet_setup_id(self):
        """Gets the timesheet_setup_id of this TimesheetsTimesheetHoursResponse.  # noqa: E501


        :return: The timesheet_setup_id of this TimesheetsTimesheetHoursResponse.  # noqa: E501
        :rtype: int
        """
        return self._timesheet_setup_id

    @timesheet_setup_id.setter
    def timesheet_setup_id(self, timesheet_setup_id):
        """Sets the timesheet_setup_id of this TimesheetsTimesheetHoursResponse.


        :param timesheet_setup_id: The timesheet_setup_id of this TimesheetsTimesheetHoursResponse.  # noqa: E501
        :type: int
        """

        self._timesheet_setup_id = timesheet_setup_id

    @property
    def total_seconds(self):
        """Gets the total_seconds of this TimesheetsTimesheetHoursResponse.  # noqa: E501


        :return: The total_seconds of this TimesheetsTimesheetHoursResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_seconds

    @total_seconds.setter
    def total_seconds(self, total_seconds):
        """Sets the total_seconds of this TimesheetsTimesheetHoursResponse.


        :param total_seconds: The total_seconds of this TimesheetsTimesheetHoursResponse.  # noqa: E501
        :type: int
        """

        self._total_seconds = total_seconds

    @property
    def working_hours_in_minutes(self):
        """Gets the working_hours_in_minutes of this TimesheetsTimesheetHoursResponse.  # noqa: E501


        :return: The working_hours_in_minutes of this TimesheetsTimesheetHoursResponse.  # noqa: E501
        :rtype: int
        """
        return self._working_hours_in_minutes

    @working_hours_in_minutes.setter
    def working_hours_in_minutes(self, working_hours_in_minutes):
        """Sets the working_hours_in_minutes of this TimesheetsTimesheetHoursResponse.


        :param working_hours_in_minutes: The working_hours_in_minutes of this TimesheetsTimesheetHoursResponse.  # noqa: E501
        :type: int
        """

        self._working_hours_in_minutes = working_hours_in_minutes

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
        if issubclass(TimesheetsTimesheetHoursResponse, dict):
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
        if not isinstance(other, TimesheetsTimesheetHoursResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimesheetsTimesheetHoursResponse):
            return True

        return self.to_dict() != other.to_dict()
