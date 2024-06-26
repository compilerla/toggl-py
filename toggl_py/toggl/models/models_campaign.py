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


class ModelsCampaign:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"discount": "int", "end": "str", "key": "str", "name": "str", "start": "str"}

    attribute_map = {"discount": "discount", "end": "end", "key": "key", "name": "name", "start": "start"}

    def __init__(self, discount=None, end=None, key=None, name=None, start=None, _configuration=None):  # noqa: E501
        """ModelsCampaign - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._discount = None
        self._end = None
        self._key = None
        self._name = None
        self._start = None
        self.discriminator = None

        if discount is not None:
            self.discount = discount
        if end is not None:
            self.end = end
        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if start is not None:
            self.start = start

    @property
    def discount(self):
        """Gets the discount of this ModelsCampaign.  # noqa: E501


        :return: The discount of this ModelsCampaign.  # noqa: E501
        :rtype: int
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this ModelsCampaign.


        :param discount: The discount of this ModelsCampaign.  # noqa: E501
        :type: int
        """

        self._discount = discount

    @property
    def end(self):
        """Gets the end of this ModelsCampaign.  # noqa: E501


        :return: The end of this ModelsCampaign.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this ModelsCampaign.


        :param end: The end of this ModelsCampaign.  # noqa: E501
        :type: str
        """

        self._end = end

    @property
    def key(self):
        """Gets the key of this ModelsCampaign.  # noqa: E501


        :return: The key of this ModelsCampaign.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ModelsCampaign.


        :param key: The key of this ModelsCampaign.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this ModelsCampaign.  # noqa: E501


        :return: The name of this ModelsCampaign.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelsCampaign.


        :param name: The name of this ModelsCampaign.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def start(self):
        """Gets the start of this ModelsCampaign.  # noqa: E501


        :return: The start of this ModelsCampaign.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ModelsCampaign.


        :param start: The start of this ModelsCampaign.  # noqa: E501
        :type: str
        """

        self._start = start

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
        if issubclass(ModelsCampaign, dict):
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
        if not isinstance(other, ModelsCampaign):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsCampaign):
            return True

        return self.to_dict() != other.to_dict()
