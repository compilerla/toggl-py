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


class CustomerCoupon:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "amount_off": "int",
        "deleted": "bool",
        "duration": "str",
        "duration_in_months": "int",
        "id": "str",
        "name": "str",
        "percent_off": "float",
        "valid": "bool",
    }

    attribute_map = {
        "amount_off": "amount_off",
        "deleted": "deleted",
        "duration": "duration",
        "duration_in_months": "duration_in_months",
        "id": "id",
        "name": "name",
        "percent_off": "percent_off",
        "valid": "valid",
    }

    def __init__(
        self,
        amount_off: int = None,
        deleted: bool = None,
        duration: str = None,
        duration_in_months: int = None,
        id: str = None,
        name: str = None,
        percent_off: float = None,
        valid: bool = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        CustomerCoupon - a model defined in Swagger

        Parameters:
          amount_off (int): Optional
          deleted (bool): Optional
          duration (str): Optional
          duration_in_months (int): Optional
          id (str): Optional
          name (str): Optional
          percent_off (float): Optional
          valid (bool): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._amount_off = None
        self._deleted = None
        self._duration = None
        self._duration_in_months = None
        self._id = None
        self._name = None
        self._percent_off = None
        self._valid = None
        self.discriminator = None

        if amount_off is not None:
            self.amount_off = amount_off
        if deleted is not None:
            self.deleted = deleted
        if duration is not None:
            self.duration = duration
        if duration_in_months is not None:
            self.duration_in_months = duration_in_months
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if percent_off is not None:
            self.percent_off = percent_off
        if valid is not None:
            self.valid = valid

    @property
    def amount_off(self) -> int:
        """Gets the amount_off of this CustomerCoupon.  # noqa: E501


        :return: The amount_off of this CustomerCoupon.  # noqa: E501
        :rtype: int
        """
        return self._amount_off

    @amount_off.setter
    def amount_off(self, amount_off: int):
        """Sets the amount_off of this CustomerCoupon.


        :param amount_off: The amount_off of this CustomerCoupon.  # noqa: E501
        :type: int
        """

        self._amount_off = amount_off

    @property
    def deleted(self) -> bool:
        """Gets the deleted of this CustomerCoupon.  # noqa: E501


        :return: The deleted of this CustomerCoupon.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted: bool):
        """Sets the deleted of this CustomerCoupon.


        :param deleted: The deleted of this CustomerCoupon.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def duration(self) -> str:
        """Gets the duration of this CustomerCoupon.  # noqa: E501


        :return: The duration of this CustomerCoupon.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration: str):
        """Sets the duration of this CustomerCoupon.


        :param duration: The duration of this CustomerCoupon.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def duration_in_months(self) -> int:
        """Gets the duration_in_months of this CustomerCoupon.  # noqa: E501


        :return: The duration_in_months of this CustomerCoupon.  # noqa: E501
        :rtype: int
        """
        return self._duration_in_months

    @duration_in_months.setter
    def duration_in_months(self, duration_in_months: int):
        """Sets the duration_in_months of this CustomerCoupon.


        :param duration_in_months: The duration_in_months of this CustomerCoupon.  # noqa: E501
        :type: int
        """

        self._duration_in_months = duration_in_months

    @property
    def id(self) -> str:
        """Gets the id of this CustomerCoupon.  # noqa: E501


        :return: The id of this CustomerCoupon.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this CustomerCoupon.


        :param id: The id of this CustomerCoupon.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this CustomerCoupon.  # noqa: E501


        :return: The name of this CustomerCoupon.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this CustomerCoupon.


        :param name: The name of this CustomerCoupon.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def percent_off(self) -> float:
        """Gets the percent_off of this CustomerCoupon.  # noqa: E501


        :return: The percent_off of this CustomerCoupon.  # noqa: E501
        :rtype: float
        """
        return self._percent_off

    @percent_off.setter
    def percent_off(self, percent_off: float):
        """Sets the percent_off of this CustomerCoupon.


        :param percent_off: The percent_off of this CustomerCoupon.  # noqa: E501
        :type: float
        """

        self._percent_off = percent_off

    @property
    def valid(self) -> bool:
        """Gets the valid of this CustomerCoupon.  # noqa: E501


        :return: The valid of this CustomerCoupon.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid: bool):
        """Sets the valid of this CustomerCoupon.


        :param valid: The valid of this CustomerCoupon.  # noqa: E501
        :type: bool
        """

        self._valid = valid

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
        if issubclass(CustomerCoupon, dict):
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
        if not isinstance(other, CustomerCoupon):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerCoupon):
            return True

        return self.to_dict() != other.to_dict()
