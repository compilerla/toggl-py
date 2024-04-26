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


class CustomerPaymentMethodUSBankAccount:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"bank_name": "str", "blocked": "bool", "blocked_reason": "str", "last4": "str"}

    attribute_map = {"bank_name": "bank_name", "blocked": "blocked", "blocked_reason": "blocked_reason", "last4": "last4"}

    def __init__(self, bank_name=None, blocked=None, blocked_reason=None, last4=None, _configuration=None):  # noqa: E501
        """CustomerPaymentMethodUSBankAccount - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bank_name = None
        self._blocked = None
        self._blocked_reason = None
        self._last4 = None
        self.discriminator = None

        if bank_name is not None:
            self.bank_name = bank_name
        if blocked is not None:
            self.blocked = blocked
        if blocked_reason is not None:
            self.blocked_reason = blocked_reason
        if last4 is not None:
            self.last4 = last4

    @property
    def bank_name(self):
        """Gets the bank_name of this CustomerPaymentMethodUSBankAccount.  # noqa: E501


        :return: The bank_name of this CustomerPaymentMethodUSBankAccount.  # noqa: E501
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        """Sets the bank_name of this CustomerPaymentMethodUSBankAccount.


        :param bank_name: The bank_name of this CustomerPaymentMethodUSBankAccount.  # noqa: E501
        :type: str
        """

        self._bank_name = bank_name

    @property
    def blocked(self):
        """Gets the blocked of this CustomerPaymentMethodUSBankAccount.  # noqa: E501


        :return: The blocked of this CustomerPaymentMethodUSBankAccount.  # noqa: E501
        :rtype: bool
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """Sets the blocked of this CustomerPaymentMethodUSBankAccount.


        :param blocked: The blocked of this CustomerPaymentMethodUSBankAccount.  # noqa: E501
        :type: bool
        """

        self._blocked = blocked

    @property
    def blocked_reason(self):
        """Gets the blocked_reason of this CustomerPaymentMethodUSBankAccount.  # noqa: E501


        :return: The blocked_reason of this CustomerPaymentMethodUSBankAccount.  # noqa: E501
        :rtype: str
        """
        return self._blocked_reason

    @blocked_reason.setter
    def blocked_reason(self, blocked_reason):
        """Sets the blocked_reason of this CustomerPaymentMethodUSBankAccount.


        :param blocked_reason: The blocked_reason of this CustomerPaymentMethodUSBankAccount.  # noqa: E501
        :type: str
        """

        self._blocked_reason = blocked_reason

    @property
    def last4(self):
        """Gets the last4 of this CustomerPaymentMethodUSBankAccount.  # noqa: E501


        :return: The last4 of this CustomerPaymentMethodUSBankAccount.  # noqa: E501
        :rtype: str
        """
        return self._last4

    @last4.setter
    def last4(self, last4):
        """Sets the last4 of this CustomerPaymentMethodUSBankAccount.


        :param last4: The last4 of this CustomerPaymentMethodUSBankAccount.  # noqa: E501
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
        if issubclass(CustomerPaymentMethodUSBankAccount, dict):
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
        if not isinstance(other, CustomerPaymentMethodUSBankAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerPaymentMethodUSBankAccount):
            return True

        return self.to_dict() != other.to_dict()
