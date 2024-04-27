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


class SummaryAudit:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"group_filter": "SummaryAuditGroupFilter", "show_empty_groups": "bool", "show_tracked_groups": "bool"}

    attribute_map = {
        "group_filter": "group_filter",
        "show_empty_groups": "show_empty_groups",
        "show_tracked_groups": "show_tracked_groups",
    }

    def __init__(self, group_filter=None, show_empty_groups=None, show_tracked_groups=None, _configuration=None):  # noqa: E501
        """SummaryAudit - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._group_filter = None
        self._show_empty_groups = None
        self._show_tracked_groups = None
        self.discriminator = None

        if group_filter is not None:
            self.group_filter = group_filter
        if show_empty_groups is not None:
            self.show_empty_groups = show_empty_groups
        if show_tracked_groups is not None:
            self.show_tracked_groups = show_tracked_groups

    @property
    def group_filter(self):
        """Gets the group_filter of this SummaryAudit.  # noqa: E501


        :return: The group_filter of this SummaryAudit.  # noqa: E501
        :rtype: SummaryAuditGroupFilter
        """
        return self._group_filter

    @group_filter.setter
    def group_filter(self, group_filter):
        """Sets the group_filter of this SummaryAudit.


        :param group_filter: The group_filter of this SummaryAudit.  # noqa: E501
        :type: SummaryAuditGroupFilter
        """

        self._group_filter = group_filter

    @property
    def show_empty_groups(self):
        """Gets the show_empty_groups of this SummaryAudit.  # noqa: E501

        Whether empty groups should be displayed, default false, premium feature.  # noqa: E501

        :return: The show_empty_groups of this SummaryAudit.  # noqa: E501
        :rtype: bool
        """
        return self._show_empty_groups

    @show_empty_groups.setter
    def show_empty_groups(self, show_empty_groups):
        """Sets the show_empty_groups of this SummaryAudit.

        Whether empty groups should be displayed, default false, premium feature.  # noqa: E501

        :param show_empty_groups: The show_empty_groups of this SummaryAudit.  # noqa: E501
        :type: bool
        """

        self._show_empty_groups = show_empty_groups

    @property
    def show_tracked_groups(self):
        """Gets the show_tracked_groups of this SummaryAudit.  # noqa: E501

        Whether tacked groups should be displayed, default true, premium feature.  # noqa: E501

        :return: The show_tracked_groups of this SummaryAudit.  # noqa: E501
        :rtype: bool
        """
        return self._show_tracked_groups

    @show_tracked_groups.setter
    def show_tracked_groups(self, show_tracked_groups):
        """Sets the show_tracked_groups of this SummaryAudit.

        Whether tacked groups should be displayed, default true, premium feature.  # noqa: E501

        :param show_tracked_groups: The show_tracked_groups of this SummaryAudit.  # noqa: E501
        :type: bool
        """

        self._show_tracked_groups = show_tracked_groups

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
        if issubclass(SummaryAudit, dict):
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
        if not isinstance(other, SummaryAudit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SummaryAudit):
            return True

        return self.to_dict() != other.to_dict()
