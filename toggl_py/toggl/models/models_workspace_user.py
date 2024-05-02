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
from toggl.models.utils_int64_slice import UtilsInt64Slice  # noqa: F401


class ModelsWorkspaceUser:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "active": "bool",
        "admin": "bool",
        "at": "str",
        "avatar_file_name": "str",
        "email": "str",
        "group_ids": "UtilsInt64Slice",
        "id": "int",
        "inactive": "bool",
        "invitation_code": "str",
        "invite_url": "str",
        "labour_cost": "int",
        "name": "str",
        "rate": "float",
        "rate_last_updated": "str",
        "role": "str",
        "timezone": "str",
        "uid": "int",
        "wid": "int",
        "working_hours_in_minutes": "int",
    }

    attribute_map = {
        "active": "active",
        "admin": "admin",
        "at": "at",
        "avatar_file_name": "avatar_file_name",
        "email": "email",
        "group_ids": "group_ids",
        "id": "id",
        "inactive": "inactive",
        "invitation_code": "invitation_code",
        "invite_url": "invite_url",
        "labour_cost": "labour_cost",
        "name": "name",
        "rate": "rate",
        "rate_last_updated": "rate_last_updated",
        "role": "role",
        "timezone": "timezone",
        "uid": "uid",
        "wid": "wid",
        "working_hours_in_minutes": "working_hours_in_minutes",
    }

    def __init__(
        self,
        active: bool = None,
        admin: bool = None,
        at: str = None,
        avatar_file_name: str = None,
        email: str = None,
        group_ids: UtilsInt64Slice = None,
        id: int = None,
        inactive: bool = None,
        invitation_code: str = None,
        invite_url: str = None,
        labour_cost: int = None,
        name: str = None,
        rate: float = None,
        rate_last_updated: str = None,
        role: str = None,
        timezone: str = None,
        uid: int = None,
        wid: int = None,
        working_hours_in_minutes: int = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        ModelsWorkspaceUser - a model defined in Swagger

        Parameters:
          active (bool): Optional
          admin (bool): Optional
          at (str): Optional
          avatar_file_name (str): Optional
          email (str): Optional
          group_ids (UtilsInt64Slice): Optional
          id (int): Optional
          inactive (bool): Optional
          invitation_code (str): Optional
          invite_url (str): Optional
          labour_cost (int): Optional
          name (str): Optional
          rate (float): Optional
          rate_last_updated (str): Optional
          role (str): Optional
          timezone (str): Optional
          uid (int): Optional
          wid (int): Optional
          working_hours_in_minutes (int): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active = None
        self._admin = None
        self._at = None
        self._avatar_file_name = None
        self._email = None
        self._group_ids = None
        self._id = None
        self._inactive = None
        self._invitation_code = None
        self._invite_url = None
        self._labour_cost = None
        self._name = None
        self._rate = None
        self._rate_last_updated = None
        self._role = None
        self._timezone = None
        self._uid = None
        self._wid = None
        self._working_hours_in_minutes = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if admin is not None:
            self.admin = admin
        if at is not None:
            self.at = at
        if avatar_file_name is not None:
            self.avatar_file_name = avatar_file_name
        if email is not None:
            self.email = email
        if group_ids is not None:
            self.group_ids = group_ids
        if id is not None:
            self.id = id
        if inactive is not None:
            self.inactive = inactive
        if invitation_code is not None:
            self.invitation_code = invitation_code
        if invite_url is not None:
            self.invite_url = invite_url
        if labour_cost is not None:
            self.labour_cost = labour_cost
        if name is not None:
            self.name = name
        if rate is not None:
            self.rate = rate
        if rate_last_updated is not None:
            self.rate_last_updated = rate_last_updated
        if role is not None:
            self.role = role
        if timezone is not None:
            self.timezone = timezone
        if uid is not None:
            self.uid = uid
        if wid is not None:
            self.wid = wid
        if working_hours_in_minutes is not None:
            self.working_hours_in_minutes = working_hours_in_minutes

    @property
    def active(self) -> bool:
        """Gets the active of this ModelsWorkspaceUser.  # noqa: E501


        :return: The active of this ModelsWorkspaceUser.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active: bool):
        """Sets the active of this ModelsWorkspaceUser.


        :param active: The active of this ModelsWorkspaceUser.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def admin(self) -> bool:
        """Gets the admin of this ModelsWorkspaceUser.  # noqa: E501


        :return: The admin of this ModelsWorkspaceUser.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin: bool):
        """Sets the admin of this ModelsWorkspaceUser.


        :param admin: The admin of this ModelsWorkspaceUser.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def at(self) -> str:
        """Gets the at of this ModelsWorkspaceUser.  # noqa: E501


        :return: The at of this ModelsWorkspaceUser.  # noqa: E501
        :rtype: str
        """
        return self._at

    @at.setter
    def at(self, at: str):
        """Sets the at of this ModelsWorkspaceUser.


        :param at: The at of this ModelsWorkspaceUser.  # noqa: E501
        :type: str
        """

        self._at = at

    @property
    def avatar_file_name(self) -> str:
        """Gets the avatar_file_name of this ModelsWorkspaceUser.  # noqa: E501


        :return: The avatar_file_name of this ModelsWorkspaceUser.  # noqa: E501
        :rtype: str
        """
        return self._avatar_file_name

    @avatar_file_name.setter
    def avatar_file_name(self, avatar_file_name: str):
        """Sets the avatar_file_name of this ModelsWorkspaceUser.


        :param avatar_file_name: The avatar_file_name of this ModelsWorkspaceUser.  # noqa: E501
        :type: str
        """

        self._avatar_file_name = avatar_file_name

    @property
    def email(self) -> str:
        """Gets the email of this ModelsWorkspaceUser.  # noqa: E501


        :return: The email of this ModelsWorkspaceUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this ModelsWorkspaceUser.


        :param email: The email of this ModelsWorkspaceUser.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def group_ids(self) -> UtilsInt64Slice:
        """Gets the group_ids of this ModelsWorkspaceUser.  # noqa: E501


        :return: The group_ids of this ModelsWorkspaceUser.  # noqa: E501
        :rtype: UtilsInt64Slice
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids: UtilsInt64Slice):
        """Sets the group_ids of this ModelsWorkspaceUser.


        :param group_ids: The group_ids of this ModelsWorkspaceUser.  # noqa: E501
        :type: UtilsInt64Slice
        """

        self._group_ids = group_ids

    @property
    def id(self) -> int:
        """Gets the id of this ModelsWorkspaceUser.  # noqa: E501


        :return: The id of this ModelsWorkspaceUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this ModelsWorkspaceUser.


        :param id: The id of this ModelsWorkspaceUser.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def inactive(self) -> bool:
        """Gets the inactive of this ModelsWorkspaceUser.  # noqa: E501


        :return: The inactive of this ModelsWorkspaceUser.  # noqa: E501
        :rtype: bool
        """
        return self._inactive

    @inactive.setter
    def inactive(self, inactive: bool):
        """Sets the inactive of this ModelsWorkspaceUser.


        :param inactive: The inactive of this ModelsWorkspaceUser.  # noqa: E501
        :type: bool
        """

        self._inactive = inactive

    @property
    def invitation_code(self) -> str:
        """Gets the invitation_code of this ModelsWorkspaceUser.  # noqa: E501


        :return: The invitation_code of this ModelsWorkspaceUser.  # noqa: E501
        :rtype: str
        """
        return self._invitation_code

    @invitation_code.setter
    def invitation_code(self, invitation_code: str):
        """Sets the invitation_code of this ModelsWorkspaceUser.


        :param invitation_code: The invitation_code of this ModelsWorkspaceUser.  # noqa: E501
        :type: str
        """

        self._invitation_code = invitation_code

    @property
    def invite_url(self) -> str:
        """Gets the invite_url of this ModelsWorkspaceUser.  # noqa: E501


        :return: The invite_url of this ModelsWorkspaceUser.  # noqa: E501
        :rtype: str
        """
        return self._invite_url

    @invite_url.setter
    def invite_url(self, invite_url: str):
        """Sets the invite_url of this ModelsWorkspaceUser.


        :param invite_url: The invite_url of this ModelsWorkspaceUser.  # noqa: E501
        :type: str
        """

        self._invite_url = invite_url

    @property
    def labour_cost(self) -> int:
        """Gets the labour_cost of this ModelsWorkspaceUser.  # noqa: E501


        :return: The labour_cost of this ModelsWorkspaceUser.  # noqa: E501
        :rtype: int
        """
        return self._labour_cost

    @labour_cost.setter
    def labour_cost(self, labour_cost: int):
        """Sets the labour_cost of this ModelsWorkspaceUser.


        :param labour_cost: The labour_cost of this ModelsWorkspaceUser.  # noqa: E501
        :type: int
        """

        self._labour_cost = labour_cost

    @property
    def name(self) -> str:
        """Gets the name of this ModelsWorkspaceUser.  # noqa: E501


        :return: The name of this ModelsWorkspaceUser.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ModelsWorkspaceUser.


        :param name: The name of this ModelsWorkspaceUser.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def rate(self) -> float:
        """Gets the rate of this ModelsWorkspaceUser.  # noqa: E501


        :return: The rate of this ModelsWorkspaceUser.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate: float):
        """Sets the rate of this ModelsWorkspaceUser.


        :param rate: The rate of this ModelsWorkspaceUser.  # noqa: E501
        :type: float
        """

        self._rate = rate

    @property
    def rate_last_updated(self) -> str:
        """Gets the rate_last_updated of this ModelsWorkspaceUser.  # noqa: E501


        :return: The rate_last_updated of this ModelsWorkspaceUser.  # noqa: E501
        :rtype: str
        """
        return self._rate_last_updated

    @rate_last_updated.setter
    def rate_last_updated(self, rate_last_updated: str):
        """Sets the rate_last_updated of this ModelsWorkspaceUser.


        :param rate_last_updated: The rate_last_updated of this ModelsWorkspaceUser.  # noqa: E501
        :type: str
        """

        self._rate_last_updated = rate_last_updated

    @property
    def role(self) -> str:
        """Gets the role of this ModelsWorkspaceUser.  # noqa: E501


        :return: The role of this ModelsWorkspaceUser.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role: str):
        """Sets the role of this ModelsWorkspaceUser.


        :param role: The role of this ModelsWorkspaceUser.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def timezone(self) -> str:
        """Gets the timezone of this ModelsWorkspaceUser.  # noqa: E501


        :return: The timezone of this ModelsWorkspaceUser.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone: str):
        """Sets the timezone of this ModelsWorkspaceUser.


        :param timezone: The timezone of this ModelsWorkspaceUser.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def uid(self) -> int:
        """Gets the uid of this ModelsWorkspaceUser.  # noqa: E501


        :return: The uid of this ModelsWorkspaceUser.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid: int):
        """Sets the uid of this ModelsWorkspaceUser.


        :param uid: The uid of this ModelsWorkspaceUser.  # noqa: E501
        :type: int
        """

        self._uid = uid

    @property
    def wid(self) -> int:
        """Gets the wid of this ModelsWorkspaceUser.  # noqa: E501


        :return: The wid of this ModelsWorkspaceUser.  # noqa: E501
        :rtype: int
        """
        return self._wid

    @wid.setter
    def wid(self, wid: int):
        """Sets the wid of this ModelsWorkspaceUser.


        :param wid: The wid of this ModelsWorkspaceUser.  # noqa: E501
        :type: int
        """

        self._wid = wid

    @property
    def working_hours_in_minutes(self) -> int:
        """Gets the working_hours_in_minutes of this ModelsWorkspaceUser.  # noqa: E501


        :return: The working_hours_in_minutes of this ModelsWorkspaceUser.  # noqa: E501
        :rtype: int
        """
        return self._working_hours_in_minutes

    @working_hours_in_minutes.setter
    def working_hours_in_minutes(self, working_hours_in_minutes: int):
        """Sets the working_hours_in_minutes of this ModelsWorkspaceUser.


        :param working_hours_in_minutes: The working_hours_in_minutes of this ModelsWorkspaceUser.  # noqa: E501
        :type: int
        """

        self._working_hours_in_minutes = working_hours_in_minutes

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
        if issubclass(ModelsWorkspaceUser, dict):
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
        if not isinstance(other, ModelsWorkspaceUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsWorkspaceUser):
            return True

        return self.to_dict() != other.to_dict()
