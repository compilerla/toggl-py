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
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from toggl.models.models_subdivision import ModelsSubdivision  # noqa: F401


class SubscriptionContactDetailRequest:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "company_address": "str",
        "company_city": "str",
        "company_name": "str",
        "contact_email": "str",
        "contact_person": "str",
        "country_id": "int",
        "country_subdivision_id": "int",
        "sub_division": "ModelsSubdivision",
        "tax_number": "str",
        "zip_code": "str",
    }

    attribute_map = {
        "company_address": "company_address",
        "company_city": "company_city",
        "company_name": "company_name",
        "contact_email": "contact_email",
        "contact_person": "contact_person",
        "country_id": "country_id",
        "country_subdivision_id": "country_subdivision_id",
        "sub_division": "subDivision",
        "tax_number": "tax_number",
        "zip_code": "zip_code",
    }

    def __init__(
        self,
        company_address: str,
        company_name: str,
        contact_email: str,
        country_id: int,
        company_city: str = None,
        contact_person: str = None,
        country_subdivision_id: int = None,
        sub_division: ModelsSubdivision = None,
        tax_number: str = None,
        zip_code: str = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        SubscriptionContactDetailRequest - a model defined in Swagger

        Parameters:
          company_address (str): Required
          company_name (str): Required
          contact_email (str): Required
          country_id (int): Required
          company_city (str): Optional
          contact_person (str): Optional
          country_subdivision_id (int): Optional
          sub_division (ModelsSubdivision): Optional
          tax_number (str): Optional
          zip_code (str): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._company_address = None
        self._company_city = None
        self._company_name = None
        self._contact_email = None
        self._contact_person = None
        self._country_id = None
        self._country_subdivision_id = None
        self._sub_division = None
        self._tax_number = None
        self._zip_code = None
        self.discriminator = None

        self.company_address = company_address
        if company_city is not None:
            self.company_city = company_city
        self.company_name = company_name
        self.contact_email = contact_email
        if contact_person is not None:
            self.contact_person = contact_person
        self.country_id = country_id
        if country_subdivision_id is not None:
            self.country_subdivision_id = country_subdivision_id
        if sub_division is not None:
            self.sub_division = sub_division
        if tax_number is not None:
            self.tax_number = tax_number
        if zip_code is not None:
            self.zip_code = zip_code

    @property
    def company_address(self) -> str:
        """Gets the company_address of this SubscriptionContactDetailRequest.  # noqa: E501


        :return: The company_address of this SubscriptionContactDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._company_address

    @company_address.setter
    def company_address(self, company_address: str):
        """Sets the company_address of this SubscriptionContactDetailRequest.


        :param company_address: The company_address of this SubscriptionContactDetailRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and company_address is None:
            raise ValueError("Invalid value for `company_address`, must not be `None`")  # noqa: E501

        self._company_address = company_address

    @property
    def company_city(self) -> str:
        """Gets the company_city of this SubscriptionContactDetailRequest.  # noqa: E501


        :return: The company_city of this SubscriptionContactDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._company_city

    @company_city.setter
    def company_city(self, company_city: str):
        """Sets the company_city of this SubscriptionContactDetailRequest.


        :param company_city: The company_city of this SubscriptionContactDetailRequest.  # noqa: E501
        :type: str
        """

        self._company_city = company_city

    @property
    def company_name(self) -> str:
        """Gets the company_name of this SubscriptionContactDetailRequest.  # noqa: E501


        :return: The company_name of this SubscriptionContactDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name: str):
        """Sets the company_name of this SubscriptionContactDetailRequest.


        :param company_name: The company_name of this SubscriptionContactDetailRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and company_name is None:
            raise ValueError("Invalid value for `company_name`, must not be `None`")  # noqa: E501

        self._company_name = company_name

    @property
    def contact_email(self) -> str:
        """Gets the contact_email of this SubscriptionContactDetailRequest.  # noqa: E501


        :return: The contact_email of this SubscriptionContactDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email: str):
        """Sets the contact_email of this SubscriptionContactDetailRequest.


        :param contact_email: The contact_email of this SubscriptionContactDetailRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and contact_email is None:
            raise ValueError("Invalid value for `contact_email`, must not be `None`")  # noqa: E501

        self._contact_email = contact_email

    @property
    def contact_person(self) -> str:
        """Gets the contact_person of this SubscriptionContactDetailRequest.  # noqa: E501


        :return: The contact_person of this SubscriptionContactDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._contact_person

    @contact_person.setter
    def contact_person(self, contact_person: str):
        """Sets the contact_person of this SubscriptionContactDetailRequest.


        :param contact_person: The contact_person of this SubscriptionContactDetailRequest.  # noqa: E501
        :type: str
        """

        self._contact_person = contact_person

    @property
    def country_id(self) -> int:
        """Gets the country_id of this SubscriptionContactDetailRequest.  # noqa: E501


        :return: The country_id of this SubscriptionContactDetailRequest.  # noqa: E501
        :rtype: int
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id: int):
        """Sets the country_id of this SubscriptionContactDetailRequest.


        :param country_id: The country_id of this SubscriptionContactDetailRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and country_id is None:
            raise ValueError("Invalid value for `country_id`, must not be `None`")  # noqa: E501

        self._country_id = country_id

    @property
    def country_subdivision_id(self) -> int:
        """Gets the country_subdivision_id of this SubscriptionContactDetailRequest.  # noqa: E501

        CountrySubdivisionID is the ID of the country subdivision (state in USA) This field is required if country_id == 235 (United states)  # noqa: E501

        :return: The country_subdivision_id of this SubscriptionContactDetailRequest.  # noqa: E501
        :rtype: int
        """
        return self._country_subdivision_id

    @country_subdivision_id.setter
    def country_subdivision_id(self, country_subdivision_id: int):
        """Sets the country_subdivision_id of this SubscriptionContactDetailRequest.

        CountrySubdivisionID is the ID of the country subdivision (state in USA) This field is required if country_id == 235 (United states)  # noqa: E501

        :param country_subdivision_id: The country_subdivision_id of this SubscriptionContactDetailRequest.  # noqa: E501
        :type: int
        """

        self._country_subdivision_id = country_subdivision_id

    @property
    def sub_division(self) -> ModelsSubdivision:
        """Gets the sub_division of this SubscriptionContactDetailRequest.  # noqa: E501


        :return: The sub_division of this SubscriptionContactDetailRequest.  # noqa: E501
        :rtype: ModelsSubdivision
        """
        return self._sub_division

    @sub_division.setter
    def sub_division(self, sub_division: ModelsSubdivision):
        """Sets the sub_division of this SubscriptionContactDetailRequest.


        :param sub_division: The sub_division of this SubscriptionContactDetailRequest.  # noqa: E501
        :type: ModelsSubdivision
        """

        self._sub_division = sub_division

    @property
    def tax_number(self) -> str:
        """Gets the tax_number of this SubscriptionContactDetailRequest.  # noqa: E501


        :return: The tax_number of this SubscriptionContactDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._tax_number

    @tax_number.setter
    def tax_number(self, tax_number: str):
        """Sets the tax_number of this SubscriptionContactDetailRequest.


        :param tax_number: The tax_number of this SubscriptionContactDetailRequest.  # noqa: E501
        :type: str
        """

        self._tax_number = tax_number

    @property
    def zip_code(self) -> str:
        """Gets the zip_code of this SubscriptionContactDetailRequest.  # noqa: E501

        ZIPCode field is required if country_id == 235 (United states)  # noqa: E501

        :return: The zip_code of this SubscriptionContactDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code: str):
        """Sets the zip_code of this SubscriptionContactDetailRequest.

        ZIPCode field is required if country_id == 235 (United states)  # noqa: E501

        :param zip_code: The zip_code of this SubscriptionContactDetailRequest.  # noqa: E501
        :type: str
        """

        self._zip_code = zip_code

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
        if issubclass(SubscriptionContactDetailRequest, dict):
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
        if not isinstance(other, SubscriptionContactDetailRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionContactDetailRequest):
            return True

        return self.to_dict() != other.to_dict()
