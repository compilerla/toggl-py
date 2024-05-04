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


class ModelsUserInvoiceTax:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {"amount": "float", "name": "str", "tax_id": "int"}

    attribute_map = {"amount": "amount", "name": "name", "tax_id": "tax_id"}

    def __init__(
        self, amount: float = None, name: str = None, tax_id: int = None, _configuration: Configuration = None  # noqa: E501
    ):
        """
        ModelsUserInvoiceTax - a model defined in Swagger

        Parameters:
          amount (float): Optional
          name (str): Optional
          tax_id (int): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._amount = None
        self._name = None
        self._tax_id = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if name is not None:
            self.name = name
        if tax_id is not None:
            self.tax_id = tax_id

    @property
    def amount(self) -> float:
        """Gets the amount of this ModelsUserInvoiceTax.  # noqa: E501


        :return: The amount of this ModelsUserInvoiceTax.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        """Sets the amount of this ModelsUserInvoiceTax.


        :param amount: The amount of this ModelsUserInvoiceTax.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def name(self) -> str:
        """Gets the name of this ModelsUserInvoiceTax.  # noqa: E501


        :return: The name of this ModelsUserInvoiceTax.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ModelsUserInvoiceTax.


        :param name: The name of this ModelsUserInvoiceTax.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tax_id(self) -> int:
        """Gets the tax_id of this ModelsUserInvoiceTax.  # noqa: E501


        :return: The tax_id of this ModelsUserInvoiceTax.  # noqa: E501
        :rtype: int
        """
        return self._tax_id

    @tax_id.setter
    def tax_id(self, tax_id: int):
        """Sets the tax_id of this ModelsUserInvoiceTax.


        :param tax_id: The tax_id of this ModelsUserInvoiceTax.  # noqa: E501
        :type: int
        """

        self._tax_id = tax_id

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
        if issubclass(ModelsUserInvoiceTax, dict):
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
        if not isinstance(other, ModelsUserInvoiceTax):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsUserInvoiceTax):
            return True

        return self.to_dict() != other.to_dict()
