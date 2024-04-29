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


class DtoProjectUserParamsRequest:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"client_ids": "list[int]", "project_ids": "list[int]", "start_id": "int"}

    attribute_map = {"client_ids": "client_ids", "project_ids": "project_ids", "start_id": "start_id"}

    def __init__(self, client_ids=None, project_ids=None, start_id=None, _configuration=None):  # noqa: E501
        """DtoProjectUserParamsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_ids = None
        self._project_ids = None
        self._start_id = None
        self.discriminator = None

        if client_ids is not None:
            self.client_ids = client_ids
        if project_ids is not None:
            self.project_ids = project_ids
        if start_id is not None:
            self.start_id = start_id

    @property
    def client_ids(self):
        """Gets the client_ids of this DtoProjectUserParamsRequest.  # noqa: E501

        Client IDs, optional.  # noqa: E501

        :return: The client_ids of this DtoProjectUserParamsRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._client_ids

    @client_ids.setter
    def client_ids(self, client_ids):
        """Sets the client_ids of this DtoProjectUserParamsRequest.

        Client IDs, optional.  # noqa: E501

        :param client_ids: The client_ids of this DtoProjectUserParamsRequest.  # noqa: E501
        :type: list[int]
        """

        self._client_ids = client_ids

    @property
    def project_ids(self):
        """Gets the project_ids of this DtoProjectUserParamsRequest.  # noqa: E501

        Project IDs, optional.  # noqa: E501

        :return: The project_ids of this DtoProjectUserParamsRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._project_ids

    @project_ids.setter
    def project_ids(self, project_ids):
        """Sets the project_ids of this DtoProjectUserParamsRequest.

        Project IDs, optional.  # noqa: E501

        :param project_ids: The project_ids of this DtoProjectUserParamsRequest.  # noqa: E501
        :type: list[int]
        """

        self._project_ids = project_ids

    @property
    def start_id(self):
        """Gets the start_id of this DtoProjectUserParamsRequest.  # noqa: E501


        :return: The start_id of this DtoProjectUserParamsRequest.  # noqa: E501
        :rtype: int
        """
        return self._start_id

    @start_id.setter
    def start_id(self, start_id):
        """Sets the start_id of this DtoProjectUserParamsRequest.


        :param start_id: The start_id of this DtoProjectUserParamsRequest.  # noqa: E501
        :type: int
        """

        self._start_id = start_id

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
        if issubclass(DtoProjectUserParamsRequest, dict):
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
        if not isinstance(other, DtoProjectUserParamsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DtoProjectUserParamsRequest):
            return True

        return self.to_dict() != other.to_dict()
