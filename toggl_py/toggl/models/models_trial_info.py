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


class ModelsTrialInfo:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "can_have_trial": "bool",
        "last_pricing_plan_id": "int",
        "next_payment_date": "str",
        "trial": "bool",
        "trial_available": "bool",
        "trial_end_date": "str",
    }

    attribute_map = {
        "can_have_trial": "can_have_trial",
        "last_pricing_plan_id": "last_pricing_plan_id",
        "next_payment_date": "next_payment_date",
        "trial": "trial",
        "trial_available": "trial_available",
        "trial_end_date": "trial_end_date",
    }

    def __init__(
        self,
        can_have_trial=None,
        last_pricing_plan_id=None,
        next_payment_date=None,
        trial=None,
        trial_available=None,
        trial_end_date=None,
        _configuration=None,
    ):  # noqa: E501
        """ModelsTrialInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._can_have_trial = None
        self._last_pricing_plan_id = None
        self._next_payment_date = None
        self._trial = None
        self._trial_available = None
        self._trial_end_date = None
        self.discriminator = None

        if can_have_trial is not None:
            self.can_have_trial = can_have_trial
        if last_pricing_plan_id is not None:
            self.last_pricing_plan_id = last_pricing_plan_id
        if next_payment_date is not None:
            self.next_payment_date = next_payment_date
        if trial is not None:
            self.trial = trial
        if trial_available is not None:
            self.trial_available = trial_available
        if trial_end_date is not None:
            self.trial_end_date = trial_end_date

    @property
    def can_have_trial(self):
        """Gets the can_have_trial of this ModelsTrialInfo.  # noqa: E501

        CanHaveInitialTrial is true if neither the organization nor the owner has never had a trial before  # noqa: E501

        :return: The can_have_trial of this ModelsTrialInfo.  # noqa: E501
        :rtype: bool
        """
        return self._can_have_trial

    @can_have_trial.setter
    def can_have_trial(self, can_have_trial):
        """Sets the can_have_trial of this ModelsTrialInfo.

        CanHaveInitialTrial is true if neither the organization nor the owner has never had a trial before  # noqa: E501

        :param can_have_trial: The can_have_trial of this ModelsTrialInfo.  # noqa: E501
        :type: bool
        """

        self._can_have_trial = can_have_trial

    @property
    def last_pricing_plan_id(self):
        """Gets the last_pricing_plan_id of this ModelsTrialInfo.  # noqa: E501

        What was the previous plan before the trial  # noqa: E501

        :return: The last_pricing_plan_id of this ModelsTrialInfo.  # noqa: E501
        :rtype: int
        """
        return self._last_pricing_plan_id

    @last_pricing_plan_id.setter
    def last_pricing_plan_id(self, last_pricing_plan_id):
        """Sets the last_pricing_plan_id of this ModelsTrialInfo.

        What was the previous plan before the trial  # noqa: E501

        :param last_pricing_plan_id: The last_pricing_plan_id of this ModelsTrialInfo.  # noqa: E501
        :type: int
        """

        self._last_pricing_plan_id = last_pricing_plan_id

    @property
    def next_payment_date(self):
        """Gets the next_payment_date of this ModelsTrialInfo.  # noqa: E501

        When the trial payment is due  # noqa: E501

        :return: The next_payment_date of this ModelsTrialInfo.  # noqa: E501
        :rtype: str
        """
        return self._next_payment_date

    @next_payment_date.setter
    def next_payment_date(self, next_payment_date):
        """Sets the next_payment_date of this ModelsTrialInfo.

        When the trial payment is due  # noqa: E501

        :param next_payment_date: The next_payment_date of this ModelsTrialInfo.  # noqa: E501
        :type: str
        """

        self._next_payment_date = next_payment_date

    @property
    def trial(self):
        """Gets the trial of this ModelsTrialInfo.  # noqa: E501

        Whether the organization's subscription is currently on trial  # noqa: E501

        :return: The trial of this ModelsTrialInfo.  # noqa: E501
        :rtype: bool
        """
        return self._trial

    @trial.setter
    def trial(self, trial):
        """Sets the trial of this ModelsTrialInfo.

        Whether the organization's subscription is currently on trial  # noqa: E501

        :param trial: The trial of this ModelsTrialInfo.  # noqa: E501
        :type: bool
        """

        self._trial = trial

    @property
    def trial_available(self):
        """Gets the trial_available of this ModelsTrialInfo.  # noqa: E501

        When a trial is available for this organization  # noqa: E501

        :return: The trial_available of this ModelsTrialInfo.  # noqa: E501
        :rtype: bool
        """
        return self._trial_available

    @trial_available.setter
    def trial_available(self, trial_available):
        """Sets the trial_available of this ModelsTrialInfo.

        When a trial is available for this organization  # noqa: E501

        :param trial_available: The trial_available of this ModelsTrialInfo.  # noqa: E501
        :type: bool
        """

        self._trial_available = trial_available

    @property
    def trial_end_date(self):
        """Gets the trial_end_date of this ModelsTrialInfo.  # noqa: E501

        When the trial ends  # noqa: E501

        :return: The trial_end_date of this ModelsTrialInfo.  # noqa: E501
        :rtype: str
        """
        return self._trial_end_date

    @trial_end_date.setter
    def trial_end_date(self, trial_end_date):
        """Sets the trial_end_date of this ModelsTrialInfo.

        When the trial ends  # noqa: E501

        :param trial_end_date: The trial_end_date of this ModelsTrialInfo.  # noqa: E501
        :type: str
        """

        self._trial_end_date = trial_end_date

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
        if issubclass(ModelsTrialInfo, dict):
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
        if not isinstance(other, ModelsTrialInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsTrialInfo):
            return True

        return self.to_dict() != other.to_dict()
