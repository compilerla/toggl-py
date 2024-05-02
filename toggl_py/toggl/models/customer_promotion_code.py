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


class CustomerPromotionCode:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {"active": "bool", "code": "str", "expires_at": "str", "id": "str"}

    attribute_map = {"active": "active", "code": "code", "expires_at": "expires_at", "id": "id"}

    def __init__(
        self,
        active: bool = None,
        code: str = None,
        expires_at: str = None,
        id: str = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        CustomerPromotionCode - a model defined in Swagger

        Parameters:
          active (bool): Optional
          code (str): Optional
          expires_at (str): Optional
          id (str): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active = None
        self._code = None
        self._expires_at = None
        self._id = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if code is not None:
            self.code = code
        if expires_at is not None:
            self.expires_at = expires_at
        if id is not None:
            self.id = id

    @property
    def active(self) -> bool:
        """Gets the active of this CustomerPromotionCode.  # noqa: E501


        :return: The active of this CustomerPromotionCode.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active: bool):
        """Sets the active of this CustomerPromotionCode.


        :param active: The active of this CustomerPromotionCode.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def code(self) -> str:
        """Gets the code of this CustomerPromotionCode.  # noqa: E501


        :return: The code of this CustomerPromotionCode.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this CustomerPromotionCode.


        :param code: The code of this CustomerPromotionCode.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def expires_at(self) -> str:
        """Gets the expires_at of this CustomerPromotionCode.  # noqa: E501


        :return: The expires_at of this CustomerPromotionCode.  # noqa: E501
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at: str):
        """Sets the expires_at of this CustomerPromotionCode.


        :param expires_at: The expires_at of this CustomerPromotionCode.  # noqa: E501
        :type: str
        """

        self._expires_at = expires_at

    @property
    def id(self) -> str:
        """Gets the id of this CustomerPromotionCode.  # noqa: E501


        :return: The id of this CustomerPromotionCode.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this CustomerPromotionCode.


        :param id: The id of this CustomerPromotionCode.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(CustomerPromotionCode, dict):
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
        if not isinstance(other, CustomerPromotionCode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerPromotionCode):
            return True

        return self.to_dict() != other.to_dict()
