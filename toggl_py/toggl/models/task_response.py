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
from toggl.models.task_with_total import TaskWithTotal  # noqa: F401


class TaskResponse:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "data": "list[TaskWithTotal]",
        "page": "int",
        "per_page": "int",
        "sort_field": "str",
        "sort_order": "str",
        "total_count": "int",
    }

    attribute_map = {
        "data": "data",
        "page": "page",
        "per_page": "per_page",
        "sort_field": "sort_field",
        "sort_order": "sort_order",
        "total_count": "total_count",
    }

    def __init__(
        self,
        data: list[TaskWithTotal] = None,
        page: int = None,
        per_page: int = None,
        sort_field: str = None,
        sort_order: str = None,
        total_count: int = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        TaskResponse - a model defined in Swagger

        Parameters:
          data (list[TaskWithTotal]): Optional
          page (int): Optional
          per_page (int): Optional
          sort_field (str): Optional
          sort_order (str): Optional
          total_count (int): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._data = None
        self._page = None
        self._per_page = None
        self._sort_field = None
        self._sort_order = None
        self._total_count = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_order is not None:
            self.sort_order = sort_order
        if total_count is not None:
            self.total_count = total_count

    @property
    def data(self) -> list[TaskWithTotal]:
        """Gets the data of this TaskResponse.  # noqa: E501


        :return: The data of this TaskResponse.  # noqa: E501
        :rtype: list[TaskWithTotal]
        """
        return self._data

    @data.setter
    def data(self, data: list[TaskWithTotal]):
        """Sets the data of this TaskResponse.


        :param data: The data of this TaskResponse.  # noqa: E501
        :type: list[TaskWithTotal]
        """

        self._data = data

    @property
    def page(self) -> int:
        """Gets the page of this TaskResponse.  # noqa: E501


        :return: The page of this TaskResponse.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page: int):
        """Sets the page of this TaskResponse.


        :param page: The page of this TaskResponse.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def per_page(self) -> int:
        """Gets the per_page of this TaskResponse.  # noqa: E501


        :return: The per_page of this TaskResponse.  # noqa: E501
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page: int):
        """Sets the per_page of this TaskResponse.


        :param per_page: The per_page of this TaskResponse.  # noqa: E501
        :type: int
        """

        self._per_page = per_page

    @property
    def sort_field(self) -> str:
        """Gets the sort_field of this TaskResponse.  # noqa: E501


        :return: The sort_field of this TaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field: str):
        """Sets the sort_field of this TaskResponse.


        :param sort_field: The sort_field of this TaskResponse.  # noqa: E501
        :type: str
        """

        self._sort_field = sort_field

    @property
    def sort_order(self) -> str:
        """Gets the sort_order of this TaskResponse.  # noqa: E501


        :return: The sort_order of this TaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order: str):
        """Sets the sort_order of this TaskResponse.


        :param sort_order: The sort_order of this TaskResponse.  # noqa: E501
        :type: str
        """

        self._sort_order = sort_order

    @property
    def total_count(self) -> int:
        """Gets the total_count of this TaskResponse.  # noqa: E501


        :return: The total_count of this TaskResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count: int):
        """Sets the total_count of this TaskResponse.


        :param total_count: The total_count of this TaskResponse.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if issubclass(TaskResponse, dict):
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
        if not isinstance(other, TaskResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskResponse):
            return True

        return self.to_dict() != other.to_dict()
