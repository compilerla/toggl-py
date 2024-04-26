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


class ModelsRecurringPeriod:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"end_date": "str", "start_date": "str"}

    attribute_map = {"end_date": "end_date", "start_date": "start_date"}

    def __init__(self, end_date=None, start_date=None, _configuration=None):  # noqa: E501
        """ModelsRecurringPeriod - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._end_date = None
        self._start_date = None
        self.discriminator = None

        if end_date is not None:
            self.end_date = end_date
        if start_date is not None:
            self.start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ModelsRecurringPeriod.  # noqa: E501


        :return: The end_date of this ModelsRecurringPeriod.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ModelsRecurringPeriod.


        :param end_date: The end_date of this ModelsRecurringPeriod.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def start_date(self):
        """Gets the start_date of this ModelsRecurringPeriod.  # noqa: E501


        :return: The start_date of this ModelsRecurringPeriod.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ModelsRecurringPeriod.


        :param start_date: The start_date of this ModelsRecurringPeriod.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

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
        if issubclass(ModelsRecurringPeriod, dict):
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
        if not isinstance(other, ModelsRecurringPeriod):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsRecurringPeriod):
            return True

        return self.to_dict() != other.to_dict()