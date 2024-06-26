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


class GoalsParamsCreate:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "cadence_period": "str",
        "comparing": "str",
        "description": "str",
        "end": "str",
        "goal_type": "ModelsGoalType",
        "icon": "int",
        "icon_color": "str",
        "name": "str",
        "start": "str",
        "target_value": "int",
        "workspace_id": "int",
    }

    attribute_map = {
        "cadence_period": "cadence_period",
        "comparing": "comparing",
        "description": "description",
        "end": "end",
        "goal_type": "goal_type",
        "icon": "icon",
        "icon_color": "icon_color",
        "name": "name",
        "start": "start",
        "target_value": "target_value",
        "workspace_id": "workspace_id",
    }

    def __init__(
        self,
        cadence_period=None,
        comparing=None,
        description=None,
        end=None,
        goal_type=None,
        icon=None,
        icon_color=None,
        name=None,
        start=None,
        target_value=None,
        workspace_id=None,
        _configuration=None,
    ):  # noqa: E501
        """GoalsParamsCreate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cadence_period = None
        self._comparing = None
        self._description = None
        self._end = None
        self._goal_type = None
        self._icon = None
        self._icon_color = None
        self._name = None
        self._start = None
        self._target_value = None
        self._workspace_id = None
        self.discriminator = None

        self.cadence_period = cadence_period
        self.comparing = comparing
        if description is not None:
            self.description = description
        if end is not None:
            self.end = end
        self.goal_type = goal_type
        if icon is not None:
            self.icon = icon
        if icon_color is not None:
            self.icon_color = icon_color
        self.name = name
        self.start = start
        self.target_value = target_value
        self.workspace_id = workspace_id

    @property
    def cadence_period(self):
        """Gets the cadence_period of this GoalsParamsCreate.  # noqa: E501


        :return: The cadence_period of this GoalsParamsCreate.  # noqa: E501
        :rtype: str
        """
        return self._cadence_period

    @cadence_period.setter
    def cadence_period(self, cadence_period):
        """Sets the cadence_period of this GoalsParamsCreate.


        :param cadence_period: The cadence_period of this GoalsParamsCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cadence_period is None:
            raise ValueError("Invalid value for `cadence_period`, must not be `None`")  # noqa: E501

        self._cadence_period = cadence_period

    @property
    def comparing(self):
        """Gets the comparing of this GoalsParamsCreate.  # noqa: E501


        :return: The comparing of this GoalsParamsCreate.  # noqa: E501
        :rtype: str
        """
        return self._comparing

    @comparing.setter
    def comparing(self, comparing):
        """Sets the comparing of this GoalsParamsCreate.


        :param comparing: The comparing of this GoalsParamsCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and comparing is None:
            raise ValueError("Invalid value for `comparing`, must not be `None`")  # noqa: E501

        self._comparing = comparing

    @property
    def description(self):
        """Gets the description of this GoalsParamsCreate.  # noqa: E501


        :return: The description of this GoalsParamsCreate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GoalsParamsCreate.


        :param description: The description of this GoalsParamsCreate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def end(self):
        """Gets the end of this GoalsParamsCreate.  # noqa: E501


        :return: The end of this GoalsParamsCreate.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this GoalsParamsCreate.


        :param end: The end of this GoalsParamsCreate.  # noqa: E501
        :type: str
        """

        self._end = end

    @property
    def goal_type(self):
        """Gets the goal_type of this GoalsParamsCreate.  # noqa: E501


        :return: The goal_type of this GoalsParamsCreate.  # noqa: E501
        :rtype: ModelsGoalType
        """
        return self._goal_type

    @goal_type.setter
    def goal_type(self, goal_type):
        """Sets the goal_type of this GoalsParamsCreate.


        :param goal_type: The goal_type of this GoalsParamsCreate.  # noqa: E501
        :type: ModelsGoalType
        """
        if self._configuration.client_side_validation and goal_type is None:
            raise ValueError("Invalid value for `goal_type`, must not be `None`")  # noqa: E501

        self._goal_type = goal_type

    @property
    def icon(self):
        """Gets the icon of this GoalsParamsCreate.  # noqa: E501


        :return: The icon of this GoalsParamsCreate.  # noqa: E501
        :rtype: int
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this GoalsParamsCreate.


        :param icon: The icon of this GoalsParamsCreate.  # noqa: E501
        :type: int
        """

        self._icon = icon

    @property
    def icon_color(self):
        """Gets the icon_color of this GoalsParamsCreate.  # noqa: E501


        :return: The icon_color of this GoalsParamsCreate.  # noqa: E501
        :rtype: str
        """
        return self._icon_color

    @icon_color.setter
    def icon_color(self, icon_color):
        """Sets the icon_color of this GoalsParamsCreate.


        :param icon_color: The icon_color of this GoalsParamsCreate.  # noqa: E501
        :type: str
        """

        self._icon_color = icon_color

    @property
    def name(self):
        """Gets the name of this GoalsParamsCreate.  # noqa: E501


        :return: The name of this GoalsParamsCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GoalsParamsCreate.


        :param name: The name of this GoalsParamsCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def start(self):
        """Gets the start of this GoalsParamsCreate.  # noqa: E501


        :return: The start of this GoalsParamsCreate.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this GoalsParamsCreate.


        :param start: The start of this GoalsParamsCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def target_value(self):
        """Gets the target_value of this GoalsParamsCreate.  # noqa: E501


        :return: The target_value of this GoalsParamsCreate.  # noqa: E501
        :rtype: int
        """
        return self._target_value

    @target_value.setter
    def target_value(self, target_value):
        """Sets the target_value of this GoalsParamsCreate.


        :param target_value: The target_value of this GoalsParamsCreate.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and target_value is None:
            raise ValueError("Invalid value for `target_value`, must not be `None`")  # noqa: E501

        self._target_value = target_value

    @property
    def workspace_id(self):
        """Gets the workspace_id of this GoalsParamsCreate.  # noqa: E501


        :return: The workspace_id of this GoalsParamsCreate.  # noqa: E501
        :rtype: int
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this GoalsParamsCreate.


        :param workspace_id: The workspace_id of this GoalsParamsCreate.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and workspace_id is None:
            raise ValueError("Invalid value for `workspace_id`, must not be `None`")  # noqa: E501

        self._workspace_id = workspace_id

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
        if issubclass(GoalsParamsCreate, dict):
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
        if not isinstance(other, GoalsParamsCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GoalsParamsCreate):
            return True

        return self.to_dict() != other.to_dict()
