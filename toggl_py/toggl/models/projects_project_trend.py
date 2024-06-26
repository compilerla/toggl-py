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


class ProjectsProjectTrend:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "billable": "bool",
        "end_date": "str",
        "previous_period_start": "str",
        "project_ids": "list[int]",
        "rounding": "int",
        "rounding_minutes": "int",
        "start_date": "str",
    }

    attribute_map = {
        "billable": "billable",
        "end_date": "end_date",
        "previous_period_start": "previous_period_start",
        "project_ids": "project_ids",
        "rounding": "rounding",
        "rounding_minutes": "rounding_minutes",
        "start_date": "start_date",
    }

    def __init__(
        self,
        billable=None,
        end_date=None,
        previous_period_start=None,
        project_ids=None,
        rounding=None,
        rounding_minutes=None,
        start_date=None,
        _configuration=None,
    ):  # noqa: E501
        """ProjectsProjectTrend - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._billable = None
        self._end_date = None
        self._previous_period_start = None
        self._project_ids = None
        self._rounding = None
        self._rounding_minutes = None
        self._start_date = None
        self.discriminator = None

        if billable is not None:
            self.billable = billable
        if end_date is not None:
            self.end_date = end_date
        if previous_period_start is not None:
            self.previous_period_start = previous_period_start
        if project_ids is not None:
            self.project_ids = project_ids
        if rounding is not None:
            self.rounding = rounding
        if rounding_minutes is not None:
            self.rounding_minutes = rounding_minutes
        if start_date is not None:
            self.start_date = start_date

    @property
    def billable(self):
        """Gets the billable of this ProjectsProjectTrend.  # noqa: E501

        Whether the project is set as billable, optional, premium feature.  # noqa: E501

        :return: The billable of this ProjectsProjectTrend.  # noqa: E501
        :rtype: bool
        """
        return self._billable

    @billable.setter
    def billable(self, billable):
        """Sets the billable of this ProjectsProjectTrend.

        Whether the project is set as billable, optional, premium feature.  # noqa: E501

        :param billable: The billable of this ProjectsProjectTrend.  # noqa: E501
        :type: bool
        """

        self._billable = billable

    @property
    def end_date(self):
        """Gets the end_date of this ProjectsProjectTrend.  # noqa: E501

        End date, example time.DateOnly. Should be greater than Start date.  # noqa: E501

        :return: The end_date of this ProjectsProjectTrend.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ProjectsProjectTrend.

        End date, example time.DateOnly. Should be greater than Start date.  # noqa: E501

        :param end_date: The end_date of this ProjectsProjectTrend.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def previous_period_start(self):
        """Gets the previous_period_start of this ProjectsProjectTrend.  # noqa: E501

        Previous start date, example time.DateOnly.  # noqa: E501

        :return: The previous_period_start of this ProjectsProjectTrend.  # noqa: E501
        :rtype: str
        """
        return self._previous_period_start

    @previous_period_start.setter
    def previous_period_start(self, previous_period_start):
        """Sets the previous_period_start of this ProjectsProjectTrend.

        Previous start date, example time.DateOnly.  # noqa: E501

        :param previous_period_start: The previous_period_start of this ProjectsProjectTrend.  # noqa: E501
        :type: str
        """

        self._previous_period_start = previous_period_start

    @property
    def project_ids(self):
        """Gets the project_ids of this ProjectsProjectTrend.  # noqa: E501

        Project IDs, optional.  # noqa: E501

        :return: The project_ids of this ProjectsProjectTrend.  # noqa: E501
        :rtype: list[int]
        """
        return self._project_ids

    @project_ids.setter
    def project_ids(self, project_ids):
        """Sets the project_ids of this ProjectsProjectTrend.

        Project IDs, optional.  # noqa: E501

        :param project_ids: The project_ids of this ProjectsProjectTrend.  # noqa: E501
        :type: list[int]
        """

        self._project_ids = project_ids

    @property
    def rounding(self):
        """Gets the rounding of this ProjectsProjectTrend.  # noqa: E501

        Rounding, optional, duration rounding settings, premium feature.  # noqa: E501

        :return: The rounding of this ProjectsProjectTrend.  # noqa: E501
        :rtype: int
        """
        return self._rounding

    @rounding.setter
    def rounding(self, rounding):
        """Sets the rounding of this ProjectsProjectTrend.

        Rounding, optional, duration rounding settings, premium feature.  # noqa: E501

        :param rounding: The rounding of this ProjectsProjectTrend.  # noqa: E501
        :type: int
        """

        self._rounding = rounding

    @property
    def rounding_minutes(self):
        """Gets the rounding_minutes of this ProjectsProjectTrend.  # noqa: E501

        RoundingMinutes, optional, duration rounding minutes settings, premium feature.  # noqa: E501

        :return: The rounding_minutes of this ProjectsProjectTrend.  # noqa: E501
        :rtype: int
        """
        return self._rounding_minutes

    @rounding_minutes.setter
    def rounding_minutes(self, rounding_minutes):
        """Sets the rounding_minutes of this ProjectsProjectTrend.

        RoundingMinutes, optional, duration rounding minutes settings, premium feature.  # noqa: E501

        :param rounding_minutes: The rounding_minutes of this ProjectsProjectTrend.  # noqa: E501
        :type: int
        """

        self._rounding_minutes = rounding_minutes

    @property
    def start_date(self):
        """Gets the start_date of this ProjectsProjectTrend.  # noqa: E501

        Start date, example time.DateOnly. Should be less than End date.  # noqa: E501

        :return: The start_date of this ProjectsProjectTrend.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ProjectsProjectTrend.

        Start date, example time.DateOnly. Should be less than End date.  # noqa: E501

        :param start_date: The start_date of this ProjectsProjectTrend.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

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
        if issubclass(ProjectsProjectTrend, dict):
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
        if not isinstance(other, ProjectsProjectTrend):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectsProjectTrend):
            return True

        return self.to_dict() != other.to_dict()
