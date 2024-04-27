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


class CustomerPaymentMethod:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "card": "CustomerPaymentMethodCard",
        "sepa_debit": "CustomerPaymentMethodSEPADebit",
        "type": "str",
        "us_bank_account": "CustomerPaymentMethodUSBankAccount",
    }

    attribute_map = {"card": "card", "sepa_debit": "sepa_debit", "type": "type", "us_bank_account": "us_bank_account"}

    def __init__(self, card=None, sepa_debit=None, type=None, us_bank_account=None, _configuration=None):  # noqa: E501
        """CustomerPaymentMethod - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._card = None
        self._sepa_debit = None
        self._type = None
        self._us_bank_account = None
        self.discriminator = None

        if card is not None:
            self.card = card
        if sepa_debit is not None:
            self.sepa_debit = sepa_debit
        if type is not None:
            self.type = type
        if us_bank_account is not None:
            self.us_bank_account = us_bank_account

    @property
    def card(self):
        """Gets the card of this CustomerPaymentMethod.  # noqa: E501


        :return: The card of this CustomerPaymentMethod.  # noqa: E501
        :rtype: CustomerPaymentMethodCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """Sets the card of this CustomerPaymentMethod.


        :param card: The card of this CustomerPaymentMethod.  # noqa: E501
        :type: CustomerPaymentMethodCard
        """

        self._card = card

    @property
    def sepa_debit(self):
        """Gets the sepa_debit of this CustomerPaymentMethod.  # noqa: E501


        :return: The sepa_debit of this CustomerPaymentMethod.  # noqa: E501
        :rtype: CustomerPaymentMethodSEPADebit
        """
        return self._sepa_debit

    @sepa_debit.setter
    def sepa_debit(self, sepa_debit):
        """Sets the sepa_debit of this CustomerPaymentMethod.


        :param sepa_debit: The sepa_debit of this CustomerPaymentMethod.  # noqa: E501
        :type: CustomerPaymentMethodSEPADebit
        """

        self._sepa_debit = sepa_debit

    @property
    def type(self):
        """Gets the type of this CustomerPaymentMethod.  # noqa: E501


        :return: The type of this CustomerPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CustomerPaymentMethod.


        :param type: The type of this CustomerPaymentMethod.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def us_bank_account(self):
        """Gets the us_bank_account of this CustomerPaymentMethod.  # noqa: E501


        :return: The us_bank_account of this CustomerPaymentMethod.  # noqa: E501
        :rtype: CustomerPaymentMethodUSBankAccount
        """
        return self._us_bank_account

    @us_bank_account.setter
    def us_bank_account(self, us_bank_account):
        """Sets the us_bank_account of this CustomerPaymentMethod.


        :param us_bank_account: The us_bank_account of this CustomerPaymentMethod.  # noqa: E501
        :type: CustomerPaymentMethodUSBankAccount
        """

        self._us_bank_account = us_bank_account

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
        if issubclass(CustomerPaymentMethod, dict):
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
        if not isinstance(other, CustomerPaymentMethod):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerPaymentMethod):
            return True

        return self.to_dict() != other.to_dict()
