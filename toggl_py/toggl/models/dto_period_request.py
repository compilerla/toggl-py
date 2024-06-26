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


class DtoPeriodRequest:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"_from": "str", "preset": "str", "to": "str"}

    attribute_map = {"_from": "from", "preset": "preset", "to": "to"}

    def __init__(self, _from=None, preset=None, to=None, _configuration=None):  # noqa: E501
        """DtoPeriodRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self.__from = None
        self._preset = None
        self._to = None
        self.discriminator = None

        if _from is not None:
            self._from = _from
        if preset is not None:
            self.preset = preset
        if to is not None:
            self.to = to

    @property
    def _from(self):
        """Gets the _from of this DtoPeriodRequest.  # noqa: E501


        :return: The _from of this DtoPeriodRequest.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this DtoPeriodRequest.


        :param _from: The _from of this DtoPeriodRequest.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def preset(self):
        """Gets the preset of this DtoPeriodRequest.  # noqa: E501


        :return: The preset of this DtoPeriodRequest.  # noqa: E501
        :rtype: str
        """
        return self._preset

    @preset.setter
    def preset(self, preset):
        """Sets the preset of this DtoPeriodRequest.


        :param preset: The preset of this DtoPeriodRequest.  # noqa: E501
        :type: str
        """

        self._preset = preset

    @property
    def to(self):
        """Gets the to of this DtoPeriodRequest.  # noqa: E501


        :return: The to of this DtoPeriodRequest.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this DtoPeriodRequest.


        :param to: The to of this DtoPeriodRequest.  # noqa: E501
        :type: str
        """

        self._to = to

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
        if issubclass(DtoPeriodRequest, dict):
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
        if not isinstance(other, DtoPeriodRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DtoPeriodRequest):
            return True

        return self.to_dict() != other.to_dict()
