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


class UserPayload:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "admin": "bool",
        "inactive": "bool",
        "labour_cost": "int",
        "posted_fields": "list[str]",
        "rate": "float",
        "rate_change_mode": "str",
        "role": "str",
        "working_hours_in_minutes": "int",
    }

    attribute_map = {
        "admin": "admin",
        "inactive": "inactive",
        "labour_cost": "labour_cost",
        "posted_fields": "postedFields",
        "rate": "rate",
        "rate_change_mode": "rate_change_mode",
        "role": "role",
        "working_hours_in_minutes": "working_hours_in_minutes",
    }

    def __init__(
        self,
        admin=None,
        inactive=None,
        labour_cost=None,
        posted_fields=None,
        rate=None,
        rate_change_mode=None,
        role=None,
        working_hours_in_minutes=None,
        _configuration=None,
    ):  # noqa: E501
        """UserPayload - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._admin = None
        self._inactive = None
        self._labour_cost = None
        self._posted_fields = None
        self._rate = None
        self._rate_change_mode = None
        self._role = None
        self._working_hours_in_minutes = None
        self.discriminator = None

        if admin is not None:
            self.admin = admin
        if inactive is not None:
            self.inactive = inactive
        if labour_cost is not None:
            self.labour_cost = labour_cost
        if posted_fields is not None:
            self.posted_fields = posted_fields
        if rate is not None:
            self.rate = rate
        if rate_change_mode is not None:
            self.rate_change_mode = rate_change_mode
        if role is not None:
            self.role = role
        if working_hours_in_minutes is not None:
            self.working_hours_in_minutes = working_hours_in_minutes

    @property
    def admin(self):
        """Gets the admin of this UserPayload.  # noqa: E501


        :return: The admin of this UserPayload.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this UserPayload.


        :param admin: The admin of this UserPayload.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def inactive(self):
        """Gets the inactive of this UserPayload.  # noqa: E501


        :return: The inactive of this UserPayload.  # noqa: E501
        :rtype: bool
        """
        return self._inactive

    @inactive.setter
    def inactive(self, inactive):
        """Sets the inactive of this UserPayload.


        :param inactive: The inactive of this UserPayload.  # noqa: E501
        :type: bool
        """

        self._inactive = inactive

    @property
    def labour_cost(self):
        """Gets the labour_cost of this UserPayload.  # noqa: E501

        Paid feature  # noqa: E501

        :return: The labour_cost of this UserPayload.  # noqa: E501
        :rtype: int
        """
        return self._labour_cost

    @labour_cost.setter
    def labour_cost(self, labour_cost):
        """Sets the labour_cost of this UserPayload.

        Paid feature  # noqa: E501

        :param labour_cost: The labour_cost of this UserPayload.  # noqa: E501
        :type: int
        """

        self._labour_cost = labour_cost

    @property
    def posted_fields(self):
        """Gets the posted_fields of this UserPayload.  # noqa: E501

        for explicit NULL-s, add field name here  # noqa: E501

        :return: The posted_fields of this UserPayload.  # noqa: E501
        :rtype: list[str]
        """
        return self._posted_fields

    @posted_fields.setter
    def posted_fields(self, posted_fields):
        """Sets the posted_fields of this UserPayload.

        for explicit NULL-s, add field name here  # noqa: E501

        :param posted_fields: The posted_fields of this UserPayload.  # noqa: E501
        :type: list[str]
        """

        self._posted_fields = posted_fields

    @property
    def rate(self):
        """Gets the rate of this UserPayload.  # noqa: E501

        Paid feature  # noqa: E501

        :return: The rate of this UserPayload.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this UserPayload.

        Paid feature  # noqa: E501

        :param rate: The rate of this UserPayload.  # noqa: E501
        :type: float
        """

        self._rate = rate

    @property
    def rate_change_mode(self):
        """Gets the rate_change_mode of this UserPayload.  # noqa: E501

        Paid feature  # noqa: E501

        :return: The rate_change_mode of this UserPayload.  # noqa: E501
        :rtype: str
        """
        return self._rate_change_mode

    @rate_change_mode.setter
    def rate_change_mode(self, rate_change_mode):
        """Sets the rate_change_mode of this UserPayload.

        Paid feature  # noqa: E501

        :param rate_change_mode: The rate_change_mode of this UserPayload.  # noqa: E501
        :type: str
        """

        self._rate_change_mode = rate_change_mode

    @property
    def role(self):
        """Gets the role of this UserPayload.  # noqa: E501

        Allowed inputs: \"admin\", \"user\", \"projectlead\" and \"teamlead\"  # noqa: E501

        :return: The role of this UserPayload.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UserPayload.

        Allowed inputs: \"admin\", \"user\", \"projectlead\" and \"teamlead\"  # noqa: E501

        :param role: The role of this UserPayload.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def working_hours_in_minutes(self):
        """Gets the working_hours_in_minutes of this UserPayload.  # noqa: E501

        Paid feature  # noqa: E501

        :return: The working_hours_in_minutes of this UserPayload.  # noqa: E501
        :rtype: int
        """
        return self._working_hours_in_minutes

    @working_hours_in_minutes.setter
    def working_hours_in_minutes(self, working_hours_in_minutes):
        """Sets the working_hours_in_minutes of this UserPayload.

        Paid feature  # noqa: E501

        :param working_hours_in_minutes: The working_hours_in_minutes of this UserPayload.  # noqa: E501
        :type: int
        """

        self._working_hours_in_minutes = working_hours_in_minutes

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
        if issubclass(UserPayload, dict):
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
        if not isinstance(other, UserPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserPayload):
            return True

        return self.to_dict() != other.to_dict()
