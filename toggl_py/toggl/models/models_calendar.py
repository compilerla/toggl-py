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


class ModelsCalendar:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "background_color": "str",
        "calendar_id": "int",
        "calendar_integration_id": "int",
        "created_at": "str",
        "default_planned_task_id": "int",
        "default_project_id": "int",
        "default_workspace_id": "int",
        "deleted_at": "str",
        "external_id": "str",
        "foreground_color": "str",
        "name": "str",
        "remind_tracking": "bool",
        "selected": "bool",
        "updated_at": "str",
    }

    attribute_map = {
        "background_color": "background_color",
        "calendar_id": "calendar_id",
        "calendar_integration_id": "calendar_integration_id",
        "created_at": "created_at",
        "default_planned_task_id": "default_planned_task_id",
        "default_project_id": "default_project_id",
        "default_workspace_id": "default_workspace_id",
        "deleted_at": "deleted_at",
        "external_id": "external_id",
        "foreground_color": "foreground_color",
        "name": "name",
        "remind_tracking": "remind_tracking",
        "selected": "selected",
        "updated_at": "updated_at",
    }

    def __init__(
        self,
        background_color=None,
        calendar_id=None,
        calendar_integration_id=None,
        created_at=None,
        default_planned_task_id=None,
        default_project_id=None,
        default_workspace_id=None,
        deleted_at=None,
        external_id=None,
        foreground_color=None,
        name=None,
        remind_tracking=None,
        selected=None,
        updated_at=None,
        _configuration=None,
    ):  # noqa: E501
        """ModelsCalendar - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._background_color = None
        self._calendar_id = None
        self._calendar_integration_id = None
        self._created_at = None
        self._default_planned_task_id = None
        self._default_project_id = None
        self._default_workspace_id = None
        self._deleted_at = None
        self._external_id = None
        self._foreground_color = None
        self._name = None
        self._remind_tracking = None
        self._selected = None
        self._updated_at = None
        self.discriminator = None

        if background_color is not None:
            self.background_color = background_color
        if calendar_id is not None:
            self.calendar_id = calendar_id
        if calendar_integration_id is not None:
            self.calendar_integration_id = calendar_integration_id
        if created_at is not None:
            self.created_at = created_at
        if default_planned_task_id is not None:
            self.default_planned_task_id = default_planned_task_id
        if default_project_id is not None:
            self.default_project_id = default_project_id
        if default_workspace_id is not None:
            self.default_workspace_id = default_workspace_id
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if external_id is not None:
            self.external_id = external_id
        if foreground_color is not None:
            self.foreground_color = foreground_color
        if name is not None:
            self.name = name
        if remind_tracking is not None:
            self.remind_tracking = remind_tracking
        if selected is not None:
            self.selected = selected
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def background_color(self):
        """Gets the background_color of this ModelsCalendar.  # noqa: E501


        :return: The background_color of this ModelsCalendar.  # noqa: E501
        :rtype: str
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this ModelsCalendar.


        :param background_color: The background_color of this ModelsCalendar.  # noqa: E501
        :type: str
        """

        self._background_color = background_color

    @property
    def calendar_id(self):
        """Gets the calendar_id of this ModelsCalendar.  # noqa: E501


        :return: The calendar_id of this ModelsCalendar.  # noqa: E501
        :rtype: int
        """
        return self._calendar_id

    @calendar_id.setter
    def calendar_id(self, calendar_id):
        """Sets the calendar_id of this ModelsCalendar.


        :param calendar_id: The calendar_id of this ModelsCalendar.  # noqa: E501
        :type: int
        """

        self._calendar_id = calendar_id

    @property
    def calendar_integration_id(self):
        """Gets the calendar_integration_id of this ModelsCalendar.  # noqa: E501


        :return: The calendar_integration_id of this ModelsCalendar.  # noqa: E501
        :rtype: int
        """
        return self._calendar_integration_id

    @calendar_integration_id.setter
    def calendar_integration_id(self, calendar_integration_id):
        """Sets the calendar_integration_id of this ModelsCalendar.


        :param calendar_integration_id: The calendar_integration_id of this ModelsCalendar.  # noqa: E501
        :type: int
        """

        self._calendar_integration_id = calendar_integration_id

    @property
    def created_at(self):
        """Gets the created_at of this ModelsCalendar.  # noqa: E501


        :return: The created_at of this ModelsCalendar.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ModelsCalendar.


        :param created_at: The created_at of this ModelsCalendar.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def default_planned_task_id(self):
        """Gets the default_planned_task_id of this ModelsCalendar.  # noqa: E501


        :return: The default_planned_task_id of this ModelsCalendar.  # noqa: E501
        :rtype: int
        """
        return self._default_planned_task_id

    @default_planned_task_id.setter
    def default_planned_task_id(self, default_planned_task_id):
        """Sets the default_planned_task_id of this ModelsCalendar.


        :param default_planned_task_id: The default_planned_task_id of this ModelsCalendar.  # noqa: E501
        :type: int
        """

        self._default_planned_task_id = default_planned_task_id

    @property
    def default_project_id(self):
        """Gets the default_project_id of this ModelsCalendar.  # noqa: E501


        :return: The default_project_id of this ModelsCalendar.  # noqa: E501
        :rtype: int
        """
        return self._default_project_id

    @default_project_id.setter
    def default_project_id(self, default_project_id):
        """Sets the default_project_id of this ModelsCalendar.


        :param default_project_id: The default_project_id of this ModelsCalendar.  # noqa: E501
        :type: int
        """

        self._default_project_id = default_project_id

    @property
    def default_workspace_id(self):
        """Gets the default_workspace_id of this ModelsCalendar.  # noqa: E501


        :return: The default_workspace_id of this ModelsCalendar.  # noqa: E501
        :rtype: int
        """
        return self._default_workspace_id

    @default_workspace_id.setter
    def default_workspace_id(self, default_workspace_id):
        """Sets the default_workspace_id of this ModelsCalendar.


        :param default_workspace_id: The default_workspace_id of this ModelsCalendar.  # noqa: E501
        :type: int
        """

        self._default_workspace_id = default_workspace_id

    @property
    def deleted_at(self):
        """Gets the deleted_at of this ModelsCalendar.  # noqa: E501


        :return: The deleted_at of this ModelsCalendar.  # noqa: E501
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this ModelsCalendar.


        :param deleted_at: The deleted_at of this ModelsCalendar.  # noqa: E501
        :type: str
        """

        self._deleted_at = deleted_at

    @property
    def external_id(self):
        """Gets the external_id of this ModelsCalendar.  # noqa: E501


        :return: The external_id of this ModelsCalendar.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this ModelsCalendar.


        :param external_id: The external_id of this ModelsCalendar.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def foreground_color(self):
        """Gets the foreground_color of this ModelsCalendar.  # noqa: E501


        :return: The foreground_color of this ModelsCalendar.  # noqa: E501
        :rtype: str
        """
        return self._foreground_color

    @foreground_color.setter
    def foreground_color(self, foreground_color):
        """Sets the foreground_color of this ModelsCalendar.


        :param foreground_color: The foreground_color of this ModelsCalendar.  # noqa: E501
        :type: str
        """

        self._foreground_color = foreground_color

    @property
    def name(self):
        """Gets the name of this ModelsCalendar.  # noqa: E501


        :return: The name of this ModelsCalendar.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelsCalendar.


        :param name: The name of this ModelsCalendar.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def remind_tracking(self):
        """Gets the remind_tracking of this ModelsCalendar.  # noqa: E501

        The following fields are deprecated but we need to keep them for backward compatibility with previous versions of mobile apps  # noqa: E501

        :return: The remind_tracking of this ModelsCalendar.  # noqa: E501
        :rtype: bool
        """
        return self._remind_tracking

    @remind_tracking.setter
    def remind_tracking(self, remind_tracking):
        """Sets the remind_tracking of this ModelsCalendar.

        The following fields are deprecated but we need to keep them for backward compatibility with previous versions of mobile apps  # noqa: E501

        :param remind_tracking: The remind_tracking of this ModelsCalendar.  # noqa: E501
        :type: bool
        """

        self._remind_tracking = remind_tracking

    @property
    def selected(self):
        """Gets the selected of this ModelsCalendar.  # noqa: E501


        :return: The selected of this ModelsCalendar.  # noqa: E501
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this ModelsCalendar.


        :param selected: The selected of this ModelsCalendar.  # noqa: E501
        :type: bool
        """

        self._selected = selected

    @property
    def updated_at(self):
        """Gets the updated_at of this ModelsCalendar.  # noqa: E501


        :return: The updated_at of this ModelsCalendar.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ModelsCalendar.


        :param updated_at: The updated_at of this ModelsCalendar.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(ModelsCalendar, dict):
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
        if not isinstance(other, ModelsCalendar):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsCalendar):
            return True

        return self.to_dict() != other.to_dict()
