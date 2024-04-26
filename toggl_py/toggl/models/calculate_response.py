"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Last changed: 2024-04-26T22:13:16.785Z
Generated by: https://github.com/compilerla/toggl-py/tree/main/codegen
"""

import pprint
import re  # noqa: F401

from toggl.configuration import Configuration


class CalculateResponse:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"calculation": "str", "currency": "str", "period": "int", "tax_percentage": "int", "total_amount": "int"}

    attribute_map = {
        "calculation": "calculation",
        "currency": "currency",
        "period": "period",
        "tax_percentage": "tax_percentage",
        "total_amount": "total_amount",
    }

    def __init__(
        self, calculation=None, currency=None, period=None, tax_percentage=None, total_amount=None, _configuration=None
    ):  # noqa: E501
        """CalculateResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._calculation = None
        self._currency = None
        self._period = None
        self._tax_percentage = None
        self._total_amount = None
        self.discriminator = None

        if calculation is not None:
            self.calculation = calculation
        if currency is not None:
            self.currency = currency
        if period is not None:
            self.period = period
        if tax_percentage is not None:
            self.tax_percentage = tax_percentage
        if total_amount is not None:
            self.total_amount = total_amount

    @property
    def calculation(self):
        """Gets the calculation of this CalculateResponse.  # noqa: E501


        :return: The calculation of this CalculateResponse.  # noqa: E501
        :rtype: str
        """
        return self._calculation

    @calculation.setter
    def calculation(self, calculation):
        """Sets the calculation of this CalculateResponse.


        :param calculation: The calculation of this CalculateResponse.  # noqa: E501
        :type: str
        """

        self._calculation = calculation

    @property
    def currency(self):
        """Gets the currency of this CalculateResponse.  # noqa: E501


        :return: The currency of this CalculateResponse.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CalculateResponse.


        :param currency: The currency of this CalculateResponse.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def period(self):
        """Gets the period of this CalculateResponse.  # noqa: E501


        :return: The period of this CalculateResponse.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this CalculateResponse.


        :param period: The period of this CalculateResponse.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def tax_percentage(self):
        """Gets the tax_percentage of this CalculateResponse.  # noqa: E501


        :return: The tax_percentage of this CalculateResponse.  # noqa: E501
        :rtype: int
        """
        return self._tax_percentage

    @tax_percentage.setter
    def tax_percentage(self, tax_percentage):
        """Sets the tax_percentage of this CalculateResponse.


        :param tax_percentage: The tax_percentage of this CalculateResponse.  # noqa: E501
        :type: int
        """

        self._tax_percentage = tax_percentage

    @property
    def total_amount(self):
        """Gets the total_amount of this CalculateResponse.  # noqa: E501


        :return: The total_amount of this CalculateResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this CalculateResponse.


        :param total_amount: The total_amount of this CalculateResponse.  # noqa: E501
        :type: int
        """

        self._total_amount = total_amount

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
        if issubclass(CalculateResponse, dict):
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
        if not isinstance(other, CalculateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CalculateResponse):
            return True

        return self.to_dict() != other.to_dict()
