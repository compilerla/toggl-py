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


class ModelsOrgUserDetailed:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "admin": "bool",
        "avatar_url": "str",
        "email": "str",
        "fullname": "str",
        "groups": "list[ModelsGroupDict]",
        "inactive": "bool",
        "joined": "bool",
        "organization_id": "int",
        "organization_user_id": "int",
        "owner": "bool",
        "user_id": "int",
        "workspaces": "list[ModelsOrgUserWorkspaceDetails]",
    }

    attribute_map = {
        "admin": "admin",
        "avatar_url": "avatar_url",
        "email": "email",
        "fullname": "fullname",
        "groups": "groups",
        "inactive": "inactive",
        "joined": "joined",
        "organization_id": "organization_id",
        "organization_user_id": "organization_user_id",
        "owner": "owner",
        "user_id": "user_id",
        "workspaces": "workspaces",
    }

    def __init__(
        self,
        admin=None,
        avatar_url=None,
        email=None,
        fullname=None,
        groups=None,
        inactive=None,
        joined=None,
        organization_id=None,
        organization_user_id=None,
        owner=None,
        user_id=None,
        workspaces=None,
        _configuration=None,
    ):  # noqa: E501
        """ModelsOrgUserDetailed - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._admin = None
        self._avatar_url = None
        self._email = None
        self._fullname = None
        self._groups = None
        self._inactive = None
        self._joined = None
        self._organization_id = None
        self._organization_user_id = None
        self._owner = None
        self._user_id = None
        self._workspaces = None
        self.discriminator = None

        if admin is not None:
            self.admin = admin
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if email is not None:
            self.email = email
        if fullname is not None:
            self.fullname = fullname
        if groups is not None:
            self.groups = groups
        if inactive is not None:
            self.inactive = inactive
        if joined is not None:
            self.joined = joined
        if organization_id is not None:
            self.organization_id = organization_id
        if organization_user_id is not None:
            self.organization_user_id = organization_user_id
        if owner is not None:
            self.owner = owner
        if user_id is not None:
            self.user_id = user_id
        if workspaces is not None:
            self.workspaces = workspaces

    @property
    def admin(self):
        """Gets the admin of this ModelsOrgUserDetailed.  # noqa: E501


        :return: The admin of this ModelsOrgUserDetailed.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this ModelsOrgUserDetailed.


        :param admin: The admin of this ModelsOrgUserDetailed.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def avatar_url(self):
        """Gets the avatar_url of this ModelsOrgUserDetailed.  # noqa: E501


        :return: The avatar_url of this ModelsOrgUserDetailed.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this ModelsOrgUserDetailed.


        :param avatar_url: The avatar_url of this ModelsOrgUserDetailed.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def email(self):
        """Gets the email of this ModelsOrgUserDetailed.  # noqa: E501


        :return: The email of this ModelsOrgUserDetailed.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ModelsOrgUserDetailed.


        :param email: The email of this ModelsOrgUserDetailed.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def fullname(self):
        """Gets the fullname of this ModelsOrgUserDetailed.  # noqa: E501


        :return: The fullname of this ModelsOrgUserDetailed.  # noqa: E501
        :rtype: str
        """
        return self._fullname

    @fullname.setter
    def fullname(self, fullname):
        """Sets the fullname of this ModelsOrgUserDetailed.


        :param fullname: The fullname of this ModelsOrgUserDetailed.  # noqa: E501
        :type: str
        """

        self._fullname = fullname

    @property
    def groups(self):
        """Gets the groups of this ModelsOrgUserDetailed.  # noqa: E501


        :return: The groups of this ModelsOrgUserDetailed.  # noqa: E501
        :rtype: list[ModelsGroupDict]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ModelsOrgUserDetailed.


        :param groups: The groups of this ModelsOrgUserDetailed.  # noqa: E501
        :type: list[ModelsGroupDict]
        """

        self._groups = groups

    @property
    def inactive(self):
        """Gets the inactive of this ModelsOrgUserDetailed.  # noqa: E501


        :return: The inactive of this ModelsOrgUserDetailed.  # noqa: E501
        :rtype: bool
        """
        return self._inactive

    @inactive.setter
    def inactive(self, inactive):
        """Sets the inactive of this ModelsOrgUserDetailed.


        :param inactive: The inactive of this ModelsOrgUserDetailed.  # noqa: E501
        :type: bool
        """

        self._inactive = inactive

    @property
    def joined(self):
        """Gets the joined of this ModelsOrgUserDetailed.  # noqa: E501


        :return: The joined of this ModelsOrgUserDetailed.  # noqa: E501
        :rtype: bool
        """
        return self._joined

    @joined.setter
    def joined(self, joined):
        """Sets the joined of this ModelsOrgUserDetailed.


        :param joined: The joined of this ModelsOrgUserDetailed.  # noqa: E501
        :type: bool
        """

        self._joined = joined

    @property
    def organization_id(self):
        """Gets the organization_id of this ModelsOrgUserDetailed.  # noqa: E501


        :return: The organization_id of this ModelsOrgUserDetailed.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this ModelsOrgUserDetailed.


        :param organization_id: The organization_id of this ModelsOrgUserDetailed.  # noqa: E501
        :type: int
        """

        self._organization_id = organization_id

    @property
    def organization_user_id(self):
        """Gets the organization_user_id of this ModelsOrgUserDetailed.  # noqa: E501


        :return: The organization_user_id of this ModelsOrgUserDetailed.  # noqa: E501
        :rtype: int
        """
        return self._organization_user_id

    @organization_user_id.setter
    def organization_user_id(self, organization_user_id):
        """Sets the organization_user_id of this ModelsOrgUserDetailed.


        :param organization_user_id: The organization_user_id of this ModelsOrgUserDetailed.  # noqa: E501
        :type: int
        """

        self._organization_user_id = organization_user_id

    @property
    def owner(self):
        """Gets the owner of this ModelsOrgUserDetailed.  # noqa: E501


        :return: The owner of this ModelsOrgUserDetailed.  # noqa: E501
        :rtype: bool
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ModelsOrgUserDetailed.


        :param owner: The owner of this ModelsOrgUserDetailed.  # noqa: E501
        :type: bool
        """

        self._owner = owner

    @property
    def user_id(self):
        """Gets the user_id of this ModelsOrgUserDetailed.  # noqa: E501


        :return: The user_id of this ModelsOrgUserDetailed.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ModelsOrgUserDetailed.


        :param user_id: The user_id of this ModelsOrgUserDetailed.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def workspaces(self):
        """Gets the workspaces of this ModelsOrgUserDetailed.  # noqa: E501


        :return: The workspaces of this ModelsOrgUserDetailed.  # noqa: E501
        :rtype: list[ModelsOrgUserWorkspaceDetails]
        """
        return self._workspaces

    @workspaces.setter
    def workspaces(self, workspaces):
        """Sets the workspaces of this ModelsOrgUserDetailed.


        :param workspaces: The workspaces of this ModelsOrgUserDetailed.  # noqa: E501
        :type: list[ModelsOrgUserWorkspaceDetails]
        """

        self._workspaces = workspaces

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
        if issubclass(ModelsOrgUserDetailed, dict):
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
        if not isinstance(other, ModelsOrgUserDetailed):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsOrgUserDetailed):
            return True

        return self.to_dict() != other.to_dict()
