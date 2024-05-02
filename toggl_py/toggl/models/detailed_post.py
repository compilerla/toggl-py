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


class DetailedPost:
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
        "description": "str",
        "end_date": "str",
        "first_id": "int",
        "first_row_number": "int",
        "first_timestamp": "int",
        "group_ids": "list[int]",
        "grouped": "bool",
        "hide_amounts": "bool",
        "max_duration_seconds": "int",
        "min_duration_seconds": "int",
        "order_by": "str",
        "order_dir": "str",
        "page_size": "int",
        "posted_fields": "list[str]",
        "project_ids": "list[int]",
        "rounding": "int",
        "rounding_minutes": "int",
        "start_time": "str",
        "start_date": "str",
        "tag_ids": "list[int]",
        "task_ids": "list[int]",
        "time_entry_ids": "list[int]",
        "user_ids": "list[int]",
    }

    attribute_map = {
        "billable": "billable",
        "client_ids": "client_ids",
        "description": "description",
        "end_date": "end_date",
        "first_id": "first_id",
        "first_row_number": "first_row_number",
        "first_timestamp": "first_timestamp",
        "group_ids": "group_ids",
        "grouped": "grouped",
        "hide_amounts": "hide_amounts",
        "max_duration_seconds": "max_duration_seconds",
        "min_duration_seconds": "min_duration_seconds",
        "order_by": "order_by",
        "order_dir": "order_dir",
        "page_size": "page_size",
        "posted_fields": "postedFields",
        "project_ids": "project_ids",
        "rounding": "rounding",
        "rounding_minutes": "rounding_minutes",
        "start_time": "startTime",
        "start_date": "start_date",
        "tag_ids": "tag_ids",
        "task_ids": "task_ids",
        "time_entry_ids": "time_entry_ids",
        "user_ids": "user_ids",
    }

    def __init__(
        self,
        billable: bool = None,
        client_ids: list[int] = None,
        description: str = None,
        end_date: str = None,
        first_id: int = None,
        first_row_number: int = None,
        first_timestamp: int = None,
        group_ids: list[int] = None,
        grouped: bool = None,
        hide_amounts: bool = None,
        max_duration_seconds: int = None,
        min_duration_seconds: int = None,
        order_by: str = None,
        order_dir: str = None,
        page_size: int = None,
        posted_fields: list[str] = None,
        project_ids: list[int] = None,
        rounding: int = None,
        rounding_minutes: int = None,
        start_time: str = None,
        start_date: str = None,
        tag_ids: list[int] = None,
        task_ids: list[int] = None,
        time_entry_ids: list[int] = None,
        user_ids: list[int] = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        DetailedPost - a model defined in Swagger

        Parameters:
          billable (bool): Optional
          client_ids (list[int]): Optional
          description (str): Optional
          end_date (str): Optional
          first_id (int): Optional
          first_row_number (int): Optional
          first_timestamp (int): Optional
          group_ids (list[int]): Optional
          grouped (bool): Optional
          hide_amounts (bool): Optional
          max_duration_seconds (int): Optional
          min_duration_seconds (int): Optional
          order_by (str): Optional
          order_dir (str): Optional
          page_size (int): Optional
          posted_fields (list[str]): Optional
          project_ids (list[int]): Optional
          rounding (int): Optional
          rounding_minutes (int): Optional
          start_time (str): Optional
          start_date (str): Optional
          tag_ids (list[int]): Optional
          task_ids (list[int]): Optional
          time_entry_ids (list[int]): Optional
          user_ids (list[int]): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._billable = None
        self._client_ids = None
        self._description = None
        self._end_date = None
        self._first_id = None
        self._first_row_number = None
        self._first_timestamp = None
        self._group_ids = None
        self._grouped = None
        self._hide_amounts = None
        self._max_duration_seconds = None
        self._min_duration_seconds = None
        self._order_by = None
        self._order_dir = None
        self._page_size = None
        self._posted_fields = None
        self._project_ids = None
        self._rounding = None
        self._rounding_minutes = None
        self._start_time = None
        self._start_date = None
        self._tag_ids = None
        self._task_ids = None
        self._time_entry_ids = None
        self._user_ids = None
        self.discriminator = None

        if billable is not None:
            self.billable = billable
        if client_ids is not None:
            self.client_ids = client_ids
        if description is not None:
            self.description = description
        if end_date is not None:
            self.end_date = end_date
        if first_id is not None:
            self.first_id = first_id
        if first_row_number is not None:
            self.first_row_number = first_row_number
        if first_timestamp is not None:
            self.first_timestamp = first_timestamp
        if group_ids is not None:
            self.group_ids = group_ids
        if grouped is not None:
            self.grouped = grouped
        if hide_amounts is not None:
            self.hide_amounts = hide_amounts
        if max_duration_seconds is not None:
            self.max_duration_seconds = max_duration_seconds
        if min_duration_seconds is not None:
            self.min_duration_seconds = min_duration_seconds
        if order_by is not None:
            self.order_by = order_by
        if order_dir is not None:
            self.order_dir = order_dir
        if page_size is not None:
            self.page_size = page_size
        if posted_fields is not None:
            self.posted_fields = posted_fields
        if project_ids is not None:
            self.project_ids = project_ids
        if rounding is not None:
            self.rounding = rounding
        if rounding_minutes is not None:
            self.rounding_minutes = rounding_minutes
        if start_time is not None:
            self.start_time = start_time
        if start_date is not None:
            self.start_date = start_date
        if tag_ids is not None:
            self.tag_ids = tag_ids
        if task_ids is not None:
            self.task_ids = task_ids
        if time_entry_ids is not None:
            self.time_entry_ids = time_entry_ids
        if user_ids is not None:
            self.user_ids = user_ids

    @property
    def billable(self) -> bool:
        """Gets the billable of this DetailedPost.  # noqa: E501

        Whether the time entry is set as billable, optional, premium feature.  # noqa: E501

        :return: The billable of this DetailedPost.  # noqa: E501
        :rtype: bool
        """
        return self._billable

    @billable.setter
    def billable(self, billable: bool):
        """Sets the billable of this DetailedPost.

        Whether the time entry is set as billable, optional, premium feature.  # noqa: E501

        :param billable: The billable of this DetailedPost.  # noqa: E501
        :type: bool
        """

        self._billable = billable

    @property
    def client_ids(self) -> list[int]:
        """Gets the client_ids of this DetailedPost.  # noqa: E501

        Client IDs, optional, filtering attribute. To filter records with no clients, use [null].  # noqa: E501

        :return: The client_ids of this DetailedPost.  # noqa: E501
        :rtype: list[int]
        """
        return self._client_ids

    @client_ids.setter
    def client_ids(self, client_ids: list[int]):
        """Sets the client_ids of this DetailedPost.

        Client IDs, optional, filtering attribute. To filter records with no clients, use [null].  # noqa: E501

        :param client_ids: The client_ids of this DetailedPost.  # noqa: E501
        :type: list[int]
        """

        self._client_ids = client_ids

    @property
    def description(self) -> str:
        """Gets the description of this DetailedPost.  # noqa: E501

        Description, optional, filtering attribute.  # noqa: E501

        :return: The description of this DetailedPost.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this DetailedPost.

        Description, optional, filtering attribute.  # noqa: E501

        :param description: The description of this DetailedPost.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def end_date(self) -> str:
        """Gets the end_date of this DetailedPost.  # noqa: E501

        End date, example time.DateOnly. Should be greater than Start date.  # noqa: E501

        :return: The end_date of this DetailedPost.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: str):
        """Sets the end_date of this DetailedPost.

        End date, example time.DateOnly. Should be greater than Start date.  # noqa: E501

        :param end_date: The end_date of this DetailedPost.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def first_id(self) -> int:
        """Gets the first_id of this DetailedPost.  # noqa: E501


        :return: The first_id of this DetailedPost.  # noqa: E501
        :rtype: int
        """
        return self._first_id

    @first_id.setter
    def first_id(self, first_id: int):
        """Sets the first_id of this DetailedPost.


        :param first_id: The first_id of this DetailedPost.  # noqa: E501
        :type: int
        """

        self._first_id = first_id

    @property
    def first_row_number(self) -> int:
        """Gets the first_row_number of this DetailedPost.  # noqa: E501


        :return: The first_row_number of this DetailedPost.  # noqa: E501
        :rtype: int
        """
        return self._first_row_number

    @first_row_number.setter
    def first_row_number(self, first_row_number: int):
        """Sets the first_row_number of this DetailedPost.


        :param first_row_number: The first_row_number of this DetailedPost.  # noqa: E501
        :type: int
        """

        self._first_row_number = first_row_number

    @property
    def first_timestamp(self) -> int:
        """Gets the first_timestamp of this DetailedPost.  # noqa: E501


        :return: The first_timestamp of this DetailedPost.  # noqa: E501
        :rtype: int
        """
        return self._first_timestamp

    @first_timestamp.setter
    def first_timestamp(self, first_timestamp: int):
        """Sets the first_timestamp of this DetailedPost.


        :param first_timestamp: The first_timestamp of this DetailedPost.  # noqa: E501
        :type: int
        """

        self._first_timestamp = first_timestamp

    @property
    def group_ids(self) -> list[int]:
        """Gets the group_ids of this DetailedPost.  # noqa: E501

        Group IDs, optional, filtering attribute.  # noqa: E501

        :return: The group_ids of this DetailedPost.  # noqa: E501
        :rtype: list[int]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids: list[int]):
        """Sets the group_ids of this DetailedPost.

        Group IDs, optional, filtering attribute.  # noqa: E501

        :param group_ids: The group_ids of this DetailedPost.  # noqa: E501
        :type: list[int]
        """

        self._group_ids = group_ids

    @property
    def grouped(self) -> bool:
        """Gets the grouped of this DetailedPost.  # noqa: E501

        Whether time entries should be grouped, optional, default false.  # noqa: E501

        :return: The grouped of this DetailedPost.  # noqa: E501
        :rtype: bool
        """
        return self._grouped

    @grouped.setter
    def grouped(self, grouped: bool):
        """Sets the grouped of this DetailedPost.

        Whether time entries should be grouped, optional, default false.  # noqa: E501

        :param grouped: The grouped of this DetailedPost.  # noqa: E501
        :type: bool
        """

        self._grouped = grouped

    @property
    def hide_amounts(self) -> bool:
        """Gets the hide_amounts of this DetailedPost.  # noqa: E501

        Whether amounts should be hidden, optional, default false.  # noqa: E501

        :return: The hide_amounts of this DetailedPost.  # noqa: E501
        :rtype: bool
        """
        return self._hide_amounts

    @hide_amounts.setter
    def hide_amounts(self, hide_amounts: bool):
        """Sets the hide_amounts of this DetailedPost.

        Whether amounts should be hidden, optional, default false.  # noqa: E501

        :param hide_amounts: The hide_amounts of this DetailedPost.  # noqa: E501
        :type: bool
        """

        self._hide_amounts = hide_amounts

    @property
    def max_duration_seconds(self) -> int:
        """Gets the max_duration_seconds of this DetailedPost.  # noqa: E501

        Max duration seconds, optional, filtering attribute. Time Audit only, should be greater than MinDurationSeconds.  # noqa: E501

        :return: The max_duration_seconds of this DetailedPost.  # noqa: E501
        :rtype: int
        """
        return self._max_duration_seconds

    @max_duration_seconds.setter
    def max_duration_seconds(self, max_duration_seconds: int):
        """Sets the max_duration_seconds of this DetailedPost.

        Max duration seconds, optional, filtering attribute. Time Audit only, should be greater than MinDurationSeconds.  # noqa: E501

        :param max_duration_seconds: The max_duration_seconds of this DetailedPost.  # noqa: E501
        :type: int
        """

        self._max_duration_seconds = max_duration_seconds

    @property
    def min_duration_seconds(self) -> int:
        """Gets the min_duration_seconds of this DetailedPost.  # noqa: E501

        Min duration seconds, optional, filtering attribute. Time Audit only, should be less than MaxDurationSeconds.  # noqa: E501

        :return: The min_duration_seconds of this DetailedPost.  # noqa: E501
        :rtype: int
        """
        return self._min_duration_seconds

    @min_duration_seconds.setter
    def min_duration_seconds(self, min_duration_seconds: int):
        """Sets the min_duration_seconds of this DetailedPost.

        Min duration seconds, optional, filtering attribute. Time Audit only, should be less than MaxDurationSeconds.  # noqa: E501

        :param min_duration_seconds: The min_duration_seconds of this DetailedPost.  # noqa: E501
        :type: int
        """

        self._min_duration_seconds = min_duration_seconds

    @property
    def order_by(self) -> str:
        """Gets the order_by of this DetailedPost.  # noqa: E501

        Order by field, optional, default \"date\". Can be \"date\", \"user\", \"duration\", \"description\" or \"last_update\".  # noqa: E501

        :return: The order_by of this DetailedPost.  # noqa: E501
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by: str):
        """Sets the order_by of this DetailedPost.

        Order by field, optional, default \"date\". Can be \"date\", \"user\", \"duration\", \"description\" or \"last_update\".  # noqa: E501

        :param order_by: The order_by of this DetailedPost.  # noqa: E501
        :type: str
        """

        self._order_by = order_by

    @property
    def order_dir(self) -> str:
        """Gets the order_dir of this DetailedPost.  # noqa: E501

        Order direction, optional. Can be ASC or DESC.  # noqa: E501

        :return: The order_dir of this DetailedPost.  # noqa: E501
        :rtype: str
        """
        return self._order_dir

    @order_dir.setter
    def order_dir(self, order_dir: str):
        """Sets the order_dir of this DetailedPost.

        Order direction, optional. Can be ASC or DESC.  # noqa: E501

        :param order_dir: The order_dir of this DetailedPost.  # noqa: E501
        :type: str
        """

        self._order_dir = order_dir

    @property
    def page_size(self) -> int:
        """Gets the page_size of this DetailedPost.  # noqa: E501

        PageSize defines the number of items per page, optional, default 50.  # noqa: E501

        :return: The page_size of this DetailedPost.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size: int):
        """Sets the page_size of this DetailedPost.

        PageSize defines the number of items per page, optional, default 50.  # noqa: E501

        :param page_size: The page_size of this DetailedPost.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def posted_fields(self) -> list[str]:
        """Gets the posted_fields of this DetailedPost.  # noqa: E501


        :return: The posted_fields of this DetailedPost.  # noqa: E501
        :rtype: list[str]
        """
        return self._posted_fields

    @posted_fields.setter
    def posted_fields(self, posted_fields: list[str]):
        """Sets the posted_fields of this DetailedPost.


        :param posted_fields: The posted_fields of this DetailedPost.  # noqa: E501
        :type: list[str]
        """

        self._posted_fields = posted_fields

    @property
    def project_ids(self) -> list[int]:
        """Gets the project_ids of this DetailedPost.  # noqa: E501

        Project IDs, optional, filtering attribute. To filter records with no projects, use [null].  # noqa: E501

        :return: The project_ids of this DetailedPost.  # noqa: E501
        :rtype: list[int]
        """
        return self._project_ids

    @project_ids.setter
    def project_ids(self, project_ids: list[int]):
        """Sets the project_ids of this DetailedPost.

        Project IDs, optional, filtering attribute. To filter records with no projects, use [null].  # noqa: E501

        :param project_ids: The project_ids of this DetailedPost.  # noqa: E501
        :type: list[int]
        """

        self._project_ids = project_ids

    @property
    def rounding(self) -> int:
        """Gets the rounding of this DetailedPost.  # noqa: E501

        Whether time should be rounded, optional, default from workspace settings.  # noqa: E501

        :return: The rounding of this DetailedPost.  # noqa: E501
        :rtype: int
        """
        return self._rounding

    @rounding.setter
    def rounding(self, rounding: int):
        """Sets the rounding of this DetailedPost.

        Whether time should be rounded, optional, default from workspace settings.  # noqa: E501

        :param rounding: The rounding of this DetailedPost.  # noqa: E501
        :type: int
        """

        self._rounding = rounding

    @property
    def rounding_minutes(self) -> int:
        """Gets the rounding_minutes of this DetailedPost.  # noqa: E501

        Rounding minutes value, optional, default from workspace settings. Should be 0, 1, 5, 6, 10, 12, 15, 30, 60 or 240.  # noqa: E501

        :return: The rounding_minutes of this DetailedPost.  # noqa: E501
        :rtype: int
        """
        return self._rounding_minutes

    @rounding_minutes.setter
    def rounding_minutes(self, rounding_minutes: int):
        """Sets the rounding_minutes of this DetailedPost.

        Rounding minutes value, optional, default from workspace settings. Should be 0, 1, 5, 6, 10, 12, 15, 30, 60 or 240.  # noqa: E501

        :param rounding_minutes: The rounding_minutes of this DetailedPost.  # noqa: E501
        :type: int
        """

        self._rounding_minutes = rounding_minutes

    @property
    def start_time(self) -> str:
        """Gets the start_time of this DetailedPost.  # noqa: E501


        :return: The start_time of this DetailedPost.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time: str):
        """Sets the start_time of this DetailedPost.


        :param start_time: The start_time of this DetailedPost.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def start_date(self) -> str:
        """Gets the start_date of this DetailedPost.  # noqa: E501

        Start date, example time.DateOnly. Should be less than End date.  # noqa: E501

        :return: The start_date of this DetailedPost.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: str):
        """Sets the start_date of this DetailedPost.

        Start date, example time.DateOnly. Should be less than End date.  # noqa: E501

        :param start_date: The start_date of this DetailedPost.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def tag_ids(self) -> list[int]:
        """Gets the tag_ids of this DetailedPost.  # noqa: E501

        Tag IDs, optional, filtering attribute. To filter records with no tags, use [null].  # noqa: E501

        :return: The tag_ids of this DetailedPost.  # noqa: E501
        :rtype: list[int]
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids: list[int]):
        """Sets the tag_ids of this DetailedPost.

        Tag IDs, optional, filtering attribute. To filter records with no tags, use [null].  # noqa: E501

        :param tag_ids: The tag_ids of this DetailedPost.  # noqa: E501
        :type: list[int]
        """

        self._tag_ids = tag_ids

    @property
    def task_ids(self) -> list[int]:
        """Gets the task_ids of this DetailedPost.  # noqa: E501

        Task IDs, optional, filtering attribute. To filter records with no tasks, use [null].  # noqa: E501

        :return: The task_ids of this DetailedPost.  # noqa: E501
        :rtype: list[int]
        """
        return self._task_ids

    @task_ids.setter
    def task_ids(self, task_ids: list[int]):
        """Sets the task_ids of this DetailedPost.

        Task IDs, optional, filtering attribute. To filter records with no tasks, use [null].  # noqa: E501

        :param task_ids: The task_ids of this DetailedPost.  # noqa: E501
        :type: list[int]
        """

        self._task_ids = task_ids

    @property
    def time_entry_ids(self) -> list[int]:
        """Gets the time_entry_ids of this DetailedPost.  # noqa: E501

        TimeEntryIDs filters by time entries. This was added to support retro-compatibility with reports v2.  # noqa: E501

        :return: The time_entry_ids of this DetailedPost.  # noqa: E501
        :rtype: list[int]
        """
        return self._time_entry_ids

    @time_entry_ids.setter
    def time_entry_ids(self, time_entry_ids: list[int]):
        """Sets the time_entry_ids of this DetailedPost.

        TimeEntryIDs filters by time entries. This was added to support retro-compatibility with reports v2.  # noqa: E501

        :param time_entry_ids: The time_entry_ids of this DetailedPost.  # noqa: E501
        :type: list[int]
        """

        self._time_entry_ids = time_entry_ids

    @property
    def user_ids(self) -> list[int]:
        """Gets the user_ids of this DetailedPost.  # noqa: E501

        User IDs, optional, filtering attribute.  # noqa: E501

        :return: The user_ids of this DetailedPost.  # noqa: E501
        :rtype: list[int]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids: list[int]):
        """Sets the user_ids of this DetailedPost.

        User IDs, optional, filtering attribute.  # noqa: E501

        :param user_ids: The user_ids of this DetailedPost.  # noqa: E501
        :type: list[int]
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
        if issubclass(DetailedPost, dict):
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
        if not isinstance(other, DetailedPost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DetailedPost):
            return True

        return self.to_dict() != other.to_dict()
