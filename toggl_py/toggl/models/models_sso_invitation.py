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


class ModelsSSOInvitation:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "accounts_signup_url": "str",
        "code": "str",
        "email": "str",
        "organization_id": "int",
        "sender_email": "str",
        "sender_name": "str",
        "sso": "bool",
        "token": "str",
    }

    attribute_map = {
        "accounts_signup_url": "accounts_signup_url",
        "code": "code",
        "email": "email",
        "organization_id": "organization_id",
        "sender_email": "sender_email",
        "sender_name": "sender_name",
        "sso": "sso",
        "token": "token",
    }

    def __init__(
        self,
        accounts_signup_url: str = None,
        code: str = None,
        email: str = None,
        organization_id: int = None,
        sender_email: str = None,
        sender_name: str = None,
        sso: bool = None,
        token: str = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        ModelsSSOInvitation - a model defined in Swagger

        Parameters:
          accounts_signup_url (str): Optional
          code (str): Optional
          email (str): Optional
          organization_id (int): Optional
          sender_email (str): Optional
          sender_name (str): Optional
          sso (bool): Optional
          token (str): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._accounts_signup_url = None
        self._code = None
        self._email = None
        self._organization_id = None
        self._sender_email = None
        self._sender_name = None
        self._sso = None
        self._token = None
        self.discriminator = None

        if accounts_signup_url is not None:
            self.accounts_signup_url = accounts_signup_url
        if code is not None:
            self.code = code
        if email is not None:
            self.email = email
        if organization_id is not None:
            self.organization_id = organization_id
        if sender_email is not None:
            self.sender_email = sender_email
        if sender_name is not None:
            self.sender_name = sender_name
        if sso is not None:
            self.sso = sso
        if token is not None:
            self.token = token

    @property
    def accounts_signup_url(self) -> str:
        """Gets the accounts_signup_url of this ModelsSSOInvitation.  # noqa: E501

        AccountsSignupURL is a legacy field, should be removed one more after this issue gets done https://github.com/toggl/accounts-fe/issues/704  # noqa: E501

        :return: The accounts_signup_url of this ModelsSSOInvitation.  # noqa: E501
        :rtype: str
        """
        return self._accounts_signup_url

    @accounts_signup_url.setter
    def accounts_signup_url(self, accounts_signup_url: str):
        """Sets the accounts_signup_url of this ModelsSSOInvitation.

        AccountsSignupURL is a legacy field, should be removed one more after this issue gets done https://github.com/toggl/accounts-fe/issues/704  # noqa: E501

        :param accounts_signup_url: The accounts_signup_url of this ModelsSSOInvitation.  # noqa: E501
        :type: str
        """

        self._accounts_signup_url = accounts_signup_url

    @property
    def code(self) -> str:
        """Gets the code of this ModelsSSOInvitation.  # noqa: E501


        :return: The code of this ModelsSSOInvitation.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this ModelsSSOInvitation.


        :param code: The code of this ModelsSSOInvitation.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def email(self) -> str:
        """Gets the email of this ModelsSSOInvitation.  # noqa: E501


        :return: The email of this ModelsSSOInvitation.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this ModelsSSOInvitation.


        :param email: The email of this ModelsSSOInvitation.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def organization_id(self) -> int:
        """Gets the organization_id of this ModelsSSOInvitation.  # noqa: E501


        :return: The organization_id of this ModelsSSOInvitation.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id: int):
        """Sets the organization_id of this ModelsSSOInvitation.


        :param organization_id: The organization_id of this ModelsSSOInvitation.  # noqa: E501
        :type: int
        """

        self._organization_id = organization_id

    @property
    def sender_email(self) -> str:
        """Gets the sender_email of this ModelsSSOInvitation.  # noqa: E501


        :return: The sender_email of this ModelsSSOInvitation.  # noqa: E501
        :rtype: str
        """
        return self._sender_email

    @sender_email.setter
    def sender_email(self, sender_email: str):
        """Sets the sender_email of this ModelsSSOInvitation.


        :param sender_email: The sender_email of this ModelsSSOInvitation.  # noqa: E501
        :type: str
        """

        self._sender_email = sender_email

    @property
    def sender_name(self) -> str:
        """Gets the sender_name of this ModelsSSOInvitation.  # noqa: E501


        :return: The sender_name of this ModelsSSOInvitation.  # noqa: E501
        :rtype: str
        """
        return self._sender_name

    @sender_name.setter
    def sender_name(self, sender_name: str):
        """Sets the sender_name of this ModelsSSOInvitation.


        :param sender_name: The sender_name of this ModelsSSOInvitation.  # noqa: E501
        :type: str
        """

        self._sender_name = sender_name

    @property
    def sso(self) -> bool:
        """Gets the sso of this ModelsSSOInvitation.  # noqa: E501


        :return: The sso of this ModelsSSOInvitation.  # noqa: E501
        :rtype: bool
        """
        return self._sso

    @sso.setter
    def sso(self, sso: bool):
        """Sets the sso of this ModelsSSOInvitation.


        :param sso: The sso of this ModelsSSOInvitation.  # noqa: E501
        :type: bool
        """

        self._sso = sso

    @property
    def token(self) -> str:
        """Gets the token of this ModelsSSOInvitation.  # noqa: E501


        :return: The token of this ModelsSSOInvitation.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this ModelsSSOInvitation.


        :param token: The token of this ModelsSSOInvitation.  # noqa: E501
        :type: str
        """

        self._token = token

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
        if issubclass(ModelsSSOInvitation, dict):
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
        if not isinstance(other, ModelsSSOInvitation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsSSOInvitation):
            return True

        return self.to_dict() != other.to_dict()
