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


class SavedListParams:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "fixed_dates": "bool",
        "name": "str",
        "page": "int",
        "per_page": "int",
        "public": "bool",
        "scheduled": "bool",
        "sort_direction": "str",
        "sort_field": "str",
    }

    attribute_map = {
        "fixed_dates": "fixed_dates",
        "name": "name",
        "page": "page",
        "per_page": "per_page",
        "public": "public",
        "scheduled": "scheduled",
        "sort_direction": "sort_direction",
        "sort_field": "sort_field",
    }

    def __init__(
        self,
        fixed_dates: bool = None,
        name: str = None,
        page: int = None,
        per_page: int = None,
        public: bool = None,
        scheduled: bool = None,
        sort_direction: str = None,
        sort_field: str = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        SavedListParams - a model defined in Swagger

        Parameters:
          fixed_dates (bool): Optional
          name (str): Optional
          page (int): Optional
          per_page (int): Optional
          public (bool): Optional
          scheduled (bool): Optional
          sort_direction (str): Optional
          sort_field (str): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._fixed_dates = None
        self._name = None
        self._page = None
        self._per_page = None
        self._public = None
        self._scheduled = None
        self._sort_direction = None
        self._sort_field = None
        self.discriminator = None

        if fixed_dates is not None:
            self.fixed_dates = fixed_dates
        if name is not None:
            self.name = name
        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page
        if public is not None:
            self.public = public
        if scheduled is not None:
            self.scheduled = scheduled
        if sort_direction is not None:
            self.sort_direction = sort_direction
        if sort_field is not None:
            self.sort_field = sort_field

    @property
    def fixed_dates(self) -> bool:
        """Gets the fixed_dates of this SavedListParams.  # noqa: E501


        :return: The fixed_dates of this SavedListParams.  # noqa: E501
        :rtype: bool
        """
        return self._fixed_dates

    @fixed_dates.setter
    def fixed_dates(self, fixed_dates: bool):
        """Sets the fixed_dates of this SavedListParams.


        :param fixed_dates: The fixed_dates of this SavedListParams.  # noqa: E501
        :type: bool
        """

        self._fixed_dates = fixed_dates

    @property
    def name(self) -> str:
        """Gets the name of this SavedListParams.  # noqa: E501


        :return: The name of this SavedListParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this SavedListParams.


        :param name: The name of this SavedListParams.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def page(self) -> int:
        """Gets the page of this SavedListParams.  # noqa: E501


        :return: The page of this SavedListParams.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page: int):
        """Sets the page of this SavedListParams.


        :param page: The page of this SavedListParams.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def per_page(self) -> int:
        """Gets the per_page of this SavedListParams.  # noqa: E501


        :return: The per_page of this SavedListParams.  # noqa: E501
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page: int):
        """Sets the per_page of this SavedListParams.


        :param per_page: The per_page of this SavedListParams.  # noqa: E501
        :type: int
        """

        self._per_page = per_page

    @property
    def public(self) -> bool:
        """Gets the public of this SavedListParams.  # noqa: E501


        :return: The public of this SavedListParams.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public: bool):
        """Sets the public of this SavedListParams.


        :param public: The public of this SavedListParams.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def scheduled(self) -> bool:
        """Gets the scheduled of this SavedListParams.  # noqa: E501


        :return: The scheduled of this SavedListParams.  # noqa: E501
        :rtype: bool
        """
        return self._scheduled

    @scheduled.setter
    def scheduled(self, scheduled: bool):
        """Sets the scheduled of this SavedListParams.


        :param scheduled: The scheduled of this SavedListParams.  # noqa: E501
        :type: bool
        """

        self._scheduled = scheduled

    @property
    def sort_direction(self) -> str:
        """Gets the sort_direction of this SavedListParams.  # noqa: E501


        :return: The sort_direction of this SavedListParams.  # noqa: E501
        :rtype: str
        """
        return self._sort_direction

    @sort_direction.setter
    def sort_direction(self, sort_direction: str):
        """Sets the sort_direction of this SavedListParams.


        :param sort_direction: The sort_direction of this SavedListParams.  # noqa: E501
        :type: str
        """

        self._sort_direction = sort_direction

    @property
    def sort_field(self) -> str:
        """Gets the sort_field of this SavedListParams.  # noqa: E501


        :return: The sort_field of this SavedListParams.  # noqa: E501
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field: str):
        """Sets the sort_field of this SavedListParams.


        :param sort_field: The sort_field of this SavedListParams.  # noqa: E501
        :type: str
        """

        self._sort_field = sort_field

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
        if issubclass(SavedListParams, dict):
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
        if not isinstance(other, SavedListParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SavedListParams):
            return True

        return self.to_dict() != other.to_dict()
