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


class OrganizationPostOrganizationReply:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"id": "int", "name": "str", "permissions": "str", "workspace_id": "int", "workspace_name": "str"}

    attribute_map = {
        "id": "id",
        "name": "name",
        "permissions": "permissions",
        "workspace_id": "workspace_id",
        "workspace_name": "workspace_name",
    }

    def __init__(
        self, id=None, name=None, permissions=None, workspace_id=None, workspace_name=None, _configuration=None
    ):  # noqa: E501
        """OrganizationPostOrganizationReply - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._permissions = None
        self._workspace_id = None
        self._workspace_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if permissions is not None:
            self.permissions = permissions
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if workspace_name is not None:
            self.workspace_name = workspace_name

    @property
    def id(self):
        """Gets the id of this OrganizationPostOrganizationReply.  # noqa: E501


        :return: The id of this OrganizationPostOrganizationReply.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganizationPostOrganizationReply.


        :param id: The id of this OrganizationPostOrganizationReply.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this OrganizationPostOrganizationReply.  # noqa: E501


        :return: The name of this OrganizationPostOrganizationReply.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationPostOrganizationReply.


        :param name: The name of this OrganizationPostOrganizationReply.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def permissions(self):
        """Gets the permissions of this OrganizationPostOrganizationReply.  # noqa: E501


        :return: The permissions of this OrganizationPostOrganizationReply.  # noqa: E501
        :rtype: str
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this OrganizationPostOrganizationReply.


        :param permissions: The permissions of this OrganizationPostOrganizationReply.  # noqa: E501
        :type: str
        """

        self._permissions = permissions

    @property
    def workspace_id(self):
        """Gets the workspace_id of this OrganizationPostOrganizationReply.  # noqa: E501


        :return: The workspace_id of this OrganizationPostOrganizationReply.  # noqa: E501
        :rtype: int
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this OrganizationPostOrganizationReply.


        :param workspace_id: The workspace_id of this OrganizationPostOrganizationReply.  # noqa: E501
        :type: int
        """

        self._workspace_id = workspace_id

    @property
    def workspace_name(self):
        """Gets the workspace_name of this OrganizationPostOrganizationReply.  # noqa: E501


        :return: The workspace_name of this OrganizationPostOrganizationReply.  # noqa: E501
        :rtype: str
        """
        return self._workspace_name

    @workspace_name.setter
    def workspace_name(self, workspace_name):
        """Sets the workspace_name of this OrganizationPostOrganizationReply.


        :param workspace_name: The workspace_name of this OrganizationPostOrganizationReply.  # noqa: E501
        :type: str
        """

        self._workspace_name = workspace_name

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
        if issubclass(OrganizationPostOrganizationReply, dict):
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
        if not isinstance(other, OrganizationPostOrganizationReply):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationPostOrganizationReply):
            return True

        return self.to_dict() != other.to_dict()
