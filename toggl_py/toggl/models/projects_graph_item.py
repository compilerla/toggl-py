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


class ProjectsGraphItem:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"_date": "str", "earnings": "int", "labour_cost": "int"}

    attribute_map = {"_date": "date", "earnings": "earnings", "labour_cost": "labour_cost"}

    def __init__(self, _date=None, earnings=None, labour_cost=None, _configuration=None):  # noqa: E501
        """ProjectsGraphItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self.__date = None
        self._earnings = None
        self._labour_cost = None
        self.discriminator = None

        if _date is not None:
            self._date = _date
        if earnings is not None:
            self.earnings = earnings
        if labour_cost is not None:
            self.labour_cost = labour_cost

    @property
    def _date(self):
        """Gets the _date of this ProjectsGraphItem.  # noqa: E501


        :return: The _date of this ProjectsGraphItem.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ProjectsGraphItem.


        :param _date: The _date of this ProjectsGraphItem.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def earnings(self):
        """Gets the earnings of this ProjectsGraphItem.  # noqa: E501


        :return: The earnings of this ProjectsGraphItem.  # noqa: E501
        :rtype: int
        """
        return self._earnings

    @earnings.setter
    def earnings(self, earnings):
        """Sets the earnings of this ProjectsGraphItem.


        :param earnings: The earnings of this ProjectsGraphItem.  # noqa: E501
        :type: int
        """

        self._earnings = earnings

    @property
    def labour_cost(self):
        """Gets the labour_cost of this ProjectsGraphItem.  # noqa: E501


        :return: The labour_cost of this ProjectsGraphItem.  # noqa: E501
        :rtype: int
        """
        return self._labour_cost

    @labour_cost.setter
    def labour_cost(self, labour_cost):
        """Sets the labour_cost of this ProjectsGraphItem.


        :param labour_cost: The labour_cost of this ProjectsGraphItem.  # noqa: E501
        :type: int
        """

        self._labour_cost = labour_cost

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
        if issubclass(ProjectsGraphItem, dict):
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
        if not isinstance(other, ProjectsGraphItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectsGraphItem):
            return True

        return self.to_dict() != other.to_dict()
