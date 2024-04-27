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


class CustomerPaymentMethodCard:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"brand": "str", "country": "str", "exp_month": "int", "exp_year": "int", "last4": "str"}

    attribute_map = {
        "brand": "brand",
        "country": "country",
        "exp_month": "exp_month",
        "exp_year": "exp_year",
        "last4": "last4",
    }

    def __init__(self, brand=None, country=None, exp_month=None, exp_year=None, last4=None, _configuration=None):  # noqa: E501
        """CustomerPaymentMethodCard - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._brand = None
        self._country = None
        self._exp_month = None
        self._exp_year = None
        self._last4 = None
        self.discriminator = None

        if brand is not None:
            self.brand = brand
        if country is not None:
            self.country = country
        if exp_month is not None:
            self.exp_month = exp_month
        if exp_year is not None:
            self.exp_year = exp_year
        if last4 is not None:
            self.last4 = last4

    @property
    def brand(self):
        """Gets the brand of this CustomerPaymentMethodCard.  # noqa: E501


        :return: The brand of this CustomerPaymentMethodCard.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this CustomerPaymentMethodCard.


        :param brand: The brand of this CustomerPaymentMethodCard.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def country(self):
        """Gets the country of this CustomerPaymentMethodCard.  # noqa: E501


        :return: The country of this CustomerPaymentMethodCard.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CustomerPaymentMethodCard.


        :param country: The country of this CustomerPaymentMethodCard.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def exp_month(self):
        """Gets the exp_month of this CustomerPaymentMethodCard.  # noqa: E501


        :return: The exp_month of this CustomerPaymentMethodCard.  # noqa: E501
        :rtype: int
        """
        return self._exp_month

    @exp_month.setter
    def exp_month(self, exp_month):
        """Sets the exp_month of this CustomerPaymentMethodCard.


        :param exp_month: The exp_month of this CustomerPaymentMethodCard.  # noqa: E501
        :type: int
        """

        self._exp_month = exp_month

    @property
    def exp_year(self):
        """Gets the exp_year of this CustomerPaymentMethodCard.  # noqa: E501


        :return: The exp_year of this CustomerPaymentMethodCard.  # noqa: E501
        :rtype: int
        """
        return self._exp_year

    @exp_year.setter
    def exp_year(self, exp_year):
        """Sets the exp_year of this CustomerPaymentMethodCard.


        :param exp_year: The exp_year of this CustomerPaymentMethodCard.  # noqa: E501
        :type: int
        """

        self._exp_year = exp_year

    @property
    def last4(self):
        """Gets the last4 of this CustomerPaymentMethodCard.  # noqa: E501


        :return: The last4 of this CustomerPaymentMethodCard.  # noqa: E501
        :rtype: str
        """
        return self._last4

    @last4.setter
    def last4(self, last4):
        """Sets the last4 of this CustomerPaymentMethodCard.


        :param last4: The last4 of this CustomerPaymentMethodCard.  # noqa: E501
        :type: str
        """

        self._last4 = last4

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
        if issubclass(CustomerPaymentMethodCard, dict):
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
        if not isinstance(other, CustomerPaymentMethodCard):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerPaymentMethodCard):
            return True

        return self.to_dict() != other.to_dict()
