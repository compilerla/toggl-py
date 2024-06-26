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


class AccountingPurchaseOrderListItem:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"created_at": "str", "due_date": "str", "id": "int"}

    attribute_map = {"created_at": "created_at", "due_date": "due_date", "id": "id"}

    def __init__(self, created_at=None, due_date=None, id=None, _configuration=None):  # noqa: E501
        """AccountingPurchaseOrderListItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_at = None
        self._due_date = None
        self._id = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if due_date is not None:
            self.due_date = due_date
        if id is not None:
            self.id = id

    @property
    def created_at(self):
        """Gets the created_at of this AccountingPurchaseOrderListItem.  # noqa: E501


        :return: The created_at of this AccountingPurchaseOrderListItem.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AccountingPurchaseOrderListItem.


        :param created_at: The created_at of this AccountingPurchaseOrderListItem.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def due_date(self):
        """Gets the due_date of this AccountingPurchaseOrderListItem.  # noqa: E501


        :return: The due_date of this AccountingPurchaseOrderListItem.  # noqa: E501
        :rtype: str
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this AccountingPurchaseOrderListItem.


        :param due_date: The due_date of this AccountingPurchaseOrderListItem.  # noqa: E501
        :type: str
        """

        self._due_date = due_date

    @property
    def id(self):
        """Gets the id of this AccountingPurchaseOrderListItem.  # noqa: E501


        :return: The id of this AccountingPurchaseOrderListItem.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountingPurchaseOrderListItem.


        :param id: The id of this AccountingPurchaseOrderListItem.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(AccountingPurchaseOrderListItem, dict):
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
        if not isinstance(other, AccountingPurchaseOrderListItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountingPurchaseOrderListItem):
            return True

        return self.to_dict() != other.to_dict()
