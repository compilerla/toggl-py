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
from toggl.models.timeentry_patch_failure import TimeentryPatchFailure  # noqa: F401


class TimeentryPatchOutput:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {"failure": "list[TimeentryPatchFailure]", "success": "list[int]"}

    attribute_map = {"failure": "failure", "success": "success"}

    def __init__(
        self,
        failure: list[TimeentryPatchFailure] = None,
        success: list[int] = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        TimeentryPatchOutput - a model defined in Swagger

        Parameters:
          failure (list[TimeentryPatchFailure]): Optional
          success (list[int]): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._failure = None
        self._success = None
        self.discriminator = None

        if failure is not None:
            self.failure = failure
        if success is not None:
            self.success = success

    @property
    def failure(self) -> list[TimeentryPatchFailure]:
        """Gets the failure of this TimeentryPatchOutput.  # noqa: E501


        :return: The failure of this TimeentryPatchOutput.  # noqa: E501
        :rtype: list[TimeentryPatchFailure]
        """
        return self._failure

    @failure.setter
    def failure(self, failure: list[TimeentryPatchFailure]):
        """Sets the failure of this TimeentryPatchOutput.


        :param failure: The failure of this TimeentryPatchOutput.  # noqa: E501
        :type: list[TimeentryPatchFailure]
        """

        self._failure = failure

    @property
    def success(self) -> list[int]:
        """Gets the success of this TimeentryPatchOutput.  # noqa: E501

        The IDs for which the patch was succesful.  # noqa: E501

        :return: The success of this TimeentryPatchOutput.  # noqa: E501
        :rtype: list[int]
        """
        return self._success

    @success.setter
    def success(self, success: list[int]):
        """Sets the success of this TimeentryPatchOutput.

        The IDs for which the patch was succesful.  # noqa: E501

        :param success: The success of this TimeentryPatchOutput.  # noqa: E501
        :type: list[int]
        """

        self._success = success

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
        if issubclass(TimeentryPatchOutput, dict):
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
        if not isinstance(other, TimeentryPatchOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimeentryPatchOutput):
            return True

        return self.to_dict() != other.to_dict()
