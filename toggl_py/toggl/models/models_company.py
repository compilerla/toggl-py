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


class ModelsCompany:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "address": "str",
        "bank_details": "str",
        "company_id": "int",
        "name": "str",
        "tax_number": "str",
        "tax_number_name": "str",
        "tax_type": "str",
    }

    attribute_map = {
        "address": "address",
        "bank_details": "bank_details",
        "company_id": "company_id",
        "name": "name",
        "tax_number": "tax_number",
        "tax_number_name": "tax_number_name",
        "tax_type": "tax_type",
    }

    def __init__(
        self,
        address: str = None,
        bank_details: str = None,
        company_id: int = None,
        name: str = None,
        tax_number: str = None,
        tax_number_name: str = None,
        tax_type: str = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        ModelsCompany - a model defined in Swagger

        Parameters:
          address (str): Optional
          bank_details (str): Optional
          company_id (int): Optional
          name (str): Optional
          tax_number (str): Optional
          tax_number_name (str): Optional
          tax_type (str): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address = None
        self._bank_details = None
        self._company_id = None
        self._name = None
        self._tax_number = None
        self._tax_number_name = None
        self._tax_type = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if bank_details is not None:
            self.bank_details = bank_details
        if company_id is not None:
            self.company_id = company_id
        if name is not None:
            self.name = name
        if tax_number is not None:
            self.tax_number = tax_number
        if tax_number_name is not None:
            self.tax_number_name = tax_number_name
        if tax_type is not None:
            self.tax_type = tax_type

    @property
    def address(self) -> str:
        """Gets the address of this ModelsCompany.  # noqa: E501


        :return: The address of this ModelsCompany.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this ModelsCompany.


        :param address: The address of this ModelsCompany.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def bank_details(self) -> str:
        """Gets the bank_details of this ModelsCompany.  # noqa: E501


        :return: The bank_details of this ModelsCompany.  # noqa: E501
        :rtype: str
        """
        return self._bank_details

    @bank_details.setter
    def bank_details(self, bank_details: str):
        """Sets the bank_details of this ModelsCompany.


        :param bank_details: The bank_details of this ModelsCompany.  # noqa: E501
        :type: str
        """

        self._bank_details = bank_details

    @property
    def company_id(self) -> int:
        """Gets the company_id of this ModelsCompany.  # noqa: E501


        :return: The company_id of this ModelsCompany.  # noqa: E501
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id: int):
        """Sets the company_id of this ModelsCompany.


        :param company_id: The company_id of this ModelsCompany.  # noqa: E501
        :type: int
        """

        self._company_id = company_id

    @property
    def name(self) -> str:
        """Gets the name of this ModelsCompany.  # noqa: E501


        :return: The name of this ModelsCompany.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ModelsCompany.


        :param name: The name of this ModelsCompany.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tax_number(self) -> str:
        """Gets the tax_number of this ModelsCompany.  # noqa: E501


        :return: The tax_number of this ModelsCompany.  # noqa: E501
        :rtype: str
        """
        return self._tax_number

    @tax_number.setter
    def tax_number(self, tax_number: str):
        """Sets the tax_number of this ModelsCompany.


        :param tax_number: The tax_number of this ModelsCompany.  # noqa: E501
        :type: str
        """

        self._tax_number = tax_number

    @property
    def tax_number_name(self) -> str:
        """Gets the tax_number_name of this ModelsCompany.  # noqa: E501


        :return: The tax_number_name of this ModelsCompany.  # noqa: E501
        :rtype: str
        """
        return self._tax_number_name

    @tax_number_name.setter
    def tax_number_name(self, tax_number_name: str):
        """Sets the tax_number_name of this ModelsCompany.


        :param tax_number_name: The tax_number_name of this ModelsCompany.  # noqa: E501
        :type: str
        """

        self._tax_number_name = tax_number_name

    @property
    def tax_type(self) -> str:
        """Gets the tax_type of this ModelsCompany.  # noqa: E501


        :return: The tax_type of this ModelsCompany.  # noqa: E501
        :rtype: str
        """
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type: str):
        """Sets the tax_type of this ModelsCompany.


        :param tax_type: The tax_type of this ModelsCompany.  # noqa: E501
        :type: str
        """

        self._tax_type = tax_type

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
        if issubclass(ModelsCompany, dict):
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
        if not isinstance(other, ModelsCompany):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsCompany):
            return True

        return self.to_dict() != other.to_dict()
