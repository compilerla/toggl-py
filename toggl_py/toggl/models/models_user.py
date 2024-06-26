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


class ModelsUser:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"api_token": "str", "email": "str", "fullname": "str", "id": "int", "timezone": "str"}

    attribute_map = {"api_token": "api_token", "email": "email", "fullname": "fullname", "id": "id", "timezone": "timezone"}

    def __init__(self, api_token=None, email=None, fullname=None, id=None, timezone=None, _configuration=None):  # noqa: E501
        """ModelsUser - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._api_token = None
        self._email = None
        self._fullname = None
        self._id = None
        self._timezone = None
        self.discriminator = None

        if api_token is not None:
            self.api_token = api_token
        if email is not None:
            self.email = email
        if fullname is not None:
            self.fullname = fullname
        if id is not None:
            self.id = id
        if timezone is not None:
            self.timezone = timezone

    @property
    def api_token(self):
        """Gets the api_token of this ModelsUser.  # noqa: E501

        will be omitted if empty  # noqa: E501

        :return: The api_token of this ModelsUser.  # noqa: E501
        :rtype: str
        """
        return self._api_token

    @api_token.setter
    def api_token(self, api_token):
        """Sets the api_token of this ModelsUser.

        will be omitted if empty  # noqa: E501

        :param api_token: The api_token of this ModelsUser.  # noqa: E501
        :type: str
        """

        self._api_token = api_token

    @property
    def email(self):
        """Gets the email of this ModelsUser.  # noqa: E501


        :return: The email of this ModelsUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ModelsUser.


        :param email: The email of this ModelsUser.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def fullname(self):
        """Gets the fullname of this ModelsUser.  # noqa: E501


        :return: The fullname of this ModelsUser.  # noqa: E501
        :rtype: str
        """
        return self._fullname

    @fullname.setter
    def fullname(self, fullname):
        """Sets the fullname of this ModelsUser.


        :param fullname: The fullname of this ModelsUser.  # noqa: E501
        :type: str
        """

        self._fullname = fullname

    @property
    def id(self):
        """Gets the id of this ModelsUser.  # noqa: E501


        :return: The id of this ModelsUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelsUser.


        :param id: The id of this ModelsUser.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def timezone(self):
        """Gets the timezone of this ModelsUser.  # noqa: E501


        :return: The timezone of this ModelsUser.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this ModelsUser.


        :param timezone: The timezone of this ModelsUser.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

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
        if issubclass(ModelsUser, dict):
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
        if not isinstance(other, ModelsUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsUser):
            return True

        return self.to_dict() != other.to_dict()
