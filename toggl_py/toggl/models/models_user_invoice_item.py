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


class ModelsUserInvoiceItem:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"amount": "float", "description": "str", "item_id": "int", "quantity": "float"}

    attribute_map = {"amount": "amount", "description": "description", "item_id": "item_id", "quantity": "quantity"}

    def __init__(self, amount=None, description=None, item_id=None, quantity=None, _configuration=None):  # noqa: E501
        """ModelsUserInvoiceItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._amount = None
        self._description = None
        self._item_id = None
        self._quantity = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if description is not None:
            self.description = description
        if item_id is not None:
            self.item_id = item_id
        if quantity is not None:
            self.quantity = quantity

    @property
    def amount(self):
        """Gets the amount of this ModelsUserInvoiceItem.  # noqa: E501


        :return: The amount of this ModelsUserInvoiceItem.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ModelsUserInvoiceItem.


        :param amount: The amount of this ModelsUserInvoiceItem.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def description(self):
        """Gets the description of this ModelsUserInvoiceItem.  # noqa: E501


        :return: The description of this ModelsUserInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelsUserInvoiceItem.


        :param description: The description of this ModelsUserInvoiceItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def item_id(self):
        """Gets the item_id of this ModelsUserInvoiceItem.  # noqa: E501


        :return: The item_id of this ModelsUserInvoiceItem.  # noqa: E501
        :rtype: int
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this ModelsUserInvoiceItem.


        :param item_id: The item_id of this ModelsUserInvoiceItem.  # noqa: E501
        :type: int
        """

        self._item_id = item_id

    @property
    def quantity(self):
        """Gets the quantity of this ModelsUserInvoiceItem.  # noqa: E501


        :return: The quantity of this ModelsUserInvoiceItem.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ModelsUserInvoiceItem.


        :param quantity: The quantity of this ModelsUserInvoiceItem.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

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
        if issubclass(ModelsUserInvoiceItem, dict):
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
        if not isinstance(other, ModelsUserInvoiceItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsUserInvoiceItem):
            return True

        return self.to_dict() != other.to_dict()
