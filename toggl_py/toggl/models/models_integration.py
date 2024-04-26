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


class ModelsIntegration:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "calendar_integration_id": "int",
        "created_at": "str",
        "email": "str",
        "error_status": "str",
        "provider": "str",
    }

    attribute_map = {
        "calendar_integration_id": "calendar_integration_id",
        "created_at": "created_at",
        "email": "email",
        "error_status": "error_status",
        "provider": "provider",
    }

    def __init__(
        self, calendar_integration_id=None, created_at=None, email=None, error_status=None, provider=None, _configuration=None
    ):  # noqa: E501
        """ModelsIntegration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._calendar_integration_id = None
        self._created_at = None
        self._email = None
        self._error_status = None
        self._provider = None
        self.discriminator = None

        if calendar_integration_id is not None:
            self.calendar_integration_id = calendar_integration_id
        if created_at is not None:
            self.created_at = created_at
        if email is not None:
            self.email = email
        if error_status is not None:
            self.error_status = error_status
        if provider is not None:
            self.provider = provider

    @property
    def calendar_integration_id(self):
        """Gets the calendar_integration_id of this ModelsIntegration.  # noqa: E501


        :return: The calendar_integration_id of this ModelsIntegration.  # noqa: E501
        :rtype: int
        """
        return self._calendar_integration_id

    @calendar_integration_id.setter
    def calendar_integration_id(self, calendar_integration_id):
        """Sets the calendar_integration_id of this ModelsIntegration.


        :param calendar_integration_id: The calendar_integration_id of this ModelsIntegration.  # noqa: E501
        :type: int
        """

        self._calendar_integration_id = calendar_integration_id

    @property
    def created_at(self):
        """Gets the created_at of this ModelsIntegration.  # noqa: E501


        :return: The created_at of this ModelsIntegration.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ModelsIntegration.


        :param created_at: The created_at of this ModelsIntegration.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def email(self):
        """Gets the email of this ModelsIntegration.  # noqa: E501


        :return: The email of this ModelsIntegration.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ModelsIntegration.


        :param email: The email of this ModelsIntegration.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def error_status(self):
        """Gets the error_status of this ModelsIntegration.  # noqa: E501


        :return: The error_status of this ModelsIntegration.  # noqa: E501
        :rtype: str
        """
        return self._error_status

    @error_status.setter
    def error_status(self, error_status):
        """Sets the error_status of this ModelsIntegration.


        :param error_status: The error_status of this ModelsIntegration.  # noqa: E501
        :type: str
        """

        self._error_status = error_status

    @property
    def provider(self):
        """Gets the provider of this ModelsIntegration.  # noqa: E501


        :return: The provider of this ModelsIntegration.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ModelsIntegration.


        :param provider: The provider of this ModelsIntegration.  # noqa: E501
        :type: str
        """

        self._provider = provider

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
        if issubclass(ModelsIntegration, dict):
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
        if not isinstance(other, ModelsIntegration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsIntegration):
            return True

        return self.to_dict() != other.to_dict()
