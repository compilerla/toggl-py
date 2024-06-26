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


class DictionaryReportUserDict:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"avatar_url": "str", "email": "str", "group_ids": "str", "id": "int", "name": "str"}

    attribute_map = {"avatar_url": "avatar_url", "email": "email", "group_ids": "group_ids", "id": "id", "name": "name"}

    def __init__(self, avatar_url=None, email=None, group_ids=None, id=None, name=None, _configuration=None):  # noqa: E501
        """DictionaryReportUserDict - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._avatar_url = None
        self._email = None
        self._group_ids = None
        self._id = None
        self._name = None
        self.discriminator = None

        if avatar_url is not None:
            self.avatar_url = avatar_url
        if email is not None:
            self.email = email
        if group_ids is not None:
            self.group_ids = group_ids
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def avatar_url(self):
        """Gets the avatar_url of this DictionaryReportUserDict.  # noqa: E501


        :return: The avatar_url of this DictionaryReportUserDict.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this DictionaryReportUserDict.


        :param avatar_url: The avatar_url of this DictionaryReportUserDict.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def email(self):
        """Gets the email of this DictionaryReportUserDict.  # noqa: E501


        :return: The email of this DictionaryReportUserDict.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this DictionaryReportUserDict.


        :param email: The email of this DictionaryReportUserDict.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def group_ids(self):
        """Gets the group_ids of this DictionaryReportUserDict.  # noqa: E501


        :return: The group_ids of this DictionaryReportUserDict.  # noqa: E501
        :rtype: str
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this DictionaryReportUserDict.


        :param group_ids: The group_ids of this DictionaryReportUserDict.  # noqa: E501
        :type: str
        """

        self._group_ids = group_ids

    @property
    def id(self):
        """Gets the id of this DictionaryReportUserDict.  # noqa: E501


        :return: The id of this DictionaryReportUserDict.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DictionaryReportUserDict.


        :param id: The id of this DictionaryReportUserDict.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DictionaryReportUserDict.  # noqa: E501


        :return: The name of this DictionaryReportUserDict.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DictionaryReportUserDict.


        :param name: The name of this DictionaryReportUserDict.  # noqa: E501
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
        if issubclass(DictionaryReportUserDict, dict):
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
        if not isinstance(other, DictionaryReportUserDict):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DictionaryReportUserDict):
            return True

        return self.to_dict() != other.to_dict()
