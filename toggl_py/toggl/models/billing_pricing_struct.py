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


class BillingPricingStruct:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "currency_id": "int",
        "discount_percentage": "int",
        "discount_to": "str",
        "plans": "list[BillingFancyPlan]",
        "tax_included": "bool",
        "tax_percentage": "float",
        "tax_type": "str",
        "user_count": "int",
    }

    attribute_map = {
        "currency_id": "currency_id",
        "discount_percentage": "discount_percentage",
        "discount_to": "discount_to",
        "plans": "plans",
        "tax_included": "tax_included",
        "tax_percentage": "tax_percentage",
        "tax_type": "tax_type",
        "user_count": "user_count",
    }

    def __init__(
        self,
        currency_id=None,
        discount_percentage=None,
        discount_to=None,
        plans=None,
        tax_included=None,
        tax_percentage=None,
        tax_type=None,
        user_count=None,
        _configuration=None,
    ):  # noqa: E501
        """BillingPricingStruct - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._currency_id = None
        self._discount_percentage = None
        self._discount_to = None
        self._plans = None
        self._tax_included = None
        self._tax_percentage = None
        self._tax_type = None
        self._user_count = None
        self.discriminator = None

        if currency_id is not None:
            self.currency_id = currency_id
        if discount_percentage is not None:
            self.discount_percentage = discount_percentage
        if discount_to is not None:
            self.discount_to = discount_to
        if plans is not None:
            self.plans = plans
        if tax_included is not None:
            self.tax_included = tax_included
        if tax_percentage is not None:
            self.tax_percentage = tax_percentage
        if tax_type is not None:
            self.tax_type = tax_type
        if user_count is not None:
            self.user_count = user_count

    @property
    def currency_id(self):
        """Gets the currency_id of this BillingPricingStruct.  # noqa: E501


        :return: The currency_id of this BillingPricingStruct.  # noqa: E501
        :rtype: int
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this BillingPricingStruct.


        :param currency_id: The currency_id of this BillingPricingStruct.  # noqa: E501
        :type: int
        """

        self._currency_id = currency_id

    @property
    def discount_percentage(self):
        """Gets the discount_percentage of this BillingPricingStruct.  # noqa: E501


        :return: The discount_percentage of this BillingPricingStruct.  # noqa: E501
        :rtype: int
        """
        return self._discount_percentage

    @discount_percentage.setter
    def discount_percentage(self, discount_percentage):
        """Sets the discount_percentage of this BillingPricingStruct.


        :param discount_percentage: The discount_percentage of this BillingPricingStruct.  # noqa: E501
        :type: int
        """

        self._discount_percentage = discount_percentage

    @property
    def discount_to(self):
        """Gets the discount_to of this BillingPricingStruct.  # noqa: E501


        :return: The discount_to of this BillingPricingStruct.  # noqa: E501
        :rtype: str
        """
        return self._discount_to

    @discount_to.setter
    def discount_to(self, discount_to):
        """Sets the discount_to of this BillingPricingStruct.


        :param discount_to: The discount_to of this BillingPricingStruct.  # noqa: E501
        :type: str
        """

        self._discount_to = discount_to

    @property
    def plans(self):
        """Gets the plans of this BillingPricingStruct.  # noqa: E501


        :return: The plans of this BillingPricingStruct.  # noqa: E501
        :rtype: list[BillingFancyPlan]
        """
        return self._plans

    @plans.setter
    def plans(self, plans):
        """Sets the plans of this BillingPricingStruct.


        :param plans: The plans of this BillingPricingStruct.  # noqa: E501
        :type: list[BillingFancyPlan]
        """

        self._plans = plans

    @property
    def tax_included(self):
        """Gets the tax_included of this BillingPricingStruct.  # noqa: E501


        :return: The tax_included of this BillingPricingStruct.  # noqa: E501
        :rtype: bool
        """
        return self._tax_included

    @tax_included.setter
    def tax_included(self, tax_included):
        """Sets the tax_included of this BillingPricingStruct.


        :param tax_included: The tax_included of this BillingPricingStruct.  # noqa: E501
        :type: bool
        """

        self._tax_included = tax_included

    @property
    def tax_percentage(self):
        """Gets the tax_percentage of this BillingPricingStruct.  # noqa: E501


        :return: The tax_percentage of this BillingPricingStruct.  # noqa: E501
        :rtype: float
        """
        return self._tax_percentage

    @tax_percentage.setter
    def tax_percentage(self, tax_percentage):
        """Sets the tax_percentage of this BillingPricingStruct.


        :param tax_percentage: The tax_percentage of this BillingPricingStruct.  # noqa: E501
        :type: float
        """

        self._tax_percentage = tax_percentage

    @property
    def tax_type(self):
        """Gets the tax_type of this BillingPricingStruct.  # noqa: E501


        :return: The tax_type of this BillingPricingStruct.  # noqa: E501
        :rtype: str
        """
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        """Sets the tax_type of this BillingPricingStruct.


        :param tax_type: The tax_type of this BillingPricingStruct.  # noqa: E501
        :type: str
        """

        self._tax_type = tax_type

    @property
    def user_count(self):
        """Gets the user_count of this BillingPricingStruct.  # noqa: E501


        :return: The user_count of this BillingPricingStruct.  # noqa: E501
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this BillingPricingStruct.


        :param user_count: The user_count of this BillingPricingStruct.  # noqa: E501
        :type: int
        """

        self._user_count = user_count

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
        if issubclass(BillingPricingStruct, dict):
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
        if not isinstance(other, BillingPricingStruct):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BillingPricingStruct):
            return True

        return self.to_dict() != other.to_dict()