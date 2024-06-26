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


class ModelsContactDetail:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "company_address": "str",
        "company_city": "str",
        "company_name": "str",
        "contact_detail_id": "int",
        "contact_email": "str",
        "contact_person": "str",
        "country_id": "int",
        "country_subdivision_id": "int",
        "created_at": "str",
        "customer_id": "int",
        "is_eu_resident": "bool",
        "updated_at": "str",
        "user_id": "int",
        "vat_number": "str",
        "vat_number_valid": "bool",
        "vat_number_validated_at": "str",
        "zip_code": "str",
    }

    attribute_map = {
        "company_address": "company_address",
        "company_city": "company_city",
        "company_name": "company_name",
        "contact_detail_id": "contact_detail_id",
        "contact_email": "contact_email",
        "contact_person": "contact_person",
        "country_id": "country_id",
        "country_subdivision_id": "country_subdivision_id",
        "created_at": "created_at",
        "customer_id": "customer_id",
        "is_eu_resident": "is_eu_resident",
        "updated_at": "updated_at",
        "user_id": "user_id",
        "vat_number": "vat_number",
        "vat_number_valid": "vat_number_valid",
        "vat_number_validated_at": "vat_number_validated_at",
        "zip_code": "zip_code",
    }

    def __init__(
        self,
        company_address=None,
        company_city=None,
        company_name=None,
        contact_detail_id=None,
        contact_email=None,
        contact_person=None,
        country_id=None,
        country_subdivision_id=None,
        created_at=None,
        customer_id=None,
        is_eu_resident=None,
        updated_at=None,
        user_id=None,
        vat_number=None,
        vat_number_valid=None,
        vat_number_validated_at=None,
        zip_code=None,
        _configuration=None,
    ):  # noqa: E501
        """ModelsContactDetail - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._company_address = None
        self._company_city = None
        self._company_name = None
        self._contact_detail_id = None
        self._contact_email = None
        self._contact_person = None
        self._country_id = None
        self._country_subdivision_id = None
        self._created_at = None
        self._customer_id = None
        self._is_eu_resident = None
        self._updated_at = None
        self._user_id = None
        self._vat_number = None
        self._vat_number_valid = None
        self._vat_number_validated_at = None
        self._zip_code = None
        self.discriminator = None

        if company_address is not None:
            self.company_address = company_address
        if company_city is not None:
            self.company_city = company_city
        if company_name is not None:
            self.company_name = company_name
        if contact_detail_id is not None:
            self.contact_detail_id = contact_detail_id
        if contact_email is not None:
            self.contact_email = contact_email
        if contact_person is not None:
            self.contact_person = contact_person
        if country_id is not None:
            self.country_id = country_id
        if country_subdivision_id is not None:
            self.country_subdivision_id = country_subdivision_id
        if created_at is not None:
            self.created_at = created_at
        if customer_id is not None:
            self.customer_id = customer_id
        if is_eu_resident is not None:
            self.is_eu_resident = is_eu_resident
        if updated_at is not None:
            self.updated_at = updated_at
        if user_id is not None:
            self.user_id = user_id
        if vat_number is not None:
            self.vat_number = vat_number
        if vat_number_valid is not None:
            self.vat_number_valid = vat_number_valid
        if vat_number_validated_at is not None:
            self.vat_number_validated_at = vat_number_validated_at
        if zip_code is not None:
            self.zip_code = zip_code

    @property
    def company_address(self):
        """Gets the company_address of this ModelsContactDetail.  # noqa: E501


        :return: The company_address of this ModelsContactDetail.  # noqa: E501
        :rtype: str
        """
        return self._company_address

    @company_address.setter
    def company_address(self, company_address):
        """Sets the company_address of this ModelsContactDetail.


        :param company_address: The company_address of this ModelsContactDetail.  # noqa: E501
        :type: str
        """

        self._company_address = company_address

    @property
    def company_city(self):
        """Gets the company_city of this ModelsContactDetail.  # noqa: E501


        :return: The company_city of this ModelsContactDetail.  # noqa: E501
        :rtype: str
        """
        return self._company_city

    @company_city.setter
    def company_city(self, company_city):
        """Sets the company_city of this ModelsContactDetail.


        :param company_city: The company_city of this ModelsContactDetail.  # noqa: E501
        :type: str
        """

        self._company_city = company_city

    @property
    def company_name(self):
        """Gets the company_name of this ModelsContactDetail.  # noqa: E501


        :return: The company_name of this ModelsContactDetail.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ModelsContactDetail.


        :param company_name: The company_name of this ModelsContactDetail.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def contact_detail_id(self):
        """Gets the contact_detail_id of this ModelsContactDetail.  # noqa: E501


        :return: The contact_detail_id of this ModelsContactDetail.  # noqa: E501
        :rtype: int
        """
        return self._contact_detail_id

    @contact_detail_id.setter
    def contact_detail_id(self, contact_detail_id):
        """Sets the contact_detail_id of this ModelsContactDetail.


        :param contact_detail_id: The contact_detail_id of this ModelsContactDetail.  # noqa: E501
        :type: int
        """

        self._contact_detail_id = contact_detail_id

    @property
    def contact_email(self):
        """Gets the contact_email of this ModelsContactDetail.  # noqa: E501


        :return: The contact_email of this ModelsContactDetail.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this ModelsContactDetail.


        :param contact_email: The contact_email of this ModelsContactDetail.  # noqa: E501
        :type: str
        """

        self._contact_email = contact_email

    @property
    def contact_person(self):
        """Gets the contact_person of this ModelsContactDetail.  # noqa: E501


        :return: The contact_person of this ModelsContactDetail.  # noqa: E501
        :rtype: str
        """
        return self._contact_person

    @contact_person.setter
    def contact_person(self, contact_person):
        """Sets the contact_person of this ModelsContactDetail.


        :param contact_person: The contact_person of this ModelsContactDetail.  # noqa: E501
        :type: str
        """

        self._contact_person = contact_person

    @property
    def country_id(self):
        """Gets the country_id of this ModelsContactDetail.  # noqa: E501


        :return: The country_id of this ModelsContactDetail.  # noqa: E501
        :rtype: int
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """Sets the country_id of this ModelsContactDetail.


        :param country_id: The country_id of this ModelsContactDetail.  # noqa: E501
        :type: int
        """

        self._country_id = country_id

    @property
    def country_subdivision_id(self):
        """Gets the country_subdivision_id of this ModelsContactDetail.  # noqa: E501


        :return: The country_subdivision_id of this ModelsContactDetail.  # noqa: E501
        :rtype: int
        """
        return self._country_subdivision_id

    @country_subdivision_id.setter
    def country_subdivision_id(self, country_subdivision_id):
        """Sets the country_subdivision_id of this ModelsContactDetail.


        :param country_subdivision_id: The country_subdivision_id of this ModelsContactDetail.  # noqa: E501
        :type: int
        """

        self._country_subdivision_id = country_subdivision_id

    @property
    def created_at(self):
        """Gets the created_at of this ModelsContactDetail.  # noqa: E501


        :return: The created_at of this ModelsContactDetail.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ModelsContactDetail.


        :param created_at: The created_at of this ModelsContactDetail.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def customer_id(self):
        """Gets the customer_id of this ModelsContactDetail.  # noqa: E501


        :return: The customer_id of this ModelsContactDetail.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ModelsContactDetail.


        :param customer_id: The customer_id of this ModelsContactDetail.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

    @property
    def is_eu_resident(self):
        """Gets the is_eu_resident of this ModelsContactDetail.  # noqa: E501


        :return: The is_eu_resident of this ModelsContactDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_eu_resident

    @is_eu_resident.setter
    def is_eu_resident(self, is_eu_resident):
        """Sets the is_eu_resident of this ModelsContactDetail.


        :param is_eu_resident: The is_eu_resident of this ModelsContactDetail.  # noqa: E501
        :type: bool
        """

        self._is_eu_resident = is_eu_resident

    @property
    def updated_at(self):
        """Gets the updated_at of this ModelsContactDetail.  # noqa: E501


        :return: The updated_at of this ModelsContactDetail.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ModelsContactDetail.


        :param updated_at: The updated_at of this ModelsContactDetail.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def user_id(self):
        """Gets the user_id of this ModelsContactDetail.  # noqa: E501


        :return: The user_id of this ModelsContactDetail.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ModelsContactDetail.


        :param user_id: The user_id of this ModelsContactDetail.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def vat_number(self):
        """Gets the vat_number of this ModelsContactDetail.  # noqa: E501


        :return: The vat_number of this ModelsContactDetail.  # noqa: E501
        :rtype: str
        """
        return self._vat_number

    @vat_number.setter
    def vat_number(self, vat_number):
        """Sets the vat_number of this ModelsContactDetail.


        :param vat_number: The vat_number of this ModelsContactDetail.  # noqa: E501
        :type: str
        """

        self._vat_number = vat_number

    @property
    def vat_number_valid(self):
        """Gets the vat_number_valid of this ModelsContactDetail.  # noqa: E501

        DEPRECATED  # noqa: E501

        :return: The vat_number_valid of this ModelsContactDetail.  # noqa: E501
        :rtype: bool
        """
        return self._vat_number_valid

    @vat_number_valid.setter
    def vat_number_valid(self, vat_number_valid):
        """Sets the vat_number_valid of this ModelsContactDetail.

        DEPRECATED  # noqa: E501

        :param vat_number_valid: The vat_number_valid of this ModelsContactDetail.  # noqa: E501
        :type: bool
        """

        self._vat_number_valid = vat_number_valid

    @property
    def vat_number_validated_at(self):
        """Gets the vat_number_validated_at of this ModelsContactDetail.  # noqa: E501

        DEPRECATED  # noqa: E501

        :return: The vat_number_validated_at of this ModelsContactDetail.  # noqa: E501
        :rtype: str
        """
        return self._vat_number_validated_at

    @vat_number_validated_at.setter
    def vat_number_validated_at(self, vat_number_validated_at):
        """Sets the vat_number_validated_at of this ModelsContactDetail.

        DEPRECATED  # noqa: E501

        :param vat_number_validated_at: The vat_number_validated_at of this ModelsContactDetail.  # noqa: E501
        :type: str
        """

        self._vat_number_validated_at = vat_number_validated_at

    @property
    def zip_code(self):
        """Gets the zip_code of this ModelsContactDetail.  # noqa: E501


        :return: The zip_code of this ModelsContactDetail.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this ModelsContactDetail.


        :param zip_code: The zip_code of this ModelsContactDetail.  # noqa: E501
        :type: str
        """

        self._zip_code = zip_code

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
        if issubclass(ModelsContactDetail, dict):
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
        if not isinstance(other, ModelsContactDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsContactDetail):
            return True

        return self.to_dict() != other.to_dict()
