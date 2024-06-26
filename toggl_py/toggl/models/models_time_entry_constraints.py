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


class ModelsTimeEntryConstraints:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "description_present": "bool",
        "project_present": "bool",
        "tag_present": "bool",
        "task_present": "bool",
        "time_entry_constraints_enabled": "bool",
    }

    attribute_map = {
        "description_present": "description_present",
        "project_present": "project_present",
        "tag_present": "tag_present",
        "task_present": "task_present",
        "time_entry_constraints_enabled": "time_entry_constraints_enabled",
    }

    def __init__(
        self,
        description_present=None,
        project_present=None,
        tag_present=None,
        task_present=None,
        time_entry_constraints_enabled=None,
        _configuration=None,
    ):  # noqa: E501
        """ModelsTimeEntryConstraints - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description_present = None
        self._project_present = None
        self._tag_present = None
        self._task_present = None
        self._time_entry_constraints_enabled = None
        self.discriminator = None

        if description_present is not None:
            self.description_present = description_present
        if project_present is not None:
            self.project_present = project_present
        if tag_present is not None:
            self.tag_present = tag_present
        if task_present is not None:
            self.task_present = task_present
        if time_entry_constraints_enabled is not None:
            self.time_entry_constraints_enabled = time_entry_constraints_enabled

    @property
    def description_present(self):
        """Gets the description_present of this ModelsTimeEntryConstraints.  # noqa: E501


        :return: The description_present of this ModelsTimeEntryConstraints.  # noqa: E501
        :rtype: bool
        """
        return self._description_present

    @description_present.setter
    def description_present(self, description_present):
        """Sets the description_present of this ModelsTimeEntryConstraints.


        :param description_present: The description_present of this ModelsTimeEntryConstraints.  # noqa: E501
        :type: bool
        """

        self._description_present = description_present

    @property
    def project_present(self):
        """Gets the project_present of this ModelsTimeEntryConstraints.  # noqa: E501


        :return: The project_present of this ModelsTimeEntryConstraints.  # noqa: E501
        :rtype: bool
        """
        return self._project_present

    @project_present.setter
    def project_present(self, project_present):
        """Sets the project_present of this ModelsTimeEntryConstraints.


        :param project_present: The project_present of this ModelsTimeEntryConstraints.  # noqa: E501
        :type: bool
        """

        self._project_present = project_present

    @property
    def tag_present(self):
        """Gets the tag_present of this ModelsTimeEntryConstraints.  # noqa: E501


        :return: The tag_present of this ModelsTimeEntryConstraints.  # noqa: E501
        :rtype: bool
        """
        return self._tag_present

    @tag_present.setter
    def tag_present(self, tag_present):
        """Sets the tag_present of this ModelsTimeEntryConstraints.


        :param tag_present: The tag_present of this ModelsTimeEntryConstraints.  # noqa: E501
        :type: bool
        """

        self._tag_present = tag_present

    @property
    def task_present(self):
        """Gets the task_present of this ModelsTimeEntryConstraints.  # noqa: E501


        :return: The task_present of this ModelsTimeEntryConstraints.  # noqa: E501
        :rtype: bool
        """
        return self._task_present

    @task_present.setter
    def task_present(self, task_present):
        """Sets the task_present of this ModelsTimeEntryConstraints.


        :param task_present: The task_present of this ModelsTimeEntryConstraints.  # noqa: E501
        :type: bool
        """

        self._task_present = task_present

    @property
    def time_entry_constraints_enabled(self):
        """Gets the time_entry_constraints_enabled of this ModelsTimeEntryConstraints.  # noqa: E501


        :return: The time_entry_constraints_enabled of this ModelsTimeEntryConstraints.  # noqa: E501
        :rtype: bool
        """
        return self._time_entry_constraints_enabled

    @time_entry_constraints_enabled.setter
    def time_entry_constraints_enabled(self, time_entry_constraints_enabled):
        """Sets the time_entry_constraints_enabled of this ModelsTimeEntryConstraints.


        :param time_entry_constraints_enabled: The time_entry_constraints_enabled of this ModelsTimeEntryConstraints.  # noqa: E501
        :type: bool
        """

        self._time_entry_constraints_enabled = time_entry_constraints_enabled

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
        if issubclass(ModelsTimeEntryConstraints, dict):
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
        if not isinstance(other, ModelsTimeEntryConstraints):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsTimeEntryConstraints):
            return True

        return self.to_dict() != other.to_dict()
