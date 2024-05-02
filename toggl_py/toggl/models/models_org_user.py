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
from toggl.models.models_group_dict import ModelsGroupDict  # noqa: F401
from toggl.models.models_org_user_workspace import ModelsOrgUserWorkspace  # noqa: F401


class ModelsOrgUser:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "admin": "bool",
        "avatar_url": "str",
        "can_edit_email": "bool",
        "email": "str",
        "groups": "list[ModelsGroupDict]",
        "id": "int",
        "inactive": "bool",
        "invitation_code": "str",
        "joined": "bool",
        "name": "str",
        "owner": "bool",
        "user_id": "int",
        "workspaces": "list[ModelsOrgUserWorkspace]",
    }

    attribute_map = {
        "admin": "admin",
        "avatar_url": "avatar_url",
        "can_edit_email": "can_edit_email",
        "email": "email",
        "groups": "groups",
        "id": "id",
        "inactive": "inactive",
        "invitation_code": "invitation_code",
        "joined": "joined",
        "name": "name",
        "owner": "owner",
        "user_id": "user_id",
        "workspaces": "workspaces",
    }

    def __init__(
        self,
        admin: bool = None,
        avatar_url: str = None,
        can_edit_email: bool = None,
        email: str = None,
        groups: list[ModelsGroupDict] = None,
        id: int = None,
        inactive: bool = None,
        invitation_code: str = None,
        joined: bool = None,
        name: str = None,
        owner: bool = None,
        user_id: int = None,
        workspaces: list[ModelsOrgUserWorkspace] = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        ModelsOrgUser - a model defined in Swagger

        Parameters:
          admin (bool): Optional
          avatar_url (str): Optional
          can_edit_email (bool): Optional
          email (str): Optional
          groups (list[ModelsGroupDict]): Optional
          id (int): Optional
          inactive (bool): Optional
          invitation_code (str): Optional
          joined (bool): Optional
          name (str): Optional
          owner (bool): Optional
          user_id (int): Optional
          workspaces (list[ModelsOrgUserWorkspace]): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._admin = None
        self._avatar_url = None
        self._can_edit_email = None
        self._email = None
        self._groups = None
        self._id = None
        self._inactive = None
        self._invitation_code = None
        self._joined = None
        self._name = None
        self._owner = None
        self._user_id = None
        self._workspaces = None
        self.discriminator = None

        if admin is not None:
            self.admin = admin
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if can_edit_email is not None:
            self.can_edit_email = can_edit_email
        if email is not None:
            self.email = email
        if groups is not None:
            self.groups = groups
        if id is not None:
            self.id = id
        if inactive is not None:
            self.inactive = inactive
        if invitation_code is not None:
            self.invitation_code = invitation_code
        if joined is not None:
            self.joined = joined
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if user_id is not None:
            self.user_id = user_id
        if workspaces is not None:
            self.workspaces = workspaces

    @property
    def admin(self) -> bool:
        """Gets the admin of this ModelsOrgUser.  # noqa: E501


        :return: The admin of this ModelsOrgUser.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin: bool):
        """Sets the admin of this ModelsOrgUser.


        :param admin: The admin of this ModelsOrgUser.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def avatar_url(self) -> str:
        """Gets the avatar_url of this ModelsOrgUser.  # noqa: E501


        :return: The avatar_url of this ModelsOrgUser.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url: str):
        """Sets the avatar_url of this ModelsOrgUser.


        :param avatar_url: The avatar_url of this ModelsOrgUser.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def can_edit_email(self) -> bool:
        """Gets the can_edit_email of this ModelsOrgUser.  # noqa: E501


        :return: The can_edit_email of this ModelsOrgUser.  # noqa: E501
        :rtype: bool
        """
        return self._can_edit_email

    @can_edit_email.setter
    def can_edit_email(self, can_edit_email: bool):
        """Sets the can_edit_email of this ModelsOrgUser.


        :param can_edit_email: The can_edit_email of this ModelsOrgUser.  # noqa: E501
        :type: bool
        """

        self._can_edit_email = can_edit_email

    @property
    def email(self) -> str:
        """Gets the email of this ModelsOrgUser.  # noqa: E501


        :return: The email of this ModelsOrgUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this ModelsOrgUser.


        :param email: The email of this ModelsOrgUser.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def groups(self) -> list[ModelsGroupDict]:
        """Gets the groups of this ModelsOrgUser.  # noqa: E501


        :return: The groups of this ModelsOrgUser.  # noqa: E501
        :rtype: list[ModelsGroupDict]
        """
        return self._groups

    @groups.setter
    def groups(self, groups: list[ModelsGroupDict]):
        """Sets the groups of this ModelsOrgUser.


        :param groups: The groups of this ModelsOrgUser.  # noqa: E501
        :type: list[ModelsGroupDict]
        """

        self._groups = groups

    @property
    def id(self) -> int:
        """Gets the id of this ModelsOrgUser.  # noqa: E501


        :return: The id of this ModelsOrgUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this ModelsOrgUser.


        :param id: The id of this ModelsOrgUser.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def inactive(self) -> bool:
        """Gets the inactive of this ModelsOrgUser.  # noqa: E501


        :return: The inactive of this ModelsOrgUser.  # noqa: E501
        :rtype: bool
        """
        return self._inactive

    @inactive.setter
    def inactive(self, inactive: bool):
        """Sets the inactive of this ModelsOrgUser.


        :param inactive: The inactive of this ModelsOrgUser.  # noqa: E501
        :type: bool
        """

        self._inactive = inactive

    @property
    def invitation_code(self) -> str:
        """Gets the invitation_code of this ModelsOrgUser.  # noqa: E501


        :return: The invitation_code of this ModelsOrgUser.  # noqa: E501
        :rtype: str
        """
        return self._invitation_code

    @invitation_code.setter
    def invitation_code(self, invitation_code: str):
        """Sets the invitation_code of this ModelsOrgUser.


        :param invitation_code: The invitation_code of this ModelsOrgUser.  # noqa: E501
        :type: str
        """

        self._invitation_code = invitation_code

    @property
    def joined(self) -> bool:
        """Gets the joined of this ModelsOrgUser.  # noqa: E501


        :return: The joined of this ModelsOrgUser.  # noqa: E501
        :rtype: bool
        """
        return self._joined

    @joined.setter
    def joined(self, joined: bool):
        """Sets the joined of this ModelsOrgUser.


        :param joined: The joined of this ModelsOrgUser.  # noqa: E501
        :type: bool
        """

        self._joined = joined

    @property
    def name(self) -> str:
        """Gets the name of this ModelsOrgUser.  # noqa: E501


        :return: The name of this ModelsOrgUser.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ModelsOrgUser.


        :param name: The name of this ModelsOrgUser.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def owner(self) -> bool:
        """Gets the owner of this ModelsOrgUser.  # noqa: E501


        :return: The owner of this ModelsOrgUser.  # noqa: E501
        :rtype: bool
        """
        return self._owner

    @owner.setter
    def owner(self, owner: bool):
        """Sets the owner of this ModelsOrgUser.


        :param owner: The owner of this ModelsOrgUser.  # noqa: E501
        :type: bool
        """

        self._owner = owner

    @property
    def user_id(self) -> int:
        """Gets the user_id of this ModelsOrgUser.  # noqa: E501


        :return: The user_id of this ModelsOrgUser.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this ModelsOrgUser.


        :param user_id: The user_id of this ModelsOrgUser.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def workspaces(self) -> list[ModelsOrgUserWorkspace]:
        """Gets the workspaces of this ModelsOrgUser.  # noqa: E501


        :return: The workspaces of this ModelsOrgUser.  # noqa: E501
        :rtype: list[ModelsOrgUserWorkspace]
        """
        return self._workspaces

    @workspaces.setter
    def workspaces(self, workspaces: list[ModelsOrgUserWorkspace]):
        """Sets the workspaces of this ModelsOrgUser.


        :param workspaces: The workspaces of this ModelsOrgUser.  # noqa: E501
        :type: list[ModelsOrgUserWorkspace]
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
        if issubclass(ModelsOrgUser, dict):
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
        if not isinstance(other, ModelsOrgUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsOrgUser):
            return True

        return self.to_dict() != other.to_dict()
