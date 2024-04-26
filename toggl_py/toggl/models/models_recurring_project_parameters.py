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


class ModelsRecurringProjectParameters:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "custom_period": "int",
        "estimated_seconds": "int",
        "parameter_end_date": "str",
        "parameter_start_date": "str",
        "period": "str",
        "project_start_date": "str",
    }

    attribute_map = {
        "custom_period": "custom_period",
        "estimated_seconds": "estimated_seconds",
        "parameter_end_date": "parameter_end_date",
        "parameter_start_date": "parameter_start_date",
        "period": "period",
        "project_start_date": "project_start_date",
    }

    def __init__(
        self,
        custom_period=None,
        estimated_seconds=None,
        parameter_end_date=None,
        parameter_start_date=None,
        period=None,
        project_start_date=None,
        _configuration=None,
    ):  # noqa: E501
        """ModelsRecurringProjectParameters - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._custom_period = None
        self._estimated_seconds = None
        self._parameter_end_date = None
        self._parameter_start_date = None
        self._period = None
        self._project_start_date = None
        self.discriminator = None

        if custom_period is not None:
            self.custom_period = custom_period
        if estimated_seconds is not None:
            self.estimated_seconds = estimated_seconds
        if parameter_end_date is not None:
            self.parameter_end_date = parameter_end_date
        if parameter_start_date is not None:
            self.parameter_start_date = parameter_start_date
        if period is not None:
            self.period = period
        if project_start_date is not None:
            self.project_start_date = project_start_date

    @property
    def custom_period(self):
        """Gets the custom_period of this ModelsRecurringProjectParameters.  # noqa: E501

        Custom period, used when \"period\" field is \"custom\"  # noqa: E501

        :return: The custom_period of this ModelsRecurringProjectParameters.  # noqa: E501
        :rtype: int
        """
        return self._custom_period

    @custom_period.setter
    def custom_period(self, custom_period):
        """Sets the custom_period of this ModelsRecurringProjectParameters.

        Custom period, used when \"period\" field is \"custom\"  # noqa: E501

        :param custom_period: The custom_period of this ModelsRecurringProjectParameters.  # noqa: E501
        :type: int
        """

        self._custom_period = custom_period

    @property
    def estimated_seconds(self):
        """Gets the estimated_seconds of this ModelsRecurringProjectParameters.  # noqa: E501

        Estimated seconds  # noqa: E501

        :return: The estimated_seconds of this ModelsRecurringProjectParameters.  # noqa: E501
        :rtype: int
        """
        return self._estimated_seconds

    @estimated_seconds.setter
    def estimated_seconds(self, estimated_seconds):
        """Sets the estimated_seconds of this ModelsRecurringProjectParameters.

        Estimated seconds  # noqa: E501

        :param estimated_seconds: The estimated_seconds of this ModelsRecurringProjectParameters.  # noqa: E501
        :type: int
        """

        self._estimated_seconds = estimated_seconds

    @property
    def parameter_end_date(self):
        """Gets the parameter_end_date of this ModelsRecurringProjectParameters.  # noqa: E501

        Recurring end date  # noqa: E501

        :return: The parameter_end_date of this ModelsRecurringProjectParameters.  # noqa: E501
        :rtype: str
        """
        return self._parameter_end_date

    @parameter_end_date.setter
    def parameter_end_date(self, parameter_end_date):
        """Sets the parameter_end_date of this ModelsRecurringProjectParameters.

        Recurring end date  # noqa: E501

        :param parameter_end_date: The parameter_end_date of this ModelsRecurringProjectParameters.  # noqa: E501
        :type: str
        """

        self._parameter_end_date = parameter_end_date

    @property
    def parameter_start_date(self):
        """Gets the parameter_start_date of this ModelsRecurringProjectParameters.  # noqa: E501

        Recurring start date  # noqa: E501

        :return: The parameter_start_date of this ModelsRecurringProjectParameters.  # noqa: E501
        :rtype: str
        """
        return self._parameter_start_date

    @parameter_start_date.setter
    def parameter_start_date(self, parameter_start_date):
        """Sets the parameter_start_date of this ModelsRecurringProjectParameters.

        Recurring start date  # noqa: E501

        :param parameter_start_date: The parameter_start_date of this ModelsRecurringProjectParameters.  # noqa: E501
        :type: str
        """

        self._parameter_start_date = parameter_start_date

    @property
    def period(self):
        """Gets the period of this ModelsRecurringProjectParameters.  # noqa: E501

        Period  # noqa: E501

        :return: The period of this ModelsRecurringProjectParameters.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ModelsRecurringProjectParameters.

        Period  # noqa: E501

        :param period: The period of this ModelsRecurringProjectParameters.  # noqa: E501
        :type: str
        """

        self._period = period

    @property
    def project_start_date(self):
        """Gets the project_start_date of this ModelsRecurringProjectParameters.  # noqa: E501

        Project start date  # noqa: E501

        :return: The project_start_date of this ModelsRecurringProjectParameters.  # noqa: E501
        :rtype: str
        """
        return self._project_start_date

    @project_start_date.setter
    def project_start_date(self, project_start_date):
        """Sets the project_start_date of this ModelsRecurringProjectParameters.

        Project start date  # noqa: E501

        :param project_start_date: The project_start_date of this ModelsRecurringProjectParameters.  # noqa: E501
        :type: str
        """

        self._project_start_date = project_start_date

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
        if issubclass(ModelsRecurringProjectParameters, dict):
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
        if not isinstance(other, ModelsRecurringProjectParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsRecurringProjectParameters):
            return True

        return self.to_dict() != other.to_dict()