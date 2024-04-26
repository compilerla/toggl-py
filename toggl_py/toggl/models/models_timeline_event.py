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


class ModelsTimelineEvent:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "desktop_id": "str",
        "end_time": "int",
        "filename": "str",
        "id": "int",
        "idle": "bool",
        "start_time": "int",
        "title": "str",
    }

    attribute_map = {
        "desktop_id": "desktop_id",
        "end_time": "end_time",
        "filename": "filename",
        "id": "id",
        "idle": "idle",
        "start_time": "start_time",
        "title": "title",
    }

    def __init__(
        self,
        desktop_id=None,
        end_time=None,
        filename=None,
        id=None,
        idle=None,
        start_time=None,
        title=None,
        _configuration=None,
    ):  # noqa: E501
        """ModelsTimelineEvent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._desktop_id = None
        self._end_time = None
        self._filename = None
        self._id = None
        self._idle = None
        self._start_time = None
        self._title = None
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if end_time is not None:
            self.end_time = end_time
        if filename is not None:
            self.filename = filename
        if id is not None:
            self.id = id
        if idle is not None:
            self.idle = idle
        if start_time is not None:
            self.start_time = start_time
        if title is not None:
            self.title = title

    @property
    def desktop_id(self):
        """Gets the desktop_id of this ModelsTimelineEvent.  # noqa: E501


        :return: The desktop_id of this ModelsTimelineEvent.  # noqa: E501
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this ModelsTimelineEvent.


        :param desktop_id: The desktop_id of this ModelsTimelineEvent.  # noqa: E501
        :type: str
        """

        self._desktop_id = desktop_id

    @property
    def end_time(self):
        """Gets the end_time of this ModelsTimelineEvent.  # noqa: E501


        :return: The end_time of this ModelsTimelineEvent.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ModelsTimelineEvent.


        :param end_time: The end_time of this ModelsTimelineEvent.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def filename(self):
        """Gets the filename of this ModelsTimelineEvent.  # noqa: E501


        :return: The filename of this ModelsTimelineEvent.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this ModelsTimelineEvent.


        :param filename: The filename of this ModelsTimelineEvent.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def id(self):
        """Gets the id of this ModelsTimelineEvent.  # noqa: E501


        :return: The id of this ModelsTimelineEvent.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelsTimelineEvent.


        :param id: The id of this ModelsTimelineEvent.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def idle(self):
        """Gets the idle of this ModelsTimelineEvent.  # noqa: E501


        :return: The idle of this ModelsTimelineEvent.  # noqa: E501
        :rtype: bool
        """
        return self._idle

    @idle.setter
    def idle(self, idle):
        """Sets the idle of this ModelsTimelineEvent.


        :param idle: The idle of this ModelsTimelineEvent.  # noqa: E501
        :type: bool
        """

        self._idle = idle

    @property
    def start_time(self):
        """Gets the start_time of this ModelsTimelineEvent.  # noqa: E501


        :return: The start_time of this ModelsTimelineEvent.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ModelsTimelineEvent.


        :param start_time: The start_time of this ModelsTimelineEvent.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def title(self):
        """Gets the title of this ModelsTimelineEvent.  # noqa: E501


        :return: The title of this ModelsTimelineEvent.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ModelsTimelineEvent.


        :param title: The title of this ModelsTimelineEvent.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(ModelsTimelineEvent, dict):
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
        if not isinstance(other, ModelsTimelineEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsTimelineEvent):
            return True

        return self.to_dict() != other.to_dict()
