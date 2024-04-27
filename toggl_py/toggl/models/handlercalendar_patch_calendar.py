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


class HandlercalendarPatchCalendar:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "default_planned_task_id": "int",
        "default_project_id": "int",
        "default_workspace_id": "int",
        "remind_tracking": "bool",
        "selected": "bool",
    }

    attribute_map = {
        "default_planned_task_id": "default_planned_task_id",
        "default_project_id": "default_project_id",
        "default_workspace_id": "default_workspace_id",
        "remind_tracking": "remind_tracking",
        "selected": "selected",
    }

    def __init__(
        self,
        default_planned_task_id=None,
        default_project_id=None,
        default_workspace_id=None,
        remind_tracking=None,
        selected=None,
        _configuration=None,
    ):  # noqa: E501
        """HandlercalendarPatchCalendar - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._default_planned_task_id = None
        self._default_project_id = None
        self._default_workspace_id = None
        self._remind_tracking = None
        self._selected = None
        self.discriminator = None

        if default_planned_task_id is not None:
            self.default_planned_task_id = default_planned_task_id
        if default_project_id is not None:
            self.default_project_id = default_project_id
        if default_workspace_id is not None:
            self.default_workspace_id = default_workspace_id
        if remind_tracking is not None:
            self.remind_tracking = remind_tracking
        if selected is not None:
            self.selected = selected

    @property
    def default_planned_task_id(self):
        """Gets the default_planned_task_id of this HandlercalendarPatchCalendar.  # noqa: E501


        :return: The default_planned_task_id of this HandlercalendarPatchCalendar.  # noqa: E501
        :rtype: int
        """
        return self._default_planned_task_id

    @default_planned_task_id.setter
    def default_planned_task_id(self, default_planned_task_id):
        """Sets the default_planned_task_id of this HandlercalendarPatchCalendar.


        :param default_planned_task_id: The default_planned_task_id of this HandlercalendarPatchCalendar.  # noqa: E501
        :type: int
        """

        self._default_planned_task_id = default_planned_task_id

    @property
    def default_project_id(self):
        """Gets the default_project_id of this HandlercalendarPatchCalendar.  # noqa: E501


        :return: The default_project_id of this HandlercalendarPatchCalendar.  # noqa: E501
        :rtype: int
        """
        return self._default_project_id

    @default_project_id.setter
    def default_project_id(self, default_project_id):
        """Sets the default_project_id of this HandlercalendarPatchCalendar.


        :param default_project_id: The default_project_id of this HandlercalendarPatchCalendar.  # noqa: E501
        :type: int
        """

        self._default_project_id = default_project_id

    @property
    def default_workspace_id(self):
        """Gets the default_workspace_id of this HandlercalendarPatchCalendar.  # noqa: E501


        :return: The default_workspace_id of this HandlercalendarPatchCalendar.  # noqa: E501
        :rtype: int
        """
        return self._default_workspace_id

    @default_workspace_id.setter
    def default_workspace_id(self, default_workspace_id):
        """Sets the default_workspace_id of this HandlercalendarPatchCalendar.


        :param default_workspace_id: The default_workspace_id of this HandlercalendarPatchCalendar.  # noqa: E501
        :type: int
        """

        self._default_workspace_id = default_workspace_id

    @property
    def remind_tracking(self):
        """Gets the remind_tracking of this HandlercalendarPatchCalendar.  # noqa: E501

        The following fields are deprecated but we need to keep them for backward compatibility with previous versions of mobile apps  # noqa: E501

        :return: The remind_tracking of this HandlercalendarPatchCalendar.  # noqa: E501
        :rtype: bool
        """
        return self._remind_tracking

    @remind_tracking.setter
    def remind_tracking(self, remind_tracking):
        """Sets the remind_tracking of this HandlercalendarPatchCalendar.

        The following fields are deprecated but we need to keep them for backward compatibility with previous versions of mobile apps  # noqa: E501

        :param remind_tracking: The remind_tracking of this HandlercalendarPatchCalendar.  # noqa: E501
        :type: bool
        """

        self._remind_tracking = remind_tracking

    @property
    def selected(self):
        """Gets the selected of this HandlercalendarPatchCalendar.  # noqa: E501


        :return: The selected of this HandlercalendarPatchCalendar.  # noqa: E501
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this HandlercalendarPatchCalendar.


        :param selected: The selected of this HandlercalendarPatchCalendar.  # noqa: E501
        :type: bool
        """

        self._selected = selected

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
        if issubclass(HandlercalendarPatchCalendar, dict):
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
        if not isinstance(other, HandlercalendarPatchCalendar):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HandlercalendarPatchCalendar):
            return True

        return self.to_dict() != other.to_dict()
