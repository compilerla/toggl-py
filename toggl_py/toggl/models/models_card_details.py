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


class ModelsCardDetails:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "added_at": "str",
        "card_number": "str",
        "card_type": "str",
        "creator_id": "int",
        "creator_name": "str",
        "expiry_date": "str",
        "holder_name": "str",
    }

    attribute_map = {
        "added_at": "added_at",
        "card_number": "card_number",
        "card_type": "card_type",
        "creator_id": "creator_id",
        "creator_name": "creator_name",
        "expiry_date": "expiry_date",
        "holder_name": "holder_name",
    }

    def __init__(
        self,
        added_at: str = None,
        card_number: str = None,
        card_type: str = None,
        creator_id: int = None,
        creator_name: str = None,
        expiry_date: str = None,
        holder_name: str = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        ModelsCardDetails - a model defined in Swagger

        Parameters:
          added_at (str): Optional
          card_number (str): Optional
          card_type (str): Optional
          creator_id (int): Optional
          creator_name (str): Optional
          expiry_date (str): Optional
          holder_name (str): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._added_at = None
        self._card_number = None
        self._card_type = None
        self._creator_id = None
        self._creator_name = None
        self._expiry_date = None
        self._holder_name = None
        self.discriminator = None

        if added_at is not None:
            self.added_at = added_at
        if card_number is not None:
            self.card_number = card_number
        if card_type is not None:
            self.card_type = card_type
        if creator_id is not None:
            self.creator_id = creator_id
        if creator_name is not None:
            self.creator_name = creator_name
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if holder_name is not None:
            self.holder_name = holder_name

    @property
    def added_at(self) -> str:
        """Gets the added_at of this ModelsCardDetails.  # noqa: E501


        :return: The added_at of this ModelsCardDetails.  # noqa: E501
        :rtype: str
        """
        return self._added_at

    @added_at.setter
    def added_at(self, added_at: str):
        """Sets the added_at of this ModelsCardDetails.


        :param added_at: The added_at of this ModelsCardDetails.  # noqa: E501
        :type: str
        """

        self._added_at = added_at

    @property
    def card_number(self) -> str:
        """Gets the card_number of this ModelsCardDetails.  # noqa: E501


        :return: The card_number of this ModelsCardDetails.  # noqa: E501
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number: str):
        """Sets the card_number of this ModelsCardDetails.


        :param card_number: The card_number of this ModelsCardDetails.  # noqa: E501
        :type: str
        """

        self._card_number = card_number

    @property
    def card_type(self) -> str:
        """Gets the card_type of this ModelsCardDetails.  # noqa: E501


        :return: The card_type of this ModelsCardDetails.  # noqa: E501
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type: str):
        """Sets the card_type of this ModelsCardDetails.


        :param card_type: The card_type of this ModelsCardDetails.  # noqa: E501
        :type: str
        """

        self._card_type = card_type

    @property
    def creator_id(self) -> int:
        """Gets the creator_id of this ModelsCardDetails.  # noqa: E501


        :return: The creator_id of this ModelsCardDetails.  # noqa: E501
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id: int):
        """Sets the creator_id of this ModelsCardDetails.


        :param creator_id: The creator_id of this ModelsCardDetails.  # noqa: E501
        :type: int
        """

        self._creator_id = creator_id

    @property
    def creator_name(self) -> str:
        """Gets the creator_name of this ModelsCardDetails.  # noqa: E501


        :return: The creator_name of this ModelsCardDetails.  # noqa: E501
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name: str):
        """Sets the creator_name of this ModelsCardDetails.


        :param creator_name: The creator_name of this ModelsCardDetails.  # noqa: E501
        :type: str
        """

        self._creator_name = creator_name

    @property
    def expiry_date(self) -> str:
        """Gets the expiry_date of this ModelsCardDetails.  # noqa: E501


        :return: The expiry_date of this ModelsCardDetails.  # noqa: E501
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date: str):
        """Sets the expiry_date of this ModelsCardDetails.


        :param expiry_date: The expiry_date of this ModelsCardDetails.  # noqa: E501
        :type: str
        """

        self._expiry_date = expiry_date

    @property
    def holder_name(self) -> str:
        """Gets the holder_name of this ModelsCardDetails.  # noqa: E501


        :return: The holder_name of this ModelsCardDetails.  # noqa: E501
        :rtype: str
        """
        return self._holder_name

    @holder_name.setter
    def holder_name(self, holder_name: str):
        """Sets the holder_name of this ModelsCardDetails.


        :param holder_name: The holder_name of this ModelsCardDetails.  # noqa: E501
        :type: str
        """

        self._holder_name = holder_name

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
        if issubclass(ModelsCardDetails, dict):
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
        if not isinstance(other, ModelsCardDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsCardDetails):
            return True

        return self.to_dict() != other.to_dict()
