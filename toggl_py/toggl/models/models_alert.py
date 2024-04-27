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


class ModelsAlert:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "errors": "list[ModelsAlertError]",
        "id": "int",
        "object_type": "int",
        "project_id": "int",
        "receiver_groups": "str",
        "receiver_roles": "str",
        "receiver_users": "str",
        "receivers": "int",
        "source_kind": "str",
        "threshold": "int",
        "threshold_type": "str",
        "thresholds": "str",
        "wid": "int",
    }

    attribute_map = {
        "errors": "errors",
        "id": "id",
        "object_type": "object_type",
        "project_id": "project_id",
        "receiver_groups": "receiver_groups",
        "receiver_roles": "receiver_roles",
        "receiver_users": "receiver_users",
        "receivers": "receivers",
        "source_kind": "source_kind",
        "threshold": "threshold",
        "threshold_type": "threshold_type",
        "thresholds": "thresholds",
        "wid": "wid",
    }

    def __init__(
        self,
        errors=None,
        id=None,
        object_type=None,
        project_id=None,
        receiver_groups=None,
        receiver_roles=None,
        receiver_users=None,
        receivers=None,
        source_kind=None,
        threshold=None,
        threshold_type=None,
        thresholds=None,
        wid=None,
        _configuration=None,
    ):  # noqa: E501
        """ModelsAlert - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._errors = None
        self._id = None
        self._object_type = None
        self._project_id = None
        self._receiver_groups = None
        self._receiver_roles = None
        self._receiver_users = None
        self._receivers = None
        self._source_kind = None
        self._threshold = None
        self._threshold_type = None
        self._thresholds = None
        self._wid = None
        self.discriminator = None

        if errors is not None:
            self.errors = errors
        if id is not None:
            self.id = id
        if object_type is not None:
            self.object_type = object_type
        if project_id is not None:
            self.project_id = project_id
        if receiver_groups is not None:
            self.receiver_groups = receiver_groups
        if receiver_roles is not None:
            self.receiver_roles = receiver_roles
        if receiver_users is not None:
            self.receiver_users = receiver_users
        if receivers is not None:
            self.receivers = receivers
        if source_kind is not None:
            self.source_kind = source_kind
        if threshold is not None:
            self.threshold = threshold
        if threshold_type is not None:
            self.threshold_type = threshold_type
        if thresholds is not None:
            self.thresholds = thresholds
        if wid is not None:
            self.wid = wid

    @property
    def errors(self):
        """Gets the errors of this ModelsAlert.  # noqa: E501


        :return: The errors of this ModelsAlert.  # noqa: E501
        :rtype: list[ModelsAlertError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ModelsAlert.


        :param errors: The errors of this ModelsAlert.  # noqa: E501
        :type: list[ModelsAlertError]
        """

        self._errors = errors

    @property
    def id(self):
        """Gets the id of this ModelsAlert.  # noqa: E501


        :return: The id of this ModelsAlert.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelsAlert.


        :param id: The id of this ModelsAlert.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def object_type(self):
        """Gets the object_type of this ModelsAlert.  # noqa: E501


        :return: The object_type of this ModelsAlert.  # noqa: E501
        :rtype: int
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this ModelsAlert.


        :param object_type: The object_type of this ModelsAlert.  # noqa: E501
        :type: int
        """

        self._object_type = object_type

    @property
    def project_id(self):
        """Gets the project_id of this ModelsAlert.  # noqa: E501


        :return: The project_id of this ModelsAlert.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ModelsAlert.


        :param project_id: The project_id of this ModelsAlert.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def receiver_groups(self):
        """Gets the receiver_groups of this ModelsAlert.  # noqa: E501


        :return: The receiver_groups of this ModelsAlert.  # noqa: E501
        :rtype: str
        """
        return self._receiver_groups

    @receiver_groups.setter
    def receiver_groups(self, receiver_groups):
        """Sets the receiver_groups of this ModelsAlert.


        :param receiver_groups: The receiver_groups of this ModelsAlert.  # noqa: E501
        :type: str
        """

        self._receiver_groups = receiver_groups

    @property
    def receiver_roles(self):
        """Gets the receiver_roles of this ModelsAlert.  # noqa: E501


        :return: The receiver_roles of this ModelsAlert.  # noqa: E501
        :rtype: str
        """
        return self._receiver_roles

    @receiver_roles.setter
    def receiver_roles(self, receiver_roles):
        """Sets the receiver_roles of this ModelsAlert.


        :param receiver_roles: The receiver_roles of this ModelsAlert.  # noqa: E501
        :type: str
        """

        self._receiver_roles = receiver_roles

    @property
    def receiver_users(self):
        """Gets the receiver_users of this ModelsAlert.  # noqa: E501


        :return: The receiver_users of this ModelsAlert.  # noqa: E501
        :rtype: str
        """
        return self._receiver_users

    @receiver_users.setter
    def receiver_users(self, receiver_users):
        """Sets the receiver_users of this ModelsAlert.


        :param receiver_users: The receiver_users of this ModelsAlert.  # noqa: E501
        :type: str
        """

        self._receiver_users = receiver_users

    @property
    def receivers(self):
        """Gets the receivers of this ModelsAlert.  # noqa: E501


        :return: The receivers of this ModelsAlert.  # noqa: E501
        :rtype: int
        """
        return self._receivers

    @receivers.setter
    def receivers(self, receivers):
        """Sets the receivers of this ModelsAlert.


        :param receivers: The receivers of this ModelsAlert.  # noqa: E501
        :type: int
        """

        self._receivers = receivers

    @property
    def source_kind(self):
        """Gets the source_kind of this ModelsAlert.  # noqa: E501


        :return: The source_kind of this ModelsAlert.  # noqa: E501
        :rtype: str
        """
        return self._source_kind

    @source_kind.setter
    def source_kind(self, source_kind):
        """Sets the source_kind of this ModelsAlert.


        :param source_kind: The source_kind of this ModelsAlert.  # noqa: E501
        :type: str
        """

        self._source_kind = source_kind

    @property
    def threshold(self):
        """Gets the threshold of this ModelsAlert.  # noqa: E501


        :return: The threshold of this ModelsAlert.  # noqa: E501
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this ModelsAlert.


        :param threshold: The threshold of this ModelsAlert.  # noqa: E501
        :type: int
        """

        self._threshold = threshold

    @property
    def threshold_type(self):
        """Gets the threshold_type of this ModelsAlert.  # noqa: E501


        :return: The threshold_type of this ModelsAlert.  # noqa: E501
        :rtype: str
        """
        return self._threshold_type

    @threshold_type.setter
    def threshold_type(self, threshold_type):
        """Sets the threshold_type of this ModelsAlert.


        :param threshold_type: The threshold_type of this ModelsAlert.  # noqa: E501
        :type: str
        """

        self._threshold_type = threshold_type

    @property
    def thresholds(self):
        """Gets the thresholds of this ModelsAlert.  # noqa: E501

        using pq types is a workaround to enable reading postgres arrays into go types we should wrap these pq types to avoid polluting our domain  # noqa: E501

        :return: The thresholds of this ModelsAlert.  # noqa: E501
        :rtype: str
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """Sets the thresholds of this ModelsAlert.

        using pq types is a workaround to enable reading postgres arrays into go types we should wrap these pq types to avoid polluting our domain  # noqa: E501

        :param thresholds: The thresholds of this ModelsAlert.  # noqa: E501
        :type: str
        """

        self._thresholds = thresholds

    @property
    def wid(self):
        """Gets the wid of this ModelsAlert.  # noqa: E501


        :return: The wid of this ModelsAlert.  # noqa: E501
        :rtype: int
        """
        return self._wid

    @wid.setter
    def wid(self, wid):
        """Sets the wid of this ModelsAlert.


        :param wid: The wid of this ModelsAlert.  # noqa: E501
        :type: int
        """

        self._wid = wid

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
        if issubclass(ModelsAlert, dict):
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
        if not isinstance(other, ModelsAlert):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsAlert):
            return True

        return self.to_dict() != other.to_dict()
