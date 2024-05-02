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


class ModelsAlphaFeature:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {"alpha_feature_id": "int", "code": "str", "deleted_at": "str", "description": "str", "enabled": "bool"}

    attribute_map = {
        "alpha_feature_id": "alpha_feature_id",
        "code": "code",
        "deleted_at": "deleted_at",
        "description": "description",
        "enabled": "enabled",
    }

    def __init__(
        self,
        alpha_feature_id: int = None,
        code: str = None,
        deleted_at: str = None,
        description: str = None,
        enabled: bool = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        ModelsAlphaFeature - a model defined in Swagger

        Parameters:
          alpha_feature_id (int): Optional
          code (str): Optional
          deleted_at (str): Optional
          description (str): Optional
          enabled (bool): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alpha_feature_id = None
        self._code = None
        self._deleted_at = None
        self._description = None
        self._enabled = None
        self.discriminator = None

        if alpha_feature_id is not None:
            self.alpha_feature_id = alpha_feature_id
        if code is not None:
            self.code = code
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled

    @property
    def alpha_feature_id(self) -> int:
        """Gets the alpha_feature_id of this ModelsAlphaFeature.  # noqa: E501

        Feature ID  # noqa: E501

        :return: The alpha_feature_id of this ModelsAlphaFeature.  # noqa: E501
        :rtype: int
        """
        return self._alpha_feature_id

    @alpha_feature_id.setter
    def alpha_feature_id(self, alpha_feature_id: int):
        """Sets the alpha_feature_id of this ModelsAlphaFeature.

        Feature ID  # noqa: E501

        :param alpha_feature_id: The alpha_feature_id of this ModelsAlphaFeature.  # noqa: E501
        :type: int
        """

        self._alpha_feature_id = alpha_feature_id

    @property
    def code(self) -> str:
        """Gets the code of this ModelsAlphaFeature.  # noqa: E501

        Feature code  # noqa: E501

        :return: The code of this ModelsAlphaFeature.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this ModelsAlphaFeature.

        Feature code  # noqa: E501

        :param code: The code of this ModelsAlphaFeature.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def deleted_at(self) -> str:
        """Gets the deleted_at of this ModelsAlphaFeature.  # noqa: E501

        Time of deletion, omitted if empty  # noqa: E501

        :return: The deleted_at of this ModelsAlphaFeature.  # noqa: E501
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at: str):
        """Sets the deleted_at of this ModelsAlphaFeature.

        Time of deletion, omitted if empty  # noqa: E501

        :param deleted_at: The deleted_at of this ModelsAlphaFeature.  # noqa: E501
        :type: str
        """

        self._deleted_at = deleted_at

    @property
    def description(self) -> str:
        """Gets the description of this ModelsAlphaFeature.  # noqa: E501

        Feature description, omitted if empty  # noqa: E501

        :return: The description of this ModelsAlphaFeature.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this ModelsAlphaFeature.

        Feature description, omitted if empty  # noqa: E501

        :param description: The description of this ModelsAlphaFeature.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enabled(self) -> bool:
        """Gets the enabled of this ModelsAlphaFeature.  # noqa: E501

        Whether the feature is enabled  # noqa: E501

        :return: The enabled of this ModelsAlphaFeature.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        """Sets the enabled of this ModelsAlphaFeature.

        Whether the feature is enabled  # noqa: E501

        :param enabled: The enabled of this ModelsAlphaFeature.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

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
        if issubclass(ModelsAlphaFeature, dict):
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
        if not isinstance(other, ModelsAlphaFeature):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsAlphaFeature):
            return True

        return self.to_dict() != other.to_dict()
