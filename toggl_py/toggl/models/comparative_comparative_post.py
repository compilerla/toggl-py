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


class ComparativeComparativePost:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "billable": "bool",
        "client_ids": "list[int]",
        "end_date": "str",
        "group_ids": "list[int]",
        "project_ids": "list[int]",
        "resolution": "str",
        "rounding": "int",
        "rounding_minutes": "int",
        "start_date": "str",
        "tag_ids": "list[int]",
        "task_ids": "list[int]",
        "user_ids": "list[int]",
    }

    attribute_map = {
        "billable": "billable",
        "client_ids": "client_ids",
        "end_date": "end_date",
        "group_ids": "group_ids",
        "project_ids": "project_ids",
        "resolution": "resolution",
        "rounding": "rounding",
        "rounding_minutes": "rounding_minutes",
        "start_date": "start_date",
        "tag_ids": "tag_ids",
        "task_ids": "task_ids",
        "user_ids": "user_ids",
    }

    def __init__(
        self,
        billable=None,
        client_ids=None,
        end_date=None,
        group_ids=None,
        project_ids=None,
        resolution=None,
        rounding=None,
        rounding_minutes=None,
        start_date=None,
        tag_ids=None,
        task_ids=None,
        user_ids=None,
        _configuration=None,
    ):  # noqa: E501
        """ComparativeComparativePost - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._billable = None
        self._client_ids = None
        self._end_date = None
        self._group_ids = None
        self._project_ids = None
        self._resolution = None
        self._rounding = None
        self._rounding_minutes = None
        self._start_date = None
        self._tag_ids = None
        self._task_ids = None
        self._user_ids = None
        self.discriminator = None

        if billable is not None:
            self.billable = billable
        if client_ids is not None:
            self.client_ids = client_ids
        if end_date is not None:
            self.end_date = end_date
        if group_ids is not None:
            self.group_ids = group_ids
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
        if tag_ids is not None:
            self.tag_ids = tag_ids
        if task_ids is not None:
            self.task_ids = task_ids
        if user_ids is not None:
            self.user_ids = user_ids

    @property
    def billable(self):
        """Gets the billable of this ComparativeComparativePost.  # noqa: E501


        :return: The billable of this ComparativeComparativePost.  # noqa: E501
        :rtype: bool
        """
        return self._billable

    @billable.setter
    def billable(self, billable):
        """Sets the billable of this ComparativeComparativePost.


        :param billable: The billable of this ComparativeComparativePost.  # noqa: E501
        :type: bool
        """

        self._billable = billable

    @property
    def client_ids(self):
        """Gets the client_ids of this ComparativeComparativePost.  # noqa: E501


        :return: The client_ids of this ComparativeComparativePost.  # noqa: E501
        :rtype: list[int]
        """
        return self._client_ids

    @client_ids.setter
    def client_ids(self, client_ids):
        """Sets the client_ids of this ComparativeComparativePost.


        :param client_ids: The client_ids of this ComparativeComparativePost.  # noqa: E501
        :type: list[int]
        """

        self._client_ids = client_ids

    @property
    def end_date(self):
        """Gets the end_date of this ComparativeComparativePost.  # noqa: E501


        :return: The end_date of this ComparativeComparativePost.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ComparativeComparativePost.


        :param end_date: The end_date of this ComparativeComparativePost.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def group_ids(self):
        """Gets the group_ids of this ComparativeComparativePost.  # noqa: E501


        :return: The group_ids of this ComparativeComparativePost.  # noqa: E501
        :rtype: list[int]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this ComparativeComparativePost.


        :param group_ids: The group_ids of this ComparativeComparativePost.  # noqa: E501
        :type: list[int]
        """

        self._group_ids = group_ids

    @property
    def project_ids(self):
        """Gets the project_ids of this ComparativeComparativePost.  # noqa: E501


        :return: The project_ids of this ComparativeComparativePost.  # noqa: E501
        :rtype: list[int]
        """
        return self._project_ids

    @project_ids.setter
    def project_ids(self, project_ids):
        """Sets the project_ids of this ComparativeComparativePost.


        :param project_ids: The project_ids of this ComparativeComparativePost.  # noqa: E501
        :type: list[int]
        """

        self._project_ids = project_ids

    @property
    def resolution(self):
        """Gets the resolution of this ComparativeComparativePost.  # noqa: E501


        :return: The resolution of this ComparativeComparativePost.  # noqa: E501
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this ComparativeComparativePost.


        :param resolution: The resolution of this ComparativeComparativePost.  # noqa: E501
        :type: str
        """

        self._resolution = resolution

    @property
    def rounding(self):
        """Gets the rounding of this ComparativeComparativePost.  # noqa: E501


        :return: The rounding of this ComparativeComparativePost.  # noqa: E501
        :rtype: int
        """
        return self._rounding

    @rounding.setter
    def rounding(self, rounding):
        """Sets the rounding of this ComparativeComparativePost.


        :param rounding: The rounding of this ComparativeComparativePost.  # noqa: E501
        :type: int
        """

        self._rounding = rounding

    @property
    def rounding_minutes(self):
        """Gets the rounding_minutes of this ComparativeComparativePost.  # noqa: E501


        :return: The rounding_minutes of this ComparativeComparativePost.  # noqa: E501
        :rtype: int
        """
        return self._rounding_minutes

    @rounding_minutes.setter
    def rounding_minutes(self, rounding_minutes):
        """Sets the rounding_minutes of this ComparativeComparativePost.


        :param rounding_minutes: The rounding_minutes of this ComparativeComparativePost.  # noqa: E501
        :type: int
        """

        self._rounding_minutes = rounding_minutes

    @property
    def start_date(self):
        """Gets the start_date of this ComparativeComparativePost.  # noqa: E501


        :return: The start_date of this ComparativeComparativePost.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ComparativeComparativePost.


        :param start_date: The start_date of this ComparativeComparativePost.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def tag_ids(self):
        """Gets the tag_ids of this ComparativeComparativePost.  # noqa: E501


        :return: The tag_ids of this ComparativeComparativePost.  # noqa: E501
        :rtype: list[int]
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids):
        """Sets the tag_ids of this ComparativeComparativePost.


        :param tag_ids: The tag_ids of this ComparativeComparativePost.  # noqa: E501
        :type: list[int]
        """

        self._tag_ids = tag_ids

    @property
    def task_ids(self):
        """Gets the task_ids of this ComparativeComparativePost.  # noqa: E501


        :return: The task_ids of this ComparativeComparativePost.  # noqa: E501
        :rtype: list[int]
        """
        return self._task_ids

    @task_ids.setter
    def task_ids(self, task_ids):
        """Sets the task_ids of this ComparativeComparativePost.


        :param task_ids: The task_ids of this ComparativeComparativePost.  # noqa: E501
        :type: list[int]
        """

        self._task_ids = task_ids

    @property
    def user_ids(self):
        """Gets the user_ids of this ComparativeComparativePost.  # noqa: E501


        :return: The user_ids of this ComparativeComparativePost.  # noqa: E501
        :rtype: list[int]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this ComparativeComparativePost.


        :param user_ids: The user_ids of this ComparativeComparativePost.  # noqa: E501
        :type: list[int]
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
        if issubclass(ComparativeComparativePost, dict):
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
        if not isinstance(other, ComparativeComparativePost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComparativeComparativePost):
            return True

        return self.to_dict() != other.to_dict()
