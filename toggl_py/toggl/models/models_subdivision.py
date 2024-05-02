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


class ModelsSubdivision:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "company_id": "int",
        "country_id": "int",
        "country_subdivision_id": "int",
        "iso_code": "str",
        "name": "str",
    }

    attribute_map = {
        "company_id": "company_id",
        "country_id": "country_id",
        "country_subdivision_id": "country_subdivision_id",
        "iso_code": "iso_code",
        "name": "name",
    }

    def __init__(
        self,
        company_id: int = None,
        country_id: int = None,
        country_subdivision_id: int = None,
        iso_code: str = None,
        name: str = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        ModelsSubdivision - a model defined in Swagger

        Parameters:
          company_id (int): Optional
          country_id (int): Optional
          country_subdivision_id (int): Optional
          iso_code (str): Optional
          name (str): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._company_id = None
        self._country_id = None
        self._country_subdivision_id = None
        self._iso_code = None
        self._name = None
        self.discriminator = None

        if company_id is not None:
            self.company_id = company_id
        if country_id is not None:
            self.country_id = country_id
        if country_subdivision_id is not None:
            self.country_subdivision_id = country_subdivision_id
        if iso_code is not None:
            self.iso_code = iso_code
        if name is not None:
            self.name = name

    @property
    def company_id(self) -> int:
        """Gets the company_id of this ModelsSubdivision.  # noqa: E501


        :return: The company_id of this ModelsSubdivision.  # noqa: E501
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id: int):
        """Sets the company_id of this ModelsSubdivision.


        :param company_id: The company_id of this ModelsSubdivision.  # noqa: E501
        :type: int
        """

        self._company_id = company_id

    @property
    def country_id(self) -> int:
        """Gets the country_id of this ModelsSubdivision.  # noqa: E501


        :return: The country_id of this ModelsSubdivision.  # noqa: E501
        :rtype: int
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id: int):
        """Sets the country_id of this ModelsSubdivision.


        :param country_id: The country_id of this ModelsSubdivision.  # noqa: E501
        :type: int
        """

        self._country_id = country_id

    @property
    def country_subdivision_id(self) -> int:
        """Gets the country_subdivision_id of this ModelsSubdivision.  # noqa: E501


        :return: The country_subdivision_id of this ModelsSubdivision.  # noqa: E501
        :rtype: int
        """
        return self._country_subdivision_id

    @country_subdivision_id.setter
    def country_subdivision_id(self, country_subdivision_id: int):
        """Sets the country_subdivision_id of this ModelsSubdivision.


        :param country_subdivision_id: The country_subdivision_id of this ModelsSubdivision.  # noqa: E501
        :type: int
        """

        self._country_subdivision_id = country_subdivision_id

    @property
    def iso_code(self) -> str:
        """Gets the iso_code of this ModelsSubdivision.  # noqa: E501


        :return: The iso_code of this ModelsSubdivision.  # noqa: E501
        :rtype: str
        """
        return self._iso_code

    @iso_code.setter
    def iso_code(self, iso_code: str):
        """Sets the iso_code of this ModelsSubdivision.


        :param iso_code: The iso_code of this ModelsSubdivision.  # noqa: E501
        :type: str
        """

        self._iso_code = iso_code

    @property
    def name(self) -> str:
        """Gets the name of this ModelsSubdivision.  # noqa: E501


        :return: The name of this ModelsSubdivision.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ModelsSubdivision.


        :param name: The name of this ModelsSubdivision.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(ModelsSubdivision, dict):
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
        if not isinstance(other, ModelsSubdivision):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsSubdivision):
            return True

        return self.to_dict() != other.to_dict()
