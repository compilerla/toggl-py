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
    from toggl.models.models_pricing_plan import ModelsPricingPlan  # noqa: F401


class ModelsPlan:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "id": "int",
        "max_user_count": "int",
        "name": "str",
        "pricing_plans": "list[ModelsPricingPlan]",
        "product_handle": "str",
    }

    attribute_map = {
        "id": "id",
        "max_user_count": "max_user_count",
        "name": "name",
        "pricing_plans": "pricing_plans",
        "product_handle": "product_handle",
    }

    def __init__(
        self,
        id: int = None,
        max_user_count: int = None,
        name: str = None,
        pricing_plans: list[ModelsPricingPlan] = None,
        product_handle: str = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        ModelsPlan - a model defined in Swagger

        Parameters:
          id (int): Optional
          max_user_count (int): Optional
          name (str): Optional
          pricing_plans (list[ModelsPricingPlan]): Optional
          product_handle (str): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._max_user_count = None
        self._name = None
        self._pricing_plans = None
        self._product_handle = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if max_user_count is not None:
            self.max_user_count = max_user_count
        if name is not None:
            self.name = name
        if pricing_plans is not None:
            self.pricing_plans = pricing_plans
        if product_handle is not None:
            self.product_handle = product_handle

    @property
    def id(self) -> int:
        """Gets the id of this ModelsPlan.  # noqa: E501


        :return: The id of this ModelsPlan.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this ModelsPlan.


        :param id: The id of this ModelsPlan.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def max_user_count(self) -> int:
        """Gets the max_user_count of this ModelsPlan.  # noqa: E501


        :return: The max_user_count of this ModelsPlan.  # noqa: E501
        :rtype: int
        """
        return self._max_user_count

    @max_user_count.setter
    def max_user_count(self, max_user_count: int):
        """Sets the max_user_count of this ModelsPlan.


        :param max_user_count: The max_user_count of this ModelsPlan.  # noqa: E501
        :type: int
        """

        self._max_user_count = max_user_count

    @property
    def name(self) -> str:
        """Gets the name of this ModelsPlan.  # noqa: E501


        :return: The name of this ModelsPlan.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ModelsPlan.


        :param name: The name of this ModelsPlan.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pricing_plans(self) -> list[ModelsPricingPlan]:
        """Gets the pricing_plans of this ModelsPlan.  # noqa: E501


        :return: The pricing_plans of this ModelsPlan.  # noqa: E501
        :rtype: list[ModelsPricingPlan]
        """
        return self._pricing_plans

    @pricing_plans.setter
    def pricing_plans(self, pricing_plans: list[ModelsPricingPlan]):
        """Sets the pricing_plans of this ModelsPlan.


        :param pricing_plans: The pricing_plans of this ModelsPlan.  # noqa: E501
        :type: list[ModelsPricingPlan]
        """

        self._pricing_plans = pricing_plans

    @property
    def product_handle(self) -> str:
        """Gets the product_handle of this ModelsPlan.  # noqa: E501


        :return: The product_handle of this ModelsPlan.  # noqa: E501
        :rtype: str
        """
        return self._product_handle

    @product_handle.setter
    def product_handle(self, product_handle: str):
        """Sets the product_handle of this ModelsPlan.


        :param product_handle: The product_handle of this ModelsPlan.  # noqa: E501
        :type: str
        """

        self._product_handle = product_handle

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
        if issubclass(ModelsPlan, dict):
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
        if not isinstance(other, ModelsPlan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsPlan):
            return True

        return self.to_dict() != other.to_dict()
