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


class DashboardAllActivities:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "description": "str",
        "duration": "int",
        "project_id": "int",
        "stop": "datetime",
        "tid": "int",
        "user_id": "int",
    }

    attribute_map = {
        "description": "description",
        "duration": "duration",
        "project_id": "project_id",
        "stop": "stop",
        "tid": "tid",
        "user_id": "user_id",
    }

    def __init__(
        self, description=None, duration=None, project_id=None, stop=None, tid=None, user_id=None, _configuration=None
    ):  # noqa: E501
        """DashboardAllActivities - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._duration = None
        self._project_id = None
        self._stop = None
        self._tid = None
        self._user_id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if duration is not None:
            self.duration = duration
        if project_id is not None:
            self.project_id = project_id
        if stop is not None:
            self.stop = stop
        if tid is not None:
            self.tid = tid
        if user_id is not None:
            self.user_id = user_id

    @property
    def description(self):
        """Gets the description of this DashboardAllActivities.  # noqa: E501


        :return: The description of this DashboardAllActivities.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DashboardAllActivities.


        :param description: The description of this DashboardAllActivities.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def duration(self):
        """Gets the duration of this DashboardAllActivities.  # noqa: E501


        :return: The duration of this DashboardAllActivities.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this DashboardAllActivities.


        :param duration: The duration of this DashboardAllActivities.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def project_id(self):
        """Gets the project_id of this DashboardAllActivities.  # noqa: E501


        :return: The project_id of this DashboardAllActivities.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DashboardAllActivities.


        :param project_id: The project_id of this DashboardAllActivities.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def stop(self):
        """Gets the stop of this DashboardAllActivities.  # noqa: E501


        :return: The stop of this DashboardAllActivities.  # noqa: E501
        :rtype: datetime
        """
        return self._stop

    @stop.setter
    def stop(self, stop):
        """Sets the stop of this DashboardAllActivities.


        :param stop: The stop of this DashboardAllActivities.  # noqa: E501
        :type: datetime
        """

        self._stop = stop

    @property
    def tid(self):
        """Gets the tid of this DashboardAllActivities.  # noqa: E501


        :return: The tid of this DashboardAllActivities.  # noqa: E501
        :rtype: int
        """
        return self._tid

    @tid.setter
    def tid(self, tid):
        """Sets the tid of this DashboardAllActivities.


        :param tid: The tid of this DashboardAllActivities.  # noqa: E501
        :type: int
        """

        self._tid = tid

    @property
    def user_id(self):
        """Gets the user_id of this DashboardAllActivities.  # noqa: E501


        :return: The user_id of this DashboardAllActivities.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this DashboardAllActivities.


        :param user_id: The user_id of this DashboardAllActivities.  # noqa: E501
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
        if issubclass(DashboardAllActivities, dict):
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
        if not isinstance(other, DashboardAllActivities):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DashboardAllActivities):
            return True

        return self.to_dict() != other.to_dict()
