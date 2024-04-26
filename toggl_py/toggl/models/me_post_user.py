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


class MePostUser:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "country_id": "int",
        "created_with": "str",
        "email": "str",
        "full_name": "str",
        "invitation_code": "str",
        "password": "str",
        "timezone": "str",
        "tos_accepted": "bool",
        "workspace": "MePostInitialWorkspace",
    }

    attribute_map = {
        "country_id": "country_id",
        "created_with": "created_with",
        "email": "email",
        "full_name": "full_name",
        "invitation_code": "invitation_code",
        "password": "password",
        "timezone": "timezone",
        "tos_accepted": "tos_accepted",
        "workspace": "workspace",
    }

    def __init__(
        self,
        country_id=None,
        created_with=None,
        email=None,
        full_name=None,
        invitation_code=None,
        password=None,
        timezone=None,
        tos_accepted=None,
        workspace=None,
        _configuration=None,
    ):  # noqa: E501
        """MePostUser - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._country_id = None
        self._created_with = None
        self._email = None
        self._full_name = None
        self._invitation_code = None
        self._password = None
        self._timezone = None
        self._tos_accepted = None
        self._workspace = None
        self.discriminator = None

        if country_id is not None:
            self.country_id = country_id
        if created_with is not None:
            self.created_with = created_with
        self.email = email
        if full_name is not None:
            self.full_name = full_name
        if invitation_code is not None:
            self.invitation_code = invitation_code
        self.password = password
        if timezone is not None:
            self.timezone = timezone
        self.tos_accepted = tos_accepted
        if workspace is not None:
            self.workspace = workspace

    @property
    def country_id(self):
        """Gets the country_id of this MePostUser.  # noqa: E501

        User's country ID, if not provided will be United States  # noqa: E501

        :return: The country_id of this MePostUser.  # noqa: E501
        :rtype: int
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """Sets the country_id of this MePostUser.

        User's country ID, if not provided will be United States  # noqa: E501

        :param country_id: The country_id of this MePostUser.  # noqa: E501
        :type: int
        """

        self._country_id = country_id

    @property
    def created_with(self):
        """Gets the created_with of this MePostUser.  # noqa: E501

        Should describe the application/service that is using the API  # noqa: E501

        :return: The created_with of this MePostUser.  # noqa: E501
        :rtype: str
        """
        return self._created_with

    @created_with.setter
    def created_with(self, created_with):
        """Sets the created_with of this MePostUser.

        Should describe the application/service that is using the API  # noqa: E501

        :param created_with: The created_with of this MePostUser.  # noqa: E501
        :type: str
        """

        self._created_with = created_with

    @property
    def email(self):
        """Gets the email of this MePostUser.  # noqa: E501

        Email for new user account  # noqa: E501

        :return: The email of this MePostUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this MePostUser.

        Email for new user account  # noqa: E501

        :param email: The email of this MePostUser.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def full_name(self):
        """Gets the full_name of this MePostUser.  # noqa: E501

        User's full name, if not provided will be derived from the email address  # noqa: E501

        :return: The full_name of this MePostUser.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this MePostUser.

        User's full name, if not provided will be derived from the email address  # noqa: E501

        :param full_name: The full_name of this MePostUser.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def invitation_code(self):
        """Gets the invitation_code of this MePostUser.  # noqa: E501

        Optional, used when creating account through an invitation  # noqa: E501

        :return: The invitation_code of this MePostUser.  # noqa: E501
        :rtype: str
        """
        return self._invitation_code

    @invitation_code.setter
    def invitation_code(self, invitation_code):
        """Sets the invitation_code of this MePostUser.

        Optional, used when creating account through an invitation  # noqa: E501

        :param invitation_code: The invitation_code of this MePostUser.  # noqa: E501
        :type: str
        """

        self._invitation_code = invitation_code

    @property
    def password(self):
        """Gets the password of this MePostUser.  # noqa: E501

        Password for new user account  # noqa: E501

        :return: The password of this MePostUser.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this MePostUser.

        Password for new user account  # noqa: E501

        :param password: The password of this MePostUser.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if self._configuration.client_side_validation and password is not None and len(password) < 6:
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `6`")  # noqa: E501

        self._password = password

    @property
    def timezone(self):
        """Gets the timezone of this MePostUser.  # noqa: E501

        User's timezone, if not provided will be UTC  # noqa: E501

        :return: The timezone of this MePostUser.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this MePostUser.

        User's timezone, if not provided will be UTC  # noqa: E501

        :param timezone: The timezone of this MePostUser.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def tos_accepted(self):
        """Gets the tos_accepted of this MePostUser.  # noqa: E501

        Whether the Terms of Service have been accepted  # noqa: E501

        :return: The tos_accepted of this MePostUser.  # noqa: E501
        :rtype: bool
        """
        return self._tos_accepted

    @tos_accepted.setter
    def tos_accepted(self, tos_accepted):
        """Sets the tos_accepted of this MePostUser.

        Whether the Terms of Service have been accepted  # noqa: E501

        :param tos_accepted: The tos_accepted of this MePostUser.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and tos_accepted is None:
            raise ValueError("Invalid value for `tos_accepted`, must not be `None`")  # noqa: E501

        self._tos_accepted = tos_accepted

    @property
    def workspace(self):
        """Gets the workspace of this MePostUser.  # noqa: E501

        Optional workspace settings, used when creating account not through an invitation  # noqa: E501

        :return: The workspace of this MePostUser.  # noqa: E501
        :rtype: MePostInitialWorkspace
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this MePostUser.

        Optional workspace settings, used when creating account not through an invitation  # noqa: E501

        :param workspace: The workspace of this MePostUser.  # noqa: E501
        :type: MePostInitialWorkspace
        """

        self._workspace = workspace

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
        if issubclass(MePostUser, dict):
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
        if not isinstance(other, MePostUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MePostUser):
            return True

        return self.to_dict() != other.to_dict()