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


class ModelsOrganizationUserSimple:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"avatar_url": "str", "joined": "bool", "name": "str", "user_id": "int"}

    attribute_map = {"avatar_url": "avatar_url", "joined": "joined", "name": "name", "user_id": "user_id"}

    def __init__(self, avatar_url=None, joined=None, name=None, user_id=None, _configuration=None):  # noqa: E501
        """ModelsOrganizationUserSimple - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._avatar_url = None
        self._joined = None
        self._name = None
        self._user_id = None
        self.discriminator = None

        if avatar_url is not None:
            self.avatar_url = avatar_url
        if joined is not None:
            self.joined = joined
        if name is not None:
            self.name = name
        if user_id is not None:
            self.user_id = user_id

    @property
    def avatar_url(self):
        """Gets the avatar_url of this ModelsOrganizationUserSimple.  # noqa: E501


        :return: The avatar_url of this ModelsOrganizationUserSimple.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this ModelsOrganizationUserSimple.


        :param avatar_url: The avatar_url of this ModelsOrganizationUserSimple.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def joined(self):
        """Gets the joined of this ModelsOrganizationUserSimple.  # noqa: E501


        :return: The joined of this ModelsOrganizationUserSimple.  # noqa: E501
        :rtype: bool
        """
        return self._joined

    @joined.setter
    def joined(self, joined):
        """Sets the joined of this ModelsOrganizationUserSimple.


        :param joined: The joined of this ModelsOrganizationUserSimple.  # noqa: E501
        :type: bool
        """

        self._joined = joined

    @property
    def name(self):
        """Gets the name of this ModelsOrganizationUserSimple.  # noqa: E501


        :return: The name of this ModelsOrganizationUserSimple.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelsOrganizationUserSimple.


        :param name: The name of this ModelsOrganizationUserSimple.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def user_id(self):
        """Gets the user_id of this ModelsOrganizationUserSimple.  # noqa: E501


        :return: The user_id of this ModelsOrganizationUserSimple.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ModelsOrganizationUserSimple.


        :param user_id: The user_id of this ModelsOrganizationUserSimple.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

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
        if issubclass(ModelsOrganizationUserSimple, dict):
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
        if not isinstance(other, ModelsOrganizationUserSimple):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsOrganizationUserSimple):
            return True

        return self.to_dict() != other.to_dict()
