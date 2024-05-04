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
    from toggl.models.billing_fancy_pricing_plan import BillingFancyPricingPlan  # noqa: F401


class BillingFancyPlan:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {"name": "str", "plan_id": "int", "pricing_plans": "list[BillingFancyPricingPlan]"}

    attribute_map = {"name": "name", "plan_id": "plan_id", "pricing_plans": "pricing_plans"}

    def __init__(
        self,
        name: str = None,
        plan_id: int = None,
        pricing_plans: list[BillingFancyPricingPlan] = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        BillingFancyPlan - a model defined in Swagger

        Parameters:
          name (str): Optional
          plan_id (int): Optional
          pricing_plans (list[BillingFancyPricingPlan]): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._plan_id = None
        self._pricing_plans = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if plan_id is not None:
            self.plan_id = plan_id
        if pricing_plans is not None:
            self.pricing_plans = pricing_plans

    @property
    def name(self) -> str:
        """Gets the name of this BillingFancyPlan.  # noqa: E501


        :return: The name of this BillingFancyPlan.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this BillingFancyPlan.


        :param name: The name of this BillingFancyPlan.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def plan_id(self) -> int:
        """Gets the plan_id of this BillingFancyPlan.  # noqa: E501


        :return: The plan_id of this BillingFancyPlan.  # noqa: E501
        :rtype: int
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id: int):
        """Sets the plan_id of this BillingFancyPlan.


        :param plan_id: The plan_id of this BillingFancyPlan.  # noqa: E501
        :type: int
        """

        self._plan_id = plan_id

    @property
    def pricing_plans(self) -> list[BillingFancyPricingPlan]:
        """Gets the pricing_plans of this BillingFancyPlan.  # noqa: E501


        :return: The pricing_plans of this BillingFancyPlan.  # noqa: E501
        :rtype: list[BillingFancyPricingPlan]
        """
        return self._pricing_plans

    @pricing_plans.setter
    def pricing_plans(self, pricing_plans: list[BillingFancyPricingPlan]):
        """Sets the pricing_plans of this BillingFancyPlan.


        :param pricing_plans: The pricing_plans of this BillingFancyPlan.  # noqa: E501
        :type: list[BillingFancyPricingPlan]
        """

        self._pricing_plans = pricing_plans

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
        if issubclass(BillingFancyPlan, dict):
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
        if not isinstance(other, BillingFancyPlan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BillingFancyPlan):
            return True

        return self.to_dict() != other.to_dict()
