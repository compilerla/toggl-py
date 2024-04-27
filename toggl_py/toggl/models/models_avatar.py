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


class ModelsAvatar:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"avatar_urls": "ModelsImageURLs", "file_type": "str", "name": "str"}

    attribute_map = {"avatar_urls": "avatar_urls", "file_type": "fileType", "name": "name"}

    def __init__(self, avatar_urls=None, file_type=None, name=None, _configuration=None):  # noqa: E501
        """ModelsAvatar - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._avatar_urls = None
        self._file_type = None
        self._name = None
        self.discriminator = None

        if avatar_urls is not None:
            self.avatar_urls = avatar_urls
        if file_type is not None:
            self.file_type = file_type
        if name is not None:
            self.name = name

    @property
    def avatar_urls(self):
        """Gets the avatar_urls of this ModelsAvatar.  # noqa: E501


        :return: The avatar_urls of this ModelsAvatar.  # noqa: E501
        :rtype: ModelsImageURLs
        """
        return self._avatar_urls

    @avatar_urls.setter
    def avatar_urls(self, avatar_urls):
        """Sets the avatar_urls of this ModelsAvatar.


        :param avatar_urls: The avatar_urls of this ModelsAvatar.  # noqa: E501
        :type: ModelsImageURLs
        """

        self._avatar_urls = avatar_urls

    @property
    def file_type(self):
        """Gets the file_type of this ModelsAvatar.  # noqa: E501


        :return: The file_type of this ModelsAvatar.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this ModelsAvatar.


        :param file_type: The file_type of this ModelsAvatar.  # noqa: E501
        :type: str
        """

        self._file_type = file_type

    @property
    def name(self):
        """Gets the name of this ModelsAvatar.  # noqa: E501


        :return: The name of this ModelsAvatar.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelsAvatar.


        :param name: The name of this ModelsAvatar.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(ModelsAvatar, dict):
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
        if not isinstance(other, ModelsAvatar):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsAvatar):
            return True

        return self.to_dict() != other.to_dict()
