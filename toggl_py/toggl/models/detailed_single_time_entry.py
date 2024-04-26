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


class DetailedSingleTimeEntry:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"at": "str", "id": "int", "seconds": "int", "start": "str", "stop": "str"}

    attribute_map = {"at": "at", "id": "id", "seconds": "seconds", "start": "start", "stop": "stop"}

    def __init__(self, at=None, id=None, seconds=None, start=None, stop=None, _configuration=None):  # noqa: E501
        """DetailedSingleTimeEntry - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._at = None
        self._id = None
        self._seconds = None
        self._start = None
        self._stop = None
        self.discriminator = None

        if at is not None:
            self.at = at
        if id is not None:
            self.id = id
        if seconds is not None:
            self.seconds = seconds
        if start is not None:
            self.start = start
        if stop is not None:
            self.stop = stop

    @property
    def at(self):
        """Gets the at of this DetailedSingleTimeEntry.  # noqa: E501


        :return: The at of this DetailedSingleTimeEntry.  # noqa: E501
        :rtype: str
        """
        return self._at

    @at.setter
    def at(self, at):
        """Sets the at of this DetailedSingleTimeEntry.


        :param at: The at of this DetailedSingleTimeEntry.  # noqa: E501
        :type: str
        """

        self._at = at

    @property
    def id(self):
        """Gets the id of this DetailedSingleTimeEntry.  # noqa: E501


        :return: The id of this DetailedSingleTimeEntry.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DetailedSingleTimeEntry.


        :param id: The id of this DetailedSingleTimeEntry.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def seconds(self):
        """Gets the seconds of this DetailedSingleTimeEntry.  # noqa: E501


        :return: The seconds of this DetailedSingleTimeEntry.  # noqa: E501
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        """Sets the seconds of this DetailedSingleTimeEntry.


        :param seconds: The seconds of this DetailedSingleTimeEntry.  # noqa: E501
        :type: int
        """

        self._seconds = seconds

    @property
    def start(self):
        """Gets the start of this DetailedSingleTimeEntry.  # noqa: E501


        :return: The start of this DetailedSingleTimeEntry.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this DetailedSingleTimeEntry.


        :param start: The start of this DetailedSingleTimeEntry.  # noqa: E501
        :type: str
        """

        self._start = start

    @property
    def stop(self):
        """Gets the stop of this DetailedSingleTimeEntry.  # noqa: E501


        :return: The stop of this DetailedSingleTimeEntry.  # noqa: E501
        :rtype: str
        """
        return self._stop

    @stop.setter
    def stop(self, stop):
        """Sets the stop of this DetailedSingleTimeEntry.


        :param stop: The stop of this DetailedSingleTimeEntry.  # noqa: E501
        :type: str
        """

        self._stop = stop

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
        if issubclass(DetailedSingleTimeEntry, dict):
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
        if not isinstance(other, DetailedSingleTimeEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DetailedSingleTimeEntry):
            return True

        return self.to_dict() != other.to_dict()
