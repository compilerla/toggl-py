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


class SubscriptionInvoiceInfo:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "amount": "int",
        "created_at": "str",
        "currency_id": "int",
        "due": "str",
        "id": "int",
        "paid_at": "str",
        "tax_percentage": "float",
        "total_amount": "int",
    }

    attribute_map = {
        "amount": "amount",
        "created_at": "created_at",
        "currency_id": "currency_id",
        "due": "due",
        "id": "id",
        "paid_at": "paid_at",
        "tax_percentage": "tax_percentage",
        "total_amount": "total_amount",
    }

    def __init__(
        self,
        amount: int = None,
        created_at: str = None,
        currency_id: int = None,
        due: str = None,
        id: int = None,
        paid_at: str = None,
        tax_percentage: float = None,
        total_amount: int = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        SubscriptionInvoiceInfo - a model defined in Swagger

        Parameters:
          amount (int): Optional
          created_at (str): Optional
          currency_id (int): Optional
          due (str): Optional
          id (int): Optional
          paid_at (str): Optional
          tax_percentage (float): Optional
          total_amount (int): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._amount = None
        self._created_at = None
        self._currency_id = None
        self._due = None
        self._id = None
        self._paid_at = None
        self._tax_percentage = None
        self._total_amount = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if created_at is not None:
            self.created_at = created_at
        if currency_id is not None:
            self.currency_id = currency_id
        if due is not None:
            self.due = due
        if id is not None:
            self.id = id
        if paid_at is not None:
            self.paid_at = paid_at
        if tax_percentage is not None:
            self.tax_percentage = tax_percentage
        if total_amount is not None:
            self.total_amount = total_amount

    @property
    def amount(self) -> int:
        """Gets the amount of this SubscriptionInvoiceInfo.  # noqa: E501


        :return: The amount of this SubscriptionInvoiceInfo.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount: int):
        """Sets the amount of this SubscriptionInvoiceInfo.


        :param amount: The amount of this SubscriptionInvoiceInfo.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def created_at(self) -> str:
        """Gets the created_at of this SubscriptionInvoiceInfo.  # noqa: E501


        :return: The created_at of this SubscriptionInvoiceInfo.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: str):
        """Sets the created_at of this SubscriptionInvoiceInfo.


        :param created_at: The created_at of this SubscriptionInvoiceInfo.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def currency_id(self) -> int:
        """Gets the currency_id of this SubscriptionInvoiceInfo.  # noqa: E501


        :return: The currency_id of this SubscriptionInvoiceInfo.  # noqa: E501
        :rtype: int
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id: int):
        """Sets the currency_id of this SubscriptionInvoiceInfo.


        :param currency_id: The currency_id of this SubscriptionInvoiceInfo.  # noqa: E501
        :type: int
        """

        self._currency_id = currency_id

    @property
    def due(self) -> str:
        """Gets the due of this SubscriptionInvoiceInfo.  # noqa: E501


        :return: The due of this SubscriptionInvoiceInfo.  # noqa: E501
        :rtype: str
        """
        return self._due

    @due.setter
    def due(self, due: str):
        """Sets the due of this SubscriptionInvoiceInfo.


        :param due: The due of this SubscriptionInvoiceInfo.  # noqa: E501
        :type: str
        """

        self._due = due

    @property
    def id(self) -> int:
        """Gets the id of this SubscriptionInvoiceInfo.  # noqa: E501


        :return: The id of this SubscriptionInvoiceInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this SubscriptionInvoiceInfo.


        :param id: The id of this SubscriptionInvoiceInfo.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def paid_at(self) -> str:
        """Gets the paid_at of this SubscriptionInvoiceInfo.  # noqa: E501


        :return: The paid_at of this SubscriptionInvoiceInfo.  # noqa: E501
        :rtype: str
        """
        return self._paid_at

    @paid_at.setter
    def paid_at(self, paid_at: str):
        """Sets the paid_at of this SubscriptionInvoiceInfo.


        :param paid_at: The paid_at of this SubscriptionInvoiceInfo.  # noqa: E501
        :type: str
        """

        self._paid_at = paid_at

    @property
    def tax_percentage(self) -> float:
        """Gets the tax_percentage of this SubscriptionInvoiceInfo.  # noqa: E501


        :return: The tax_percentage of this SubscriptionInvoiceInfo.  # noqa: E501
        :rtype: float
        """
        return self._tax_percentage

    @tax_percentage.setter
    def tax_percentage(self, tax_percentage: float):
        """Sets the tax_percentage of this SubscriptionInvoiceInfo.


        :param tax_percentage: The tax_percentage of this SubscriptionInvoiceInfo.  # noqa: E501
        :type: float
        """

        self._tax_percentage = tax_percentage

    @property
    def total_amount(self) -> int:
        """Gets the total_amount of this SubscriptionInvoiceInfo.  # noqa: E501


        :return: The total_amount of this SubscriptionInvoiceInfo.  # noqa: E501
        :rtype: int
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount: int):
        """Sets the total_amount of this SubscriptionInvoiceInfo.


        :param total_amount: The total_amount of this SubscriptionInvoiceInfo.  # noqa: E501
        :type: int
        """

        self._total_amount = total_amount

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
        if issubclass(SubscriptionInvoiceInfo, dict):
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
        if not isinstance(other, SubscriptionInvoiceInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionInvoiceInfo):
            return True

        return self.to_dict() != other.to_dict()
