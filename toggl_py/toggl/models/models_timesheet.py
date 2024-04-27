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


class ModelsTimesheet:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "approved_or_rejected_at": "str",
        "approved_or_rejected_id": "int",
        "approved_or_rejected_name": "str",
        "approver_id": "int",
        "approver_name": "str",
        "created_at": "str",
        "deleted_at": "str",
        "end_date": "str",
        "member_id": "int",
        "member_name": "str",
        "period_editable": "bool",
        "period_end_date": "str",
        "period_locked": "bool",
        "period_start_date": "str",
        "periodicity": "str",
        "rejection_comment": "str",
        "reminder_day": "str",
        "reminder_sent_at": "str",
        "reminder_time": "str",
        "start_date": "str",
        "status": "str",
        "submitted_at": "str",
        "timesheet_setup_id": "int",
        "timezone": "str",
        "updated_at": "str",
        "working_hours_in_minutes": "int",
        "workspace_id": "int",
    }

    attribute_map = {
        "approved_or_rejected_at": "approvedOrRejectedAt",
        "approved_or_rejected_id": "approvedOrRejectedID",
        "approved_or_rejected_name": "approvedOrRejectedName",
        "approver_id": "approverID",
        "approver_name": "approverName",
        "created_at": "createdAt",
        "deleted_at": "deletedAt",
        "end_date": "endDate",
        "member_id": "memberID",
        "member_name": "memberName",
        "period_editable": "periodEditable",
        "period_end_date": "periodEndDate",
        "period_locked": "periodLocked",
        "period_start_date": "periodStartDate",
        "periodicity": "periodicity",
        "rejection_comment": "rejectionComment",
        "reminder_day": "reminderDay",
        "reminder_sent_at": "reminderSentAt",
        "reminder_time": "reminderTime",
        "start_date": "startDate",
        "status": "status",
        "submitted_at": "submittedAt",
        "timesheet_setup_id": "timesheetSetupID",
        "timezone": "timezone",
        "updated_at": "updatedAt",
        "working_hours_in_minutes": "workingHoursInMinutes",
        "workspace_id": "workspaceID",
    }

    def __init__(
        self,
        approved_or_rejected_at=None,
        approved_or_rejected_id=None,
        approved_or_rejected_name=None,
        approver_id=None,
        approver_name=None,
        created_at=None,
        deleted_at=None,
        end_date=None,
        member_id=None,
        member_name=None,
        period_editable=None,
        period_end_date=None,
        period_locked=None,
        period_start_date=None,
        periodicity=None,
        rejection_comment=None,
        reminder_day=None,
        reminder_sent_at=None,
        reminder_time=None,
        start_date=None,
        status=None,
        submitted_at=None,
        timesheet_setup_id=None,
        timezone=None,
        updated_at=None,
        working_hours_in_minutes=None,
        workspace_id=None,
        _configuration=None,
    ):  # noqa: E501
        """ModelsTimesheet - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._approved_or_rejected_at = None
        self._approved_or_rejected_id = None
        self._approved_or_rejected_name = None
        self._approver_id = None
        self._approver_name = None
        self._created_at = None
        self._deleted_at = None
        self._end_date = None
        self._member_id = None
        self._member_name = None
        self._period_editable = None
        self._period_end_date = None
        self._period_locked = None
        self._period_start_date = None
        self._periodicity = None
        self._rejection_comment = None
        self._reminder_day = None
        self._reminder_sent_at = None
        self._reminder_time = None
        self._start_date = None
        self._status = None
        self._submitted_at = None
        self._timesheet_setup_id = None
        self._timezone = None
        self._updated_at = None
        self._working_hours_in_minutes = None
        self._workspace_id = None
        self.discriminator = None

        if approved_or_rejected_at is not None:
            self.approved_or_rejected_at = approved_or_rejected_at
        if approved_or_rejected_id is not None:
            self.approved_or_rejected_id = approved_or_rejected_id
        if approved_or_rejected_name is not None:
            self.approved_or_rejected_name = approved_or_rejected_name
        if approver_id is not None:
            self.approver_id = approver_id
        if approver_name is not None:
            self.approver_name = approver_name
        if created_at is not None:
            self.created_at = created_at
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if end_date is not None:
            self.end_date = end_date
        if member_id is not None:
            self.member_id = member_id
        if member_name is not None:
            self.member_name = member_name
        if period_editable is not None:
            self.period_editable = period_editable
        if period_end_date is not None:
            self.period_end_date = period_end_date
        if period_locked is not None:
            self.period_locked = period_locked
        if period_start_date is not None:
            self.period_start_date = period_start_date
        if periodicity is not None:
            self.periodicity = periodicity
        if rejection_comment is not None:
            self.rejection_comment = rejection_comment
        if reminder_day is not None:
            self.reminder_day = reminder_day
        if reminder_sent_at is not None:
            self.reminder_sent_at = reminder_sent_at
        if reminder_time is not None:
            self.reminder_time = reminder_time
        if start_date is not None:
            self.start_date = start_date
        if status is not None:
            self.status = status
        if submitted_at is not None:
            self.submitted_at = submitted_at
        if timesheet_setup_id is not None:
            self.timesheet_setup_id = timesheet_setup_id
        if timezone is not None:
            self.timezone = timezone
        if updated_at is not None:
            self.updated_at = updated_at
        if working_hours_in_minutes is not None:
            self.working_hours_in_minutes = working_hours_in_minutes
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def approved_or_rejected_at(self):
        """Gets the approved_or_rejected_at of this ModelsTimesheet.  # noqa: E501


        :return: The approved_or_rejected_at of this ModelsTimesheet.  # noqa: E501
        :rtype: str
        """
        return self._approved_or_rejected_at

    @approved_or_rejected_at.setter
    def approved_or_rejected_at(self, approved_or_rejected_at):
        """Sets the approved_or_rejected_at of this ModelsTimesheet.


        :param approved_or_rejected_at: The approved_or_rejected_at of this ModelsTimesheet.  # noqa: E501
        :type: str
        """

        self._approved_or_rejected_at = approved_or_rejected_at

    @property
    def approved_or_rejected_id(self):
        """Gets the approved_or_rejected_id of this ModelsTimesheet.  # noqa: E501


        :return: The approved_or_rejected_id of this ModelsTimesheet.  # noqa: E501
        :rtype: int
        """
        return self._approved_or_rejected_id

    @approved_or_rejected_id.setter
    def approved_or_rejected_id(self, approved_or_rejected_id):
        """Sets the approved_or_rejected_id of this ModelsTimesheet.


        :param approved_or_rejected_id: The approved_or_rejected_id of this ModelsTimesheet.  # noqa: E501
        :type: int
        """

        self._approved_or_rejected_id = approved_or_rejected_id

    @property
    def approved_or_rejected_name(self):
        """Gets the approved_or_rejected_name of this ModelsTimesheet.  # noqa: E501


        :return: The approved_or_rejected_name of this ModelsTimesheet.  # noqa: E501
        :rtype: str
        """
        return self._approved_or_rejected_name

    @approved_or_rejected_name.setter
    def approved_or_rejected_name(self, approved_or_rejected_name):
        """Sets the approved_or_rejected_name of this ModelsTimesheet.


        :param approved_or_rejected_name: The approved_or_rejected_name of this ModelsTimesheet.  # noqa: E501
        :type: str
        """

        self._approved_or_rejected_name = approved_or_rejected_name

    @property
    def approver_id(self):
        """Gets the approver_id of this ModelsTimesheet.  # noqa: E501


        :return: The approver_id of this ModelsTimesheet.  # noqa: E501
        :rtype: int
        """
        return self._approver_id

    @approver_id.setter
    def approver_id(self, approver_id):
        """Sets the approver_id of this ModelsTimesheet.


        :param approver_id: The approver_id of this ModelsTimesheet.  # noqa: E501
        :type: int
        """

        self._approver_id = approver_id

    @property
    def approver_name(self):
        """Gets the approver_name of this ModelsTimesheet.  # noqa: E501


        :return: The approver_name of this ModelsTimesheet.  # noqa: E501
        :rtype: str
        """
        return self._approver_name

    @approver_name.setter
    def approver_name(self, approver_name):
        """Sets the approver_name of this ModelsTimesheet.


        :param approver_name: The approver_name of this ModelsTimesheet.  # noqa: E501
        :type: str
        """

        self._approver_name = approver_name

    @property
    def created_at(self):
        """Gets the created_at of this ModelsTimesheet.  # noqa: E501


        :return: The created_at of this ModelsTimesheet.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ModelsTimesheet.


        :param created_at: The created_at of this ModelsTimesheet.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this ModelsTimesheet.  # noqa: E501


        :return: The deleted_at of this ModelsTimesheet.  # noqa: E501
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this ModelsTimesheet.


        :param deleted_at: The deleted_at of this ModelsTimesheet.  # noqa: E501
        :type: str
        """

        self._deleted_at = deleted_at

    @property
    def end_date(self):
        """Gets the end_date of this ModelsTimesheet.  # noqa: E501


        :return: The end_date of this ModelsTimesheet.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ModelsTimesheet.


        :param end_date: The end_date of this ModelsTimesheet.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def member_id(self):
        """Gets the member_id of this ModelsTimesheet.  # noqa: E501


        :return: The member_id of this ModelsTimesheet.  # noqa: E501
        :rtype: int
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """Sets the member_id of this ModelsTimesheet.


        :param member_id: The member_id of this ModelsTimesheet.  # noqa: E501
        :type: int
        """

        self._member_id = member_id

    @property
    def member_name(self):
        """Gets the member_name of this ModelsTimesheet.  # noqa: E501


        :return: The member_name of this ModelsTimesheet.  # noqa: E501
        :rtype: str
        """
        return self._member_name

    @member_name.setter
    def member_name(self, member_name):
        """Sets the member_name of this ModelsTimesheet.


        :param member_name: The member_name of this ModelsTimesheet.  # noqa: E501
        :type: str
        """

        self._member_name = member_name

    @property
    def period_editable(self):
        """Gets the period_editable of this ModelsTimesheet.  # noqa: E501


        :return: The period_editable of this ModelsTimesheet.  # noqa: E501
        :rtype: bool
        """
        return self._period_editable

    @period_editable.setter
    def period_editable(self, period_editable):
        """Sets the period_editable of this ModelsTimesheet.


        :param period_editable: The period_editable of this ModelsTimesheet.  # noqa: E501
        :type: bool
        """

        self._period_editable = period_editable

    @property
    def period_end_date(self):
        """Gets the period_end_date of this ModelsTimesheet.  # noqa: E501


        :return: The period_end_date of this ModelsTimesheet.  # noqa: E501
        :rtype: str
        """
        return self._period_end_date

    @period_end_date.setter
    def period_end_date(self, period_end_date):
        """Sets the period_end_date of this ModelsTimesheet.


        :param period_end_date: The period_end_date of this ModelsTimesheet.  # noqa: E501
        :type: str
        """

        self._period_end_date = period_end_date

    @property
    def period_locked(self):
        """Gets the period_locked of this ModelsTimesheet.  # noqa: E501


        :return: The period_locked of this ModelsTimesheet.  # noqa: E501
        :rtype: bool
        """
        return self._period_locked

    @period_locked.setter
    def period_locked(self, period_locked):
        """Sets the period_locked of this ModelsTimesheet.


        :param period_locked: The period_locked of this ModelsTimesheet.  # noqa: E501
        :type: bool
        """

        self._period_locked = period_locked

    @property
    def period_start_date(self):
        """Gets the period_start_date of this ModelsTimesheet.  # noqa: E501


        :return: The period_start_date of this ModelsTimesheet.  # noqa: E501
        :rtype: str
        """
        return self._period_start_date

    @period_start_date.setter
    def period_start_date(self, period_start_date):
        """Sets the period_start_date of this ModelsTimesheet.


        :param period_start_date: The period_start_date of this ModelsTimesheet.  # noqa: E501
        :type: str
        """

        self._period_start_date = period_start_date

    @property
    def periodicity(self):
        """Gets the periodicity of this ModelsTimesheet.  # noqa: E501


        :return: The periodicity of this ModelsTimesheet.  # noqa: E501
        :rtype: str
        """
        return self._periodicity

    @periodicity.setter
    def periodicity(self, periodicity):
        """Sets the periodicity of this ModelsTimesheet.


        :param periodicity: The periodicity of this ModelsTimesheet.  # noqa: E501
        :type: str
        """

        self._periodicity = periodicity

    @property
    def rejection_comment(self):
        """Gets the rejection_comment of this ModelsTimesheet.  # noqa: E501


        :return: The rejection_comment of this ModelsTimesheet.  # noqa: E501
        :rtype: str
        """
        return self._rejection_comment

    @rejection_comment.setter
    def rejection_comment(self, rejection_comment):
        """Sets the rejection_comment of this ModelsTimesheet.


        :param rejection_comment: The rejection_comment of this ModelsTimesheet.  # noqa: E501
        :type: str
        """

        self._rejection_comment = rejection_comment

    @property
    def reminder_day(self):
        """Gets the reminder_day of this ModelsTimesheet.  # noqa: E501


        :return: The reminder_day of this ModelsTimesheet.  # noqa: E501
        :rtype: str
        """
        return self._reminder_day

    @reminder_day.setter
    def reminder_day(self, reminder_day):
        """Sets the reminder_day of this ModelsTimesheet.


        :param reminder_day: The reminder_day of this ModelsTimesheet.  # noqa: E501
        :type: str
        """

        self._reminder_day = reminder_day

    @property
    def reminder_sent_at(self):
        """Gets the reminder_sent_at of this ModelsTimesheet.  # noqa: E501


        :return: The reminder_sent_at of this ModelsTimesheet.  # noqa: E501
        :rtype: str
        """
        return self._reminder_sent_at

    @reminder_sent_at.setter
    def reminder_sent_at(self, reminder_sent_at):
        """Sets the reminder_sent_at of this ModelsTimesheet.


        :param reminder_sent_at: The reminder_sent_at of this ModelsTimesheet.  # noqa: E501
        :type: str
        """

        self._reminder_sent_at = reminder_sent_at

    @property
    def reminder_time(self):
        """Gets the reminder_time of this ModelsTimesheet.  # noqa: E501


        :return: The reminder_time of this ModelsTimesheet.  # noqa: E501
        :rtype: str
        """
        return self._reminder_time

    @reminder_time.setter
    def reminder_time(self, reminder_time):
        """Sets the reminder_time of this ModelsTimesheet.


        :param reminder_time: The reminder_time of this ModelsTimesheet.  # noqa: E501
        :type: str
        """

        self._reminder_time = reminder_time

    @property
    def start_date(self):
        """Gets the start_date of this ModelsTimesheet.  # noqa: E501


        :return: The start_date of this ModelsTimesheet.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ModelsTimesheet.


        :param start_date: The start_date of this ModelsTimesheet.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def status(self):
        """Gets the status of this ModelsTimesheet.  # noqa: E501


        :return: The status of this ModelsTimesheet.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ModelsTimesheet.


        :param status: The status of this ModelsTimesheet.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def submitted_at(self):
        """Gets the submitted_at of this ModelsTimesheet.  # noqa: E501


        :return: The submitted_at of this ModelsTimesheet.  # noqa: E501
        :rtype: str
        """
        return self._submitted_at

    @submitted_at.setter
    def submitted_at(self, submitted_at):
        """Sets the submitted_at of this ModelsTimesheet.


        :param submitted_at: The submitted_at of this ModelsTimesheet.  # noqa: E501
        :type: str
        """

        self._submitted_at = submitted_at

    @property
    def timesheet_setup_id(self):
        """Gets the timesheet_setup_id of this ModelsTimesheet.  # noqa: E501


        :return: The timesheet_setup_id of this ModelsTimesheet.  # noqa: E501
        :rtype: int
        """
        return self._timesheet_setup_id

    @timesheet_setup_id.setter
    def timesheet_setup_id(self, timesheet_setup_id):
        """Sets the timesheet_setup_id of this ModelsTimesheet.


        :param timesheet_setup_id: The timesheet_setup_id of this ModelsTimesheet.  # noqa: E501
        :type: int
        """

        self._timesheet_setup_id = timesheet_setup_id

    @property
    def timezone(self):
        """Gets the timezone of this ModelsTimesheet.  # noqa: E501


        :return: The timezone of this ModelsTimesheet.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this ModelsTimesheet.


        :param timezone: The timezone of this ModelsTimesheet.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def updated_at(self):
        """Gets the updated_at of this ModelsTimesheet.  # noqa: E501


        :return: The updated_at of this ModelsTimesheet.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ModelsTimesheet.


        :param updated_at: The updated_at of this ModelsTimesheet.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def working_hours_in_minutes(self):
        """Gets the working_hours_in_minutes of this ModelsTimesheet.  # noqa: E501


        :return: The working_hours_in_minutes of this ModelsTimesheet.  # noqa: E501
        :rtype: int
        """
        return self._working_hours_in_minutes

    @working_hours_in_minutes.setter
    def working_hours_in_minutes(self, working_hours_in_minutes):
        """Sets the working_hours_in_minutes of this ModelsTimesheet.


        :param working_hours_in_minutes: The working_hours_in_minutes of this ModelsTimesheet.  # noqa: E501
        :type: int
        """

        self._working_hours_in_minutes = working_hours_in_minutes

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ModelsTimesheet.  # noqa: E501


        :return: The workspace_id of this ModelsTimesheet.  # noqa: E501
        :rtype: int
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ModelsTimesheet.


        :param workspace_id: The workspace_id of this ModelsTimesheet.  # noqa: E501
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
        if issubclass(ModelsTimesheet, dict):
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
        if not isinstance(other, ModelsTimesheet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsTimesheet):
            return True

        return self.to_dict() != other.to_dict()
