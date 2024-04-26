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


class InvitationInfo:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "email": "str",
        "invitation_id": "int",
        "invite_url": "str",
        "organization_id": "int",
        "recipient_id": "int",
        "sender_id": "int",
    }

    attribute_map = {
        "email": "email",
        "invitation_id": "invitation_id",
        "invite_url": "invite_url",
        "organization_id": "organization_id",
        "recipient_id": "recipient_id",
        "sender_id": "sender_id",
    }

    def __init__(
        self,
        email=None,
        invitation_id=None,
        invite_url=None,
        organization_id=None,
        recipient_id=None,
        sender_id=None,
        _configuration=None,
    ):  # noqa: E501
        """InvitationInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._email = None
        self._invitation_id = None
        self._invite_url = None
        self._organization_id = None
        self._recipient_id = None
        self._sender_id = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if invitation_id is not None:
            self.invitation_id = invitation_id
        if invite_url is not None:
            self.invite_url = invite_url
        if organization_id is not None:
            self.organization_id = organization_id
        if recipient_id is not None:
            self.recipient_id = recipient_id
        if sender_id is not None:
            self.sender_id = sender_id

    @property
    def email(self):
        """Gets the email of this InvitationInfo.  # noqa: E501


        :return: The email of this InvitationInfo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InvitationInfo.


        :param email: The email of this InvitationInfo.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def invitation_id(self):
        """Gets the invitation_id of this InvitationInfo.  # noqa: E501


        :return: The invitation_id of this InvitationInfo.  # noqa: E501
        :rtype: int
        """
        return self._invitation_id

    @invitation_id.setter
    def invitation_id(self, invitation_id):
        """Sets the invitation_id of this InvitationInfo.


        :param invitation_id: The invitation_id of this InvitationInfo.  # noqa: E501
        :type: int
        """

        self._invitation_id = invitation_id

    @property
    def invite_url(self):
        """Gets the invite_url of this InvitationInfo.  # noqa: E501


        :return: The invite_url of this InvitationInfo.  # noqa: E501
        :rtype: str
        """
        return self._invite_url

    @invite_url.setter
    def invite_url(self, invite_url):
        """Sets the invite_url of this InvitationInfo.


        :param invite_url: The invite_url of this InvitationInfo.  # noqa: E501
        :type: str
        """

        self._invite_url = invite_url

    @property
    def organization_id(self):
        """Gets the organization_id of this InvitationInfo.  # noqa: E501


        :return: The organization_id of this InvitationInfo.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this InvitationInfo.


        :param organization_id: The organization_id of this InvitationInfo.  # noqa: E501
        :type: int
        """

        self._organization_id = organization_id

    @property
    def recipient_id(self):
        """Gets the recipient_id of this InvitationInfo.  # noqa: E501


        :return: The recipient_id of this InvitationInfo.  # noqa: E501
        :rtype: int
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this InvitationInfo.


        :param recipient_id: The recipient_id of this InvitationInfo.  # noqa: E501
        :type: int
        """

        self._recipient_id = recipient_id

    @property
    def sender_id(self):
        """Gets the sender_id of this InvitationInfo.  # noqa: E501


        :return: The sender_id of this InvitationInfo.  # noqa: E501
        :rtype: int
        """
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        """Sets the sender_id of this InvitationInfo.


        :param sender_id: The sender_id of this InvitationInfo.  # noqa: E501
        :type: int
        """

        self._sender_id = sender_id

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
        if issubclass(InvitationInfo, dict):
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
        if not isinstance(other, InvitationInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvitationInfo):
            return True

        return self.to_dict() != other.to_dict()