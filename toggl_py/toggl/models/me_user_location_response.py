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


class MeUserLocationResponse:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"city": "str", "city_lat_long": "str", "country_code": "str", "country_name": "str", "state": "str"}

    attribute_map = {
        "city": "city",
        "city_lat_long": "city_lat_long",
        "country_code": "country_code",
        "country_name": "country_name",
        "state": "state",
    }

    def __init__(
        self, city=None, city_lat_long=None, country_code=None, country_name=None, state=None, _configuration=None
    ):  # noqa: E501
        """MeUserLocationResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._city = None
        self._city_lat_long = None
        self._country_code = None
        self._country_name = None
        self._state = None
        self.discriminator = None

        if city is not None:
            self.city = city
        if city_lat_long is not None:
            self.city_lat_long = city_lat_long
        if country_code is not None:
            self.country_code = country_code
        if country_name is not None:
            self.country_name = country_name
        if state is not None:
            self.state = state

    @property
    def city(self):
        """Gets the city of this MeUserLocationResponse.  # noqa: E501


        :return: The city of this MeUserLocationResponse.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this MeUserLocationResponse.


        :param city: The city of this MeUserLocationResponse.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def city_lat_long(self):
        """Gets the city_lat_long of this MeUserLocationResponse.  # noqa: E501


        :return: The city_lat_long of this MeUserLocationResponse.  # noqa: E501
        :rtype: str
        """
        return self._city_lat_long

    @city_lat_long.setter
    def city_lat_long(self, city_lat_long):
        """Sets the city_lat_long of this MeUserLocationResponse.


        :param city_lat_long: The city_lat_long of this MeUserLocationResponse.  # noqa: E501
        :type: str
        """

        self._city_lat_long = city_lat_long

    @property
    def country_code(self):
        """Gets the country_code of this MeUserLocationResponse.  # noqa: E501


        :return: The country_code of this MeUserLocationResponse.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this MeUserLocationResponse.


        :param country_code: The country_code of this MeUserLocationResponse.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def country_name(self):
        """Gets the country_name of this MeUserLocationResponse.  # noqa: E501


        :return: The country_name of this MeUserLocationResponse.  # noqa: E501
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """Sets the country_name of this MeUserLocationResponse.


        :param country_name: The country_name of this MeUserLocationResponse.  # noqa: E501
        :type: str
        """

        self._country_name = country_name

    @property
    def state(self):
        """Gets the state of this MeUserLocationResponse.  # noqa: E501


        :return: The state of this MeUserLocationResponse.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this MeUserLocationResponse.


        :param state: The state of this MeUserLocationResponse.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if issubclass(MeUserLocationResponse, dict):
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
        if not isinstance(other, MeUserLocationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MeUserLocationResponse):
            return True

        return self.to_dict() != other.to_dict()
