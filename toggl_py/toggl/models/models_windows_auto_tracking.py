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
from toggl.models.models_windows_auto_tracking_parameters import ModelsWindowsAutoTrackingParameters  # noqa: F401


class ModelsWindowsAutoTracking:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "description": "str",
        "enabled": "bool",
        "parameters": "ModelsWindowsAutoTrackingParameters",
        "project_id": "int",
        "skip_when_timer_is_running": "bool",
        "start_without_confirmation": "bool",
        "task_id": "int",
        "type": "int",
    }

    attribute_map = {
        "description": "description",
        "enabled": "enabled",
        "parameters": "parameters",
        "project_id": "project_id",
        "skip_when_timer_is_running": "skip_when_timer_is_running",
        "start_without_confirmation": "start_without_confirmation",
        "task_id": "task_id",
        "type": "type",
    }

    def __init__(
        self,
        description: str = None,
        enabled: bool = None,
        parameters: ModelsWindowsAutoTrackingParameters = None,
        project_id: int = None,
        skip_when_timer_is_running: bool = None,
        start_without_confirmation: bool = None,
        task_id: int = None,
        type: int = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        ModelsWindowsAutoTracking - a model defined in Swagger

        Parameters:
          description (str): Optional
          enabled (bool): Optional
          parameters (ModelsWindowsAutoTrackingParameters): Optional
          project_id (int): Optional
          skip_when_timer_is_running (bool): Optional
          start_without_confirmation (bool): Optional
          task_id (int): Optional
          type (int): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._enabled = None
        self._parameters = None
        self._project_id = None
        self._skip_when_timer_is_running = None
        self._start_without_confirmation = None
        self._task_id = None
        self._type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if parameters is not None:
            self.parameters = parameters
        if project_id is not None:
            self.project_id = project_id
        if skip_when_timer_is_running is not None:
            self.skip_when_timer_is_running = skip_when_timer_is_running
        if start_without_confirmation is not None:
            self.start_without_confirmation = start_without_confirmation
        if task_id is not None:
            self.task_id = task_id
        if type is not None:
            self.type = type

    @property
    def description(self) -> str:
        """Gets the description of this ModelsWindowsAutoTracking.  # noqa: E501


        :return: The description of this ModelsWindowsAutoTracking.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this ModelsWindowsAutoTracking.


        :param description: The description of this ModelsWindowsAutoTracking.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enabled(self) -> bool:
        """Gets the enabled of this ModelsWindowsAutoTracking.  # noqa: E501


        :return: The enabled of this ModelsWindowsAutoTracking.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        """Sets the enabled of this ModelsWindowsAutoTracking.


        :param enabled: The enabled of this ModelsWindowsAutoTracking.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def parameters(self) -> ModelsWindowsAutoTrackingParameters:
        """Gets the parameters of this ModelsWindowsAutoTracking.  # noqa: E501


        :return: The parameters of this ModelsWindowsAutoTracking.  # noqa: E501
        :rtype: ModelsWindowsAutoTrackingParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters: ModelsWindowsAutoTrackingParameters):
        """Sets the parameters of this ModelsWindowsAutoTracking.


        :param parameters: The parameters of this ModelsWindowsAutoTracking.  # noqa: E501
        :type: ModelsWindowsAutoTrackingParameters
        """

        self._parameters = parameters

    @property
    def project_id(self) -> int:
        """Gets the project_id of this ModelsWindowsAutoTracking.  # noqa: E501


        :return: The project_id of this ModelsWindowsAutoTracking.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id: int):
        """Sets the project_id of this ModelsWindowsAutoTracking.


        :param project_id: The project_id of this ModelsWindowsAutoTracking.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def skip_when_timer_is_running(self) -> bool:
        """Gets the skip_when_timer_is_running of this ModelsWindowsAutoTracking.  # noqa: E501


        :return: The skip_when_timer_is_running of this ModelsWindowsAutoTracking.  # noqa: E501
        :rtype: bool
        """
        return self._skip_when_timer_is_running

    @skip_when_timer_is_running.setter
    def skip_when_timer_is_running(self, skip_when_timer_is_running: bool):
        """Sets the skip_when_timer_is_running of this ModelsWindowsAutoTracking.


        :param skip_when_timer_is_running: The skip_when_timer_is_running of this ModelsWindowsAutoTracking.  # noqa: E501
        :type: bool
        """

        self._skip_when_timer_is_running = skip_when_timer_is_running

    @property
    def start_without_confirmation(self) -> bool:
        """Gets the start_without_confirmation of this ModelsWindowsAutoTracking.  # noqa: E501


        :return: The start_without_confirmation of this ModelsWindowsAutoTracking.  # noqa: E501
        :rtype: bool
        """
        return self._start_without_confirmation

    @start_without_confirmation.setter
    def start_without_confirmation(self, start_without_confirmation: bool):
        """Sets the start_without_confirmation of this ModelsWindowsAutoTracking.


        :param start_without_confirmation: The start_without_confirmation of this ModelsWindowsAutoTracking.  # noqa: E501
        :type: bool
        """

        self._start_without_confirmation = start_without_confirmation

    @property
    def task_id(self) -> int:
        """Gets the task_id of this ModelsWindowsAutoTracking.  # noqa: E501


        :return: The task_id of this ModelsWindowsAutoTracking.  # noqa: E501
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id: int):
        """Sets the task_id of this ModelsWindowsAutoTracking.


        :param task_id: The task_id of this ModelsWindowsAutoTracking.  # noqa: E501
        :type: int
        """

        self._task_id = task_id

    @property
    def type(self) -> int:
        """Gets the type of this ModelsWindowsAutoTracking.  # noqa: E501


        :return: The type of this ModelsWindowsAutoTracking.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type: int):
        """Sets the type of this ModelsWindowsAutoTracking.


        :param type: The type of this ModelsWindowsAutoTracking.  # noqa: E501
        :type: int
        """

        self._type = type

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
        if issubclass(ModelsWindowsAutoTracking, dict):
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
        if not isinstance(other, ModelsWindowsAutoTracking):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsWindowsAutoTracking):
            return True

        return self.to_dict() != other.to_dict()
