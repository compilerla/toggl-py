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


class SubscriptionFeatureReturn:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"enabled": "bool", "id": "int", "name": "str"}

    attribute_map = {"enabled": "enabled", "id": "id", "name": "name"}

    def __init__(self, enabled=None, id=None, name=None, _configuration=None):  # noqa: E501
        """SubscriptionFeatureReturn - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enabled = None
        self._id = None
        self._name = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def enabled(self):
        """Gets the enabled of this SubscriptionFeatureReturn.  # noqa: E501


        :return: The enabled of this SubscriptionFeatureReturn.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SubscriptionFeatureReturn.


        :param enabled: The enabled of this SubscriptionFeatureReturn.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this SubscriptionFeatureReturn.  # noqa: E501


        :return: The id of this SubscriptionFeatureReturn.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionFeatureReturn.


        :param id: The id of this SubscriptionFeatureReturn.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SubscriptionFeatureReturn.  # noqa: E501


        :return: The name of this SubscriptionFeatureReturn.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionFeatureReturn.


        :param name: The name of this SubscriptionFeatureReturn.  # noqa: E501
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
        if issubclass(SubscriptionFeatureReturn, dict):
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
        if not isinstance(other, SubscriptionFeatureReturn):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionFeatureReturn):
            return True

        return self.to_dict() != other.to_dict()
