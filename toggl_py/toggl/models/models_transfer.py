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


class ModelsTransfer:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "created_at": "str",
        "current_owner_accepted": "bool",
        "current_owner_answered_at": "str",
        "current_owner_id": "int",
        "finished_at": "str",
        "new_owner_accepted": "bool",
        "new_owner_answered_at": "str",
        "new_owner_id": "int",
        "organization_id": "int",
        "outcome_name": "str",
        "owner_transfer_id": "int",
        "requester_id": "int",
    }

    attribute_map = {
        "created_at": "created_at",
        "current_owner_accepted": "current_owner_accepted",
        "current_owner_answered_at": "current_owner_answered_at",
        "current_owner_id": "current_owner_id",
        "finished_at": "finished_at",
        "new_owner_accepted": "new_owner_accepted",
        "new_owner_answered_at": "new_owner_answered_at",
        "new_owner_id": "new_owner_id",
        "organization_id": "organization_id",
        "outcome_name": "outcome_name",
        "owner_transfer_id": "owner_transfer_id",
        "requester_id": "requester_id",
    }

    def __init__(
        self,
        created_at=None,
        current_owner_accepted=None,
        current_owner_answered_at=None,
        current_owner_id=None,
        finished_at=None,
        new_owner_accepted=None,
        new_owner_answered_at=None,
        new_owner_id=None,
        organization_id=None,
        outcome_name=None,
        owner_transfer_id=None,
        requester_id=None,
        _configuration=None,
    ):  # noqa: E501
        """ModelsTransfer - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_at = None
        self._current_owner_accepted = None
        self._current_owner_answered_at = None
        self._current_owner_id = None
        self._finished_at = None
        self._new_owner_accepted = None
        self._new_owner_answered_at = None
        self._new_owner_id = None
        self._organization_id = None
        self._outcome_name = None
        self._owner_transfer_id = None
        self._requester_id = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if current_owner_accepted is not None:
            self.current_owner_accepted = current_owner_accepted
        if current_owner_answered_at is not None:
            self.current_owner_answered_at = current_owner_answered_at
        if current_owner_id is not None:
            self.current_owner_id = current_owner_id
        if finished_at is not None:
            self.finished_at = finished_at
        if new_owner_accepted is not None:
            self.new_owner_accepted = new_owner_accepted
        if new_owner_answered_at is not None:
            self.new_owner_answered_at = new_owner_answered_at
        if new_owner_id is not None:
            self.new_owner_id = new_owner_id
        if organization_id is not None:
            self.organization_id = organization_id
        if outcome_name is not None:
            self.outcome_name = outcome_name
        if owner_transfer_id is not None:
            self.owner_transfer_id = owner_transfer_id
        if requester_id is not None:
            self.requester_id = requester_id

    @property
    def created_at(self):
        """Gets the created_at of this ModelsTransfer.  # noqa: E501


        :return: The created_at of this ModelsTransfer.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ModelsTransfer.


        :param created_at: The created_at of this ModelsTransfer.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def current_owner_accepted(self):
        """Gets the current_owner_accepted of this ModelsTransfer.  # noqa: E501


        :return: The current_owner_accepted of this ModelsTransfer.  # noqa: E501
        :rtype: bool
        """
        return self._current_owner_accepted

    @current_owner_accepted.setter
    def current_owner_accepted(self, current_owner_accepted):
        """Sets the current_owner_accepted of this ModelsTransfer.


        :param current_owner_accepted: The current_owner_accepted of this ModelsTransfer.  # noqa: E501
        :type: bool
        """

        self._current_owner_accepted = current_owner_accepted

    @property
    def current_owner_answered_at(self):
        """Gets the current_owner_answered_at of this ModelsTransfer.  # noqa: E501


        :return: The current_owner_answered_at of this ModelsTransfer.  # noqa: E501
        :rtype: str
        """
        return self._current_owner_answered_at

    @current_owner_answered_at.setter
    def current_owner_answered_at(self, current_owner_answered_at):
        """Sets the current_owner_answered_at of this ModelsTransfer.


        :param current_owner_answered_at: The current_owner_answered_at of this ModelsTransfer.  # noqa: E501
        :type: str
        """

        self._current_owner_answered_at = current_owner_answered_at

    @property
    def current_owner_id(self):
        """Gets the current_owner_id of this ModelsTransfer.  # noqa: E501


        :return: The current_owner_id of this ModelsTransfer.  # noqa: E501
        :rtype: int
        """
        return self._current_owner_id

    @current_owner_id.setter
    def current_owner_id(self, current_owner_id):
        """Sets the current_owner_id of this ModelsTransfer.


        :param current_owner_id: The current_owner_id of this ModelsTransfer.  # noqa: E501
        :type: int
        """

        self._current_owner_id = current_owner_id

    @property
    def finished_at(self):
        """Gets the finished_at of this ModelsTransfer.  # noqa: E501


        :return: The finished_at of this ModelsTransfer.  # noqa: E501
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this ModelsTransfer.


        :param finished_at: The finished_at of this ModelsTransfer.  # noqa: E501
        :type: str
        """

        self._finished_at = finished_at

    @property
    def new_owner_accepted(self):
        """Gets the new_owner_accepted of this ModelsTransfer.  # noqa: E501


        :return: The new_owner_accepted of this ModelsTransfer.  # noqa: E501
        :rtype: bool
        """
        return self._new_owner_accepted

    @new_owner_accepted.setter
    def new_owner_accepted(self, new_owner_accepted):
        """Sets the new_owner_accepted of this ModelsTransfer.


        :param new_owner_accepted: The new_owner_accepted of this ModelsTransfer.  # noqa: E501
        :type: bool
        """

        self._new_owner_accepted = new_owner_accepted

    @property
    def new_owner_answered_at(self):
        """Gets the new_owner_answered_at of this ModelsTransfer.  # noqa: E501


        :return: The new_owner_answered_at of this ModelsTransfer.  # noqa: E501
        :rtype: str
        """
        return self._new_owner_answered_at

    @new_owner_answered_at.setter
    def new_owner_answered_at(self, new_owner_answered_at):
        """Sets the new_owner_answered_at of this ModelsTransfer.


        :param new_owner_answered_at: The new_owner_answered_at of this ModelsTransfer.  # noqa: E501
        :type: str
        """

        self._new_owner_answered_at = new_owner_answered_at

    @property
    def new_owner_id(self):
        """Gets the new_owner_id of this ModelsTransfer.  # noqa: E501


        :return: The new_owner_id of this ModelsTransfer.  # noqa: E501
        :rtype: int
        """
        return self._new_owner_id

    @new_owner_id.setter
    def new_owner_id(self, new_owner_id):
        """Sets the new_owner_id of this ModelsTransfer.


        :param new_owner_id: The new_owner_id of this ModelsTransfer.  # noqa: E501
        :type: int
        """

        self._new_owner_id = new_owner_id

    @property
    def organization_id(self):
        """Gets the organization_id of this ModelsTransfer.  # noqa: E501


        :return: The organization_id of this ModelsTransfer.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this ModelsTransfer.


        :param organization_id: The organization_id of this ModelsTransfer.  # noqa: E501
        :type: int
        """

        self._organization_id = organization_id

    @property
    def outcome_name(self):
        """Gets the outcome_name of this ModelsTransfer.  # noqa: E501


        :return: The outcome_name of this ModelsTransfer.  # noqa: E501
        :rtype: str
        """
        return self._outcome_name

    @outcome_name.setter
    def outcome_name(self, outcome_name):
        """Sets the outcome_name of this ModelsTransfer.


        :param outcome_name: The outcome_name of this ModelsTransfer.  # noqa: E501
        :type: str
        """

        self._outcome_name = outcome_name

    @property
    def owner_transfer_id(self):
        """Gets the owner_transfer_id of this ModelsTransfer.  # noqa: E501


        :return: The owner_transfer_id of this ModelsTransfer.  # noqa: E501
        :rtype: int
        """
        return self._owner_transfer_id

    @owner_transfer_id.setter
    def owner_transfer_id(self, owner_transfer_id):
        """Sets the owner_transfer_id of this ModelsTransfer.


        :param owner_transfer_id: The owner_transfer_id of this ModelsTransfer.  # noqa: E501
        :type: int
        """

        self._owner_transfer_id = owner_transfer_id

    @property
    def requester_id(self):
        """Gets the requester_id of this ModelsTransfer.  # noqa: E501


        :return: The requester_id of this ModelsTransfer.  # noqa: E501
        :rtype: int
        """
        return self._requester_id

    @requester_id.setter
    def requester_id(self, requester_id):
        """Sets the requester_id of this ModelsTransfer.


        :param requester_id: The requester_id of this ModelsTransfer.  # noqa: E501
        :type: int
        """

        self._requester_id = requester_id

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
        if issubclass(ModelsTransfer, dict):
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
        if not isinstance(other, ModelsTransfer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsTransfer):
            return True

        return self.to_dict() != other.to_dict()