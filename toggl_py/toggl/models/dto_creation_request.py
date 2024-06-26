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


class DtoCreationRequest:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "description": "str",
        "name": "str",
        "organization_id": "int",
        "pinned": "bool",
        "preferences": "object",
        "query": "DtoQueryRequest",
        "source": "str",
        "type": "str",
    }

    attribute_map = {
        "description": "description",
        "name": "name",
        "organization_id": "organization_id",
        "pinned": "pinned",
        "preferences": "preferences",
        "query": "query",
        "source": "source",
        "type": "type",
    }

    def __init__(
        self,
        description=None,
        name=None,
        organization_id=None,
        pinned=None,
        preferences=None,
        query=None,
        source=None,
        type=None,
        _configuration=None,
    ):  # noqa: E501
        """DtoCreationRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._name = None
        self._organization_id = None
        self._pinned = None
        self._preferences = None
        self._query = None
        self._source = None
        self._type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.name = name
        self.organization_id = organization_id
        if pinned is not None:
            self.pinned = pinned
        if preferences is not None:
            self.preferences = preferences
        self.query = query
        if source is not None:
            self.source = source
        self.type = type

    @property
    def description(self):
        """Gets the description of this DtoCreationRequest.  # noqa: E501


        :return: The description of this DtoCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DtoCreationRequest.


        :param description: The description of this DtoCreationRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this DtoCreationRequest.  # noqa: E501


        :return: The name of this DtoCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DtoCreationRequest.


        :param name: The name of this DtoCreationRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def organization_id(self):
        """Gets the organization_id of this DtoCreationRequest.  # noqa: E501


        :return: The organization_id of this DtoCreationRequest.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this DtoCreationRequest.


        :param organization_id: The organization_id of this DtoCreationRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and organization_id is None:
            raise ValueError("Invalid value for `organization_id`, must not be `None`")  # noqa: E501

        self._organization_id = organization_id

    @property
    def pinned(self):
        """Gets the pinned of this DtoCreationRequest.  # noqa: E501


        :return: The pinned of this DtoCreationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._pinned

    @pinned.setter
    def pinned(self, pinned):
        """Sets the pinned of this DtoCreationRequest.


        :param pinned: The pinned of this DtoCreationRequest.  # noqa: E501
        :type: bool
        """

        self._pinned = pinned

    @property
    def preferences(self):
        """Gets the preferences of this DtoCreationRequest.  # noqa: E501


        :return: The preferences of this DtoCreationRequest.  # noqa: E501
        :rtype: object
        """
        return self._preferences

    @preferences.setter
    def preferences(self, preferences):
        """Sets the preferences of this DtoCreationRequest.


        :param preferences: The preferences of this DtoCreationRequest.  # noqa: E501
        :type: object
        """

        self._preferences = preferences

    @property
    def query(self):
        """Gets the query of this DtoCreationRequest.  # noqa: E501


        :return: The query of this DtoCreationRequest.  # noqa: E501
        :rtype: DtoQueryRequest
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this DtoCreationRequest.


        :param query: The query of this DtoCreationRequest.  # noqa: E501
        :type: DtoQueryRequest
        """
        if self._configuration.client_side_validation and query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def source(self):
        """Gets the source of this DtoCreationRequest.  # noqa: E501


        :return: The source of this DtoCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DtoCreationRequest.


        :param source: The source of this DtoCreationRequest.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def type(self):
        """Gets the type of this DtoCreationRequest.  # noqa: E501


        :return: The type of this DtoCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DtoCreationRequest.


        :param type: The type of this DtoCreationRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(DtoCreationRequest, dict):
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
        if not isinstance(other, DtoCreationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DtoCreationRequest):
            return True

        return self.to_dict() != other.to_dict()
