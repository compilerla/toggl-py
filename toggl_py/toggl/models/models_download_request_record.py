"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Last changed: 2024-04-26T22:13:16.785Z
Generated by: https://github.com/compilerla/toggl-py/tree/main/codegen
"""

import pprint
import re  # noqa: F401

from toggl.configuration import Configuration


class ModelsDownloadRequestRecord:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"state": "str", "token": "str"}

    attribute_map = {"state": "state", "token": "token"}

    def __init__(self, state=None, token=None, _configuration=None):  # noqa: E501
        """ModelsDownloadRequestRecord - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._state = None
        self._token = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if token is not None:
            self.token = token

    @property
    def state(self):
        """Gets the state of this ModelsDownloadRequestRecord.  # noqa: E501


        :return: The state of this ModelsDownloadRequestRecord.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ModelsDownloadRequestRecord.


        :param state: The state of this ModelsDownloadRequestRecord.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def token(self):
        """Gets the token of this ModelsDownloadRequestRecord.  # noqa: E501


        :return: The token of this ModelsDownloadRequestRecord.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this ModelsDownloadRequestRecord.


        :param token: The token of this ModelsDownloadRequestRecord.  # noqa: E501
        :type: str
        """

        self._token = token

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
        if issubclass(ModelsDownloadRequestRecord, dict):
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
        if not isinstance(other, ModelsDownloadRequestRecord):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsDownloadRequestRecord):
            return True

        return self.to_dict() != other.to_dict()
