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


class ModelsMacOSAutoTracking:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {"id": "str", "keyword": "str", "project_id": "int", "task_id": "int"}

    attribute_map = {"id": "id", "keyword": "keyword", "project_id": "project_id", "task_id": "task_id"}

    def __init__(
        self,
        id: str = None,
        keyword: str = None,
        project_id: int = None,
        task_id: int = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        ModelsMacOSAutoTracking - a model defined in Swagger

        Parameters:
          id (str): Optional
          keyword (str): Optional
          project_id (int): Optional
          task_id (int): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._keyword = None
        self._project_id = None
        self._task_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if keyword is not None:
            self.keyword = keyword
        if project_id is not None:
            self.project_id = project_id
        if task_id is not None:
            self.task_id = task_id

    @property
    def id(self) -> str:
        """Gets the id of this ModelsMacOSAutoTracking.  # noqa: E501


        :return: The id of this ModelsMacOSAutoTracking.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this ModelsMacOSAutoTracking.


        :param id: The id of this ModelsMacOSAutoTracking.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def keyword(self) -> str:
        """Gets the keyword of this ModelsMacOSAutoTracking.  # noqa: E501


        :return: The keyword of this ModelsMacOSAutoTracking.  # noqa: E501
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword: str):
        """Sets the keyword of this ModelsMacOSAutoTracking.


        :param keyword: The keyword of this ModelsMacOSAutoTracking.  # noqa: E501
        :type: str
        """

        self._keyword = keyword

    @property
    def project_id(self) -> int:
        """Gets the project_id of this ModelsMacOSAutoTracking.  # noqa: E501


        :return: The project_id of this ModelsMacOSAutoTracking.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id: int):
        """Sets the project_id of this ModelsMacOSAutoTracking.


        :param project_id: The project_id of this ModelsMacOSAutoTracking.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def task_id(self) -> int:
        """Gets the task_id of this ModelsMacOSAutoTracking.  # noqa: E501


        :return: The task_id of this ModelsMacOSAutoTracking.  # noqa: E501
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id: int):
        """Sets the task_id of this ModelsMacOSAutoTracking.


        :param task_id: The task_id of this ModelsMacOSAutoTracking.  # noqa: E501
        :type: int
        """

        self._task_id = task_id

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
        if issubclass(ModelsMacOSAutoTracking, dict):
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
        if not isinstance(other, ModelsMacOSAutoTracking):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsMacOSAutoTracking):
            return True

        return self.to_dict() != other.to_dict()
