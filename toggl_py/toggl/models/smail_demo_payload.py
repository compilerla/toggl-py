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


class SmailDemoPayload:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "email": "str",
        "first_name": "str",
        "last_name": "str",
        "phone": "str",
        "purpose": "str",
        "source": "str",
        "team_size": "str",
    }

    attribute_map = {
        "email": "Email",
        "first_name": "FirstName",
        "last_name": "LastName",
        "phone": "Phone",
        "purpose": "Purpose",
        "source": "Source",
        "team_size": "TeamSize",
    }

    def __init__(
        self,
        email=None,
        first_name=None,
        last_name=None,
        phone=None,
        purpose=None,
        source=None,
        team_size=None,
        _configuration=None,
    ):  # noqa: E501
        """SmailDemoPayload - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._email = None
        self._first_name = None
        self._last_name = None
        self._phone = None
        self._purpose = None
        self._source = None
        self._team_size = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if phone is not None:
            self.phone = phone
        if purpose is not None:
            self.purpose = purpose
        if source is not None:
            self.source = source
        if team_size is not None:
            self.team_size = team_size

    @property
    def email(self):
        """Gets the email of this SmailDemoPayload.  # noqa: E501


        :return: The email of this SmailDemoPayload.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SmailDemoPayload.


        :param email: The email of this SmailDemoPayload.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this SmailDemoPayload.  # noqa: E501


        :return: The first_name of this SmailDemoPayload.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this SmailDemoPayload.


        :param first_name: The first_name of this SmailDemoPayload.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this SmailDemoPayload.  # noqa: E501


        :return: The last_name of this SmailDemoPayload.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this SmailDemoPayload.


        :param last_name: The last_name of this SmailDemoPayload.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def phone(self):
        """Gets the phone of this SmailDemoPayload.  # noqa: E501


        :return: The phone of this SmailDemoPayload.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this SmailDemoPayload.


        :param phone: The phone of this SmailDemoPayload.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def purpose(self):
        """Gets the purpose of this SmailDemoPayload.  # noqa: E501


        :return: The purpose of this SmailDemoPayload.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this SmailDemoPayload.


        :param purpose: The purpose of this SmailDemoPayload.  # noqa: E501
        :type: str
        """

        self._purpose = purpose

    @property
    def source(self):
        """Gets the source of this SmailDemoPayload.  # noqa: E501


        :return: The source of this SmailDemoPayload.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this SmailDemoPayload.


        :param source: The source of this SmailDemoPayload.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def team_size(self):
        """Gets the team_size of this SmailDemoPayload.  # noqa: E501


        :return: The team_size of this SmailDemoPayload.  # noqa: E501
        :rtype: str
        """
        return self._team_size

    @team_size.setter
    def team_size(self, team_size):
        """Sets the team_size of this SmailDemoPayload.


        :param team_size: The team_size of this SmailDemoPayload.  # noqa: E501
        :type: str
        """

        self._team_size = team_size

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
        if issubclass(SmailDemoPayload, dict):
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
        if not isinstance(other, SmailDemoPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmailDemoPayload):
            return True

        return self.to_dict() != other.to_dict()
