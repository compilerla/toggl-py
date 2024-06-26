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


class ModelsPricingPlan:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "amount_in_cents": "int",
        "currency": "str",
        "period": "int",
        "plan": "ModelsPlan",
        "plan_id": "int",
        "price_point_handle": "str",
        "pricing_plan_id": "int",
    }

    attribute_map = {
        "amount_in_cents": "amount_in_cents",
        "currency": "currency",
        "period": "period",
        "plan": "plan",
        "plan_id": "plan_id",
        "price_point_handle": "price_point_handle",
        "pricing_plan_id": "pricing_plan_id",
    }

    def __init__(
        self,
        amount_in_cents=None,
        currency=None,
        period=None,
        plan=None,
        plan_id=None,
        price_point_handle=None,
        pricing_plan_id=None,
        _configuration=None,
    ):  # noqa: E501
        """ModelsPricingPlan - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._amount_in_cents = None
        self._currency = None
        self._period = None
        self._plan = None
        self._plan_id = None
        self._price_point_handle = None
        self._pricing_plan_id = None
        self.discriminator = None

        if amount_in_cents is not None:
            self.amount_in_cents = amount_in_cents
        if currency is not None:
            self.currency = currency
        if period is not None:
            self.period = period
        if plan is not None:
            self.plan = plan
        if plan_id is not None:
            self.plan_id = plan_id
        if price_point_handle is not None:
            self.price_point_handle = price_point_handle
        if pricing_plan_id is not None:
            self.pricing_plan_id = pricing_plan_id

    @property
    def amount_in_cents(self):
        """Gets the amount_in_cents of this ModelsPricingPlan.  # noqa: E501


        :return: The amount_in_cents of this ModelsPricingPlan.  # noqa: E501
        :rtype: int
        """
        return self._amount_in_cents

    @amount_in_cents.setter
    def amount_in_cents(self, amount_in_cents):
        """Sets the amount_in_cents of this ModelsPricingPlan.


        :param amount_in_cents: The amount_in_cents of this ModelsPricingPlan.  # noqa: E501
        :type: int
        """

        self._amount_in_cents = amount_in_cents

    @property
    def currency(self):
        """Gets the currency of this ModelsPricingPlan.  # noqa: E501


        :return: The currency of this ModelsPricingPlan.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ModelsPricingPlan.


        :param currency: The currency of this ModelsPricingPlan.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def period(self):
        """Gets the period of this ModelsPricingPlan.  # noqa: E501


        :return: The period of this ModelsPricingPlan.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ModelsPricingPlan.


        :param period: The period of this ModelsPricingPlan.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def plan(self):
        """Gets the plan of this ModelsPricingPlan.  # noqa: E501


        :return: The plan of this ModelsPricingPlan.  # noqa: E501
        :rtype: ModelsPlan
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this ModelsPricingPlan.


        :param plan: The plan of this ModelsPricingPlan.  # noqa: E501
        :type: ModelsPlan
        """

        self._plan = plan

    @property
    def plan_id(self):
        """Gets the plan_id of this ModelsPricingPlan.  # noqa: E501


        :return: The plan_id of this ModelsPricingPlan.  # noqa: E501
        :rtype: int
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this ModelsPricingPlan.


        :param plan_id: The plan_id of this ModelsPricingPlan.  # noqa: E501
        :type: int
        """

        self._plan_id = plan_id

    @property
    def price_point_handle(self):
        """Gets the price_point_handle of this ModelsPricingPlan.  # noqa: E501


        :return: The price_point_handle of this ModelsPricingPlan.  # noqa: E501
        :rtype: str
        """
        return self._price_point_handle

    @price_point_handle.setter
    def price_point_handle(self, price_point_handle):
        """Sets the price_point_handle of this ModelsPricingPlan.


        :param price_point_handle: The price_point_handle of this ModelsPricingPlan.  # noqa: E501
        :type: str
        """

        self._price_point_handle = price_point_handle

    @property
    def pricing_plan_id(self):
        """Gets the pricing_plan_id of this ModelsPricingPlan.  # noqa: E501


        :return: The pricing_plan_id of this ModelsPricingPlan.  # noqa: E501
        :rtype: int
        """
        return self._pricing_plan_id

    @pricing_plan_id.setter
    def pricing_plan_id(self, pricing_plan_id):
        """Sets the pricing_plan_id of this ModelsPricingPlan.


        :param pricing_plan_id: The pricing_plan_id of this ModelsPricingPlan.  # noqa: E501
        :type: int
        """

        self._pricing_plan_id = pricing_plan_id

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
        if issubclass(ModelsPricingPlan, dict):
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
        if not isinstance(other, ModelsPricingPlan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsPricingPlan):
            return True

        return self.to_dict() != other.to_dict()
