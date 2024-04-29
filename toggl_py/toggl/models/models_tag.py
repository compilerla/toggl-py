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


class ModelsTag:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "at": "str",
        "creator_id": "int",
        "deleted_at": "datetime",
        "id": "int",
        "name": "str",
        "permissions": "str",
        "workspace_id": "int",
    }

    attribute_map = {
        "at": "at",
        "creator_id": "creator_id",
        "deleted_at": "deleted_at",
        "id": "id",
        "name": "name",
        "permissions": "permissions",
        "workspace_id": "workspace_id",
    }

    def __init__(
        self,
        at=None,
        creator_id=None,
        deleted_at=None,
        id=None,
        name=None,
        permissions=None,
        workspace_id=None,
        _configuration=None,
    ):  # noqa: E501
        """ModelsTag - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._at = None
        self._creator_id = None
        self._deleted_at = None
        self._id = None
        self._name = None
        self._permissions = None
        self._workspace_id = None
        self.discriminator = None

        if at is not None:
            self.at = at
        if creator_id is not None:
            self.creator_id = creator_id
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if permissions is not None:
            self.permissions = permissions
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def at(self):
        """Gets the at of this ModelsTag.  # noqa: E501

        When was created/last modified  # noqa: E501

        :return: The at of this ModelsTag.  # noqa: E501
        :rtype: str
        """
        return self._at

    @at.setter
    def at(self, at):
        """Sets the at of this ModelsTag.

        When was created/last modified  # noqa: E501

        :param at: The at of this ModelsTag.  # noqa: E501
        :type: str
        """

        self._at = at

    @property
    def creator_id(self):
        """Gets the creator_id of this ModelsTag.  # noqa: E501

        CreatorID the user who created the tag  # noqa: E501

        :return: The creator_id of this ModelsTag.  # noqa: E501
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this ModelsTag.

        CreatorID the user who created the tag  # noqa: E501

        :param creator_id: The creator_id of this ModelsTag.  # noqa: E501
        :type: int
        """

        self._creator_id = creator_id

    @property
    def deleted_at(self):
        """Gets the deleted_at of this ModelsTag.  # noqa: E501

        When was deleted  # noqa: E501

        :return: The deleted_at of this ModelsTag.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this ModelsTag.

        When was deleted  # noqa: E501

        :param deleted_at: The deleted_at of this ModelsTag.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def id(self):
        """Gets the id of this ModelsTag.  # noqa: E501

        Tag ID  # noqa: E501

        :return: The id of this ModelsTag.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelsTag.

        Tag ID  # noqa: E501

        :param id: The id of this ModelsTag.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ModelsTag.  # noqa: E501

        Tag name  # noqa: E501

        :return: The name of this ModelsTag.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelsTag.

        Tag name  # noqa: E501

        :param name: The name of this ModelsTag.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def permissions(self):
        """Gets the permissions of this ModelsTag.  # noqa: E501


        :return: The permissions of this ModelsTag.  # noqa: E501
        :rtype: str
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this ModelsTag.


        :param permissions: The permissions of this ModelsTag.  # noqa: E501
        :type: str
        """

        self._permissions = permissions

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ModelsTag.  # noqa: E501

        Workspace ID  # noqa: E501

        :return: The workspace_id of this ModelsTag.  # noqa: E501
        :rtype: int
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ModelsTag.

        Workspace ID  # noqa: E501

        :param workspace_id: The workspace_id of this ModelsTag.  # noqa: E501
        :type: int
        """

        self._workspace_id = workspace_id

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
        if issubclass(ModelsTag, dict):
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
        if not isinstance(other, ModelsTag):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsTag):
            return True

        return self.to_dict() != other.to_dict()
