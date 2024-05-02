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


class ModelsSimpleWorkspaceUser:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "email": "str",
        "fullname": "str",
        "id": "int",
        "inactive": "bool",
        "is_active": "bool",
        "is_admin": "bool",
        "role": "str",
    }

    attribute_map = {
        "email": "email",
        "fullname": "fullname",
        "id": "id",
        "inactive": "inactive",
        "is_active": "is_active",
        "is_admin": "is_admin",
        "role": "role",
    }

    def __init__(
        self,
        email: str = None,
        fullname: str = None,
        id: int = None,
        inactive: bool = None,
        is_active: bool = None,
        is_admin: bool = None,
        role: str = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        ModelsSimpleWorkspaceUser - a model defined in Swagger

        Parameters:
          email (str): Optional
          fullname (str): Optional
          id (int): Optional
          inactive (bool): Optional
          is_active (bool): Optional
          is_admin (bool): Optional
          role (str): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._email = None
        self._fullname = None
        self._id = None
        self._inactive = None
        self._is_active = None
        self._is_admin = None
        self._role = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if fullname is not None:
            self.fullname = fullname
        if id is not None:
            self.id = id
        if inactive is not None:
            self.inactive = inactive
        if is_active is not None:
            self.is_active = is_active
        if is_admin is not None:
            self.is_admin = is_admin
        if role is not None:
            self.role = role

    @property
    def email(self) -> str:
        """Gets the email of this ModelsSimpleWorkspaceUser.  # noqa: E501

        Email of the user  # noqa: E501

        :return: The email of this ModelsSimpleWorkspaceUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this ModelsSimpleWorkspaceUser.

        Email of the user  # noqa: E501

        :param email: The email of this ModelsSimpleWorkspaceUser.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def fullname(self) -> str:
        """Gets the fullname of this ModelsSimpleWorkspaceUser.  # noqa: E501

        Name of the user  # noqa: E501

        :return: The fullname of this ModelsSimpleWorkspaceUser.  # noqa: E501
        :rtype: str
        """
        return self._fullname

    @fullname.setter
    def fullname(self, fullname: str):
        """Sets the fullname of this ModelsSimpleWorkspaceUser.

        Name of the user  # noqa: E501

        :param fullname: The fullname of this ModelsSimpleWorkspaceUser.  # noqa: E501
        :type: str
        """

        self._fullname = fullname

    @property
    def id(self) -> int:
        """Gets the id of this ModelsSimpleWorkspaceUser.  # noqa: E501

        Global user identifier  # noqa: E501

        :return: The id of this ModelsSimpleWorkspaceUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this ModelsSimpleWorkspaceUser.

        Global user identifier  # noqa: E501

        :param id: The id of this ModelsSimpleWorkspaceUser.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def inactive(self) -> bool:
        """Gets the inactive of this ModelsSimpleWorkspaceUser.  # noqa: E501

        internal  # noqa: E501

        :return: The inactive of this ModelsSimpleWorkspaceUser.  # noqa: E501
        :rtype: bool
        """
        return self._inactive

    @inactive.setter
    def inactive(self, inactive: bool):
        """Sets the inactive of this ModelsSimpleWorkspaceUser.

        internal  # noqa: E501

        :param inactive: The inactive of this ModelsSimpleWorkspaceUser.  # noqa: E501
        :type: bool
        """

        self._inactive = inactive

    @property
    def is_active(self) -> bool:
        """Gets the is_active of this ModelsSimpleWorkspaceUser.  # noqa: E501

        internal  # noqa: E501

        :return: The is_active of this ModelsSimpleWorkspaceUser.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active: bool):
        """Sets the is_active of this ModelsSimpleWorkspaceUser.

        internal  # noqa: E501

        :param is_active: The is_active of this ModelsSimpleWorkspaceUser.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def is_admin(self) -> bool:
        """Gets the is_admin of this ModelsSimpleWorkspaceUser.  # noqa: E501

        Flag indicating if user is admin  # noqa: E501

        :return: The is_admin of this ModelsSimpleWorkspaceUser.  # noqa: E501
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin: bool):
        """Sets the is_admin of this ModelsSimpleWorkspaceUser.

        Flag indicating if user is admin  # noqa: E501

        :param is_admin: The is_admin of this ModelsSimpleWorkspaceUser.  # noqa: E501
        :type: bool
        """

        self._is_admin = is_admin

    @property
    def role(self) -> str:
        """Gets the role of this ModelsSimpleWorkspaceUser.  # noqa: E501

        Role of the user  # noqa: E501

        :return: The role of this ModelsSimpleWorkspaceUser.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role: str):
        """Sets the role of this ModelsSimpleWorkspaceUser.

        Role of the user  # noqa: E501

        :param role: The role of this ModelsSimpleWorkspaceUser.  # noqa: E501
        :type: str
        """

        self._role = role

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
        if issubclass(ModelsSimpleWorkspaceUser, dict):
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
        if not isinstance(other, ModelsSimpleWorkspaceUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsSimpleWorkspaceUser):
            return True

        return self.to_dict() != other.to_dict()
