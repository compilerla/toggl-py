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


class TimesheetsetupsAPITimesheetSetup:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "approver_id": "int",
        "approver_name": "str",
        "end_date": "str",
        "errors": "list[ModelsTimesheetSetupError]",
        "id": "int",
        "member_id": "int",
        "member_name": "str",
        "periodicity": "str",
        "reminder_day": "str",
        "reminder_time": "str",
        "start_date": "str",
        "workspace_id": "int",
    }

    attribute_map = {
        "approver_id": "approver_id",
        "approver_name": "approver_name",
        "end_date": "end_date",
        "errors": "errors",
        "id": "id",
        "member_id": "member_id",
        "member_name": "member_name",
        "periodicity": "periodicity",
        "reminder_day": "reminder_day",
        "reminder_time": "reminder_time",
        "start_date": "start_date",
        "workspace_id": "workspace_id",
    }

    def __init__(
        self,
        approver_id=None,
        approver_name=None,
        end_date=None,
        errors=None,
        id=None,
        member_id=None,
        member_name=None,
        periodicity=None,
        reminder_day=None,
        reminder_time=None,
        start_date=None,
        workspace_id=None,
        _configuration=None,
    ):  # noqa: E501
        """TimesheetsetupsAPITimesheetSetup - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._approver_id = None
        self._approver_name = None
        self._end_date = None
        self._errors = None
        self._id = None
        self._member_id = None
        self._member_name = None
        self._periodicity = None
        self._reminder_day = None
        self._reminder_time = None
        self._start_date = None
        self._workspace_id = None
        self.discriminator = None

        if approver_id is not None:
            self.approver_id = approver_id
        if approver_name is not None:
            self.approver_name = approver_name
        if end_date is not None:
            self.end_date = end_date
        if errors is not None:
            self.errors = errors
        if id is not None:
            self.id = id
        if member_id is not None:
            self.member_id = member_id
        if member_name is not None:
            self.member_name = member_name
        if periodicity is not None:
            self.periodicity = periodicity
        if reminder_day is not None:
            self.reminder_day = reminder_day
        if reminder_time is not None:
            self.reminder_time = reminder_time
        if start_date is not None:
            self.start_date = start_date
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def approver_id(self):
        """Gets the approver_id of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501


        :return: The approver_id of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :rtype: int
        """
        return self._approver_id

    @approver_id.setter
    def approver_id(self, approver_id):
        """Sets the approver_id of this TimesheetsetupsAPITimesheetSetup.


        :param approver_id: The approver_id of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :type: int
        """

        self._approver_id = approver_id

    @property
    def approver_name(self):
        """Gets the approver_name of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501


        :return: The approver_name of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :rtype: str
        """
        return self._approver_name

    @approver_name.setter
    def approver_name(self, approver_name):
        """Sets the approver_name of this TimesheetsetupsAPITimesheetSetup.


        :param approver_name: The approver_name of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :type: str
        """

        self._approver_name = approver_name

    @property
    def end_date(self):
        """Gets the end_date of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501


        :return: The end_date of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this TimesheetsetupsAPITimesheetSetup.


        :param end_date: The end_date of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def errors(self):
        """Gets the errors of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501


        :return: The errors of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :rtype: list[ModelsTimesheetSetupError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this TimesheetsetupsAPITimesheetSetup.


        :param errors: The errors of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :type: list[ModelsTimesheetSetupError]
        """

        self._errors = errors

    @property
    def id(self):
        """Gets the id of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501


        :return: The id of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TimesheetsetupsAPITimesheetSetup.


        :param id: The id of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def member_id(self):
        """Gets the member_id of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501


        :return: The member_id of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :rtype: int
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """Sets the member_id of this TimesheetsetupsAPITimesheetSetup.


        :param member_id: The member_id of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :type: int
        """

        self._member_id = member_id

    @property
    def member_name(self):
        """Gets the member_name of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501


        :return: The member_name of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :rtype: str
        """
        return self._member_name

    @member_name.setter
    def member_name(self, member_name):
        """Sets the member_name of this TimesheetsetupsAPITimesheetSetup.


        :param member_name: The member_name of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :type: str
        """

        self._member_name = member_name

    @property
    def periodicity(self):
        """Gets the periodicity of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501


        :return: The periodicity of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :rtype: str
        """
        return self._periodicity

    @periodicity.setter
    def periodicity(self, periodicity):
        """Sets the periodicity of this TimesheetsetupsAPITimesheetSetup.


        :param periodicity: The periodicity of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :type: str
        """

        self._periodicity = periodicity

    @property
    def reminder_day(self):
        """Gets the reminder_day of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501


        :return: The reminder_day of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :rtype: str
        """
        return self._reminder_day

    @reminder_day.setter
    def reminder_day(self, reminder_day):
        """Sets the reminder_day of this TimesheetsetupsAPITimesheetSetup.


        :param reminder_day: The reminder_day of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :type: str
        """

        self._reminder_day = reminder_day

    @property
    def reminder_time(self):
        """Gets the reminder_time of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501


        :return: The reminder_time of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :rtype: str
        """
        return self._reminder_time

    @reminder_time.setter
    def reminder_time(self, reminder_time):
        """Sets the reminder_time of this TimesheetsetupsAPITimesheetSetup.


        :param reminder_time: The reminder_time of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :type: str
        """

        self._reminder_time = reminder_time

    @property
    def start_date(self):
        """Gets the start_date of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501


        :return: The start_date of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this TimesheetsetupsAPITimesheetSetup.


        :param start_date: The start_date of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def workspace_id(self):
        """Gets the workspace_id of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501


        :return: The workspace_id of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :rtype: int
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this TimesheetsetupsAPITimesheetSetup.


        :param workspace_id: The workspace_id of this TimesheetsetupsAPITimesheetSetup.  # noqa: E501
        :type: int
        """

        self._workspace_id = workspace_id

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
        if issubclass(TimesheetsetupsAPITimesheetSetup, dict):
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
        if not isinstance(other, TimesheetsetupsAPITimesheetSetup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimesheetsetupsAPITimesheetSetup):
            return True

        return self.to_dict() != other.to_dict()