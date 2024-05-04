"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

from __future__ import annotations  # noqa: F401
import pprint
import re  # noqa: F401
from datetime import datetime  # noqa: F401
from typing import Any

from toggl.configuration import Configuration
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from toggl.models.project_recurring_parameters import ProjectRecurringParameters  # noqa: F401


class ProjectPayload:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "active": "bool",
        "auto_estimates": "bool",
        "billable": "bool",
        "cid": "int",
        "client_id": "int",
        "client_name": "str",
        "color": "str",
        "currency": "str",
        "end_date": "str",
        "estimated_hours": "int",
        "fixed_fee": "float",
        "is_private": "bool",
        "name": "str",
        "rate": "float",
        "rate_change_mode": "str",
        "recurring": "bool",
        "recurring_parameters": "ProjectRecurringParameters",
        "start_date": "str",
        "template": "bool",
        "template_id": "int",
    }

    attribute_map = {
        "active": "active",
        "auto_estimates": "auto_estimates",
        "billable": "billable",
        "cid": "cid",
        "client_id": "client_id",
        "client_name": "client_name",
        "color": "color",
        "currency": "currency",
        "end_date": "end_date",
        "estimated_hours": "estimated_hours",
        "fixed_fee": "fixed_fee",
        "is_private": "is_private",
        "name": "name",
        "rate": "rate",
        "rate_change_mode": "rate_change_mode",
        "recurring": "recurring",
        "recurring_parameters": "recurring_parameters",
        "start_date": "start_date",
        "template": "template",
        "template_id": "template_id",
    }

    def __init__(
        self,
        active: bool = None,
        auto_estimates: bool = None,
        billable: bool = None,
        cid: int = None,
        client_id: int = None,
        client_name: str = None,
        color: str = None,
        currency: str = None,
        end_date: str = None,
        estimated_hours: int = None,
        fixed_fee: float = None,
        is_private: bool = None,
        name: str = None,
        rate: float = None,
        rate_change_mode: str = None,
        recurring: bool = None,
        recurring_parameters: ProjectRecurringParameters = None,
        start_date: str = None,
        template: bool = None,
        template_id: int = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        ProjectPayload - a model defined in Swagger

        Parameters:
          active (bool): Optional
          auto_estimates (bool): Optional
          billable (bool): Optional
          cid (int): Optional
          client_id (int): Optional
          client_name (str): Optional
          color (str): Optional
          currency (str): Optional
          end_date (str): Optional
          estimated_hours (int): Optional
          fixed_fee (float): Optional
          is_private (bool): Optional
          name (str): Optional
          rate (float): Optional
          rate_change_mode (str): Optional
          recurring (bool): Optional
          recurring_parameters (ProjectRecurringParameters): Optional
          start_date (str): Optional
          template (bool): Optional
          template_id (int): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active = None
        self._auto_estimates = None
        self._billable = None
        self._cid = None
        self._client_id = None
        self._client_name = None
        self._color = None
        self._currency = None
        self._end_date = None
        self._estimated_hours = None
        self._fixed_fee = None
        self._is_private = None
        self._name = None
        self._rate = None
        self._rate_change_mode = None
        self._recurring = None
        self._recurring_parameters = None
        self._start_date = None
        self._template = None
        self._template_id = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if auto_estimates is not None:
            self.auto_estimates = auto_estimates
        if billable is not None:
            self.billable = billable
        if cid is not None:
            self.cid = cid
        if client_id is not None:
            self.client_id = client_id
        if client_name is not None:
            self.client_name = client_name
        if color is not None:
            self.color = color
        if currency is not None:
            self.currency = currency
        if end_date is not None:
            self.end_date = end_date
        if estimated_hours is not None:
            self.estimated_hours = estimated_hours
        if fixed_fee is not None:
            self.fixed_fee = fixed_fee
        if is_private is not None:
            self.is_private = is_private
        if name is not None:
            self.name = name
        if rate is not None:
            self.rate = rate
        if rate_change_mode is not None:
            self.rate_change_mode = rate_change_mode
        if recurring is not None:
            self.recurring = recurring
        if recurring_parameters is not None:
            self.recurring_parameters = recurring_parameters
        if start_date is not None:
            self.start_date = start_date
        if template is not None:
            self.template = template
        if template_id is not None:
            self.template_id = template_id

    @property
    def active(self) -> bool:
        """Gets the active of this ProjectPayload.  # noqa: E501

        Whether the project is active or archived  # noqa: E501

        :return: The active of this ProjectPayload.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active: bool):
        """Sets the active of this ProjectPayload.

        Whether the project is active or archived  # noqa: E501

        :param active: The active of this ProjectPayload.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def auto_estimates(self) -> bool:
        """Gets the auto_estimates of this ProjectPayload.  # noqa: E501

        Whether estimates are based on task hours, optional, premium feature  # noqa: E501

        :return: The auto_estimates of this ProjectPayload.  # noqa: E501
        :rtype: bool
        """
        return self._auto_estimates

    @auto_estimates.setter
    def auto_estimates(self, auto_estimates: bool):
        """Sets the auto_estimates of this ProjectPayload.

        Whether estimates are based on task hours, optional, premium feature  # noqa: E501

        :param auto_estimates: The auto_estimates of this ProjectPayload.  # noqa: E501
        :type: bool
        """

        self._auto_estimates = auto_estimates

    @property
    def billable(self) -> bool:
        """Gets the billable of this ProjectPayload.  # noqa: E501

        Whether the project is set as billable, optional, premium feature  # noqa: E501

        :return: The billable of this ProjectPayload.  # noqa: E501
        :rtype: bool
        """
        return self._billable

    @billable.setter
    def billable(self, billable: bool):
        """Sets the billable of this ProjectPayload.

        Whether the project is set as billable, optional, premium feature  # noqa: E501

        :param billable: The billable of this ProjectPayload.  # noqa: E501
        :type: bool
        """

        self._billable = billable

    @property
    def cid(self) -> int:
        """Gets the cid of this ProjectPayload.  # noqa: E501

        Client ID, legacy  # noqa: E501

        :return: The cid of this ProjectPayload.  # noqa: E501
        :rtype: int
        """
        return self._cid

    @cid.setter
    def cid(self, cid: int):
        """Sets the cid of this ProjectPayload.

        Client ID, legacy  # noqa: E501

        :param cid: The cid of this ProjectPayload.  # noqa: E501
        :type: int
        """

        self._cid = cid

    @property
    def client_id(self) -> int:
        """Gets the client_id of this ProjectPayload.  # noqa: E501

        Client ID, optional  # noqa: E501

        :return: The client_id of this ProjectPayload.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id: int):
        """Sets the client_id of this ProjectPayload.

        Client ID, optional  # noqa: E501

        :param client_id: The client_id of this ProjectPayload.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def client_name(self) -> str:
        """Gets the client_name of this ProjectPayload.  # noqa: E501

        Client name, optional  # noqa: E501

        :return: The client_name of this ProjectPayload.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name: str):
        """Sets the client_name of this ProjectPayload.

        Client name, optional  # noqa: E501

        :param client_name: The client_name of this ProjectPayload.  # noqa: E501
        :type: str
        """

        self._client_name = client_name

    @property
    def color(self) -> str:
        """Gets the color of this ProjectPayload.  # noqa: E501

        Project color  # noqa: E501

        :return: The color of this ProjectPayload.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color: str):
        """Sets the color of this ProjectPayload.

        Project color  # noqa: E501

        :param color: The color of this ProjectPayload.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def currency(self) -> str:
        """Gets the currency of this ProjectPayload.  # noqa: E501

        Project currency, optional, premium feature  # noqa: E501

        :return: The currency of this ProjectPayload.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency: str):
        """Sets the currency of this ProjectPayload.

        Project currency, optional, premium feature  # noqa: E501

        :param currency: The currency of this ProjectPayload.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def end_date(self) -> str:
        """Gets the end_date of this ProjectPayload.  # noqa: E501

        End date of a project timeframe  # noqa: E501

        :return: The end_date of this ProjectPayload.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: str):
        """Sets the end_date of this ProjectPayload.

        End date of a project timeframe  # noqa: E501

        :param end_date: The end_date of this ProjectPayload.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def estimated_hours(self) -> int:
        """Gets the estimated_hours of this ProjectPayload.  # noqa: E501

        Estimated hours, optional, premium feature  # noqa: E501

        :return: The estimated_hours of this ProjectPayload.  # noqa: E501
        :rtype: int
        """
        return self._estimated_hours

    @estimated_hours.setter
    def estimated_hours(self, estimated_hours: int):
        """Sets the estimated_hours of this ProjectPayload.

        Estimated hours, optional, premium feature  # noqa: E501

        :param estimated_hours: The estimated_hours of this ProjectPayload.  # noqa: E501
        :type: int
        """

        self._estimated_hours = estimated_hours

    @property
    def fixed_fee(self) -> float:
        """Gets the fixed_fee of this ProjectPayload.  # noqa: E501

        Project fixed fee, optional, premium feature  # noqa: E501

        :return: The fixed_fee of this ProjectPayload.  # noqa: E501
        :rtype: float
        """
        return self._fixed_fee

    @fixed_fee.setter
    def fixed_fee(self, fixed_fee: float):
        """Sets the fixed_fee of this ProjectPayload.

        Project fixed fee, optional, premium feature  # noqa: E501

        :param fixed_fee: The fixed_fee of this ProjectPayload.  # noqa: E501
        :type: float
        """

        self._fixed_fee = fixed_fee

    @property
    def is_private(self) -> bool:
        """Gets the is_private of this ProjectPayload.  # noqa: E501

        Whether the project is private or not  # noqa: E501

        :return: The is_private of this ProjectPayload.  # noqa: E501
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private: bool):
        """Sets the is_private of this ProjectPayload.

        Whether the project is private or not  # noqa: E501

        :param is_private: The is_private of this ProjectPayload.  # noqa: E501
        :type: bool
        """

        self._is_private = is_private

    @property
    def name(self) -> str:
        """Gets the name of this ProjectPayload.  # noqa: E501

        Project name  # noqa: E501

        :return: The name of this ProjectPayload.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ProjectPayload.

        Project name  # noqa: E501

        :param name: The name of this ProjectPayload.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def rate(self) -> float:
        """Gets the rate of this ProjectPayload.  # noqa: E501

        Hourly rate, optional, premium feature  # noqa: E501

        :return: The rate of this ProjectPayload.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate: float):
        """Sets the rate of this ProjectPayload.

        Hourly rate, optional, premium feature  # noqa: E501

        :param rate: The rate of this ProjectPayload.  # noqa: E501
        :type: float
        """

        self._rate = rate

    @property
    def rate_change_mode(self) -> str:
        """Gets the rate_change_mode of this ProjectPayload.  # noqa: E501

        Rate change mode, optional, premium feature. Can be \"start-today\", \"override-current\", \"override-all\"  # noqa: E501

        :return: The rate_change_mode of this ProjectPayload.  # noqa: E501
        :rtype: str
        """
        return self._rate_change_mode

    @rate_change_mode.setter
    def rate_change_mode(self, rate_change_mode: str):
        """Sets the rate_change_mode of this ProjectPayload.

        Rate change mode, optional, premium feature. Can be \"start-today\", \"override-current\", \"override-all\"  # noqa: E501

        :param rate_change_mode: The rate_change_mode of this ProjectPayload.  # noqa: E501
        :type: str
        """

        self._rate_change_mode = rate_change_mode

    @property
    def recurring(self) -> bool:
        """Gets the recurring of this ProjectPayload.  # noqa: E501

        Project is recurring, optional, premium feature  # noqa: E501

        :return: The recurring of this ProjectPayload.  # noqa: E501
        :rtype: bool
        """
        return self._recurring

    @recurring.setter
    def recurring(self, recurring: bool):
        """Sets the recurring of this ProjectPayload.

        Project is recurring, optional, premium feature  # noqa: E501

        :param recurring: The recurring of this ProjectPayload.  # noqa: E501
        :type: bool
        """

        self._recurring = recurring

    @property
    def recurring_parameters(self) -> ProjectRecurringParameters:
        """Gets the recurring_parameters of this ProjectPayload.  # noqa: E501

        Project recurring parameters, optional, premium feature  # noqa: E501

        :return: The recurring_parameters of this ProjectPayload.  # noqa: E501
        :rtype: ProjectRecurringParameters
        """
        return self._recurring_parameters

    @recurring_parameters.setter
    def recurring_parameters(self, recurring_parameters: ProjectRecurringParameters):
        """Sets the recurring_parameters of this ProjectPayload.

        Project recurring parameters, optional, premium feature  # noqa: E501

        :param recurring_parameters: The recurring_parameters of this ProjectPayload.  # noqa: E501
        :type: ProjectRecurringParameters
        """

        self._recurring_parameters = recurring_parameters

    @property
    def start_date(self) -> str:
        """Gets the start_date of this ProjectPayload.  # noqa: E501

        Start date of a project timeframe  # noqa: E501

        :return: The start_date of this ProjectPayload.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: str):
        """Sets the start_date of this ProjectPayload.

        Start date of a project timeframe  # noqa: E501

        :param start_date: The start_date of this ProjectPayload.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def template(self) -> bool:
        """Gets the template of this ProjectPayload.  # noqa: E501

        Project is template, optional, premium feature  # noqa: E501

        :return: The template of this ProjectPayload.  # noqa: E501
        :rtype: bool
        """
        return self._template

    @template.setter
    def template(self, template: bool):
        """Sets the template of this ProjectPayload.

        Project is template, optional, premium feature  # noqa: E501

        :param template: The template of this ProjectPayload.  # noqa: E501
        :type: bool
        """

        self._template = template

    @property
    def template_id(self) -> int:
        """Gets the template_id of this ProjectPayload.  # noqa: E501

        Template ID, optional  # noqa: E501

        :return: The template_id of this ProjectPayload.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id: int):
        """Sets the template_id of this ProjectPayload.

        Template ID, optional  # noqa: E501

        :param template_id: The template_id of this ProjectPayload.  # noqa: E501
        :type: int
        """

        self._template_id = template_id

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
        if issubclass(ProjectPayload, dict):
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
        if not isinstance(other, ProjectPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectPayload):
            return True

        return self.to_dict() != other.to_dict()
