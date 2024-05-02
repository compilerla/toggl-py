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
from toggl.models.models_card_details import ModelsCardDetails  # noqa: F401
from toggl.models.models_contact_detail import ModelsContactDetail  # noqa: F401
from toggl.models.models_payment_detail import ModelsPaymentDetail  # noqa: F401
from toggl.models.models_period import ModelsPeriod  # noqa: F401


class ModelsSubscription:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "auto_renew": "bool",
        "card_details": "ModelsCardDetails",
        "company_id": "int",
        "contact_detail": "ModelsContactDetail",
        "created_at": "datetime",
        "currency": "str",
        "customer_id": "int",
        "deleted_at": "datetime",
        "last_pricing_plan_id": "int",
        "organization_id": "int",
        "payment_details": "ModelsPaymentDetail",
        "pricing_plan_id": "int",
        "renewal_at": "datetime",
        "subscription_id": "int",
        "subscription_period": "ModelsPeriod",
        "workspace_id": "int",
    }

    attribute_map = {
        "auto_renew": "auto_renew",
        "card_details": "card_details",
        "company_id": "company_id",
        "contact_detail": "contact_detail",
        "created_at": "created_at",
        "currency": "currency",
        "customer_id": "customer_id",
        "deleted_at": "deleted_at",
        "last_pricing_plan_id": "last_pricing_plan_id",
        "organization_id": "organization_id",
        "payment_details": "payment_details",
        "pricing_plan_id": "pricing_plan_id",
        "renewal_at": "renewal_at",
        "subscription_id": "subscription_id",
        "subscription_period": "subscription_period",
        "workspace_id": "workspace_id",
    }

    def __init__(
        self,
        auto_renew: bool = None,
        card_details: ModelsCardDetails = None,
        company_id: int = None,
        contact_detail: ModelsContactDetail = None,
        created_at: datetime = None,
        currency: str = None,
        customer_id: int = None,
        deleted_at: datetime = None,
        last_pricing_plan_id: int = None,
        organization_id: int = None,
        payment_details: ModelsPaymentDetail = None,
        pricing_plan_id: int = None,
        renewal_at: datetime = None,
        subscription_id: int = None,
        subscription_period: ModelsPeriod = None,
        workspace_id: int = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        ModelsSubscription - a model defined in Swagger

        Parameters:
          auto_renew (bool): Optional
          card_details (ModelsCardDetails): Optional
          company_id (int): Optional
          contact_detail (ModelsContactDetail): Optional
          created_at (datetime): Optional
          currency (str): Optional
          customer_id (int): Optional
          deleted_at (datetime): Optional
          last_pricing_plan_id (int): Optional
          organization_id (int): Optional
          payment_details (ModelsPaymentDetail): Optional
          pricing_plan_id (int): Optional
          renewal_at (datetime): Optional
          subscription_id (int): Optional
          subscription_period (ModelsPeriod): Optional
          workspace_id (int): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_renew = None
        self._card_details = None
        self._company_id = None
        self._contact_detail = None
        self._created_at = None
        self._currency = None
        self._customer_id = None
        self._deleted_at = None
        self._last_pricing_plan_id = None
        self._organization_id = None
        self._payment_details = None
        self._pricing_plan_id = None
        self._renewal_at = None
        self._subscription_id = None
        self._subscription_period = None
        self._workspace_id = None
        self.discriminator = None

        if auto_renew is not None:
            self.auto_renew = auto_renew
        if card_details is not None:
            self.card_details = card_details
        if company_id is not None:
            self.company_id = company_id
        if contact_detail is not None:
            self.contact_detail = contact_detail
        if created_at is not None:
            self.created_at = created_at
        if currency is not None:
            self.currency = currency
        if customer_id is not None:
            self.customer_id = customer_id
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if last_pricing_plan_id is not None:
            self.last_pricing_plan_id = last_pricing_plan_id
        if organization_id is not None:
            self.organization_id = organization_id
        if payment_details is not None:
            self.payment_details = payment_details
        if pricing_plan_id is not None:
            self.pricing_plan_id = pricing_plan_id
        if renewal_at is not None:
            self.renewal_at = renewal_at
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if subscription_period is not None:
            self.subscription_period = subscription_period
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def auto_renew(self) -> bool:
        """Gets the auto_renew of this ModelsSubscription.  # noqa: E501


        :return: The auto_renew of this ModelsSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew: bool):
        """Sets the auto_renew of this ModelsSubscription.


        :param auto_renew: The auto_renew of this ModelsSubscription.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def card_details(self) -> ModelsCardDetails:
        """Gets the card_details of this ModelsSubscription.  # noqa: E501


        :return: The card_details of this ModelsSubscription.  # noqa: E501
        :rtype: ModelsCardDetails
        """
        return self._card_details

    @card_details.setter
    def card_details(self, card_details: ModelsCardDetails):
        """Sets the card_details of this ModelsSubscription.


        :param card_details: The card_details of this ModelsSubscription.  # noqa: E501
        :type: ModelsCardDetails
        """

        self._card_details = card_details

    @property
    def company_id(self) -> int:
        """Gets the company_id of this ModelsSubscription.  # noqa: E501


        :return: The company_id of this ModelsSubscription.  # noqa: E501
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id: int):
        """Sets the company_id of this ModelsSubscription.


        :param company_id: The company_id of this ModelsSubscription.  # noqa: E501
        :type: int
        """

        self._company_id = company_id

    @property
    def contact_detail(self) -> ModelsContactDetail:
        """Gets the contact_detail of this ModelsSubscription.  # noqa: E501


        :return: The contact_detail of this ModelsSubscription.  # noqa: E501
        :rtype: ModelsContactDetail
        """
        return self._contact_detail

    @contact_detail.setter
    def contact_detail(self, contact_detail: ModelsContactDetail):
        """Sets the contact_detail of this ModelsSubscription.


        :param contact_detail: The contact_detail of this ModelsSubscription.  # noqa: E501
        :type: ModelsContactDetail
        """

        self._contact_detail = contact_detail

    @property
    def created_at(self) -> datetime:
        """Gets the created_at of this ModelsSubscription.  # noqa: E501


        :return: The created_at of this ModelsSubscription.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: datetime):
        """Sets the created_at of this ModelsSubscription.


        :param created_at: The created_at of this ModelsSubscription.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def currency(self) -> str:
        """Gets the currency of this ModelsSubscription.  # noqa: E501


        :return: The currency of this ModelsSubscription.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency: str):
        """Sets the currency of this ModelsSubscription.


        :param currency: The currency of this ModelsSubscription.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def customer_id(self) -> int:
        """Gets the customer_id of this ModelsSubscription.  # noqa: E501


        :return: The customer_id of this ModelsSubscription.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id: int):
        """Sets the customer_id of this ModelsSubscription.


        :param customer_id: The customer_id of this ModelsSubscription.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

    @property
    def deleted_at(self) -> datetime:
        """Gets the deleted_at of this ModelsSubscription.  # noqa: E501


        :return: The deleted_at of this ModelsSubscription.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at: datetime):
        """Sets the deleted_at of this ModelsSubscription.


        :param deleted_at: The deleted_at of this ModelsSubscription.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def last_pricing_plan_id(self) -> int:
        """Gets the last_pricing_plan_id of this ModelsSubscription.  # noqa: E501


        :return: The last_pricing_plan_id of this ModelsSubscription.  # noqa: E501
        :rtype: int
        """
        return self._last_pricing_plan_id

    @last_pricing_plan_id.setter
    def last_pricing_plan_id(self, last_pricing_plan_id: int):
        """Sets the last_pricing_plan_id of this ModelsSubscription.


        :param last_pricing_plan_id: The last_pricing_plan_id of this ModelsSubscription.  # noqa: E501
        :type: int
        """

        self._last_pricing_plan_id = last_pricing_plan_id

    @property
    def organization_id(self) -> int:
        """Gets the organization_id of this ModelsSubscription.  # noqa: E501


        :return: The organization_id of this ModelsSubscription.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id: int):
        """Sets the organization_id of this ModelsSubscription.


        :param organization_id: The organization_id of this ModelsSubscription.  # noqa: E501
        :type: int
        """

        self._organization_id = organization_id

    @property
    def payment_details(self) -> ModelsPaymentDetail:
        """Gets the payment_details of this ModelsSubscription.  # noqa: E501


        :return: The payment_details of this ModelsSubscription.  # noqa: E501
        :rtype: ModelsPaymentDetail
        """
        return self._payment_details

    @payment_details.setter
    def payment_details(self, payment_details: ModelsPaymentDetail):
        """Sets the payment_details of this ModelsSubscription.


        :param payment_details: The payment_details of this ModelsSubscription.  # noqa: E501
        :type: ModelsPaymentDetail
        """

        self._payment_details = payment_details

    @property
    def pricing_plan_id(self) -> int:
        """Gets the pricing_plan_id of this ModelsSubscription.  # noqa: E501


        :return: The pricing_plan_id of this ModelsSubscription.  # noqa: E501
        :rtype: int
        """
        return self._pricing_plan_id

    @pricing_plan_id.setter
    def pricing_plan_id(self, pricing_plan_id: int):
        """Sets the pricing_plan_id of this ModelsSubscription.


        :param pricing_plan_id: The pricing_plan_id of this ModelsSubscription.  # noqa: E501
        :type: int
        """

        self._pricing_plan_id = pricing_plan_id

    @property
    def renewal_at(self) -> datetime:
        """Gets the renewal_at of this ModelsSubscription.  # noqa: E501


        :return: The renewal_at of this ModelsSubscription.  # noqa: E501
        :rtype: datetime
        """
        return self._renewal_at

    @renewal_at.setter
    def renewal_at(self, renewal_at: datetime):
        """Sets the renewal_at of this ModelsSubscription.


        :param renewal_at: The renewal_at of this ModelsSubscription.  # noqa: E501
        :type: datetime
        """

        self._renewal_at = renewal_at

    @property
    def subscription_id(self) -> int:
        """Gets the subscription_id of this ModelsSubscription.  # noqa: E501


        :return: The subscription_id of this ModelsSubscription.  # noqa: E501
        :rtype: int
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id: int):
        """Sets the subscription_id of this ModelsSubscription.


        :param subscription_id: The subscription_id of this ModelsSubscription.  # noqa: E501
        :type: int
        """

        self._subscription_id = subscription_id

    @property
    def subscription_period(self) -> ModelsPeriod:
        """Gets the subscription_period of this ModelsSubscription.  # noqa: E501


        :return: The subscription_period of this ModelsSubscription.  # noqa: E501
        :rtype: ModelsPeriod
        """
        return self._subscription_period

    @subscription_period.setter
    def subscription_period(self, subscription_period: ModelsPeriod):
        """Sets the subscription_period of this ModelsSubscription.


        :param subscription_period: The subscription_period of this ModelsSubscription.  # noqa: E501
        :type: ModelsPeriod
        """

        self._subscription_period = subscription_period

    @property
    def workspace_id(self) -> int:
        """Gets the workspace_id of this ModelsSubscription.  # noqa: E501


        :return: The workspace_id of this ModelsSubscription.  # noqa: E501
        :rtype: int
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id: int):
        """Sets the workspace_id of this ModelsSubscription.


        :param workspace_id: The workspace_id of this ModelsSubscription.  # noqa: E501
        :type: int
        """

        self._workspace_id = workspace_id

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
        if issubclass(ModelsSubscription, dict):
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
        if not isinstance(other, ModelsSubscription):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsSubscription):
            return True

        return self.to_dict() != other.to_dict()
