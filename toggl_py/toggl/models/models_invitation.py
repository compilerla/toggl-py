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


class ModelsInvitation:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"code": "str", "email": "str", "organization_id": "int", "sender_email": "str", "sender_name": "str"}

    attribute_map = {
        "code": "code",
        "email": "email",
        "organization_id": "organization_id",
        "sender_email": "sender_email",
        "sender_name": "sender_name",
    }

    def __init__(
        self, code=None, email=None, organization_id=None, sender_email=None, sender_name=None, _configuration=None
    ):  # noqa: E501
        """ModelsInvitation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code = None
        self._email = None
        self._organization_id = None
        self._sender_email = None
        self._sender_name = None
        self.discriminator = None

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

    @property
    def code(self):
        """Gets the code of this ModelsInvitation.  # noqa: E501


        :return: The code of this ModelsInvitation.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ModelsInvitation.


        :param code: The code of this ModelsInvitation.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def email(self):
        """Gets the email of this ModelsInvitation.  # noqa: E501


        :return: The email of this ModelsInvitation.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ModelsInvitation.


        :param email: The email of this ModelsInvitation.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def organization_id(self):
        """Gets the organization_id of this ModelsInvitation.  # noqa: E501


        :return: The organization_id of this ModelsInvitation.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this ModelsInvitation.


        :param organization_id: The organization_id of this ModelsInvitation.  # noqa: E501
        :type: int
        """

        self._organization_id = organization_id

    @property
    def sender_email(self):
        """Gets the sender_email of this ModelsInvitation.  # noqa: E501


        :return: The sender_email of this ModelsInvitation.  # noqa: E501
        :rtype: str
        """
        return self._sender_email

    @sender_email.setter
    def sender_email(self, sender_email):
        """Sets the sender_email of this ModelsInvitation.


        :param sender_email: The sender_email of this ModelsInvitation.  # noqa: E501
        :type: str
        """

        self._sender_email = sender_email

    @property
    def sender_name(self):
        """Gets the sender_name of this ModelsInvitation.  # noqa: E501


        :return: The sender_name of this ModelsInvitation.  # noqa: E501
        :rtype: str
        """
        return self._sender_name

    @sender_name.setter
    def sender_name(self, sender_name):
        """Sets the sender_name of this ModelsInvitation.


        :param sender_name: The sender_name of this ModelsInvitation.  # noqa: E501
        :type: str
        """

        self._sender_name = sender_name

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
        if issubclass(ModelsInvitation, dict):
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
        if not isinstance(other, ModelsInvitation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsInvitation):
            return True

        return self.to_dict() != other.to_dict()
