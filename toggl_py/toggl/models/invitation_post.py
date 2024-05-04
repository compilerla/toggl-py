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
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from toggl.models.invitation_post_workspaces import InvitationPostWorkspaces  # noqa: F401


class InvitationPost:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {"emails": "list[str]", "workspaces": "list[InvitationPostWorkspaces]"}

    attribute_map = {"emails": "emails", "workspaces": "workspaces"}

    def __init__(
        self,
        emails: list[str] = None,
        workspaces: list[InvitationPostWorkspaces] = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        InvitationPost - a model defined in Swagger

        Parameters:
          emails (list[str]): Optional
          workspaces (list[InvitationPostWorkspaces]): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._emails = None
        self._workspaces = None
        self.discriminator = None

        if emails is not None:
            self.emails = emails
        if workspaces is not None:
            self.workspaces = workspaces

    @property
    def emails(self) -> list[str]:
        """Gets the emails of this InvitationPost.  # noqa: E501


        :return: The emails of this InvitationPost.  # noqa: E501
        :rtype: list[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails: list[str]):
        """Sets the emails of this InvitationPost.


        :param emails: The emails of this InvitationPost.  # noqa: E501
        :type: list[str]
        """

        self._emails = emails

    @property
    def workspaces(self) -> list[InvitationPostWorkspaces]:
        """Gets the workspaces of this InvitationPost.  # noqa: E501


        :return: The workspaces of this InvitationPost.  # noqa: E501
        :rtype: list[InvitationPostWorkspaces]
        """
        return self._workspaces

    @workspaces.setter
    def workspaces(self, workspaces: list[InvitationPostWorkspaces]):
        """Sets the workspaces of this InvitationPost.


        :param workspaces: The workspaces of this InvitationPost.  # noqa: E501
        :type: list[InvitationPostWorkspaces]
        """

        self._workspaces = workspaces

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
        if issubclass(InvitationPost, dict):
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
        if not isinstance(other, InvitationPost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvitationPost):
            return True

        return self.to_dict() != other.to_dict()
