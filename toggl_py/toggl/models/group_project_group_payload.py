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


class GroupProjectGroupPayload:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"group_id": "int", "project_id": "int"}

    attribute_map = {"group_id": "group_id", "project_id": "project_id"}

    def __init__(self, group_id=None, project_id=None, _configuration=None):  # noqa: E501
        """GroupProjectGroupPayload - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._group_id = None
        self._project_id = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if project_id is not None:
            self.project_id = project_id

    @property
    def group_id(self):
        """Gets the group_id of this GroupProjectGroupPayload.  # noqa: E501

        Group ID  # noqa: E501

        :return: The group_id of this GroupProjectGroupPayload.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GroupProjectGroupPayload.

        Group ID  # noqa: E501

        :param group_id: The group_id of this GroupProjectGroupPayload.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def project_id(self):
        """Gets the project_id of this GroupProjectGroupPayload.  # noqa: E501

        Project ID  # noqa: E501

        :return: The project_id of this GroupProjectGroupPayload.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this GroupProjectGroupPayload.

        Project ID  # noqa: E501

        :param project_id: The project_id of this GroupProjectGroupPayload.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

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
        if issubclass(GroupProjectGroupPayload, dict):
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
        if not isinstance(other, GroupProjectGroupPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupProjectGroupPayload):
            return True

        return self.to_dict() != other.to_dict()
