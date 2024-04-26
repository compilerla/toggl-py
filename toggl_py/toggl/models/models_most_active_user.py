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


class ModelsMostActiveUser:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"duration": "int", "user_id": "int"}

    attribute_map = {"duration": "duration", "user_id": "user_id"}

    def __init__(self, duration=None, user_id=None, _configuration=None):  # noqa: E501
        """ModelsMostActiveUser - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._duration = None
        self._user_id = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if user_id is not None:
            self.user_id = user_id

    @property
    def duration(self):
        """Gets the duration of this ModelsMostActiveUser.  # noqa: E501


        :return: The duration of this ModelsMostActiveUser.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ModelsMostActiveUser.


        :param duration: The duration of this ModelsMostActiveUser.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def user_id(self):
        """Gets the user_id of this ModelsMostActiveUser.  # noqa: E501


        :return: The user_id of this ModelsMostActiveUser.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ModelsMostActiveUser.


        :param user_id: The user_id of this ModelsMostActiveUser.  # noqa: E501
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
        if issubclass(ModelsMostActiveUser, dict):
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
        if not isinstance(other, ModelsMostActiveUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsMostActiveUser):
            return True

        return self.to_dict() != other.to_dict()