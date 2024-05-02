"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import pprint
import re  # noqa: F401
from datetime import datetime  # noqa: F401
from typing import Any

from toggl.configuration import Configuration
from toggl.models.models_goal_cadence import ModelsGoalCadence  # noqa: F401
from toggl.models.models_goal_type import ModelsGoalType  # noqa: F401


class ModelsPlainGoal:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "archived": "bool",
        "archived_at": "str",
        "cadence_period": "str",
        "comparing": "str",
        "current_cadence": "ModelsGoalCadence",
        "description": "str",
        "end": "str",
        "goal_id": "int",
        "goal_parameter_id": "int",
        "goal_type": "ModelsGoalType",
        "icon": "int",
        "icon_color": "str",
        "name": "str",
        "start": "str",
        "target_value": "int",
        "type_name": "str",
        "user_id": "int",
        "workspace_id": "int",
    }

    attribute_map = {
        "archived": "archived",
        "archived_at": "archived_at",
        "cadence_period": "cadence_period",
        "comparing": "comparing",
        "current_cadence": "current_cadence",
        "description": "description",
        "end": "end",
        "goal_id": "goal_id",
        "goal_parameter_id": "goal_parameter_id",
        "goal_type": "goal_type",
        "icon": "icon",
        "icon_color": "icon_color",
        "name": "name",
        "start": "start",
        "target_value": "target_value",
        "type_name": "type_name",
        "user_id": "user_id",
        "workspace_id": "workspace_id",
    }

    def __init__(
        self,
        archived: bool = None,
        archived_at: str = None,
        cadence_period: str = None,
        comparing: str = None,
        current_cadence: ModelsGoalCadence = None,
        description: str = None,
        end: str = None,
        goal_id: int = None,
        goal_parameter_id: int = None,
        goal_type: ModelsGoalType = None,
        icon: int = None,
        icon_color: str = None,
        name: str = None,
        start: str = None,
        target_value: int = None,
        type_name: str = None,
        user_id: int = None,
        workspace_id: int = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        ModelsPlainGoal - a model defined in Swagger

        Parameters:
          archived (bool): Optional
          archived_at (str): Optional
          cadence_period (str): Optional
          comparing (str): Optional
          current_cadence (ModelsGoalCadence): Optional
          description (str): Optional
          end (str): Optional
          goal_id (int): Optional
          goal_parameter_id (int): Optional
          goal_type (ModelsGoalType): Optional
          icon (int): Optional
          icon_color (str): Optional
          name (str): Optional
          start (str): Optional
          target_value (int): Optional
          type_name (str): Optional
          user_id (int): Optional
          workspace_id (int): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._archived = None
        self._archived_at = None
        self._cadence_period = None
        self._comparing = None
        self._current_cadence = None
        self._description = None
        self._end = None
        self._goal_id = None
        self._goal_parameter_id = None
        self._goal_type = None
        self._icon = None
        self._icon_color = None
        self._name = None
        self._start = None
        self._target_value = None
        self._type_name = None
        self._user_id = None
        self._workspace_id = None
        self.discriminator = None

        if archived is not None:
            self.archived = archived
        if archived_at is not None:
            self.archived_at = archived_at
        if cadence_period is not None:
            self.cadence_period = cadence_period
        if comparing is not None:
            self.comparing = comparing
        if current_cadence is not None:
            self.current_cadence = current_cadence
        if description is not None:
            self.description = description
        if end is not None:
            self.end = end
        if goal_id is not None:
            self.goal_id = goal_id
        if goal_parameter_id is not None:
            self.goal_parameter_id = goal_parameter_id
        if goal_type is not None:
            self.goal_type = goal_type
        if icon is not None:
            self.icon = icon
        if icon_color is not None:
            self.icon_color = icon_color
        if name is not None:
            self.name = name
        if start is not None:
            self.start = start
        if target_value is not None:
            self.target_value = target_value
        if type_name is not None:
            self.type_name = type_name
        if user_id is not None:
            self.user_id = user_id
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def archived(self) -> bool:
        """Gets the archived of this ModelsPlainGoal.  # noqa: E501


        :return: The archived of this ModelsPlainGoal.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived: bool):
        """Sets the archived of this ModelsPlainGoal.


        :param archived: The archived of this ModelsPlainGoal.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def archived_at(self) -> str:
        """Gets the archived_at of this ModelsPlainGoal.  # noqa: E501


        :return: The archived_at of this ModelsPlainGoal.  # noqa: E501
        :rtype: str
        """
        return self._archived_at

    @archived_at.setter
    def archived_at(self, archived_at: str):
        """Sets the archived_at of this ModelsPlainGoal.


        :param archived_at: The archived_at of this ModelsPlainGoal.  # noqa: E501
        :type: str
        """

        self._archived_at = archived_at

    @property
    def cadence_period(self) -> str:
        """Gets the cadence_period of this ModelsPlainGoal.  # noqa: E501


        :return: The cadence_period of this ModelsPlainGoal.  # noqa: E501
        :rtype: str
        """
        return self._cadence_period

    @cadence_period.setter
    def cadence_period(self, cadence_period: str):
        """Sets the cadence_period of this ModelsPlainGoal.


        :param cadence_period: The cadence_period of this ModelsPlainGoal.  # noqa: E501
        :type: str
        """

        self._cadence_period = cadence_period

    @property
    def comparing(self) -> str:
        """Gets the comparing of this ModelsPlainGoal.  # noqa: E501


        :return: The comparing of this ModelsPlainGoal.  # noqa: E501
        :rtype: str
        """
        return self._comparing

    @comparing.setter
    def comparing(self, comparing: str):
        """Sets the comparing of this ModelsPlainGoal.


        :param comparing: The comparing of this ModelsPlainGoal.  # noqa: E501
        :type: str
        """

        self._comparing = comparing

    @property
    def current_cadence(self) -> ModelsGoalCadence:
        """Gets the current_cadence of this ModelsPlainGoal.  # noqa: E501


        :return: The current_cadence of this ModelsPlainGoal.  # noqa: E501
        :rtype: ModelsGoalCadence
        """
        return self._current_cadence

    @current_cadence.setter
    def current_cadence(self, current_cadence: ModelsGoalCadence):
        """Sets the current_cadence of this ModelsPlainGoal.


        :param current_cadence: The current_cadence of this ModelsPlainGoal.  # noqa: E501
        :type: ModelsGoalCadence
        """

        self._current_cadence = current_cadence

    @property
    def description(self) -> str:
        """Gets the description of this ModelsPlainGoal.  # noqa: E501


        :return: The description of this ModelsPlainGoal.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this ModelsPlainGoal.


        :param description: The description of this ModelsPlainGoal.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def end(self) -> str:
        """Gets the end of this ModelsPlainGoal.  # noqa: E501


        :return: The end of this ModelsPlainGoal.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end: str):
        """Sets the end of this ModelsPlainGoal.


        :param end: The end of this ModelsPlainGoal.  # noqa: E501
        :type: str
        """

        self._end = end

    @property
    def goal_id(self) -> int:
        """Gets the goal_id of this ModelsPlainGoal.  # noqa: E501


        :return: The goal_id of this ModelsPlainGoal.  # noqa: E501
        :rtype: int
        """
        return self._goal_id

    @goal_id.setter
    def goal_id(self, goal_id: int):
        """Sets the goal_id of this ModelsPlainGoal.


        :param goal_id: The goal_id of this ModelsPlainGoal.  # noqa: E501
        :type: int
        """

        self._goal_id = goal_id

    @property
    def goal_parameter_id(self) -> int:
        """Gets the goal_parameter_id of this ModelsPlainGoal.  # noqa: E501


        :return: The goal_parameter_id of this ModelsPlainGoal.  # noqa: E501
        :rtype: int
        """
        return self._goal_parameter_id

    @goal_parameter_id.setter
    def goal_parameter_id(self, goal_parameter_id: int):
        """Sets the goal_parameter_id of this ModelsPlainGoal.


        :param goal_parameter_id: The goal_parameter_id of this ModelsPlainGoal.  # noqa: E501
        :type: int
        """

        self._goal_parameter_id = goal_parameter_id

    @property
    def goal_type(self) -> ModelsGoalType:
        """Gets the goal_type of this ModelsPlainGoal.  # noqa: E501


        :return: The goal_type of this ModelsPlainGoal.  # noqa: E501
        :rtype: ModelsGoalType
        """
        return self._goal_type

    @goal_type.setter
    def goal_type(self, goal_type: ModelsGoalType):
        """Sets the goal_type of this ModelsPlainGoal.


        :param goal_type: The goal_type of this ModelsPlainGoal.  # noqa: E501
        :type: ModelsGoalType
        """

        self._goal_type = goal_type

    @property
    def icon(self) -> int:
        """Gets the icon of this ModelsPlainGoal.  # noqa: E501


        :return: The icon of this ModelsPlainGoal.  # noqa: E501
        :rtype: int
        """
        return self._icon

    @icon.setter
    def icon(self, icon: int):
        """Sets the icon of this ModelsPlainGoal.


        :param icon: The icon of this ModelsPlainGoal.  # noqa: E501
        :type: int
        """

        self._icon = icon

    @property
    def icon_color(self) -> str:
        """Gets the icon_color of this ModelsPlainGoal.  # noqa: E501


        :return: The icon_color of this ModelsPlainGoal.  # noqa: E501
        :rtype: str
        """
        return self._icon_color

    @icon_color.setter
    def icon_color(self, icon_color: str):
        """Sets the icon_color of this ModelsPlainGoal.


        :param icon_color: The icon_color of this ModelsPlainGoal.  # noqa: E501
        :type: str
        """

        self._icon_color = icon_color

    @property
    def name(self) -> str:
        """Gets the name of this ModelsPlainGoal.  # noqa: E501


        :return: The name of this ModelsPlainGoal.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ModelsPlainGoal.


        :param name: The name of this ModelsPlainGoal.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def start(self) -> str:
        """Gets the start of this ModelsPlainGoal.  # noqa: E501


        :return: The start of this ModelsPlainGoal.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start: str):
        """Sets the start of this ModelsPlainGoal.


        :param start: The start of this ModelsPlainGoal.  # noqa: E501
        :type: str
        """

        self._start = start

    @property
    def target_value(self) -> int:
        """Gets the target_value of this ModelsPlainGoal.  # noqa: E501


        :return: The target_value of this ModelsPlainGoal.  # noqa: E501
        :rtype: int
        """
        return self._target_value

    @target_value.setter
    def target_value(self, target_value: int):
        """Sets the target_value of this ModelsPlainGoal.


        :param target_value: The target_value of this ModelsPlainGoal.  # noqa: E501
        :type: int
        """

        self._target_value = target_value

    @property
    def type_name(self) -> str:
        """Gets the type_name of this ModelsPlainGoal.  # noqa: E501


        :return: The type_name of this ModelsPlainGoal.  # noqa: E501
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name: str):
        """Sets the type_name of this ModelsPlainGoal.


        :param type_name: The type_name of this ModelsPlainGoal.  # noqa: E501
        :type: str
        """

        self._type_name = type_name

    @property
    def user_id(self) -> int:
        """Gets the user_id of this ModelsPlainGoal.  # noqa: E501


        :return: The user_id of this ModelsPlainGoal.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this ModelsPlainGoal.


        :param user_id: The user_id of this ModelsPlainGoal.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def workspace_id(self) -> int:
        """Gets the workspace_id of this ModelsPlainGoal.  # noqa: E501


        :return: The workspace_id of this ModelsPlainGoal.  # noqa: E501
        :rtype: int
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id: int):
        """Sets the workspace_id of this ModelsPlainGoal.


        :param workspace_id: The workspace_id of this ModelsPlainGoal.  # noqa: E501
        :type: int
        """

        self._workspace_id = workspace_id

    def to_dict(self) -> dict[str, Any]:
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
        if issubclass(ModelsPlainGoal, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModelsPlainGoal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsPlainGoal):
            return True

        return self.to_dict() != other.to_dict()
