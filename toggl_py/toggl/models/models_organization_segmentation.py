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


class ModelsOrganizationSegmentation:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "demo_requested": "bool",
        "full_name": "str",
        "heard": "str",
        "industries": "str",
        "members_range": "str",
        "organization_id": "int",
        "reasons": "str",
        "skipped_step": "str",
        "user_id": "int",
    }

    attribute_map = {
        "demo_requested": "demo_requested",
        "full_name": "full_name",
        "heard": "heard",
        "industries": "industries",
        "members_range": "members_range",
        "organization_id": "organization_id",
        "reasons": "reasons",
        "skipped_step": "skipped_step",
        "user_id": "user_id",
    }

    def __init__(
        self,
        demo_requested=None,
        full_name=None,
        heard=None,
        industries=None,
        members_range=None,
        organization_id=None,
        reasons=None,
        skipped_step=None,
        user_id=None,
        _configuration=None,
    ):  # noqa: E501
        """ModelsOrganizationSegmentation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._demo_requested = None
        self._full_name = None
        self._heard = None
        self._industries = None
        self._members_range = None
        self._organization_id = None
        self._reasons = None
        self._skipped_step = None
        self._user_id = None
        self.discriminator = None

        if demo_requested is not None:
            self.demo_requested = demo_requested
        if full_name is not None:
            self.full_name = full_name
        if heard is not None:
            self.heard = heard
        if industries is not None:
            self.industries = industries
        if members_range is not None:
            self.members_range = members_range
        if organization_id is not None:
            self.organization_id = organization_id
        if reasons is not None:
            self.reasons = reasons
        if skipped_step is not None:
            self.skipped_step = skipped_step
        if user_id is not None:
            self.user_id = user_id

    @property
    def demo_requested(self):
        """Gets the demo_requested of this ModelsOrganizationSegmentation.  # noqa: E501


        :return: The demo_requested of this ModelsOrganizationSegmentation.  # noqa: E501
        :rtype: bool
        """
        return self._demo_requested

    @demo_requested.setter
    def demo_requested(self, demo_requested):
        """Sets the demo_requested of this ModelsOrganizationSegmentation.


        :param demo_requested: The demo_requested of this ModelsOrganizationSegmentation.  # noqa: E501
        :type: bool
        """

        self._demo_requested = demo_requested

    @property
    def full_name(self):
        """Gets the full_name of this ModelsOrganizationSegmentation.  # noqa: E501


        :return: The full_name of this ModelsOrganizationSegmentation.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this ModelsOrganizationSegmentation.


        :param full_name: The full_name of this ModelsOrganizationSegmentation.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def heard(self):
        """Gets the heard of this ModelsOrganizationSegmentation.  # noqa: E501


        :return: The heard of this ModelsOrganizationSegmentation.  # noqa: E501
        :rtype: str
        """
        return self._heard

    @heard.setter
    def heard(self, heard):
        """Sets the heard of this ModelsOrganizationSegmentation.


        :param heard: The heard of this ModelsOrganizationSegmentation.  # noqa: E501
        :type: str
        """

        self._heard = heard

    @property
    def industries(self):
        """Gets the industries of this ModelsOrganizationSegmentation.  # noqa: E501


        :return: The industries of this ModelsOrganizationSegmentation.  # noqa: E501
        :rtype: str
        """
        return self._industries

    @industries.setter
    def industries(self, industries):
        """Sets the industries of this ModelsOrganizationSegmentation.


        :param industries: The industries of this ModelsOrganizationSegmentation.  # noqa: E501
        :type: str
        """

        self._industries = industries

    @property
    def members_range(self):
        """Gets the members_range of this ModelsOrganizationSegmentation.  # noqa: E501


        :return: The members_range of this ModelsOrganizationSegmentation.  # noqa: E501
        :rtype: str
        """
        return self._members_range

    @members_range.setter
    def members_range(self, members_range):
        """Sets the members_range of this ModelsOrganizationSegmentation.


        :param members_range: The members_range of this ModelsOrganizationSegmentation.  # noqa: E501
        :type: str
        """

        self._members_range = members_range

    @property
    def organization_id(self):
        """Gets the organization_id of this ModelsOrganizationSegmentation.  # noqa: E501


        :return: The organization_id of this ModelsOrganizationSegmentation.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this ModelsOrganizationSegmentation.


        :param organization_id: The organization_id of this ModelsOrganizationSegmentation.  # noqa: E501
        :type: int
        """

        self._organization_id = organization_id

    @property
    def reasons(self):
        """Gets the reasons of this ModelsOrganizationSegmentation.  # noqa: E501


        :return: The reasons of this ModelsOrganizationSegmentation.  # noqa: E501
        :rtype: str
        """
        return self._reasons

    @reasons.setter
    def reasons(self, reasons):
        """Sets the reasons of this ModelsOrganizationSegmentation.


        :param reasons: The reasons of this ModelsOrganizationSegmentation.  # noqa: E501
        :type: str
        """

        self._reasons = reasons

    @property
    def skipped_step(self):
        """Gets the skipped_step of this ModelsOrganizationSegmentation.  # noqa: E501


        :return: The skipped_step of this ModelsOrganizationSegmentation.  # noqa: E501
        :rtype: str
        """
        return self._skipped_step

    @skipped_step.setter
    def skipped_step(self, skipped_step):
        """Sets the skipped_step of this ModelsOrganizationSegmentation.


        :param skipped_step: The skipped_step of this ModelsOrganizationSegmentation.  # noqa: E501
        :type: str
        """

        self._skipped_step = skipped_step

    @property
    def user_id(self):
        """Gets the user_id of this ModelsOrganizationSegmentation.  # noqa: E501


        :return: The user_id of this ModelsOrganizationSegmentation.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ModelsOrganizationSegmentation.


        :param user_id: The user_id of this ModelsOrganizationSegmentation.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

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
        if issubclass(ModelsOrganizationSegmentation, dict):
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
        if not isinstance(other, ModelsOrganizationSegmentation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsOrganizationSegmentation):
            return True

        return self.to_dict() != other.to_dict()
