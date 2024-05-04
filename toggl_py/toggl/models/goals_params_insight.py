"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

from __future__ import annotations  # noqa: F401
import pprint
import re  # noqa: F401
from datetime import datetime  # noqa: F401
from typing import Any

from toggl.configuration import Configuration
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from toggl.models.models_goal_type import ModelsGoalType  # noqa: F401


class GoalsParamsInsight:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {"cadence_period": "str", "goal_type": "ModelsGoalType", "user_id": "int", "workspace_id": "int"}

    attribute_map = {
        "cadence_period": "cadence_period",
        "goal_type": "goal_type",
        "user_id": "user_id",
        "workspace_id": "workspace_id",
    }

    def __init__(
        self,
        cadence_period: str,
        goal_type: ModelsGoalType,
        user_id: int,
        workspace_id: int,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        GoalsParamsInsight - a model defined in Swagger

        Parameters:
          cadence_period (str): Required
          goal_type (ModelsGoalType): Required
          user_id (int): Required
          workspace_id (int): Required
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cadence_period = None
        self._goal_type = None
        self._user_id = None
        self._workspace_id = None
        self.discriminator = None

        self.cadence_period = cadence_period
        self.goal_type = goal_type
        self.user_id = user_id
        self.workspace_id = workspace_id

    @property
    def cadence_period(self) -> str:
        """Gets the cadence_period of this GoalsParamsInsight.  # noqa: E501


        :return: The cadence_period of this GoalsParamsInsight.  # noqa: E501
        :rtype: str
        """
        return self._cadence_period

    @cadence_period.setter
    def cadence_period(self, cadence_period: str):
        """Sets the cadence_period of this GoalsParamsInsight.


        :param cadence_period: The cadence_period of this GoalsParamsInsight.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cadence_period is None:
            raise ValueError("Invalid value for `cadence_period`, must not be `None`")  # noqa: E501

        self._cadence_period = cadence_period

    @property
    def goal_type(self) -> ModelsGoalType:
        """Gets the goal_type of this GoalsParamsInsight.  # noqa: E501


        :return: The goal_type of this GoalsParamsInsight.  # noqa: E501
        :rtype: ModelsGoalType
        """
        return self._goal_type

    @goal_type.setter
    def goal_type(self, goal_type: ModelsGoalType):
        """Sets the goal_type of this GoalsParamsInsight.


        :param goal_type: The goal_type of this GoalsParamsInsight.  # noqa: E501
        :type: ModelsGoalType
        """
        if self._configuration.client_side_validation and goal_type is None:
            raise ValueError("Invalid value for `goal_type`, must not be `None`")  # noqa: E501

        self._goal_type = goal_type

    @property
    def user_id(self) -> int:
        """Gets the user_id of this GoalsParamsInsight.  # noqa: E501


        :return: The user_id of this GoalsParamsInsight.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this GoalsParamsInsight.


        :param user_id: The user_id of this GoalsParamsInsight.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def workspace_id(self) -> int:
        """Gets the workspace_id of this GoalsParamsInsight.  # noqa: E501


        :return: The workspace_id of this GoalsParamsInsight.  # noqa: E501
        :rtype: int
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id: int):
        """Sets the workspace_id of this GoalsParamsInsight.


        :param workspace_id: The workspace_id of this GoalsParamsInsight.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and workspace_id is None:
            raise ValueError("Invalid value for `workspace_id`, must not be `None`")  # noqa: E501

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
        if issubclass(GoalsParamsInsight, dict):
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
        if not isinstance(other, GoalsParamsInsight):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GoalsParamsInsight):
            return True

        return self.to_dict() != other.to_dict()
