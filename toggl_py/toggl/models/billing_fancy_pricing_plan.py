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


class BillingFancyPricingPlan:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "actual_price_in_usd_cents": "int",
        "campaign": "ModelsCampaign",
        "list_price_in_usd_cents": "int",
        "name": "str",
        "period": "int",
        "price_point_handle": "str",
        "prices_month": "BillingPricesStruct",
        "prices_period": "BillingPricesStruct",
        "pricing_plan_id": "int",
    }

    attribute_map = {
        "actual_price_in_usd_cents": "actual_price_in_usd_cents",
        "campaign": "campaign",
        "list_price_in_usd_cents": "list_price_in_usd_cents",
        "name": "name",
        "period": "period",
        "price_point_handle": "price_point_handle",
        "prices_month": "prices_month",
        "prices_period": "prices_period",
        "pricing_plan_id": "pricing_plan_id",
    }

    def __init__(
        self,
        actual_price_in_usd_cents=None,
        campaign=None,
        list_price_in_usd_cents=None,
        name=None,
        period=None,
        price_point_handle=None,
        prices_month=None,
        prices_period=None,
        pricing_plan_id=None,
        _configuration=None,
    ):  # noqa: E501
        """BillingFancyPricingPlan - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._actual_price_in_usd_cents = None
        self._campaign = None
        self._list_price_in_usd_cents = None
        self._name = None
        self._period = None
        self._price_point_handle = None
        self._prices_month = None
        self._prices_period = None
        self._pricing_plan_id = None
        self.discriminator = None

        if actual_price_in_usd_cents is not None:
            self.actual_price_in_usd_cents = actual_price_in_usd_cents
        if campaign is not None:
            self.campaign = campaign
        if list_price_in_usd_cents is not None:
            self.list_price_in_usd_cents = list_price_in_usd_cents
        if name is not None:
            self.name = name
        if period is not None:
            self.period = period
        if price_point_handle is not None:
            self.price_point_handle = price_point_handle
        if prices_month is not None:
            self.prices_month = prices_month
        if prices_period is not None:
            self.prices_period = prices_period
        if pricing_plan_id is not None:
            self.pricing_plan_id = pricing_plan_id

    @property
    def actual_price_in_usd_cents(self):
        """Gets the actual_price_in_usd_cents of this BillingFancyPricingPlan.  # noqa: E501


        :return: The actual_price_in_usd_cents of this BillingFancyPricingPlan.  # noqa: E501
        :rtype: int
        """
        return self._actual_price_in_usd_cents

    @actual_price_in_usd_cents.setter
    def actual_price_in_usd_cents(self, actual_price_in_usd_cents):
        """Sets the actual_price_in_usd_cents of this BillingFancyPricingPlan.


        :param actual_price_in_usd_cents: The actual_price_in_usd_cents of this BillingFancyPricingPlan.  # noqa: E501
        :type: int
        """

        self._actual_price_in_usd_cents = actual_price_in_usd_cents

    @property
    def campaign(self):
        """Gets the campaign of this BillingFancyPricingPlan.  # noqa: E501


        :return: The campaign of this BillingFancyPricingPlan.  # noqa: E501
        :rtype: ModelsCampaign
        """
        return self._campaign

    @campaign.setter
    def campaign(self, campaign):
        """Sets the campaign of this BillingFancyPricingPlan.


        :param campaign: The campaign of this BillingFancyPricingPlan.  # noqa: E501
        :type: ModelsCampaign
        """

        self._campaign = campaign

    @property
    def list_price_in_usd_cents(self):
        """Gets the list_price_in_usd_cents of this BillingFancyPricingPlan.  # noqa: E501


        :return: The list_price_in_usd_cents of this BillingFancyPricingPlan.  # noqa: E501
        :rtype: int
        """
        return self._list_price_in_usd_cents

    @list_price_in_usd_cents.setter
    def list_price_in_usd_cents(self, list_price_in_usd_cents):
        """Sets the list_price_in_usd_cents of this BillingFancyPricingPlan.


        :param list_price_in_usd_cents: The list_price_in_usd_cents of this BillingFancyPricingPlan.  # noqa: E501
        :type: int
        """

        self._list_price_in_usd_cents = list_price_in_usd_cents

    @property
    def name(self):
        """Gets the name of this BillingFancyPricingPlan.  # noqa: E501


        :return: The name of this BillingFancyPricingPlan.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BillingFancyPricingPlan.


        :param name: The name of this BillingFancyPricingPlan.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def period(self):
        """Gets the period of this BillingFancyPricingPlan.  # noqa: E501


        :return: The period of this BillingFancyPricingPlan.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this BillingFancyPricingPlan.


        :param period: The period of this BillingFancyPricingPlan.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def price_point_handle(self):
        """Gets the price_point_handle of this BillingFancyPricingPlan.  # noqa: E501


        :return: The price_point_handle of this BillingFancyPricingPlan.  # noqa: E501
        :rtype: str
        """
        return self._price_point_handle

    @price_point_handle.setter
    def price_point_handle(self, price_point_handle):
        """Sets the price_point_handle of this BillingFancyPricingPlan.


        :param price_point_handle: The price_point_handle of this BillingFancyPricingPlan.  # noqa: E501
        :type: str
        """

        self._price_point_handle = price_point_handle

    @property
    def prices_month(self):
        """Gets the prices_month of this BillingFancyPricingPlan.  # noqa: E501


        :return: The prices_month of this BillingFancyPricingPlan.  # noqa: E501
        :rtype: BillingPricesStruct
        """
        return self._prices_month

    @prices_month.setter
    def prices_month(self, prices_month):
        """Sets the prices_month of this BillingFancyPricingPlan.


        :param prices_month: The prices_month of this BillingFancyPricingPlan.  # noqa: E501
        :type: BillingPricesStruct
        """

        self._prices_month = prices_month

    @property
    def prices_period(self):
        """Gets the prices_period of this BillingFancyPricingPlan.  # noqa: E501


        :return: The prices_period of this BillingFancyPricingPlan.  # noqa: E501
        :rtype: BillingPricesStruct
        """
        return self._prices_period

    @prices_period.setter
    def prices_period(self, prices_period):
        """Sets the prices_period of this BillingFancyPricingPlan.


        :param prices_period: The prices_period of this BillingFancyPricingPlan.  # noqa: E501
        :type: BillingPricesStruct
        """

        self._prices_period = prices_period

    @property
    def pricing_plan_id(self):
        """Gets the pricing_plan_id of this BillingFancyPricingPlan.  # noqa: E501


        :return: The pricing_plan_id of this BillingFancyPricingPlan.  # noqa: E501
        :rtype: int
        """
        return self._pricing_plan_id

    @pricing_plan_id.setter
    def pricing_plan_id(self, pricing_plan_id):
        """Sets the pricing_plan_id of this BillingFancyPricingPlan.


        :param pricing_plan_id: The pricing_plan_id of this BillingFancyPricingPlan.  # noqa: E501
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
        if issubclass(BillingFancyPricingPlan, dict):
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
        if not isinstance(other, BillingFancyPricingPlan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BillingFancyPricingPlan):
            return True

        return self.to_dict() != other.to_dict()