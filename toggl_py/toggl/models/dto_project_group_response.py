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


class DtoProjectGroupResponse:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"group_id": "int", "id": "int", "name": "str", "project_id": "int"}

    attribute_map = {"group_id": "group_id", "id": "id", "name": "name", "project_id": "project_id"}

    def __init__(self, group_id=None, id=None, name=None, project_id=None, _configuration=None):  # noqa: E501
        """DtoProjectGroupResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._group_id = None
        self._id = None
        self._name = None
        self._project_id = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id

    @property
    def group_id(self):
        """Gets the group_id of this DtoProjectGroupResponse.  # noqa: E501


        :return: The group_id of this DtoProjectGroupResponse.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this DtoProjectGroupResponse.


        :param group_id: The group_id of this DtoProjectGroupResponse.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def id(self):
        """Gets the id of this DtoProjectGroupResponse.  # noqa: E501


        :return: The id of this DtoProjectGroupResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DtoProjectGroupResponse.


        :param id: The id of this DtoProjectGroupResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DtoProjectGroupResponse.  # noqa: E501


        :return: The name of this DtoProjectGroupResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DtoProjectGroupResponse.


        :param name: The name of this DtoProjectGroupResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this DtoProjectGroupResponse.  # noqa: E501


        :return: The project_id of this DtoProjectGroupResponse.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DtoProjectGroupResponse.


        :param project_id: The project_id of this DtoProjectGroupResponse.  # noqa: E501
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
        if issubclass(DtoProjectGroupResponse, dict):
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
        if not isinstance(other, DtoProjectGroupResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DtoProjectGroupResponse):
            return True

        return self.to_dict() != other.to_dict()
